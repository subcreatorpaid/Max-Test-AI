"""History Invoice graphics kit v2, part 2: one-off graphic types so the same graphic is not reused
(Hammad 2026-11-10: "use different type of graphics every time other than the chapter's main one;
repeat only for similar explanations"). Same palette, beige paper, Inter + Caladea, confidence tags."""
from kit import *

# every graphic sits on the part-card background (Hammad 2026-11-10)
def _paper_bg(col=PAPER, seed=11): return ledger()
def _cork(): return ledger()
def _slate(): return ledger()
def _title(d,title,sub="",x=86,y=70,col=PAPER):
    if title: d.text((x,y),title,font=F(52,"b"),fill=col)
    if sub: d.text((x+4,y+66),sub,font=F(34,"s"),fill=ORANGE)
def _fit(d,s,font_k,size,maxw):
    f=F(size,font_k)
    while d.textlength(s,font=f)>maxw and size>14: size-=2; f=F(size,font_k)
    return f
INKT=(30,26,22)

# 1 sea chart: beige nautical chart, hatched land, soundings, red mine marks
def seachart(bbox, marks=(), title="", sub="", t="", src="", lanes=()):
    im=_paper_bg((206,198,176)); d=ImageDraw.Draw(im); lo0,la0,lo1,la1=bbox
    def P(lo,la): return ((lo-lo0)/(lo1-lo0)*W,(la1-la)/(la1-la0)*H)
    for lo in range(int(lo0),int(lo1)+1): x=P(lo,0)[0]; d.line([x,0,x,H],fill=(44,40,36),width=1)
    for la in range(int(la0),int(la1)+1): y=P(0,la)[1]; d.line([0,y,W,y],fill=(44,40,36),width=1)
    r=random.Random(2)
    for _ in range(240): d.text((r.randrange(W),r.randrange(H)),str(r.randint(8,90)),font=F(12,"r"),fill=(70,66,60))
    land=Image.new("L",(W,H),0); ld=ImageDraw.Draw(land)
    for rec,shp in shapes():
        pts=shp.points; parts=list(shp.parts)+[len(pts)]
        for a,b in zip(parts[:-1],parts[1:]):
            ring=[P(*p) for p in pts[a:b]]
            if len(ring)>2: ld.polygon(ring,fill=255); d.line(ring+[ring[0]],fill=(150,140,124),width=2)
    hatch=Image.new("RGB",(W,H),(60,55,48)); hd=ImageDraw.Draw(hatch)
    for k in range(-H,W,9): hd.line([k,H,k+H,0],fill=(78,72,64),width=2)
    im=Image.composite(hatch,im,land); d=ImageDraw.Draw(im)
    for pts_,col in lanes: d.line([P(*p) for p in pts_],fill=col,width=3)
    for lo,la in marks:
        x,y=P(lo,la); d.ellipse([x-8,y-8,x+8,y+8],outline=RED,width=2); d.line([x-6,y-6,x+6,y+6],fill=RED,width=2); d.line([x-6,y+6,x+6,y-6],fill=RED,width=2)
    c=paper_rect((560,150),(226,214,192),False,5); cd=ImageDraw.Draw(c); cd.rectangle([8,8,551,141],outline=(110,90,64),width=3)
    cd.text((30,22),title,font=_fit(cd,title,"s",50,500),fill=INKT); cd.text((32,88),sub.upper(),font=F(20,"b"),fill=RED)
    im=drop(im.convert("RGBA"),c,(60,H-210),0,8)
    return tag(im.convert("RGB"),t,src)

# 2 timeline: dates on a line, paper flags, outcome stamps
def timeline(events, title="", t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title)
    y0=360; d.line([80,y0,W-80,y0],fill=ORANGE,width=5); n=len(events); step=(W-460)/max(1,n-1)
    for i,(date,label,st) in enumerate(events):
        x=int(230+i*step); d.ellipse([x-12,y0-12,x+12,y0+12],fill=ORANGE)
        d.text((x-d.textlength(date,font=F(34,"b"))/2,y0-70),date,font=F(34,"b"),fill=PAPER)
        p=paper_rect((300,110),PAPER,True,i+3); pd=ImageDraw.Draw(p); pd.text((20,20),label,font=_fit(pd,label,"s",36,260),fill=INKT)
        im=drop(im,p,(x-150,y0+40),[-2,1,-1][i%3],8)
        if st: s=stamp(st,RED,26,-6); im.paste(s,(x-s.width//2,y0+150),s)
    return tag(im.convert("RGB"),t,src)

# 3 ticket: perforated passage ticket
def ticket(head, big, lines=(), st="", t="", src=""):
    im=dark().convert("RGBA"); w,h=900,380; p=paper_rect((w,h),PAPER,False,8); pd=ImageDraw.Draw(p)
    for cy in (0,h): pd.ellipse([640-26,cy-26,640+26,cy+26],fill=(0,0,0,0))
    for y in range(20,h-20,18): pd.line([640,y,640,y+9],fill=(120,110,96),width=3)
    pd.text((40,34),head.upper(),font=F(24,"mono"),fill=(90,80,68)); pd.text((40,90),big,font=_fit(pd,big,"mono",76,580),fill=RED)
    for j,l in enumerate(lines): pd.text((40,200+j*44),l,font=F(28,"monor"),fill=INKT)
    pd.text((670,60),"ADMIT",font=F(30,"mono"),fill=(90,80,68)); pd.text((670,110),"ONE",font=F(54,"mono"),fill=INKT); pd.text((670,180),"SHIP",font=F(54,"mono"),fill=INKT)
    im=drop(im,p,(190,170),-3)
    if st: s=stamp(st,RED,46,-12); im.paste(s,(700,430),s)
    return tag(im.convert("RGB"),t,src)

# 4 horizontal bars
def bars(rows, title="", sub="", t="", src="", hi=None):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title,sub)
    mx=max(v for _,v,_ in rows)
    for i,(lab,v,txt) in enumerate(rows):
        y=260+i*130; d.text((90,y+20),lab.upper(),font=F(26,"b"),fill=GREY)
        L=int(max(16,(W-560)*v/mx)); c=ORANGE if (hi==i or (hi is None and v==mx)) else PAPER
        bar=paper_rect((L,70),c,True,i+40); im=drop(im,bar,(380,y),0,6); d=ImageDraw.Draw(im)
        d.text((400+L,y+8),txt,font=F(48,"b"),fill=c)
    return tag(im.convert("RGB"),t,src)

# 5 envelope: next invoice
def envelope(title, sub="", kicker="NEXT INVOICE"):
    im=dark().convert("RGBA"); e=paper_rect((760,440),(176,134,86),False,6); ed=ImageDraw.Draw(e)
    ed.polygon([(0,0),(380,250),(760,0)],fill=(158,118,74)); ed.line([(0,0),(380,250),(760,0)],fill=(120,86,52),width=3)
    ed.ellipse([340,210,420,290],fill=ORANGE); ed.text((360,232),"HI",font=F(28,"xb"),fill=(120,40,10))
    lab=paper_rect((560,130),PAPER,False,3); ld=ImageDraw.Draw(lab); ld.text((24,16),kicker,font=F(22,"mono"),fill=RED)
    ld.text((24,52),title,font=_fit(ld,title,"s",40,510),fill=INKT); e.paste(lab,(100,295),lab)
    im=drop(im,e,(260,120),-2); d=ImageDraw.Draw(im)
    if sub: d.text((W/2-d.textlength(sub,font=F(30,"b"))/2,612),sub,font=F(30,"b"),fill=ORANGE)
    return im.convert("RGB")

# 6 balance scale
def scale(left, right, title="", t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title)
    cx,cy=W//2,250; tilt=70
    d.polygon([(cx-60,640),(cx+60,640),(cx+12,cy),(cx-12,cy)],fill=(70,62,54)); d.line([cx-330,cy-tilt+140,cx+330,cy+tilt],fill=PAPER,width=10)
    d.ellipse([cx-18,cy+40,cx+18,cy+76],fill=ORANGE)
    for (lab,val,col),(x,y) in ((left,(cx-330,cy+70)),(right,(cx+330,cy+tilt))):
        d.line([x,y,x-90,y+150],fill=GREY,width=3); d.line([x,y,x+90,y+150],fill=GREY,width=3)
        p=paper_rect((300,130),PAPER,False,len(lab)); pd=ImageDraw.Draw(p); pd.text((18,14),lab.upper(),font=_fit(pd,lab.upper(),"b",22,270),fill=(80,70,60))
        pd.text((18,52),val,font=_fit(pd,val,"xb",54,270),fill=col); im=drop(im,p,(x-150,y+150),0,8); d=ImageDraw.Draw(im)
    return tag(im.convert("RGB"),t,src)

# 7 checklist with ticks/crosses
def checklist(title, items, hi=None, t="", src="", st=""):
    im=dark().convert("RGBA"); p=paper_rect((820,560),PAPER,False,12); pd=ImageDraw.Draw(p)
    pd.text((50,36),title,font=F(38,"s"),fill=INKT); pd.line([50,96,770,96],fill=(150,140,124),width=2)
    for i,(txt,ok) in enumerate(items):
        y=130+i*96; pd.rectangle([50,y,96,y+46],outline=(60,52,44),width=3)
        if ok: pd.line([(58,y+24),(72,y+38),(94,y+4)],fill=GREEN,width=7)
        else: pd.line([58,y+8,90,y+40],fill=RED,width=7); pd.line([58,y+40,90,y+8],fill=RED,width=7)
        pd.text((120,y+4),txt,font=F(34,"m"),fill=INKT)
        if hi==i:
            w=pd.textlength(txt,font=F(34,"m"))
            for k in range(3): pd.ellipse([100-k*3,y-16+k*2,140+w+k*2,y+62-k],outline=(196,40,32),width=4)
    im=drop(im,p,(230,90),-1.5)
    if st: s=stamp(st,RED,46); im.paste(s,(800,520),s)
    return tag(im.convert("RGB"),t,src)

# 8 speech bubbles
def bubbles(items, header="", t="", src=""):
    im=dark().convert("RGBA"); d=ImageDraw.Draw(im)
    if header: d.text((90,70),header.upper(),font=F(22,"m"),fill=GREY)
    for i,(who,txt) in enumerate(items):
        x=90+i*580; y=170+(i%2)*60; w,h=520,300
        b=Image.new("RGBA",(w,h+60),(0,0,0,0)); bp=paper_rect((w,h),PAPER,False,i+60); b.paste(bp,(0,0),bp)
        bd=ImageDraw.Draw(b); bd.polygon([(80,h-2),(150,h-2),(70,h+56)],fill=PAPER+(255,))
        for j,l in enumerate(wrap(bd,"“"+txt+"”",F(44,"s"),460)[:4]): bd.text((30,34+j*58),l,font=F(44,"s"),fill=INKT)
        im=drop(im,b,(x,y),[-2,2][i%2],10); d=ImageDraw.Draw(im); d.text((x+60,y+h+90),who.upper(),font=F(28,"b"),fill=ORANGE)
    return tag(im.convert("RGB"),t,src)

# 9 progress bar that stops
def progress(title, sub, frac, left="", st="PAUSED", t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title,sub,y=120)
    x0,x1,y=90,W-90,380; d.rounded_rectangle([x0,y,x1,y+70],12,fill=(36,33,30),outline=(70,64,58),width=2)
    d.rounded_rectangle([x0+6,y+6,x0+6+(x1-x0-12)*frac,y+64],10,fill=ORANGE)
    for k in range(0,int((x1-x0-12)*frac),28): d.line([x0+6+k,y+64,x0+26+k,y+6],fill=(250,140,70),width=6)
    if left: d.text((x0,y+92),left,font=F(28,"m"),fill=GREY)
    if st: s=stamp(st,RED,72,-10); im.paste(s,(int(x0+(x1-x0)*frac)-60,y-60),s)
    return tag(im.convert("RGB"),t,src)

# 10 notebook page (handwritten note)
def notebook(text, who, when, t="", src=""):
    im=dark().convert("RGBA"); w,h=820,560; p=paper_rect((w,h),PAPER,False,14); pd=ImageDraw.Draw(p)
    for y in range(110,h,52): pd.line([0,y,w,y],fill=(150,170,190),width=2)
    pd.line([90,0,90,h],fill=(200,90,80),width=3)
    for x in range(60,w,70): pd.ellipse([x,14,x+22,36],fill=(24,20,17))
    for j,l in enumerate(wrap(pd,"“"+text+"”",F(48,"s"),690)[:5]): pd.text((110,64+j*52),l,font=F(48,"s"),fill=(30,40,90))
    pd.text((110,h-104),"— "+who,font=F(24,"b"),fill=INKT); pd.text((110,h-68),when,font=F(22,"m"),fill=ORANGE)
    im=drop(im,p,(230,90),2)
    return tag(im.convert("RGB"),t,src)

# 11 mechanical counter
def odometer(digits, title, sub="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); n=len(digits); cw=150; x0=(W-n*cw-20)//2; y=230
    d.rounded_rectangle([x0-30,y-30,x0+n*cw+10,y+250],18,fill=(54,50,46),outline=(110,100,90),width=4)
    for i,ch in enumerate(digits):
        x=x0+i*cw; d.rounded_rectangle([x,y,x+cw-20,y+190],8,fill=(232,224,210) if ch!="?" else (36,33,30))
        d.line([x,y+95,x+cw-20,y+95],fill=(0,0,0),width=2)
        f=F(150,"mono"); d.text((x+(cw-20-d.textlength(ch,font=f))/2,y+8),ch,font=f,fill=ORANGE if ch=="?" else INKT)
    d.text((W/2-d.textlength(title,font=F(54,"b"))/2,530),title,font=F(54,"b"),fill=PAPER)
    if sub: d.text((W/2-d.textlength(sub,font=F(36,"s"))/2,600),sub,font=F(36,"s"),fill=ORANGE)
    return tag(im,t,src)

# 12 tear-off calendar pages
def calendar(pages, title="", t="", src=""):
    im=dark().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title)
    n=len(pages); cw=320; gap=50; x0=(W-(n*cw+(n-1)*gap))//2
    for i,(mon,big,sub) in enumerate(pages):
        p=paper_rect((cw,380),PAPER,False,i+70); pd=ImageDraw.Draw(p); pd.rectangle([0,0,cw,90],fill=RED)
        for k in range(6): pd.ellipse([30+k*48,10,44+k*48,24],fill=(24,20,17))
        pd.text(((cw-pd.textlength(mon,font=F(44,"xb")))/2,30),mon,font=F(44,"xb"),fill=PAPER)
        f=_fit(pd,big,"b",96,cw-30); pd.text(((cw-pd.textlength(big,font=f))/2,130),big,font=f,fill=INKT)
        pd.text(((cw-pd.textlength(sub,font=F(28,"s")))/2,280),sub,font=F(28,"s"),fill=ORANGE)
        im=drop(im,p,(x0+i*(cw+gap),190),[-3,1,3][i%3],12)
    return tag(im.convert("RGB"),t,src)

# 13 chalk tally board
def tally(groups, title="", t="", src=""):
    im=_slate(); d=ImageDraw.Draw(im); _title(d,title,col=(230,230,220)); chalk=(228,226,214)
    r=random.Random(5)
    for gi,(lab,n,show,col) in enumerate(groups):
        y=200+gi*150; d.text((80,y+30),lab.upper(),font=F(28,"b"),fill=col)
        for k in range(min(n,45)):
            g,j=divmod(k,5); x=330+g*84+j*14
            if j<4: d.line([x+r.randint(-1,1),y+10,x+r.randint(-2,2),y+90],fill=col,width=4)
            else: d.line([x-60,y+80,x+6,y+20],fill=col,width=4)
        d.text((W-250,y+10),show,font=F(84,"b"),fill=col)
    return tag(im,t,src)

# 14 monthly columns
def columns(labels, vals, hi=None, title="", sub="", t="", src="", note=""):
    im=ledger(); d=ImageDraw.Draw(im); _title(d,title,sub)
    n=len(vals); bw=min(260,(W-200)//n); mx=max(vals); base=620
    for i,(lab,v) in enumerate(zip(labels,vals)):
        x=(W-n*bw)//2+i*bw; h=int(300*v/mx); c=RED if i==hi else (90,82,72)
        d.rectangle([x+14,base-h,x+bw-14,base],fill=c); d.text((x+bw/2-d.textlength(lab,font=F(22,"b"))/2,base+14),lab,font=F(22,"b"),fill=GREY)
        v_=str(v); d.text((x+bw/2-d.textlength(v_,font=F(64,"b"))/2,base-h-80),v_,font=F(64,"b"),fill=RED if i==hi else PAPER)
        if i==hi and note: d.text((x+bw/2-d.textlength(note,font=F(30,"s"))/2,base-h-120),note,font=F(30,"s"),fill=ORANGE)
    return tag(im,t,src)

# 15 fleet silhouettes with fire
def fleet(ships, title="", sub="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.line([0,472,W,472],fill=(60,55,50),width=2); _title(d,title,sub)
    n=len(ships); step=(W-160)/n
    for i,(kind,fire) in enumerate(ships):
        x=int(80+i*step); s=1.0 if kind=="tanker" else 0.55; L=int(170*s); y=470
        d.polygon([(x,y-30*s),(x+L,y-30*s),(x+L-14*s,y),(x+12*s,y)],fill=(96,90,82)); d.rectangle([x+L-44*s,y-62*s,x+L-16*s,y-30*s],fill=(96,90,82))
        if fire:
            fl=Image.new("RGBA",(W,H),(0,0,0,0)); fd=ImageDraw.Draw(fl); cx=x+L//2
            fd.ellipse([cx-60,y-150,cx+60,y-10],fill=ORANGE+(150,)); fd.ellipse([cx-30,y-110,cx+30,y-20],fill=(255,190,80,220))
            fl=fl.filter(ImageFilter.GaussianBlur(14)); im=Image.alpha_composite(im.convert("RGBA"),fl).convert("RGB"); d=ImageDraw.Draw(im)
        d.text((x,y+30),"TUG" if kind!="tanker" else f"TANKER {i+1}",font=F(18,"b"),fill=GREY)
    return tag(im,t,src)

# 16 official notice with seal
def notice(org, head, body, st="", t="", src=""):
    im=dark().convert("RGBA"); w,h=760,600; p=paper_rect((w,h),PAPER,False,16); pd=ImageDraw.Draw(p)
    pd.ellipse([w/2-46,30,w/2+46,122],outline=ORANGE,width=6); pd.ellipse([w/2-30,46,w/2+30,106],outline=ORANGE,width=2)
    pd.text(((w-pd.textlength(org.upper(),font=F(22,"b")))/2,140),org.upper(),font=F(22,"b"),fill=(80,70,60))
    pd.text(((w-pd.textlength(head,font=F(48,"s")))/2,190),head,font=_fit(pd,head,"s",48,w-80),fill=INKT); pd.line([60,262,w-60,262],fill=(150,140,124),width=2)
    for j,l in enumerate(wrap(pd,body,F(30,"m"),w-120)[:5]): pd.text((60,290+j*44),l,font=F(30,"m"),fill=INKT)
    for k in range(4): pd.line([60,h-110+k*20,w-60-k*90,h-110+k*20],fill=(170,160,144),width=6)
    im=drop(im,p,(260,60),1.5)
    if st: s=stamp(st,RED,52,-10); im.paste(s,(700,430),s)
    return tag(im.convert("RGB"),t,src)

# 17 newspaper clipping
def clipping(masthead, headline, sub="", date="", hi_line=True, t="", src=""):
    im=dark().convert("RGBA"); w,h=880,560; p=paper_rect((w,h),(214,206,190),True,17); pd=ImageDraw.Draw(p)
    pd.text((40,24),masthead.upper(),font=F(26,"s"),fill=(60,52,44)); pd.text((w-40-pd.textlength(date,font=F(20,"m")),30),date,font=F(20,"m"),fill=(90,80,68))
    pd.line([40,66,w-40,66],fill=INKT,width=3)
    hl=wrap(pd,headline,F(54,"b"),w-80)[:2]
    for j,l in enumerate(hl):
        if hi_line and j==0: pd.rectangle([36,84,44+pd.textlength(l,font=F(54,"b")),146],fill=(236,170,120))
        pd.text((40,84+j*64),l,font=F(54,"b"),fill=INKT)
    y=100+len(hl)*64; pd.text((40,y),sub,font=F(28,"s"),fill=(70,60,50))
    r=random.Random(9)
    for col in range(3):
        for k in range(8): x=40+col*275; yy=y+60+k*26; pd.line([x,yy,x+r.randint(180,250),yy],fill=(150,142,128),width=6)
    im=drop(im,p,(200,90),-2.5)
    return tag(im.convert("RGB"),t,src)

# 18 cork pinboard
def pinboard(cards, pinst="", t="", src=""):
    im=_cork().convert("RGBA"); n=len(cards); pos=[]
    for i,lines in enumerate(cards):
        w=520 if n==1 else 420; h=110+len(lines)*62; p=paper_rect((w,h),PAPER,False,i+80); pd=ImageDraw.Draw(p)
        for j,l in enumerate(lines): pd.text((30,40+j*62),l,font=_fit(pd,l,"s" if j else "b",44 if j else 26,w-60),fill=INKT if j else (90,80,68))
        x=(W-w)//2 if n==1 else 150+i*560; y=170; im=drop(im,p,(x,y),[-3,2][i%2],10); pos.append((x+w//2,y+18))
    d=ImageDraw.Draw(im)
    for x,y in pos: d.ellipse([x-16,y-16,x+16,y+16],fill=RED); d.ellipse([x-6,y-10,x+2,y-2],fill=(240,140,140))
    if pinst: s=stamp(pinst,RED,64,-8); im.paste(s,(760,470),s)
    return tag(im.convert("RGB"),t,src)

# 19 film strip with a year
def filmyear(year, sub, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im)
    d.rectangle([0,140,W,580],fill=(14,12,10))
    for x in range(10,W,60): d.rounded_rectangle([x,158,x+34,184],4,fill=(40,36,32)); d.rounded_rectangle([x,536,x+34,562],4,fill=(40,36,32))
    for i in range(3): d.rectangle([60+i*400,210,420+i*400,510],fill=(46,40,32) if i!=1 else (70,58,40))
    f=F(220,"bebas"); d.text((W/2-d.textlength(year,font=f)/2,232),year,font=f,fill=PAPER)
    d.text((W/2-d.textlength(sub,font=F(40,"s"))/2,610),sub,font=F(40,"s"),fill=ORANGE)
    return tag(im,t,src)

# 20 versus split
def versus(a, b, title="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.line([W//2,180,W//2,H-60],fill=(60,55,50),width=2); _title(d,title)
    mx=max(a[1],b[1])
    for i,(lab,v) in enumerate((a,b)):
        x=W//4+i*W//2; h=int(340*v/mx); c=ORANGE if v==mx else PAPER
        d.rectangle([x-70,620-h,x+70,620],fill=c); d.text((x-d.textlength(str(v),font=F(80,"b"))/2,620-h-100),str(v),font=F(80,"b"),fill=c)
        d.text((x-d.textlength(lab,font=F(34,"b"))/2,640),lab,font=F(34,"b"),fill=GREY)
    d.text((W/2-30,320),"vs",font=F(48,"s"),fill=ORANGE)
    return tag(im,t,src)

# 21 bronze plaque
def plaque(lines, t="", src=""):
    im=dark(); w,h=820,440; x0,y0=(W-w)//2,(H-h)//2
    p=Image.new("RGB",(w,h)); pd=ImageDraw.Draw(p)
    for y in range(h): c=int(110+60*math.sin(y/h*math.pi)); pd.line([0,y,w,y],fill=(c+40,c,int(c*0.45)))
    pd.rectangle([14,14,w-15,h-15],outline=(80,56,24),width=6)
    for cx,cy in ((34,34),(w-34,34),(34,h-34),(w-34,h-34)): pd.ellipse([cx-8,cy-8,cx+8,cy+8],fill=(90,64,30))
    for j,(txt,sz) in enumerate(lines):
        f=F(sz,"s" if j==0 else "b"); y=60+sum(l[1]+30 for l in lines[:j])
        pd.text(((w-pd.textlength(txt,font=f))/2+2,y+2),txt,font=f,fill=(70,48,20)); pd.text(((w-pd.textlength(txt,font=f))/2,y),txt,font=f,fill=(240,214,150))
    im.paste(p,(x0,y0)); return tag(im,t,src)

# 22 ruler with a legal limit
def limitbar(limit, actual, maxv, unit, title="", sub="", t="", src="", labels=("Legal limit","Some crews")):
    im=ledger(); d=ImageDraw.Draw(im); _title(d,title,sub); x0,x1=100,W-100; y=360
    def X(v): return x0+(x1-x0)*v/maxv
    d.rectangle([x0,y,x1,y+60],fill=(214,204,186))
    for m in range(maxv+1):
        d.line([X(m),y,X(m),y+(30 if m%3==0 else 16)],fill=INKT,width=3)
        if m%3==0: d.text((X(m)-10,y+70),str(m),font=F(22,"b"),fill=GREY)
    d.rectangle([x0,y+250,X(actual),y+300],fill=ORANGE); lab=f"{actual} {unit}"; d.text((X(actual)-d.textlength(lab,font=F(40,"b")),y+190),lab,font=F(40,"b"),fill=ORANGE)
    d.text((x0,y+214),labels[1].upper(),font=F(22,"b"),fill=GREY)
    for k in range(y-40,y+330,22): d.line([X(limit),k,X(limit),k+12],fill=RED,width=5)
    d.text((X(limit)+12,y-48),f"{labels[0]} · {limit} {unit}",font=F(30,"b"),fill=RED)
    return tag(im,t,src)

# 23 two clipboards that disagree
def clipboards(a, b, t="", src=""):
    im=dark().convert("RGBA")
    for i,(who,txt) in enumerate((a,b)):
        cb=Image.new("RGBA",(440,520),(0,0,0,0)); cd=ImageDraw.Draw(cb); cd.rounded_rectangle([0,0,439,519],18,fill=(120,86,52,255))
        p=paper_rect((380,440),PAPER,False,i+90); pd=ImageDraw.Draw(p); pd.text((24,60),who.upper(),font=F(24,"b"),fill=(90,80,68))
        for j,l in enumerate(wrap(pd,txt,F(46,"s"),330)[:4]): pd.text((24,110+j*58),l,font=F(46,"s"),fill=INKT)
        cb.paste(p,(30,50),p); cd.rounded_rectangle([150,20,290,70],10,fill=(150,150,150,255))
        im=drop(im,cb,(130+i*580,110),[-3,3][i],12)
    d=ImageDraw.Draw(im); d.text((W/2-30,300),"≠",font=F(110,"b"),fill=ORANGE)
    return tag(im.convert("RGB"),t,src)

# 24 letterhead with highlighted line
def letter(org, quote_, who, when, t="", src=""):
    im=dark().convert("RGBA"); w,h=820,600; p=paper_rect((w,h),PAPER,False,24); pd=ImageDraw.Draw(p)
    pd.rectangle([0,0,w,80],fill=NAVY); pd.text((40,22),org.upper(),font=F(30,"b"),fill=PAPER); pd.text((w-220,30),"PRESS STATEMENT",font=F(18,"m"),fill=(180,190,210))
    for k in range(3): pd.line([50,120+k*30,w-60-k*80,120+k*30],fill=(176,166,150),width=6)
    ls=wrap(pd,"“"+quote_+"”",F(40,"s"),w-110)[:4]
    for j,l in enumerate(ls):
        y=230+j*54; pd.rectangle([46,y-4,54+pd.textlength(l,font=F(40,"s")),y+46],fill=(236,170,120)); pd.text((50,y),l,font=F(40,"s"),fill=INKT)
    pd.text((50,h-90),who.upper(),font=F(22,"b"),fill=(60,52,44)); pd.text((50,h-56),when,font=F(20,"m"),fill=ORANGE)
    im=drop(im,p,(230,60),-1.5)
    return tag(im.convert("RGB"),t,src)

# 25 two-step stairs
def steps(items, title="", t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title); n=len(items); sw=(W-200)//n
    for i,(lab,txt) in enumerate(items):
        x=100+i*sw; top=560-(i+1)*150
        d.rectangle([x,top,x+sw-20,600],fill=(60,54,48) if i<n-1 else ORANGE)
        d.text((x+24,top+20),lab.upper(),font=F(40,"xb"),fill=PAPER if i<n-1 else INKT)
        d.text((x+24,top+76),txt,font=_fit(d,txt,"s",40,sw-60),fill=ORANGE if i<n-1 else INKT)
        if i<n-1: d.line([x+sw-80,top-60,x+sw+30,top-120],fill=ORANGE,width=5); d.polygon([(x+sw+30,top-120),(x+sw+4,top-120),(x+sw+22,top-96)],fill=ORANGE)
    return tag(im.convert("RGB"),t,src)

# 26 cost flow chain
def flow(nodes, title="", sub="", t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title,sub); n=len(nodes); bw=230; gap=(W-180-n*bw)//max(1,n-1)
    for i,(a,b) in enumerate(nodes):
        x=90+i*(bw+gap); y=320; last=i==n-1
        p=paper_rect((bw,160),ORANGE if last else PAPER,False,i+100); pd=ImageDraw.Draw(p)
        pd.text((20,24),a.upper(),font=_fit(pd,a.upper(),"xb",32,bw-40),fill=INKT); pd.text((20,84),b,font=_fit(pd,b,"s",30,bw-40),fill=(60,40,20) if last else ORANGE)
        im=drop(im,p,(x,y),0,8); d=ImageDraw.Draw(im)
        if not last:
            ax=x+bw+10; d.line([ax,y+80,ax+gap-20,y+80],fill=ORANGE,width=6); d.polygon([(ax+gap-20,y+68),(ax+gap-4,y+80),(ax+gap-20,y+92)],fill=ORANGE)
            d.ellipse([ax+gap/2-22,y+20,ax+gap/2+22,y+64],fill=(214,170,60),outline=(150,110,30),width=3)
    return tag(im.convert("RGB"),t,src)

# 27 fuel pump display
def pump(value, sub, label="WAR INSURANCE", t="", src=""):
    im=dark(); d=ImageDraw.Draw(im); x0,y0=300,90
    d.rounded_rectangle([x0,y0,x0+680,y0+520],24,fill=(150,30,28)); d.rounded_rectangle([x0+40,y0+40,x0+640,y0+300],12,fill=(14,14,12))
    d.text((x0+70,y0+60),label,font=F(22,"mono"),fill=(120,110,90)); f=F(130,"mono")
    d.text((x0+340-d.textlength(value,font=f)/2,y0+110),value,font=f,fill=ORANGE)
    d.rounded_rectangle([x0+40,y0+330,x0+640,y0+480],12,fill=PAPER)
    for j,l in enumerate(wrap(d,sub,F(30,"s"),560)[:3]): d.text((x0+66,y0+350+j*40),l,font=F(30,"s"),fill=INKT)
    return tag(im,t,src)

# 28 hanging price tags
def pricetags(items, title="", t="", src=""):
    im=dark().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title); n=len(items); step=(W-160)//n
    for i,(name,val) in enumerate(items):
        x=80+i*step+20; y=230+(i%2)*40; w=step-60
        tg=Image.new("RGBA",(w,300),(0,0,0,0)); td=ImageDraw.Draw(tg)
        td.polygon([(0,40),(40,0),(w,0),(w,300),(0,300)],fill=PAPER+(255,)); td.ellipse([24,24,48,48],fill=(24,20,17))
        td.text((24,80),name.upper(),font=_fit(td,name.upper(),"b",26,w-40),fill=(80,70,60)); td.text((24,140),val,font=_fit(td,val,"xb",64,w-40),fill=RED if i==n-1 else INKT)
        d.line([x+36,y+36,x+36+30,y-120],fill=(200,190,170),width=3); im=drop(im,tg,(x,y),[-6,4,-3][i%3],8); d=ImageDraw.Draw(im)
    return tag(im.convert("RGB"),t,src)

# 29 roadmap with numbered stops
def roadmap(stops, title="", t="", src=""):
    im=_paper_bg((200,190,168),29).convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title)
    pts=[(160,560),(420,380),(720,520),(1060,300)]
    for k in range(60):
        s=k/59; i=min(int(s*3),2); u=s*3-i; a,b=pts[i],pts[i+1]
        if k%2==0: x=a[0]+(b[0]-a[0])*u; y=a[1]+(b[1]-a[1])*u; d.ellipse([x-5,y-5,x+5,y+5],fill=GREY)
    for i,((x,y),lab) in enumerate(zip(pts,stops)):
        d.ellipse([x-34,y-34,x+34,y+34],fill=ORANGE if i==len(stops)-1 else (70,64,58)); d.text((x-12,y-24),str(i+1),font=F(40,"b"),fill=PAPER)
        d.text((x-d.textlength(lab,font=F(30,"b"))/2,y+44),lab,font=F(30,"b"),fill=PAPER)
    return tag(im.convert("RGB"),t,src)

# 30 contact cards
def contacts(cards, title="", t="", src=""):
    im=dark().convert("RGBA"); d=ImageDraw.Draw(im); _title(d,title)
    for i,(name,line) in enumerate(cards):
        p=paper_rect((620,250),PAPER,False,i+110); pd=ImageDraw.Draw(p); pd.rectangle([0,0,18,250],fill=ORANGE)
        for j,l in enumerate(wrap(pd,name,F(40,"b"),560)[:2]): pd.text((50,40+j*50),l,font=F(40,"b"),fill=INKT)
        pd.text((50,170),line,font=F(26,"s"),fill=(90,80,68)); im=drop(im,p,(120+i*480,220+i*70),[-3,3][i%2],12)
    return tag(im.convert("RGB"),t,src)

# 31 comment prompt
def comment(prompt, hint, t="", src=""):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im)
    for j,l in enumerate(wrap(d,prompt,F(56,"b"),W-200)[:2]): d.text((100,110+j*70),l,font=F(56,"b"),fill=PAPER)
    p=paper_rect((1040,190),PAPER,False,31); pd=ImageDraw.Draw(p); pd.ellipse([30,40,110,120],fill=ORANGE)
    pd.text((140,46),hint,font=F(40,"s"),fill=(120,110,96)); pd.line([140,110,520,110],fill=INKT,width=3); pd.line([520,40,520,100],fill=INKT,width=4)
    pd.rounded_rectangle([830,120,1010,172],10,fill=INKT); pd.text((862,130),"COMMENT",font=F(24,"b"),fill=PAPER)
    im=drop(im,p,(120,360),0,10)
    return tag(im.convert("RGB"),t,src)
