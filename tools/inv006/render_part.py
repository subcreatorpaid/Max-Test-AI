# INV-006 part worker: python3 render_part.py <PART> <vo_dir> <out_dir> [clipdir ...]
# Renders one part (shots -> crossfaded part video, silent, final grade). Footage ~50% of screen time.
import sys, os, json, glob, subprocess, runpy, pathlib, math, re, hashlib
from multiprocessing import Pool
HERE=pathlib.Path(__file__).parent; sys.path.insert(0,str(HERE))
import anim6 as A6, spec6
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance
PART, VOD, OUT = sys.argv[1], pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3]); OUT.mkdir(parents=True, exist_ok=True)
CLIPDIRS=[pathlib.Path(p) for p in sys.argv[4:]]
FPS=25; PW,PH=A6.PW,A6.PH; XF=0.5  # crossfade seconds
R=runpy.run_path(str(HERE/"script_v4.py"))["R"]; ROW={r[0]:r for r in R}
SG=json.load(open(VOD/"segs6.json"))["segs"][PART]
TMP=OUT/f"tmp-{PART}"; TMP.mkdir(exist_ok=True)
# ---------- footage library ----------
FOOT_FULL={"CO-01":"still","P2-11b":"still","P2-02":"P2-02","P2-05":"P2-05","P3-02":"P3-02","P3-06":"P3-06","P3-11b":"P3-11b","P5-02":"P5-02","P5-04":"P5-04","P5-05":"P5-05","RC-08":"RC-08","P5-01d":"home","P4-05b":"city","P2-11f":"winter"}
THEMES=[("ship",r"ship|tanker|cargo|strait|sea\b|port|sail|auction|atlantic|hormuz"),("winter",r"winter|cold|snow|frost|january|weather|beast"),
 ("home",r"home|heating|boiler|radiator|kitchen|stove|famil|household|warm"),("gas",r"\bgas\b|plant|pipeline|storage|tank|rough|north sea|field|laffan|production|lng|liquefied"),
 ("money",r"bill|pound|price|cap\b|debt|money|pay|cost|vat|tax|wholesale|ofgem|forecast|market"),("power",r"electric|power|lights"),
 ("land",r"fertili|urea|factory|harvest|industr|farm"),("city",r"britain|london|europe|leeds|lyon|germany|tokyo|asia|america|countr")]
def clips(): 
    out={}
    for d in CLIPDIRS:
        for f in sorted(glob.glob(str(d/"*.mp4"))):
            name=os.path.basename(f); m=re.match(r"([a-z]+)\d+-pixabay",name)
            out.setdefault(m.group(1) if m else name.split("-pixabay")[0], []).append(f)
    return out
LIB=clips()
def photos():
    out={}
    for d in CLIPDIRS:
        for f in sorted(glob.glob(str(d/'*.jpg'))):
            m=re.match(r'([a-z]+)\d+\.jpg',os.path.basename(f))
            if m: out.setdefault(m.group(1),[]).append(f)
    return out
PHO=photos()
_pu={}
def pick_photo(theme):
    pool=PHO.get(theme) or [c for v in PHO.values() for c in v]
    if not pool: return None
    k=_pu.get(theme, int(hashlib.md5((PART+'p').encode()).hexdigest(),16)%len(pool)); _pu[theme]=k+1
    return pool[k%len(pool)]
SLOT=[0]
def footage(theme, code, text='', small=''):
    SLOT[0]+=1
    if SLOT[0]%5 in (1,3):
        ph=pick_photo(theme)
        if ph: return ('photo',{'img':ph,'text':text,'small':small,'dir':SLOT[0]%4})
    return ('clip',{'clip':pick(theme,code),'text':text,'small':small})
_used={}
def pick(theme, seed):
    pool=LIB.get(theme) or LIB.get("misc") or [c for v in LIB.values() for c in v]
    if not pool: return None
    k=_used.get(theme, int(hashlib.md5(PART.encode()).hexdigest(),16)%len(pool)); _used[theme]=k+1
    return pool[k%len(pool)]
def theme_for(row):
    txt=(row[1]+" "+row[3]).lower()
    for th,rx in THEMES:
        if re.search(rx, txt): return th
    return "misc"
# ---------- plan: list of (kind, code, dur, info) ----------
starts=SG["starts"]; total=SG["dur"]
plan=[]
for i,(code,st) in enumerate(starts):
    en=starts[i+1][1] if i+1<len(starts) else total
    if i==0: st=0.0
    d=en-st; row=ROW[code]; ff=FOOT_FULL.get(code)
    if ff=="still": plan.append(("gfx",code,d,{})); continue
    if ff:
        c=[x for x in LIB.get(ff,[])] if ff in LIB else []
        if c: plan.append(("clip",code,d,{"clip":c[0],"text":row[4]}))
        else:
            k_,inf=footage(ff if ff in LIB else theme_for(row), code, row[4]); plan.append((k_,code,d,inf))
        continue
    if "s_part" in row[3] or d<6.5:
        plan.append(("gfx",code,d,{})); continue
    # split: graphic first (number lands), footage second
    g=max(4.0, d*0.5); plan.append(("gfx",code,g,{})); k_,inf=footage(theme_for(row),code,'',row[4]); plan.append((k_,code,d-g,inf))
# frame-exact durations
acc=0.0; fr=[]
for k,p in enumerate(plan):
    a=round(acc*FPS); acc+=p[2]; b=round(acc*FPS); fr.append(b-a)
def gfx_frame(code,t,dur):
    row=ROW[code]; A6.T=t; A6.E=1.0
    im=spec6.SPEC[code](row[4], row[5]).convert("RGB")
    z=1.0+0.05*min(1,t/max(dur,1))
    cw,ch=PW/z,PH/z; x0=(PW-cw)/2; y0=(PH-ch)/2
    return im.resize((PW,PH),Image.BILINEAR,box=(x0,y0,x0+cw,y0+ch))
def overlay_png(code, text, small, path):
    A6.T=10; im=Image.new("RGBA",(PW,PH),(0,0,0,0))
    sh=Image.new("L",(PW,PH),0); ImageDraw.Draw(sh).rectangle([0,PH-260*1.5,PW*0.75,PH],fill=150 if (text or small) else 90); sh=sh.filter(ImageFilter.GaussianBlur(90))
    im.putalpha(sh); d=A6.D(im)
    if text:
        for i,l in enumerate(A6.wrap(d,text,A6.f(46),A6.W*0.62)[:2]): d.text((50,A6.H-200+i*56),l,font=A6.f(46),fill=A6.PAPER+(255,))
    elif small:
        d.rectangle([40,A6.H-150,46,A6.H-104],fill=A6.ORANGE+(255,)); d.text((60,A6.H-148),small[:70],font=A6.f(30),fill=A6.PAPER+(255,))
    d.text((A6.W-300,30),"ILLUSTRATIVE FOOTAGE",font=A6.f(20),fill=A6.GREY+(220,))
    tag=ROW[code][5]
    if tag: d.text((40,A6.H-46),tag.upper()[:90],font=A6.f(20,"reg"),fill=A6.GREY+(255,))
    im.save(path)
ENC=["-c:v","libx264","-crf","16","-preset","veryfast","-pix_fmt","yuv420p","-r",str(FPS)]
def render(k):
    kind,code,_,info=plan[k]; n=fr[k]+(int(XF*FPS) if k<len(plan)-1 else 0); dur=n/FPS
    out=TMP/f"{k:03d}.mp4"
    if out.exists(): return str(out)
    if kind=="clip" and info.get("clip"):
        png=TMP/f"{k:03d}.png"; overlay_png(code, info.get("text",""), info.get("small",""), png)
        vf=(f"[0:v]scale=2074:1166,crop=1920:1080:x='154*t/{dur:.3f}':y='43-20*t/{dur:.3f}',eq=saturation=0.62:contrast=1.06:brightness=-0.045:gamma=0.94,"
            f"colorbalance=bs=0.06:bm=0.03,fps={FPS},format=yuv420p[v];[1:v]format=rgba,fade=in:st=0.4:d=0.6:alpha=1[o];[v][o]overlay=0:0")
        subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y","-stream_loop","-1","-i",info["clip"],"-loop","1","-i",str(png),"-filter_complex",vf,"-frames:v",str(n),"-an"]+ENC+[str(out)],check=True)
        return str(out)
    if kind=="photo":
        png=TMP/f"{k:03d}.png"; overlay_png(code, info.get("text",""), info.get("small",""), png)
        N=n; dr=info["dir"]
        zexpr={0:f"1.0+0.10*on/{N}",1:f"1.10-0.10*on/{N}",2:"1.08",3:"1.08"}[dr]
        xexpr={0:"iw/2-(iw/zoom/2)",1:"iw/2-(iw/zoom/2)",2:f"(iw-iw/zoom)*on/{N}",3:f"(iw-iw/zoom)*(1-on/{N})"}[dr]
        vf=(f"[0:v]scale=3840:2160:force_original_aspect_ratio=increase,crop=3840:2160,unsharp=5:5:0.6,zoompan=z='{zexpr}':x='{xexpr}':y='ih/2-(ih/zoom/2)':d={N}:s=1920x1080:fps={FPS},"
            f"eq=saturation=0.62:contrast=1.06:brightness=-0.045:gamma=0.94,colorbalance=bs=0.06:bm=0.03,format=yuv420p[v];[1:v]format=rgba,fade=in:st=0.4:d=0.6:alpha=1[o];[v][o]overlay=0:0")
        subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y","-i",info["img"],"-loop","1","-i",str(png),"-filter_complex",vf,"-frames:v",str(n),"-an"]+ENC+[str(out)],check=True)
        return str(out)
    code_=code
    p=subprocess.Popen(["ffmpeg","-nostdin","-loglevel","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{PW}x{PH}","-r",str(FPS),"-i","-","-an"]+ENC+[str(out)+".t.mp4"],stdin=subprocess.PIPE)
    for j in range(n): p.stdin.write(gfx_frame(code_, j/FPS, dur).tobytes())
    p.stdin.close(); p.wait(); os.rename(str(out)+".t.mp4",out); return str(out)
if __name__=="__main__":
    with Pool(int(os.environ.get("WORKERS","4"))) as pool: segs=list(pool.imap(render, range(len(plan))))
    # crossfade chain
    TR=["fade","dissolve","fade","smoothleft","fade","dissolve","fade","smoothright"]
    inputs=[]; [inputs.extend(["-i",s]) for s in segs]
    fc=[]; last="[0:v]"; off=0.0
    for k in range(1,len(segs)):
        off+=fr[k-1]/FPS
        nxt=ROW[plan[k][1]]; tr="fadeblack" if "s_part" in nxt[3] and plan[k][0]=="gfx" and plan[k][1]!=plan[k-1][1] else TR[k%len(TR)]
        lab=f"[x{k}]"; fc.append(f"{last}[{k}:v]xfade=transition={tr}:duration={XF}:offset={off:.3f}{lab}"); last=lab
    fc.append(f"{last}noise=alls=7:allf=t,vignette=PI/5,format=yuv420p[vout]")
    final=OUT/f"{PART}.mp4"
    subprocess.run(["ffmpeg","-nostdin","-loglevel","error","-y"]+inputs+["-filter_complex",";".join(fc),"-map","[vout]","-frames:v",str(sum(fr)),
        "-c:v","libx264","-crf","23","-maxrate","12M","-bufsize","24M","-preset","medium","-g","50","-pix_fmt","yuv420p","-r",str(FPS),str(final)],check=True)
    # shot log for the sound mix
    t=0.0; log=[]
    for k,p in enumerate(plan):
        log.append({"code":p[1],"kind":p[0],"t":round(t,3),"dur":round(fr[k]/FPS,3),"visual":ROW[p[1]][3][:60],"sfx":ROW[p[1]][6]}); t+=fr[k]/FPS
    json.dump({"part":PART,"dur":sum(fr)/FPS,"vo_dur":total,"shots":log}, open(OUT/f"{PART}-shots.json","w"), indent=1)
    gt=sum(fr[k] for k,p in enumerate(plan) if p[0]=="gfx"); pt=sum(fr[k] for k,p in enumerate(plan) if p[0]=="photo"); print(PART,"done", f"{sum(fr)/FPS:.1f}s", f"graphics {100*gt/sum(fr):.0f}% video {100*(sum(fr)-gt-pt)/sum(fr):.0f}% photos {100*pt/sum(fr):.0f}%")
