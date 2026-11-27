# INV-021 What Happens If the Iran Blockade Lasts a Year? Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Visual kinds: G graphic (spec21) · F clip · S photo.
# Iran follow-up series #4: answer + number inside 30 s, subscribe ask ~4 min naming the next video (Iran gets the bomb),
# end screen back to "What Happens If the Iran War Restarts?". Every caption types on with a key sound.
import os
VID = "INV-021"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "BLOCKADE: DAY 130+", "P2": "IRAN EXPORTS ≈ 0", "P3": "BRENT ≈ $88", "P4": "3 WAYS IT BREAKS",
          "P5": "+6p/L PER $10", "P6": "NEXT: 11 DEC"}

part("Cold open", "0:00", [
("CO-01", "Right now, the United States Navy is stopping ships from reaching or leaving every port in Iran. It has been doing it, on and off, since the thirteenth of {April}.", "C01 C02",
 "G map: Iran coastline outlined in red, US ship icons along it; label BLOCKADE SINCE 13 APRIL", "BLOCKADE SINCE 13 APRIL", "REPORTED · CENTCOM via Wikipedia", "sub hit"),
("CO-02", "Iran's oil exports have, in the words of its own central bank governor, effectively {ceased}.", "C09",
 "G number card: IRAN OIL EXPORTS ≈ 0; faded 1.84M BPD IN MARCH", "IRAN'S OIL EXPORTS ≈ 0", "REPORTED · Mehr via Wikipedia; Kpler", "stamp thud"),
("CO-03", "And yet oil is about eighty-eight dollars a barrel. Lower than {October}.", "C18 C28",
 "G ladder: $117.64 · 30 OCT → $88 · NOW", "BRENT ≈ $88", "REPORTED · Benzinga; Visordown", "whoosh"),
("CO-04", "So what happens if this goes on for a whole year? Here's the short answer. Your bill depends on one thing: what Iran does when it runs out of places to put its {oil}.", "C10 C11",
 "G three scenario cards: CALM · SQUEEZE · SHOCK", "IT DEPENDS ON IRAN'S NEXT MOVE", "SCENARIO", "riser"),
("CO-05", "In the worst case, that's about twenty-two pence more on a litre of petrol, and ninety cents more on a gallon of {gas}.", "C32",
 "G two price tags: UK +22p A LITRE · US +90¢ A GALLON", "WORST CASE: +22p · +90¢", "ILLUSTRATION · our maths if Brent returns to $126", "register ding"),
("CO-06", "In this video, we'll look at what the blockade is, what it's doing to Iran, why your bill hasn't exploded yet, and the three ways it could. Let's open the {invoice}.", "",
 "G roadmap: THE BLOCKADE · IRAN · WHY NOT YET · 3 WAYS · YOUR BILL · THE EXIT", "A YEAR OF BLOCKADE", "", "riser"),
])

part("Part 1: The blockade", "~1:00", [
("P1-01", "Part one. The blockade.", "", "G part card PART 1 · THE BLOCKADE", "PART 1 · THE BLOCKADE", "", "reverse cymbal + sub drop"),
("P1-02", "It began on the thirteenth of April, the day after peace talks in Islamabad {failed}.", "C01",
 "G timeline: 11-12 APR TALKS FAIL · 13 APR BLOCKADE", "13 APRIL 2026", "REPORTED · Wikipedia", "map whoosh"),
("P1-03", "The US military said it covered the entire Iranian coastline. Not the Strait of Hormuz itself. Just every ship going to or from an Iranian {port}.", "C01",
 "G map: Gulf, Iran coast in red, strait left open; label PORTS, NOT THE STRAIT", "PORTS, NOT THE STRAIT", "REPORTED · CENTCOM", "map whoosh"),
("P1-04", "More than ten thousand American personnel. More than a dozen warships. Dozens of {aircraft}.", "C05",
 "G three number cards: 10,000+ PERSONNEL · 12+ WARSHIPS · DOZENS OF AIRCRAFT", "10,000+ US PERSONNEL", "REPORTED · CENTCOM", "counter"),
("P1-05", "Within six days, a US destroyer fired into the engine room of an Iranian cargo ship called the Touska, after a six-hour warning. Marines took it {over}.", "C04",
 "G document card: SEIZED · TOUSKA · 19 APR", "TOUSKA SEIZED · 19 APRIL", "REPORTED · Wikipedia", "stamp thud"),
("P1-06", "Three more tankers followed. Each was carrying about one point nine million barrels of {oil}.", "C04",
 "G checklist: TIFANI · MAJESTIC X · LENORE · 1.9M BARRELS EACH", "1.9M BARRELS EACH", "REPORTED · Wikipedia", "pen"),
("P1-07", "By late May, ninety-four ships had been turned {away}.", "C03",
 "G dots: 94 dots fill; label TURNED AWAY BY 22 MAY", "94 SHIPS TURNED AWAY", "REPORTED · CENTCOM", "counter"),
("P1-08", "In June, a peace deal was signed, and the blockade was lifted. It lasted less than a {month}.", "C02",
 "G timeline: 17 JUN MOU · 18 JUN LIFTED · 14 JUL BACK", "LIFTED 18 JUNE", "REPORTED · Wikipedia", "map whoosh"),
("P1-09", "On the fourteenth of July, it came back. And since then, a hundred and thirty-five more ships have been {diverted}.", "C02 C03",
 "G number card 135 · SHIPS DIVERTED SINCE 14 JULY", "135 DIVERTED SINCE 14 JULY", "REPORTED · CENTCOM, 10 Oct", "counter"),
("P1-10", "This month, the US said the blockade had passed a hundred and thirty days in a {row}.", "C06",
 "G calendar: 130 DAYS circled", "130 DAYS IN A ROW", "REPORTED · Gulf News", "stamp thud"),
("P1-11", "The commander in charge said it had already stopped twenty-five billion dollars' worth of Iranian crude from leaving the {country}.", "C07",
 "G number card $25BN · CRUDE STOPPED, BY 16 OCT", "$25 BILLION STOPPED", "REPORTED · CENTCOM via Wikipedia", "counter"),
("P1-12", "Iran called it an act of war. And it hit back the way it could. It seized two cargo ships of its {own}.", "C22",
 "G two document cards: SEIZED BY IRAN · MSC FRANCESCA · EPAMINODES", "IRAN SEIZED 2 SHIPS", "REPORTED · Wikipedia", "stamp thud"),
("P1-12b", "Blockades are old tools. In nineteen sixty-two, America put a naval quarantine around Cuba during the missile crisis. That one ended within weeks, with a {deal}.", "C46",
 "G timeline: OCT 1962 CUBA QUARANTINE · ENDED IN WEEKS", "1962: CUBA, WEEKS", "VERIFIED · Wikipedia", "map whoosh"),
("P1-12c", "This one is already into its eighth month, counting both runs. And neither side is talking about a {deal}.", "C02 C26",
 "G calendar: APR → NOV filled; label MONTH 8", "MONTH 8, NO TALKS", "REPORTED · Wikipedia; Gulf News", "stamp thud"),
("P1-13", "Running total. Line one. A blockade a hundred and thirty days {old}.", "", "G running receipt line 1", "LINE 1 · 130 DAYS", "", "printer"),
])

part("Bumper", "~4:00", [
("BR-01", "Quick one. This is part four of our Iran War Bill series. Next: what happens if Iran gets the bomb. {Subscribe}, so you don't miss it.", "",
 "G sub card: 4 OF THE IRAN WAR BILL · NEXT: WHAT IF IRAN GETS THE BOMB?", "SUBSCRIBE", "", "soft tick"),
])

part("Part 2: What it's doing to Iran", "~4:15", [
("P2-01", "Part two. What it's doing to Iran.", "", "G part card PART 2 · WHAT IT'S DOING TO IRAN", "PART 2 · IRAN", "", "reverse cymbal + sub drop"),
("P2-02", "Start with the oil. In March, before the blockade, Iran was exporting about one point eight million barrels a {day}.", "C08",
 "G bars: MARCH 1.84M · APRIL 1.34M · MAY <0.3M (barrels a day)", "1.84M BARRELS A DAY", "REPORTED · Kpler via Al Jazeera", "counter"),
("P2-03", "In April, one point three. By May, less than three hundred {thousand}.", "C08",
 "G same bars, May bar drops; label -84%", "UNDER 300,000 BY MAY", "REPORTED · Kpler via Al Jazeera", "whoosh"),
("P2-04", "By August, the central bank said exports had effectively {stopped}.", "C09",
 "G card: EXPORTS 'EFFECTIVELY CEASED' · CENTRAL BANK, 19 AUG", "'EFFECTIVELY CEASED'", "REPORTED · Mehr via Wikipedia", "stamp thud"),
("P2-05", "But Iran didn't stop pumping. It started storing. In June, about a hundred and forty-seven million barrels of Iranian oil were sitting on tankers at {sea}.", "C10",
 "G tanker icons fill; label 147M BARRELS AFLOAT", "147M BARRELS AFLOAT", "REPORTED · Kpler via Al Jazeera", "counter"),
("P2-06", "About sixty-seven million of those were trapped inside the Gulf, unable to get past the {line}.", "C10",
 "G map: Gulf, tanker dots inside a red line; label 67M BARRELS TRAPPED", "67M TRAPPED IN THE GULF", "REPORTED · Kpler", "map whoosh"),
("P2-07", "Could it go by land? Not really. One train carries sixty to seventy thousand barrels. One tanker carries more than six hundred {thousand}.", "C12",
 "G two bars: TRAIN 70,000 · TANKER 600,000+", "1 TANKER = 9 TRAINS", "REPORTED · Al Jazeera", "whoosh"),
("P2-08", "Now look at the money. Before the troubles began, a dollar bought about forty-two thousand {rials}.", "C13",
 "G number card 42,000 · RIALS PER DOLLAR, BEFORE", "42,000 RIALS = $1", "REPORTED · Wikipedia", "counter"),
("P2-09", "By January, it was more than a {million}.", "C13", "G ladder rial: 42,000 → 1.1M", "1.1 MILLION BY JANUARY", "REPORTED · Wikipedia", "whoosh"),
("P2-10", "In August, two {million}.", "C13", "G ladder rial: 1.1M → 2.02M", "2 MILLION BY AUGUST", "REPORTED · Time via Wikipedia", "whoosh"),
("P2-11", "And this week, on the black market, about two point eight {million}.", "C13", "G number card 2.8M · 24 NOV", "2.8 MILLION THIS WEEK", "REPORTED · Gulf News, 24 Nov", "stamp thud"),
("P2-12", "That shows up on the kitchen table. Eggs went from seventy thousand rials to two hundred {thousand}.", "C14",
 "G two price tags: EGGS · 70,000 → 200,000 RIALS", "EGGS: 70,000 → 200,000", "REPORTED · Wikipedia", "register ding"),
("P2-13", "Some families are spending up to seventy percent of their income on {food}.", "C14", "G gauge 70% · OF INCOME ON FOOD", "UP TO 70% ON FOOD", "REPORTED · Wikipedia", "counter"),
("P2-14", "There's a nationwide shortage of medicine. And in August, two banks collapsed and had to be folded into the state {bank}.", "C14 C15",
 "G checklist: MEDICINE SHORTAGE · BANK NOOR COLLAPSED · AYANDEH BANK COLLAPSED", "TWO BANKS COLLAPSED", "REPORTED · Wikipedia", "pen"),
("P2-15", "Inflation figures vary, and none of them can be checked independently. One report put it at seventy percent by {September}.", "C16",
 "G card: INFLATION ≈ 70%? · FIGURES CONFLICT", "INFLATION ≈ 70% (REPORTED)", "REPORTED · Euronews via Wikipedia", "glitch"),
("P2-15b", "And behind every one of those numbers is someone who had nothing to do with any of this. About twenty thousand sailors were stranded in the Gulf in April, on two thousand {ships}.", "C43",
 "G dots: each dot ≈ 250 seafarers; big 20,000", "20,000 SEAFARERS STRANDED", "REPORTED · IMO via Wikipedia", "counter"),
("P2-16", "So the blockade is doing what it was designed to do. It is squeezing Iran very {hard}.", "", "G card: IT IS WORKING. ON IRAN.", "IT'S SQUEEZING IRAN", "", "stamp thud"),
("P2-17", "Running total. Line two. Iran's oil exports, close to {zero}.", "", "G running receipt line 2", "LINE 2 · EXPORTS ≈ 0", "", "printer"),
])

part("Part 3: Why your bill hasn't exploded", "~7:30", [
("P3-01", "Part three. Why your bill hasn't exploded. Yet.", "", "G part card PART 3 · WHY NOT YET", "PART 3 · WHY NOT YET", "", "reverse cymbal + sub drop"),
("P3-02", "Here's the strange part. Take about two million barrels a day off the world market, and you'd expect oil to {soar}.", "C17",
 "G barrel icon removed from a stack; label -2M BARRELS A DAY", "-2M BARRELS A DAY", "REPORTED · Brookings via Wikipedia", "whoosh"),
("P3-03", "But before it began, analysts at the Brookings Institution expected the effect on prices to be {moderate}.", "C17",
 "G quote card: 'MODERATE' · BROOKINGS", "'MODERATE'", "REPORTED · Brookings via Wikipedia", "pen"),
("P3-04", "That's partly because the blockade targets Iran's ports, not the strait. Other countries' tankers can still sail {through}.", "C01",
 "G map: Hormuz, Iranian ports red, other tankers moving through", "OTHER TANKERS CAN STILL SAIL", "REPORTED · CENTCOM", "map whoosh"),
("P3-04b", "Not many do. Traffic through Hormuz is still about sixty-five percent below what it was before the war. In one week this month, just three hundred and eight ships {crossed}.", "C37",
 "G bars: BEFORE THE WAR 100 · NOW 35; label -65%", "HORMUZ TRAFFIC -65%", "REPORTED · UKMTO via Al Jazeera", "whoosh"),
("P3-04c", "And insurance for a big tanker now costs about seven and a half to ten percent of the ship's value. That's around twenty-one million dollars for a single {trip}.", "C38",
 "G bars: BEFORE 1-3% · NOW 7.5-10%; reveal ≈ $21M A TRIP", "≈ $21M TO INSURE ONE TRIP", "REPORTED · S&P Global", "register ding"),
("P3-04d", "So the market had already priced in a crippled strait months ago. Losing Iran's own barrels on top was the smaller {shock}.", "C37 C38",
 "G stacked bar: STRAIT RISK (big) + IRAN BARRELS (small)", "THE STRAIT WAS THE BIG SHOCK", "ILLUSTRATION", "stamp thud"),
("P3-05", "And much of Iran's oil was going to one big buyer anyway. China. Asia takes most of the crude that comes through the strait, and China alone used to get about a third of its oil that {way}.", "C41",
 "G flow: IRAN OIL → CHINA; label LARGEST BUYER", "CHINA WAS THE BIG BUYER", "REPORTED · Al Jazeera", "whoosh"),
("P3-06", "So oil has actually fallen. From a hundred and seventeen dollars at the end of October, to about eighty-eight this {week}.", "C18 C28",
 "G line chart Brent: 27 FEB $71 · PEAK $126 · 30 OCT $117.64 · NOW $88", "BRENT ≈ $88", "REPORTED · Visordown; Benzinga", "whoosh"),
("P3-07", "Before the war began in February, it was about seventy-one. So there's still about seventeen dollars of war in every {barrel}.", "C28",
 "G stacked bar: PRE-WAR $71 + WAR $17", "$17 OF WAR IN EVERY BARREL", "ILLUSTRATION · our maths", "stamp thud"),
("P3-08", "And in Britain, petrol is about a hundred and sixty-seven pence a litre. The RAC thinks it could fall below one fifty, if the cuts are passed {on}.", "C29",
 "G two numbers: NOW ≈ 167p · RAC: < 150p", "COULD FALL BELOW 150p", "REPORTED · RAC", "register ding"),
("P3-08b", "In America, the average gallon was three seventy-eight last week, the lowest since March. In May, it was more than four fifty. So on both sides of the Atlantic, the blockade's first months have actually come with falling prices at the {pump}.", "C49",
 "G line chart US gallon: MAY $4.50+ → 17 NOV $3.78", "US GAS: $4.50+ → $3.78", "REPORTED · AP; AAA", "whoosh"),
("P3-08c", "That's not because the blockade is cheap. It's because the market is betting on calm. And markets can change their minds in an {afternoon}.", "",
 "G card: THE MARKET IS BETTING ON CALM", "THE MARKET BETS ON CALM", "", "glitch"),
("P3-09", "So for now, the blockade is costing Iran far more than it's costing {you}.", "", "G scale tipping: IRAN heavy · YOU light", "IRAN PAYS MORE. FOR NOW.", "", "stamp thud"),
("P3-10", "But a year is a long time. And there's a reason that word, for now, matters so {much}.", "", "G card: FOR NOW.", "FOR NOW.", "", "glitch"),
("P3-11", "Running total. Line three. Brent about eighty-eight {dollars}.", "", "G running receipt line 3", "LINE 3 · BRENT ≈ $88", "", "printer"),
])

part("Part 4: Three ways it breaks", "~10:00", [
("P4-01", "Part four. Three ways it breaks.", "", "G part card PART 4 · THREE WAYS IT BREAKS", "PART 4 · 3 WAYS IT BREAKS", "", "reverse cymbal + sub drop"),
("P4-01b", "We've looked at what's happened. Now let's look at a year. Twelve more months of the same pressure. There are three ways the calm could {break}.", "",
 "G calendar: 12 months, DEC → NOV; label 12 MORE MONTHS", "12 MORE MONTHS", "SCENARIO", "whoosh"),
("P4-02", "Way number one. The tanks fill {up}.", "C10 C11", "G card 1 · THE TANKS FILL UP", "1 · THE TANKS FILL UP", "", "stamp thud"),
("P4-03", "Floating storage isn't forever. Ships cost money. Oil wells don't like being switched off and on. As one analyst put it, the real pressure comes once that storage starts running {out}.", "C10 C11",
 "G storage gauge filling to FULL; label 'THE REAL PRESSURE'", "WHEN STORAGE RUNS OUT", "REPORTED · Marc Ayoub via Al Jazeera", "riser"),
("P4-04", "And this week, reports said Iran had put crews on more than fourteen tankers at Kharg Island, its main oil {terminal}.", "C20",
 "G map: Kharg Island pin; label 14+ TANKERS CREWED", "14+ TANKERS CREWED AT KHARG", "REPORTED · Benzinga via Yahoo", "map whoosh"),
("P4-05", "A tanker with a crew is a tanker that's planning to {move}.", "C20", "G card: CREWED = READY TO MOVE", "READY TO MOVE?", "SCENARIO", "glitch"),
("P4-05b", "Iran's foreign ministry calls those reports speculation. But if loaded tankers try to run the line, the Navy has to choose: let them go, or stop them by {force}.", "C44 C04",
 "G two doors: LET THEM GO · STOP THEM BY FORCE", "LET THEM GO, OR STOP THEM?", "REPORTED · Benzinga; SCENARIO", "glitch"),
("P4-05c", "It has already chosen force before. Since July, it has disabled several ships with missiles. Each of those is a moment that could turn into something {bigger}.", "C04",
 "G checklist: BELMA · LAVINE · VELA NOVA · OCEAN MOLICA · DISABLED", "SHIPS DISABLED SINCE JULY", "REPORTED · Wikipedia", "pen"),
("P4-06", "Way number two. Iran hits {back}.", "C19", "G card 2 · IRAN HITS BACK", "2 · IRAN HITS BACK", "", "stamp thud"),
("P4-07", "Its foreign ministry says it will use all its tools to confront what it calls US aggression. One MP says Iran has full control of Hormuz, and the blockade will be {broken}.", "C19",
 "G two quote cards: 'ALL OUR TOOLS' · 'WILL BE BROKEN'", "'ALL OUR TOOLS'", "CLAIM · Iran's foreign ministry; MP Kowsari", "pen"),
("P4-08", "On Thursday, drones were shot down over Kuwait. Falling debris killed two Italian citizens. Saudi Arabia blamed Iran. Iran denied it, and offered a joint {investigation}.", "C21",
 "G map: Kuwait pin; label DRONES OVER KUWAIT · 26-27 NOV", "DRONES OVER KUWAIT", "REPORTED · Gulf News, 27 Nov", "map whoosh"),
("P4-08b", "Attacks on shipping are already happening. More than thirty in October, the most of any month in this war. At least twenty-two more in November so {far}.", "C36",
 "G bars: OCT 30+ · NOV (TO 22ND) 22+", "30+ ATTACKS ON SHIPS IN OCTOBER", "REPORTED · CNN/UKMTO", "counter"),
("P4-08c", "And Iran's Revolutionary Guard claims tankers hit mines in the strait twice this month. Nobody has confirmed {it}.", "C39",
 "G document card: CLAIM · MINES · 17 & 23 NOV · NOT CONFIRMED", "MINE CLAIMS · NOT CONFIRMED", "CLAIM · IRGC", "glitch"),
("P4-09", "We've seen how this escalates before. In the tanker war of the nineteen-eighties, a reflagged supertanker hit a mine on the very first American escort {convoy}.", "C40",
 "G timeline: 24 JUL 1987 BRIDGETON · 14 APR 1988 SAMUEL B. ROBERTS · 18 APR 1988 PRAYING MANTIS", "1987: THE FIRST CONVOY HIT", "VERIFIED · Wikipedia", "map whoosh"),
("P4-09b", "A year later, a fifteen-hundred-dollar mine did eighty-nine million dollars of damage to a US warship. Within four days, the two navies were fighting the biggest American sea battle since the Second World {War}.", "C40",
 "G two numbers: MINE $1,500 · REPAIR $89.5M", "$1,500 MINE · $89.5M REPAIR", "VERIFIED · Wikipedia", "stamp thud"),
("P4-10", "Way number three. The strait itself. About a quarter of the world's seaborne oil, and a fifth of its liquefied gas, used to pass through {Hormuz}.", "C35",
 "G map: Hormuz with oil and LNG flows; labels 25% OIL · 20% LNG", "25% OF SEABORNE OIL", "REPORTED · Wikipedia", "map whoosh"),
("P4-11", "Today the blockade stops Iran's ships. If Iran ever tried to stop everyone else's, the bill would land on every country at {once}.", "C35",
 "G flow: IRAN SHIPS STOPPED → IRAN STOPS OTHERS → EVERYONE PAYS", "THEN EVERYONE PAYS", "SCENARIO", "riser"),
("P4-12", "The first two are already stirring. The third hasn't happened. But a year gives each of them twelve months to {grow}.", "", "G three cards with 12 MONTHS stamp", "12 MONTHS FOR EACH", "SCENARIO", "stamp thud"),
("P4-13", "Running total. Line four. Three ways it could {break}.", "", "G running receipt line 4", "LINE 4 · 3 WAYS", "", "printer"),
])

part("Part 5: Your bill", "~13:00", [
("P5-01", "Part five. Your bill.", "", "G part card PART 5 · YOUR BILL", "PART 5 · YOUR BILL", "", "reverse cymbal + sub drop"),
("P5-02", "First, the rule of thumb. Every ten dollars on a barrel adds about six pence to a litre of petrol, once VAT is on, and about twenty-four cents to a gallon of {gas}.", "C32",
 "G stacked: $10 A BARREL = ≈ 6p A LITRE = ≈ 24¢ A GALLON", "$10 A BARREL ≈ 6p A LITRE", "ILLUSTRATION · our maths", "counter"),
("P5-03", "Now three versions of the {year}.", "", "G three scenario columns: CALM · SQUEEZE · SHOCK", "THREE VERSIONS", "SCENARIO", "whoosh"),
("P5-04", "Version one. Calm. The blockade grinds on, Iran doesn't escalate, and oil stays near eighty-eight. Petrol could drift towards the RAC's one fifty. That's the good {year}.", "C29 C32",
 "G scenario card CALM: OIL ≈ $88 · PETROL → ≈ 150p", "CALM: PETROL → ≈ 150p", "SCENARIO · RAC estimate", "register ding"),
("P5-05", "Version two. Squeeze. Iran hits back, insurers panic, and oil goes back to where it was in October. About a hundred and seventeen {dollars}.", "C28",
 "G scenario card SQUEEZE: OIL → $117", "SQUEEZE: OIL → $117", "SCENARIO", "whoosh"),
("P5-06", "That's about seventeen pence more on a litre. Nine pounds fifty more on a fifty-five litre tank. Sixty-nine cents more on a {gallon}.", "C32",
 "G three price tags: +17p A LITRE · +£9.50 A TANK · +69¢ A GALLON", "+17p · +£9.50 · +69¢", "ILLUSTRATION · our maths", "register ding"),
("P5-07", "Version three. Shock. The strait is threatened, and oil returns to this year's peak of a hundred and twenty-six {dollars}.", "C28",
 "G scenario card SHOCK: OIL → $126", "SHOCK: OIL → $126", "SCENARIO", "whoosh"),
("P5-08", "That's about twenty-two pence more on a litre. Twelve pounds a tank. Ninety cents a {gallon}.", "C32",
 "G three price tags: +22p A LITRE · +£12 A TANK · +90¢ A GALLON", "+22p · +£12 · +90¢", "ILLUSTRATION · our maths", "register ding"),
("P5-09", "Fill up twice a month in the shock version, and that's about two hundred and ninety pounds over the {year}.", "C32",
 "G pricetag: 24 FILL-UPS × £12 ≈ £290 A YEAR", "≈ £290 A YEAR", "ILLUSTRATION · our maths", "register ding"),
("P5-09b", "That's the arithmetic. But remember the rule from our last video. When oil rises, petrol follows within weeks. When it falls, it takes twice as long. So a shock year costs you on the way up, and keeps costing on the way {down}.", "C48",
 "G rocket and feather lines", "UP FAST · DOWN SLOW", "VERIFIED · Borenstein & Cameron (NBER)", "whoosh"),
("P5-10", "Then there's gas. Before the war, Europe got about an eighth of its liquefied gas from Qatar, through {Hormuz}.", "C31",
 "G map: Qatar → Hormuz → Europe LNG route", "QATAR'S GAS USES HORMUZ", "REPORTED · Wikipedia", "map whoosh"),
("P5-11", "Britain's energy cap is already rising twenty-six percent in January, to two thousand one hundred and sixty-six pounds a {year}.", "C30",
 "G number card £2,166 · ENERGY CAP FROM 1 JAN; faded £1,723", "£2,166 FROM JANUARY", "REPORTED · Ofgem", "counter"),
("P5-12", "The cap is reset every three months from earlier wholesale prices. So if the strait wobbles in the spring, it shows up in your bill by the {summer}.", "C30",
 "G calendar: JAN · APR · JUL · OCT; circle JUL; label LAGS 3 MONTHS", "A SPRING SHOCK = A SUMMER BILL", "VERIFIED · Ofgem", "pen"),
("P5-12b", "There's a slower bill too. Up to thirty percent of the world's traded fertiliser normally goes through the strait. Urea, the most common one, jumped about fifty percent in the first month of the {war}.", "C42",
 "G line chart urea index FEB 100 → LATE MAR 150", "UREA +50% IN A MONTH", "REPORTED · Wikipedia", "whoosh"),
("P5-12c", "Fertiliser this winter is bread and vegetables next year. A long blockade with a nervous strait keeps that bill in the {post}.", "C42",
 "G chain: FERTILISER · FIELD · HARVEST · YOUR SHOPPING", "FERTILISER TODAY = FOOD NEXT YEAR", "ILLUSTRATION", "pen"),
("P5-13", "And in America, gas is about three seventy-eight a gallon. The shock version takes it close to four seventy, near May's record {high}.", "C33 C32",
 "G two price tags: NOW $3.78 · SHOCK ≈ $4.68", "US: $3.78 → ≈ $4.68", "ILLUSTRATION · our maths", "register ding"),
("P5-14", "Running total. Line five. Up to twenty-two pence a litre, if it {breaks}.", "", "G running receipt line 5", "LINE 5 · UP TO +22p", "", "printer"),
])

part("Part 6: The exit", "~16:00", [
("P6-01", "Part six. The exit.", "", "G part card PART 6 · THE EXIT", "PART 6 · THE EXIT", "", "reverse cymbal + sub drop"),
("P6-02", "So how does a blockade end? Not with a bang, usually. With money, or with a {deal}.", "", "G two doors: MONEY · DEAL", "MONEY, OR A DEAL", "", "whoosh"),
("P6-03", "The money first. The war has cost the United States more than forty-eight billion dollars. Current funding runs out on the eleventh of {December}.", "C34 C24",
 "G calendar: NOV · DEC · JAN; circle 11 DEC FUNDING ENDS", "FUNDING ENDS 11 DEC", "REPORTED · Pentagon; Al Jazeera", "pen"),
("P6-04", "Democrats won this month's elections, and their leaders say ending the war is a priority. The President says it's funded through {January}.", "C24",
 "G split: CONGRESS: END IT · PRESIDENT: FUNDED TO JAN", "FUNDED THROUGH JANUARY?", "REPORTED · Al Jazeera; Gulf News", "glitch"),
("P6-05", "Then the deal. Iran's list of seven conditions for talks includes lifting the {blockade}.", "C26",
 "G checklist: 7 CONDITIONS · #1 LIFT THE BLOCKADE", "CONDITION: LIFT THE BLOCKADE", "REPORTED · Gulf News", "pen"),
("P6-06", "On Thanksgiving, the President said victory is at hand. It will happen whenever I want it to {happen}.", "C23",
 "G quote card: 'VICTORY AT HAND' · 26 NOV", "'VICTORY AT HAND'", "REPORTED · Gulf News, 27 Nov", "pen"),
("P6-07", "And Iran's supreme leader says anyone expecting the election to change American policy is seriously {mistaken}.", "C25",
 "G quote card: 'SERIOUSLY MISTAKEN' · MOJTABA KHAMENEI", "'SERIOUSLY MISTAKEN'", "REPORTED · Al Jazeera", "pen"),
("P6-08", "So both sides are betting the other blinks first. That's the definition of a long {blockade}.", "", "G two clocks facing each other; label WHO BLINKS?", "WHO BLINKS FIRST?", "", "glitch"),
("P6-08b", "So here's what a year might look like on the calendar. December: the money fight in Washington. January: a new Congress. April: Britain's next energy price cap. Summer: America's driving season, when demand for petrol {peaks}.", "C24 C47",
 "G roadmap: DEC FUNDING · JAN NEW CONGRESS · APR ENERGY CAP · SUMMER DRIVING SEASON", "THE YEAR ON A CALENDAR", "VERIFIED · Ofgem; US Congress", "riser"),
("P6-08c", "Every one of those is a moment where the blockade either eases, or gets more expensive for somebody. And if it's Iran that decides it has nothing left to lose, it gets expensive for {everybody}.", "",
 "G chain: EASES · OR · ESCALATES → EVERYONE PAYS", "EASE, OR ESCALATE", "SCENARIO", "glitch"),
("P6-09", "What should you watch? Three things. The eleventh of December in Washington. Tankers moving at Kharg Island. And any attack on a ship that isn't {Iranian}.", "C24 C20",
 "G checklist: 11 DEC FUNDING · KHARG TANKERS · ATTACKS ON OTHER SHIPS", "WHAT TO WATCH", "", "pen"),
("P6-10", "If you see the third one, expect the rocket at the pump within {weeks}.", "C32", "G rocket line rising; label PUMP: WEEKS", "THEN: THE ROCKET", "SCENARIO", "whoosh"),
])

part("The Receipt", "~18:00", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. A blockade a hundred and thirty days {old}.", "C06", "G receipt line 1 prints", "130 DAYS", "", "printer"),
("RC-03", "Line two. Iran's oil exports, close to {zero}.", "C09", "G receipt line 2", "EXPORTS ≈ 0", "", "printer"),
("RC-04", "Line three. Brent about eighty-eight {dollars}, for now.", "C18", "G receipt line 3", "BRENT ≈ $88", "", "printer"),
("RC-05", "Line four. Three ways it could {break}.", "", "G receipt line 4", "3 WAYS IT BREAKS", "", "printer"),
("RC-06", "Line five. Up to twenty-two pence a litre, and ninety cents a gallon, if it {does}.", "C32", "G receipt line 5", "UP TO +22p · +90¢", "", "printer"),
("RC-07", "A blockade squeezes one country. A broken blockade bills everyone. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp NOT YET DUE; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: next video tile WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-021 What Happens If the Iran Blockade Lasts a Year?: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/128:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not financial advice.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-021-blockade-year/INV-021-blockade-year-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
