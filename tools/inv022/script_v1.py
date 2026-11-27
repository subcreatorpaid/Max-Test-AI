# INV-022 What If Iran Gets the Bomb? Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Visual kinds: G graphic (spec22) · F clip · S photo.
# Iran follow-up series #5: answer + number inside 30 s, subscribe ask ~4 min naming the next video (1979),
# end screen back to "What Happens If the Iran War Restarts?". No weapon-design detail anywhere.
import os
VID = "INV-022"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "IAEA: BLIND SINCE JUN 2025", "P2": "60% · 90% = WEAPONS", "P3": "WEEKS? YEARS?", "P4": "3 PATHS",
          "P5": "+6p/L PER $10", "P6": "WATCH: INSPECTORS"}

part("Cold open", "0:00", [
("CO-01", "Somewhere in Iran there's a stockpile of uranium that's just one step short of weapons-grade. Nobody outside Iran knows exactly where it {is}.", "D04 D09",
 "G map: Iran with a question mark; label LOCATION: UNKNOWN", "LOCATION: UNKNOWN", "REPORTED · IAEA via Wikipedia", "sub hit"),
("CO-02", "The last time inspectors counted it, in the spring of 2025, the UN watchdog said it was enough for nine nuclear weapons, if it were enriched {further}.", "D01",
 "G dots: 9 dots; label ENOUGH FOR 9, IF ENRICHED FURTHER", "ENOUGH FOR 9 WEAPONS", "REPORTED · IAEA, 31 May 2025", "counter"),
("CO-03", "So what happens to your bills if Iran gets the bomb? Here's the short answer. The bomb itself isn't what lands on your bill. The fight to stop it {is}.", "",
 "G card: THE BILL ISN'T THE BOMB. IT'S THE FIGHT.", "THE BILL IS THE FIGHT", "", "stamp thud"),
("CO-04", "If that fight restarts the war and oil goes back to this year's peak, that's about twenty-two pence more on a litre of petrol, and ninety cents more on a gallon of {gas}.", "D31 D32",
 "G two price tags: UK +22p A LITRE · US +90¢ A GALLON", "+22p A LITRE · +90¢ A GALLON", "ILLUSTRATION · our maths", "register ding"),
("CO-05", "But there's also a version where this gets cheaper. In this video: where the uranium is, how we got here, how close Iran really is, and the three paths from here, with the bill for each. Let's open the {invoice}.", "",
 "G roadmap: WHERE IT IS · HOW WE GOT HERE · HOW CLOSE · 3 PATHS · YOUR BILL", "THREE PATHS, THREE BILLS", "", "riser"),
])

part("Part 1: Where it is", "~1:00", [
("P1-01", "Part one. Where it is.", "", "G part card PART 1 · WHERE IT IS", "PART 1 · WHERE IT IS", "", "reverse cymbal + sub drop"),
("P1-02", "Uranium has to be enriched before it's useful. For a power station, a few percent is {enough}.", "D10 D03",
 "G ladder: 0% · 3.67% POWER · 60% · 90% WEAPONS; marker at 3.67%", "POWER STATION: A FEW %", "VERIFIED · Wikipedia", "whoosh"),
("P1-03", "Weapons-grade is about ninety percent. Iran has been enriching to sixty. Just short of {weapons-grade}.", "D03 D13",
 "G ladder: marker climbs 3.67 → 60; 90 line red", "IRAN: 60% · WEAPONS: 90%", "VERIFIED · Wikipedia", "whoosh"),
("P1-04", "In June 2025, the International Atomic Energy Agency put Iran's sixty percent stockpile at about four hundred and forty {kilograms}.", "D02",
 "G number card ≈ 441 KG · 60% URANIUM · JUNE 2025", "≈ 441 KG AT 60%", "REPORTED · IAEA via Wikipedia", "counter"),
("P1-05", "Then came the bombs. And since then, inspectors haven't been allowed {back}.", "D04 D15",
 "G calendar: JUN 2025 → NOV 2026 crossed out; label NO INSPECTORS", "NO INSPECTORS SINCE JUNE 2025", "REPORTED · IAEA", "stamp thud"),
("P1-06", "In September, the agency said it could no longer verify the stockpile's size, what it's made of, or where it {is}.", "D04",
 "G checklist with crosses: SIZE ✗ · MAKE-UP ✗ · LOCATION ✗", "SIZE ✗ · LOCATION ✗", "REPORTED · IAEA via Wikipedia", "pen"),
("P1-07", "Reports since then say much of it was moved before the strikes, or stored deep underground. Nobody has confirmed {where}.", "D09",
 "G map: three faded question marks; label MOVED? BURIED?", "MOVED? BURIED?", "REPORTED · Reuters via Wikipedia", "glitch"),
("P1-08", "This month, the agency's chief said Iran hasn't given it any information about its nuclear material since June {2025}.", "D05",
 "G quote card: NO INFORMATION SINCE JUNE 2025 · IAEA CHIEF, 18 NOV", "NO INFO SINCE JUNE 2025", "REPORTED · JNS, 18 Nov 2026", "pen"),
("P1-09", "And an Iranian lawmaker said inspections stay blocked until Iran's seven conditions for ending the war are met. There is no protocol, he said, for inspecting sites that have been {bombed}.", "D06",
 "G quote card: 'THERE IS NO PROTOCOL' · IRANIAN MP, NOV 2026", "'THERE IS NO PROTOCOL'", "REPORTED · Benzinga via Yahoo", "pen"),
("P1-10", "The watchdog says that lack of access raises proliferation {concerns}.", "D07",
 "G card: 'RAISES PROLIFERATION CONCERNS' · IAEA", "'PROLIFERATION CONCERNS'", "REPORTED · IAEA", "stamp thud"),
("P1-10b", "Think about what that means for the people making decisions. Every intelligence agency, every government, every oil trader is now guessing. And when people have to guess about something this dangerous, they tend to assume the {worst}.", "D04",
 "G chain: NO INSPECTORS · GUESSING · ASSUME THE WORST · RISK PREMIUM", "BLIND = ASSUME THE WORST", "ANALYSIS", "glitch"),
("P1-11", "In plain English: the world is blind, and it knows it's {blind}.", "", "G card: THE WORLD IS BLIND.", "THE WORLD IS BLIND", "", "glitch"),
("P1-12", "Running total. Line one. Enough for nine, location {unknown}.", "", "G running receipt line 1", "LINE 1 · LOCATION UNKNOWN", "", "printer"),
])

part("Bumper", "~3:45", [
("BR-01", "Quick one. This is part five of our Iran War Bill series. Next: the last time Iran shut off the oil, in 1979. {Subscribe}, so you don't miss it.", "",
 "G sub card: 5 OF THE IRAN WAR BILL · NEXT: THE LAST TIME IRAN SHUT THE OIL", "SUBSCRIBE", "", "soft tick"),
])

part("Part 2: How we got here", "~4:00", [
("P2-01", "Part two. How we got here.", "", "G part card PART 2 · HOW WE GOT HERE", "PART 2 · HOW WE GOT HERE", "", "reverse cymbal + sub drop"),
("P2-01b", "It starts, strangely, with America. In 1967, Iran's first research reactor in Tehran switched on. Its first fuel was highly enriched uranium, supplied by the United {States}.", "D38",
 "G timeline: NOV 1967 · TEHRAN RESEARCH REACTOR · US-SUPPLIED FUEL", "1967: US-SUPPLIED FUEL", "VERIFIED · Wikipedia", "map whoosh"),
("P2-01c", "Back then, Iran was an ally, ruled by the Shah. That changed in 1979, and so did everything about this {programme}.", "D38",
 "G card: 1967 ALLY → 1979 REVOLUTION", "ALLY, THEN REVOLUTION", "VERIFIED · Wikipedia", "glitch"),
("P2-02", "Iran signed the Nuclear Non-Proliferation Treaty as a country without nuclear weapons. The treaty came into force in March {1970}.", "D26",
 "G document card: NPT · IN FORCE MARCH 1970 · IRAN: NON-NUCLEAR STATE", "NPT · 1970", "VERIFIED · Wikipedia", "pen"),
("P2-03", "In 2003, by most accounts, it shelved a secret weapons project, after the then supreme leader issued a religious ruling against nuclear {weapons}.", "D22",
 "G timeline: 2003 · WEAPONS PROJECT SHELVED · FATWA", "2003: PROJECT SHELVED", "REPORTED · Wikipedia", "map whoosh"),
("P2-03b", "By 2013, Iran had about three hundred and seventy kilograms of twenty percent uranium. Almost enough, if enriched further, for one bomb. The time it would need was put at a few {months}.", "D39",
 "G number card ≈ 370 KG AT 20% · 2013; sub 'BREAKOUT: A FEW MONTHS'", "2013: A FEW MONTHS AWAY", "REPORTED · Wikipedia", "counter"),
("P2-04", "In 2015 came the nuclear deal. Enrichment capped at three point six seven percent, for fifteen years. The stockpile capped at three hundred {kilograms}.", "D10",
 "G two numbers: CAP 3.67% · STOCKPILE 300 KG; kicker 14 JULY 2015", "2015: 3.67% · 300 KG", "VERIFIED · Wikipedia", "stamp thud"),
("P2-05", "In 2018, the United States walked out. President Trump called the deal a giant {fiction}.", "D11",
 "G quote card: 'A GIANT FICTION' · 2018", "2018: US WALKS OUT", "VERIFIED · Wikipedia", "pen"),
("P2-06", "A year later, Iran broke both limits. In 2020, it said it would ignore them {altogether}.", "D12",
 "G ladder: 3.67% → beyond; 300 KG → beyond; stamp BROKEN", "2019-20: LIMITS BROKEN", "VERIFIED · Wikipedia", "stamp thud"),
("P2-07", "In 2021, it started enriching to sixty percent. In 2023, inspectors found traces at eighty-{four}.", "D13",
 "G ladder: 20 → 60 → 84 (traces); 90 line red", "60%, THEN TRACES AT 84%", "VERIFIED · Wikipedia", "whoosh"),
("P2-08", "In 2025, Europe reimposed UN sanctions. And in June, Israel and then America bombed Iran's main nuclear {sites}.", "D14 D15",
 "G map: Fordow, Natanz, Isfahan pins; label 22 JUNE 2025", "JUNE 2025: SITES BOMBED", "VERIFIED · Wikipedia", "map whoosh"),
("P2-09", "Fordow, Natanz and Isfahan were hit on the twenty-second of June. The agency's chief later said almost all the sensitive equipment at Fordow had been {destroyed}.", "D15 D17",
 "G checklist: FORDOW · NATANZ · ISFAHAN · HIT 22 JUN", "'ALMOST ALL' DESTROYED AT FORDOW", "REPORTED · IAEA via Wikipedia", "pen"),
("P2-09b", "That war lasted twelve days. Iran said more than a thousand people were killed. Israel said thirty-two civilians and a soldier died. Israel's strikes also killed at least ten of Iran's leading nuclear {scientists}.", "D40",
 "G three number cards: 1,060 KILLED (IRAN) · 33 (ISRAEL) · 10+ NUCLEAR SCIENTISTS", "12 DAYS, 1,000+ DEAD", "REPORTED · Wikipedia", "stamp thud"),
("P2-10", "The Pentagon later said that set Iran back one to two {years}.", "D16", "G number card 1-2 YEARS · PENTAGON ESTIMATE", "SET BACK 1-2 YEARS", "REPORTED · Wikipedia", "counter"),
("P2-11", "Then, this February, the war. The first strikes killed Iran's supreme leader. His son, Mojtaba Khamenei, took his {place}.", "D23",
 "G timeline: 28 FEB 2026 WAR · 8 MAR NEW SUPREME LEADER", "28 FEB 2026: THE WAR", "REPORTED · Wikipedia", "map whoosh"),
("P2-11b", "Washington said one reason for that war was to stop Iran getting a nuclear weapon. So the bomb isn't a side issue in this conflict. It's the {centre} of it.", "D41",
 "G card: THE BOMB IS THE CENTRE OF THIS WAR", "THE BOMB IS THE CENTRE", "REPORTED · Wikipedia", "stamp thud"),
("P2-12", "The man who issued the ruling against nuclear weapons is gone. Whether the ruling outlives him is one of the biggest unknowns in this {story}.", "D22 D23",
 "G card: THE RULING'S AUTHOR IS GONE", "DOES THE RULING SURVIVE?", "ANALYSIS", "glitch"),
("P2-13", "Running total. Line two. Ten years from a deal to a {war}.", "", "G running receipt line 2", "LINE 2 · DEAL TO WAR", "", "printer"),
])

part("Part 3: How close", "~7:15", [
("P3-01", "Part three. How close is Iran, really?", "", "G part card PART 3 · HOW CLOSE?", "PART 3 · HOW CLOSE?", "", "reverse cymbal + sub drop"),
("P3-02", "Here's the honest answer. Nobody outside Iran knows, and the people who claim to know {disagree}.", "", "G card: NOBODY KNOWS. THEY DISAGREE.", "NOBODY KNOWS", "", "stamp thud"),
("P3-03", "In March 2025, America's intelligence chief told Congress that Iran was not building a nuclear {weapon}.", "D18",
 "G quote card: 'NOT BUILDING A NUCLEAR WEAPON' · US DNI, MAR 2025", "US INTEL: 'NOT BUILDING'", "REPORTED · Wikipedia", "pen"),
("P3-04", "In June, the atomic agency's chief said he had no proof of a systematic effort to build one. But he couldn't promise the programme was entirely {peaceful}.", "D19",
 "G split: NO PROOF OF A BOMB EFFORT · CAN'T PROMISE IT'S PEACEFUL", "NO PROOF · NO PROMISE", "REPORTED · Wikipedia", "glitch"),
("P3-05", "Israel's prime minister said Iran could have a weapon within a year. Maybe {less}.", "D20",
 "G quote card: 'LESS THAN A YEAR' · NETANYAHU, JUN 2025", "ISRAEL: 'LESS THAN A YEAR'", "CLAIM · Wikipedia", "pen"),
("P3-06", "And some analysts say turning sixty percent material into weapons-grade could take a matter of weeks, if the machines {survived}.", "D21",
 "G calendar weeks: WK 1-4 circled; label IF THE MACHINES SURVIVED", "'A MATTER OF WEEKS'?", "ESTIMATE · ISPI via Wikipedia", "pen"),
("P3-07", "But enriched uranium isn't a bomb. You still need a working device and a way to deliver it. Those steps take time, and they're easier for spies and satellites to {spot}.", "",
 "G chain: ENRICHED URANIUM · DEVICE · DELIVERY · TEST", "URANIUM ISN'T A BOMB", "VERIFIED · general", "pen"),
("P3-08", "In February, the agency said it had found no evidence that Iran was building a {weapon}.", "D08",
 "G card: NO EVIDENCE OF WEAPONIZING · IAEA, FEB 2026", "IAEA: NO EVIDENCE (FEB 2026)", "REPORTED · Wikipedia", "stamp thud"),
("P3-08b", "And remember, that was before this year's war. The facilities have been bombed again since, including Natanz, twice in March. Some of the machines may be gone. Some of the people who knew how to run them are {gone}.", "D24 D40",
 "G map: Natanz pin; label STRUCK 2 MAR & 21 MAR 2026", "NATANZ HIT AGAIN, MARCH 2026", "REPORTED · Wikipedia", "map whoosh"),
("P3-08c", "But you can't bomb away knowledge entirely. And a country that feels cornered may want the bomb more, not less. That's the argument on both {sides}.", "",
 "G split: BOMBING SLOWS IT · BOMBING MAKES THEM WANT IT MORE", "THE ARGUMENT ON BOTH SIDES", "ANALYSIS", "glitch"),
("P3-09", "So the range runs from weeks to years. What everyone agrees on is that being blind makes the guess {worse}.", "D04",
 "G slider: WEEKS ← → YEARS; fog over the middle", "WEEKS? YEARS?", "ANALYSIS", "glitch"),
("P3-10", "There is a precedent for a country going all the way. North Korea announced it was leaving the treaty in January 2003. It tested its first bomb in October {2006}.", "D28",
 "G timeline: JAN 2003 LEAVES NPT · OCT 2006 FIRST TEST", "NORTH KOREA: 2003 → 2006", "VERIFIED · Wikipedia", "map whoosh"),
("P3-11", "Three and a half years. Under sanctions. With very little {oil}.", "D28", "G number card 3.5 YEARS", "3.5 YEARS", "VERIFIED · Wikipedia", "counter"),
("P3-12", "Running total. Line three. Weeks, or years. Nobody can {check}.", "", "G running receipt line 3", "LINE 3 · NOBODY CAN CHECK", "", "printer"),
])

part("Part 4: Three paths", "~10:00", [
("P4-01", "Part four. Three paths.", "", "G part card PART 4 · THREE PATHS", "PART 4 · THREE PATHS", "", "reverse cymbal + sub drop"),
("P4-02", "Path one. The race. Israel or America decides Iran is getting too close, and strikes {again}.", "D15 D24",
 "G card 1 · THE RACE", "1 · THE RACE", "SCENARIO", "stamp thud"),
("P4-03", "This isn't theoretical. It's happened twice in eighteen months. And each time, oil reacted within {hours}.", "D15 D24 D31",
 "G timeline: JUN 2025 STRIKES · FEB 2026 WAR; oil spikes", "TWICE IN 18 MONTHS", "VERIFIED · Wikipedia", "map whoosh"),
("P4-04", "In June 2025, a short war pushed Brent close to eighty dollars. Within two days of the ceasefire, it had fallen about fifteen percent, to around sixty-{seven}.", "D30",
 "G ladder: ≈ $80 → ≈ $67; label -15% IN 2 DAYS", "2025: SPIKE, THEN FALL", "REPORTED · Business Today; Argaam", "whoosh"),
("P4-05", "This February, a longer war took it past a hundred within nine days, and on to a hundred and twenty-{six}.", "D31",
 "G line chart: 27 FEB $71 · 8 MAR $100 · PEAK $126", "2026: $71 → $126", "REPORTED · Wikipedia", "whoosh"),
("P4-06", "So the race path has a price tag we already know. A short strike is a spike. A long war is a {shock}.", "D30 D31",
 "G two cards: SHORT = SPIKE · LONG = SHOCK", "SPIKE, OR SHOCK", "ANALYSIS", "stamp thud"),
("P4-07", "Path two. The bomb. Iran gets there, and tells the world, or lets it {guess}.", "", "G card 2 · THE BOMB", "2 · THE BOMB", "SCENARIO", "stamp thud"),
("P4-08", "The first thing that changes is the neighbourhood. In 2018, Saudi Arabia's crown prince said that if Iran developed a nuclear bomb, his country would follow suit as soon as {possible}.", "D29",
 "G quote card: 'FOLLOW SUIT AS SOON AS POSSIBLE' · MBS, CBS 2018", "SAUDI: 'FOLLOW SUIT'", "REPORTED · CBS News, Mar 2018", "pen"),
("P4-09", "That's the world's biggest oil exporting region with two rival nuclear programmes, either side of the world's most important oil {strait}.", "D29",
 "G map: Saudi Arabia and Iran either side of the Gulf; Hormuz pin", "TWO RIVALS, ONE STRAIT", "SCENARIO", "map whoosh"),
("P4-09b", "And it's worth saying what the region already has. Israel is widely believed to have nuclear weapons. It has never confirmed it, and it has never signed the {treaty}.", "D27",
 "G card: ISRAEL · NOT IN THE NPT · WIDELY BELIEVED ARMED", "ISRAEL: NEVER SIGNED", "VERIFIED · Wikipedia", "pen"),
("P4-10", "Markets don't like that. They'd likely add a permanent risk premium to every barrel. Today's war premium is about seventeen dollars. A nuclear one wouldn't fade when the shooting {stopped}.", "D36",
 "G stacked bar: PRE-WAR $71 + WAR $17 + NUCLEAR RISK ?", "A PREMIUM THAT DOESN'T FADE", "ILLUSTRATION · SCENARIO", "stamp thud"),
("P4-11", "Path three. The deal. Inspectors go back in, sanctions ease, and Iran's oil comes back on the {market}.", "D25 D35",
 "G card 3 · THE DEAL", "3 · THE DEAL", "SCENARIO", "stamp thud"),
("P4-12", "The gap is wide. America wants a permanent end to all enrichment. Iran says it has a right to a civilian programme, and wants seven conditions met before it even {talks}.", "D25 D35",
 "G split: US: ZERO ENRICHMENT · IRAN: RIGHT TO ENRICH + 7 CONDITIONS", "ZERO vs A RIGHT", "REPORTED · Wikipedia; Gulf News", "glitch"),
("P4-12b", "There's history here too. The 2015 deal held for about three years, until America walked out. Within about a year of that, Iran had broken its limits. Deals like this take years to build, and months to {break}.", "D10 D11 D12",
 "G timeline: 2015 DEAL · 2018 US EXIT · 2019 LIMITS BROKEN", "3 YEARS ON, THEN OFF", "VERIFIED · Wikipedia", "map whoosh"),
("P4-13", "But this is the only path where your bill goes {down}.", "", "G card: THE ONLY CHEAPER PATH", "THE ONLY CHEAPER PATH", "", "register ding"),
("P4-14", "Running total. Line four. Three paths: a race, a bomb, or a {deal}.", "", "G running receipt line 4", "LINE 4 · RACE · BOMB · DEAL", "", "printer"),
])

part("Part 5: Your bill", "~13:15", [
("P5-01", "Part five. Your bill.", "", "G part card PART 5 · YOUR BILL", "PART 5 · YOUR BILL", "", "reverse cymbal + sub drop"),
("P5-02", "Same rule of thumb as always. Every ten dollars on a barrel is about six pence on a litre of petrol, and about twenty-four cents on a gallon of {gas}.", "D32",
 "G stacked: $10 A BARREL = ≈ 6p A LITRE = ≈ 24¢ A GALLON", "$10 ≈ 6p ≈ 24¢", "ILLUSTRATION · our maths", "counter"),
("P5-03", "The race, short version. A spike like June 2025. Oil jumps ten dollars, maybe more, for a couple of weeks. About six pence a litre, briefly. Then it falls {back}.", "D30 D32",
 "G scenario card RACE (SHORT): +$10 · ≈ +6p · WEEKS", "SHORT RACE: ≈ +6p, BRIEFLY", "SCENARIO · our maths", "register ding"),
("P5-04", "The race, long version. Another war like this year. Oil back to a hundred and twenty-six. About twenty-two pence a litre, twelve pounds a tank, ninety cents a {gallon}.", "D31 D32",
 "G three price tags: +22p A LITRE · +£12 A TANK · +90¢ A GALLON", "LONG RACE: +22p · +£12 · +90¢", "SCENARIO · our maths", "register ding"),
("P5-05", "And remember, pump prices go up like a rocket and come down like a feather. A spike costs you for weeks after it's {over}.", "",
 "G rocket and feather lines", "UP FAST · DOWN SLOW", "VERIFIED · NBER", "whoosh"),
("P5-06", "The bomb. Harder to price, because it's a slow cost, not a shock. A permanent premium on every barrel. Ten dollars of extra fear is six pence a litre, every litre, for {years}.", "D32",
 "G pricetag: +$10 FOREVER = +6p A LITRE, EVERY LITRE", "+6p A LITRE, FOR YEARS", "SCENARIO · our maths", "register ding"),
("P5-07", "Over a year of fill-ups, that's about seventy-five pounds for a typical driver. Not a crisis. A tax nobody {voted} for.", "D32",
 "G pricetag: ≈ £75 A YEAR (24 × 55 L × 6p)", "≈ £75 A YEAR", "ILLUSTRATION · our maths", "stamp thud"),
("P5-08", "The deal. If Iran's oil comes back and the war premium melts away, Brent could head back towards seventy-one. That's about ten pence off a litre, and forty cents off a {gallon}.", "D31 D32",
 "G two price tags: -10p A LITRE · -40¢ A GALLON", "DEAL: -10p · -40¢", "SCENARIO · our maths", "register ding"),
("P5-08b", "In America, the shock version takes the average gallon from three seventy-eight to about four sixty-eight. That's close to May's record. The deal version takes it towards three thirty-{eight}.", "D42 D32",
 "G three price tags: DEAL ≈ $3.38 · NOW $3.78 · SHOCK ≈ $4.68", "US: $3.38 ← $3.78 → $4.68", "ILLUSTRATION · our maths", "register ding"),
("P5-09", "Then there's the energy bill. Britain's cap goes up to two thousand one hundred and sixty-six pounds in January, partly because of gas prices tied to this {conflict}.", "D34",
 "G number card £2,166 · ENERGY CAP FROM 1 JAN; faded £1,723", "£2,166 FROM JANUARY", "REPORTED · Ofgem", "counter"),
("P5-10", "Before the war, Europe got about an eighth of its liquefied gas from Qatar, through Hormuz. Any path that threatens the strait threatens that {gas}.", "D34",
 "G map: Qatar → Hormuz → Europe LNG route", "QATAR'S GAS USES HORMUZ", "REPORTED · Wikipedia", "map whoosh"),
("P5-10b", "And there's the slow bill. A permanent risk premium doesn't just hit fuel. It's in the cost of shipping, the price of fertiliser, the insurance on every cargo that sails near the {Gulf}.", "",
 "G chain: RISK PREMIUM · SHIPPING · FERTILISER · INSURANCE · YOUR SHOPPING", "THE SLOW BILL", "ANALYSIS", "pen"),
("P5-11", "So here's the table. The deal: cheaper. A short race: a few weeks of pain. A long race: twenty-two pence. The bomb: a little more, for {ever}.", "",
 "G table: DEAL -10p · SHORT RACE +6p (WEEKS) · LONG RACE +22p · BOMB +6p (YEARS)", "THE TABLE", "SCENARIO · our maths", "pen"),
("P5-12", "Running total. Line five. From ten pence cheaper, to twenty-two pence {dearer}.", "", "G running receipt line 5", "LINE 5 · -10p TO +22p", "", "printer"),
])

part("Part 6: What to watch", "~16:15", [
("P6-01", "Part six. What to watch.", "", "G part card PART 6 · WHAT TO WATCH", "PART 6 · WHAT TO WATCH", "", "reverse cymbal + sub drop"),
("P6-02", "One. Inspectors. If the atomic agency gets back into Iran, the fog lifts, and the race path gets less {likely}.", "D05",
 "G checklist item 1: INSPECTORS BACK?", "1 · INSPECTORS BACK?", "", "pen"),
("P6-03", "Two. The treaty. North Korea's path started with leaving it. Any talk in Tehran of leaving the treaty is the loudest alarm there {is}.", "D28",
 "G checklist item 2: TALK OF LEAVING THE NPT?", "2 · LEAVING THE TREATY?", "", "pen"),
("P6-04", "Three. The seven conditions. They tie the nuclear question to the war, the blockade and sanctions. Any movement on one moves {all} of them.", "D06 D35",
 "G checklist item 3: 7 CONDITIONS MOVING?", "3 · THE 7 CONDITIONS", "", "pen"),
("P6-05", "And four. The price of a barrel the day after any headline. It's the fastest lie detector we {have}.", "D30",
 "G checklist item 4: OIL THE DAY AFTER", "4 · OIL THE DAY AFTER", "", "pen"),
("P6-05b", "None of these will be on the front page every day. But each one tells you which of the three paths we're on, weeks before it shows up at the {pump}.", "",
 "G roadmap: INSPECTORS · TREATY · CONDITIONS · OIL → WHICH PATH?", "WHICH PATH ARE WE ON?", "", "riser"),
("P6-06", "Iran getting the bomb would change the region for a generation. But the bill you pay depends far more on whether the world stops it with diplomacy, or with {bombs}.", "",
 "G two doors: DIPLOMACY · BOMBS", "DIPLOMACY, OR BOMBS", "", "glitch"),
])

part("The Receipt", "~17:30", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. Enough for nine weapons, location {unknown}.", "D01 D04", "G receipt line 1 prints", "LOCATION UNKNOWN", "", "printer"),
("RC-03", "Line two. Ten years from a deal to a {war}.", "D10 D23", "G receipt line 2", "DEAL TO WAR", "", "printer"),
("RC-04", "Line three. Weeks, or years. Nobody can {check}.", "D04", "G receipt line 3", "NOBODY CAN CHECK", "", "printer"),
("RC-05", "Line four. Three paths: a race, a bomb, or a {deal}.", "", "G receipt line 4", "RACE · BOMB · DEAL", "", "printer"),
("RC-06", "Line five. From ten pence cheaper, to twenty-two pence {dearer}.", "D32", "G receipt line 5", "-10p TO +22p", "", "printer"),
("RC-07", "A bomb is built in secret. The bill for stopping it arrives in public. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp UNVERIFIED; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: next video tile WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-022 What If Iran Gets the Bomb?: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/128:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not financial advice.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-022-iran-bomb/INV-022-iran-bomb-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
