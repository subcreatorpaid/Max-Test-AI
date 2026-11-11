"""Fetch freely licensed photos from Wikimedia Commons for a search term.
Usage: python scripts/commons_photos.py <out_dir> "<search>" [n]
Writes images + credits.md (author, licence, source URL). Only CC BY / CC BY-SA / CC0 / PD kept."""
import sys, json, urllib.request, urllib.parse, pathlib, re
out=pathlib.Path(sys.argv[1]); q=sys.argv[2]; n=int(sys.argv[3]) if len(sys.argv)>3 else 12
out.mkdir(parents=True, exist_ok=True)
UA={'User-Agent':'history-invoice-pipeline/1.0 (github actions)'}
def get(u): return urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=60).read()
api='https://commons.wikimedia.org/w/api.php?'+urllib.parse.urlencode(dict(action='query',generator='search',gsrsearch=q+' filetype:bitmap',gsrnamespace=6,gsrlimit=40,prop='imageinfo',iiprop='url|extmetadata|size',iiurlwidth=1600,format='json'))
pages=sorted(json.loads(get(api))['query']['pages'].values(),key=lambda p:p.get('index',0))
cred=['# Wikimedia Commons candidates for: '+q,'']; k=0
for p in pages:
    ii=p['imageinfo'][0]; md=ii.get('extmetadata',{})
    lic=md.get('LicenseShortName',{}).get('value','')
    if not re.search(r'CC BY|CC0|Public domain|PD',lic,re.I): continue
    if 'NC' in lic or 'ND' in lic: continue
    k+=1; fn=out/f'c{k:02d}.jpg'
    try: fn.write_bytes(get(ii.get('thumburl') or ii['url']))
    except Exception as e: k-=1; continue
    art=re.sub('<[^>]+>','',md.get('Artist',{}).get('value','unknown')).strip()
    cred.append(f"- {fn.name}: {p['title']} | {art} | {lic} | {ii.get('descriptionurl','')} | {ii['width']}x{ii['height']}")
    if k>=n: break
(out/'credits.md').write_text('\n'.join(cred)+'\n'); print(k,'images')
