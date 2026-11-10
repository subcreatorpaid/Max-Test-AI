"""History Invoice graphics kit v2 ("ledger" look), adapted from the Round Two draft part 3 (studied 2026-11-10).
Mixes our brand (ink/paper/orange, Inter + Caladea, confidence tags, the Receipt) with the reference's
paper cards, rubber stamps, documents with a circled line, split-flap boards, cut-paper figures, navy globe and receipt printer."""
import math, random, pathlib
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance, ImageOps, ImageChops
import shapefile
W, H = 1280, 720
INK=(20,17,15); PAPER=(214,204,186); PAPER2=(226,214,192); ORANGE=(232,89,12); RED=(196,36,40); GREEN=(46,125,70)
GREY=(140,132,120); DIM=(70,64,58); NAVY=(20,38,66); LANDC=(92,84,72); CRIMSON=(193,18,31)
ROOT=pathlib.Path(__file__).resolve().parents[2]
ASSETS=ROOT/"tools/inv006/assets"
FI="/usr/share/fonts/opentype/inter/"
def F(sz,k="b"):
    p={"b":FI+"Inter-Bold.otf","xb":FI+"Inter-ExtraBold.otf","r":FI+"Inter-Regular.otf","m":FI+"Inter-Medium.otf",
       "s":str(ASSETS/"CaladeaBI.ttf"),"bebas":str(ASSETS/"Bebas.ttf"),"mono":"/usr/share/fonts/truetype/liberation/LiberationMono-Bold.ttf",
       "monor":"/usr/share/fonts/truetype/liberation/LiberationMono-Regular.ttf"}[k]
    return ImageFont.truetype(p,sz)
R=random.Random(7)

def grain(im, amt=10):
    n=Image.effect_noise((W,H),amt).convert("RGB"); return ImageChops.add(im, n, 1.0, -128)
def vignette(im, s=0.55):
    m=Image.new("L",(W,H),0); d=ImageDraw.Draw(m); d.ellipse([-W*0.25,-H*0.35,W*1.25,H*1.35],fill=255)
    m=m.filter(ImageFilter.GaussianBlur(160)); dark=Image.new("RGB",(W,H),(0,0,0))
    return Image.composite(im, Image.blend(im,dark,s), m)
def ledger():
    im=Image.new("RGB",(W,H),INK); d=ImageDraw.Draw(im)
    for y in range(40,H,26): d.line([0,y,W,y],fill=(27,24,21),width=1)
    return vignette(grain(im,14),0.6)
def dark():  # Hammad 2026-11-10: every graphic uses the part-card background
    return ledger()
def tag(im, t, src=""):
    if not t: return im
    d=ImageDraw.Draw(im); s=(t+(" · "+src if src else "")).upper()[:70]
    x=W-40-d.textlength(s,font=F(15,"m")); d.text((x,26),s,font=F(15,"m"),fill=GREY)
    d.line([x-34,35,x-10,35],fill=ORANGE,width=2); return im
def wrap(d,text,font,maxw):
    out=[];cur=""
    for w in text.split():
        t=(cur+" "+w).strip()
        if d.textlength(t,font=font)<=maxw: cur=t
        else: out.append(cur); cur=w
    if cur: out.append(cur)
    return out
def paper_rect(size, col=PAPER, torn=True, seed=1):
    w,h=size; r=random.Random(seed); im=Image.new("RGBA",(w,h),(0,0,0,0)); d=ImageDraw.Draw(im)
    pts=[]
    step=14
    for x in range(0,w+1,step): pts.append((x, r.randint(0,4) if torn else 0))
    for y in range(0,h+1,step): pts.append((w-(r.randint(0,4) if torn else 0), y))
    for x in range(w,-1,-step): pts.append((x, h-(r.randint(0,5) if torn else 0)))
    for y in range(h,-1,-step): pts.append(((r.randint(0,4) if torn else 0), y))
    d.polygon(pts, fill=col+(255,))
    tex=Image.effect_noise((w,h),22).convert("L").point(lambda v: 255-int((255-v)*0.12))
    base=Image.new("RGB",(w,h),col); base=ImageChops.multiply(base, Image.merge("RGB",(tex,tex,tex)))
    out=Image.new("RGBA",(w,h)); out.paste(base,(0,0),im); return out
def drop(im, layer, xy, angle=0, shadow=18):
    if angle: layer=layer.rotate(angle,expand=True,resample=Image.BICUBIC)
    sh=Image.new("RGBA",layer.size,(0,0,0,0)); a=layer.split()[3].point(lambda v: int(v*0.7))
    sh.putalpha(a); sh=sh.filter(ImageFilter.GaussianBlur(shadow))
    blk=Image.new("RGBA",layer.size,(0,0,0,255)); blk.putalpha(sh.split()[3])
    im.paste(blk,(xy[0]+10,xy[1]+14),blk); im.paste(layer,xy,layer); return im
def stamp(text, col=RED, size=54, angle=-8):
    f=F(size,"xb"); tw=int(ImageDraw.Draw(Image.new("L",(1,1))).textlength(text,font=f))+40; th=size+30
    L=Image.new("L",(tw,th),0); d=ImageDraw.Draw(L); d.rectangle([3,3,tw-4,th-4],outline=255,width=5); d.text((20,8),text,font=f,fill=255)
    n=Image.effect_noise((tw,th),90).point(lambda v: 255 if v>95 else 0); L=ImageChops.multiply(L,n.convert("L"))
    L=L.filter(ImageFilter.GaussianBlur(0.6)); im=Image.new("RGBA",(tw,th),col+(0,)); im.putalpha(L.point(lambda v:int(v*0.9)))
    return im.rotate(angle,expand=True,resample=Image.BICUBIC)

# ---------- N: ledger number card (reference 0:00) ----------
def number(big, sub="", kicker="", t="", src="", faded=""):
    im=ledger(); d=ImageDraw.Draw(im)
    if kicker: d.line([92,128,116,128],fill=ORANGE,width=3); d.text((126,118),kicker.upper(),font=F(20,"m"),fill=GREY)
    if faded: d.text((700,200),faded,font=F(220,"bebas"),fill=(38,34,30))
    fb=F(150 if len(big)<8 else (112 if len(big)<12 else 84),"b"); d.text((86,160),big,font=fb,fill=PAPER)
    if sub:
        for i,l in enumerate(wrap(d,sub,F(42,"s"),W-200)[:2]): d.text((92,350+i*52),l,font=F(42,"s"),fill=ORANGE)
    return tag(im,t,src)
# ---------- footage / still frame, toned, orange glow, paper lower-third (reference 0:17, 2:52, 5:37) ----------
# Hammad 2026-11-10: about 30% of footage in shadow, the rest coloured by scene intensity
SHADOW="CO-01 RC-11 P1-03b P1-13 P3-07 P3-11 P3-12 P3-13 P4-06 P5-09e P6-08 P6-09".split()
HIGH="CO-03 CO-04 P1-05 P1-06 P1-08c P1-11 P2-10b P3-05c P3-06 P5-02 P5-06 P5-07 P6-02".split()
LOW="P1-03 P1-08b P2-02 P2-04b P2-06 P4-08 P4-09 P5-03 P5-09b P6-03 P6-07b RC-05".split()
GRADE={**{c:"shadow" for c in SHADOW},**{c:"high" for c in HIGH},**{c:"low" for c in LOW}}
CUR=[""]
def tone(img, glow=None, mode="warm"):
    src=img.convert("RGB"); r=max(W/src.width,H/src.height); src=src.resize((int(src.width*r)+1,int(src.height*r)+1))
    l=(src.width-W)//2; t=(src.height-H)//2; im=src.crop((l,t,l+W,t+H))
    g=GRADE.get(CUR[0],"mid") if mode!="mono" else "mono"
    if g in("mono","shadow"):  # shadow: dark, almost colourless, cold, heavy vignette
        x=ImageEnhance.Color(im).enhance(0.12); x=ImageEnhance.Contrast(x).enhance(1.2); im=ImageEnhance.Brightness(x).enhance(0.68)
        im=Image.blend(im,Image.new("RGB",(W,H),(8,14,26)),0.15)
    else:  # colour by scene intensity, all 20% darker (Hammad): low = calm/cool, mid = INV-006 look, high = punchy/warm
        c,k,b,tint,a={"low":(0.8,1.0,0.8,(10,20,35),0.10),"mid":(0.9,1.05,0.8,(10,20,35),0.07),"high":(1.15,1.12,0.8,(60,30,10),0.06)}[g]
        im=ImageEnhance.Color(im).enhance(c); im=ImageEnhance.Contrast(im).enhance(k); im=ImageEnhance.Brightness(im).enhance(b)
        im=Image.blend(im,Image.new("RGB",(W,H),tint),a)
    if glow:
        m=Image.new("L",(W,H),0); d=ImageDraw.Draw(m); x,y=glow; d.ellipse([x-70,y-55,x+70,y+55],fill=200); m=m.filter(ImageFilter.GaussianBlur(40))
        im=Image.composite(Image.new("RGB",(W,H),ORANGE),im,m.point(lambda v:int(v*0.35)))
    return vignette(grain(im,8),0.55 if g in('mono','shadow') else 0.35)
def lower(im, title, sub=""):
    d=ImageDraw.Draw(im); ft=F(28,"xb"); fs=F(22,"s")
    w=int(max(d.textlength(title.upper(),font=ft), d.textlength(sub,font=fs) if sub else 0))+44; h=88 if sub else 58
    p=paper_rect((w,h),PAPER,True,len(title)); pd=ImageDraw.Draw(p); pd.text((20,12),title.upper(),font=ft,fill=(30,26,22))
    if sub: pd.text((20,48),sub,font=fs,fill=ORANGE)
    return drop(im.convert("RGBA"),p,(60,H-h-70),0,10).convert("RGB")
def footage(photo, title="", sub="", glow=None, t="", src="", mode="warm", corner=""):
    if photo and pathlib.Path(photo).exists(): im=tone(Image.open(photo),glow,mode)
    else:
        im=dark(); d=ImageDraw.Draw(im); d.text((W/2-260,H/2-20),"[ matching shot to fetch ]",font=F(36,"s"),fill=GREY)
    if corner: im=corner_number(im,corner)
    if title: im=lower(im,title,sub)
    return tag(im,t,src)
def corner_number(im, txt):
    d=ImageDraw.Draw(im); f=F(84,"b"); w=d.textlength(txt,font=f)
    sh=Image.new("L",(W,H),0); ImageDraw.Draw(sh).rectangle([W-w-140,60,W,260],fill=150); sh=sh.filter(ImageFilter.GaussianBlur(50))
    im=Image.composite(Image.new("RGB",(W,H),(0,0,0)),im,sh); d=ImageDraw.Draw(im); d.text((W-w-70,110),txt,font=f,fill=PAPER); return im
# ---------- D: document, key line circled (no magnifier) (reference 0:39) ----------
def document(title, rows, hi=0, t="", src="", lens_text=None):
    im=dark().convert("RGBA"); pw,ph=880,500; p=paper_rect((pw,ph),(214,204,186),False,3); d=ImageDraw.Draw(p)
    d.text((40,34),title,font=F(34,"s"),fill=(40,34,28)); d.line([40,86,pw-40,86],fill=(150,140,124),width=2)
    for i,(a,b) in enumerate(rows):
        y=120+i*62
        if i==hi: d.rectangle([30,y-10,pw-30,y+42],fill=(236,170,120))
        d.text((44,y),a,font=F(28,"m"),fill=(50,44,38)); d.text((pw-44-d.textlength(b,font=F(28,"b")),y),b,font=F(28,"b"),fill=(50,44,38))
    im=drop(im,p,(200,110),-2)
    # no magnifier (Hammad 2026-11-10): a red pen ring around the key value instead
    y=110+120+hi*62+16; vw=ImageDraw.Draw(p).textlength(rows[hi][1],font=F(28,"b")) if rows else 120
    cx=200+880-52-vw/2; cy=y+20; rx,ry=vw/2+34,40
    pen=Image.new("RGBA",(W,H),(0,0,0,0)); pd=ImageDraw.Draw(pen)
    for k in range(3): pd.ellipse([cx-rx-k*3,cy-ry+k*2,cx+rx+k*2,cy+ry-k],outline=(196,40,32,230),width=4)
    im=Image.alpha_composite(im,pen)
    if lens_text:
        n=paper_rect((int(ImageDraw.Draw(im).textlength(lens_text,font=F(40,"xb")))+50,74),PAPER,True,7)
        ImageDraw.Draw(n).text((25,12),lens_text,font=F(40,"xb"),fill=(196,40,32)); im=drop(im,n,(int(cx-40),int(cy+60)),3)
    return tag(im.convert("RGB"),t,src)
# ---------- T: typed paper cards + rubber stamp (reference 0:58, 4:48) ----------
def typed(cards, stamps=(), t="", src=""):
    im=dark().convert("RGBA"); n=len(cards); cw={1:820,2:560,3:380}[n]; gap=40
    x0=(W-(n*cw+(n-1)*gap))//2; fs=56 if n<3 else 40
    for i,lines in enumerate(cards):
        ch=150+len(lines)*(fs+18); p=paper_rect((cw,ch),PAPER,False,i+5); d=ImageDraw.Draw(p)
        for j,l in enumerate(lines):
            f=F(fs-14 if j==0 else fs,"s"); 
            while d.textlength(l,font=f)>cw-60 and f.size>20: f=F(f.size-2,"s")
            d.text((34,34+j*(fs+18)),l,font=f,fill=(90,80,68) if j==0 else (30,26,22))
        ang=[-2,2,-1][i%3]; x=x0+i*(cw+gap); y=(H-ch)//2-20
        im=drop(im,p,(x,y),ang)
        if i<len(stamps) and stamps[i]:
            txt,col=stamps[i] if isinstance(stamps[i],tuple) else (stamps[i],RED)
            s=stamp(txt,col,44 if n<3 else 34); im.paste(s,(x+cw-s.width-6,y+ch-s.height+34),s)
    return tag(im.convert("RGB"),t,src)
def quote(q, who, when, t="", src="", st=""):
    im=dark().convert("RGBA"); p=paper_rect((900,330),PAPER,False,9); d=ImageDraw.Draw(p)
    ls=wrap(d,"“"+q+"”",F(46,"s"),820)[:3]
    for j,l in enumerate(ls): d.text((40,40+j*60),l,font=F(46,"s"),fill=(30,26,22))
    d.text((40,250),who.upper(),font=F(22,"b"),fill=(60,52,44)); d.text((40,282),when,font=F(20,"m"),fill=ORANGE)
    im=drop(im,p,(190,190),-1.5)
    if st: s=stamp(st,RED,38); im.paste(s,(850,440),s)
    return tag(im.convert("RGB"),t,src)
# ---------- B: split-flap board (reference 1:21) ----------
def flap(rows, header="", t="", src="", hi=None):
    im=ledger(); d=ImageDraw.Draw(im); fm=F(64,"mono")
    if header: d.text((90,90),header.upper(),font=F(18,"m"),fill=GREY)
    for i,(a,b) in enumerate(rows):
        y=170+i*120; s=f"{a:<10}{b:>8}"
        for j,ch in enumerate(s):
            x=90+j*60; d.rounded_rectangle([x,y,x+54,y+92],4,fill=(36,33,30)); d.line([x,y+46,x+54,y+46],fill=(14,12,10),width=2)
            col=ORANGE if (j>=10 or hi is None or hi==i) else (160,150,136)
            if ch!=" ": d.text((x+9,y+8),ch,font=fm,fill=col)
    return tag(im,t,src)
# ---------- K: cut-paper figures (reference 1:38) ----------
def figure(layer, x, y, s, shade):
    d=ImageDraw.Draw(layer); c=shade
    d.polygon([(x-62*s,y+150*s),(x-50*s,y+40*s),(x,y+24*s),(x+50*s,y+40*s),(x+62*s,y+150*s)],fill=(c-70,c-72,c-74,255))
    d.polygon([(x-14*s,y+26*s),(x,y+60*s),(x+14*s,y+26*s)],fill=(230,222,208,255))
    d.polygon([(x-4*s,y+34*s),(x+4*s,y+34*s),(x+6*s,y+90*s),(x,y+100*s),(x-6*s,y+90*s)],fill=(170,40,36,255))
    d.ellipse([x-30*s,y-52*s,x+30*s,y+22*s],fill=(c+60,c+50,c+36,255))
    d.polygon([(x-30*s,y-20*s),(x-26*s,y-56*s),(x+8*s,y-62*s),(x+32*s,y-34*s),(x+30*s,y-18*s)],fill=(c+40,c+32,c+20,255))
def figures(n=5, tags=(), t="", src="", hi=None, grid=False):
    im=dark().convert("RGBA"); lay=Image.new("RGBA",(W,H),(0,0,0,0))
    if grid:
        for i in range(12*6):
            x=120+(i%12)*90; y=150+(i//12)*80; figure(lay,x,y,0.35,200 if (hi and i<hi) else 110)
    else:
        for i in range(n):
            x=170+i*(940/(n-1 if n>1 else 1)); figure(lay,int(x),250+(i%2)*20,1.25,150+(i%3)*20)
    lay=lay.filter(ImageFilter.GaussianBlur(0.4)); im=drop(im,lay,(0,0),0,8)
    for i,(a,b) in enumerate(tags):
        p=paper_rect((340,120),PAPER,True,i+20); d=ImageDraw.Draw(p); d.text((20,14),a.upper(),font=F(26,"b"),fill=(40,34,28)); d.text((20,52),b,font=F(48,"xb"),fill=RED)
        im=drop(im,p,(110+i*380,500),[-2,1.5,-1][i%3],8)
    return tag(im.convert("RGB"),t,src)
# ---------- M: dark map / globe with orange arcs and pins (reference 2:29, 8:10) ----------
_S=None
def shapes():
    global _S
    if _S is None:
        r=shapefile.Reader(str(ASSETS/"ne_50m_admin_0_countries.shp")); fl=[x[0] for x in r.fields[1:]]
        _S=[(dict(zip(fl,s.record)), s.shape) for s in r.shapeRecords()]
    return _S
def map_(bbox, hi=(), pins=(), arcs=(), lanes=(), dots=(), title="", sub="", t="", src="", dotcol=ORANGE, globe=None):
    im=ledger(); d=ImageDraw.Draw(im)
    if globe:
        lon0,lat0=globe; R0=330; cx,cy=W*0.62,H*0.52
        d.ellipse([cx-R0-14,cy-R0-14,cx+R0+14,cy+R0+14],fill=(44,40,36)); d.ellipse([cx-R0,cy-R0,cx+R0,cy+R0],fill=(30,27,24))
        def P(lo,la):
            lo,la,l0,p0=map(math.radians,(lo,la,lon0,lat0))
            c=math.sin(p0)*math.sin(la)+math.cos(p0)*math.cos(la)*math.cos(lo-l0)
            if c<0: return None
            return (cx+R0*math.cos(la)*math.sin(lo-l0), cy-R0*(math.cos(p0)*math.sin(la)-math.sin(p0)*math.cos(la)*math.cos(lo-l0)))
    else:
        lo0,la0,lo1,la1=bbox
        def P(lo,la): return ((lo-lo0)/(lo1-lo0)*W,(la1-la)/(la1-la0)*H)
    for rec,shp in shapes():
        nm=rec.get("ADMIN") or rec.get("NAME"); col=ORANGE if nm in hi else LANDC
        pts=shp.points; parts=list(shp.parts)+[len(pts)]
        for a,b in zip(parts[:-1],parts[1:]):
            ring=[P(*p) for p in pts[a:b]]
            if any(q is None for q in ring): ring=[q for q in ring if q]
            if len(ring)>2: d.polygon(ring,fill=col,outline=(150,140,124))
    def arc(a,b,col=ORANGE,w=4):
        A=P(*a);B=P(*b)
        if not A or not B: return
        mx,my=(A[0]+B[0])/2,(A[1]+B[1])/2-abs(B[0]-A[0])*0.25
        pts=[((1-s)**2*A[0]+2*(1-s)*s*mx+s*s*B[0],(1-s)**2*A[1]+2*(1-s)*s*my+s*s*B[1]) for s in [i/40 for i in range(41)]]
        d.line(pts,fill=col,width=w)
    for a,b in arcs: arc(a,b)
    for (pts_,col) in lanes: d.line([P(*p) for p in pts_],fill=col,width=6)
    for (lo,la) in dots:
        q=P(lo,la)
        if q: d.ellipse([q[0]-5,q[1]-5,q[0]+5,q[1]+5],fill=dotcol)
    for (lo,la,txt) in pins:
        q=P(lo,la)
        if not q: continue
        d.ellipse([q[0]-8,q[1]-8,q[0]+8,q[1]+8],fill=RED,outline=PAPER,width=2)
        if txt:
            f=F(18,"b"); w=d.textlength(txt,font=f); d.rectangle([q[0]+14,q[1]-34,q[0]+34+w,q[1]-6],fill=PAPER,outline=RED,width=2); d.text((q[0]+24,q[1]-31),txt,font=f,fill=(30,26,22))
    d=ImageDraw.Draw(im)
    if title: d.text((70,90),title,font=F(56,"b"),fill=PAPER)
    if sub: d.text((72,160),sub,font=F(44,"s"),fill=ORANGE)
    return tag(im,t,src)
# ---------- P: part card (reference 3:15) ----------
def part(n, title, sub=""):
    im=ledger(); d=ImageDraw.Draw(im)
    d.text((620,120),f"{n:02d}" if isinstance(n,int) else n,font=F(520,"b"),fill=(34,30,27))
    d.text((92,150),f"PART {n}" if isinstance(n,int) else "",font=F(20,"m"),fill=GREY)
    d.text((86,180),title,font=F(96,"b"),fill=PAPER)
    if sub: d.text((92,300),sub,font=F(36,"s"),fill=ORANGE)
    return im
# ---------- R: receipt printer (reference 3:18-5:03) ----------
def receipt(lines, title="THE INVOICE", st=None, stcol=RED, sub="INV-007 · PER HOUSEHOLD"):
    im=dark().convert("RGBA"); d=ImageDraw.Draw(im)
    d.rounded_rectangle([260,40,1020,92],8,fill=(34,31,28)); d.text((284,56),"INV · PRINT",font=F(18,"m"),fill=GREY); d.ellipse([980,58,998,76],fill=ORANGE)
    ph=140+len(lines)*78; p=paper_rect((720,ph),PAPER,False,2); pd=ImageDraw.Draw(p); fm=F(36,"mono"); fr=F(20,"monor")
    pd.text((34,26),title,font=fm,fill=(30,26,22)); pd.text((34,72),sub,font=fr,fill=(90,82,72)); pd.line([34,106,686,106],fill=(150,140,124),width=2)
    for i,(a,b) in enumerate(lines):
        y=124+i*78; pd.text((34,y),a.upper(),font=F(26,"mono"),fill=(40,34,28))
        pd.text((686-pd.textlength(b,font=F(28,"mono")),y+32),b,font=F(28,"mono"),fill=RED)
    im=drop(im,p,(280,88),0,10)
    if st: s=stamp(st,stcol,60); im.paste(s,(300,88+ph-s.height+30),s)
    return im.convert("RGB")
# ---------- W: mini-chart tiles (reference 5:52) ----------
def tiles(items, header="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); n=len(items); tw=(W-180-(n-1)*30)//n
    if header: d.text((90,90),header.upper(),font=F(18,"m"),fill=GREY)
    for i,(label,vals,big) in enumerate(items):
        x=90+i*(tw+30); y=170; d.rectangle([x,y,x+tw,y+400],fill=(30,27,24),outline=(60,55,50))
        d.text((x+20,y+18),label.upper(),font=F(18,"b"),fill=GREY)
        d.text((x+20,y+52),big,font=F(58 if len(big)<7 else 40,"b"),fill=ORANGE if i==n-1 else PAPER)
        if vals:
            mn,mx=min(vals),max(vals); pts=[(x+20+j*(tw-40)/(max(1,len(vals)-1)), y+370-((v-mn)/(mx-mn or 1))*180) for j,v in enumerate(vals)]
            d.line(pts,fill=ORANGE,width=4)
            for q in pts: d.ellipse([q[0]-5,q[1]-5,q[0]+5,q[1]+5],fill=ORANGE)
    return tag(im,t,src)
# ---------- X: folder + index cards (reference 6:46) ----------
def folder(cards, label="INV-007", photo=None):
    im=dark().convert("RGBA")
    f=paper_rect((620,440),(170,122,72),False,4); fd=ImageDraw.Draw(f); fd.text((30,24),label,font=F(26,"mono"),fill=(60,40,20)); im=drop(im,f,(120,170),-4)
    m=map_((46,21,61,31),lanes=[([(54,26.2),(56.2,26.75),(57.2,25.9),(58.6,25.2)],ORANGE)]).resize((520,330))
    if photo and pathlib.Path(photo).exists(): m=tone(Image.open(photo)).resize((520,330))
    m=m.convert("RGBA"); im=drop(im,m,(330,140),3)
    for i,(a,b) in enumerate(cards):
        c=paper_rect((480,160),PAPER,False,30+i); cd=ImageDraw.Draw(c); cd.text((28,26),a.upper(),font=F(28,"xb"),fill=(30,26,22)); cd.text((28,64),"not financial advice" if i==0 and "DO" in a.upper() else "",font=F(16,"m"),fill=GREY)
        cd.text((28,100) if a else (28,40),b,font=F(30,"m"),fill=(40,34,28)); im=drop(im,c,(600+i*40,250+i*150),[-3,2,-1,3][i%4],10)
    return im.convert("RGB")
# ---------- E: plain logo end card (no particles) (reference 8:51) ----------
def endcard(txt="THE HISTORY INVOICE", sub="Every crisis sends a bill. History keeps the receipts."):
    # no particle assemble (Hammad 2026-11-10): plain title, fades in
    im=ledger(); d=ImageDraw.Draw(im); f=F(96,"xb"); w=d.textlength(txt,font=f)
    d.text(((W-w)/2,270),txt,font=f,fill=PAPER); d.line([W/2-60,400,W/2+60,400],fill=ORANGE,width=4)
    sw=d.textlength(sub,font=F(32,"s")); d.text(((W-sw)/2,430),sub,font=F(32,"s"),fill=ORANGE)
    return im
