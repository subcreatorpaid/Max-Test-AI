# INV-022 graphics spec (What If Iran Gets the Bomb?). No weapon-design detail anywhere: only public levels, dates and amounts.
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "inv019"))
from kit19 import *

IRAN = (43.5, 24.0, 63.8, 40.2)
FORDOW = (50.99, 34.88); NATANZ = (51.73, 33.72); ISFAHAN = (51.67, 32.65); RIYADH = (46.72, 24.69)
RT = ["LOCATION: UNKNOWN", "FROM A DEAL TO A WAR", "NOBODY CAN CHECK", "RACE · BOMB · DEAL", "-10p TO +22p A LITRE"]
RUN = [("LOCATION UNKNOWN", "LINE 1"), ("DEAL TO WAR", "LINE 2"), ("NOBODY CAN CHECK", "LINE 3"), ("RACE · BOMB · DEAL", "LINE 4"), ("-10p TO +22p", "LINE 5")]
LNG = [((51.6, 25.9), (56.4, 26.4), ORANGE, 4, None, False), ((56.4, 26.4), (58.5, 22.5), ORANGE, 4, None, False), ((58.5, 22.5), (43.4, 12.6), ORANGE, 4, None, False),
       ((43.4, 12.6), (32.5, 29.9), ORANGE, 4, None, False), ((32.5, 31.2), (5.0, 43.0), ORANGE, 4, 0, False)]
def pct(a, b, la, lb, title, tag): return ladder2(a, b, la, lb, 0, 100, 10, fmt="{:g}%", bracket="", title=title, tag=tag)
def watch(n): return lambda o, t: checklist(["1 · INSPECTORS BACK?", "2 · TALK OF LEAVING THE TREATY?", "3 · THE 7 CONDITIONS MOVING?", "4 · OIL THE DAY AFTER"][:n], title="WHAT TO WATCH", tag=t)

SPEC = {
"CO-01": lambda o, t: map_scene(IRAN, z=5, hi=("Iran",), title="IRAN'S 60% URANIUM · LOCATION: UNKNOWN", tag=t, pins=[(53.5, 32.5, "?", ORANGE, 0)]),
"CO-02": tg(lambda: dots(9, 9, "ENOUGH FOR 9, IF ENRICHED FURTHER · IAEA", big="9", title="IAEA, 31 MAY 2025", col=RED)),
"CO-03": lambda o, t: card(["THE BILL ISN'T THE BOMB.", "IT'S THE FIGHT."], tag=t),
"CO-04": lambda o, t: pricetags([("UK · PER LITRE", "+22p", RED, -1), ("US · PER GALLON", "+90¢", RED, 0)], title="THE WORST PATH (OUR MATHS)", tag=t),
"CO-05": lambda o, t: roadmap(o, t, ["WHERE IT IS", "HOW WE GOT HERE", "HOW CLOSE", "3 PATHS", "YOUR BILL"]),

"P1-01": P(1, "Where it is"),
"P1-02": lambda o, t: bars([("POWER STATION", 3.67), ("WEAPONS", 90)], title="URANIUM ENRICHMENT LEVEL, %", unit="%", hi=0, tag=t, cues=[0, -1], fmt="{:g}"),
"P1-03": lambda o, t: pct(3.67, 60, "3.67% · POWER", "60% · IRAN", "IRAN'S LEVEL · WEAPONS GRADE ≈ 90%", t),
"P1-04": lambda o, t: number("≈ 441 KG", kicker="URANIUM AT 60% · JUNE 2025", sub="IAEA", tag=t),
"P1-05": lambda o, t: calendar(["JUN 25", "SEP", "DEC", "MAR 26", "JUN", "SEP", "NOV"], stamps=[(3, "NO INSPECTORS", 0)], title="IAEA ACCESS SINCE JUNE 2025", tag=t),
"P1-06": lambda o, t: checklist(["SIZE: UNKNOWN", "MAKE-UP: UNKNOWN", "LOCATION: UNKNOWN"], title="WHAT THE IAEA CAN'T CONFIRM", tag=t),
"P1-07": lambda o, t: map_scene(IRAN, z=5, hi=("Iran",), title="MOVED? BURIED?", tag=t, pins=[(51.4, 34.4, "?", ORANGE, -1), (52.4, 32.2, "?", ORANGE, -1), (54.8, 31.0, "?", ORANGE, 0)]),
"P1-08": lambda o, t: quote("No information since June 2025", "IAEA chief Rafael Grossi", "18 Nov 2026", tag=t),
"P1-09": lambda o, t: quote("There is no protocol", "Iranian MP, on inspections", "Nov 2026", tag=t),
"P1-10": lambda o, t: card(["'RAISES PROLIFERATION", "CONCERNS'"], kicker="IAEA", tag=t),
"P1-10b": lambda o, t: chain(["NO INSPECTORS", "GUESSING", "ASSUME THE WORST", "RISK PREMIUM"], title="BLIND = ASSUME THE WORST", tag=t),
"P1-11": lambda o, t: card(["THE WORLD IS BLIND."], tag=t, stamp_txt="UNVERIFIED"),
"P1-12": lambda o, t: receipt(RUN[:1], title="RUNNING TOTAL", tag=t, show=0),

"BR-01": sub_card(5, "THE LAST TIME IRAN SHUT THE OIL", of=6),

"P2-01": P(2, "How we got here"),
"P2-01b": lambda o, t: timeline([("NOV 1967", "Tehran reactor"), ("1967", "US-supplied fuel")], [1], title="IT STARTED WITH AMERICA", tag=t),
"P2-01c": lambda o, t: split(("1967", "ALLY", "the Shah"), ("1979", "REVOLUTION", "Khomeini"), tag=t),
"P2-02": lambda o, t: typed(["NPT · IN FORCE MARCH 1970", "IRAN: NON-NUCLEAR-WEAPON STATE"], label="THE TREATY", tag=t, cue_lines=[-1, 0]),
"P2-03": lambda o, t: timeline([("2003", "Weapons project shelved"), ("2003", "Fatwa")], [1], title="2003", tag=t),
"P2-03b": lambda o, t: number("≈ 370 KG", kicker="URANIUM AT 20% · 2013", sub="'breakout: a few months'", tag=t),
"P2-04": lambda o, t: two_numbers("CAP", "3.67%", "STOCKPILE", "300 KG", tag=t, note="the nuclear deal, 14 July 2015"),
"P2-05": lambda o, t: quote("A giant fiction", "President Trump, leaving the deal", "May 2018", tag=t),
"P2-06": lambda o, t: card(["3.67% · 300 KG"], kicker="2019-20: THE LIMITS", tag=t, stamp_txt="BROKEN"),
"P2-07": lambda o, t: bars([("2019", 4.5), ("2021", 60), ("2023 · TRACES", 84)], title="IRAN'S HIGHEST ENRICHMENT, % · WEAPONS ≈ 90", unit="%", hi=2, tag=t, cues=[-1, -1, 0], fmt="{:g}"),
"P2-08": lambda o, t: map_scene(IRAN, z=5, hi=("Iran",), title="22 JUNE 2025: SITES BOMBED", tag=t, pins=[(FORDOW[0], FORDOW[1], "FORDOW", RED, -1), (NATANZ[0], NATANZ[1], "NATANZ", RED, -1), (ISFAHAN[0], ISFAHAN[1], "ISFAHAN", RED, 0)]),
"P2-09": lambda o, t: checklist(["FORDOW", "NATANZ", "ISFAHAN", "ALL HIT · 22 JUNE"], title="'ALMOST ALL' DESTROYED AT FORDOW · IAEA", tag=t),
"P2-09b": lambda o, t: stats3([("1,060", "killed in Iran", -1), ("33", "killed in Israel", -1), ("10+", "nuclear scientists", 0)], title="THE 12-DAY WAR, 2025", tag=t),
"P2-10": lambda o, t: number("1-2 YEARS", kicker="SET BACK · PENTAGON ESTIMATE", tag=t),
"P2-11": lambda o, t: timeline([("28 FEB 2026", "The war"), ("8 MAR", "New supreme leader")], [1], title="2026", tag=t),
"P2-11b": lambda o, t: card(["THE BOMB IS THE", "CENTRE OF THIS WAR."], tag=t),
"P2-12": lambda o, t: card(["THE RULING'S", "AUTHOR IS GONE."], kicker="DOES THE FATWA SURVIVE?", tag=t, stamp_txt="ANALYSIS"),
"P2-13": lambda o, t: receipt(RUN[:2], title="RUNNING TOTAL", tag=t, show=1),

"P3-01": P(3, "How close?"),
"P3-02": lambda o, t: card(["NOBODY KNOWS.", "THEY DISAGREE."], tag=t),
"P3-03": lambda o, t: quote("Not building a nuclear weapon", "US intelligence chief Tulsi Gabbard", "Mar 2025", tag=t),
"P3-04": lambda o, t: split(("IAEA", "NO PROOF", "of a bomb effort"), ("IAEA", "NO PROMISE", "that it's peaceful"), tag=t),
"P3-05": lambda o, t: quote("Less than a year", "Benjamin Netanyahu", "Jun 2025", tag=t),
"P3-06": lambda o, t: calendar(["WK 1", "WK 2", "WK 3", "WK 4"], circles=[(3, "'A MATTER OF WEEKS'?", 0)], title="IF THE MACHINES SURVIVED · ISPI", tag=t),
"P3-07": lambda o, t: chain(["URANIUM", "DEVICE", "DELIVERY", "TEST"], title="URANIUM ISN'T A BOMB", tag=t),
"P3-08": lambda o, t: card(["NO EVIDENCE OF", "WEAPONIZING"], kicker="IAEA · FEB 2026", tag=t),
"P3-08b": lambda o, t: map_scene(IRAN, z=5, hi=("Iran",), title="NATANZ HIT AGAIN · 2 & 21 MARCH 2026", tag=t, pins=[(NATANZ[0], NATANZ[1], "NATANZ", RED, 0)]),
"P3-08c": lambda o, t: split(("ONE SIDE", "SLOWS IT", "bombing sets it back"), ("OTHER SIDE", "SPEEDS IT", "they want it more"), tag=t),
"P3-09": lambda o, t: two_numbers("FASTEST GUESS", "WEEKS?", "SLOWEST GUESS", "YEARS?", tag=t, note="nobody can check"),
"P3-10": lambda o, t: timeline([("JAN 2003", "Leaves the NPT"), ("OCT 2006", "First test")], [1], title="NORTH KOREA", tag=t),
"P3-11": lambda o, t: number("3.5 YEARS", kicker="TREATY EXIT TO FIRST TEST · NORTH KOREA", tag=t),
"P3-12": lambda o, t: receipt(RUN[:3], title="RUNNING TOTAL", tag=t, show=2),

"P4-01": P(4, "Three paths"),
"P4-02": lambda o, t: card(["1 · THE RACE"], tag=t, stamp_txt="SCENARIO"),
"P4-03": lambda o, t: timeline([("JUN 2025", "Strikes"), ("FEB 2026", "War")], [1], title="TWICE IN 18 MONTHS", tag=t),
"P4-04": lambda o, t: ladder2(80, 67, "≈ $80", "≈ $67 · -15%", 60, 90, 5, title="JUNE 2025: SPIKE, THEN FALL (BRENT)", tag=t),
"P4-05": lambda o, t: linechart({"BRENT": [("27 FEB", 71), ("8 MAR", 100), ("PEAK", 126)]}, title="2026: $71 → $126", tag=t, marks=[("$126", 2, 0)], ylab_fmt="${:g}"),
"P4-06": lambda o, t: split(("SHORT RACE", "SPIKE", "weeks"), ("LONG RACE", "SHOCK", "months"), tag=t),
"P4-07": lambda o, t: card(["2 · THE BOMB"], tag=t, stamp_txt="SCENARIO"),
"P4-08": lambda o, t: quote("Follow suit as soon as possible", "Saudi Crown Prince Mohammed bin Salman, CBS", "Mar 2018", tag=t),
"P4-09": lambda o, t: map_scene(GULF, z=6, hi=("Iran",), hi2=("Saudi Arabia",), title="TWO RIVALS, ONE STRAIT", tag=t, pins=[(STRAIT[0], STRAIT[1], "HORMUZ", ORANGE, 0)]),
"P4-09b": lambda o, t: card(["ISRAEL: NEVER SIGNED", "THE NPT"], kicker="WIDELY BELIEVED TO BE ARMED", tag=t),
"P4-10": lambda o, t: stacked([("PRE-WAR $71", 71, CYAN, -1), ("WAR $17", 17, ORANGE, -1), ("NUCLEAR ?", 10, RED, 0)], title="A PREMIUM THAT DOESN'T FADE (ILLUSTRATION)", total="", tag=t),
"P4-11": lambda o, t: card(["3 · THE DEAL"], tag=t, stamp_txt="SCENARIO"),
"P4-12": lambda o, t: split(("US", "ZERO", "enrichment"), ("IRAN", "A RIGHT", "to enrich + 7 conditions"), tag=t),
"P4-12b": lambda o, t: timeline([("2015", "Deal"), ("2018", "US exit"), ("2019", "Limits broken")], [2], title="3 YEARS ON, THEN OFF", tag=t),
"P4-13": lambda o, t: card(["THE ONLY", "CHEAPER PATH."], tag=t),
"P4-14": lambda o, t: receipt(RUN[:4], title="RUNNING TOTAL", tag=t, show=3),

"P5-01": P(5, "Your bill"),
"P5-02": lambda o, t: stats3([("$10", "a barrel", -1), ("≈ 6p", "a litre, with VAT", -1), ("≈ 24¢", "a US gallon", 0)], title="THE RULE OF THUMB (OUR MATHS)", tag=t),
"P5-03": lambda o, t: pricetags([("SHORT RACE · OIL", "+$10", ORANGE, -1), ("PER LITRE", "≈ +6p", RED, -1), ("HOW LONG", "WEEKS", PAPER, 0)], title="SHORT RACE (OUR MATHS)", tag=t),
"P5-04": lambda o, t: pricetags([("PER LITRE", "+22p", RED, -1), ("55-LITRE TANK", "+£12", RED, -1), ("US GALLON", "+90¢", RED, 0)], title="LONG RACE (OUR MATHS)", tag=t),
"P5-05": lambda o, t: rocket_feather("both", tag=t, title="UP FAST · DOWN SLOW"),
"P5-06": lambda o, t: pricetags([("+$10, FOR YEARS", "+6p", RED, 0)], title="THE BOMB, FOR YEARS (OUR MATHS)", tag=t),
"P5-07": lambda o, t: pricetags([("24 × 55 L × 6p", "≈ £75", RED, 0)], title="A YEAR OF FILL-UPS (OUR MATHS)", tag=t),
"P5-08": lambda o, t: pricetags([("PER LITRE", "-10p", CYAN, -1), ("US GALLON", "-40¢", CYAN, 0)], title="THE DEAL (OUR MATHS)", tag=t),
"P5-08b": lambda o, t: pricetags([("DEAL", "≈ $3.38", CYAN, -1), ("NOW", "$3.78", ORANGE, -1), ("SHOCK", "≈ $4.68", RED, 0)], title="US GALLON (OUR MATHS)", tag=t),
"P5-09": lambda o, t: number("£2,166", kicker="ENERGY PRICE CAP · FROM 1 JAN 2027", sub="Ofgem", faded="£1,723", tag=t),
"P5-10": lambda o, t: map_scene(WIDE, z=4, hi=("Qatar",), title="QATAR'S GAS USES HORMUZ", tag=t, lines=LNG, pins=[(56.4, 26.4, "HORMUZ", RED, None)]),
"P5-10b": lambda o, t: chain(["RISK PREMIUM", "SHIPPING", "FERTILISER", "YOUR SHOPPING"], title="THE SLOW BILL", tag=t),
"P5-11": lambda o, t: card(["DEAL: -10p", "RACE: +6p TO +22p", "BOMB: +6p, FOR YEARS"], kicker="A LITRE, BY PATH (OUR MATHS)", tag=t),
"P5-12": lambda o, t: receipt(RUN[:5], title="RUNNING TOTAL", tag=t, show=4),

"P6-01": P(6, "What to watch"),
"P6-02": watch(1), "P6-03": watch(2), "P6-04": watch(3), "P6-05": watch(4),
"P6-05b": lambda o, t: roadmap(o, t, ["INSPECTORS", "TREATY", "CONDITIONS", "OIL", "WHICH PATH?"]),
"P6-06": lambda o, t: split(("DOOR 1", "DIPLOMACY", "cheaper"), ("DOOR 2", "BOMBS", "dearer"), tag=t),
}
SPEC["RC-01"] = lambda o, t: receipt(RT, title="THE RECEIPT", tag="", show=0, cues_from=[99])
for i in range(5):
    SPEC[f"RC-0{i+2}"] = (lambda i: lambda o, t: receipt(RT[:i+1], title="THE RECEIPT", tag="", show=i))(i)
SPEC["RC-07"] = lambda o, t: receipt(RT + [("UNVERIFIED", "")], title="THE RECEIPT", tag="", show=5, final_stamp="UNVERIFIED")
SPEC["RC-08"] = lambda o, t: endcard("WHAT HAPPENS IF THE IRAN WAR RESTARTS?", "Every crisis sends a bill. History keeps the receipts.")
