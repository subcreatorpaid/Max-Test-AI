# INV-009 storyboard SPEC: one panel per script row, kit v2 ledger look. ST = stills dir (set by build).
import kit
from kit import *
from kit2 import *
import pathlib, sys, math
sys.path.insert(0, str(kit.ROOT/"tools/inv009"))
import visuals_v1 as V
kit.GRADE.clear(); kit.GRADE.update({**{c:"shadow" for c in V.SHADOW},**{c:"high" for c in V.HIGH},**{c:"low" for c in V.LOW}})
ST="."
def ph(c): return f"{ST}/{c}.jpg"
TW=(116.5,20.5,124.5,27)          # Taiwan + strait
WP=(103,4,150,36)                 # western Pacific
GULF2TW=(30,-35,160,58)           # Qatar, Australia, Taiwan
TPE=(121.5,25.05); KHH=(120.3,22.6); TXG=(120.5,24.25); KEL=(121.75,25.13); MLI=(120.18,23.79); XIA=(118.1,24.5); SANYA=(109.5,18.25)
import random as _r
_rr=_r.Random(9)
CL_E=[(_rr.gauss(131,2.2),_rr.gauss(23,2.0)) for _ in range(55)]
CL_S=[(_rr.gauss(118,2.0),_rr.gauss(16,2.2)) for _ in range(55)]
LANES=[([(117.5,21.6),(118.8,23.6),(119.8,25.2),(121,26.9)],ORANGE),([(116.9,22.3),(118.2,24.2),(119.2,25.8),(120.2,27)],ORANGE)]

# ---------- new graphic types for INV-009 (one-offs) ----------
def chipgrid(n, of, title, sub, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER); d.text((92,140),sub,font=F(32,"s"),fill=ORANGE)
    for i in range(of):
        x=140+i*105; y=330; c=ORANGE if i<n else (70,64,58)
        d.rectangle([x,y,x+80,y+80],fill=c);
        for k in range(4):
            d.line([x+10+k*20,y-14,x+10+k*20,y],fill=c,width=4); d.line([x+10+k*20,y+80,x+10+k*20,y+94],fill=c,width=4)
        d.rectangle([x+22,y+22,x+58,y+58],outline=INK,width=3)
    return tag(im,t,src)
def rings(a, b, title, sub, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); cx,cy=420,390
    for r,p,w in ((230,b,34),(180,a,34)):
        d.arc([cx-r,cy-r,cx+r,cy+r],0,360,fill=(60,55,50),width=w); d.arc([cx-r,cy-r,cx+r,cy+r],-90,-90+3.6*p,fill=ORANGE if r==180 else RED,width=w)
    d.text((cx-90,cy-60),f"{a}%",font=F(96,"b"),fill=PAPER)
    d.text((720,250),title,font=F(52,"b"),fill=PAPER)
    for j,l in enumerate(wrap(d,sub,F(34,"s"),500)[:4]): d.text((722,330+j*46),l,font=F(34,"s"),fill=ORANGE)
    d.text((720,560),f"outer ring: {b}% at the top end",font=F(24,"m"),fill=GREY)
    return tag(im,t,src)
def dial(days, maxd, title, sub, t="", src="", ghost=None):
    im=ledger(); d=ImageDraw.Draw(im); cx,cy,r=430,400,220
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(30,27,24),outline=(110,100,90),width=6)
    for k in range(maxd):
        a=math.radians(-90+360*k/maxd); d.line([cx+math.cos(a)*(r-30),cy+math.sin(a)*(r-30),cx+math.cos(a)*(r-8),cy+math.sin(a)*(r-8)],fill=GREY,width=4)
    if ghost: d.pieslice([cx-r+20,cy-r+20,cx+r-20,cy+r-20],-90,-90+360*ghost/maxd,fill=(60,40,30))
    d.pieslice([cx-r+20,cy-r+20,cx+r-20,cy+r-20],-90,-90+360*days/maxd,fill=ORANGE)
    d.ellipse([cx-90,cy-90,cx+90,cy+90],fill=INK); s=str(days); d.text((cx-d.textlength(s,font=F(110,"b"))/2,cy-70),s,font=F(110,"b"),fill=PAPER)
    d.text((760,280),title,font=F(56,"b"),fill=PAPER)
    for j,l in enumerate(wrap(d,sub,F(34,"s"),460)[:4]): d.text((762,360+j*46),l,font=F(34,"s"),fill=ORANGE)
    return tag(im,t,src)
def tanks(items, title, sub="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER); d.text((92,140),sub,font=F(30,"s"),fill=ORANGE)
    for i,(lab,frac,val) in enumerate(items):
        x=240+i*460; y=230; w,h=300,360
        d.rounded_rectangle([x,y,x+w,y+h],30,outline=PAPER,width=6); hh=int((h-20)*frac)
        d.rounded_rectangle([x+10,y+h-10-hh,x+w-10,y+h-10],22,fill=RED if frac<0.2 else ORANGE)
        d.text((x+w/2-d.textlength(val,font=F(52,"b"))/2,y+h/2-60),val,font=F(52,"b"),fill=PAPER)
        d.text((x+w/2-d.textlength(lab,font=F(34,"b"))/2,y+h+20),lab,font=F(34,"b"),fill=PAPER)
    return tag(im,t,src)
def icongrid(a, b, title, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,60),title,font=F(52,"b"),fill=PAPER)
    def boat(x,y,c): d.polygon([(x,y),(x+26,y),(x+20,y+10),(x+4,y+10)],fill=c); d.rectangle([x+9,y-8,x+17,y],fill=c)
    for i in range(a[1]): boat(80+(i%25)*28,170+(i//25)*34,ORANGE)
    d.text((80,390),a[0],font=F(30,"b"),fill=ORANGE)
    for i in range(b[1]): boat(80+i*28,480,PAPER)
    d.text((80,520),b[0],font=F(30,"b"),fill=PAPER)
    return tag(im,t,src)
def stopwatch(txt, title, sub, comply=(3,4), t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); cx,cy,r=360,410,200
    d.rectangle([cx-30,cy-r-60,cx+30,cy-r-20],fill=GREY); d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(232,224,210),outline=GREY,width=10)
    d.line([cx,cy,cx,cy-r+30],fill=RED,width=8); d.text((cx-d.textlength(txt,font=F(76,"mono"))/2,cy+40),txt,font=F(76,"mono"),fill=INKT if False else (30,26,22))
    d.text((680,220),title,font=F(52,"b"),fill=PAPER); d.text((682,290),sub,font=F(34,"s"),fill=ORANGE)
    for i in range(comply[1]):
        x=700+i*130; c=GREEN if i<comply[0] else RED
        d.polygon([(x,470),(x+100,470),(x+82,500),(x+18,500)],fill=PAPER); d.rectangle([x+38,440,x+62,470],fill=PAPER)
        d.text((x+30,515),"✓" if i<comply[0] else "✗",font=F(40,"b"),fill=c)
    return tag(im,t,src)
def coins(items, title, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(52,"b"),fill=PAPER); mx=max(v for _,v,_ in items)
    for i,(lab,v,txt) in enumerate(items):
        x=220+i*330; n=int(16*v/mx)+1
        for k in range(n): d.ellipse([x,560-k*22,x+180,600-k*22],fill=ORANGE if i==len(items)-1 else (180,150,90),outline=INK,width=2)
        d.text((x+90-d.textlength(txt,font=F(44,"b"))/2,520-n*22),txt,font=F(44,"b"),fill=PAPER)
        d.text((x+90-d.textlength(lab,font=F(26,"b"))/2,620),lab,font=F(26,"b"),fill=GREY)
    return tag(im,t,src)
def division(a, b, res, title, t="", src=""):
    im=ledger().convert("RGBA"); p=paper_rect((900,460),PAPER,False,41); pd=ImageDraw.Draw(p)
    for y in range(70,460,48): pd.line([0,y,900,y],fill=(176,190,200),width=1)
    pd.text((50,40),title,font=F(34,"s"),fill=(30,26,22))
    pd.text((60,130),a,font=F(70,"mono"),fill=(30,26,22)); pd.text((60,220),"÷ "+b,font=F(70,"mono"),fill=(30,26,22))
    pd.line([60,320,700,320],fill=(30,26,22),width=4); pd.text((60,340),"≈ "+res,font=F(76,"mono"),fill=RED)
    im=drop(im,p,(190,130),-1.5); return tag(im.convert("RGB"),t,src)
def mirror(items, title, sub="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,60),title,font=F(52,"b"),fill=PAPER); d.text((92,128),sub,font=F(28,"s"),fill=ORANGE)
    cx=W//2; d.line([cx,200,cx,650],fill=GREY,width=3); mx=max(abs(v) for _,v,_ in items)
    for i,(lab,v,txt) in enumerate(items):
        y=230+i*140; w=int(480*abs(v)/mx); c=RED if i==len(items)-1 else ORANGE
        if i%2==0: d.rectangle([cx-w,y,cx,y+80],fill=c); d.text((cx-w-10-d.textlength(txt,font=F(40,"b")),y+18),txt,font=F(40,"b"),fill=PAPER); d.text((cx+20,y+24),lab,font=F(30,"b"),fill=GREY)
        else: d.rectangle([cx,y,cx+w,y+80],fill=c); d.text((cx+w+12,y+18),txt,font=F(40,"b"),fill=PAPER); d.text((cx-20-d.textlength(lab,font=F(30,"b")),y+24),lab,font=F(30,"b"),fill=GREY)
    return tag(im,t,src)
def window(marks, title, shade=(0,1), t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,80),title,font=F(56,"b"),fill=PAPER)
    x0,x1=120,W-120; y=400; n=len(marks)
    xs=[x0+(x1-x0)*i/(n-1) for i in range(n)]
    d.rectangle([xs[shade[0]],y-70,xs[shade[1]],y+70],fill=(70,40,24))
    d.line([x0,y,x1,y],fill=PAPER,width=6)
    for x,(lab,sub,hot) in zip(xs,marks):
        d.line([x,y-30,x,y+30],fill=ORANGE if hot else PAPER,width=6); d.text((x-d.textlength(lab,font=F(54,"b"))/2,y-130),lab,font=F(54,"b"),fill=ORANGE if hot else PAPER)
        d.text((x-d.textlength(sub,font=F(26,"s"))/2,y+50),sub,font=F(26,"s"),fill=GREY)
    return tag(im,t,src)
def yearcard(year, sub):
    im=ledger(); d=ImageDraw.Draw(im); d.text((W/2-d.textlength(year,font=F(300,"bebas"))/2,120),year,font=F(300,"bebas"),fill=PAPER)
    d.text((W/2-d.textlength(sub,font=F(44,"s"))/2,470),sub,font=F(44,"s"),fill=ORANGE)
    s=stamp("REHEARSAL",RED,48); im.paste(s,(850,140),s); return im
def road6(stops, title):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER)
    n=len(stops); xs=[130+i*(W-260)/(n-1) for i in range(n)]; y=380
    d.line([xs[0],y,xs[-1],y],fill=GREY,width=4)
    for i,(x,lab) in enumerate(zip(xs,stops)):
        d.ellipse([x-30,y-30,x+30,y+30],fill=ORANGE if i==n-1 else (70,64,58)); d.text((x-10,y-22),str(i+1),font=F(36,"b"),fill=PAPER)
        for j,l in enumerate(wrap(d,lab,F(26,"b"),180)): d.text((x-d.textlength(l,font=F(26,"b"))/2,y+50+j*32),l,font=F(26,"b"),fill=PAPER)
    return im
def inset(base, panel, scale_=0.42):
    p=panel.resize((int(W*scale_),int(H*scale_))); b=base.convert("RGBA"); x,y=W-p.width-40,60
    ImageDraw.Draw(b).rectangle([x-6,y-6,x+p.width+6,y+p.height+6],fill=PAPER); b.paste(p,(x,y)); return b.convert("RGB")
def ships_map(extra_pins=(), title="100+ ships", sub="two clusters · Nov 2026", t="CLAIM", src="TAIWAN NSC / AEI-ISW"):
    return map_(WP,hi=["Taiwan"],dots=CL_E+CL_S,pins=extra_pins,title=title,sub=sub,t=t,src=src)

RECEIPT_LINES=[("Your car","+45% (2021 floor)"),("Your devices","NOT MODELLED"),("Your share","$7,200 / $14,900"),("Your energy","NOT PRICED"),("Watch","18 NOV · 28 NOV · 10 JAN")]
def rc(n, st=None): return receipt(RECEIPT_LINES[:n],title="THE RECEIPT",st=st,sub="INV-009 · EXAMPLE US HOUSEHOLD")

SPEC={
"CO-01":lambda: ships_map(),
"CO-02":lambda: footage(ph("CO-02"),"What happens if China invades Taiwan?","or simply closes the door around it"),
"CO-03":lambda: number("$15,000","per US household, year one of a war","BLOOMBERG ECONOMICS MODEL · WORLD -$10.6 TRILLION","SCENARIO","BLOOMBERG, FEB 2026",faded="$10.6T"),
"CO-04":lambda: typed([["A model","of something that","hasn't happened"],["One side says","a claim"],["Official","data"]],["SCENARIO",("CLAIM",ORANGE),("VERIFIED",GREEN)]),
"CO-05":lambda: road6(["The chips","The strait","Why 2027","The rehearsal","The money","Your table"],"Where this goes"),
"P1-01":lambda: part(1,"What Taiwan Makes","Why the world depends on Taiwan's chips"),
"P1-02":lambda: footage(ph("P1-02"),"23 million people","130 km from China",t="VERIFIED",src="AFP; CSIS"),
"P1-03":lambda: footage(ph("P1-03"),"≈ 9 in 10","of the most advanced chips",glow=(640,360),t="REPORTED",src="RHODIUM GROUP"),
"P1-04":lambda: rings(70,90,"TSMC","nearly 70% of all contract-made chips",t="REPORTED",src="MARKETSCREENER, JUN 2026"),
"P1-04b":lambda: footage(ph("P1-04b"),"Older chips: 1/3 to 1/2","fridges, tools, car windows",t="REPORTED",src="RHODIUM GROUP"),
"P1-05":lambda: footage(ph("P1-05"),"Nvidia ≈22% · Apple ≈18%","of TSMC's revenue, 2026",t="REPORTED",src="CNBC VIA MACRUMORS"),
"P1-06":lambda: donut(35,"of the world's car microcontrollers","1,000+ chips in a new car","TSMC alone",t="REPORTED",src="RHODIUM; WAFER WORLD"),
"P1-07":lambda: footage(ph("P1-07"),"$640.7bn exports · 2025","30.9% to the United States",t="VERIFIED",src="TAIWAN MOF VIA ING"),
"P1-08":lambda: yearcard("2021","the last time chips ran short"),
"P1-09":lambda: footage(ph("P1-09"),"7.7 million cars","never built · 2021",t="REPORTED",src="ALIXPARTNERS"),
"P1-10":lambda: document("BLS Consumer Price Index · June 2021",[("All items","+5.4%"),("New vehicles","+5.3%"),("Used cars and trucks","+45.2%"),("Gasoline","+45.1%")],hi=2,t="VERIFIED",src="BLS, 13 JUL 2021"),
"P1-10b":lambda: tiles([("Cars not built",None,"7.7M"),("Buyers paid",None,"+$90bn"),("Cost to US",None,"≈1% GDP")],"The 2021 chip shortage",t="REPORTED",src="ALIXPARTNERS; MARKETSCREENER"),
"P1-11":lambda: pricetags([("Used car, 2020","$25,000"),("Same car, 2021","$36,300"),("Taiwan","OPEN")],"+45% on one example car",t="ILLUSTRATION",src="OUR MATHS"),
"P1-12":lambda: map_(TW,hi=["Taiwan"],lanes=LANES,title="Now close the sea",sub="not the factories"),
"BR-01":lambda: envelope("The Winter Bill: who freezes first","SUBSCRIBE"),
"P2-01":lambda: part(2,"The Strait","How the Taiwan Strait moves world trade"),
"P2-02":lambda: map_(TW,hi=["Taiwan"],lanes=LANES,title="$2.45 trillion",sub="1/5 of sea trade · 2022",t="REPORTED",src="CSIS VIA AFP"),
"P2-03":lambda: footage(ph("P2-03"),"≈ half of all container ships","went through it · Jan-Jul 2022",t="REPORTED",src="BLOOMBERG"),
"P2-04":lambda: map_(TW,hi=["Taiwan"],pins=[(*KHH,"KAOHSIUNG · 57%"),(*TXG,"TAICHUNG"),(*TPE,"TAIPEI"),(*KEL,"KEELUNG"),(*MLI,"MAILIAO")],title="The ports face China",sub="Kaohsiung: 57% of sea trade",t="REPORTED",src="CSIS, 2024"),
"P2-05":lambda: footage(ph("P2-05"),"97% of its energy","comes in by sea",t="REPORTED",src="MOEA / TAIPOWER"),
"P2-06":lambda: inset(footage(ph("P2-06"),"About half its power","comes from gas",t="REPORTED",src="CHUNG-HUA INST.; ATLANTIC COUNCIL"),dial(11,14,"","")),
"P2-07":lambda: map_(GULF2TW,hi=["Taiwan","Qatar"],arcs=[((145,-30),(121,23.5)),((-100,30),(121,23.5))],lanes=[([(51.4,25.5),(56.4,26.4),(60,24),(75,12),(100,4),(121,23.5)],RED)],pins=[(51.4,25.3,"QATAR · 1/3"),(121,23.5,"TAIWAN")],title="1/3 of its gas was Qatari",sub="now from Australia and the US",t="REPORTED",src="ATLANTIC COUNCIL (KPLER)"),
"P2-07b":lambda: inset(footage(ph("P2-07b"),"Oil ≈ 5 months","gas ≈ 11 days",t="REPORTED",src="ATLANTIC COUNCIL; MOEA"),tanks([("OIL",0.95,"≈150 d"),("GAS",0.1,"≈11 d")],"Reserves")),
"P2-08":lambda: footage(ph("P2-08"),"Squeezed from far away","what if it's from close by?"),
"P2-09":lambda: footage(ph("P2-09"),"Why 2027?",""),
"P3-01":lambda: part(3,"Why 2027","The Davidson window explained"),
"P3-02":lambda: footage(ph("P3-02"),"The Davidson window","2021 → 2027",t="VERIFIED",src="STARS AND STRIPES"),
"P3-03":lambda: typed([["CIA Director W. Burns, 2023","Xi told the military:","“ready by 2027”"]],["REPORTED"]),
"P3-04":lambda: quote("All indications point to the PLA meeting President Xi Jinping's directive to be ready to invade Taiwan by 2027.","Adm. John Aquilino · US Indo-Pacific Command","2024",t="VERIFIED",src="USNI NEWS"),
"P3-05":lambda: document("ODNI Annual Threat Assessment · March 2026",[("Invasion in 2027?","do not currently plan"),("Fixed timeline?","none"),("Big date","2049"),("Key question","will the US intervene?")],hi=0,t="VERIFIED",src="ODNI VIA USNI NEWS"),
"P3-05b":lambda: window([("2021","Davidson",False),("2027","ready by",True),("2049","PRC at 100",False)],"Two dates, not one",shade=(0,1),t="VERIFIED",src="ODNI"),
"P3-06":lambda: halves(("MAR 2026",["US intelligence:","“do not currently","plan” to invade"],NAVY),("OCT 2026",["US Army Pacific:","window “still","valid”"],RED),"Same government · same year · two answers"),
"P3-07":lambda: scale(("Able to","CAN",ORANGE),("Decided to","WILL?",INKT),"Can is not will",t="VERIFIED",src="ODNI"),
"P3-08":lambda: notebook("…whether or not the U.S. will militarily intervene on Taiwan's behalf","ODNI Annual Threat Assessment","March 2026",t="VERIFIED",src="ODNI VIA USNI"),
"P3-09":lambda: flow([("Insure","higher premiums"),("Stockpile","extra chips"),("Second factory","years away"),("Total","no number yet")],"The cost of not knowing"),
"P3-10":lambda: ships_map(title="Watch the ships",sub="what are they practising?",t="",src=""),
"P4-01":lambda: part(4,"The Rehearsal","China's drills: blockade vs quarantine"),
"P4-02":lambda: map_(TW,hi=["Taiwan"],lanes=[([(117.4,22.6),(118.9,24.4),(120.4,26.4),(121.2,27)],PAPER)],dots=[p for p in [(_rr.uniform(117.5,123.8),_rr.uniform(20.8,26.9)) for _ in range(220)] if not (119.9<p[0]<122.1 and 21.8<p[1]<25.4)][:130],title="Justice Mission 2025",sub="130 aircraft · 90 crossed the line",t="VERIFIED",src="TAIWAN MND VIA USNI"),
"P4-03":lambda: calendar([("DEC","29","drills begin"),("DEC","30","rockets, landings"),("DEC","31","over")],"Three days",t="VERIFIED",src="USNI NEWS"),
"P4-04":lambda: ships_map(extra_pins=[(*SANYA,"SANYA"),(128,21,"LIAONING"),(115,14,"FUJIAN")],title="100+ ships · 2 carriers",sub="November 2026"),
"P4-04b":lambda: tally([("Air sorties",49,"49",PAPER),("To the south",36,"36",ORANGE)],"2 November 2026",t="REPORTED",src="TAIWAN MND VIA AEI"),
"P4-05":lambda: bubbles([("AEI / ISW","maybe an unannounced drill to cut Taiwan off"),("Taiwan · China","'area denial' · 'routine training'")],"Who says what",t="CLAIM",src="TAIPEI TIMES 10 NOV"),
"P4-05b":lambda: inset(footage(ph("P4-05b"),"2.63 million a day","cyberattacks, 2025",t="CLAIM",src="TAIWAN NSB"),odometer("2.63M","","")),
"P4-06":lambda: typed([["Not an invasion.","Quarantine"]],["SCENARIO"]),
"P4-07":lambda: footage(ph("P4-07"),"Quarantine: coast guard checks","a customs check that never ends",t="VERIFIED",src="CSIS DEFINITION"),
"P4-08":lambda: icongrid(("CHINA COAST GUARD · 150+ OCEAN-GOING",150),("TAIWAN · ≈10",10),"150+ vs about 10",t="REPORTED",src="CSIS"),
"P4-09":lambda: stopwatch("48:00","Checks start","48 hours after the announcement",t="SCENARIO",src="CSIS, 2024"),
"P4-10":lambda: inset(footage(ph("P4-10"),"≈ 9 days of gas","after checks begin (winter)",t="ESTIMATE",src="OUR MATHS"),dial(9,14,"","",ghost=11)),
"P4-11":lambda: columns(["US EXPERTS","TAIWAN EXPERTS"],[13,9],hi=0,title="Completely confident",sub="the US would act against a quarantine",t="REPORTED",src="CSIS SURVEY 2024"),
"P4-12":lambda: receipt([("Chip shortage, plants open","+45% used cars"),("Quarantine gas clock","≈ 9 days"),("Advanced chips at stake","9 in 10")],title="THE BILL SO FAR",st="HALF-RECEIPT",sub="INV-009 · WHAT WE KNOW"),
"P4-13":lambda: footage(ph("P4-13"),"What would it cost","the rest of us?"),
"P5-01":lambda: part(5,"The Money","What a Taiwan war would cost"),
"P5-02":lambda: clipboards(("Blockade","Bloomberg model, first-year GDP hit"),("War","Bloomberg model, first-year GDP hit")),
"P5-03":lambda: tiles([("World",None,"-5.3%"),("US",None,"-3.2%"),("China",None,"-8.9%"),("Taiwan",None,"-12.5%")],"Blockade · year one",t="SCENARIO",src="BLOOMBERG, FEB 2026"),
"P5-04":lambda: bars([("World",9.6,"-9.6%"),("US",6.6,"-6.6%"),("Japan",14.7,"-14.7%"),("South Korea",23,"-23%")],"War · year one","world -$10.6 trillion",t="SCENARIO",src="BLOOMBERG, FEB 2026",hi=3),
"P5-05":lambda: footage(ph("P5-05"),"COVID 2020: -2.2%","both Taiwan versions are worse",t="VERIFIED",src="BEA"),
"P5-05b":lambda: mirror([("CHINA",-11,"-11%"),("US",-6.6,"-6.6%"),("TAIWAN (ASSUMED)",-40,"-40%")],"Nobody escapes","war version, year one",t="SCENARIO",src="BLOOMBERG"),
"P5-06":lambda: division("$30.86 trillion","137 million homes","$225,000 each","US output per household, 2025",t="ESTIMATE",src="BEA; CENSUS; OUR MATHS"),
"P5-07":lambda: inset(footage(ph("P5-07"),"Lost work, lost sales","spread across everyone",t="ESTIMATE",src="OUR MATHS"),coins([("COVID",4950,"$4,950"),("BLOCKADE",7200,"$7,200"),("WAR",14900,"$14,900")],"")),
"P5-08":lambda: ticket("Rhodium Group · blockade","$2 TRILLION+",["activity at risk","a floor, not a ceiling"],st="FLOOR",t="ESTIMATE",src="RHODIUM GROUP, 2022"),
"P5-09":lambda: footage(ph("P5-09"),"$1.6 trillion","yearly sales at chip-dependent firms",t="ESTIMATE",src="RHODIUM GROUP"),
"P5-09b":lambda: footage(ph("P5-09b"),"≈ $198bn Taiwan → US","2025 · servers, chips, parts",t="ESTIMATE",src="OUR MATHS ON TAIWAN MOF"),
"P5-10":lambda: footage(ph("P5-10"),"$165bn for Arizona","$20bn+ and years per plant",t="REPORTED",src="MARKETSCREENER, JUN 2026"),
"P5-11":lambda: yearcard("2021","× the whole island"),
"P5-12":lambda: footage(ph("P5-12"),"What do the deals cost?",""),
"P6-01":lambda: part(6,"The Deal","Trump, Xi and the Taiwan arms deal"),
"P6-02":lambda: notice("US arms sale to Taiwan","$14 billion package","Funded by Taiwan's legislature in May 2026. Held by Washington since: 'a very good negotiating chip'.",st="ON HOLD",t="REPORTED",src="DOMINO THEORY, OCT 2026"),
"P6-02b":lambda: letter("US State Department","military stockpiles elsewhere are a factor","Secretary of State Marco Rubio (paraphrase)","September 2026",t="REPORTED",src="DOMINO THEORY"),
"P6-03":lambda: footage(ph("P6-03"),"Held until after APEC?","SCMP, 19 Sep 2026 · anonymous sources",t="REPORTED",src="SCMP"),
"P6-04":lambda: footage(ph("P6-04"),"APEC Shenzhen · 18-19 Nov","Taiwan votes 28 Nov · G20 in December",t="REPORTED",src="AEI; TAIPEI TIMES"),
"P6-05":lambda: inset(footage(ph("P6-05"),"Trade truce ends","10 January 2027",t="REPORTED",src="DOMINO THEORY"),flap([("TRUCE","10 JAN")],"")),
"P6-06":lambda: footage(ph("P6-06"),"Hormuz: open to Chinese ships","Iran's claim · special fees",t="CLAIM",src="IRAN VIA AEI"),
"P6-07":lambda: footage(ph("P6-07"),"24 war games","dozens of ships, hundreds of aircraft",t="SCENARIO",src="CSIS, JAN 2023"),
"P6-08":lambda: footage(ph("P6-08"),"23 million people","the line no model prices",t="VERIFIED"),
"P6-08b":lambda: checklist("What nobody knows",[("A plan for 2027?",False),("Quarantine, blockade or war?",False),("Would America fight?",False),("What the 100 ships did",False)],st="UNKNOWN"),
"P6-09":lambda: footage(ph("P6-09"),"At your table","line by line"),
"RC-01":lambda: rc(0,"SCENARIO"),
"RC-02":lambda: inset(footage(ph("RC-02"),"Line 1 · your car","+45% was the floor (2021)",t="VERIFIED",src="BLS"),rc(1)),
"RC-03":lambda: inset(footage(ph("RC-03"),"Line 2 · your devices","not modelled · at risk",t="REPORTED",src="RHODIUM"),rc(2)),
"RC-04":lambda: rc(3),
"RC-05":lambda: inset(footage(ph("RC-05"),"Line 4 · your energy","not priced · tight"),rc(4)),
"RC-06":lambda: rc(5,"WATCH"),
"RC-07":lambda: inset(footage(ph("RC-07"),"Buy what you need","not in a panic · buffer 3-6 months"),checklist("Not financial advice",[("Buy what you need anyway",True),("Buffer 3-6 months",True)])),
"RC-08":lambda: steps([("1","+20% stress test"),("2","Don't trade headlines")],"What you can do"),
"RC-09":lambda: comment("Chips or energy: which hits your home first?","and where are you watching from?"),
"RC-10":lambda: footage(ph("RC-10"),"Every crisis sends a bill.","History keeps the receipts."),
}
DESC={}
