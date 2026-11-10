"""Build INV-009 storyboard PDF in kit v2. usage: python build8.py <stills_dir> <ref_frames_dir|-> <out_dir>"""
import sys, pathlib, textwrap
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import kit, spec9 as spec7
from kit import *
ROOT=kit.ROOT; sys.path.insert(0,str(ROOT/"tools/inv009"))
import script_v1 as S8, visuals_v1 as V
class S: R=[r for _,_,rs in S8.PARTS for r in rs]
spec7.ST=sys.argv[1]; REF=sys.argv[2]; OUT=pathlib.Path(sys.argv[3]); (OUT/"panels").mkdir(parents=True,exist_ok=True)
for r in S.R:
    c=r[0]; kit.CUR[0]=c; im=spec7.SPEC[c](); im.save(OUT/"panels"/f"{c}.jpg",quality=88)
print("panels",len(S.R))
# ---- storyboard pages: 2x3 panels with code, kind, narration, shot note
PW,PH=1754,1240
def page_header(d,title,n):
    d.rectangle([0,0,PW,80],fill=INK); d.text((40,22),title,font=F(34,"b"),fill=PAPER); d.text((PW-200,28),f"page {n}",font=F(24,"m"),fill=GREY)
pages=[]; rows=S.R; per=6
KN={"G":("GRAPHIC",ORANGE),"F":("VIDEO",(70,140,200)),"S":("PHOTO",(120,170,90))}
# cover + playbook pages first
def cover():
    pg=Image.new("RGB",(PW,PH),(244,238,226)); d=ImageDraw.Draw(pg)
    d.text((80,90),"INV-009 · What Happens If China Invades Taiwan?",font=F(64,"b"),fill=INK)
    d.text((84,180),"Storyboard v1 · ledger look (same kit as INV-007 and INV-008)",font=F(32,"s"),fill=ORANGE)
    w=sum(len(r[1].split()) for r in rows); tot={"G":0,"F":0,"S":0}
    for r in rows: tot[V.V[r[0]][0]]+=len(r[1].split())
    lines=[f"Script v1: {len(rows)} paragraphs · {w} words · about 19 min of voice, ~20 min cut (can grow to ~30)",
           f"Mix by narration time: graphics {round(100*tot['G']/w)}% · video {round(100*tot['F']/w)}% · photos {round(100*tot['S']/w)}%  (target 50 / 30 / 20)",
           "Every video clip and photo matches the line being spoken. If no match is found, the shot becomes a graphic.",
           "No 'Illustration' label on screen (YouTube's synthetic-content box is still ticked at upload).",
           "Photos and clips in this storyboard are first picks from Pixabay; final clips are fetched per line before render.",
           "Then every paragraph in order, with a grade label under each photo or clip."]
    for i,l in enumerate(lines): d.text((90,300+i*60),"• "+l,font=F(28,"m"),fill=(40,34,28))
    tiles_=["CO-01","P1-03","P2-06","P4-09","P5-04","RC-06"]
    for i,c in enumerate(tiles_):
        im=Image.open(OUT/"panels"/f"{c}.jpg").resize((520,292)); pg.paste(im,(80+(i%3)*540,700+(i//3)*310))
    return pg
pages.append(cover())
for k in range(0,len(rows),per):
    pg=Image.new("RGB",(PW,PH),(244,238,226)); d=ImageDraw.Draw(pg); page_header(d,"INV-009 storyboard v1",len(pages)+1)
    for i,r in enumerate(rows[k:k+per]):
        x=40+(i%2)*860; y=100+(i//2)*375; c=r[0]; kind,desc,q=V.V[c]; desc=spec7.DESC.get(c,desc)
        pg.paste(Image.open(OUT/"panels"/f"{c}.jpg").resize((400,225)),(x,y))
        kn,kc=KN[kind]; d.rectangle([x,y+232,x+120,y+262],fill=kc); d.text((x+10,y+236),kn,font=F(18,"b"),fill=(255,255,255))
        d.text((x+132,y+234),c,font=F(24,"b"),fill=INK)
        if kind in "FS":
            g=kit.GRADE.get(c,"mid"); gl={"shadow":("SHADOW",(40,44,52)),"low":("COLOUR · CALM",(70,110,150)),"mid":("COLOUR",(120,110,90)),"high":("COLOUR · INTENSE",(200,90,30))}[g]
            d.text((x+260,y+238),gl[0],font=F(16,"b"),fill=gl[1])
        for j,l in enumerate(textwrap.wrap(r[1],50)[:9]): d.text((x+412,y+2+j*25),l,font=F(17,"r"),fill=(40,34,28))
        for j,l in enumerate(textwrap.wrap(desc,70)[:3]): d.text((x,y+272+j*24),l,font=F(16,"m"),fill=(110,100,88))
    pages.append(pg)
pages[0].save(OUT/"INV-009-taiwan-2027-storyboard-v1.pdf",save_all=True,append_images=pages[1:],resolution=150)
pages[0].save(OUT/"cover.jpg",quality=88)
print("pages",len(pages))
