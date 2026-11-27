# INV-020 graphics spec (Iran War: Oil Fell. Why Didn't Your Bill?). Rows not listed fall back to a card of their on-screen text.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "inv019"))
from kit19 import *

RT = ["OIL: DOWN A QUARTER", "PETROL: DOWN ≈ 4%", "≈ 10p A LITRE STILL OWED", "DIESEL STUCK NEAR £2", "ENERGY BILLS +26% IN JAN"]
RUN = [("OIL -25% · PETROL -4%", "LINE 1"), ("UP IN 4 WEEKS · DOWN IN 8", "LINE 2"), ("≈ 10p A LITRE OWED", "LINE 3"), ("DIESEL NEAR £2", "LINE 4"), ("ENERGY CAP +26%", "LINE 5")]

SPEC = {
"CO-01": lambda o, t: ladder2(117.64, 88, "$117.64 · 30 OCT", "$88 · 24 NOV", 60, 130, 10, bracket="-25%", title="BRENT CRUDE, $ A BARREL", tag=t),
"CO-02": lambda o, t: two_numbers("OIL", "-25%", "PETROL", "-4%", tag=t, note="since the peak"),
"CO-03": lambda o, t: two_numbers("WHOLESALE PETROL", "-15p+", "STILL NOT AT THE PUMP", "≈ 10p", tag=t, note="AA, Nov 2026"),
"CO-04": lambda o, t: pricetags([("PER TANK", "£5.50", ORANGE, -1), ("ENERGY CAP · JAN", "+26%", RED, 0)], title="THE TWO BILLS", tag=t),
"CO-05": lambda o, t: rocket_feather("both", tag=t, title="ROCKETS AND FEATHERS"),

"P1-01": P(1, "The fall"),
"P1-02": lambda o, t: number("$117.64", kicker="BRENT · CLOSE, 30 OCT 2026", sub="the October high", tag=t),
"P1-03": lambda o, t: ladder2(117.64, 94.62, "$117.64 · 30 OCT", "$94.62 · 4 NOV", 60, 130, 10, bracket="≈ -9% ON 4 NOV", title="BRENT CRUDE, $ A BARREL", tag=t),
"P1-04": lambda o, t: card(["BELOW $90", "FIRST TIME SINCE AUGUST"], kicker="≈ 10 NOV", tag=t),
"P1-05": lambda o, t: linechart({"BRENT": [("30 OCT", 117.6), ("4 NOV", 94.6), ("10 NOV", 89.7), ("24 NOV", 88)]}, title="BRENT, $ A BARREL", tag=t, marks=[("3-MONTH LOW", 3, 0)], ylab_fmt="${:g}"),
"P1-05b": lambda o, t: stacked([("PRE-WAR $71", 71, CYAN, -1), ("WAR LEFT $17", 17, ORANGE, 0)], title="TODAY'S $88 BARREL (OUR MATHS)", total="$88", tag=t),
"P1-06": lambda o, t: chain(["TALKS HOPES", "TANKERS MOVE", "OIL FALLS", "DENIAL: $92+"], title="OIL TRADES ON HEADLINES", tag=t),
"P1-07": lambda o, t: ladder2(77, 62, "77p · MID-OCT", "62p · NOV", 50, 90, 5, fmt="{:g}p", bracket="-15p", title="UK WHOLESALE PETROL, PENCE A LITRE", tag=t),
"P1-08": lambda o, t: stacked([("WHOLESALE 15p", 15, GREEN, -1), ("+ VAT 3p", 3, CYAN, 0)], title="WHAT THE PUMP SHOULD SHOW (OUR MATHS)", total="≈ -18p", tag=t),
"P1-09": lambda o, t: two_numbers("PETROL · 5 OCT", "174.94p", "DIESEL · 5 OCT", "200.20p", tag=t, note="RAC peak"),
"P1-10": lambda o, t: two_numbers("PETROL · MID-NOV", "167.07p", "DIESEL · MID-NOV", "196.77p", tag=t, note="government weekly figure"),
"P1-11": lambda o, t: bars([("WHOLESALE", 15), ("PETROL PUMP", 8), ("DIESEL PUMP", 3.5)], title="FALL SINCE THE PEAK, PENCE A LITRE", unit="p", hi=0, tag=t, cues=[-1, -1, 0], fmt="{:g}"),
"P1-12": lambda o, t: number("$3.78", kicker="US AVERAGE GALLON · 17 NOV", sub="lowest since March", tag=t),
"P1-12b": lambda o, t: linechart({"US GALLON": [("FEB", 3.1), ("MAY", 4.5), ("17 NOV", 3.78)]}, title="US AVERAGE GALLON, 2026 (SHAPE)", tag=t, marks=[("$4.50+ · MAY", 1, 0), ("$3.78", 2, 0)], ylab_fmt="${:g}"),
"P1-13": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0),

"BR-01": sub_card(3, "WHAT IF THE BLOCKADE LASTS A YEAR?"),

"P2-01": P(2, "Rockets and feathers"),
"P2-02": lambda o, t: card(["DO PUMP PRICES FALL", "AS FAST AS THEY RISE?"], kicker="EARLY 1990s · TWO US ECONOMISTS", tag=t),
"P2-03": lambda o, t: rocket_feather("up", tag=t, title="WHEN CRUDE GOES UP"),
"P2-04": lambda o, t: rocket_feather("down", tag=t, title="WHEN CRUDE GOES DOWN"),
"P2-05": lambda o, t: flow({"a": (230, 360, "CRUDE", PAPER_HI), "b": (560, 360, "REFINERY", PAPER_HI), "c": (850, 360, "WHOLESALE", ORANGE), "d": (1110, 360, "FORECOURT", RED)},
                           [("a", "b", "", 0), ("b", "c", "", 0), ("c", "d", "", 0)], title="WHERE THE DELAY IS", tag=t),
"P2-05b": lambda o, t: card(["PRICES FALLING?", "DRIVERS STOP SHOPPING AROUND."], kicker="SHORT-RUN MARKET POWER", tag=t),
"P2-06": lambda o, t: card(["SUMMER 2022"], kicker="AFTER RUSSIA INVADED UKRAINE", tag=t),
"P2-07": lambda o, t: number("191.53p", kicker="UK PETROL RECORD · 3 JUL 2022", sub="diesel peaked at 199.09p", tag=t),
"P2-08": lambda o, t: bars([("WHOLESALE", 20), ("PUMP", 9)], title="FALL OVER 8 WEEKS, 2022, PENCE A LITRE", unit="p", hi=1, tag=t, cues=[-1, 0]),
"P2-09": lambda o, t: pricetags([("PER TANK · RAC", "≈ £9", RED, 0)], title="2022", tag=t),
"P2-10": lambda o, t: card(["RETAILER MARGINS ≈ 20p", "3× THE LONG-TERM AVERAGE"], kicker="2022 · RAC", tag=t),
"P2-11": lambda o, t: bars([("2019", 4.6), ("2022", 10.8)], title="SUPERMARKET FUEL MARGIN, PENCE A LITRE · CMA", unit="p", hi=1, tag=t, cues=[-1, 0], fmt="{:.1f}"),
"P2-12": lambda o, t: number("£900M", kicker="EXTRA COST TO DRIVERS · CMA", sub="in a single year", tag=t),
"P2-13": lambda o, t: rocket_feather("both", tag=t, title="DIESEL, 2023 · CMA"),
"P2-13b": lambda o, t: number("+13p", kicker="DIESEL, EARLY 2023 · PER LITRE", sub="vs normal margins · CMA", tag=t),
"P2-13c": lambda o, t: checklist(["LIVE PRICES AS OPEN DATA", "PERMANENT FUEL PRICE MONITOR"], title="THE CMA'S FIX", tag=t),
"P2-14": lambda o, t: card(["HISTORY", "REPEATING ITSELF?"], kicker="RAC · NOV 2026", tag=t),
"P2-15": lambda o, t: receipt(RUN[:2], title="RUNNING TOTAL", tag=t, show=1),

"P3-01": P(3, "Where is your 10p?"),
"P3-02": lambda o, t: card(["BOUGHT IN OCTOBER,", "SOLD IN NOVEMBER."], kicker="1 · IN THE GROUND", tag=t),
"P3-03": lambda o, t: calendar(["WK 1", "WK 2", "WK 3", "WK 4"], circles=[(1, "RAC: ≈ 2 WEEKS", 0)], title="WHOLESALE → PUMP", tag=t),
"P3-04": lambda o, t: calendar(["WK 1", "WK 2", "WK 3", "WK 4"], circles=[(3, "STILL NEAR PEAK", 0)], stamps=[(0, "OIL FALLS", -1)], title="SINCE 30 OCT · AA", tag=t),
"P3-04b": lambda o, t: two_numbers("ALREADY OFF", "≈ 8p", "STILL DUE · AA", "≈ 10p", tag=t, note="if wholesale prices hold"),
"P3-05": signs,
"P3-05b": lambda o, t: card(["SUPERMARKETS USED TO", "LEAD THE CUTS."], kicker="2 · IN THE MARGIN", tag=t),
"P3-06": uk_ni,
"P3-07": lambda o, t: pricetags([("N. IRELAND · TANK", "≈ -£4", GREEN, 0)], title="SAME OIL, SAME WHOLESALE", tag=t),
"P3-08": lambda o, t: two_numbers("AVERAGE", "157.1p", "CHEAPEST", "137.9p", tag=t, note="live price tracker, this week"),
"P3-09": lambda o, t: pricetags([("GAP PER LITRE", "19p", ORANGE, -1), ("55-LITRE TANK", "£10+", GREEN, 0)], title="3 · AT THE STATION DOWN THE ROAD", tag=t),
"P3-10": lambda o, t: chain(["IN THE GROUND", "IN THE MARGIN", "AT THE CHEAP STATION"], title="WHERE YOUR 10p IS", tag=t),
"P3-11": lambda o, t: receipt(RUN[:3], title="RUNNING TOTAL", tag=t, show=2),

"P4-01": P(4, "Why diesel is stuck"),
"P4-02": lambda o, t: ladder2(200.2, 196.77, "200.20p · PEAK", "196.77p · MID-NOV", 180, 210, 5, fmt="{:g}p", bracket="-3.4p", title="UK DIESEL, PENCE A LITRE", tag=t),
"P4-03": lambda o, t: two_numbers("PETROL WHOLESALE", "-15p", "DIESEL WHOLESALE", "-4p", tag=t, note="since mid-October · AA"),
"P4-04": barrel_cut,
"P4-05": lambda o, t: map_scene(WIDE, z=4, hi=("United Kingdom",), hi2=("Saudi Arabia", "Kuwait", "United Arab Emirates"), title="DIESEL: A WORLD PRICE", tag=t,
                               lines=[((50.0, 26.5), (56.4, 26.4), ORANGE, 4, None, False), ((56.4, 26.4), (43.4, 12.6), ORANGE, 4, None, False), ((43.4, 12.6), (32.5, 29.9), ORANGE, 4, None, False), ((32.5, 31.2), (-2.0, 51.5), ORANGE, 4, 0, False)]),
"P4-05b": lambda o, t: ladder2(196.77, 190, "196.77p · NOW", "≈ 190p · RAC", 180, 210, 5, fmt="{:g}p", title="DIESEL, WHERE IT COULD GO", tag=t),
"P4-06": lambda o, t: chain(["LORRIES", "TRACTORS", "DELIVERY VANS"], title="DIESEL MOVES EVERYTHING", tag=t),
"P4-07": lambda o, t: chain(["DIESEL STICKS", "FREIGHT STICKS", "SHOP PRICES STICK"], title="THE BILL YOU DON'T SEE", tag=t),
"P4-08": lambda o, t: card(["OIL IS PRICED IN DOLLARS.", "WEAK POUND = SMALLER SAVING."], tag=t),
"P4-09": lambda o, t: receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=3),

"P5-01": P(5, "Your other bills"),
"P5-02": lambda o, t: stacked([("TAX ≈ 50%", 50, GREY, -1), ("FUEL + MARGIN", 50, ORANGE, 0)], title="ONE LITRE OF PETROL (OUR MATHS)", total="≈ 167p", tag=t),
"P5-03": lambda o, t: two_numbers("FUEL DUTY", "52.95p", "THEN VAT", "20%", tag=t, note="5p cut extended to July 2027"),
"P5-04": lambda o, t: two_numbers("SHOULD BE", "≈ 18p", "SO FAR", "≈ 8p", tag=t, note="our maths from wholesale"),
"P5-05": lambda o, t: number("+26%", kicker="ENERGY PRICE CAP · FROM 1 JAN 2027", sub="Ofgem", tag=t),
"P5-06": lambda o, t: number("£2,166", kicker="A YEAR · TYPICAL HOME", sub="up from £1,723", faded="£1,723", tag=t),
"P5-07": lambda o, t: pricetags([("MORE A YEAR", "+£443", RED, 0)], title="HIGHEST SINCE 2023", tag=t),
"P5-08": lambda o, t: map_scene(WIDE, z=4, hi=("Qatar",), title="QATAR'S GAS TO EUROPE · ≈ 1/8 OF EUROPE'S LNG", tag=t,
                                lines=[((51.6, 25.9), (56.4, 26.4), ORANGE, 4, None, False), ((56.4, 26.4), (58.5, 22.5), ORANGE, 4, None, False), ((58.5, 22.5), (43.4, 12.6), ORANGE, 4, None, False),
                                       ((43.4, 12.6), (32.5, 29.9), ORANGE, 4, None, False), ((32.5, 31.2), (5.0, 43.0), ORANGE, 4, 0, False)],
                                pins=[(56.4, 26.4, "HORMUZ", RED, None), (QATAR[0], QATAR[1], "", ORANGE, None)]),
"P5-08b": lambda o, t: chain(["GAS PRICE", "POWER PRICE", "YOUR WHOLE BILL"], title="GAS SETS THE POWER PRICE", tag=t),
"P5-08c": lambda o, t: card(["VAT CUT ON ELECTRICITY", "TO END OF JUNE 2027"], kicker="ALREADY IN THE £2,166", tag=t),
"P5-09": lambda o, t: calendar(["OCT", "NOV", "DEC", "JAN"], circles=[(3, "NEW CAP", 0)], stamps=[(3, "LOCKED", -1)], title="THE CAP LOOKS BACKWARDS", tag=t),
"P5-10": lambda o, t: two_numbers("PETROL SAVED", "≈ -£130", "ENERGY CAP", "+£443", tag=t, note="a year · our maths vs Ofgem"),
"P5-11": lambda o, t: card(["NOT CHEAPER.", "LESS EXPENSIVE."], tag=t),
"P5-12": lambda o, t: receipt(RUN[:5], title="RUNNING TOTAL", tag=t, show=4),

"P6-01": P(6, "What next, what you can do"),
"P6-02": lambda o, t: two_numbers("PETROL · RAC", "< 150p", "DIESEL · RAC", "≈ 190p", tag=t, note="if savings are passed on"),
"P6-03": lambda o, t: calendar(["7 DAYS", "14", "21", "28"], circles=[(3, "FAIRFUELUK CHECK", 0)], title="THE CLOCK STARTS NOW", tag=t),
"P6-04": lambda o, t: bars([("BEFORE", 88), ("WITHIN HOURS", 92)], title="BRENT, $ A BARREL, WHEN IRAN DENIED TALKS", unit="$", hi=1, tag=t, cues=[-1, 0], reveal=(1, "$92+")),
"P6-05": lambda o, t: rocket_feather("up", tag=t, title="IF OIL GOES BACK UP"),
"P6-05b": lambda o, t: card(["NEXT IN THE SERIES:", "WHAT IF THE BLOCKADE LASTS A YEAR?"], tag=t),
"P6-06": lambda o, t: checklist(["CHECK PRICES BEFORE YOU FILL", "GAP THIS WEEK: 19p A LITRE"], title="WHAT YOU CAN DO", tag=t),
"P6-06b": lambda o, t: checklist(["AVOID MOTORWAY SERVICES", "DIESEL: CHEAP STATIONS"], title="WHAT YOU CAN DO", tag=t),
"P6-07": lambda o, t: card(["FEATHERS FALL FASTER", "WHEN SOMEONE BLOWS."], tag=t),
}
SPEC["RC-01"] = lambda o, t: receipt(RT, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(5):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RT[:i+1], title="THE RECEIPT", tag="", show=i))(i)
SPEC["RC-07"] = lambda o, t: receipt(RT + [("STILL WAITING", "")], title="THE RECEIPT", tag="", show=5, final_stamp="STILL WAITING")
SPEC["RC-08"] = lambda o, t: endcard("WHAT HAPPENS IF THE IRAN WAR RESTARTS?", "Every crisis sends a bill. History keeps the receipts.")
