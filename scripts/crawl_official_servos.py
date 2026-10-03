"""Checkpointed read-only crawl of public FEETECH product pages and attachments."""
from pathlib import Path
import hashlib, json, re, time, urllib.request, urllib.parse
from lxml import html
from concurrent.futures import ThreadPoolExecutor

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'imports/official-feetech-2026-10-02'
CACHE.mkdir(exist_ok=True)
ALLOWED={'www.feetechrc.com','www.feetech.cn','feetechrc.com','feetech.cn'}

def fetch(url):
    parsed=urllib.parse.urlsplit(url)
    if parsed.hostname not in ALLOWED: raise ValueError('Non-official host: '+url)
    safe=urllib.parse.urlunsplit((parsed.scheme,parsed.netloc,urllib.parse.quote(parsed.path,safe='/%:@'),urllib.parse.quote(parsed.query,safe='=&%'),''))
    path=CACHE/(hashlib.sha256(url.encode()).hexdigest()[:20]+'.html')
    if path.exists(): return path.read_bytes()
    for attempt in range(3):
        try:
            req=urllib.request.Request(safe,headers={'User-Agent':'FEETECH-Wiki-Documentation-Sync/1.0'})
            with urllib.request.urlopen(req,timeout=30) as response:
                content=response.read()
            if len(content)<1000: raise ValueError('Empty response')
            path.write_bytes(content);time.sleep(.15);return content
        except Exception:
            if attempt==2: raise
            time.sleep(1+attempt)

def text(node): return ' '.join(node.itertext()).strip()
def parse_catalog(url):
    tree=html.fromstring(fetch(url).decode('utf-8'))
    rows=[]
    for li in tree.xpath('//div[contains(concat(" ",normalize-space(@class)," ")," product ")]/ul/li'):
        pre=li.xpath('.//pre')
        if not pre: continue
        spec='\n'.join(pre[0].itertext())
        links=li.xpath('.//a[@href]/@href')
        if not links: continue
        model=re.search(r'(?:Product Model No|产品型号)\s*[：:]\s*([^\r\n]+)',spec,re.I)
        if model:
            rows.append({'label':model[1].strip(),'url':urllib.parse.urljoin(url,links[0]),'summary':spec})
    paging={urllib.parse.urljoin(url,h) for h in tree.xpath('//a[@href]/@href') if re.search(r'/products-page-\d+(?:\?.*)?$',h)}
    return rows,paging

def index():
    queue={'https://www.feetechrc.com/products','https://www.feetech.cn/products'};done=set();rows=[]
    while queue:
        batch=sorted(queue-done)
        if not batch:break
        queue=set()
        with ThreadPoolExecutor(max_workers=3) as pool:
            for url,(products,paging) in zip(batch,pool.map(parse_catalog,batch)):
                done.add(url);rows.extend(products);queue.update(paging-done)
                print('Catalog',url,len(products),flush=True)
        (CACHE/'catalog.json').write_text(json.dumps({'pages':sorted(done),'products':rows},ensure_ascii=False,indent=2),encoding='utf-8')
    return list({(r['label'],r['url']):r for r in rows}.values())

def parse_product(url):
    content=fetch(url);tree=html.fromstring(content.decode('utf-8'))
    tables=[]
    for table in tree.xpath('//table'):
        rows=[]
        for tr in table.xpath('.//tr'):
            cells=[' '.join(text(c).split()) for c in tr.xpath('./td|./th')]
            if cells: rows.append(cells)
        if rows: tables.append(rows)
    pdfs=[]
    for a in tree.xpath('//a[@href]'):
        href=urllib.parse.urljoin(url,a.get('href'))
        if re.search(r'\.(?:pdf|zip|rar|step|stp|dxf|dwg)(?:\?|$)',href,re.I):
            entry={'url':href,'title':a.get('title') or text(a)}
            if entry not in pdfs:pdfs.append(entry)
    images=[]
    for a in tree.xpath('//a[@data-at-1920]'):
        href=urllib.parse.urljoin(url,a.get('data-at-1920'))
        if href not in images:images.append(href)
    drawings=list(dict.fromkeys(urllib.parse.urljoin(url,src) for src in tree.xpath('//*[@id="tab2"]//img[contains(@src,"/upload/image/")]/@src')))
    return {'url':url,'tables':tables,'attachments':pdfs,'images':images,'drawings':drawings,'text':'\n'.join(line.strip() for line in tree.xpath('//body')[0].itertext() if line.strip())}

def main():
    rows=index();items=json.loads((ROOT/'docs/javascripts/servo-selector-data.js').read_text(encoding='utf-8').split('=',1)[1].strip().rstrip(';'))
    matched={};unmatched=[]
    for item in items:
        model=item['model'];found=[r for r in rows if r['label'].upper()==model]
        english=[r for r in found if urllib.parse.urlsplit(r['url']).hostname=='www.feetechrc.com']
        if english:found=english
        if not found:
            # Existing source URL belongs to the exact model from the supplied package.
            source=item.get('source')
            if source:
                u=source.replace('www.feetech.cn/en/','www.feetechrc.com/').replace('www.feetech.cn/','www.feetechrc.com/')
                found=[{'label':model,'url':u,'summary':''}]
        if not found:
            alias=item.get('coverModel','').upper()
            candidates=[r for r in rows if r['label'].upper()==alias]
            english=[r for r in candidates if urllib.parse.urlsplit(r['url']).hostname=='www.feetechrc.com']
            if english:candidates=english
            # Only unique exact aliases, and never use one alias for two suffixes.
            if alias and len(candidates)==1 and sum(i.get('coverModel','').upper()==alias for i in items)==1:
                found=candidates
        urls=list(dict.fromkeys(r['url'] for r in found))
        if len(urls)==1:matched[model]={'catalog':found[0],'url':urls[0]}
        else:unmatched.append(model)
    # Search the site's own product-search form for older, unlisted models.
    def search_item(item):
        hits=[]
        for term in dict.fromkeys([item['model'],item.get('coverModel',item['model'])]):
            url='https://www.feetechrc.com/products.html?keyword='+urllib.parse.quote(term)
            try:
                products,_=parse_catalog(url)
                hits.extend(r for r in products if r['label'].upper() in {item['model'],item.get('coverModel','').upper()})
            except Exception as exc:print('Search error',term,str(exc),flush=True)
        urls=list(dict.fromkeys(r['url'] for r in hits))
        return item['model'],hits[0] if len(urls)==1 else None
    with ThreadPoolExecutor(max_workers=3) as pool:
        for model,hit in pool.map(search_item,[i for i in items if i['model'] in unmatched]):
            if hit:matched[model]={'catalog':hit,'url':hit['url']};unmatched.remove(model)
    (CACHE/'mapping.json').write_text(json.dumps({'matched':matched,'unmatched':unmatched},ensure_ascii=False,indent=2),encoding='utf-8')
    print('Matched',len(matched),'unmatched',len(unmatched),flush=True)
    def worker(pair):
        model,entry=pair
        try:
            record=parse_product(entry['url']);record['model']=model;record['catalog']=entry['catalog']
            (CACHE/(model.lower()+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2),encoding='utf-8')
            return model,len(record['attachments']),len(record['images']),None
        except Exception as exc:return model,0,0,str(exc)
    with ThreadPoolExecutor(max_workers=3) as pool:
        results=list(pool.map(worker,matched.items()))
        for result in results:print(result,flush=True)
    (CACHE/'crawl-report.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')

if __name__=='__main__':main()
