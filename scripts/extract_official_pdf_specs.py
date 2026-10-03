"""Extract factual engineering rows and missing drawing previews from verified PDFs."""
import json,re
from pathlib import Path
import pdfplumber
from PIL import ImageChops
from crawl_official_servos import ROOT,CACHE

def main():
    for ap in CACHE.glob('*.assets.json'):
        assets=json.loads(ap.read_text(encoding='utf8'))
        if not assets.get('pdfs'):continue
        checkpoint=CACHE/(assets['model'].lower()+'.pdf-specs.json')
        if checkpoint.exists():continue
        pdf=assets['pdfs'][0];facts=[];drawing=None
        with pdfplumber.open(ROOT/pdf['path']) as doc:
            for n,page in enumerate(doc.pages):
                # Only engineering rows; manufacturer approval/certification prose is excluded.
                for table in page.extract_tables():
                    for row in table:
                        cells=[' '.join(c.split()) for c in row if c is not None and c.strip()]
                        if len(cells)>=3 and re.fullmatch(r'[567]-\d+',cells[0]):
                            facts.append({'page':n+1,'key':cells[1],'values':cells[2:]})
                        elif len(cells)>=2 and re.search(r'Signal Period|Signal high Voltage|Signal Low Voltage',cells[0],re.I):
                            facts.append({'page':n+1,'key':cells[0],'values':cells[1:]})
                text=page.extract_text() or ''
                if not assets['drawings'] and not drawing and n>=3 and re.search(r'9\s*外观尺寸|9\s*Outside Dimension',text,re.I):
                    words=page.extract_words();anchor=[w['top'] for w in words if 'Outside' in w['text'] or '外观尺寸' in w['text']]
                    if anchor:
                        top=max(anchor)+18
                        crop=page.crop((0,top,page.width,page.height-12));im=crop.to_image(resolution=160).original.convert('RGB')
                        # Trim blank margins without deleting any dimension labels.
                        diff=ImageChops.difference(im,__import__('PIL.Image',fromlist=['Image']).new('RGB',im.size,'white'))
                        bbox=diff.point(lambda v:255 if v>50 else 0).getbbox()
                        if bbox:
                            x0,y0,x1,y1=bbox;im=im.crop((max(0,x0-12),max(0,y0-12),min(im.width,x1+12),min(im.height,y1+12)))
                            path=CACHE/'assets'/(assets['model'].lower()+'-pdf-drawing.png');im.save(path)
                            drawing={'url':pdf['url'],'path':path.relative_to(ROOT).as_posix(),'order':0,'pdf_page':n+1}
            cover=doc.pages[0].extract_text() or ''
        (CACHE/(assets['model'].lower()+'.pdf-specs.json')).write_text(json.dumps({'model':assets['model'],'pdf':pdf,'cover':cover[:1500],'facts':facts},ensure_ascii=False,indent=2),encoding='utf8')
        if drawing:
            assets['drawings']=[drawing];ap.write_text(json.dumps(assets,ensure_ascii=False,indent=2),encoding='utf8');print('PDF drawing',assets['model'],drawing['pdf_page'],flush=True)
    print('PDF extraction complete',flush=True)
if __name__=='__main__':main()
