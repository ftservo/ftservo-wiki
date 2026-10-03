"""Import supplied model packages, preserving source files in an offline archive.

Images are deterministically cropped to a square with 80% subject coverage.
The source folder is never deleted by this script; review and validate first.
"""
from pathlib import Path
import hashlib
import json
import math
import re
import shutil
import zipfile
import io
from html import escape
from PIL import Image, ImageChops, ImageDraw, ImageFilter
import product_package as package

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'models_buffer'
DATA = ROOT / 'docs/javascripts/servo-selector-data.js'
OUT = ROOT / 'imports/models-buffer-2026-10-02'
KEYS = dict(zip(
    ['输入电压','堵转扭矩','额定扭矩','空载速度','行程 / 旋转','控制接口','产品系列','产品型号','资料版本','外形尺寸','重量','齿轮','电机','外壳','操作角度','中位脉宽','死区','旋转方向','机内限位','输出轴','静态电流','空载电流','防护等级','工作温度','存储温度','通信协议','位置反馈','结构'],
    ['Input voltage','Stall torque','Rated torque','No-load speed','Travel / rotation','Control interface','Family','Label model','Document revision','Dimensions','Weight','Gears','Motor','Case','Position control range','Neutral pulse width','Deadband','Rotation direction','Mechanical stop','Output shaft','Idle current','No-load current','Ingress protection','Operating temperature','Storage temperature','Communication','Position feedback','Shaft structure']))

def translate(value):
    for zh,en in [('轴承与出力轴','Bearings and output shaft'),('滚珠轴承','Ball bearings'),('出力轴','output shaft'),('线长','cable length'),('铝中壳','aluminum middle case'),('塑胶壳','plastic case'),('齿轮','gears'),('半双工异步串行','half-duplex asynchronous serial'),('物理层','physical layer'),('个 ID 可选','selectable IDs'),('双轴输出','Dual-shaft output'),('单轴输出','Single-shaft output'),('协议位置值','protocol position value'),('协议','protocol'),('12 位','12-bit')]:
        value=value.replace(zh,en)
    for zh, en in [('官方页面抓取日期','Official page captured'),('连续旋转','Continuous rotation'),('调速','speed control'),('位置值','position value'),('磁编码','magnetic encoder'),('无刷电机','Brushless motor'),('空心杯电机','Coreless motor'),('铁芯电机','Iron-core motor'),('钢齿轮','Steel gears'),('铜齿轮','Copper gears'),('金属齿轮','Metal gears'),('塑胶','plastic'),('铝壳','aluminum case'),('铝合金','Aluminum alloy'),('钛齿','Titanium gears'),('减速比','gear ratio'),('官方参数表未标注','Not stated in the source table'),('碳刷电机','Carbon-brush motor'),('官方标注','source label'),('CAN 总线','CAN bus'),('逆时针','Counterclockwise'),('无','None'),('单圈','Single-turn'),('范围内的','within'),('行程','travel')]:
        value = value.replace(zh, en)
    for zh,en in [('铜gears','Copper gears'),('钢gears','Steel gears'),('金属gears','Metal gears')]:
        value=value.replace(zh,en)
    return value

def specs(text):
    section = text.split('## 关键参数',1)[1].split('\n## ',1)[0]
    return {k.strip():v.strip().replace('**','').replace('`','') for k,v in re.findall(r'^\| ([^|]+) \| ([^|]+) \|$',section,re.M) if k != '项目'}

def number(value):
    found = re.search(r'\d+(?:\.\d+)?', value or '')
    return float(found[0]) if found else None

def group(model):
    prefix = model.split('-')[0].lower()
    return prefix if prefix in ['hd','hl','sc','sm','st','fu'] else 'pwm'

def crop(source, target):
    image = Image.open(source).convert('RGB')
    # Ignore near-white JPEG noise, while retaining cables, ears and shafts.
    diff = ImageChops.difference(image, Image.new('RGB',image.size,'white'))
    mask = diff.convert('L').point(lambda v: 255 if v > 35 else 0)
    # Some supplied JPEGs have a one-pixel gray frame; discard that frame.
    ImageDraw.Draw(mask).rectangle((0,0,image.width-1,image.height-1),outline=0,width=3)
    bbox = mask.getbbox()
    # Row/column occupancy locates the body without letting thin cables
    # determine its scale. The square retains nearby ears/shaft; leads may
    # naturally continue beyond the frame, as in standard product photography.
    pixels = mask.load()
    cols = [sum(pixels[x,y]>0 for y in range(image.height)) for x in range(image.width)]
    rows = [sum(pixels[x,y]>0 for x in range(image.width)) for y in range(image.height)]
    xs = [x for x,v in enumerate(cols) if v > max(cols)*.22]
    ys = [y for y,v in enumerate(rows) if v > max(rows)*.22]
    if not xs or not ys: raise ValueError(f'Empty product image: {source}')
    bbox = (min(xs),min(ys),max(xs)+1,max(ys)+1)
    pad = max(14,round(max(bbox[2]-bbox[0],bbox[3]-bbox[1])*.15))
    region = (max(0,bbox[0]-pad),max(0,bbox[1]-pad),min(image.width,bbox[2]+pad),min(image.height,bbox[3]+pad))
    recovered=mask.crop(region).getbbox()
    bbox=(region[0]+recovered[0],region[1]+recovered[1],region[0]+recovered[2],region[1]+recovered[3])
    subject=image.crop(bbox)
    side=math.ceil(max(subject.size)/.8)
    square=Image.new('RGB',(side,side),'white')
    square.paste(subject,((side-subject.width)//2,(side-subject.height)//2))
    square=square.resize((800,800),Image.Resampling.LANCZOS)
    for quality in (75,65,55,45):
        encoded=io.BytesIO()
        square.save(encoded,'WEBP',quality=quality,method=6)
        if encoded.tell() <= source.stat().st_size: break
    target.write_bytes(encoded.getvalue())
    return list(bbox)

def english_main(model, manifest, values, raw):
    rows = '\n'.join(f'| {KEYS.get(k,translate(k))} | {translate(v)} |' for k,v in values.items())
    warnings = re.findall(r'!!! warning "([^\"]+)"\n((?:    .+\n?)+)',raw)
    notes = ''
    if warnings:
        descriptions={
            'ft-325b-c001':'The source table states 325 kg·cm@12V, but the supply range is 16–25 V. Confirm the torque test voltage with FEETECH.',
            'ft-150b-c002':'The source title states 12V / 150 kg·cm; its parameter table states 220 kg·cm@14.8V. Confirm the conflicting torque values with FEETECH.',
            'ft-9020-c001':'The title states 7.4V / 20 kg·cm, the table states 5.5–9V / 24.3 kg·cm@8.4V, and the introduction states 8 kg·cm. Confirm these inconsistent values.',
            'sm-1000-c001':'The source lists SM-1000-C001 and SM-1500-C001 with the same dimensions, weight and product image, but different torque ratings (120 / 180 kg·cm). The image follows the exact model source.',
            'sm-1500-c001':'The source lists SM-1000-C001 and SM-1500-C001 with the same dimensions, weight and product image, but different torque ratings (120 / 180 kg·cm). The image follows the exact model source.'}
        if 'Modbus' in raw:
            notes='\n!!! warning "Modbus-RTU model"\n    This exact model uses Modbus-RTU over RS-485. Obtain its own register table; SMS_STS addresses, units and control modes do not apply.\n'
        else:
            notes='\n!!! warning "Source inconsistencies"\n    '+descriptions.get(model,'The supplied source records conflicting values. Confirm them with FEETECH before integration.')+'\n'
    sources = '\n'.join(f'- [FEETECH model source]({s["url"]})' for s in manifest['sources'] if s.get('url'))
    return f'''# {model.upper()}

![{model.upper()}](images/main.webp){{ .ft-model-main-image }}

Specifications transcribed from the supplied documentation for this exact model and suffix.

[Back to catalog](../../datasheets/{group(model)}.md){{ .md-button }}

{package.route_section(True)}## Key specifications

| Parameter | Specification |
| --- | --- |
{rows}
{notes}
{sources}

!!! info "Selection note"
    Stall torque is a short-duration limit, not continuous operating torque. Confirm power, shared ground, interface and mechanical clearance before enabling torque.

{package.resource_section(manifest,True)}

{package.support_section(True)}'''

def english_software(manifest, raw):
    text=package.software_page(manifest,True)
    if 'Modbus' not in raw: return text
    start=text.index('## Choose the application layer')
    end=text.index('## Read first, then move',start)
    return text[:start]+'''## Select the matching protocol

This exact model uses **Modbus-RTU over RS-485**. Obtain the register table for this model and firmware. The SMS_STS packet layout, addresses, units and control modes do not apply. Use a Modbus-RTU client and read only documented registers before configuring movement. See the [Modbus-RTU guide](../../../reference/protocol/modbus.md).

'''+text[end:]

def main():
    folders = sorted(p for p in SOURCE.iterdir() if p.is_dir())
    items = json.loads(DATA.read_text(encoding='utf-8').split('=',1)[1].strip().rstrip(';'))
    by_id = {item['model'].lower():item for item in items}
    OUT.parent.mkdir(exist_ok=True)
    archive = OUT.with_suffix('.zip')
    if archive.exists():
        raise ValueError('Source archive exists; inspect it before repeating this import.')
    with zipfile.ZipFile(archive,'x',zipfile.ZIP_DEFLATED) as z:
        for path in sorted(SOURCE.rglob('*')):
            if path.is_file(): z.write(path,path.relative_to(SOURCE).as_posix())
    report = {'archive':str(archive.relative_to(ROOT)), 'models':[], 'newModels':[], 'review':[]}
    for folder in folders:
        model = folder.name
        manifest = json.loads((folder/'manifest.json').read_text(encoding='utf-8'))
        assert manifest['model_id'] == model
        raw = (folder/'main.md').read_text(encoding='utf-8')
        values = specs(raw)
        new = model not in by_id
        if new:
            report['newModels'].append(model)
            item = {'model':model.upper(),'family':manifest['family'],'interface':manifest['interface'],'sourceGroup':group(model).upper()+'系列','coverModel':manifest['model_name'],'revision':manifest['document_revision'],'description':'','detail':f'models/{model}/main/'}
            items.append(item); by_id[model] = item
        item = by_id[model]
        previous_voltage = item.get('voltage')
        item['image'] = f'models/{model}/images/main.webp'
        # Only update exact fields provided by this model's supplied table.
        for key, label in [('voltage','输入电压'),('torque','堵转扭矩')]:
            value = values.get(label)
            if not value: continue
            item[key+'Label'] = value
            item[key] = number(value.split('@')[-1]) if key=='voltage' and '@' in value else number(value)
            if key=='voltage':
                voltages = re.findall(r'\d+(?:\.\d+)?',value)
                if len(voltages)==2:
                    item['voltageMin'],item['voltageMax'] = map(float,voltages)
                    if not new: item['voltage'] = previous_voltage or item['voltageMax']
                    else: item['voltage'] = item['voltageMax']
                voltage_test = re.search(r'@(\d+(?:\.\d+)?)\s*V', values.get('堵转扭矩',''))
                if voltage_test: item['voltage'] = float(voltage_test[1])
        speed = values.get('空载速度','')
        if speed:
            item['speedLabel'] = translate(speed)
            if 'RPM/60' in speed:
                report['review'].append({'model':model,'field':'speed','source':speed,'reason':'Ambiguous RPM/60° unit; excluded from numerical filtering'})
            else:
                rpm = re.search(r'(\d+(?:\.\d+)?)\s*RPM',speed,re.I)
                seconds = re.search(r'(\d+(?:\.\d+)?)\s*s/60',speed)
                if rpm: item['speed']=float(rpm[1])
                elif seconds and float(seconds[1])>0: item['speed']=round(10/float(seconds[1]),2)
                test = re.search(r'@(\d+(?:\.\d+)?)\s*V',speed)
                if test: item['speedVoltage']=float(test[1])
                if item.get('speed') is not None:
                    item['speedSourceLabel']=speed
                    item['speedLabel']=f'{item["speed"]:g} rpm'+(f'@{item["speedVoltage"]:g} V' if item.get('speedVoltage') else '')
        angle = values.get('行程 / 旋转',values.get('操作角度',''))
        if '连续旋转' in angle: item['continuous']=True
        elif number(angle) is not None: item['positionRange']=number(angle)
        structure=values.get('结构','')
        if '双轴' in structure: item['shaft']='dual'
        elif '单轴' in structure: item['shaft']='single'
        dimensions = re.findall(r'\d+(?:\.\d+)?',values.get('外形尺寸',''))
        if len(dimensions)==3: item['dimensions']=list(map(float,dimensions))
        weight = values.get('重量','')
        if number(weight) is not None:
            item['weight']=number(weight)
            tolerance=re.search(r'±\s*(\d+(?:\.\d+)?)',weight)
            if tolerance: item['weightTolerance']=float(tolerance[1])
        gear=values.get('齿轮','')
        for word, enum in [('钢','steel'),('铜','copper'),('钛','titanium'),('塑','plastic'),('POM','plastic')]:
            if word in gear: item['gear']=enum; break
        case=values.get('外壳','')
        if '铝合金' in case or '铝壳' in gear or '金属壳' in gear: item['case']='metal'
        elif '塑胶壳' in gear: item['case']='plastic'
        motor=values.get('电机','')
        # "Brushless" alone does not establish a coreless rotor construction.
        if motor:
            item['motorNote']=motor; item['motorNoteEn']=translate(motor)
            if '有刷' in motor and '铁芯' in motor: item['motor']='brushed-iron'
            else: item['motor']=None
        source = next((x for x in manifest['sources'] if x.get('url')),None)
        if source:
            item['source']=source['url'];item['sourceChecked']=source.get('captured','2026-10-02')
        for locale in ['','en/']:
            target=ROOT/f'docs/{locale}products/models/{model}'
            target.mkdir(parents=True,exist_ok=True); (target/'images').mkdir(exist_ok=True)
            if not locale: bbox=crop(folder/'product-image.jpg',target/'images/main.webp')
            if locale: shutil.copy2(ROOT/f'docs/products/models/{model}/images/main.webp',target/'images/main.webp')
            if not (target/'main.md').exists():
                text=english_main(model,manifest,values,raw) if locale else raw.replace('product-image.jpg','images/main.webp').replace('.ft-model-hero','.ft-model-main-image')
                (target/'main.md').write_text(text,encoding='utf-8')
            else:
                page=target/'main.md';text=page.read_text(encoding='utf-8')
                text=re.sub(r'^!\[[^\]]*\]\([^\n]+\)[^\n]*\n?', '',text, count=1,flags=re.M)
                text=text.replace('\n',f'\n\n![{model.upper()}](images/main.webp){{ .ft-model-main-image }}\n',1)
                page.write_text(text,encoding='utf-8')
            for name, generator in [('software.md',package.software_page),('mechanical.md',package.mechanical_page)]:
                if not (target/name).exists():
                    content=(english_software(manifest,raw) if name=='software.md' else generator(manifest,True)) if locale else (folder/name).read_text(encoding='utf-8')
                    (target/name).write_text(content,encoding='utf-8')
            if not (target/'manifest.json').exists(): shutil.copy2(folder/'manifest.json',target/'manifest.json')
            for extra in folder.rglob('*'):
                if extra.is_file() and extra.name not in ['main.md','mechanical.md','software.md','manifest.json','product-image.jpg','.gitkeep']:
                    dest=target/extra.relative_to(folder)
                    if not dest.exists(): dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(extra,dest)
        report['models'].append({'model':model,'crop':bbox,'sourceBytes':(folder/'product-image.jpg').stat().st_size,'webpBytes':(ROOT/f'docs/products/models/{model}/images/main.webp').stat().st_size,'sourceSha256':hashlib.sha256((folder/'product-image.jpg').read_bytes()).hexdigest()})
    items.sort(key=lambda item:item['model'])
    DATA.write_text('window.FEETECH_SERVO_DATA='+json.dumps(items,ensure_ascii=False,indent=2)+';\n',encoding='utf-8')
    # Generate all catalogs from the same model data, including new CAN series.
    for locale in ['','en/']:
        for name in ['hd','hl','pwm','sc','sm','st','fu']:
            rows=[i for i in items if group(i['model'])==name]
            title=f'{name.upper()} series specifications' if locale else f'{name.upper()} 系列规格'
            intro=f'{len(rows)} models. Compare primary specifications and open each model for integration details.' if locale else f'本目录提供 {len(rows)} 款舵机。比较主要参数，并进入型号页查看完整资料。'
            text=f'# {title}\n\n{intro}\n\n[Product selector](../index.md)\n\n<div class="servo-catalog-grid">\n'
            for item in rows:
                path=escape('../../'+item['image']); link=escape('../../'+item['detail']);model=escape(item['model'])
                metrics=''
                for key,zh,en in [('voltage','输入电压','Input voltage'),('torque','堵转扭矩','Stall torque'),('speed','空载速度','No-load speed')]:
                    value=item.get(key+'Label') or ('Not provided' if locale else '待补充')
                    metrics+=f'<div><dt>{en if locale else zh}</dt><dd>{escape(value)}</dd></div>'
                text+=f'<article class="ft-selector-card servo-catalog-card">\n<figure class="ft-product-image"><img src="{path}" alt="{model}" width="800" height="800" loading="lazy"></figure>\n<div class="ft-selector-card-top"><h3><a href="{link}">{model}</a></h3><div class="ft-selector-badges"><span>{escape(item["family"])}</span><span>{escape(item["interface"])}</span></div></div>\n<dl class="ft-selector-metrics">{metrics}</dl><div class="ft-selector-actions"><a class="ft-selector-detail" href="{link}">{"Model page" if locale else "查看型号页"}</a></div>\n</article>\n'
            (ROOT/f'docs/{locale}products/datasheets/{name}.md').write_text(text+'</div>\n',encoding='utf-8')
        index=ROOT/f'docs/{locale}products/datasheets/index.md';text=index.read_text(encoding='utf-8')
        for name in ['hd','hl','pwm','sc','sm','st']:
            text=re.sub(r'(\| '+name.upper()+r' \| )\d+',lambda m:m[1]+str(sum(group(i['model'])==name for i in items)),text)
        text=text.replace('\n!!! info',('\n| FU | 1 | CAN / UAVCAN | Robot joints | [View products](./fu.md) |\n' if locale else '\n| FU | 1 | CAN / UAVCAN 总线 | 机器人关节 | [查看产品](./fu.md) |\n')+'\n!!! info',1)
        index.write_text(text,encoding='utf-8')
    OUT.with_suffix('.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    # Contact sheet for visual review before deleting the source folder.
    sheet=Image.new('RGB',(1200,math.ceil(len(folders)/8)*165),'#eee')
    draw=ImageDraw.Draw(sheet)
    for idx,f in enumerate(folders):
        image=Image.open(ROOT/f'docs/products/models/{f.name}/images/main.webp').resize((145,145))
        x=(idx%8)*150;y=(idx//8)*165;sheet.paste(image,(x,y));draw.text((x+3,y+146),f.name,fill='black')
    sheet.save(OUT.with_suffix('.jpg'))
    print(f'Imported {len(folders)} images, {len(report["newModels"])} new models; review {len(report["review"])} ambiguous values.')

if __name__=='__main__': main()
