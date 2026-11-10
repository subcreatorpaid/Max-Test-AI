# INV-008 storyboard SPEC: one panel per script row, in kit v2 (ledger look). ST = stills dir (set by build).
import kit
from kit import *
from kit2 import *
import pathlib, sys
sys.path.insert(0, str(kit.ROOT/"tools/inv008"))
import visuals_v1 as V
# per-video grade map (kit.GRADE is keyed by code; reset it for INV-008)
kit.GRADE.clear(); kit.GRADE.update({**{c:"shadow" for c in V.SHADOW},**{c:"high" for c in V.HIGH},**{c:"low" for c in V.LOW}})
ST="."
def ph(c): return f"{ST}/{c}.jpg"
MIDEAST=(20,10,65,42); WORLD=(-130,-35,150,65); UK=(-11,49.5,3,59.5); EUROPE=(-12,35,32,63)
def line(pts, title, sub, labels, t="", src="", yfmt="${:.2f}"):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER); d.text((92,140),sub,font=F(30,"s"),fill=ORANGE)
    x0,x1,y0,y1=140,W-140,600,230; mx=max(pts)
    for k in range(4): y=y0-(y0-y1)*k/3; d.line([x0,y,x1,y],fill=(40,36,32),width=1)
    P=[(x0+(x1-x0)*i/(len(pts)-1), y0-(y0-y1)*v/mx) for i,v in enumerate(pts)]
    d.line(P,fill=ORANGE,width=6)
    for (x,y),v,lab in zip(P,pts,labels):
        d.ellipse([x-8,y-8,x+8,y+8],fill=ORANGE); d.text((x-40,y-50),yfmt.format(v),font=F(30,"b"),fill=PAPER); d.text((x-40,y0+16),lab,font=F(22,"m"),fill=GREY)
    return tag(im,t,src)
def plate(a,b,title,sub):
    im=ledger().convert("RGBA"); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER); d.text((92,140),sub,font=F(30,"s"),fill=ORANGE)
    for i,(num,lab) in enumerate((a,b)):
        p=paper_rect((440,200),PAPER2,False,60+i); pd=ImageDraw.Draw(p); pd.rounded_rectangle([8,8,432,192],16,outline=INK,width=6)
        pd.text((40,50),num,font=F(96,"mono"),fill=INK); im=drop(im,p,(150+i*560,280),[-2,2][i],10); d=ImageDraw.Draw(im)
        d.text((150+i*560,510),lab,font=F(30,"b"),fill=ORANGE if i else GREY)
    return im.convert("RGB")
def week(dark_days,title,sub,t="",src=""):
    im=ledger(); d=ImageDraw.Draw(im); d.text((86,70),title,font=F(56,"b"),fill=PAPER); d.text((92,140),sub,font=F(30,"s"),fill=ORANGE)
    for i,dn in enumerate("MON TUE WED THU FRI SAT SUN".split()):
        x=90+i*160; on=i not in dark_days
        d.rectangle([x,260,x+140,520],fill=PAPER if on else (30,27,24),outline=(60,55,50)); d.text((x+30,280),dn,font=F(34,"b"),fill=INK if on else DIM)
        if on: d.ellipse([x+45,380,x+95,430],fill=ORANGE)
    return tag(im,t,src)
SPEC={
"CO-01":lambda: footage(ph("CO-01"),"Oregon","winter 1973",glow=(640,330),t="VERIFIED",src="PDX MONTHLY"),
"CO-02":lambda: flap([("BEFORE","$2.90"),("JAN 1974","$11.65"),("DRY","1 IN 5")],"1973 oil crisis · price of a barrel",t="VERIFIED",src="FED. RESERVE HISTORY"),
"CO-03":lambda: versus(("1973",4.5),("2026",14),"Barrels lost a day (millions)",t="REPORTED",src="MAJALLA CITING IEA"),
"CO-04":lambda: footage(ph("CO-04"),"+$1 a gallon","on a year earlier · Nov 2026",corner="+$1",t="VERIFIED",src="AAA"),
"CO-05":lambda: typed([["Old records","1973-75"],["This year","2026"],["Our maths","shown"]],["VERIFIED","REPORTED",("ESTIMATE",ORANGE)]),
"CO-06":lambda: roadmap(["The week","The queue","The long bill","Your table"],"Where this goes"),
"P1-01":lambda: part(1,"The Week It Started","How the 1973 oil embargo began"),
"P1-02":lambda: map_(MIDEAST,hi=["Saudi Arabia","Egypt"],pins=[(46.7,24.7,"RIYADH · AUG 1973"),(31.2,30.0,"CAIRO")],arcs=[((46.7,24.7),(31.2,30.0))],title="“The oil weapon”",sub="Faisal and Sadat agree",t="REPORTED",src="WIKIPEDIA"),
"P1-03":lambda: timeline([("6 Oct","war begins",""),("12-14 Oct","US airlift to Israel",""),("16 Oct","price +70%","")],"October 1973",t="VERIFIED",src="OFFICE OF THE HISTORIAN"),
"P1-04":lambda: document("Posted price · Gulf crude",[("Before 16 Oct","≈$3.00"),("16 Oct 1973","≈$5.12"),("Change","+70%")],hi=2,t="REPORTED",src="WIKIPEDIA (VERIFY)"),
"P1-05":lambda: calendar([("OCT","-5%","then"),("NOV","-5%","more"),("DEC","-5%","every month")],"OAPEC cuts · 17 Oct 1973",t="VERIFIED",src="OAPEC"),
"P1-06":lambda: clipping("THE MORNING LEDGER","Arab producers cut off oil to U.S.","Libya first, Saudi Arabia next","20 October 1973",t="VERIFIED",src="FED. RESERVE HISTORY"),
"P1-07":lambda: map_(WORLD,hi=["United States of America","Netherlands","Portugal","South Africa","Zimbabwe"],title="Embargoed",sub="US · Netherlands · later 3 more",t="VERIFIED",src="OFFICE OF THE HISTORIAN"),
"P1-08":lambda: footage(ph("P1-08"),"Spare capacity ≈ 1%","US fields pumping flat out",t="REPORTED",src="MAJALLA / FED (BURNS)"),
"P1-09":lambda: line([2.90,5.12,11.65],"$2.90 → $11.65","a barrel, in about 90 days",["SEP 73","OCT 73","JAN 74"],t="VERIFIED",src="FED. RESERVE HISTORY"),
"P1-10":lambda: pricetags([("1973, in 2026 $","≈$22"),("Jan 1974, in 2026 $","≈$80")],"In today's money",t="ESTIMATE",src="OUR MATHS · BLS CPI"),
"P1-11":lambda: footage(ph("P1-11"),"38.5¢ → 55.1¢","a gallon, May 1973 → June 1974",corner="+43%",t="REPORTED",src="CONTEMPORARY DATA"),
"P1-12":lambda: receipt([("Fuel (example family)","+$68/mo")],"THE 1973 INVOICE",st="ESTIMATE",stcol=ORANGE,sub="INV-008 · IN 2026 DOLLARS"),
"P1-13":lambda: footage(ph("P1-13"),"Where did the time go?",""),
"BR-01":lambda: envelope("The Hunger Bill: Hormuz on your plate","SUBSCRIBE"),
"P2-01":lambda: part(2,"The Queue","The 1973 gas lines"),
"P2-02":lambda: notice("The White House","Project Independence","A goal: no foreign oil. Announced 7 November 1973.",st="GOAL",t="VERIFIED",src="OFFICE OF THE HISTORIAN"),
"P2-03":lambda: footage(ph("P2-03"),"“As high as 17 percent”","Nixon's address · 25 Nov 1973",t="VERIFIED",src="UCSB PRESIDENCY PROJECT"),
"P2-04":lambda: footage(ph("P2-04"),"68°F","closed Sat 9pm-Sun · heating oil -15%",t="VERIFIED",src="UCSB, 25 NOV 1973"),
"P2-05":lambda: footage(ph("P2-05"),"90% complied","weekend closing",t="REPORTED",src="WIKIPEDIA"),
"P2-06":lambda: plate(("OBX 213","ODD DAYS"),("OBX 214","EVEN DAYS"),"Odd plates, odd days","last digit decides when you buy"),
"P2-07":lambda: figures(5,tags=[("Feb 1974","1 in 5"),("Stations","dry")],t="REPORTED",src="WIKIPEDIA (VERIFY)"),
"P2-08":lambda: footage(ph("P2-08"),"55 mph","1974 → 1995",t="VERIFIED",src="OFFICE OF THE HISTORIAN"),
"P2-09":lambda: odometer("6:00","School in the dark","year-round daylight saving · from 6 January 1974",t="VERIFIED",src="WIKIPEDIA"),
"P2-10":lambda: footage(ph("P2-10"),"-3.7% road fuel","110.4 → 106.3 billion gallons",t="VERIFIED",src="FHWA"),
"P2-11":lambda: footage(ph("P2-11"),"11.9 mpg","average US vehicle, 1973",t="VERIFIED",src="FHWA"),
"P2-12":lambda: receipt([("Fuel (example family)","+$68/mo"),("Time","queues · 68°F")],"THE 1973 INVOICE",sub="INV-008 · LINE 2"),
"P3-01":lambda: part(3,"The Dark","Britain's three-day week"),
"P3-02":lambda: map_(UK,hi=["United Kingdom"],title="Oil ≈ 46%",sub="of Britain's energy, 1973",t="REPORTED",src="RAC FOUNDATION"),
"P3-03":lambda: footage(ph("P3-03"),"50 mph","law by December 1973",t="VERIFIED",src="RAC FOUNDATION"),
"P3-04":lambda: ticket("Motor fuel ration book","29 NOV 1973",["issued to every motorist","binned from July 1975"],st="NEVER USED",t="VERIFIED",src="RAC FOUNDATION · HANSARD"),
"P3-05":lambda: week([3,4,5,6],"The three-day week","from 1 January 1974",t="VERIFIED",src="WIKIPEDIA"),
"P3-06":lambda: footage(ph("P3-06"),"TV off at 10:30 pm","heat one room",t="VERIFIED",src="WIKIPEDIA"),
"P3-07":lambda: pump("72p","a gallon by end-1974 · was 36p in mid-1973",label="UK PETROL",t="VERIFIED",src="RAC FOUNDATION"),
"P3-08":lambda: footage(ph("P3-08"),"81% voted to strike","24 January 1974",t="VERIFIED",src="WIKIPEDIA"),
"P3-09":lambda: progress("Hung parliament","February 1974",0.49,"Heath loses his majority · Wilson forms a minority government",st="NO MAJORITY",t="VERIFIED",src="WIKIPEDIA"),
"P3-10":lambda: footage(ph("P3-10"),"Car-free Sundays","Netherlands · from 4 Nov 1973",t="VERIFIED",src="JALOPNIK; WIKIPEDIA"),
"P3-11":lambda: map_(EUROPE,hi=["Netherlands","United Kingdom","Germany","Italy","Switzerland","Norway"],title="Sunday bans",sub="driving, flying, boating",t="REPORTED",src="WIKIPEDIA"),
"P3-12":lambda: map_((120,22,150,46),hi=["Japan"],pins=[(139.7,35.7,"TOKYO")],title="Japan · 90%",sub="of its oil from the Middle East, 1973",t="REPORTED",src="WIKIPEDIA · ASAHI"),
"P3-13":lambda: receipt([("Fuel (example family)","+$68/mo"),("Time","queues · 68°F"),("Power","3-day week · petrol x2")],"THE 1973 INVOICE",sub="INV-008 · LINE 3"),
"P4-01":lambda: part(4,"The Long Bill","Inflation, jobs and a recession"),
"P4-02":lambda: line([2.90,11.65,11.65,15.0],"The embargo ends. The price stays.","a barrel, 1973 → 1974",["SEP 73","JAN 74","MAR 74","NOV 74"],t="VERIFIED / REPORTED",src="FED · RAC FOUNDATION"),
"P4-03":lambda: footage(ph("P4-03"),"Oil is in everything","the lorry, the packet, the factory"),
"P4-04":lambda: columns(["1973","1974"],[6.2,11.0],hi=1,title="US inflation",sub="6.2% → 11.0%",t="VERIFIED",src="BLS"),
"P4-05":lambda: footage(ph("P4-05"),"+$330 a month","example: a $3,000 monthly budget",t="ESTIMATE",src="OUR MATHS · BLS"),
"P4-06":lambda: scale(("June 1974","£1.00",INKT),("June 1975","£1.26",RED),"UK prices +26.1%",t="VERIFIED",src="HANSARD, 7 AUG 1975"),
"P4-07":lambda: footage(ph("P4-07"),"2.3 million jobs","US recession · Nov 1973-Mar 1975",t="REPORTED",src="NBER · BLS"),
"P4-08":lambda: line([4.6,9.0,6.0],"9% unemployment","peak, May 1975",["1973","MAY 75","JUN 78"],t="VERIFIED",src="BLS",yfmt="{:.1f}%"),
"P4-09":lambda: tiles([("UK GDP",None,"-3.9%"),("Recovery",None,"14 qtrs")],"UK recession · 1973-75",t="REPORTED",src="WIKIPEDIA"),
"P4-10":lambda: letter("Federal Reserve History","US industrial prices were already rising above 10% a year in mid-1973","Arthur Burns, Fed chair (1974), cited","Essay, 22 Nov 2013",t="VERIFIED"),
"P4-11":lambda: footage(ph("P4-11"),"Whoever controls it","can squeeze you"),
"P4-12":lambda: receipt([("Fuel (example family)","+$68/mo"),("Time","queues · 68°F"),("Power","3-day week"),("Prices","US +11% · UK +26%"),("Jobs","2.3 million")],"THE INVOICE SO FAR",sub="INV-008 · HALF-RECEIPT"),
"P4-13":lambda: number("Did it work?","what the world built so this never happens again","THE FIX"),
"P5-01":lambda: part(5,"The Fix","What changed after 1973"),
"P5-02":lambda: progress("90 days","of imports, kept in storage · IEA, 1974",1.0,"every member must hold it",st="",t="VERIFIED",src="IEA"),
"P5-03":lambda: footage(ph("P5-03"),"Strategic Petroleum Reserve","created 1975 · + fuel economy rules",t="VERIFIED",src="OFFICE OF THE HISTORIAN"),
"P5-04":lambda: bars([("1973",1.0,"≈1.0"),("2019",0.43,"0.43")],"Oil per $1,000 of world GDP","-56%",t="VERIFIED",src="COLUMBIA CGEP, 2021",hi=1),
"P5-05":lambda: footage(ph("P5-05"),"Net exporter","USA, 2020 · first since at least 1949",t="VERIFIED",src="EIA"),
"P5-06":lambda: steps([("1991-2011","3 releases"),("2022","2 releases"),("2026","the largest")],"IEA emergency releases",t="VERIFIED",src="IEA"),
"P5-07":lambda: filmyear("2026","3x the oil lost of 1973. So why is our bill different?"),
"P6-01":lambda: part(6,"1973 vs 2026","Why there are no gas lines now"),
"P6-02":lambda: footage(ph("P6-02"),"$72 → $126","Brent, 2026 · +74%",corner="$126",t="REPORTED",src="MAJALLA (IEA)"),
"P6-03":lambda: scale(("1973","x4",RED),("2026","+74%",INKT),"Smaller loss, bigger jump",t="VERIFIED / REPORTED",src="FED · MAJALLA"),
"P6-04":lambda: versus(("1974 peak*",80),("10 Nov 2026",89),"Barrel, in 2026 dollars",t="ESTIMATE",src="OUR MATHS · TRADING ECONOMICS"),
"P6-05":lambda: footage(ph("P6-05"),"1973 paid in time","2026 pays in price"),
"P6-06":lambda: footage(ph("P6-06"),"$3.06 → $4.01","a gallon · Nov 2025 → Nov 2026",corner="$4.01",t="VERIFIED",src="AAA"),
"P6-07":lambda: clipboards(("1974, in 2026 $","+$68 a month on fuel"),("2026","+$57 a month on fuel"),t="ESTIMATE",src="OUR MATHS · EXAMPLE FAMILY"),
"P6-08":lambda: pricetags([("1974 gallon, in 2026 $","$3.77"),("9 Nov 2026","$4.01")],"A gallon, in today's money",t="ESTIMATE",src="OUR MATHS · BLS CPI"),
"P6-09":lambda: footage(ph("P6-09"),"Prices +3.7%","US, year to Sep 2026 · petrol +34%",t="VERIFIED",src="BLS"),
"P6-10":lambda: bubbles([("1974","+$330 a month"),("2026, so far","+$111 a month")],"Example: a $3,000 monthly budget"),
"P6-11":lambda: footage(ph("P6-11"),"284.6M barrels","US reserve · lowest since 1982",t="REPORTED",src="MAJALLA, SEP 2026"),
"P6-12":lambda: number("1979","the sequel: a second shock, six years later","WORLD BANK BAD CASE · GROWTH 1.3%",t="REPORTED",src="WORLD BANK",faded="1973"),
"P6-13":lambda: footage(ph("P6-13"),"Supply normal","Japan's paper makers · March 2026",t="REPORTED",src="ASAHI"),
"P6-14":lambda: number("The full invoice","then and now","THE RECEIPT"),
"RC-01":lambda: receipt([("","1974  |  2026")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-02":lambda: receipt([("","1974  |  2026"),("Fuel","$68 | $57")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-03":lambda: receipt([("","1974  |  2026"),("Fuel","$68 | $57"),("Prices","$330 | $111")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-04":lambda: receipt([("","1974  |  2026"),("Fuel","$68 | $57"),("Prices","$330 | $111"),("Time","hours | none")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-05":lambda: receipt([("","1974  |  2026"),("Fuel","$68 | $57"),("Prices","$330 | $111"),("Time","hours | none"),("Jobs","2.3M | not yet")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-06":lambda: receipt([("","1974  |  2026"),("Fuel","$68 | $57"),("Prices","$330 | $111"),("Time","hours | none"),("Jobs","2.3M | not yet"),("Cushion","none | thin")],"THE RECEIPT",sub="INV-008 · EXAMPLE FAMILY · 2026 $"),
"RC-07":lambda: footage(ph("RC-07"),"Buffer 3-6 months","+20% stress test"),
"RC-08":lambda: footage(ph("RC-08"),"What does it burn?","don't trade on headlines"),
"RC-09":lambda: comment("Do you remember 1973?","Country · your last fill-up"),
"RC-10":lambda: footage(ph("RC-10"),"Every crisis sends a bill.","History keeps the receipts."),
}
DESC={}
