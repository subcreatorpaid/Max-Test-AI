# INV-009 What Happens If China Invades Taiwan: script v1 source. Run: python3 script_v1.py -> md in videos/INV-009-taiwan-2027/
# Each row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# Visual codes: kit.py N ledger number, L footage + paper label, D document (highlight + red pen), T typed card + stamp,
# B split-flap, K cut-paper figures, M navy map, P part card, R receipt printer, W mini-chart tiles, X folder + index cards;
# kit2 one-offs named in words. Grade for footage/stills: [SHADOW] [CALM] [COLOUR] [INTENSE].
import os, re
VID = "INV-009"
PARTS = []

def part(title, start, rows):
    PARTS.append((title, start, rows))

part("Cold open", "0:00", [
("CO-01", "The western Pacific, the first week of November 2026. More than a hundred Chinese navy and coast guard ships, spread across the sea in two great clusters. Beijing hasn't announced a drill.", "F31 F32",
 "M navy map: Taiwan outlined, two orange ship clusters bloom east and south; dots count up to 100+.", "WESTERN PACIFIC · NOV 2026 · 100+ SHIPS", "CLAIM · Taiwan NSC / REPORTED · AEI-ISW", "low drone in, sonar ping"),
("CO-02", "So what happens if China invades Taiwan? Or doesn't invade at all, and simply closes the door around it?", "",
 "L footage [CALM]: container ship in a strait at dusk, slow push; paper label.", "WHAT HAPPENS IF CHINA INVADES TAIWAN?", "", "soft hit"),
("CO-03", "One model from Bloomberg Economics says a war would cut the world economy by nearly ten percent in its first year. For America, that's about fifteen thousand dollars of output for every household.", "F44 F45 H2",
 "N ledger number: $10.6 TRILLION types in, then $15,000 PER HOUSEHOLD; 2 s flash of the final Receipt.", "≈ $15,000 PER US HOUSEHOLD · YEAR ONE", "SCENARIO · Bloomberg Economics, Feb 2026 / ESTIMATE · our maths", "receipt printer burst"),
("CO-04", "Nobody has fired a shot. These are models of something that hasn't happened, and we'll say that every time. Some numbers are official. Some are claims from one side. We'll tell you which is which.", "",
 "T typed card: three tags stamp down in turn: SCENARIO · CLAIM · VERIFIED.", "A MODEL, NOT A FORECAST", "", "stamp x3"),
("CO-05", "By the end, you'll see the whole bill, line by line. We'll open the box Taiwan ships to the world, cross the strait, ask why everyone says 2027, watch the rehearsal, count the money, and come back to your table.", "",
 "Roadmap: six icons light in a row (chip, strait, calendar, ships, coins, table).", "THE CHIPS · THE STRAIT · WHY 2027 · THE REHEARSAL · THE MONEY · YOUR TABLE", "", "riser"),
])

part("Part 1: What Taiwan makes", "~1:10", [
("P1-01", "Part one. What's in the box.", "", "P part card PART 1 · WHAT TAIWAN MAKES", "PART 1 · WHAT TAIWAN MAKES", "", "reverse cymbal + sub drop"),
("P1-02", "Taiwan is an island of about twenty-three million people, barely the size of Belgium. It sits about a hundred and thirty kilometres off the coast of China.", "F10 F16",
 "M map: Taiwan glows, a ruler line draws 130 KM / 81 MILES to the mainland.", "23 MILLION PEOPLE · 130 KM FROM CHINA", "VERIFIED · AFP; CSIS", "whoosh-deep"),
("P1-03", "And it makes the thing almost everything else depends on. About nine in every ten of the world's most advanced chips are made in Taiwan.", "F01",
 "L footage [COLOUR]: cleanroom, wafer under yellow light (no faces); 10 chip icons, 9 turn orange.", "≈ 9 IN 10 ADVANCED CHIPS", "REPORTED · Rhodium Group", "tick x9, hit on 9th"),
("P1-04", "One company, TSMC, makes nearly seventy percent of all the chips that other firms design and order. At the very top end, it's about ninety percent.", "F03",
 "Pie that fills to 70%, then a second ring to 90% (kit2 one-off: double ring).", "TSMC · ~70% OF CONTRACT CHIPS · ~90% AT THE TOP", "REPORTED · MarketScreener, Jun 2026", "fill swell"),
("P1-04b", "And it isn't only the fancy chips. Taiwan also makes somewhere between a third and a half of the older, cheaper chips that run fridges, power tools and car windows.", "F02",
 "Cut-paper figures (K): fridge, drill, car door on a shelf, each with a small chip tag.", "1/3 TO 1/2 OF OLDER CHIPS", "REPORTED · Rhodium Group", "paper slide x3"),
("P1-05", "If you have an iPhone, its brain was almost certainly made there. So are the AI chips from Nvidia that run the world's data centres. In 2026, Nvidia passed Apple as TSMC's biggest customer.", "F05",
 "STILL [CALM] Ken Burns: a phone circuit board macro; then two bars NVIDIA 22% vs APPLE 18%.", "NVIDIA ≈22% · APPLE ≈18% OF TSMC", "REPORTED · CNBC via MacRumors, Jan 2026", "soft hit"),
("P1-06", "It's not only phones. A new car holds a thousand chips or more. TSMC alone is reported to make about a third of the world's car microcontrollers.", "F06 F04",
 "L footage [COLOUR]: car assembly line, robot arms; counter 1,000+ in the corner.", "1,000+ CHIPS IN A NEW CAR", "REPORTED · Wafer World; Rhodium", "counter"),
("P1-07", "In 2025, Taiwan exported a record six hundred and forty billion dollars of goods. Almost a third went to the United States.", "F07",
 "B split-flap board flips to $640.7 BN · 30.9% TO THE US.", "$640.7BN EXPORTS · 30.9% TO THE US · 2025", "VERIFIED · Taiwan MOF via ING", "split-flap clatter"),
("P1-08", "Now, we already know what happens when those chips run short. Because it happened in 2021, and nothing was even broken.", "F15",
 "Typed card: 2021 · THE DRESS REHEARSAL.", "2021", "", "pause, then low pulse"),
("P1-09", "Demand for laptops and screens jumped, a few factories stumbled, and car makers couldn't get enough chips. About seven point seven million cars were never built that year.", "F13",
 "L footage [SHADOW]: empty car factory floor / half-built cars parked in rows.", "7.7 MILLION CARS NOT BUILT · 2021", "REPORTED · AlixPartners", "low drone"),
("P1-10", "In America, used car prices rose forty-five percent in twelve months. The government said it was the biggest jump it had ever recorded. Buyers paid about ninety billion dollars more worldwide.", "F11 F13",
 "D document: BLS CPI release page; the used-cars row highlighted, red pen circle on 45.2%.", "USED CARS +45.2% · JUNE 2021", "VERIFIED · BLS, Jul 2021 / REPORTED · AlixPartners", "pen scratch"),
("P1-10b", "One estimate puts the cost of that shortage to America at about one percent of its whole economy. Nearly two hundred and forty billion dollars, from a hiccup.", "F14",
 "N ledger number: ≈ $240 BN · ≈ 1% OF US GDP.", "≈ $240BN · ≈ 1% OF US GDP", "REPORTED · MarketScreener", "sub hit"),
("P1-11", "On a twenty-five-thousand-dollar used car, that's about eleven thousand dollars more, in a year. And every chip plant in Taiwan was still running.", "H5",
 "N ledger number: $25,000 → $36,300; small line 'TAIWAN: OPEN' with a green tick.", "+≈ $11,300 ON A $25K CAR", "ILLUSTRATION · our maths", "sub hit"),
("P1-12", "So what happens when it's not the factories that stop, but the sea around them?", "",
 "Push in on the strait on the map.", "", "", "riser"),
])

part("Subscribe bridge", "~4:05", [
("BR-01", "If you want to see every line of a bill like this before it arrives, subscribe. Next, we'll follow it to the table, the way we followed Hormuz to your fuel and your heating.", "",
 "Paper card with the channel's running invoice; end-screen tile of INV-006 Winter Bill.", "SUBSCRIBE · EVERY CRISIS SENDS A BILL", "", "soft tick"),
])

part("Part 2: The strait", "~4:20", [
("P2-01", "Part two. The strait.", "", "P part card PART 2 · THE STRAIT", "PART 2 · THE STRAIT", "", "reverse cymbal + sub drop"),
("P2-02", "The Taiwan Strait is one of the busiest stretches of water on Earth. In 2022, about two point four five trillion dollars of goods passed through it. More than a fifth of all the trade that moves by sea.", "F17",
 "M map: shipping lanes draw through the strait as orange threads; value counter.", "$2.45 TRILLION · 1/5 OF SEA TRADE · 2022", "REPORTED · CSIS via AFP", "whoosh + counter"),
("P2-03", "In the first seven months of that year, nearly half of the world's container ships went through it at some point.", "F18",
 "L footage [COLOUR]: container ship from above, stacked boxes, slow drift.", "≈ HALF OF ALL CONTAINER SHIPS", "REPORTED · Bloomberg, Aug 2022", "low swell"),
("P2-04", "Now look at where Taiwan's ports are. Kaohsiung, Taichung, Taipei, Keelung. The big ones all face China. Kaohsiung alone handles more than half of Taiwan's sea trade.", "F19",
 "M map: five port pins drop on the west coast; Kaohsiung pin pulses with 57%.", "KAOHSIUNG ≈ 57% OF TAIWAN'S SEA TRADE", "REPORTED · CSIS China Power, 2024", "pin drops x5"),
("P2-05", "That matters, because Taiwan has to bring almost everything in by sea. It imports ninety-seven percent of its energy.", "F20",
 "L footage [CALM]: LNG tanker at a terminal, gas domes; paper label.", "97% OF ENERGY IMPORTED", "REPORTED · MOEA / Taipower", "soft hit"),
("P2-06", "About half of its electricity comes from gas, shipped in as LNG. And in winter, it keeps about eleven days of it. In summer, about seven.", "F20 F21",
 "Countdown dial (kit2 one-off): 11 DAYS winter, then the hand drops to 7 SUMMER.", "LNG IN STOCK: ≈ 11 DAYS (WINTER) · ≈ 7 (SUMMER)", "REPORTED · Chung-Hua Institution; Atlantic Council", "clock ticks"),
("P2-07", "Here's where our Hormuz story comes back. About a third of Taiwan's gas came from Qatar. Since March, it has had to scramble for cargoes from Australia and America instead.", "F22",
 "M map: line from Qatar to Taiwan through Hormuz cuts; new lines draw from Australia and the US.", "1/3 OF TAIWAN'S LNG WAS QATARI", "REPORTED · Atlantic Council (Kpler), Mar 2026", "cut sound + whoosh"),
("P2-07b", "It's not only gas. Before the Iran war, about seventy percent of Taiwan's crude oil came from the Middle East. Its oil reserve is deeper, about five months. Its gas reserve is the thin one.", "F22 F21",
 "Two tanks side by side (kit2 one-off: gauge tanks): OIL ≈ 146-150 DAYS full, GAS ≈ 11 DAYS nearly empty.", "OIL ≈ 5 MONTHS · GAS ≈ 11 DAYS", "REPORTED · Atlantic Council; MOEA", "liquid slosh (soft)"),
("P2-08", "So Taiwan has already lived one year with its gas lifeline squeezed from far away. The question is what happens if someone squeezes it from close by.", "",
 "Slow push on the Taiwan outline; Gulf behind it dims.", "", "", "low pulse"),
("P2-09", "And why does everyone in Washington keep saying the same year?", "",
 "Split-flap begins to flip toward 2027 and freezes on 202_.", "", "", "riser"),
])

part("Part 3: Why everyone says 2027", "~6:20", [
("P3-01", "Part three. Why everyone says 2027.", "", "P part card PART 3 · WHY 2027", "PART 3 · WHY EVERYONE SAYS 2027", "", "reverse cymbal + sub drop"),
("P3-02", "In 2021, the top American admiral in the Pacific, Philip Davidson, told the Senate that China was on course to be able to seize Taiwan by 2027. The six years before that date became known as the Davidson window.", "F23",
 "Timeline ruler (kit2 one-off): 2021 to 2027 shaded as a window; 'DAVIDSON WINDOW' label.", "THE DAVIDSON WINDOW · 2021-2027", "VERIFIED · Stars and Stripes", "tick"),
("P3-03", "In 2023, the head of the CIA said American intelligence showed Xi Jinping had told his military to be ready by 2027. Ready by. Not that he would.", "F24",
 "T typed card: 'READY BY 2027' types in; red pen underlines READY BY.", "'READY BY 2027'", "REPORTED · W. Burns via Stars and Stripes", "typewriter + pen"),
("P3-04", "In 2024, the next Pacific commander said it again. All indications, he said, point to the military meeting Xi's directive to be ready to invade by 2027.", "F25",
 "Quote card (leaders' quote style), Adm. Aquilino, no photo.", "'ALL INDICATIONS POINT TO…' · ADM. AQUILINO, 2024", "VERIFIED · USNI News", "soft hit"),
("P3-05", "Then, in March 2026, US intelligence published its yearly threat report. Its words: Chinese leaders do not currently plan to invade Taiwan in 2027. Beijing has no fixed timeline. Its big date is 2049.", "F26 F27",
 "D document: ODNI 2026 report page; the line highlighted, red pen circle on 'do not currently plan'.", "'DO NOT CURRENTLY PLAN…' · ODNI, MAR 2026", "VERIFIED · ODNI via USNI News", "pen scratch"),
("P3-05b", "2049 is the hundredth birthday of the People's Republic. That's the deadline Beijing has set for what it calls national rejuvenation, and for a world-class military.", "F27",
 "Timeline ruler extends past 2027 to 2049; 2049 glows.", "2049 · THE PRC AT 100", "VERIFIED · ODNI via USNI News", "low pulse"),
("P3-06", "And seven months later, in October 2026, the US Army's Pacific commander said the 2027 window is still valid. We need to be ready by this date, he said.", "F28",
 "Two quote cards side by side: MAR 2026 'DO NOT CURRENTLY PLAN' vs OCT 2026 'STILL VALID'.", "SAME GOVERNMENT · SAME YEAR · TWO ANSWERS", "VERIFIED · Stars and Stripes, Oct 2026", "two hits"),
("P3-07", "So which is it? Both, in a way. Being able to do something isn't the same as deciding to. The same report says China is building the readiness to invade, and that it would rather win without a fight.", "F29",
 "Scale graphic (kit2 one-off): CAN on one pan, WILL on the other; they don't balance.", "CAN ≠ WILL", "VERIFIED · ODNI via USNI News", "low pulse"),
("P3-08", "And one thing the report says Beijing will weigh is simple. Whether the United States would fight.", "F27",
 "Typed card: '…WHETHER OR NOT THE U.S. WILL MILITARILY INTERVENE'.", "THE QUESTION BEIJING ASKS", "VERIFIED · ODNI via USNI News", "silence beat"),
("P3-09", "Here's the money link. Every year this stays a question, insurers, chip buyers and car makers pay a little more to plan around it. Nobody has put one number on that yet, so we won't.", "",
 "Folder + index cards: 'INSURE · STOCKPILE · SECOND FACTORY' cards slide out; last card 'NO NUMBER YET'.", "THE COST OF NOT KNOWING", "", "card slides x3"),
("P3-10", "But we can watch what the ships are doing. And in the last year, they've been practising something.", "",
 "Map pulls back to the western Pacific; ship dots begin to move.", "", "", "riser"),
])

part("Part 4: The rehearsal", "~8:50", [
("P4-01", "Part four. The rehearsal.", "", "P part card PART 4 · THE REHEARSAL", "PART 4 · THE REHEARSAL", "", "reverse cymbal + sub drop"),
("P4-02", "On the twenty-ninth of December 2025, China launched drills it called Justice Mission 2025. On the first day, a hundred and thirty military aircraft flew around Taiwan. Ninety crossed the line down the middle of the strait.", "F30",
 "M map: median line draws; 130 aircraft ticks, 90 cross it and turn orange.", "JUSTICE MISSION 2025 · 130 AIRCRAFT · 90 CROSSED", "VERIFIED · Taiwan MND via USNI News", "jet pass (low) + ticks"),
("P4-03", "There were rocket firings and practice landings. Two days later, it was over.", "F30",
 "Calendar strip: 29 · 30 · 31 DEC with a red stamp DONE on 31.", "29-31 DEC 2025", "VERIFIED · USNI News", "stamp"),
("P4-04", "Then, at the start of November 2026, came something bigger. Taiwan says more than a hundred Chinese ships were out at once, from the South China Sea into the Pacific. Two aircraft carriers had left port.", "F31 F33",
 "M map: Liaoning and Fujian icons move out of Sanya and past the Philippines.", "100+ SHIPS · 2 CARRIERS · NOV 2026", "CLAIM · Taiwan NSC / REPORTED · AEI", "sonar ping + whoosh"),
("P4-04b", "On a single day, the second of November, Taiwan counted forty-nine Chinese air sorties near the island. Thirty-six of them were to the south, around the route the carriers took.", "F33",
 "M map zoom south of Taiwan: 49 small aircraft ticks, 36 cluster in the south.", "49 SORTIES · 36 TO THE SOUTH · 2 NOV 2026", "REPORTED · Taiwan MND via AEI", "ticks"),
("P4-05", "American analysts think it may have been an unannounced exercise in cutting Taiwan off. Taiwan's defence minister calls it area denial. That means keeping outside help away. China says its carrier training is routine.", "F32 F34",
 "Three typed cards with stamps: AEI/ISW 'ASSESSMENT' · TAIWAN 'CLAIM' · CHINA 'CLAIM'.", "WHO SAYS WHAT", "REPORTED · AEI-ISW / CLAIM · Koo / CLAIM · PRC MND", "stamp x3"),
("P4-05b", "It isn't only ships. Taiwan's security bureau says the island faced about two point six million cyberattacks a day in 2025. More than double two years before.", "F35",
 "Ticker counter (kit2 one-off: odometer) rolling to 2.63M / DAY; 2023 value faded behind at half.", "2.63M CYBERATTACKS A DAY · 2025", "CLAIM · Taiwan NSB", "fast digital ticks (soft)"),
("P4-06", "So here's the scenario most experts worry about first. Not an invasion. Something quieter, called a quarantine.", "F36",
 "Typed card: QUARANTINE types in; stamp SCENARIO.", "QUARANTINE", "SCENARIO · CSIS China Power", "typewriter + stamp"),
("P4-07", "In a blockade, the military surrounds the island, and there could be missiles and mines. In a quarantine, it's the coast guard. Ships are stopped and inspected, like a customs check that never ends. On paper, it isn't war.", "F36",
 "Side-by-side cut-paper figures (K): grey warship vs white coast guard cutter; labels BLOCKADE / QUARANTINE.", "BLOCKADE = MILITARY · QUARANTINE = 'LAW ENFORCEMENT'", "VERIFIED · CSIS definition", "paper slide"),
("P4-08", "China's coast guard has more than a hundred and fifty ocean-going ships. Taiwan's has about ten.", "F37",
 "Icon grid: 150 cutters vs 10, filling the frame.", "150+ vs ≈10", "REPORTED · CSIS", "tick cascade"),
("P4-09", "In one CSIS model, checks start about forty-eight hours after the announcement. And it works if three in four shipping firms simply go along with it, to avoid the risk.", "F37",
 "Stopwatch to 48:00 (kit2 one-off), then 4 ship icons, 3 turn to comply.", "48 HOURS · 3 IN 4 COMPLY", "SCENARIO · CSIS, 2024", "clock + soft hits"),
("P4-10", "Remember the gas. Eleven days in winter. Start the clock forty-eight hours after an announcement, and Taiwan has about nine days of gas before the lights become a choice.", "F21 F37 H7",
 "Return to the countdown dial: 11 → 9 DAYS; a city skyline silhouette with lights going out one block at a time.", "≈ 9 DAYS OF GAS LEFT", "ESTIMATE · our maths", "low drone"),
("P4-11", "And would America send ships to break a coast guard check? In a CSIS survey, only thirteen percent of American experts were completely confident it would.", "F38",
 "Bar: 13% US experts · 9% Taiwan experts 'COMPLETELY CONFIDENT'.", "13% CONFIDENT THE US WOULD ACT", "REPORTED · CSIS survey, 2024", "soft hit"),
("P4-12", "Let's stop and print what we have so far. A chip shortage with every plant open: used cars up forty-five percent. A quiet quarantine: a gas clock of about nine days, on an island that makes nine in ten of the best chips.", "F11 H7 F01",
 "R receipt printer: HALF-RECEIPT, three lines print.", "HALF-RECEIPT", "VERIFIED / ESTIMATE", "receipt printer"),
("P4-13", "So what would the full thing cost the rest of us?", "", "Receipt tears off; push to black.", "", "", "riser"),
])

part("Part 5: The money", "~11:40", [
("P5-01", "Part five. The money.", "", "P part card PART 5 · THE MONEY", "PART 5 · THE MONEY", "", "reverse cymbal + sub drop"),
("P5-02", "In February 2026, Bloomberg Economics updated its model of what a Taiwan crisis would cost in the first year. It ran two versions. A blockade, and a war.", "F44 F46",
 "D document: a model sheet with two tabs, BLOCKADE and WAR; red pen circles both.", "BLOOMBERG ECONOMICS · FEB 2026", "SCENARIO · Bloomberg via Insurance Journal", "page turn"),
("P5-03", "A blockade alone: the world economy shrinks by about five percent. America by about three. China by nearly nine.", "F46",
 "W mini-chart tiles: WORLD -5.3% · US -3.2% · CHINA -8.9% · TAIWAN -12.5%.", "BLOCKADE · YEAR ONE", "SCENARIO · Bloomberg, Feb 2026", "tile pops x4"),
("P5-04", "A war: the world shrinks by nearly ten percent. That's about ten point six trillion dollars. America by six and a half percent. Japan by almost fifteen. South Korea by twenty-three.", "F44 F45",
 "Bar chart grows country by country: WORLD -9.6% · US -6.6% · JAPAN -14.7% · KOREA -23% · CHINA -11%.", "WAR · YEAR ONE · -$10.6 TRILLION", "SCENARIO · Bloomberg, Feb 2026", "chart grow + sub"),
("P5-05", "For comparison, in 2020, the year of COVID, America's economy shrank by two point two percent. Both Taiwan versions are worse.", "F47",
 "Three bars side by side: COVID 2020 -2.2% · BLOCKADE -3.2% · WAR -6.6%.", "WORSE THAN COVID", "VERIFIED (2020) / SCENARIO", "soft hit"),
("P5-05b", "And China doesn't escape. In the war version, its economy shrinks by eleven percent. Taiwan's by an assumed forty. Everyone who starts this pays for it.", "F45",
 "Mirror bars (kit2 one-off): CHINA -11% left, TAIWAN -40% right, US -6.6% centre.", "CHINA -11% · TAIWAN -40% (ASSUMED)", "SCENARIO · Bloomberg, Feb 2026", "two low hits"),
("P5-06", "Let's turn that into a household. America produced about thirty point nine trillion dollars in 2025. There are about a hundred and thirty-seven million households. That's about two hundred and twenty-five thousand dollars of output each.", "F50 F51 H1",
 "Ledger maths card (kit2 one-off: long division on ruled paper): $30.86T ÷ 137M = $225,000.", "$30.86T ÷ 137M HOMES ≈ $225K", "ESTIMATE · BEA; Census; our maths", "pencil scratch"),
("P5-07", "A blockade takes about seven thousand dollars of that. A war, about fifteen thousand. COVID took about five. It's not money out of your pay packet line by line. It's lost work, lost sales, and lost hours, spread across everyone.", "H2 H3 H4",
 "Three coin stacks: $4,950 COVID · $7,200 BLOCKADE · $14,900 WAR.", "≈ $7,200 BLOCKADE · ≈ $14,900 WAR", "ESTIMATE · our maths", "coin drop x3"),
("P5-08", "Rhodium Group, another research firm, looked only at a blockade. It said well over two trillion dollars of activity would be at risk, and called that a floor, not a ceiling.", "F48",
 "Typed card: '$2 TRILLION+' with stamp 'FLOOR, NOT CEILING'.", "$2 TRILLION+ · 'A FLOOR'", "ESTIMATE · Rhodium Group, 2022", "stamp"),
("P5-09", "About one point six trillion of that is yearly revenue at firms that need chips. Phones, laptops, cars, medical machines, the servers behind AI.", "F48",
 "Cut-paper figures (K): five product cut-outs on a conveyor; each gets a red 'NO CHIP' tag.", "$1.6 TRILLION · CHIP-DEPENDENT SALES", "ESTIMATE · Rhodium Group", "tag clicks x5"),
("P5-09b", "In 2025, Taiwan sold about two hundred billion dollars of goods to America alone. Much of it was the servers and parts behind AI. A sealed strait stops that in a week.", "H6 F07",
 "Container stack graphic: boxes labelled SERVERS · CHIPS · PARTS pile to $198 BN; then a gate drops.", "≈ $198BN TAIWAN → US · 2025", "ESTIMATE · our maths on Taiwan MOF", "gate slam"),
("P5-10", "Why can't the chips just be made somewhere else? They're trying. TSMC has promised up to a hundred and sixty-five billion dollars for factories in Arizona. But one top-end plant costs more than twenty billion and takes years to build.", "F08 F09",
 "L footage [CALM]: construction site with cranes in a desert (no logos); paper label.", "$165BN ARIZONA · $20BN+ PER PLANT", "REPORTED · MarketScreener, Jun 2026", "low swell"),
("P5-11", "In 2021, we saw what a chip shortage did to car prices with every plant open. A blockade is that, on the scale of the whole factory floor.", "F11",
 "Return to the 2021 used-car card, then it scales up to fill the frame.", "2021 × THE WHOLE ISLAND", "", "sub hit"),
("P5-12", "But these are the costs of a crisis. What's the cost of the deals that might stop one?", "",
 "Push to two chairs at a table (cut-paper).", "", "", "riser"),
])

part("Part 6: The deal", "~14:20", [
("P6-01", "Part six. The deal.", "", "P part card PART 6 · THE DEAL", "PART 6 · THE DEAL", "", "reverse cymbal + sub drop"),
("P6-02", "In May 2026, Taiwan's lawmakers approved money for a fourteen-billion-dollar package of American weapons. Then the President met Xi Jinping in Beijing. Afterwards, he called the package a very good negotiating chip. It's been on hold since.", "F39",
 "D document: an arms package page with $14 BN highlighted; red pen circle on 'ON HOLD'.", "$14BN ARMS PACKAGE · ON HOLD SINCE MAY 2026", "REPORTED · Domino Theory, Oct 2026", "pen scratch"),
("P6-02b", "In September, the Secretary of State said American weapons stocks elsewhere were part of the decision. A weapon sent to one war is a weapon another can't have.", "F52",
 "Typed card: 'STOCKPILES ELSEWHERE' · RUBIO, SEP 2026; stamp REPORTED.", "STOCKPILES ARE PART OF IT", "REPORTED · Domino Theory", "stamp"),
("P6-03", "In September, a Hong Kong paper reported that Washington might hold big Taiwan arms sales until after the next summit, maybe to the end of the year.", "F40",
 "Calendar strip with SEP → NOV → DEC; 'MAYBE' stamped on DEC.", "HELD UNTIL AFTER APEC?", "REPORTED · SCMP (anonymous sources)", "stamp"),
("P6-04", "That summit is APEC, in Shenzhen, on the eighteenth and nineteenth of November. Ten days later, Taiwan holds local elections. In December, the leaders meet again at the G20 in Florida.", "F41",
 "Calendar card (kit2 one-off: wall planner): 18-19 NOV APEC · 28 NOV TAIWAN VOTES · DEC G20.", "18-19 NOV · 28 NOV · DEC", "REPORTED · AEI; Taipei Times", "tick x3"),
("P6-05", "And the trade truce between America and China only runs to the tenth of January 2027. That's the date your shop prices and tariffs hang on, and Taiwan is on the same table.", "F42",
 "B split-flap: TRUCE ENDS · 10 JAN 2027.", "TRADE TRUCE ENDS 10 JAN 2027", "REPORTED · Domino Theory", "split-flap clatter"),
("P6-06", "Here's the link back to Hormuz. Iran says the strait will reopen to Chinese ships, with special terms on fees. China is buying calm in one sea while it rehearses in another.", "F43",
 "M map: two seas lit at once, Hormuz (gold) and Taiwan Strait (orange).", "TWO STRAITS · ONE BUYER", "CLAIM · Iran via AEI, Nov 2026", "whoosh"),
("P6-07", "What if the deals fail and it does come to war? In twenty-four war games in 2023, CSIS found that America, Taiwan and Japan usually stopped an invasion. But they lost dozens of ships, hundreds of aircraft, and tens of thousands of service members. Taiwan's economy was devastated.", "F49",
 "L footage [SHADOW]: empty naval pier at dusk, flags still; no combat.", "24 WAR GAMES · 'DOZENS OF SHIPS, HUNDREDS OF AIRCRAFT'", "SCENARIO · CSIS, Jan 2023", "low drone, silence after 'devastated'"),
("P6-08", "That's the side of the bill no model prices. Twenty-three million people on the island. And the families of everyone sent to defend it.", "F10",
 "STILL [SHADOW] Ken Burns: Taipei at night from a distance, lights on; no faces.", "23 MILLION PEOPLE", "VERIFIED", "quiet piano note"),
("P6-08b", "And we should be honest about what nobody knows. Whether Beijing plans anything for 2027. Whether it would be a quarantine, a blockade or a war. Whether America would fight. And what those hundred ships were really doing.", "F26 F28 F38 F32",
 "X folder: four index cards stamped UNKNOWN, one by one.", "FOUR THINGS NOBODY KNOWS", "", "stamp x4"),
("P6-09", "So, line by line, what does it come to at your table?", "", "Receipt printer warms up.", "", "", "riser"),
])

part("The Receipt", "~16:40", [
("RC-01", "The Receipt. For an example American family. These are scenarios, not forecasts. Nobody knows if any of this happens.", "",
 "R receipt prints: header THE RECEIPT · WHAT HAPPENS IF CHINA INVADES TAIWAN.", "THE RECEIPT · SCENARIOS, NOT FORECASTS", "SCENARIO", "receipt printer"),
("RC-02", "Line one. Your car. The 2021 shortage added about forty-five percent to used cars, with Taiwan open. Treat that as the floor.", "F11 H5",
 "R line 1.", "YOUR CAR · +45% WAS THE FLOOR (2021)", "VERIFIED · BLS", "receipt print"),
("RC-03", "Line two. Your phone, laptop and anything with a screen. Nine in ten of the best chips come from one island. Price: not modelled. Supply: at risk.", "F01",
 "R line 2; price cell reads 'NOT MODELLED'.", "YOUR DEVICES · NOT MODELLED · AT RISK", "REPORTED · Rhodium", "receipt print"),
("RC-04", "Line three. Your share of the economy. A blockade: about seven thousand dollars a household. A war: about fifteen thousand. In year one.", "H2 H3",
 "R line 3.", "YOUR SHARE · ≈ $7,200 BLOCKADE · ≈ $14,900 WAR", "ESTIMATE · our maths on Bloomberg", "receipt print"),
("RC-05", "Line four. Your energy. Japan, Korea and Taiwan would all be bidding for gas, in a year when Hormuz is already tight. Not priced yet.", "F22 F45",
 "R line 4.", "YOUR ENERGY · NOT PRICED · TIGHT", "", "receipt print"),
("RC-06", "Line five. The dates to watch. The eighteenth of November. The twenty-eighth of November. The tenth of January.", "F41 F42",
 "R line 5 with three dates; stamp WATCH.", "WATCH · 18 NOV · 28 NOV · 10 JAN", "REPORTED", "receipt print + stamp"),
("RC-07", "What can you do? This is not financial advice. But some things make sense in any crisis. If you need a new phone, laptop or car anyway, don't wait for the next shock to buy it. Keep three to six months of essential bills in a buffer.", "",
 "X folder + index cards: BUY WHAT YOU NEED, NOT IN A PANIC · BUFFER 3-6 MONTHS.", "NOT FINANCIAL ADVICE", "", "card slides x2"),
("RC-08", "Test your budget with prices twenty percent higher. And don't trade on headlines. A summit photo can move markets in a day, and a drill can move them back.", "",
 "Index cards: +20% STRESS TEST · DON'T TRADE HEADLINES.", "", "", "card slides x2"),
("RC-09", "Tell us in the comments. Which would hit your home first, the chips or the energy? And where are you watching from?", "",
 "Comment prompt card; end screen to INV-008 The 1973 Invoice.", "CHIPS OR ENERGY: WHICH HITS YOU FIRST?", "", "riser air"),
("RC-10", "Out in the Pacific, the ships will go home, or they won't. The bill is already being written. Every crisis sends a bill. History keeps the receipts.", "F31",
 "Return to CO-01 map: ship dots fade one by one; slow fade to black; tagline in plain type.", "EVERY CRISIS SENDS A BILL. HISTORY KEEPS THE RECEIPTS.", "", "silence, then one low note"),
])

def words(t): return len(re.findall(r"[A-Za-z0-9'’.\-]+", t))

def build():
    out = []
    total = sum(words(r[1]) for _, _, rows in PARTS for r in rows)
    out.append(f"# {VID} What Happens If China Invades Taiwan: script v1\n")
    out.append("v1, 2026-11-10. Search phrase: **what happens if China invades Taiwan** (spoken at ~0:12 in CO-02; again in RC-01; add once per part after voice if needed). Lead title: **What Happens If China Invades Taiwan? Your 2027 Bill** (51 chars).\n")
    out.append(f"Narration: **{total} words, about {total/132:.0f} minutes** of voice at 132 wpm; with part cards and pauses the cut runs about {total/132+1.5:.0f}-{total/132+2.5:.0f} min. Every number points to a row in `facts.md` (F = fact, H = household maths). Every cost is a SCENARIO or ESTIMATE and the narration says so.\n")
    out.append("Visual key: N ledger number · L footage + paper label · D document (highlight + red pen, never a magnifier) · T typed card + stamp · B split-flap · K cut-paper figures · M navy map · P part card · R receipt · W mini-chart tiles · X folder + index cards · 'kit2 one-off' = a new type for this video. Footage/stills grade in brackets: [SHADOW] [CALM] [COLOUR] [INTENSE]. All graphics on the dark ledger background, beige cards, colour shots at x0.8 brightness.\n")
    for title, start, rows in PARTS:
        out.append(f"\n## {title} (starts {start})\n")
        out.append("| Code | Narration | Words | Facts | Visual | On-screen text | Tag + source | SFX |")
        out.append("|---|---|---|---|---|---|---|---|")
        for c, n, f, v, o, t, s in rows:
            out.append(f"| {VID} · {c} | {n} | {words(n)} | {f} | {v} | {o} | {t} | {s} |")
    return "\n".join(out), total

if __name__ == "__main__":
    md, total = build()
    extra = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "script_v1_extras.md")).read()
    dst = "/mnt/project-files/the-history-invoice/videos/INV-009-taiwan-2027/INV-009-taiwan-2027-script-v1.md"
    open(dst, "w").write(md + "\n\n" + extra)
    print(total)
