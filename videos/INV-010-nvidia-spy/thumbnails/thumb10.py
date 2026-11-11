import sys, math, pathlib; sys.path.insert(0,'/mnt/project-files/the-history-invoice/tools/inv006')
import anim6 as A
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageOps, ImageChops
ST=pathlib.Path('/tmp/claude-0/-home-claude/7e045e12-b471-584a-ab50-135e58b3397c/scratchpad/repos/Max-Test-AI/videos/INV-006-photos/storyboard/stills')
W,H=1920,1080
TOP=sys.argv[1] if len(sys.argv)>1 else '$400B'; BAN=sys.argv[2] if len(sys.argv)>2 else 'ONE DINNER?'; OUT=sys.argv[3] if len(sys.argv)>3 else 'r2.jpg'
def font(sz): return A.ImageFont.truetype(A.F_INTER, sz)

# --- map (right side), bluish like the reference
bbox=(78,-4,140,44); lon0,lat0,lon1,lat1=bbox
P=lambda lo,la: ((lo-lon0)/(lon1-lon0)*W, (lat1-la)/(lat1-lat0)*H)
m=Image.new('RGB',(W,H),(8,24,40)); d=ImageDraw.Draw(m)
iran=Image.new('L',(W,H),0); di=ImageDraw.Draw(iran)
qat=Image.new('L',(W,H),0); dq=ImageDraw.Draw(qat)
for rec,shp in A.shapes():
    nm=rec.get('ADMIN') or rec.get('NAME'); pts=shp.points; parts=list(shp.parts)+[len(pts)]
    for a,b in zip(parts[:-1],parts[1:]):
        r=[P(*p) for p in pts[a:b]]
        if len(r)<3: continue
        d.polygon(r,fill=(34,56,76),outline=(100,135,160))
        if nm in ('China',): di.polygon(r,fill=255)
        if nm in ('Taiwan','Malaysia','Singapore'): dq.polygon(r,fill=255)
# relief-ish texture
n=Image.effect_noise((W//4,H//4),40).resize((W,H),Image.BICUBIC).convert('RGB')
m=Image.blend(m,ImageChops.multiply(m,ImageOps.autocontrast(n)),0.25)
# cool haze at top
hz=Image.new('L',(W,H),0); ImageDraw.Draw(hz).rectangle([0,0,W,H*0.22],fill=120); m.paste((80,130,175),(0,0),hz.filter(ImageFilter.GaussianBlur(160)))
# iran: dark red fill with texture, glowing outline
fill=Image.new('RGB',(W,H),(110,10,4)); fill=Image.blend(fill,ImageChops.multiply(Image.new('RGB',(W,H),(255,110,30)),ImageOps.autocontrast(n)),0.55)
emb=Image.effect_noise((W//3,H//3),90).resize((W,H),Image.BICUBIC).point(lambda v:255 if v>175 else int(v*0.3)).filter(ImageFilter.GaussianBlur(4)); fill.paste((255,95,20),(0,0),emb)
core=iran.filter(ImageFilter.MinFilter(41)).filter(ImageFilter.GaussianBlur(60)); fill.paste((230,60,10),(0,0),core.point(lambda v:int(v*0.7)))
m.paste(fill,(0,0),iran)
edge=ImageChops.subtract(iran.filter(ImageFilter.MaxFilter(9)),iran.filter(ImageFilter.MinFilter(5)))
m.paste((255,45,15),(0,0),edge.filter(ImageFilter.GaussianBlur(32)).point(lambda v:min(255,v*5)))
m.paste((255,90,30),(0,0),edge.filter(ImageFilter.GaussianBlur(8)).point(lambda v:min(255,v*3)))
m.paste((255,200,150),(0,0),edge.filter(ImageFilter.GaussianBlur(1.5)))
# qatar small orange glow (the gas)
m.paste((255,150,40),(0,0),qat.filter(ImageFilter.MaxFilter(21)).filter(ImageFilter.GaussianBlur(20)).point(lambda v:min(255,v*3)))
m.paste((255,220,160),(0,0),qat)

# --- photo (left): LNG carrier, cold grade
PHOTO=sys.argv[4] if len(sys.argv)>4 else '';_x=('/tmp/claude-0/-home-claude/7e045e12-b471-584a-ab50-135e58b3397c/scratchpad/repos/Max-Test-AI/videos/INV-006-thumb/storyboard/stills')
src=Image.open(PHOTO).convert('RGB')                # 1280x853, tanker heading right under clouds
k=0.86; src=src.resize((int(src.width*1280/src.width*k),int(src.height*1280/src.width*k)),Image.LANCZOS); sw,sh_=src.size
PX,PY=-90,1080-sh_-40
p=Image.new('RGB',(int(W*0.62),H))
skyband=src.crop((0,0,sw,170)).transpose(Image.FLIP_TOP_BOTTOM).resize((sw,PY+220),Image.BICUBIC).filter(ImageFilter.GaussianBlur(2))
p.paste(skyband,(PX,0))
fm=Image.new('L',(sw,sh_),255); ImageDraw.Draw(fm).rectangle([0,0,sw,60],fill=0); fm=fm.filter(ImageFilter.GaussianBlur(45))
p.paste(src,(PX,PY),fm)
p.paste(src.crop((0,sh_-41,sw,sh_)).transpose(Image.FLIP_TOP_BOTTOM),(PX,PY+sh_))
rt=p.crop((PX+sw-60,0,PX+sw-1,H)).resize((p.size[0]-(PX+sw-60),H)); p.paste(rt,(PX+sw-60,0))
# moodier, cooler, more contrast like the reference
p=ImageEnhance.Color(p).enhance(1.15); p=Image.blend(p,Image.new('RGB',p.size,(30,70,120)),0.18)
p=ImageEnhance.Contrast(p).enhance(1.3); p=ImageEnhance.Brightness(p).enhance(0.95)
# union flag, waving, top-left
def usflag(w,h):
    f=Image.new('RGB',(w,h),'white'); d=ImageDraw.Draw(f)
    for i in range(13):
        if i%2==0: d.rectangle([0,i*h/13,w,(i+1)*h/13],fill=(178,34,52))
    d.rectangle([0,0,w*0.4,h*7/13],fill=(60,59,110))
    for r in range(9):
        for c in range(6 if r%2==0 else 5):
            x=w*0.4*(c+ (0.5 if r%2 else 0) +0.5)/6.2; y=h*7/13*(r+0.6)/9.4; d.ellipse([x-6,y-6,x+6,y+6],fill='white')
    return f
def union(w,h):
    f=Image.new('RGB',(w,h),(1,33,105)); d=ImageDraw.Draw(f)
    d.line([(0,0),(w,h)],fill='white',width=h//5); d.line([(0,h),(w,0)],fill='white',width=h//5)
    d.line([(0,0),(w,h)],fill=(200,16,46),width=h//15); d.line([(0,h),(w,0)],fill=(200,16,46),width=h//15)
    d.rectangle([w//2-h//6,0,w//2+h//6,h],fill='white'); d.rectangle([0,h//2-h//6,w,h//2+h//6],fill='white')
    d.rectangle([w//2-h//10,0,w//2+h//10,h],fill=(200,16,46)); d.rectangle([0,h//2-h//10,w,h//2+h//10],fill=(200,16,46))
    return f
fl=usflag(900,450); wv=Image.new('RGB',(900,560),(0,0,0)); wm=Image.new('L',(900,560),0)
for x in range(900):
    off=int(40*math.sin(x/120.0)+x*0.06); col=fl.crop((x,0,x+1,450))
    shade=0.78+0.22*math.cos(x/120.0); col=ImageEnhance.Brightness(col).enhance(shade)
    wv.paste(col,(x,off)); wm.paste(255,(x,off,x+1,off+450))
wv=wv.rotate(4,resample=Image.BICUBIC); wm=wm.rotate(4,resample=Image.BICUBIC)
fade=Image.linear_gradient('L').rotate(90).resize((900,560)); fade=ImageOps.invert(fade)
wm=ImageChops.multiply(wm,fade.point(lambda v:min(255,int(v*1.6))))
wv=ImageEnhance.Color(wv).enhance(1.3)
import os
if not os.environ.get('PERSON','').endswith('.jpg'): p.paste(wv,(-140,-120),wm)

# blend photo into map with soft diagonal edge
mask=Image.new('L',(W,H),0); dm=ImageDraw.Draw(mask)
dm.polygon([(0,0),(W*0.52,0),(W*0.46,H),(0,H)],fill=255); mask=mask.filter(ImageFilter.GaussianBlur(70))
canvas=m.copy(); canvas.paste(p,(0,0),mask.crop((0,0,p.size[0],H)))
# grade + vignette
v=Image.new('L',(W,H),0); ImageDraw.Draw(v).ellipse([-350,-300,W+350,H+300],fill=255); v=v.filter(ImageFilter.GaussianBlur(200))
canvas=Image.composite(canvas,Image.new('RGB',(W,H),(0,0,0)),v.point(lambda x:150+int(x*0.41)))

if os.environ.get('PERSON','').endswith('.png'):
    pr=Image.open(os.environ['PERSON']).convert('RGBA'); ph=int(os.environ.get('PH','900')); k=ph/pr.height; pr=pr.resize((int(pr.width*k),ph),Image.LANCZOS)
    a=pr.split()[3]; rgb=pr.convert('RGB'); rgb=ImageEnhance.Contrast(rgb).enhance(1.12); rgb=Image.blend(rgb,Image.new('RGB',rgb.size,(30,60,100)),0.08)
    fade=Image.linear_gradient('L').resize(pr.size).point(lambda v:255 if v<200 else int(255-(v-200)*3.5)); a=ImageChops.multiply(a,fade)
    ox=int(os.environ.get('PX','40')); oy=H-ph+40
    glow=Image.new('L',(W,H),0); glow.paste(a.filter(ImageFilter.MaxFilter(15)),(ox,oy)); canvas.paste((0,0,0),(0,0),glow.filter(ImageFilter.GaussianBlur(30)).point(lambda v:int(v*0.7)))
    canvas.paste(rgb,(ox,oy),a)
if os.environ.get('PERSON','').endswith('.jpg'):
    pr=Image.open(os.environ['PERSON']).convert('RGB'); k=1180/pr.height; pr=pr.resize((int(pr.width*k),1180),Image.LANCZOS)
    pr=ImageEnhance.Contrast(pr).enhance(1.15); pr=Image.blend(pr,Image.new('RGB',pr.size,(30,60,100)),0.12)
    pm=Image.new('L',pr.size,0); ImageDraw.Draw(pm).ellipse([-pr.width*0.25,pr.height*0.02,pr.width*0.95,pr.height*1.6],fill=255); pm=pm.filter(ImageFilter.GaussianBlur(70))
    ox=int(os.environ.get('PX','-60')); canvas.paste(pr,(ox,H-1180+60),pm)
gl=Image.new('L',(W,H),0); ImageDraw.Draw(gl).ellipse([W*0.45,H*0.85,W*1.1,H*1.25],fill=200); canvas.paste((220,50,10),(0,0),gl.filter(ImageFilter.GaussianBlur(90)))
# --- text, bottom right: big white word + yellow slanted bar
d=ImageDraw.Draw(canvas)
sz=300
while d.textlength(TOP,font=font(sz))>W*0.62: sz-=10
ft=font(sz)
tw=d.textlength(TOP,font=ft); x0=int(min(W*0.70-tw/2, W-60-tw)); y0=H-600
sh=Image.new('L',(W,H),0); ImageDraw.Draw(sh).text((x0+8,y0+10),TOP,font=ft,fill=255); canvas.paste((0,0,0),(0,0),sh.filter(ImageFilter.GaussianBlur(18)).point(lambda v:min(255,v*2)))
# subtle top-to-bottom grey gradient on white letters
tm=Image.new('L',(W,H),0); ImageDraw.Draw(tm).text((x0,y0),TOP,font=ft,fill=255)
grad=Image.new('RGB',(W,H)); gd=ImageDraw.Draw(grad)
for yy in range(H): c=int(255-max(0,yy-y0)/380*45); gd.line([(0,yy),(W,yy)],fill=(c,c,min(255,c+4)))
canvas.paste(grad,(0,0),tm)
d=ImageDraw.Draw(canvas)
import random; random.seed(7)
fb=A.ImageFont.truetype(str(A.A/'Bebas.ttf'),210); bw=d.textlength(BAN,font=fb)+14
by0=H-315; by1=H-85; bx1=W-20; bx0=min(int(W*0.44),W-60-int(bw)-230)
bm=Image.new('L',(W,H),0); dbm=ImageDraw.Draw(bm)
dbm.rectangle([bx0+150,by0+8,bx1-90,by1-8],fill=255)
y=by0
while y<by1:
    h=random.randint(2,6); a=random.randint(170,255)
    dbm.rectangle([bx0+int(150*random.random()**0.7),y,bx0+160,y+h],fill=a)
    dbm.rectangle([bx1-100,y,bx1-int(90*random.random()**0.8),y+h],fill=a); y+=h
for _ in range(25):
    yy=random.randint(by0+10,by1-10); xa=bx0+random.randint(150,260); dbm.line([(xa,yy),(xa+random.randint(40,140),yy)],fill=random.randint(120,200),width=1)
for x in range(bx0+140,bx1-80,5):
    dbm.rectangle([x,by0+random.randint(0,8),x+5,by0+9],fill=255); dbm.rectangle([x,by1-9,x+5,by1-9+random.randint(0,8)],fill=255)
bm=bm.filter(ImageFilter.BoxBlur(1)).filter(ImageFilter.GaussianBlur(0.8))
# colour: gold with orange lower edge and brush texture
col=Image.new('RGB',(W,H)); dc=ImageDraw.Draw(col)
for yy in range(by0,by1+1):
    t=(yy-by0)/(by1-by0); dc.line([(0,yy),(W,yy)],fill=(255,int(205-35*t**2),int(40-20*t)))
tex=Image.effect_noise((W//8,H),50).resize((W,H),Image.BICUBIC).convert('RGB')
col=Image.blend(col,ImageChops.multiply(col,ImageOps.autocontrast(tex)),0.18)
shadow=bm.filter(ImageFilter.GaussianBlur(16)).point(lambda v:int(v*0.6)); canvas.paste((0,0,0),(12,16),shadow.crop((0,0,W-12,H-16)))
canvas.paste(col,(0,0),bm)
# condensed heavy italic black text
TX=bx0+(bx1-bx0-bw)/2+10
tl=Image.new('L',(W,H),0); ImageDraw.Draw(tl).text((TX,by0+8),BAN,font=fb,fill=255,stroke_width=5,stroke_fill=255)
tl=tl.transform((W,H),Image.AFFINE,(1,0.18,-0.18*(by0+120),0,1,0),resample=Image.BICUBIC)
canvas.paste((14,12,10),(0,0),tl)
canvas=canvas.resize((1280,720),Image.LANCZOS); canvas.save(OUT,quality=92); print(OUT)
