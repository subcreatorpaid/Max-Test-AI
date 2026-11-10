#!/usr/bin/env python3
"""Fetch Pixabay VIDEO candidates for each coded shot, so Claude can pick the one that matches the narration by eye.
Key only from PIXABAY_API_KEY (GitHub Secret). Never printed or written.
Input  videos/<id>/clips.json: [{"code":"P1-05b","query":"ships anchored offshore","n":3,"min_seconds":6}, ...]
Output videos/<id>/clips/cand/<code>_<k>.jpg  (3-frame strip from the small rendition)
       videos/<id>/clips/candidates.json  ({code: [{k,id,duration,url,user,page,tags}]})
Picked clips are downloaded at render time from the saved URL (cached once, not hotlinked)."""
import json, os, sys, time, pathlib, subprocess, tempfile, urllib.parse, urllib.request
def get(url):
    req=urllib.request.Request(url, headers={"User-Agent":"history-invoice-broll/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r: return r.read()
def main(vd):
    key=os.environ.get("PIXABAY_API_KEY") or sys.exit("PIXABAY_API_KEY not set")
    vd=pathlib.Path(vd); items=json.loads((vd/"clips.json").read_text())
    out=vd/"clips"; cand=out/"cand"; cand.mkdir(parents=True, exist_ok=True)
    cj=out/"candidates.json"; res=json.loads(cj.read_text()) if cj.exists() else {}
    seen={c["id"] for v in res.values() for c in v}
    for it in items:
        code=it["code"]
        if code in res and not it.get("refresh"): continue
        p={"key":key,"q":it["query"][:100],"per_page":30,"safesearch":"true","video_type":"film"}
        try: hits=json.loads(get("https://pixabay.com/api/videos/?"+urllib.parse.urlencode(p))).get("hits",[])
        except Exception as e: print(code,"search failed",type(e).__name__); continue
        got=[]
        for h in hits:
            if len(got)>=it.get("n",3): break
            if h["id"] in seen or h.get("duration",0)<it.get("min_seconds",6): continue
            v=h["videos"]; big=next((v[s]["url"] for s in ("large","medium") if v.get(s,{}).get("url") and v[s].get("width",0)>=1280),None)
            small=next((v[s]["url"] for s in ("tiny","small","medium") if v.get(s,{}).get("url")),None)
            if not big or not small: continue
            k=len(got)+1; jpg=cand/f"{code}_{k}.jpg"
            try:
                with tempfile.NamedTemporaryFile(suffix=".mp4") as tf:
                    tf.write(get(small)); tf.flush(); d=h["duration"]
                    ins=[]; [ins.extend(["-ss",f"{d*x:.2f}","-i",tf.name]) for x in (0.15,0.5,0.85)]
                    subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y"]+ins+["-filter_complex",
                        "[0:v]scale=320:180,setsar=1[a];[1:v]scale=320:180,setsar=1[b];[2:v]scale=320:180,setsar=1[c];[a][b][c]hstack=3","-frames:v","1",str(jpg)],check=True)
            except Exception as e: print(code,k,"frame fail",type(e).__name__); continue
            seen.add(h["id"]); got.append({"k":k,"id":h["id"],"duration":h["duration"],"url":big,"user":h.get("user",""),"page":h.get("pageURL",""),"tags":h.get("tags","")})
            time.sleep(0.5)
        res[code]=got; print(code,len(got)); cj.write_text(json.dumps(res,indent=1))
    print("done")
if __name__=="__main__": main(sys.argv[1])
