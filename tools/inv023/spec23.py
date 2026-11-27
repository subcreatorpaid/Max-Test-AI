# INV-023 graphics spec (The Last Time Iran Shut the Oil: 1979).
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "inv019"))
from kit19 import *

IRAN = (43.5, 24.0, 63.8, 40.2); GULF2 = (38.0, 23.0, 63.8, 40.2)
USA = (-125, 24, -66, 50)
RT = ["IRAN'S OUTPUT: -75%", "4% SHORT · 100% PANIC", "OIL × 2.5", "UK: 22% · 3.3M OUT OF WORK", "3 INSTALMENTS"]
RUN = [("OUTPUT -75%", "LINE 1"), ("4% SHORT, 100% PANIC", "LINE 2"), ("OIL × 2.5", "LINE 3"), ("22% · 3.3M", "LINE 4"), ("3 INSTALMENTS", "LINE 5")]
def lesson(n): return lambda o, t: checklist(["1 · PANIC > BARRELS", "2 · THE PUMP IS INSTALMENT ONE", "3 · IT ENDS, SLOWLY"][:n], title="THREE LESSONS", tag=t)

SPEC = {
"CO-01": lambda o, t: bars([("BEFORE", 6.0), ("NOV 1978", 1.5)], title="IRAN'S OIL OUTPUT, M BARRELS A DAY", unit="", hi=1, tag=t, cues=[-1, 0], fmt="{:g}", reveal=(1, "-75%")),
"CO-02": lambda o, t: ladder2(15.85, 39.50, "$15.85", "$39.50", 0, 45, 5, fmt="${:g}", bracket="× 2.5", title="OIL, $ A BARREL · 1979-80", tag=t),
"CO-03": lambda o, t: stats3([("QUEUES", "at US pumps", -1), ("22%", "UK inflation", -1), ("20%", "US interest rates", 0)], title="THE 1979 BILL", tag=t),
"CO-04": lambda o, t: split(("1978", "STRIKES", "inside Iran"), ("2026", "BLOCKADE", "around Iran"), tag=t),
"CO-05": lambda o, t: checklist(["SMALL SHORTAGE", "HUGE PANIC", "A BILL FOR YEARS"], title="THE 1979 PATTERN", tag=t),
"CO-06": lambda o, t: roadmap(o, t, ["THE STRIKE", "THE PANIC", "THE PRICE", "BRITAIN", "THE LONG BILL", "THE LESSON"]),

"P1-01": P(1, "The strike"),
"P1-02": lambda o, t: map_scene(GULF2, z=5, hi=("Iran",), title="IRAN, 1978 · ONE OF THE BIGGEST EXPORTERS", tag=t, pins=[]),
"P1-03": lambda o, t: timeline([("AUTUMN 1978", "Protests"), ("OCT-NOV", "Oil strikes · 37,000")], [1], title="PROTESTS REACH THE OIL", tag=t),
"P1-04": lambda o, t: bars([("BEFORE", 6.0), ("STRIKE", 1.5)], title="IRAN'S OUTPUT, M BARRELS A DAY", unit="", hi=1, tag=t, cues=[-1, 0], fmt="{:g}"),
"P1-05": lambda o, t: card(["BACK NEAR NORMAL"], kicker="END OF NOV 1978 · NAVY PERSONNEL SENT IN", tag=t, stamp_txt="BRIEFLY"),
"P1-06": lambda o, t: card(["GENERAL STRIKE"], kicker="DECEMBER 1978", tag=t, stamp_txt="SHUT"),
"P1-07": lambda o, t: timeline([("16 JAN", "Shah leaves"), ("1 FEB", "Khomeini returns"), ("11 FEB", "Monarchy falls")], [2], title="1979", tag=t),
"P1-07b": lambda o, t: card(["HOW MUCH WILL COME BACK?", "NOBODY KNEW."], tag=t),
"P1-07c": lambda o, t: card(["NOT KNOWING COSTS MORE", "THAN NOT HAVING."], tag=t),
"P1-08": lambda o, t: chain(["IRAN", "OIL MARKET", "YOUR PUMP"], title="NEXT STOP", tag=t),
"P1-09": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0),

"BR-01": sub_card(6, "WHAT HAPPENS IF THE IRAN WAR RESTARTS?", of=6),

"P2-01": P(2, "The panic"),
"P2-02": lambda o, t: gauge(4, "of world supply lost, 1979", tag=t),
"P2-03": lambda o, t: bars([("1978 · RECORD", 100), ("1979", 96.5)], title="US PETROL SALES (1978 = 100)", unit="", hi=1, tag=t, cues=[-1, 0], fmt="{:g}", reveal=(1, "-3.5%")),
"P2-04": lambda o, t: card(["PEOPLE PANICKED."], tag=t),
"P2-05": lambda o, t: timeline([("28 MAR 1979", "Three Mile Island"), ("SPRING", "Panic buying")], [1], title="1979", tag=t),
"P2-06": lambda o, t: chain(["TOP UP", "QUEUES", "MORE PANIC", "LONGER QUEUES"], title="QUEUES MADE MORE QUEUES", tag=t),
"P2-07": lambda o, t: number("150,000", kicker="BARRELS A DAY BURNED IN QUEUES", sub="idling engines, 1979", tag=t),
"P2-08": lambda o, t: split(("ODD DAYS", "1 · 3 · 5", "odd number plates"), ("EVEN DAYS", "2 · 4 · 6", "even number plates"), tag=t),
"P2-09": lambda o, t: typed(["GASOLINE RATION COUPON", "PRINTED · NEVER USED"], label="US GOVERNMENT, 1979", tag=t, stamps=[("NEVER USED", 0)], cue_lines=[-1, -1]),
"P2-10": lambda o, t: bars([("SAID REAL", 37), ("SAID HOAX", 54)], title="WAS THE SHORTAGE REAL? · POLL, 1979", unit="%", hi=1, tag=t, cues=[-1, 0]),
"P2-11": lambda o, t: quote("A crisis of confidence", "President Jimmy Carter", "15 July 1979", tag=t),
"P2-11b": lambda o, t: two_numbers("US CONTROLLED OIL", "$6", "WORLD PRICE", "$30", tag=t, note="old US price controls"),
"P2-11c": lambda o, t: timeline([("APR 1979", "Decontrol begins"), ("JAN 1981", "Controls end")], [1], title="THE CONTROLS END", tag=t),
"P2-12": lambda o, t: card(["A 4% SHORTAGE.", "A NATIONAL MOOD."], kicker="MOODS MOVE PRICES", tag=t),
"P2-13": lambda o, t: receipt(RUN[:2], title="RUNNING TOTAL", tag=t, show=1),

"P3-01": P(3, "The price"),
"P3-02": lambda o, t: number("$15.85", kicker="OIL, A BARREL · APRIL 1979", tag=t),
"P3-03": lambda o, t: ladder2(15.85, 39.50, "$15.85 · APR 1979", "$39.50 · APR 1980", 0, 45, 5, fmt="${:g}", bracket="× 2.5", title="OIL, $ A BARREL", tag=t),
"P3-04": lambda o, t: card(["A RECORD UNTIL 2008"], kicker="IN REAL TERMS", tag=t),
"P3-05": lambda o, t: stats3([("444", "days", -1), ("52", "American hostages", 0), ("NOV 1979", "embassy seized", -1)], title="TEHRAN, 1979-81", tag=t),
"P3-06": lambda o, t: card(["THE PERSIAN GULF:", "A VITAL US INTEREST"], kicker="THE CARTER DOCTRINE · JAN 1980", tag=t),
"P3-07": lambda o, t: split(("1980", "THE DOCTRINE", "the US guards the Gulf"), ("2026", "THE BLOCKADE", "the US closes Iran's ports"), tag=t),
"P3-08": lambda o, t: map_scene(GULF2, z=5, hi=("Iran",), hi2=("Iraq",), title="SEPT 1980: IRAQ INVADES · ANOTHER -7%", tag=t, arcs=[((44.4, 33.3), (48.6, 31.3), RED, 5, 0, False)]),
"P3-09": lambda o, t: number("+250%", kicker="WTI OIL · 1978 TO 1980", tag=t),
"P3-10": lambda o, t: bars([("1979-80", 2.5), ("2026 (PEAK)", 1.8)], title="HOW FAR OIL MULTIPLIED", unit="×", hi=0, tag=t, cues=[-1, 0], fmt="{:g}"),
"P3-10b": lambda o, t: map_scene(USA, z=4, hi=("United States of America",), title="THE OTHER SIDE OF THE BILL · OIL-STATE BOOM", tag=t, pins=[(-97.5, 31.0, "TEXAS", ORANGE, -1), (-97.5, 35.5, "OKLAHOMA", ORANGE, -1), (-150.0, 61.0, "ALASKA", ORANGE, 0)]),
"P3-11": lambda o, t: receipt(RUN[:3], title="RUNNING TOTAL", tag=t, show=2),

"P4-01": P(4, "Britain"),
"P4-02": lambda o, t: timeline([("SEPT 1978", "Ford strike"), ("FEB 1979", "Winter of Discontent")], [1], title="BRITAIN, 1978-79", tag=t),
"P4-03": lambda o, t: two_numbers("PAY LIMIT", "5%", "THE WINTER", "COLDEST IN 16 YEARS", tag=t, note="1978-79"),
"P4-04": lambda o, t: calendar(["OCT", "NOV", "DEC", "JAN", "FEB"], circles=[(2, "18 DEC · TANKER DRIVERS OUT", 0)], title="1978-79", tag=t),
"P4-04b": lambda o, t: bars([("THE LIMIT", 5), ("FORD GOT", 17), ("LORRY DRIVERS ASKED", 40)], title="PAY RISES, %", unit="%", hi=2, tag=t, cues=[-1, -1, 0]),
"P4-04c": lambda o, t: typed(["'CRISIS? WHAT CRISIS?'"], label="THE SUN · JAN 1979 (A HEADLINE, NOT A QUOTE)", tag=t, cue_lines=[0]),
"P4-05": lambda o, t: timeline([("28 MAR 1979", "Lost by 1 vote"), ("MAY 1979", "Thatcher wins")], [1], title="THE GOVERNMENT FALLS", tag=t),
"P4-05b": lambda o, t: two_numbers("INFLATION", "≈ 10%", "UNEMPLOYED", "≈ 1.5M", tag=t, note="May 1979"),
"P4-06": lambda o, t: linechart({"UK INFLATION": [("1979", 10), ("1980", 22), ("1983", 4)]}, title="UK INFLATION, %", tag=t, marks=[("22%", 1, 0)], ylab_fmt="{:g}%"),
"P4-07": lambda o, t: pricetags([("JAN 1980", "£100", ORANGE, -1), ("A YEAR LATER", "£122", RED, 0)], title="THE SAME SHOPPING (ILLUSTRATION)", tag=t),
"P4-08": lambda o, t: gauge(12.5, "UK unemployment, Jan 1982", tag=t, ring_max=20),
"P4-09": lambda o, t: number("3.3M", kicker="UNEMPLOYED · SUMMER 1984", tag=t),
"P4-10": lambda o, t: split(("INFLATION", "22% → 4%", "1980 → 1983"), ("UNEMPLOYED", "1.5M → 3.3M", "1979 → 1984"), tag=t),
"P4-11": lambda o, t: receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=3),

"P5-01": P(5, "The long bill"),
"P5-02": lambda o, t: number("14.8%", kicker="US INFLATION · MARCH 1980", tag=t),
"P5-03": lambda o, t: card(["PAUL VOLCKER"], kicker="FED CHAIR FROM AUG 1979", tag=t, stamp_txt="EXPENSIVE MONEY"),
"P5-04": lambda o, t: ladder2(11, 20, "11%", "20%", 0, 25, 5, fmt="{:g}%", bracket="PRIME 21.5%", title="US INTEREST RATES", tag=t),
"P5-05": lambda o, t: chain(["20% RATES", "MORTGAGES", "LOANS", "BUSINESSES"], title="WHERE IT LANDED", tag=t),
"P5-06": lambda o, t: number("10.8%", kicker="US UNEMPLOYMENT · DEC 1982", sub="highest since the 1930s", tag=t),
"P5-07": lambda o, t: chain(["IRAN 1979", "OIL × 2.5", "INFLATION", "RATES 20%", "RECESSION 1982"], title="ONE CHAIN", tag=t),
"P5-07b": lambda o, t: number("118", kicker="SAVINGS & LOANS FAILED", sub="≈ $43bn", tag=t),
"P5-08": lambda o, t: receipt([("1 · THE PUMP", ""), ("2 · PRICES", ""), ("3 · RATES & JOBS", "")], title="THREE INSTALMENTS", tag=t, show=2),
"P5-09": lambda o, t: bars([("1976", 9), ("1980", 21)], title="JAPANESE CARS, % OF US SALES", unit="%", hi=1, tag=t, cues=[-1, 0]),
"P5-10": lambda o, t: number("-13%", kicker="US OIL USE · 1979-81", tag=t),
"P5-10b": lambda o, t: bars([("1977", 46.5), ("1982", 28)], title="IMPORTS, % OF US OIL", unit="%", hi=1, tag=t, cues=[-1, 0], fmt="{:g}"),
"P5-10c": lambda o, t: card(["WHITE HOUSE SOLAR PANELS"], kicker="JIMMY CARTER'S", tag=t, stamp_txt="REMOVED 1986"),
"P5-11": lambda o, t: receipt(RUN[:5], title="RUNNING TOTAL", tag=t, show=4),

"P6-01": P(6, "The lesson"),
"P6-02": lambda o, t: linechart({"OIL": [("APR 1979", 15.85), ("1980", 39.5), ("EARLY 1986", 27)]}, title="OIL, $ A BARREL", tag=t, marks=[("PEAK", 1, -1), ("MID-80s", 2, 0)], ylab_fmt="${:g}"),
"P6-03": lambda o, t: ladder2(27, 9.5, "$27 · 1985", "< $10 · 1986", 0, 30, 5, fmt="${:g}", title="1986: THE GLUT", tag=t),
"P6-03b": lambda o, t: checklist(["US RIGS 2,300 → 1,000", "MEXICO DEBT CRISIS", "USSR -$20BN A YEAR"], title="THE GLUT SENT BILLS TOO", tag=t),
"P6-03c": lambda o, t: bars([("1970s", 50), ("1985", 29)], title="OPEC SHARE OF WORLD OIL, %", unit="%", hi=1, tag=t, cues=[-1, 0]),
"P6-04": lambda o, t: card(["THREE LESSONS"], tag=t),
"P6-05": lesson(1), "P6-06": lesson(2), "P6-07": lesson(3),
"P6-07b": lambda o, t: split(("1979", "STRIKES", "inside Iran"), ("2026", "BLOCKADE", "+ a nervous strait"), tag=t),
"P6-07c": lambda o, t: rocket_feather("both", tag=t, title="ROCKETS AND FEATHERS, THEN AND NOW"),
"P6-07d": lambda o, t: checklist(["PUMP · MONTH 1", "PRICES · YEAR 1", "RATES & JOBS · YEAR 2"], title="JUDGE IT OVER TWO YEARS", tag=t),
"P6-08": lambda o, t: split(("1979", "1981-82", "when the real bill came"), ("2026", "?", "when ours comes"), tag=t),
}
SPEC["RC-01"] = lambda o, t: receipt(RT, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(5):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RT[:i+1], title="THE RECEIPT", tag="", show=i))(i)
SPEC["RC-07"] = lambda o, t: receipt(RT + [("PAID IN FULL, 1983", "")], title="THE RECEIPT", tag="", show=5, final_stamp="PAID IN FULL, 1983")
SPEC["RC-08"] = lambda o, t: endcard("WHAT HAPPENS IF THE IRAN WAR RESTARTS?", "Every crisis sends a bill. History keeps the receipts.")
