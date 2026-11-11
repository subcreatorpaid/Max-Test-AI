# INV-010 storyboard SPEC: one panel per script row, kit v2 ledger look. ST = stills dir (set by build).
# No photos of Jensen Huang or Alice Huang: dossier cards, buildings, cut-paper. Every claim attributed.
import kit
from kit import *
from kit2 import *
import pathlib, sys, math
sys.path.insert(0, str(kit.ROOT/"tools/inv009")); sys.path.insert(0, str(kit.ROOT/"tools/inv010"))
import spec9 as _s9                       # reuse INV-009 one-offs: inset, division, yearcard, dial, coins
import importlib.util as _u
_sp=_u.spec_from_file_location("visuals_v10", str(kit.ROOT/"tools/inv010/visuals_v1.py")); V=_u.module_from_spec(_sp); _sp.loader.exec_module(V)
kit.GRADE.clear(); kit.GRADE.update({**{c:"shadow" for c in V.SHADOW},**{c:"high" for c in V.HIGH},**{c:"low" for c in V.LOW}})
inset, division, coins = _s9.inset, _s9.division, _s9.coins
ST="."
def ph(c): return f"{ST}/{c}.jpg"
WORLD=(-130,-45,160,65); SEA=(95,-5,125,28); PAC=(-130,10,130,45)
SG=(103.85,1.3); KL=(101.7,3.1); BJ=(116.4,39.9); TPE=(121.5,25.05); SC=(-121.95,37.35)

# ---------- one-off graphic types for INV-010 ----------
def memo(lines, hi, title="STAFF MEMO", date="8 NOV 2026", t="", src=""):
    im=dark().convert("RGBA"); p=paper_rect((820,520),PAPER,False,7); d=ImageDraw.Draw(p)
    d.text((48,40),title,font=F(30,"mono"),fill=(30,26,22)); d.text((48,82),date,font=F(20,"monor"),fill=(90,82,72))
    d.line([48,118,772,118],fill=(150,140,124),width=2)
    for i,l in enumerate(lines):
        y=150+i*62
        if i==hi: d.rectangle([40,y-6,780,y+44],fill=(236,200,90))
        d.text((48,y),l,font=F(30,"r"),fill=(40,34,28))
        if i==hi: d.ellipse([30,y-20,790,y+60],outline=RED,width=5)
    im=drop(im,p,(230,110),-2,14); s=stamp("REPORTED",RED,48); im.paste(s,(860,520),s)
    return tag(im.convert("RGB"),t,src)
def cents(n, big, sub, t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); cx,cy,r=360,380,230
    d.ellipse([cx-r,cy-r,cx+r,cy+r],fill=(40,36,32),outline=GREY,width=6)
    d.pieslice([cx-r+14,cy-r+14,cx+r-14,cy+r-14],-90,-90+3.6*n,fill=ORANGE)
    d.ellipse([cx-120,cy-120,cx+120,cy+120],fill=INK); s=f"{n}¢"; d.text((cx-d.textlength(s,font=F(110,"b"))/2,cy-70),s,font=F(110,"b"),fill=PAPER)
    d.text((700,230),big,font=F(96,"b"),fill=PAPER)
    for j,l in enumerate(wrap(d,sub,F(36,"s"),520)[:3]): d.text((704,350+j*48),l,font=F(36,"s"),fill=ORANGE)
    return tag(im,t,src)
def chair(title="", sub="", lit=False):
    im=ledger(); d=ImageDraw.Draw(im)
    if lit:
        m=Image.new("L",(W,H),0); ImageDraw.Draw(m).polygon([(560,0),(720,0),(860,560),(420,560)],fill=110); m=m.filter(ImageFilter.GaussianBlur(30))
        im=Image.composite(Image.new("RGB",(W,H),(232,170,90)),im,m); d=ImageDraw.Draw(im)
    d.rectangle([180,470,1100,500],fill=(120,84,52))                      # table
    for x in (220,1040): d.rectangle([x,500,x+20,640],fill=(90,62,40))
    for i,x in enumerate((300,450,800,950)):                             # dim chairs
        d.rectangle([x,380,x+70,470],fill=(52,46,40)); d.rectangle([x,300,x+12,470],fill=(52,46,40))
    c=ORANGE if lit else PAPER; d.rectangle([610,380,690,470],fill=c); d.rectangle([610,290,624,470],fill=c); d.rectangle([610,470,622,560],fill=c); d.rectangle([678,470,690,560],fill=c)
    for x in (330,480,650,830,980): d.ellipse([x,455,x+30,470],fill=(200,190,170))   # plates
    if title: d.text((86,70),title,font=F(56,"b"),fill=PAPER)
    if sub: d.text((92,140),sub,font=F(32,"s"),fill=ORANGE)
    return im
def dossier(rows, head="SUBJECT FILE", t="", src=""):
    im=dark().convert("RGBA"); p=paper_rect((900,520),(214,204,186),False,5); d=ImageDraw.Draw(p)
    d.rectangle([40,40,260,300],outline=(120,110,96),width=4); d.text((80,150),"NO PHOTO",font=F(28,"mono"),fill=(120,110,96))
    d.text((300,44),head,font=F(32,"mono"),fill=(30,26,22))
    for i,(a,b) in enumerate(rows):
        y=110+i*82; d.text((300,y),a.upper(),font=F(20,"monor"),fill=(110,100,88)); d.text((300,y+26),b,font=F(34,"b"),fill=(30,26,22))
    im=drop(im,p,(190,110),1,14); return tag(im.convert("RGB"),t,src)
def doors(lit, labels=("STAYS","LEAVES","TIGHTER RULES"), title="Three paths", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,60),title,font=F(56,"b"),fill=PAPER)
    for i,l in enumerate(labels):
        x=150+i*360; y=180; on=(i==lit)
        d.rectangle([x,y,x+240,y+400],fill=(232,170,90) if on else (36,32,29),outline=PAPER if on else GREY,width=5)
        d.ellipse([x+200,y+200,x+216,y+216],fill=INK if on else GREY)
        d.text((x+20,y+20),f"PATH {i+1}",font=F(22,"m"),fill=INK if on else GREY)
        d.text((x+120-d.textlength(l,font=F(30,"b"))/2,y+420),l,font=F(30,"b"),fill=ORANGE if on else GREY)
    return tag(im,t,src)
def hub(centre, spokes, title="", t="", src=""):
    im=ledger(); d=ImageDraw.Draw(im); cx,cy=640,400
    if title: d.text((86,60),title,font=F(52,"b"),fill=PAPER)
    pts=[(cx-380,cy-120),(cx+380,cy-120),(cx,cy+230)]
    for (x,y),s in zip(pts,spokes):
        d.line([cx,cy,x,y],fill=RED,width=4); c=paper_rect((300,80),PAPER,False,len(s)); cd=ImageDraw.Draw(c)
        cd.text((150-cd.textlength(s.upper(),font=F(28,"xb"))/2,22),s.upper(),font=F(28,"xb"),fill=(30,26,22)); im=drop(im.convert("RGBA"),c,(int(x-150),int(y-40)),0,8).convert("RGB")
    d=ImageDraw.Draw(im); d.ellipse([cx-110,cy-110,cx+110,cy+110],fill=ORANGE); d.text((cx-d.textlength(centre,font=F(40,"b"))/2,cy-24),centre,font=F(40,"b"),fill=INK)
    return tag(im,t,src)
def crates(n=7, title="", sub="", st=None):
    im=ledger(); d=ImageDraw.Draw(im)
    if title: d.text((86,60),title,font=F(56,"b"),fill=PAPER)
    if sub: d.text((92,130),sub,font=F(32,"s"),fill=ORANGE)
    for i in range(n):
        x=200+(i%4)*230-(i//4)*-115; y=470-(i//4)*170
        d.rectangle([x,y,x+210,y+160],fill=(150,112,70),outline=(90,62,40),width=5); d.line([x,y,x+210,y+160],fill=(110,80,50),width=4); d.line([x+210,y,x,y+160],fill=(110,80,50),width=4)
        d.text((x+60,y+62),"NVDA?",font=F(26,"mono"),fill=(60,40,20))
    if st: s=stamp(st,RED,64); im=im.convert("RGBA"); im.paste(s,(820,150),s); im=im.convert("RGB")
    return im
def beat(line, sub=""):
    im=Image.new("RGB",(W,H),(8,7,6)); d=ImageDraw.Draw(im); w=d.textlength(line,font=F(46,"s"))
    d.text(((W-w)/2,H/2-40),line,font=F(46,"s"),fill=(150,140,124))
    if sub: d.text(((W-d.textlength(sub,font=F(26,"m")))/2,H/2+30),sub,font=F(26,"m"),fill=GREY)
    return im
def statement_paper():
    return receipt([("Pension statement",""),("Top holding","NVDA"),("Share of fund","≈ 7%")],title="YOUR STATEMENT",sub="EXAMPLE · S&P 500 FUND")

RECEIPT_LINES=[("Your Nvidia slice","≈ $10,000"),("One morning · 9 Nov","≈ -$880"),("The chip trail","$4.8BN · NOT KNOWN"),("Your apps · servers","+15% · NOT PRICED"),("Watch","17 NOV · 18 NOV")]
def rc(n, st=None): return receipt(RECEIPT_LINES[:n],title="THE RECEIPT",st=st,sub="INV-010 · EXAMPLE AVERAGE 401(k)")

SPEC={
"CO-01":lambda: memo(["To all employees,","I want to be honest with you.","I was unfaithful to my wife.","The board is reviewing reports..."],2,t="REPORTED",src="AP; NYT"),
"CO-02":lambda: footage(ph("CO-02"),"The Nvidia spy scandal","≈ -$400bn at one point · 9 Nov 2026",t="REPORTED",src="BLOOMBERG VIA TNW"),
"CO-03":lambda: cents(7,"≈ $10,000","of an average 401(k) sits in Nvidia, if it tracks the S&P 500",t="ILLUSTRATION",src="SPDR; FIDELITY; OUR MATHS"),
"CO-04":lambda: typed([["No charges","against anyone"],["Nvidia","denies"],["China","denies"]],[("CONFIRMED",GREEN),("REPORTED",ORANGE),"SUSPECTED"]),
"CO-05":lambda: _s9.road6(["The money","The dinner","The boxes","The probe","Your account"],"Where this goes"),
"P1-01":lambda: part(1,"The $400 Billion Morning","How much Nvidia lost, and why it's in your 401(k)"),
"P1-02":lambda: footage(ph("P1-02"),"Sunday 8 November 2026","the memo",t="REPORTED",src="AP; AL JAZEERA"),
"P1-02b":lambda: timeline([("1993","co-founded","START-UP"),("1999+","graphics cards","GAMING"),("2020s","AI data centres","AI"),("2026","≈ $4.5 trillion","No.1")],"33 years, one CEO",t="REPORTED",src="DECRYPT; AL JAZEERA"),
"P1-03":lambda: footage(ph("P1-03"),"Board probe opened","foreign intelligence target?",t="REPORTED",src="NVIDIA BOARD"),
"P1-04":lambda: letter("Nvidia board","no reason to believe national security or company secrets were compromised","Board statement","8 November 2026",t="REPORTED",src="NVIDIA BOARD"),
"P1-05":lambda: footage(ph("P1-05"),"S&P 500 up · NVDA down","-8.8% at the low · 9 Nov",t="REPORTED",src="BLOOMBERG; DECRYPT"),
"P1-06":lambda: footage(ph("P1-06"),"≈ $400bn in hours","on a memo about a marriage",t="REPORTED",src="BLOOMBERG"),
"P1-07":lambda: odometer("$4.51T","From $5.78T","6 Oct → 6 Nov 2026 · AI sell-off",t="REPORTED",src="YCHARTS VIA DECRYPT"),
"P1-07b":lambda: ticket("Nvidia · fiscal 2026","$215.9 BILLION",["revenue · profit ≈ $120bn","9 in 10 dollars: data centres"],st="FY2026",t="VERIFIED",src="NVIDIA VIA THE REGISTER"),
"P1-08":lambda: donut(6.93,"of the S&P 500 is Nvidia","the 'Big 7' ≈ 30%","One company",t="REPORTED",src="SPDR VIA DECRYPT; YARDENI"),
"P1-09":lambda: footage(ph("P1-09"),"54% of US households","have a 401(k)",t="REPORTED",src="FEDERAL RESERVE VIA FORTUNE"),
"P1-10":lambda: ledgerbook([("Average 401(k) · Q3 2025","$144,400"),("× Nvidia share of S&P 500","6.93%"),("= your Nvidia slice","≈ $10,000"),("× -8.8% at the low, 9 Nov","≈ -$880")],"If it all tracks the S&P 500",t="ILLUSTRATION",src="FIDELITY; OUR MATHS"),
"P1-11":lambda: footage(ph("P1-11"),"≈ 5% of the global index","Nvidia: the No.1 holding",t="REPORTED",src="MSCI ACWI VIA CRYPTO BRIEFING"),
"P1-12":lambda: chair("Who is she?","and how did she reach his table?"),
"BR-01":lambda: envelope("What Happens If China Invades Taiwan?","SUBSCRIBE"),
"P2-01":lambda: part(2,"The Dinner in Taipei","Who is Alice Huang?"),
"P2-02":lambda: dossier([("Name","Huang Le ('Alice')"),("Citizenship","Chinese"),("Relation to Jensen Huang","none · shared surname"),("Charges","none reported")],t="REPORTED",src="NYT; AL JAZEERA"),
"P2-03":lambda: document("Singapore company filing · March 2023",[("Old name","7Road International"),("New name","Megaspeed"),("Managing director","Huang Le"),("Business","AI computing")],hi=1,t="REPORTED",src="FILINGS VIA OPEN MAGAZINE"),
"P2-04":lambda: footage(ph("P2-04"),"Taipei · June 2024","photographed side by side",t="REPORTED",src="OPEN MAGAZINE"),
"P2-05":lambda: calendar([("JUN","2024","Taipei event"),("MAY","22","the dinner · 2025"),("OCT","29","NYT · 2026")],"Computex, Taipei",t="REPORTED",src="AL JAZEERA; OPEN MAGAZINE"),
"P2-05b":lambda: footage(ph("P2-05b"),"'Not unusual'","Nvidia on CEO meetings with customers",t="CLAIM",src="NVIDIA VIA NYT"),
"P2-05c":lambda: chair("They were watching her","according to the New York Times",lit=True),
"P2-06":lambda: inset(footage(ph("P2-06"),"New York Times · 29 Oct 2026","US officials: a Chinese intelligence asset",t="REPORTED",src="NYT"),clipping("The New York Times (recreated)","US officials see Nvidia chief as target of Chinese spy plot","","29 October 2026")),
"P2-07":lambda: map_((104,18,128,44),hi=["China","Taiwan"],arcs=[(BJ,TPE)],pins=[(*BJ,"BEIJING · MSS?"),(*TPE,"TAIPEI → SANTA CLARA")],title="'To gather information'",sub="and possibly steer chip sales",t="REPORTED",src="NYT; FT"),
"P2-08":lambda: checklist("Three unknowns",[("What she learned",False),("What it was worth",False),("Where she is now",False)],st="UNKNOWN",t="REPORTED",src="NYT; AL JAZEERA"),
"P2-09":lambda: inset(footage(ph("P2-09"),"Singapore: no probe of her","police are investigating Megaspeed",t="REPORTED",src="OPEN MAGAZINE; TNW"),bubbles([("Singapore","no such investigation"),("China","smears")],"")),
"P2-10":lambda: beat("History has a name for it."),
"P3-01":lambda: part(3,"The Oldest Trick","Chinese spy cultivation: past cases"),
"P3-02":lambda: pinboard([["CULTIVATION","build a relationship","with someone close to power"],["the tabloids say","'honeypot'"]],""),
"P3-03":lambda: clipping("Axios (recreated)","Suspected Chinese spy targeted California politicians","The congressman she helped was never accused of wrongdoing","December 2020"),
"P3-04":lambda: footage(ph("P3-04"),"MI5 interference alert","January 2022 · Christine Lee",t="REPORTED",src="MI5 VIA BBC"),
"P3-05":lambda: figures(3,tags=[("2011-15 · US","Politicians"),("2022 · UK","Parliament"),("2026 · target?","Chip CEO")]),
"P3-06":lambda: footage(ph("P3-06"),"October 2025","the President is briefed",t="REPORTED",src="NYT"),
"P3-07":lambda: document("NYT report · 29 October 2026 (recreated)",[("Briefed","about a year ago"),("Action","chose not to act"),("Reason (reported)","chip sales, China trade"),("Defensive briefing","never given")],hi=1,t="REPORTED",src="NYT"),
"P3-07b":lambda: halves(("THEN",["officials:","he didn't know","who she was"],NAVY),("NOW",["some senior","officials","doubt it"],RED),"According to the New York Times"),
"P3-08":lambda: quote("I haven't heard he's done anything wrong.","The President, on Jensen Huang","8 November 2026",t="REPORTED",src="TNW; AL JAZEERA"),
"P3-09":lambda: footage(ph("P3-09"),"Why would a spy service care?","open the boxes"),
"P4-01":lambda: part(4,"The Boxes in Malaysia","Megaspeed and the $4.8 billion chip trail"),
"P4-02":lambda: footage(ph("P4-02"),"Blackwell","banned for sale to China",t="REPORTED",src="AL JAZEERA"),
"P4-03":lambda: inset(footage(ph("P4-03"),"H200 ≈ 6× the H20","25% of certain sales to Washington",t="REPORTED",src="AL JAZEERA; NYT"),scale(("H20","before",GREY),("H200","≈ 6×",ORANGE),"")),
"P4-03b":lambda: tiles([("Data centre · Q2",None,"$89bn"),("China H200",None,"< 1%"),("Next forecast: China",None,"$0")],"China matters less than it used to",t="REPORTED",src="TNW, AUG 2026"),
"P4-04":lambda: map_(SEA,hi=["Malaysia","Singapore"],pins=[(*SG,"SINGAPORE · MEGASPEED"),(*KL,"MALAYSIA")],lanes=[([(101.7,3.1),(108,12),(113,20),(114,25)],ORANGE)],title="Where Megaspeed works",sub="and where the chips might go",t="REPORTED",src="NYT"),
"P4-05":lambda: footage(ph("P4-05"),"Malaysia · late 2024","Nvidia equipment still in its boxes",t="REPORTED",src="NYT"),
"P4-06":lambda: inset(footage(ph("P4-06"),"≥ $4.8bn of Nvidia-chip equipment","Jun 2024 - Feb 2026 · Malaysia",t="REPORTED",src="IMPORTGENIUS VIA NYT"),flap([("BOUGHT","≥ $4.8BN")],"")),
"P4-07":lambda: flow([("Inspur US arm","parent blacklisted"),("Megaspeed","buys equipment"),("Alibaba","rents computing"),("Proof?","purchases ≠ proof")],"What the Times reports","none of this is a charge"),
"P4-08":lambda: footage(ph("P4-08"),"Both deny","Megaspeed: no smuggling · Nvidia: like any customer",t="CLAIM",src="MEGASPEED; NVIDIA"),
"P4-09":lambda: receipt([("Off the company · 9 Nov","≈ $400BN"),("Avg 401(k) riding on it","≈ $10,000"),("Chips in question","≈ $4.8BN")],title="THE BILL SO FAR",st="HALF-RECEIPT",sub="INV-010 · WHAT WE KNOW"),
"P4-10":lambda: footage(ph("P4-10"),"And then","the investigation stopped"),
"P5-01":lambda: part(5,"The Probe That Stopped","Why the chip smuggling probe stalled"),
"P5-02":lambda: footage(ph("P5-02"),"Commerce · BIS","the Megaspeed file",t="REPORTED",src="NYT VIA TNW"),
"P5-03":lambda: footage(ph("P5-03"),"August 2025 · the email","Nvidia's lawyer to the agents",t="REPORTED",src="NYT"),
"P5-04":lambda: timeline([("Aug 2025","email","SENT"),("Agents","refuse to meet","REFUSED"),("DOJ","asks for pause","PAUSED"),("2026","criminal inquiry?","REPORTED")],"How the probe moved",t="REPORTED",src="NYT VIA TNW"),
"P5-05":lambda: clipboards(("Commerce","handled it strictly by the book"),("Nvidia","we talk to officials to answer questions")),
"P5-06":lambda: number("0","companies added to the entity list in over a year","COMMERCE BLACKLIST","REPORTED","TNW, NOV 2026"),
"P5-06b":lambda: notebook("...the close relationship has stalled some investigations and proposed sanctions","Current and former officials, quoted by the NYT","29 October 2026",t="REPORTED",src="NYT"),
"P5-07":lambda: footage(ph("P5-07"),"Shareholder suit · 9 Nov","'hid his ties to a suspected spy'",t="REPORTED",src="REUTERS"),
"P5-08":lambda: footage(ph("P5-08"),"Congress · 18 November","closed-door briefing requested",t="REPORTED",src="OPEN MAGAZINE; AL JAZEERA"),
"P5-09":lambda: calendar([("NOV","17","results"),("NOV","18","Congress")],"Two dates that move your fund",t="REPORTED",src="TNW; DECRYPT"),
"P5-10":lambda: inset(footage(ph("P5-10"),"So what happens","to your account?"),statement_paper()),
"P6-01":lambda: part(6,"What Happens Next","What happens to Nvidia now"),
"P6-02":lambda: doors(0,t="REPORTED",src="DECRYPT (DAN IVES)"),
"P6-03":lambda: doors(1,t="REPORTED",src="DECRYPT (CHRIS WESTON)"),
"P6-03b":lambda: hub("HUANG",["Customers","TSMC","Washington"],"One man, three lines",t="REPORTED",src="DECRYPT"),
"P6-04":lambda: typed([["Scenarios,","not forecasts"]],["SCENARIO"]),
"P6-05":lambda: doors(2,t="REPORTED",src="AL JAZEERA (ANALYSTS)"),
"P6-05b":lambda: footage(ph("P6-05b"),"Servers +15%","from early 2027",t="REPORTED",src="TNW, AUG 2026"),
"P6-05c":lambda: pricetags([("Servers, early 2027","+15%"),("Tighter rules","+?"),("Your apps","not priced")],"It arrives every month",t="SCENARIO"),
"P6-06":lambda: footage(ph("P6-06"),"The part no model prices","",t="REPORTED",src="NYT"),
"P6-07":lambda: checklist("What nobody knows",[("What, if anything, she learned",False),("Whether he knew who she was",False),("Whether chips reached China",False),("Whether anyone is charged",False)],st="UNKNOWN"),
"P6-08":lambda: receipt([],title="THE RECEIPT",sub="INV-010 · PRINTING..."),
"RC-01":lambda: rc(0,"ILLUSTRATION"),
"RC-02":lambda: inset(footage(ph("RC-02"),"Line 1 · your Nvidia slice","≈ $10,000 of an average 401(k)",t="ILLUSTRATION",src="OUR MATHS"),rc(1)),
"RC-03":lambda: rc(2),
"RC-04":lambda: rc(3),
"RC-04b":lambda: inset(footage(ph("RC-04b"),"Line 4 · your apps","servers +15% · not priced",t="REPORTED",src="TNW"),rc(4)),
"RC-05":lambda: rc(5,"WATCH"),
"RC-06":lambda: inset(footage(ph("RC-06"),"Not financial advice","check your top 10 holdings"),checklist("Open your statement",[("How much is in the top 5-10?",True)])),
"RC-07":lambda: steps([("1","Ask your provider"),("2","Don't trade headlines")],"What you can do"),
"RC-08":lambda: comment("Should one company be this big a part of everyone's retirement?","and where are you watching from?"),
"RC-09":lambda: footage(ph("RC-09"),"Every crisis sends a bill.","History keeps the receipts."),
}
DESC={}
