"""Merge missing manufacturer facts, retaining conflicting claims and provenance."""
from pathlib import Path
import json,re,shutil,io
from PIL import Image
from crawl_official_servos import ROOT,CACHE
from product_package import resource_section
import spec_overrides

DATA=ROOT/'docs/javascripts/servo-selector-data.js'
def numbers(s):return [float(x) for x in re.findall(r'\d+(?:\.\d+)?',s)]
def esc(s):return str(s).replace('|',' / ').replace('\n',' ').replace('<','&lt;').replace('>','&gt;')
def block(text,name,content,before=None):
    begin=f'<!-- {name}:start -->';end=f'<!-- {name}:end -->';value=begin+'\n'+content.strip()+'\n'+end+'\n'
    if begin in text:return re.sub(re.escape(begin)+r'.*?'+re.escape(end),lambda m:value.rstrip(),text,flags=re.S)
    if before and before in text:return text.replace(before,value+'\n'+before,1)
    return text.rstrip()+'\n\n'+value
def get(rows,pattern):
    for row in rows:
        if len(row)>1 and re.search(pattern,row[0],re.I):return ' / '.join(row[1:])
    return ''
def png_to_webp(path):
    cached=path.with_suffix('.webp')
    if cached.exists():return cached.read_bytes()
    with Image.open(path) as source:
        im=source.convert('RGBA');background=Image.new('RGB',im.size,'white');background.paste(im,mask=im.getchannel('A'))
        background.thumbnail((1800,1800),Image.Resampling.LANCZOS)
        out=io.BytesIO();background.save(out,format='WEBP',lossless=True,method=6);cached.write_bytes(out.getvalue());return out.getvalue()

def facts(rows,record,item):
    f={};notes=[]
    voltage=get(rows,r'Operating Voltage Range|Input Voltage|工作电压范围|额定工作电压|工作电压Operating')
    vs=numbers(voltage)
    if 1<=len(vs)<=2 and all(0<v<100 for v in vs):
        f.update(voltageMin=min(vs),voltageMax=max(vs))
        f['voltage']=max(vs);f['voltageLabel']=voltage
    torque=get(rows,r'Peak stall torque|Stall Torque|堵转扭矩|堵转扭力')
    tm=re.search(r'(\d+(?:\.\d+)?)\s*kg\s*[.·]?\s*cm',torque,re.I)
    tv=re.search(r'@\s*(\d+(?:\.\d+)?)\s*V',torque,re.I)
    torque_valid=not(tv and vs and len(vs)<=2 and not min(vs)<=float(tv[1])<=max(vs))
    if tm and torque_valid:
        f['torque']=float(tm[1]);f['torqueLabel']=torque.replace('kg.cm','kg·cm')
        if tv:f['torqueVoltage']=float(tv[1]);f['voltage']=float(tv[1])
    speed=re.sub(r'(?<=\d)\.\s+(?=\d)','.',get(rows,r'No.?load speed'));m=re.search(r'(\d+(?:\.\d+)?)\s*RPM',speed,re.I)
    seconds=re.search(r'(\d+(?:\.\d+)?)\s*(?:sec|s)\s*/\s*60',speed,re.I)
    if re.search(r'RPM\s*/\s*60',speed,re.I):
        m=None;seconds=None;notes.append(['空载速度单位 RPM/60° 有歧义，暂不填写选型数值。','The no-load speed unit RPM/60° is ambiguous; no numeric filter value is added.'])
    if m or seconds:
        rpm=float(m[1]) if m else 10/float(seconds[1])
        if 0<rpm<2000:
            f['speed']=round(rpm,2);f['speedLabel']=f"{round(rpm,2):g} rpm"
            v=re.search(r'@\s*(\d+(?:\.\d+)?)\s*V',speed,re.I)
            if v:f['speedVoltage']=float(v[1]);f['speedLabel']+='@'+v[1]+'V'
    size=get(rows,r'\bSize\b');sizevalues=numbers(size)
    if len(sizevalues)==3 and all(0<v<1000 for v in sizevalues):f['dimensions']=sizevalues
    weight=get(rows,r'\bWeight\b');wm=re.match(r'\s*(\d+(?:\.\d+)?)',weight)
    if wm:
        f['weight']=float(wm[1]);tol=re.search(r'±\s*(\d+(?:\.\d+)?)',weight)
        if tol:f['weightTolerance']=float(tol[1])
    angle=get(rows,r'Running degree|Operating Travel')
    if re.search(r'continuous|连续',angle,re.I):f['continuous']=True
    else:
        am=re.match(r'\s*(\d+(?:\.\d+)?)\s*(?:±\s*\d+)?\s*(?:°|deg)',angle,re.I)
        if am and 0<float(am[1])<=360:f['positionRange']=float(am[1])
    intro=' '.join(row[0] for row in rows if len(row)==1)
    if re.search(r'多圈连续|连续旋转|multi.turn continuous',intro,re.I):f['continuous']=True
    name=get(rows,r'Product Name')
    # 轴型以「产品名称」为准：官网简介正文存在跨型号复制的轴型笔误
    # （例：ST-3036-C001 中文简介写「双轴」，而产品名称与英文简介写单轴 / Single-axis）。
    # 名称未提及时才回退到简介；同一段文本内单轴表述优先，先判双轴会把这类型号误判成双轴。
    def shaft_of(text):
        if re.search(r'单轴|single.?shaft|single.?axis',text,re.I):return 'single'
        if re.search(r'双轴|double.?shaft|dual.?axis|dual.?shaft',text,re.I):return 'dual'
        return None
    shaft=shaft_of(name) or shaft_of(intro)
    if shaft:f['shaft']=shaft
    motor=get(rows,r'\bMotor\b');gear=get(rows,r'Gear type|Gear material');case=get(rows,r'\bCase\b')
    mixed=sum(bool(re.search(p,gear,re.I)) for p in (r'钢|\bsteel\b',r'铜|\bcopper\b|\bbrass\b',r'钛|titanium',r'塑|plastic'))>1
    if mixed:f.update(gearNote=gear,gearNoteEn=gear)
    elif re.search(r'钢|\bsteel\b',gear,re.I):f['gear']='steel'
    elif re.search(r'铜|\bcopper\b|\bbrass\b',gear,re.I):f['gear']='copper'
    elif re.search(r'钛|titanium',gear,re.I):f['gear']='titanium'
    elif re.search(r'塑|plastic',gear,re.I):f['gear']='plastic'
    elif gear:f.update(gearNote=gear,gearNoteEn=gear)
    if re.search(r'alum|铝|metal|金属',case,re.I) and re.search(r'plastic|塑',case,re.I):f['case']='hybrid'
    elif re.search(r'alum|铝|metal|金属',case,re.I):f['case']='metal'
    elif re.search(r'plastic|塑|\bPA\d*\b|fiberglass|\bPC\b',case,re.I):f['case']='plastic'
    if re.search(r'有刷|brushed',motor,re.I) and re.search(r'空心|coreless',motor,re.I):f['motor']='brushed-coreless'
    elif re.search(r'无刷|brushless',motor,re.I) and re.search(r'空心|coreless',motor,re.I):f['motor']='brushless-coreless'
    elif re.search(r'有刷|brushed',motor,re.I) and re.search(r'铁|\bcore\b',motor,re.I):f['motor']='brushed-iron'
    elif motor:f.update(motorNote=motor+'（细分类待确认）',motorNoteEn=motor+' · subtype unconfirmed')
    # Contradictory material descriptions are withheld from structured filters.
    if case and re.search(r'plastic|塑胶|塑料',intro,re.I) and f.get('case')=='metal':
        f.pop('case',None);notes.append(['外壳：官网简介与规格表不一致，待厂家确认。','Case: product introduction and specification table disagree; confirmation required.'])
    if motor and re.search(r'coreless|空心',motor,re.I) and re.search(r'铁芯|铁心|core motor',intro,re.I):
        f.pop('motor',None);f.pop('motorNote',None);f.pop('motorNoteEn',None);notes.append(['电机：官网简介与规格表不一致，待厂家确认。','Motor: product introduction and specification table disagree; confirmation required.'])
    for label,raw in [('堵转扭矩',get(rows,r'Peak stall torque|堵转扭矩')),('空载速度',speed)]:
        for v in re.findall(r'@\s*(\d+(?:\.\d+)?)\s*V',raw,re.I):
            if len(vs)<=2 and vs and not min(vs)<=float(v)<=max(vs):
                english_label='stall torque' if label=='堵转扭矩' else 'no-load speed'
                notes.append([f'{label}测试电压 {v} V 不在官网所列工作范围 {voltage} 内；保留原文，测试条件待确认。',f'Test voltage {v} V for {english_label} is outside the listed operating range {voltage}; source claim retained, conditions unconfirmed.'])
                if label=='空载速度':f.pop('speed',None);f.pop('speedLabel',None);f.pop('speedVoltage',None)
    return f,notes

def table_section(rows,en):
    # Numerical specification facts only; omit promotional prose and download labels.
    keep=[r for r in rows if len(r)>1 and not re.search(r'Download|Drawings|外形图|Product Name',r[0],re.I)]
    lines=['| Parameter | Manufacturer specification |' if en else '| 参数 | 官网规格原文（含测试条件） |','| --- | --- |']
    for r in keep:
        key=r[0]
        if en:
            english=re.search(r'[A-Za-z][A-Za-z\s/()\[\].±-]*',key)
            if english:key=english[0].strip().rstrip(':')
        lines.append('| '+esc(key)+' | '+esc(' / '.join(r[1:]))+' |')
    return '\n'.join(lines)

def main():
    items=json.loads(DATA.read_text(encoding='utf8').split('=',1)[1].strip().rstrip(';'));report=[]
    overrides=spec_overrides.load()
    for item in items:
        model=item['model'];rp=CACHE/(model.lower()+'.json');ap=CACHE/(model.lower()+'.assets.json')
        if not rp.exists() or not ap.exists():continue
        record=json.loads(rp.read_text(encoding='utf8'));assets=json.loads(ap.read_text(encoding='utf8'))
        if not assets['verified'] or assets['url']!=record['url']:continue
        rows=[row for table in record['tables'] for row in table];new,notes=facts(rows,record,item);filled=[]
        pp=CACHE/(model.lower()+'.pdf-specs.json');pdf_specs=json.loads(pp.read_text(encoding='utf8')) if pp.exists() else None
        if record.get('sourceKind')=='datasheet' and pdf_specs:
            rows+=[[r['key'],' / '.join(r['values'])] for r in pdf_specs['facts']]
            new,notes=facts(rows,record,item)
        if record.get('sourceNote'):notes.append(record['sourceNote'])
        supplementary=[]
        if pdf_specs:
            # Supplement only fields missing from the page; maintain page/PDF boundaries.
            pdfrows=[[r['key'],' / '.join(r['values'])] for r in pdf_specs['facts']]
            pdfnew,_=facts(pdfrows,record,item)
            for key,value in pdfnew.items():
                withheld=(key=='case' and any('Case:' in n[1] for n in notes)) or (key.startswith('motor') and any('Motor:' in n[1] for n in notes))
                if key not in new and not withheld:new[key]=value
            supplementary=[r for r in pdf_specs['facts'] if re.search(r'Angle Sansor|传感器|screw|螺丝|Back Lash|虚位|Centering|Travel.*deviation|Signal Period|Signal high Voltage|Signal Low Voltage',r['key'],re.I)]
            for key in ('case','gear','positionRange','voltageMin','voltageMax'):
                if key in new and key in pdfnew and new[key]!=pdfnew[key]:
                    labels={'case':'外壳材质','gear':'齿轮材质','positionRange':'位置控制范围','voltageMin':'输入电压下限','voltageMax':'输入电压上限'}
                    notes.append([f'{labels[key]}：官网表为 {new[key]}，所挂载 PDF 为 {pdfnew[key]}；新增筛选值暂缓录入，请核对版本。',f'{key}: website table gives {new[key]}, attached PDF gives {pdfnew[key]}; a new filter value is withheld pending revision confirmation.'])
                    new.pop(key,None)
            if any(n[1].startswith('voltage') for n in notes):
                compare=new.get('voltage');pdfmin=pdfnew.get('voltageMin');pdfmax=pdfnew.get('voltageMax')
                if compare is not None and pdfmin is not None and pdfmax is not None and pdfmin<=compare<=pdfmax:
                    # A shared test/comparison voltage remains usable even when
                    # the claimed allowable input endpoints differ.
                    new['voltageLabel']=f'{compare:g} V'
                else:new.pop('voltage',None);new.pop('voltageLabel',None)
        # 人工确认值优先（scripts/official_spec_overrides.json）：命中登记表则强制写回，
        # 抑制由此产生的自动冲突警告，并改用登记表里的说明文案。官方逐字规格表行不改写。
        override=overrides.get(model.upper())
        pending=spec_overrides.suppress_notes(notes,override)
        if override:
            for key,value in spec_overrides.fields(override).items():
                if value is None:new.pop(key,None)
                else:new[key]=value
            spec_overrides.force(item,override)
        notes=spec_overrides.confirmed_notes(override)+pending
        previous=ROOT/f'docs/products/models/{model.lower()}/official-specs.json'
        if previous.exists():filled=json.loads(previous.read_text(encoding='utf8')).get('filled_fields',[])
        if 'gearNote' in new and 'gear' not in new and 'gear' in filled and 'gear' not in spec_overrides.fields(override):item.pop('gear',None);filled.remove('gear')
        existing_voltage=re.search(r'@\s*(\d+(?:\.\d+)?)\s*V',item.get('torqueLabel',''),re.I)
        if item.get('torque') is not None and 'torqueVoltage' in new and (item['torque']!=new.get('torque') or (existing_voltage and float(existing_voltage[1])!=new['torqueVoltage'])):
            new.pop('torqueVoltage',None)
            if 'torqueVoltage' in filled:item.pop('torqueVoltage',None);filled.remove('torqueVoltage')
        for key,value in new.items():
            if item.get(key) is None or item.get(key) in ('','请咨询','待补充','Contact us','Not provided','Contact FEETECH'):item[key]=value;filled.append(key)
        if notes:
            if pending:item['specificationNote']='官网资料存在待确认项';item['specificationNoteEn']='Some official claims need confirmation'
            else:item['specificationNote']='官网资料差异说明';item['specificationNoteEn']='Source discrepancy note'
        item['source']=record['url'];item['parameterSource']=record['url'];item['parameterChecked']='2026-10-02'
        for locale in ('','en/'):
            en=bool(locale);folder=ROOT/f'docs/{locale}products/models/{model.lower()}'
            manifest=json.loads((folder/'manifest.json').read_text(encoding='utf8'))
            source={'type':'official_datasheet' if record.get('sourceKind')=='datasheet' else 'official_website','url':record['url'],'checked':'2026-10-02','model_on_page':assets['pageModel']}
            manifest['sources']=[s for s in manifest['sources'] if s.get('type') not in ('official_website','official_datasheet')]+[source]
            for kind,entries in [('datasheet',assets['pdfs']),('drawing',assets['drawings'][:1])]:
                if not entries:continue
                a=entries[0]
                if kind=='datasheet':
                    target=next(s for s in manifest['assets'] if s['kind']==kind)
                    revision=re.search(r'\b[A-Z]/\d+\b',pdf_specs['cover'])[0] if pdf_specs and re.search(r'\b[A-Z]/\d+\b',pdf_specs['cover']) else None
                    target.update(status='missing',path=None,revision=revision,source=a['url'],external_only=True)
                    continue
                else:relative='images/drawing.webp';blob=png_to_webp(ROOT/a['path']);item['drawing']='models/'+model.lower()+'/'+relative
                dest=folder/relative;dest.parent.mkdir(exist_ok=True);dest.write_bytes(blob)
                target=next(s for s in manifest['assets'] if s['kind']==kind)
                revision=re.search(r'\b[A-Z]/\d+\b',pdf_specs['cover'])[0] if kind=='datasheet' and pdf_specs and re.search(r'\b[A-Z]/\d+\b',pdf_specs['cover']) else None
                target.update(status='available',path=relative,revision=revision,source=a['url'])
            (folder/'manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
            content=('## Official model specifications' if en else '## 官网型号详细参数')+'\n\n'
            content+=(f'[FEETECH official product page]({record["url"]}) · Checked 2026-10-02. The complete model on the page is '+', '.join(assets['pageModel'])+'.\n\n' if en else f'[飞特官网型号页]({record["url"]}) · 核对日期：2026-10-02；页面型号：'+', '.join(assets['pageModel'])+'。\n\n')
            if notes:
                content+=(('!!! warning "Claims requiring confirmation"' if en else '!!! warning "官网资料待确认项"') if pending else ('!!! note "Source discrepancy note"' if en else '!!! note "官网资料差异说明"'))+'\n'
                content+='\n'.join('    '+n[int(en)] for n in notes)+'\n\n'
            content+=table_section(rows,en)+'\n\n'
            if supplementary:
                content+=('### Additional facts from the attached datasheet' if en else '### 规格书中的补充参数')+'\n\n'
                content+=('[Official datasheet]' if en else '[官网规格书]')+f'({pdf_specs["pdf"]["url"]})\n\n'
                content+=('| Parameter | Specification | PDF page |' if en else '| 参数 | 规格原文 | PDF 页码 |')+'\n| --- | --- | --- |\n'
                for r in supplementary:content+='| '+esc(r['key'])+' | '+esc(' / '.join(r['values']))+' | '+str(r['page'])+' |\n'
                content+='\n'
            if assets['skipped']:content+=('Attachment checks: ' if en else '附件核对（未纳入资料包）：')+esc('; '.join(assets['skipped']))+'\n\n'
            remaining=[a for a in record['attachments'] if a['url'] not in [p['url'] for p in assets['pdfs']]]
            if remaining:
                content+=('Other files linked by the manufacturer (model applicability unconfirmed):' if en else '官网其它关联附件（适用型号尚未核实）：')+'\n\n'
                for a in remaining:content+='- ['+esc(a['title'])+']('+a['url']+')\n'
                content+='\n'
            if assets['drawings']:content+=(f'![{model} mechanical drawing](images/drawing.webp){{ .ft-model-drawing }}\n\n[Open full-size drawing](images/drawing.webp)\n' if en else f'![{model} 机身尺寸图](images/drawing.webp){{ .ft-model-drawing }}\n\n[查看原尺寸图纸](images/drawing.webp)\n')
            main=folder/'main.md';text=main.read_text(encoding='utf8')
            for key,zh,english in [('voltage','输入电压','Input voltage'),('torque','堵转扭矩','Stall torque')]:
                if item.get(key) is not None:
                    pattern=r'(\| '+re.escape(english if en else zh)+r' \| )\*\*(?:请咨询|待补充|Contact us|Not provided|Contact FEETECH)\*\*'
                    text=re.sub(pattern,lambda m:m[1]+'**'+esc(item.get(key+'Label',str(item[key])))+'**',text)
            text=block(text,'official-specs',content,before='## 实测特性曲线' if not en else '## Measured characteristic curves')
            # Keep downloads before support; generated spec section precedes resources.
            if text.index('<!-- official-specs:start -->')>text.index('<!-- product-resources:start -->'):
                section=re.search(r'<!-- official-specs:start -->.*?<!-- official-specs:end -->',text,re.S)[0]
                text=text.replace(section,'').replace('<!-- product-resources:start -->',section+'\n\n<!-- product-resources:start -->',1)
            text=re.sub(r'<!-- product-resources:start -->.*?<!-- product-resources:end -->',lambda m:resource_section(manifest,en),text,flags=re.S)
            main.write_text(text.rstrip()+'\n',encoding='utf8')
            mechanical=folder/'mechanical.md';mt=mechanical.read_text(encoding='utf8')
            if assets['drawings']:
                mt=mt.replace('目前本资料包尚未收录这两类文件。','本页已收录官网尺寸图；STEP 状态见资料清单。').replace('Neither is currently supplied in this package.','The official dimensioned image is supplied below; check the resource table for STEP availability.')
                mt=mt.replace('上述接口尺寸与承载限制目前尚未收录，不借用相似型号或其他后缀的数据。','尺寸以本页官网图纸为依据，图纸未标注的配合、公差与承载限制仍需确认。').replace('These dimensions and load limits are not supplied here; do not borrow them from another model or suffix.','Refer to the supplied drawing for dimensions; unspecified fits, tolerances and load limits still require model-specific confirmation.')
                mt=block(mt,'official-drawing',('## Official dimensioned drawing' if en else '## 官网机身尺寸图')+f'\n\n![{model}](images/drawing.webp){{ .ft-model-drawing }}\n\n'+('[Full-size drawing](images/drawing.webp) · [Official source]' if en else '[查看原尺寸图纸](images/drawing.webp) · [官网来源]')+f'({record["url"]})\n',before='## 画支架前核对' if not en else '## Check before designing the bracket')
            mechanical.write_text(mt.rstrip()+'\n',encoding='utf8')
            software=folder/'software.md';st=software.read_text(encoding='utf8');control=[r for r in rows if len(r)>1 and re.search(r'Command|Protocol|ID范围|Communication|Baud|Pulse|Stop position|Neutral|Running degree|Resolution|Feedback|Operating Modes|Multi.Loop|Constant force|控制|旋转|中位|中立|运行模式|反馈|波特',r[0],re.I)]
            if control:st=block(st,'official-control',('## Model-specific control specifications' if en else '## 官网型号控制参数')+'\n\n'+('[Official source]' if en else '[官网来源]')+f'({record["url"]}) · 2026-10-02\n\n'+table_section(control,en)+'\n\n'+('Consult the exact firmware memory table for register writes; the specification table does not replace it.' if en else '寄存器写入仍需本完整型号与固件对应的内存表；此规格表不能替代内存表。'),before=re.search(r'^## .+',st,re.M)[0])
            software.write_text(st.rstrip()+'\n',encoding='utf8')
            specfile=folder/'official-specs.json';spec=json.loads(specfile.read_text(encoding='utf8')) if specfile.exists() else {}
            spec.update(model=model,checked='2026-10-02',source=record['url'],table=rows,notes=notes,filled_fields=filled)
            specfile.write_text(json.dumps(spec,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        report.append({'model':model,'filled':filled,'pdf':len(assets['pdfs']),'drawing':bool(assets['drawings']),'notes':notes,'skipped':assets['skipped']})
    DATA.write_text('window.FEETECH_SERVO_DATA = '+json.dumps(items,ensure_ascii=False,indent=2)+';\n',encoding='utf8')
    (CACHE/'import-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print('Updated',len(report),'models;',sum(bool(r['pdf']) for r in report),'PDFs;',sum(r['drawing'] for r in report),'drawings;',sum(len(r['filled']) for r in report),'fields')
if __name__=='__main__':main()
