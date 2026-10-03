"""Download official, model-bound assets into a resumable audit cache."""
from pathlib import Path
import hashlib,json,re,time,urllib.request,urllib.parse
from concurrent.futures import ThreadPoolExecutor
from pypdf import PdfReader
from PIL import Image
from crawl_official_servos import ROOT,CACHE,ALLOWED

def compact(s):return re.sub('[^A-Z0-9]','',s.upper())
def download(url):
    parsed=urllib.parse.urlsplit(url)
    if parsed.hostname not in ALLOWED:raise ValueError('Non-official host')
    suffix=Path(parsed.path).suffix.lower()
    folder=CACHE/'assets';folder.mkdir(exist_ok=True)
    path=folder/(hashlib.sha256(url.encode()).hexdigest()[:24]+suffix)
    if not path.exists():
        safe=urllib.parse.urlunsplit((parsed.scheme,parsed.netloc,urllib.parse.quote(parsed.path,safe='/%:@'),parsed.query,''))
        for attempt in range(3):
            try:
                with urllib.request.urlopen(urllib.request.Request(safe,headers={'User-Agent':'FEETECH-Wiki-Documentation-Sync/1.0'}),timeout=35) as response:blob=response.read()
                if len(blob)<100:raise ValueError('Empty asset')
                path.write_bytes(blob);break
            except Exception:
                if attempt==2:raise
                time.sleep(1+attempt)
    return path

def main():
    items=json.loads((ROOT/'docs/javascripts/servo-selector-data.js').read_text(encoding='utf8').split('=',1)[1].strip().rstrip(';'))
    def worker(item):
        recordpath=CACHE/(item['model'].lower()+'.json')
        if not recordpath.exists():return None
        r=json.loads(recordpath.read_text(encoding='utf8'))
        checkpoint=CACHE/(item['model'].lower()+'.assets.json')
        if checkpoint.exists():
            cached=json.loads(checkpoint.read_text(encoding='utf8'))
            if cached['url']==r['url']:return cached
        ids={compact(item['model']),compact(item.get('coverModel',item['model']))}
        models=[cells[1] for table in r['tables'] for cells in table if len(cells)>1 and re.search(r'型\s*号|\bModel\s*[:：]',cells[0],re.I)]
        valid=any(compact(m) in ids for m in models)
        result={'model':item['model'],'url':r['url'],'pageModel':models,'verified':valid,'pdfs':[],'drawings':[],'skipped':[]}
        if not valid:
            result['skipped'].append('Page model does not match full model or unique catalog alias')
            checkpoint.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8');return result
        for a in r['attachments']:
            if not a['url'].lower().endswith('.pdf'):continue
            if not any(i in compact(a['title']) for i in ids):
                result['skipped'].append('Different model PDF: '+a['title']);continue
            try:
                p=download(a['url']);reader=PdfReader(p);txt='\n'.join(page.extract_text() or '' for page in reader.pages)
                if not any(i in compact(txt) for i in ids):
                    result['skipped'].append('PDF content model not verified: '+a['title']);continue
                (p.with_suffix('.txt')).write_text(txt,encoding='utf8')
                result['pdfs'].append(dict(a,path=p.relative_to(ROOT).as_posix(),pages=len(reader.pages)))
            except Exception as exc:result['skipped'].append('PDF error: '+str(exc))
        for n,url in enumerate(r.get('drawings',[])):
            try:
                p=download(url)
                with Image.open(p) as im:im.verify()
                result['drawings'].append({'url':url,'path':p.relative_to(ROOT).as_posix(),'order':n})
            except Exception as exc:result['skipped'].append('Drawing error: '+str(exc))
        (CACHE/(item['model'].lower()+'.assets.json')).write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
        print(item['model'],len(result['pdfs']),len(result['drawings']),result['skipped'],flush=True)
        return result
    with ThreadPoolExecutor(max_workers=3) as pool:results=list(pool.map(worker,items))
    (CACHE/'asset-report.json').write_text(json.dumps([r for r in results if r],ensure_ascii=False,indent=2),encoding='utf8')
if __name__=='__main__':main()
