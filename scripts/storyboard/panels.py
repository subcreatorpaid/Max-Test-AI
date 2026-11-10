import os, sys, math, textwrap, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import shapefile
HERE = pathlib.Path(__file__).parent
A = HERE / "assets"
W, H = 1280, 720
INK=(16,15,14); PAPER=(236,228,214); ORANGE=(232,89,12); RED=(230,57,70); CYAN=(0,180,216); CRIMSON=(193,18,31); GREY=(120,114,106); LAND=(38,36,33); BORDER=(70,66,60)
F_INTER="/usr/share/fonts/opentype/inter/Inter-Bold.otf"; F_INTER_R="/usr/share/fonts/opentype/inter/Inter-Regular.otf"
if not os.path.exists(F_INTER_R): F_INTER_R=F_INTER
def f(sz, kind="inter"):
    p={"inter":F_INTER,"reg":F_INTER_R,"serif":str(A/"CaladeaBI.ttf"),"bebas":str(A/"Bebas.ttf")}[kind]
    return ImageFont.truetype(p, sz)

def base(bg=INK):
    im = Image.new("RGB",(W,H),bg)
    # vignette
    v = Image.new("L",(W,H),0); d=ImageDraw.Draw(v)
    for i in range(40):
        d.rectangle([i*8,i*5,W-i*8,H-i*5], fill=int(i*6))
    v = v.filter(ImageFilter.GaussianBlur(60))
    dark = Image.new("RGB",(W,H),(0,0,0))
    return Image.composite(im, dark, v.point(lambda x: min(255, 120+x)))

def tagline(im, tag):
    if not tag: return
    d=ImageDraw.Draw(im); d.text((40,H-46), tag.upper()[:90], font=f(20,"reg"), fill=GREY)

def center(d, y, text, font, fill):
    w = d.textlength(text, font=font); d.text(((W-w)/2, y), text, font=font, fill=fill)

def wrap(d, text, font, maxw):
    words=text.split(); lines=[]; cur=""
    for w_ in words:
        t=(cur+" "+w_).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: lines.append(cur); cur=w_
    if cur: lines.append(cur)
    return lines

# ---------- types ----------
def part(n, title, sub=""):
    im=base(); d=ImageDraw.Draw(im)
    center(d, 40, str(n), f(560,"bebas"), (34,32,30))
    center(d, 250, f"PART {n}", f(44,"inter"), ORANGE)
    center(d, 310, title.upper(), f(120,"inter"), PAPER)
    if sub: center(d, 460, sub, f(44,"serif"), ORANGE)
    return im

def number(big, sub="", kicker="", tag="", faded="", strike=None):
    im=base(); d=ImageDraw.Draw(im)
    if kicker: center(d, 150, kicker.upper(), f(34,"inter"), ORANGE)
    fb=f(170 if len(big)<9 else 120,"inter")
    if faded: center(d, 200, faded, f(260,"bebas"), (40,38,35))
    center(d, 215, big, fb, PAPER)
    if strike:
        w=d.textlength(big,font=fb); x0=(W-w)/2; d.line([x0-10,330,x0+w+10,300],fill=CRIMSON,width=12)
        center(d, 430, strike, f(120,"inter"), ORANGE)
    if sub: 
        for i,l in enumerate(wrap(d, sub, f(44,"serif"), W-200)[:2]): center(d, 450+i*56 if not strike else 580, l, f(44,"serif"), ORANGE)
    tagline(im, tag); return im

def bars(items, title="", unit="", hi=None, tag="", horizontal=False):
    im=base(); d=ImageDraw.Draw(im)
    if title: d.text((60,50), title.upper(), font=f(40,"inter"), fill=PAPER)
    mx=max(v for _,v in items) or 1
    n=len(items); bw=min(220,(W-200)//n-40); gap=((W-160)-n*bw)//max(1,n)
    for i,(lab,v) in enumerate(items):
        x=100+i*(bw+gap)+gap//2; h=int(420*v/mx); y=H-140-h
        col = ORANGE if (hi is None or i==hi) else (90,84,76)
        d.rectangle([x,y,x+bw,H-140], fill=col)
        val=f"{v:g}{unit}"; tw=d.textlength(val,font=f(40,"inter")); d.text((x+(bw-tw)/2,y-52), val, font=f(40,"inter"), fill=PAPER)
        for j,l in enumerate(wrap(d, lab, f(26,"reg"), bw+40)[:2]):
            tw=d.textlength(l,font=f(26,"reg")); d.text((x+(bw-tw)/2,H-128+j*30), l, font=f(26,"reg"), fill=PAPER)
    tagline(im, tag); return im

def line(series, title="", marks=(), tag="", ylab=""):
    im=base(); d=ImageDraw.Draw(im)
    if title: d.text((60,50), title.upper(), font=f(38,"inter"), fill=PAPER)
    allv=[v for s in series.values() for _,v in s]; mn=min(0,min(allv)); mx=max(allv)*1.12
    x0,x1,y0,y1=110,W-80,140,H-110
    d.line([x0,y1,x1,y1],fill=GREY,width=2); d.line([x0,y0,x0,y1],fill=GREY,width=2)
    cols=[ORANGE,CYAN,PAPER,RED]
    for k,(name,pts) in enumerate(series.items()):
        n=len(pts); xy=[(x0+(x1-x0)*i/max(1,n-1), y1-(y1-y0)*(v-mn)/(mx-mn)) for i,(_,v) in enumerate(pts)]
        d.line(xy, fill=cols[k%4], width=6, joint="curve")
        for (lab,v),(x,y) in zip(pts,xy):
            d.ellipse([x-7,y-7,x+7,y+7],fill=cols[k%4])
            if lab: d.text((x-30,y1+10), lab, font=f(22,"reg"), fill=GREY)
        lx,ly=xy[-1]; d.text((lx-10-d.textlength(name,font=f(26,"inter")), ly-44), name, font=f(26,"inter"), fill=cols[k%4])
    for (txt,i,s) in marks:
        pts=list(series.values())[s]; n=len(pts); x=x0+(x1-x0)*i/max(1,n-1); v=pts[i][1]; y=y1-(y1-y0)*(v-mn)/(mx-mn)
        d.ellipse([x-16,y-16,x+16,y+16],outline=PAPER,width=3); d.text((x+20,y-60), txt, font=f(30,"inter"), fill=PAPER)
    d.text((W-460,H-46),"CURVE SHAPE ILLUSTRATIVE · real data at build",font=f(18,"reg"),fill=GREY)
    tagline(im, tag); return im

def gauges(items, ghost=None, title="", tag=""):
    im=base(); d=ImageDraw.Draw(im)
    if title: center(d, 40, title.upper(), f(38,"inter"), PAPER)
    n=len(items); gw=180; gap=(W-n*gw)//(n+1)
    for i,(lab,p) in enumerate(items):
        x=gap+i*(gw+gap); top,bot=130,H-150
        d.rounded_rectangle([x,top,x+gw,bot],radius=24,outline=PAPER,width=5)
        h=int((bot-top-10)*p/100); d.rounded_rectangle([x+8,bot-8-h,x+gw-8,bot-8],radius=16,fill=ORANGE if i==n-1 else (110,100,90))
        if ghost: gy=bot-8-int((bot-top-10)*ghost/100); d.line([x-20,gy,x+gw+20,gy],fill=CYAN,width=4)
        center_x=lambda t,fo: x+(gw-d.textlength(t,font=fo))/2
        d.text((center_x(f"{p:g}%",f(48,"inter")), bot-h-70), f"{p:g}%", font=f(48,"inter"), fill=PAPER)
        d.text((center_x(lab,f(30,"inter")), bot+16), lab, font=f(30,"inter"), fill=PAPER)
    if ghost: d.text((W-330,100), f"NORMAL ≈ {ghost}%", font=f(28,"inter"), fill=CYAN)
    tagline(im, tag); return im

_SHAPES=None
def shapes():
    global _SHAPES
    if _SHAPES is None:
        r=shapefile.Reader(str(A/"ne_50m_admin_0_countries.shp")); fl=[x[0] for x in r.fields[1:]]
        _SHAPES=[(dict(zip(fl,rec.record)), rec.shape) for rec in r.shapeRecords()]
    return _SHAPES

def map_(bbox, hi=(), hi2=(), dots=(), lines=(), title="", tag="", label_hi=True):
    lon0,lat0,lon1,lat1=bbox; im=base((14,18,22)); d=ImageDraw.Draw(im)
    P=lambda lo,la: ((lo-lon0)/(lon1-lon0)*W, (lat1-la)/(lat1-lat0)*H)
    for rec,shp in shapes():
        name=rec.get("ADMIN") or rec.get("NAME")
        col = ORANGE if name in hi else (RED if name in hi2 else LAND)
        pts=shp.points; parts=list(shp.parts)+[len(pts)]
        for a,b in zip(parts[:-1],parts[1:]):
            ring=[P(*p) for p in pts[a:b]]
            if len(ring)>2: d.polygon(ring, fill=col, outline=BORDER)
    for (a,b,col,w_) in lines:
        d.line([P(*a),P(*b)], fill=col, width=w_)
    for (lo,la,txt,col) in dots:
        x,y=P(lo,la); d.ellipse([x-10,y-10,x+10,y+10],fill=col); 
        for r_ in (22,36): d.ellipse([x-r_,y-r_,x+r_,y+r_],outline=col,width=2)
        if txt: d.text((x+16,y-14), txt, font=f(28,"inter"), fill=PAPER)
    if title: d.text((50,40), title.upper(), font=f(40,"inter"), fill=PAPER)
    tagline(im, tag); return im

def receipt(lines, title="THE RECEIPT", cols=None, crimson_last=False, tag=""):
    im=base(); d=ImageDraw.Draw(im)
    pw=620 if not cols else 1100; x=(W-pw)//2
    d.rectangle([x,40,x+pw,H-40], fill=PAPER)
    # zigzag bottom
    for i in range(0,pw,24): d.polygon([(x+i,H-40),(x+i+12,H-26),(x+i+24,H-40)], fill=PAPER)
    center(d, 60, "THE HISTORY INVOICE", f(26,"inter"), INK); center(d, 96, title, f(40,"bebas"), INK)
    d.line([x+30,145,x+pw-30,145], fill=INK, width=2)
    y=165
    for i,l in enumerate(lines):
        col = CRIMSON if (crimson_last and i==len(lines)-1) else INK
        if isinstance(l, tuple):
            d.text((x+30,y), l[0], font=f(28,"reg"), fill=col); tw=d.textlength(l[1],font=f(28,"inter")); d.text((x+pw-30-tw,y), l[1], font=f(28,"inter"), fill=col)
        else: d.text((x+30,y), l, font=f(28,"reg"), fill=col)
        y+=46
    tagline(im, tag); return im

def card(lines, kicker="", style="big", tag="", stamp=None):
    im=base(); d=ImageDraw.Draw(im)
    y=150 if kicker else 120
    if kicker: center(d, 80, kicker.upper(), f(32,"inter"), ORANGE)
    for i,l in enumerate(lines):
        fo = f(64,"inter") if style=="big" else (f(48,"serif") if style=="serif" else f(42,"reg"))
        col = PAPER if i%2==0 or style!="big" else ORANGE
        for ll in wrap(d,l,fo,W-180): center(d,y,ll,fo,col); y+=fo.size+18
    if stamp:
        s=Image.new("RGBA",(700,170),(0,0,0,0)); sd=ImageDraw.Draw(s)
        sd.rectangle([5,5,695,165],outline=CRIMSON+(255,),width=10); tw=sd.textlength(stamp,font=f(120,"bebas")); sd.text(((700-tw)/2,10),stamp,font=f(120,"bebas"),fill=CRIMSON+(255,))
        s=s.rotate(-8,expand=True); im.paste(s,((W-s.width)//2,H-s.height-70),s)
    tagline(im, tag); return im

def headline(outlet, text, date, stamp=None, tag=""):
    im=base(); d=ImageDraw.Draw(im)
    d.rectangle([150,110,W-150,H-150], fill=(228,224,216))
    d.text((190,140), outlet.upper(), font=f(36,"inter"), fill=INK); d.text((W-190-d.textlength(date,font=f(28,"reg")),146), date, font=f(28,"reg"), fill=(90,90,90))
    d.line([190,200,W-190,200], fill=INK, width=3)
    y=230
    for l in wrap(d,text,f(58,"inter"),W-380): d.text((190,y),l,font=f(58,"inter"),fill=INK); y+=72
    d.text((190,H-200),"Recreated headline · outlet credited",font=f(22,"reg"),fill=(110,110,110))
    if stamp:
        s=Image.new("RGBA",(760,170),(0,0,0,0)); sd=ImageDraw.Draw(s)
        sd.rectangle([5,5,755,165],outline=CRIMSON+(255,),width=10); tw=sd.textlength(stamp,font=f(120,"bebas")); sd.text(((760-tw)/2,10),stamp,font=f(120,"bebas"),fill=CRIMSON+(255,))
        s=s.rotate(-8,expand=True); im.paste(s,(W-s.width-80,H-s.height-40),s)
    tagline(im, tag); return im

def still(code, caption, stills_dir, overlay="", tag="", label="ILLUSTRATION"):
    p=pathlib.Path(stills_dir)/f"{code}.jpg"
    if p.exists():
        src=Image.open(p).convert("RGB"); r=max(W/src.width,H/src.height); src=src.resize((int(src.width*r),int(src.height*r)))
        l=(src.width-W)//2; t=(src.height-H)//2; im=src.crop((l,t,l+W,t+H))
        # grade: desaturate, darken, cool
        from PIL import ImageEnhance
        im=ImageEnhance.Color(im).enhance(0.6); im=ImageEnhance.Brightness(im).enhance(0.8)
        cool=Image.new("RGB",(W,H),(10,20,35)); im=Image.blend(im,cool,0.15)
    else:
        im=base((30,32,36)); d=ImageDraw.Draw(im)
        for i,l in enumerate(wrap(d,caption,f(40,"serif"),W-240)[:4]): center(d,260+i*54,l,f(40,"serif"),PAPER)
        center(d,180,"[ STILL / FOOTAGE ]",f(30,"inter"),GREY)
    d=ImageDraw.Draw(im)
    # bottom-left shade + overlay text
    sh=Image.new("L",(W,H),0); sd=ImageDraw.Draw(sh); sd.rectangle([0,H-260,W*0.75,H],fill=170); sh=sh.filter(ImageFilter.GaussianBlur(60))
    im=Image.composite(Image.new("RGB",(W,H),(0,0,0)),im,sh); d=ImageDraw.Draw(im)
    if overlay:
        for i,l in enumerate(wrap(d,overlay,f(46,"inter"),W*0.62)[:2]): d.text((50,H-200+i*56),l,font=f(46,"inter"),fill=PAPER)
    if label: d.text((W-230,30),label,font=f(22,"inter"),fill=GREY)
    tagline(im, tag); return im
