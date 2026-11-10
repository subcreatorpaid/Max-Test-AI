# INV-006 animated panels. Logical canvas 1280x720, drawn natively at 1920x1080 (S=1.5).
# Module globals E (build progress 0..1, eased) and T (seconds into the shot) drive animation.
import os, re, math, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageChops
import shapefile
A = pathlib.Path(__file__).parent / "assets"
W, H, S = 1280, 720, 1.5
PW, PH = int(W*S), int(H*S)
INK=(16,15,14); PAPER=(236,228,214); ORANGE=(232,89,12); RED=(230,57,70); CYAN=(0,180,216); CRIMSON=(193,18,31); GREY=(120,114,106); LAND=(38,36,33); BORDER=(70,66,60)
E = 1.0; T = 10.0
F_INTER=str(A/"Inter-Bold.otf"); F_INTER_R=str(A/"Inter-Regular.otf")
if not os.path.exists(F_INTER_R): F_INTER_R=F_INTER
_FC={}
def f(sz, kind="inter"):
    k=(sz,kind)
    if k not in _FC:
        p={"inter":F_INTER,"reg":F_INTER_R,"serif":str(A/"CaladeaBI.ttf"),"bebas":str(A/"Bebas.ttf")}[kind]
        fo=ImageFont.truetype(p, int(round(sz*S))); fo.lsize=sz; _FC[k]=fo
    return _FC[k]
def sc(v): return v*S
def scp(pts): return [(x*S,y*S) for x,y in pts]
class D:
    def __init__(s, im): s.d=ImageDraw.Draw(im, "RGBA")
    def text(s, xy, t, font, fill): s.d.text((xy[0]*S, xy[1]*S), t, font=font, fill=fill)
    def textlength(s, t, font): return s.d.textlength(t, font=font)/S
    def line(s, pts, fill, width=1, joint=None):
        pts=[tuple(p) for p in (pts if isinstance(pts[0],(tuple,list)) else zip(pts[0::2],pts[1::2]))]
        s.d.line(scp(pts), fill=fill, width=max(1,int(width*S)), joint=joint)
    def rectangle(s, b, fill=None, outline=None, width=1): s.d.rectangle([b[0]*S,b[1]*S,b[2]*S,b[3]*S], fill=fill, outline=outline, width=max(1,int(width*S)))
    def rounded_rectangle(s, b, radius, fill=None, outline=None, width=1):
        if b[3]<=b[1] or b[2]<=b[0]: return
        s.d.rounded_rectangle([b[0]*S,b[1]*S,b[2]*S,b[3]*S], radius=radius*S, fill=fill, outline=outline, width=max(1,int(width*S)))
    def ellipse(s, b, fill=None, outline=None, width=1): s.d.ellipse([b[0]*S,b[1]*S,b[2]*S,b[3]*S], fill=fill, outline=outline, width=max(1,int(width*S)))
    def polygon(s, pts, fill=None, outline=None): s.d.polygon(scp(pts), fill=fill, outline=outline)

def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
def seg(t0, d): return ease((T-t0)/d)        # local progress of a sub-animation
def alpha(c, a): return tuple(c)+(int(255*max(0,min(1,a))),)
def mix(c1,c2,a): return tuple(int(c1[i]+(c2[i]-c1[i])*a) for i in range(3))

_BASE={}
def base(bg=INK):
    if bg not in _BASE:
        im=Image.new("RGB",(PW,PH),bg)
        v=Image.new("L",(PW,PH),0); d=ImageDraw.Draw(v)
        for i in range(40): d.rectangle([i*12,i*7.5,PW-i*12,PH-i*7.5], fill=int(i*6))
        v=v.filter(ImageFilter.GaussianBlur(90))
        _BASE[bg]=Image.composite(im, Image.new("RGB",(PW,PH),(0,0,0)), v.point(lambda x: min(255,120+x)))
    return _BASE[bg].copy()

def tagline(im, tag):
    if not tag: return
    a=seg(1.0,0.6); d=D(im); d.text((40,H-46), tag.upper()[:90], font=f(20,"reg"), fill=alpha(GREY,a))
def center(d, y, text, font, fill):
    w=d.textlength(text, font=font); d.text(((W-w)/2, y), text, font=font, fill=fill)
def wrap(d, text, font, maxw):
    words=text.split(); lines=[]; cur=""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w_
    if cur: lines.append(cur)
    return lines
def countup(s, e):
    def rep(m):
        txt=m.group(0); dec=len(txt.split(".")[1]) if "." in txt else 0; v=float(txt.replace(",",""))*e
        out=f"{v:,.{dec}f}" if "," in txt else f"{v:.{dec}f}"; return out
    return re.sub(r"\d[\d,]*(?:\.\d+)?", rep, s)

# ---------- types ----------
def part(n, title, sub=""):
    im=base(); d=D(im)
    center(d, 40, str(n), f(560,"bebas"), alpha((40,37,34), seg(0,1.2)))
    a=seg(0.15,0.5); center(d, 250-(1-a)*20, f"PART {n}", f(44,"inter"), alpha(ORANGE,a))
    b=seg(0.35,0.6); center(d, 310+(1-b)*40, title.upper(), f(120,"inter"), alpha(PAPER,b))
    if sub: center(d, 460, sub, f(44,"serif"), alpha(ORANGE, seg(0.8,0.5)))
    return im

def number(big, sub="", kicker="", tag="", faded="", strike=None):
    im=base(); d=D(im)
    if kicker: center(d, 150, kicker.upper(), f(34,"inter"), alpha(ORANGE, seg(0,0.4)))
    fb=f(170 if len(big)<9 else 120,"inter")
    if faded: center(d, 200, faded, f(260,"bebas"), alpha((44,41,38), seg(0.3,0.8)))
    e=seg(0.1,1.3); center(d, 215, countup(big, e) if not strike else big, fb, alpha(PAPER, min(1,e*3)))
    if strike:
        w=d.textlength(big,font=fb); x0=(W-w)/2; k=seg(1.0,0.35)
        if k>0: d.line([(x0-10,330),(x0-10+(w+20)*k,330-30*k)],fill=CRIMSON,width=12)
        center(d, 430, strike, f(120,"inter"), alpha(ORANGE, seg(1.4,0.4)))
    if sub:
        a=seg(1.2,0.5)
        for i,l in enumerate(wrap(d, sub, f(44,"serif"), W-200)[:2]): center(d, (450+i*56 if not strike else 580), l, f(44,"serif"), alpha(ORANGE,a))
    tagline(im, tag); return im

def bars(items, title="", unit="", hi=None, tag="", horizontal=False):
    im=base(); d=D(im)
    if title: d.text((60,50), title.upper(), font=f(40,"inter"), fill=alpha(PAPER, seg(0,0.4)))
    mx=max(v for _,v in items) or 1
    n=len(items); bw=min(220,(W-200)//n-40); gap=((W-160)-n*bw)//max(1,n)
    for i,(lab,v) in enumerate(items):
        e=seg(0.3+i*0.25, 1.0)
        x=100+i*(bw+gap)+gap//2; h=int(420*v/mx*e); y=H-140-h
        col = ORANGE if (hi is None or i==hi) else (90,84,76)
        if h>0: d.rectangle([x,y,x+bw,H-140], fill=col)
        val=countup(f"{v:g}",e)+unit; tw=d.textlength(val,font=f(40,"inter")); d.text((x+(bw-tw)/2,y-52), val, font=f(40,"inter"), fill=alpha(PAPER,min(1,e*4)))
        for j,l in enumerate(wrap(d, lab, f(26,"reg"), bw+40)[:2]):
            tw=d.textlength(l,font=f(26,"reg")); d.text((x+(bw-tw)/2,H-128+j*30), l, font=f(26,"reg"), fill=alpha(PAPER, seg(0.1,0.4)))
    tagline(im, tag); return im

def line(series, title="", marks=(), tag="", ylab=""):
    im=base(); d=D(im)
    if title: d.text((60,50), title.upper(), font=f(38,"inter"), fill=alpha(PAPER, seg(0,0.4)))
    allv=[v for s in series.values() for _,v in s]; mn=min(0,min(allv)); mx=max(allv)*1.12
    x0,x1,y0,y1=110,W-80,140,H-110
    d.line([(x0,y1),(x1,y1)],fill=GREY,width=2); d.line([(x0,y0),(x0,y1)],fill=GREY,width=2)
    cols=[ORANGE,CYAN,PAPER,RED]; e=seg(0.3,2.0)
    for k,(name,pts) in enumerate(series.items()):
        n=len(pts); xy=[(x0+(x1-x0)*i/max(1,n-1), y1-(y1-y0)*(v-mn)/(mx-mn)) for i,(_,v) in enumerate(pts)]
        pos=e*(n-1); full=int(pos); fr=pos-full
        part_=xy[:full+1]
        if full<n-1: part_=part_+[(xy[full][0]+(xy[full+1][0]-xy[full][0])*fr, xy[full][1]+(xy[full+1][1]-xy[full][1])*fr)]
        if len(part_)>1: d.line(part_, fill=cols[k%4], width=6, joint="curve")
        for i,((lab,v),(x,y)) in enumerate(zip(pts,xy)):
            if i<=pos+1e-6: d.ellipse([x-7,y-7,x+7,y+7],fill=cols[k%4])
            if lab and k==0: d.text((x-30,y1+10), lab, font=f(22,"reg"), fill=alpha(GREY, seg(0.1,0.4)))
        if e>=0.99:
            lx,ly=xy[-1]; d.text((lx-10-d.textlength(name,font=f(26,"inter")), ly-44), name, font=f(26,"inter"), fill=alpha(cols[k%4], seg(2.2,0.4)))
    for (txt,i,s_) in marks:
        pts=list(series.values())[s_]; n=len(pts)
        if e*(n-1) < i-1e-6: continue
        x=x0+(x1-x0)*i/max(1,n-1); v=pts[i][1]; y=y1-(y1-y0)*(v-mn)/(mx-mn)
        r=16+4*math.sin(T*3); d.ellipse([x-r,y-r,x+r,y+r],outline=PAPER,width=3); d.text((x+20,y-60), txt, font=f(30,"inter"), fill=PAPER)
    d.text((W-460,H-46),"CURVE SHAPE ILLUSTRATIVE",font=f(18,"reg"),fill=alpha(GREY, seg(1,0.5)))
    tagline(im, tag); return im

def gauges(items, ghost=None, title="", tag=""):
    im=base(); d=D(im)
    if title: center(d, 40, title.upper(), f(38,"inter"), alpha(PAPER, seg(0,0.4)))
    n=len(items); gw=180; gap=(W-n*gw)//(n+1)
    for i,(lab,p) in enumerate(items):
        e=seg(0.3+0.3*i,1.4)
        x=gap+i*(gw+gap); top,bot=130,H-150
        d.rounded_rectangle([x,top,x+gw,bot],radius=24,outline=PAPER,width=5)
        h=int((bot-top-10)*p/100*e); d.rounded_rectangle([x+8,bot-8-h,x+gw-8,bot-8],radius=16,fill=ORANGE if i==n-1 else (110,100,90))
        if ghost: gy=bot-8-int((bot-top-10)*ghost/100); d.line([(x-20,gy),(x+gw+20,gy)],fill=alpha(CYAN, seg(1.6,0.5)),width=4)
        cx=lambda t,fo: x+(gw-d.textlength(t,font=fo))/2
        txt=countup(f"{p:g}",e)+"%"
        d.text((cx(txt,f(48,"inter")), bot-h-70), txt, font=f(48,"inter"), fill=PAPER)
        d.text((cx(lab,f(30,"inter")), bot+16), lab, font=f(30,"inter"), fill=PAPER)
    if ghost: d.text((W-330,100), f"NORMAL ≈ {ghost}%", font=f(28,"inter"), fill=alpha(CYAN, seg(1.6,0.5)))
    tagline(im, tag); return im

_SHAPES=None
def shapes():
    global _SHAPES
    if _SHAPES is None:
        r=shapefile.Reader(str(A/"ne_50m_admin_0_countries.shp")); fl=[x[0] for x in r.fields[1:]]
        _SHAPES=[(dict(zip(fl,rec.record)), rec.shape) for rec in r.shapeRecords()]
    return _SHAPES
_MAP={}
def _mapbase(bbox, hi, hi2, lit):
    k=(bbox,tuple(hi),tuple(hi2),lit)
    if k not in _MAP:
        lon0,lat0,lon1,lat1=bbox; im=base((14,18,22)); d=D(im)
        P=lambda lo,la: ((lo-lon0)/(lon1-lon0)*W, (lat1-la)/(lat1-lat0)*H)
        for rec,shp in shapes():
            name=rec.get("ADMIN") or rec.get("NAME")
            col = (ORANGE if name in hi else (RED if name in hi2 else LAND)) if lit else LAND
            pts=shp.points; parts=list(shp.parts)+[len(pts)]
            for a,b in zip(parts[:-1],parts[1:]):
                ring=[P(*p) for p in pts[a:b]]
                if len(ring)>2: d.polygon(ring, fill=col, outline=BORDER)
        _MAP[k]=im
    return _MAP[k]
def map_(bbox, hi=(), hi2=(), dots=(), lines=(), title="", tag="", label_hi=True):
    lon0,lat0,lon1,lat1=bbox
    a=seg(0.4,0.8)
    im=Image.blend(_mapbase(bbox,hi,hi2,False), _mapbase(bbox,hi,hi2,True), a) if (hi or hi2) else _mapbase(bbox,hi,hi2,False).copy()
    d=D(im); P=lambda lo,la: ((lo-lon0)/(lon1-lon0)*W, (lat1-la)/(lat1-lat0)*H)
    for i,(p0,p1,col,w_) in enumerate(lines):
        e=seg(0.6+0.2*i,1.4); (xa,ya),(xb,yb)=P(*p0),P(*p1)
        if e>0: d.line([(xa,ya),(xa+(xb-xa)*e, ya+(yb-ya)*e)], fill=col, width=w_)
    for j,(lo,la,txt,col) in enumerate(dots):
        x,y=P(lo,la); e=seg(0.2+0.15*j,0.4)
        if e<=0: continue
        d.ellipse([x-10*e,y-10*e,x+10*e,y+10*e],fill=col)
        for ph in (0,0.5):
            q=((T*0.6+ph)%1.0); r_=12+40*q; d.ellipse([x-r_,y-r_,x+r_,y+r_],outline=alpha(col,1-q),width=2)
        if txt: d.text((x+16,y-14), txt, font=f(28,"inter"), fill=alpha(PAPER,e))
    if title: d.text((50,40), title.upper(), font=f(40,"inter"), fill=alpha(PAPER, seg(0.2,0.4)))
    tagline(im, tag); return im

def receipt(lines, title="THE RECEIPT", cols=None, crimson_last=False, tag=""):
    im=base(); d=D(im)
    pw=620 if not cols else 1100; x=(W-pw)//2
    rise=(1-seg(0,0.7))*(H)
    d.rectangle([x,40+rise,x+pw,H-40+rise], fill=PAPER)
    for i in range(0,pw,24): d.polygon([(x+i,H-40+rise),(x+i+12,H-26+rise),(x+i+24,H-40+rise)], fill=PAPER)
    center(d, 60+rise, "THE HISTORY INVOICE", f(26,"inter"), INK); center(d, 96+rise, title, f(40,"bebas"), INK)
    d.line([(x+30,145+rise),(x+pw-30,145+rise)], fill=INK, width=2)
    y=165+rise
    for i,l in enumerate(lines):
        a=seg(0.8+0.45*i,0.15)
        if a<=0: break
        col = CRIMSON if (crimson_last and i==len(lines)-1) else INK
        if isinstance(l, tuple):
            d.text((x+30,y), l[0], font=f(28,"reg"), fill=alpha(col,a)); tw=d.textlength(l[1],font=f(28,"inter")); d.text((x+pw-30-tw,y), l[1], font=f(28,"inter"), fill=alpha(col,a))
        else: d.text((x+30,y), l, font=f(28,"reg"), fill=alpha(col,a))
        y+=46
    tagline(im, tag); return im

def _stamp(im, txt, wbox, pos_fn, t0):
    k=seg(t0,0.25)
    if k<=0: return
    s=Image.new("RGBA",(int(wbox*S),int(170*S)),(0,0,0,0)); sd=D(s)
    sd.rectangle([5,5,wbox-5,165],outline=CRIMSON+(255,),width=10); tw=sd.textlength(txt,font=f(120,"bebas")); sd.text(((wbox-tw)/2,10),txt,font=f(120,"bebas"),fill=CRIMSON+(255,))
    s=s.rotate(-8,expand=True,resample=Image.BICUBIC); z=1.6-0.6*k
    s=s.resize((max(1,int(s.width*z)),max(1,int(s.height*z))))
    if k<1: s.putalpha(s.getchannel("A").point(lambda v: int(v*k)))
    x,y=pos_fn(s); im.paste(s,(int(x),int(y)),s)

def card(lines, kicker="", style="big", tag="", stamp=None):
    im=base(); d=D(im)
    y=150 if kicker else 120
    if kicker: center(d, 80, kicker.upper(), f(32,"inter"), alpha(ORANGE, seg(0,0.4)))
    for i,l in enumerate(lines):
        fo = f(64,"inter") if style=="big" else (f(48,"serif") if style=="serif" else f(42,"reg"))
        col = PAPER if i%2==0 or style!="big" else ORANGE
        a=seg(0.2+0.45*i,0.5)
        for ll in wrap(d,l,fo,W-180): center(d,y+(1-a)*18,ll,fo,alpha(col,a)); y+=fo.lsize+18
    if stamp: _stamp(im, stamp, 700, lambda s: ((PW-s.width)//2, PH-s.height-70*S), 1.2)
    tagline(im, tag); return im

def headline(outlet, text, date, stamp=None, tag=""):
    im=base(); d=D(im); dx=(1-seg(0,0.5))*W
    d.rectangle([150+dx,110,W-150+dx,H-150], fill=(228,224,216))
    d.text((190+dx,140), outlet.upper(), font=f(36,"inter"), fill=INK); d.text((W-190-d.textlength(date,font=f(28,"reg"))+dx,146), date, font=f(28,"reg"), fill=(90,90,90))
    d.line([(190+dx,200),(W-190+dx,200)], fill=INK, width=3)
    y=230
    for l in wrap(d,text,f(58,"inter"),W-380): d.text((190+dx,y),l,font=f(58,"inter"),fill=INK); y+=72
    d.text((190+dx,H-200),"Recreated headline · outlet credited",font=f(22,"reg"),fill=(110,110,110))
    if stamp: _stamp(im, stamp, 760, lambda s: (PW-s.width-80*S, PH-s.height-40*S), 1.4)
    tagline(im, tag); return im

_ST={}
def still(code, caption, stills_dir, overlay="", tag="", label="ILLUSTRATION"):
    p=pathlib.Path(stills_dir)/f"{code}.jpg"
    if p.exists():
        if code not in _ST:
            src=Image.open(p).convert("RGB"); r=max(PW*1.12/src.width,PH*1.12/src.height); src=src.resize((int(src.width*r),int(src.height*r)), Image.LANCZOS)
            src=ImageEnhance.Color(src).enhance(0.6); src=ImageEnhance.Brightness(src).enhance(0.8)
            src=Image.blend(src,Image.new("RGB",src.size,(10,20,35)),0.15); _ST[code]=src
        src=_ST[code]; k=min(1,T/12.0); ox=int((src.width-PW)*k); oy=(src.height-PH)//2
        im=src.crop((ox,oy,ox+PW,oy+PH))
    else:
        im=base((30,32,36))
    sh=Image.new("L",(PW,PH),0); ImageDraw.Draw(sh).rectangle([0,PH-260*S,PW*0.75,PH],fill=170); sh=sh.filter(ImageFilter.GaussianBlur(90))
    im=Image.composite(Image.new("RGB",(PW,PH),(0,0,0)),im,sh); d=D(im)
    if overlay:
        a=seg(0.5,0.6)
        for i,l in enumerate(wrap(d,overlay,f(46,"inter"),W*0.62)[:2]): d.text((50,H-200+i*56+(1-a)*12),l,font=f(46,"inter"),fill=alpha(PAPER,a))
    if label: d.text((W-230,30),label,font=f(22,"inter"),fill=GREY)
    tagline(im, tag); return im
