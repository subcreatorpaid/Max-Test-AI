# INV-024 graphics spec (What If the Iran War Spreads to the Gulf?).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "inv019"))
from kit19 import *

G2 = (46.0, 23.0, 58.9, 31.2)
BAH = (50.63, 25.92); QESHM = (55.9, 26.8); ALI = (47.52, 29.35); TANURA = (50.16, 26.64); LAFFAN = (51.53, 25.91); JEBEL = (55.03, 24.98)
RT = ["THE GULF IS IN THIS WAR", "56 PLANTS MAKE ITS WATER", "ONE STRIKE: GAS × 2", "DUBAI FLIGHTS -31%", "+7p TO +22p A LITRE"]
RUN = [("THE GULF IS IN IT", "LINE 1"), ("56 WATER PLANTS", "LINE 2"), ("GAS × 2", "LINE 3"), ("FLIGHTS -31%", "LINE 4"), ("+7p TO +22p", "LINE 5")]
LNG = [((51.6, 25.9), (56.4, 26.4), ORANGE, 4, None, False), ((56.4, 26.4), (58.5, 22.5), ORANGE, 4, None, False), ((58.5, 22.5), (43.4, 12.6), ORANGE, 4, None, False),
       ((43.4, 12.6), (32.5, 29.9), ORANGE, 4, None, False), ((32.5, 31.2), (5.0, 43.0), ORANGE, 4, 0, False)]
def watch(n): return lambda o, t: checklist(["1 · RAS LAFFAN", "2 · WATER PLANTS", "3 · SAUDI ARABIA", "4 · THE TALKS"][:n], title="WHAT TO WATCH", tag=t)
def gmap(title, pins, t, hi=(), hi2=(), bbox=G2): return map_scene(bbox, z=6, hi=hi, hi2=hi2, title=title, tag=t, pins=pins)

SPEC = {
"CO-01": lambda o, t: gmap("THE WAR REACHES THE GULF", [(BAH[0], BAH[1], "BAHRAIN", RED, -1), (ALI[0], ALI[1], "KUWAIT", RED, -1), (QESHM[0], QESHM[1], "QESHM", ORANGE, 0)], t, hi=("Iran",)),
"CO-02": lambda o, t: quote("Will know no geographical boundaries", "Iran's army chief Amir Hatami", "Nov 2026", tag=t),
"CO-03": lambda o, t: stats3([("1/5", "of the world's LNG", -1), ("95M", "Dubai passengers, 2025", -1), ("90%", "Kuwait's water from the sea", 0)], title="THE GULF ISN'T JUST OIL", tag=t),
"CO-04": lambda o, t: pricetags([("UK · PER LITRE", "+22p", RED, -1), ("US · PER GALLON", "+90¢", RED, 0)], title="WORST CASE: BRENT BACK TO $126 (OUR MATHS)", tag=t),
"CO-05": lambda o, t: roadmap(o, t, ["THIS MONTH", "GLASS HOUSE", "THE GAS", "THE FLIGHTS", "YOUR BILL", "WATCH"]),

"P1-01": P(1, "This month"),
"P1-02": lambda o, t: timeline([("28 FEB 2026", "US and Israel attack Iran"), ("MARCH", "Iran fires at the Gulf")], [1], title="THE WAR", tag=t),
"P1-03": tg(lambda: dots(230, 250, "DRONES FIRED AT BASES HOSTING US TROOPS · IRGC CLAIM", big="230", title="4 MARCH 2026", col=RED)),
"P1-04": lambda o, t: card(["AN 11-YEAR-OLD GIRL,", "KILLED BY SHRAPNEL"], kicker="KUWAIT · 4 MARCH", tag=t),
"P1-05": lambda o, t: gmap("RAS TANURA: SAUDI'S BIGGEST DOMESTIC REFINERY", [(TANURA[0], TANURA[1], "RAS TANURA", RED, 0)], t, hi2=("Saudi Arabia",)),
"P1-06": lambda o, t: stats3([("314", "ballistic missiles", -1), ("15", "cruise missiles", -1), ("1,672", "drones", 0)], title="UAE INTERCEPTS BY MID-MARCH", tag=t),
"P1-07": lambda o, t: timeline([("8 APR", "Ceasefire"), ("SEPT", "Last Gulf attack"), ("OCT", "Quiet")], [2], title="A QUIET AUTUMN", tag=t),
"P1-08": lambda o, t: calendar(["13 NOV", "14", "15", "16", "17", "18"], circles=[(0, "1", -1), (2, "2", -1), (4, "3", -1), (5, "4", 0)], title="BAHRAIN: 4 ATTACKS IN 6 DAYS", tag=t),
"P1-09": lambda o, t: gmap("TARGET: US RADAR, SHEIKH ISA AIR BASE", [(BAH[0], BAH[1], "BAHRAIN", RED, 0)], t, hi2=("Bahrain",)),
"P1-10": lambda o, t: hz(title="17 NOV: US STRIKES QESHM ISLAND", tag=t, labels=[(55.9, 26.55, "QESHM", 30, RED)]),
"P1-11": lambda o, t: gmap("18 NOV: KUWAIT AIR DEFENCES ON", [(ALI[0], ALI[1], "ALI AL SALEM AIR BASE", RED, 0)], t, hi2=("Kuwait",)),
"P1-12": lambda o, t: two_numbers("CREW INJURED", "11", "MISSING", "1", tag=t, note="ADNOC ship, Strait of Hormuz, 17 Nov"),
"P1-13": lambda o, t: two_numbers("US CARRIERS", "3", "KILLED IN KUWAIT", "2", tag=t, note="falling debris, 26-27 Nov"),
"P1-14": lambda o, t: checklist(["KUWAIT: 'ESCALATION'", "SAUDI: 'STRONGEST TERMS'", "GCC: IRAN 'RESPONSIBLE'", "QATAR'S MEDIATION: STALLED"], title="THE GULF REACTS", tag=t),
"P1-15": lambda o, t: map_scene((32.0, 11.0, 60.0, 31.0), z=5, hi=("Yemen",), title="HOUTHIS: THE WHOLE RED SEA COAST", tag=t, pins=[(46.72, 24.69, "RIYADH", RED, 0)]),
"P1-15b": lambda o, t: checklist(["KUWAIT AIRPORT FUEL TANKS HIT", "KUWAIT CUTS OIL OUTPUT", "DRONE AT SHAYBAH OIL FIELD"], title="NOT JUST BASES · MARCH 2026", tag=t),
"P1-16": lambda o, t: card(["NOT IF.", "HOW FAR."], tag=t),
"P1-17": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0),

"BR-01": sub_card(7, "THE NEXT IRAN WAR BILL", of=7),

"P2-01": P(2, "A glass house"),
"P2-02": lambda o, t: card(["THE GULF", "DRINKS THE SEA"], tag=t),
"P2-03": lambda o, t: bars([("KUWAIT", 90), ("OMAN", 86), ("SAUDI", 70)], title="DRINKING WATER FROM DESALINATION, %", unit="%", hi=0, tag=t, cues=[-1, -1, 0]),
"P2-04": tg(lambda: dots(56, 60, "MAKE OVER 90% OF THE GULF'S DESALINATED WATER · CIA 2010", big="56", title="56 PLANTS", col=CYAN)),
"P2-05": lambda o, t: quote("Would have to evacuate within a week", "Leaked US cable, on Riyadh and the Jubail plant", "2008", tag=t),
"P2-05b": lambda o, t: gmap("JEBEL ALI: STRIKES 12 MILES FROM A GIANT WATER PLANT", [(JEBEL[0], JEBEL[1], "JEBEL ALI", RED, 0)], t, hi2=("United Arab Emirates",)),
"P2-06": lambda o, t: card(["THIS YEAR:", "TARGETS."], tag=t),
"P2-07": lambda o, t: gmap("MARCH: DESALINATION PLANT HIT IN BAHRAIN", [(BAH[0], BAH[1], "BAHRAIN", RED, 0)], t, hi2=("Bahrain",)),
"P2-08": lambda o, t: timeline([("APR 2026", "2 Kuwaiti plants"), ("JUL 2026", "1 more")], [1], title="KUWAIT'S POWER AND WATER", tag=t),
"P2-09": lambda o, t: chain(["POWER", "WATER", "TAPS"], title="HIT THE POWER, LOSE THE WATER", tag=t),
"P2-10": lambda o, t: timeline([("1991", "Iraq wrecks Kuwait's power and water"), ("YEARS", "To recover")], [1], title="KUWAIT HAS BEEN HERE", tag=t),
"P2-11": lambda o, t: card(["IRAN: US STRIKE CUT WATER", "TO 30 VILLAGES"], kicker="IRAN'S CLAIM · NOT ACKNOWLEDGED", tag=t, stamp_txt="CLAIM"),
"P2-11b": lambda o, t: gauge(10, "Tehran's reservoirs, March 2026", tag=t),
"P2-12": lambda o, t: chain(["WATER", "PEOPLE", "OIL", "GAS"], title="NO WATER, NO OIL", tag=t),
"P2-12b": lambda o, t: split(("FIRST", "PEOPLE", "water and power"), ("SECOND", "EXPORTS", "oil and gas"), tag=t),
"P2-13": lambda o, t: card(["A GLASS HOUSE."], tag=t),
"P2-14": lambda o, t: receipt(RUN[:2], title="RUNNING TOTAL", tag=t, show=1),

"P3-01": P(3, "The gas"),
"P3-02": lambda o, t: gmap("RAS LAFFAN · ≈ 1/5 OF THE WORLD'S LNG", [(LAFFAN[0], LAFFAN[1], "RAS LAFFAN", ORANGE, 0)], t, hi2=("Qatar",)),
"P3-03": lambda o, t: typed(["PRODUCTION HALTED", "2 MARCH 2026"], label="QATARENERGY", tag=t, stamps=[("HALTED", 0)], cue_lines=[-1, -1]),
"P3-04": lambda o, t: number("+50%", kicker="UK AND DUTCH WHOLESALE GAS · IN ONE DAY", tag=t),
"P3-04b": lambda o, t: number("-86%", kicker="HORMUZ TRAFFIC · 2 MARCH", sub="≈ 700 ships idle", tag=t),
"P3-04c": lambda o, t: card(["€80-100/MWh?"], kicker="ING'S WARNING", tag=t, stamp_txt="IF QATAR STAYS OFF"),
"P3-05": lambda o, t: gmap("18 MARCH: RAS LAFFAN HIT AGAIN", [(LAFFAN[0], LAFFAN[1], "EXTENSIVE DAMAGE", RED, 0)], t, hi2=("Qatar",)),
"P3-06": lambda o, t: bars([("LATE FEB", 37), ("19 MAR", 74)], title="EUROPEAN GAS, € A MEGAWATT HOUR", unit="", hi=1, tag=t, cues=[-1, 0], reveal=(1, "× 2")),
"P3-07": lambda o, t: number("3-5 YEARS", kicker="TO REPAIR · QATARENERGY CEO", sub="17% of export capacity damaged", tag=t),
"P3-08": lambda o, t: map_scene(WIDE, z=4, hi=("Qatar",), title="EUROPE: 12-14% OF ITS LNG FROM QATAR", tag=t, lines=LNG, pins=[(56.4, 26.4, "HORMUZ", RED, None)]),
"P3-09": lambda o, t: gauge(28.8, "EU gas storage full, 18 March", sub="lowest for the date in 4 years", tag=t),
"P3-10": lambda o, t: number("£2,166", kicker="ENERGY PRICE CAP · FROM 1 JAN 2027", sub="Ofgem", faded="£1,723", tag=t),
"P3-11": lambda o, t: calendar(["JAN", "FEB", "MAR", "APR"], circles=[(3, "NEXT CAP", 0)], title="SHOCK NOW, BILL LATER", tag=t),
"P3-12": lambda o, t: quote("Massively blow up the entirety of the South Pars Gas Field", "President Trump", "Mar 2026", tag=t),
"P3-13": lambda o, t: card(["GAS FOR GAS."], tag=t, stamp_txt="ANALYSIS"),
"P3-14": lambda o, t: receipt(RUN[:3], title="RUNNING TOTAL", tag=t, show=2),

"P4-01": P(4, "The flights"),
"P4-02": lambda o, t: number("95.2M", kicker="DUBAI INTERNATIONAL · PASSENGERS 2025", sub="world's busiest for international travel", tag=t),
"P4-03": lambda o, t: bars([("BY 3 MAR", 21300), ("BY MID-MAR", 37000)], title="FLIGHTS CANCELLED", unit="", hi=1, tag=t, cues=[-1, 0]),
"P4-04": lambda o, t: typed(["DEPART NOW"], label="US STATE DEPARTMENT · 2 MARCH · 14 COUNTRIES", tag=t, cue_lines=[0]),
"P4-05": lambda o, t: pricetags([("DUBAI → EUROPE", "$200K+", RED, 0)], title="GETTING OUT", tag=t),
"P4-06": lambda o, t: bars([("H1 2025", 100), ("H1 2026", 69)], title="DUBAI PASSENGERS (H1 2025 = 100)", unit="", hi=1, tag=t, cues=[-1, 0], reveal=(1, "-31%")),
"P4-07": lambda o, t: globe((50, 30), arcs=[((-0.45, 51.47), (55.36, 25.25), "LONDON → DUBAI", -1), ((55.36, 25.25), (151.2, -33.9), "→ SYDNEY", 0)], title="THE WORLD'S CONNECTING HUB", tag=t),
"P4-08": lambda o, t: number("+35-45%", kicker="GULF FARES AT FIRST", sub="still above pre-war", tag=t),
"P4-09": lambda o, t: two_numbers("2025", "+$7.2BN", "2026 (FORECAST)", "-$4.3BN", tag=t, note="Middle East airlines, IATA"),
"P4-10": lambda o, t: two_numbers("DUBAI HOTELS, H1", "56% FULL", "DUBAI STOCKS", "-17%", tag=t, note="first half 2026 · first weeks of the war"),
"P4-10b": lambda o, t: gauge(12, "of the UAE economy is tourism (2023)", tag=t),
"P4-11": lambda o, t: card(["EXPATS WHO FLED HOME", "MAY OWE UK TAX"], tag=t),
"P4-12": lambda o, t: card(["A WIDER WAR", "COSTS MORE"], kicker="HARDEST HIT: KUWAIT AND BAHRAIN", tag=t),
"P4-12b": lambda o, t: split(("SAUDI ARABIA", "DEFENCE", "UN Charter, Article 51"), ("THE EMIRATES", "JOIN US", "a US effort in Hormuz"), tag=t),
"P4-12c": lambda o, t: timeline([("1987", "Kuwaiti tankers reflagged"), ("1988", "US escorts")], [1], title="THE TANKER WAR", tag=t),
"P4-13": lambda o, t: receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=3),

"P5-01": P(5, "Your bill"),
"P5-02": lambda o, t: stats3([("$10", "a barrel", -1), ("≈ 6p", "a litre, with VAT", -1), ("≈ 24¢", "a US gallon", 0)], title="THE RULE OF THUMB (OUR MATHS)", tag=t),
"P5-03": lambda o, t: stats3([("CONTAINED", "", -1), ("ENERGY HIT", "", -1), ("WATER WAR", "", 0)], title="THREE WAYS IT COULD GO", tag=t),
"P5-04": lambda o, t: pricetags([("OIL", "≈ $100", ORANGE, -1), ("PER LITRE", "≈ +7p", RED, 0)], title="CONTAINED (OUR MATHS)", tag=t),
"P5-04b": lambda o, t: pricetags([("A 55-LITRE TANK", "< £4", ORANGE, 0)], title="CONTAINED (OUR MATHS)", tag=t),
"P5-05": lambda o, t: pricetags([("PER LITRE", "+22p", RED, -1), ("55-LITRE TANK", "+£12", RED, -1), ("US GALLON", "+90¢", RED, 0)], title="ENERGY HIT: OIL BACK TO $126 (OUR MATHS)", tag=t),
"P5-05b": lambda o, t: pricetags([("24 FILL-UPS × £12", "£290", RED, 0)], title="ENERGY HIT, A YEAR (OUR MATHS)", tag=t),
"P5-06": lambda o, t: calendar(["JAN", "APR", "JUL", "OCT"], circles=[(1, "NEXT CAP", 0)], title="GAS: AT THE NEXT CAP CHANGE", tag=t),
"P5-07": lambda o, t: card(["WATER WAR:", "NO SENSIBLE NUMBER"], tag=t, stamp_txt="SCENARIO"),
"P5-08": lambda o, t: pricetags([("US GALLON · NOW", "$3.78", ORANGE, -1), ("ENERGY HIT", "$4.68", RED, 0)], title="AMERICA (OUR MATHS)", tag=t),
"P5-09": lambda o, t: chain(["FLIGHTS", "SHIPPING", "INSURANCE"], title="THE SLOW BILL", tag=t),
"P5-10": lambda o, t: rocket_feather("both", tag=t, title="UP FAST · DOWN SLOW"),
"P5-11": lambda o, t: receipt(RUN[:5], title="RUNNING TOTAL", tag=t, show=4),

"P6-01": P(6, "What to watch"),
"P6-02": watch(1), "P6-03": watch(2), "P6-04": watch(3), "P6-05": watch(4),
"P6-05b": lambda o, t: card(["COLD SNAP", "+ A HIT ON QATAR"], kicker="THE WINTER RISK", tag=t),
"P6-05c": lambda o, t: roadmap(o, t, ["RAS LAFFAN", "WATER", "SAUDI", "TALKS"]),
"P6-06": lambda o, t: split(("NOW", "IN THE WAR", "drones, intercepts"), ("NOT YET", "AT WAR", "the Gulf fights back"), tag=t),
}
SPEC["RC-01"] = lambda o, t: receipt(RT, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(5):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RT[:i+1], title="THE RECEIPT", tag="", show=i))(i)
SPEC["RC-07"] = lambda o, t: receipt(RT + [("PENDING", "")], title="THE RECEIPT", tag="", show=5, final_stamp="PENDING")
SPEC["RC-08"] = lambda o, t: endcard("WHAT HAPPENS IF THE IRAN WAR RESTARTS?", "Every crisis sends a bill. History keeps the receipts.")
