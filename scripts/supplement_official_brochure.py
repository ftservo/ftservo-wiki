"""Use exact full model numbers in the official brochure for explicit motor classes."""
import json,re
from pathlib import Path
from pypdf import PdfReader
from crawl_official_servos import ROOT,CACHE
from import_official_servo_specs import DATA,block,esc,facts,table_section

PDF=CACHE/'assets/bfde943a44dd8c69816985f9.pdf'
SOURCE='https://www.feetechrc.com/Data/feetechrc/upload/file/20240706/2024%E9%A3%9E%E7%89%B9%E5%AE%A3%E4%BC%A0%E5%86%8C.pdf'
def main():
    items=json.loads(DATA.read_text(encoding='utf8').split('=',1)[1].strip().rstrip(';'));entries={};checkpoint=CACHE/'brochure-motor-report.json';report=json.loads(checkpoint.read_text(encoding='utf8')) if checkpoint.exists() else []
    for n,page in enumerate(PdfReader(PDF).pages):
        for section in re.split(r'型\s*号\s*[：:]',page.extract_text() or '')[1:]:
            models=re.findall(r'\b[A-Z]{2}\s*-\s*[A-Z0-9]+\s*-\s*C\d{3}\b',section)
            for model in models:
                model=re.sub(r'\s+','',model)
                entries.setdefault(model,[]).append({'page':n+1,'text':section})
    for item in items:
        candidates=entries.get(item['model'],[])
        # The relevant model must be in the identity portion before dimensions,
        # excluding footnotes that merely mention a related suffix.
        candidates=[r for r in candidates if item['model'] in re.sub(r'\s+','',re.split(r'尺\s*寸',r['text'])[0])]
        if len(candidates)!=1:continue
        r=candidates[0]
        if item['model'] in ['FS-90MR-C001','FT-90M0-C001','FT-90M0-C012']:
            labels={'尺寸':'Size','重量':'Weight','最高转速':'No load speed','堵转扭矩':'Peak stall torque','电机类型':'Motor','齿轮类型':'Gear type','外壳材质':'Case','转动角度':'Running degree'}
            rows=[]
            for line in r['text'].splitlines():
                pair=re.match(r'\s*([^：:]+)[：:]\s*(.*)',line)
                if pair:
                    key=re.sub(r'\s+','',pair[1]);value=re.sub(r'(?<=\d)\.\s+(?=\d)','. ',pair[2]).replace('. ','.')
                    if key in labels:rows.append([key+' '+labels[key],value])
            new,notes=facts(rows,{'tables':[rows]},item);filled=[]
            for key,value in new.items():
                if item.get(key) is None:item[key]=value;filled.append(key)
            item['parameterSource']=SOURCE;item['parameterChecked']='2026-10-02'
            for locale in ('','en/'):
                en=bool(locale);folder=ROOT/f'docs/{locale}products/models/{item["model"].lower()}'
                content=('## Specifications from the official brochure' if en else '## 官网宣传册补充参数')+'\n\n'+('[2024 FEETECH brochure]' if en else '[飞特官网 2024 宣传册]')+f'({SOURCE}) · PDF '+str(r['page'])+'\n\n'+table_section(rows,en)
                main=folder/'main.md';main.write_text(block(main.read_text(encoding='utf8'),'official-brochure',content,before='<!-- product-resources:start -->'),encoding='utf8')
                (folder/'official-specs.json').write_text(json.dumps({'model':item['model'],'source':SOURCE,'pdf_page':r['page'],'checked':'2026-10-02','table':rows,'filled_fields':filled},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        if item.get('motor'):continue
        match=re.search(r'电机类型\s*[：:]\s*([^\n]+)',r['text'])
        if not match:continue
        motor=match[1].strip();value='brushless-coreless' if '无刷空心杯' in motor else 'brushed-coreless' if '有刷空心杯' in motor else 'brushed-iron' if re.search(r'有刷.*铁[芯心]',motor) else None
        if not value:continue
        rp=CACHE/(item['model'].lower()+'.json');record=json.loads(rp.read_text(encoding='utf8')) if rp.exists() else None
        current=[row[1] for table in record['tables'] for row in table if len(row)>1 and re.search(r'\bMotor\b',row[0],re.I)] if record else []
        conflict=any((value.startswith('brushed-') and re.search(r'brushless|无刷',v,re.I)) or (value.startswith('brushless-') and re.search(r'(?<!less)\bbrushed\b|有刷',v,re.I)) for v in current)
        if conflict:report.append({'model':item['model'],'motor':motor,'page':r['page'],'status':'conflict'});continue
        item['motor']=value;item['motorSource']=SOURCE;item['motorSourcePage']=r['page']
        for locale in ('','en/'):
            en=bool(locale);folder=ROOT/f'docs/{locale}products/models/{item["model"].lower()}'
            content=('## Motor classification from the official brochure' if en else '## 官网宣传册补充电机分类')+'\n\n'
            english={'brushless-coreless':'Brushless coreless motor','brushed-coreless':'Brushed coreless motor','brushed-iron':'Brushed iron-core motor'}[value]
            content+=(f'{english}. [2024 FEETECH official brochure]({SOURCE}), PDF page {r["page"]}; matched full model `{item["model"]}`.\n' if en else f'{motor}。[飞特官网 2024 宣传册]({SOURCE})，PDF 第 {r["page"]} 页，按完整型号 `{item["model"]}` 对应。\n')
            main=folder/'main.md';main.write_text(block(main.read_text(encoding='utf8'),'official-motor',content,before='<!-- official-specs:start -->'),encoding='utf8')
            spec=folder/'official-specs.json'
            if spec.exists():
                d=json.loads(spec.read_text(encoding='utf8'));d['motor_supplement']={'source':SOURCE,'page':r['page'],'raw':motor,'filter':value};spec.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
        report.append({'model':item['model'],'motor':motor,'page':r['page'],'status':'filled'})
    DATA.write_text('window.FEETECH_SERVO_DATA = '+json.dumps(items,ensure_ascii=False,indent=2)+';\n',encoding='utf8')
    (CACHE/'brochure-motor-report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    print('Motor classes supplemented:',sum(x['status']=='filled' for x in report))
if __name__=='__main__':main()
