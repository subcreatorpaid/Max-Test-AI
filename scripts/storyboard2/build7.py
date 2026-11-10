"""Build INV-007 storyboard PDF + playbook in kit v2. usage: python build7.py <stills_dir> <ref_frames_dir|-> <out_dir>"""
import sys, pathlib, textwrap
sys.path.insert(0, str(pathlib.Path(__file__).parent))
import kit, spec7
from kit import *
ROOT=kit.ROOT; sys.path.insert(0,str(ROOT/"tools/inv007"))
import script_v1 as S, visuals_v2 as V
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
    d.text((80,90),"INV-007 · The Prisoners of Hormuz",font=F(64,"b"),fill=INK)
    d.text((84,180),"Storyboard v1 + picture playbook · new 'ledger' look from the Round Two reference",font=F(32,"s"),fill=ORANGE)
    w=sum(len(r[1].split()) for r in rows); tot={"G":0,"F":0,"S":0}
    for r in rows: tot[V.V[r[0]][0]]+=len(r[1].split())
    lines=[f"Script v1: {len(rows)} paragraphs · {w} words · about 24 min of voice (can grow to ~30)",
           f"Mix by narration time: graphics {round(100*tot['G']/w)}% · video {round(100*tot['F']/w)}% · photos {round(100*tot['S']/w)}%  (target 50 / 30 / 20)",
           "Every video clip and photo matches the line being spoken. If no match is found, the shot becomes a graphic.",
           "No 'Illustration' label on screen (YouTube's synthetic-content box is still ticked at upload).",
           "Photos and clips in this storyboard are first picks from Pixabay; final clips are fetched per line before render.",
           "Pages 2-3: the playbook (reference frame vs our version). Then every paragraph in order."]
    for i,l in enumerate(lines): d.text((90,300+i*60),"• "+l,font=F(28,"m"),fill=(40,34,28))
    tiles_=["CO-01","CO-02","P1-10","P3-02","P5-08","RC-06"]
    for i,c in enumerate(tiles_):
        im=Image.open(OUT/"panels"/f"{c}.jpg").resize((520,292)); pg.paste(im,(80+(i%3)*540,700+(i//3)*310))
    return pg
pages.append(cover())
PLAY=[("N  Ledger number card","0:00",("CO-02",)),("L  Toned footage + orange glow + paper label","0:17",("CO-04",)),
      ("D  Document, key line circled","0:39",("P1-10",)),("T  Typed paper card + rubber stamp","0:58",("CO-05",)),
      ("B  Split-flap board","1:22",("P3-02",)),("K  Cut-paper figures + paper tags","1:38",("P5-08",)),
      ("M  Dark map / globe, orange arcs, pins","2:29",("P2-03",)),("P  Part card, giant faded number","3:15",("P1-01",)),
      ("R  Receipt printer + stamps","4:48",("RC-06",)),("W  Mini-chart tiles","5:52",("P3-04",)),
      ("X  Folder + index cards","6:46",("RC-07",)),("E  Plain logo end card (no particles)","8:53",(None,))]
def ts(t):
    m,s=t.split(":"); return int(m)*60+float(s)
for half in (PLAY[:6],PLAY[6:]):
    pg=Image.new("RGB",(PW,PH),(244,238,226)); d=ImageDraw.Draw(pg); page_header(d,"Playbook · reference (left)  →  INV-007 version (right)",len(pages)+1)
    for i,(name,t,(code,)) in enumerate(half):
        y=110+i*188; d.text((40,y+60),name,font=F(26,"b"),fill=INK); d.text((40,y+100),f"reference at {t}",font=F(20,"m"),fill=GREY)
        if REF!="-":
            fr=int(ts(t)*3)+3; p=pathlib.Path(REF)/f"f{fr:05d}.jpg"
            if p.exists(): pg.paste(Image.open(p).resize((310,174)),(620,y))
        im=Image.open(OUT/"panels"/f"{code}.jpg") if code else endcard(); pg.paste(im.resize((310,174)),(1000,y))
        d.text((945,y+70),"→",font=F(44,"b"),fill=ORANGE)
        rules={"N":"Hold max 6 s, then cut","L":"Only clips that match the line","D":"Use for reports, rates, contracts","T":"Stamp = the confidence tag","B":"Flips in, digits roll","K":"Faceless; never real people","M":"Arcs draw on; pins drop","P":"Fade through black + riser","R":"Prints line by line","W":"Lines draw left to right","X":"Cards slide in one by one","E":"Title fades in, no particles"}[name[0]]
        d.text((1330,y+70),rules,font=F(22,"s"),fill=(60,52,44))
    pages.append(pg)
for k in range(0,len(rows),per):
    pg=Image.new("RGB",(PW,PH),(244,238,226)); d=ImageDraw.Draw(pg); page_header(d,"INV-007 storyboard v1",len(pages)+1)
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
pages[0].save(OUT/"INV-007-prisoners-of-hormuz-storyboard-v1.pdf",save_all=True,append_images=pages[1:],resolution=150)
for i in (1,2): pages[i].save(OUT/f"playbook-{i}.jpg",quality=88)
pages[0].save(OUT/"cover.jpg",quality=88)
print("pages",len(pages))
