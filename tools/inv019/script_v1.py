# INV-019 What If the Iran War Ends Tomorrow? Here's Your Bill. Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Visual kinds: G graphic (spec19) · F clip · S photo.
# Search phrase: "Iran war ends" in the title, spoken by 0:15 and once per part.
# Iran follow-up series #2: answer + number inside 30 s, subscribe ask at ~4:30 naming next week's video,
# end screen back to "What Happens If the Iran War Restarts?". Every caption types on with a key sound.
import os
VID = "INV-019"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "PEACE? NO TALKS YET", "P2": "OIL FALLS IN HOURS", "P3": "PUMPS: 2-8 WEEKS", "P4": "INSURANCE, MINES: MONTHS",
          "P5": "-10p/L · -40¢/GAL", "P6": "PEACE ON PAPER ≠ PEACE AT SEA"}

part("Cold open", "0:00", [
("CO-01", "If the Iran war ended tomorrow, your petrol would not get cheaper {tomorrow}. The oil price would drop in hours. Your bill would take weeks. And some of it would take months.", "A16 A17",
 "G two clocks: OIL · HOURS spins fast; YOUR BILL · WEEKS crawls; on 'tomorrow' a stamp NOT TOMORROW", "OIL: HOURS · YOUR BILL: WEEKS", "VERIFIED · Borenstein & Cameron (NBER); RAC", "tick clock"),
("CO-02", "Here's the short answer. Before this war, oil was about seventy-one dollars a barrel. Today it's about {eighty-eight}. Peace could take it back.", "A06 A07",
 "G price ladder: $71 BEFORE THE WAR · $88 TODAY; bracket -$17", "$88 → $71?", "REPORTED · S&P Platts 27 Feb 2026; Gulf News 24 Nov 2026", "register ding"),
("CO-03", "That's roughly ten pence off every litre in Britain, and about {forty cents} off every gallon in America. About a fiver every time you fill a tank.", "A28",
 "G two price tags -10p A LITRE · -40¢ A GALLON; small tag -£5 A TANK", "-10p A LITRE · -40¢ A GALLON", "ILLUSTRATION · our maths, $88 back to $71", "register ding"),
("CO-04", "But your energy bill goes up by a quarter in {January}, peace or no peace. And the last time this war stopped, the ships still didn't move.", "A23 A11",
 "G number card +26% · ENERGY CAP FROM 1 JAN 2027 · £2,166", "ENERGY CAP +26% IN JANUARY", "REPORTED · Ofgem, 25 Nov 2026", "stamp thud"),
("CO-05", "So in this video, we'll work out what falls fast, what falls slow, and what doesn't fall at {all}.", "",
 "G roadmap: HOW CLOSE IS PEACE · THE LAST TIME · FAST · SLOW · YOUR BILL", "FAST · SLOW · NOT AT ALL", "", "riser"),
])

part("Part 1: How close is peace?", "~1:10", [
("P1-01", "Part one. How close is peace?", "", "G part card PART 1 · HOW CLOSE IS PEACE?", "PART 1 · HOW CLOSE IS PEACE?", "", "reverse cymbal + sub drop"),
("P1-02", "Right now, not very. Iran's chief negotiator says there will be no talks with America until Iran's seven {conditions} are met.", "A01",
 "G typed file: IRAN'S 7 CONDITIONS · NO TALKS UNTIL MET", "NO TALKS UNTIL 7 CONDITIONS", "REPORTED · Ghalibaf via Gulf News, 24 Nov 2026", "typing"),
("P1-03", "The ones reported so far: lift the naval blockade. Ease the sanctions. Release Iran's frozen money. Stop the fighting on every front. And declare the war formally {over}.", "A01",
 "G checklist of 5: LIFT BLOCKADE · EASE SANCTIONS · RELEASE FUNDS · STOP ALL FRONTS · DECLARE IT OVER", "5 OF 7 CONDITIONS REPORTED", "REPORTED · Gulf News, 24 Nov 2026", "pen"),
("P1-04", "On Thanksgiving, President Trump told American troops he's giving Iran every opportunity to make a deal. But he said he doubts they'll {agree}.", "A02",
 "G quote card 'Every opportunity' · Trump to US troops, 26 Nov 2026; pen underline on DOUBTS", "TRUMP: 'EVERY OPPORTUNITY'", "REPORTED · via Jerusalem Post, 26 Nov 2026", "paper"),
("P1-04b", "And he made his own red line clear. He said he just doesn't want Iran to have a nuclear {weapon}. That's the American condition behind all the others.", "A31",
 "G quote card 'I just don't want them to have a nuclear weapon' · Trump, 26 Nov 2026", "US RED LINE: NO IRANIAN BOMB", "REPORTED · via Jerusalem Post, 26 Nov 2026", "paper"),
("P1-05", "He called his blockade of Iran's ports the largest ever. It's been back in place since the {fifteenth} of July.", "A02 A12",
 "G timeline: 13 APR BLOCKADE · 8 JUL TRUCE COLLAPSES · 15 JUL BLOCKADE BACK · TODAY", "BLOCKADE BACK SINCE 15 JULY", "REPORTED · Wikipedia; Trump 26 Nov 2026", "map whoosh"),
("P1-06", "Behind the scenes, Qatar is trying. Its prime minister raised restarting talks with the US Secretary of State in Washington on the twenty-third of {November}.", "A05",
 "G map: Qatar pin → Washington arc; label TALKS ABOUT TALKS · 23 NOV", "QATAR: TALKS ABOUT TALKS", "REPORTED · Gulf News, 24 Nov 2026", "map whoosh"),
("P1-07", "And in Washington, there's a money {clock}. Federal funding runs out on the eleventh of December.", "A03",
 "G calendar card 11 DEC circled in red pen · FUNDING DEADLINE", "FUNDING RUNS OUT 11 DEC", "REPORTED · Al Jazeera, 26 Nov 2026", "tick clock"),
("P1-08", "A Reuters Ipsos poll found seventy-one percent of Americans want the new Congress to end this war. And in January, the Senate changes {hands}.", "A03",
 "G gauge 71% · WANT CONGRESS TO END THE WAR; small line SENATE: 53-45 R → 54-44 D IN JANUARY", "71% WANT IT ENDED", "REPORTED · Reuters/Ipsos via Al Jazeera", "chart"),
("P1-08b", "But money alone doesn't stop a war. The President can veto, and Democrats don't have the votes to override him. One analyst told Al Jazeera that cutting the funds does not end the war, because the Pentagon can keep going on what it already has for some {time}.", "A32",
 "G flow: CONGRESS CUTS FUNDS → PRESIDENT VETOES → NO 2/3 OVERRIDE → WAR CONTINUES", "FUNDING ≠ PEACE", "REPORTED · Al Jazeera, 26 Nov 2026", "chain"),
("P1-09", "The war has already cost America more than {forty-eight} billion dollars, according to the Pentagon.", "A04",
 "G number card $48 BN+ · US COST OF THE WAR SO FAR", "US COST: $48BN+", "REPORTED · Pentagon via Gulf News", "counter"),
("P1-10", "And inside Iran, the money is cracking. On the black market, one dollar now buys about two point eight {million} rials.", "A25",
 "G number card 2.8M RIALS = $1", "RIAL: 2.8M PER DOLLAR", "REPORTED · Gulf News, 24 Nov 2026", "counter"),
("P1-11", "So both sides are under pressure. That's usually how wars end. Not with a winner, but with two sides who can't afford to keep {going}.", "",
 "G split: USA · FUNDING CLOCK, 71% vs IRAN · RIAL CRASH, BLOCKADE; both bars draining", "BOTH SIDES SQUEEZED", "", "riser"),
("P1-11b", "And a deal would bring something else back: Iran's own oil. Lift the blockade, and Iranian barrels start flowing to buyers again. More supply, on top of less fear. That's why traders would sell the moment it's {signed}.", "A12",
 "G flow: DEAL → BLOCKADE LIFTED → IRANIAN OIL FLOWS → MORE SUPPLY → LOWER PRICE", "MORE SUPPLY + LESS FEAR", "ILLUSTRATION · how a deal moves supply", "chain"),
("P1-12", "So let's do the thought experiment. Imagine the war ends tomorrow. Here's what the last time tells us {first}.", "",
 "G card: IMAGINE IT ENDS TOMORROW", "IMAGINE IT ENDS TOMORROW", "SCENARIO · not a forecast", "paper"),
])

part("Break", "~4:30", [
("BR-01", "Quick one. This is part two of our Iran War Bill series. Next week: oil fell, so why didn't your bill? If you want that one, {subscribe}.", "",
 "G subscribe card: 2 OF 4 · NEXT WEEK: OIL FELL. WHY DIDN'T YOUR BILL?", "SUBSCRIBE · NEXT: OIL FELL", "", "soft tick"),
])

part("Part 2: The last time a war ended", "~4:45", [
("P2-01", "Part two. The last time a war like this ended.", "", "G part card PART 2 · THE LAST TIME", "PART 2 · THE LAST TIME", "", "reverse cymbal + sub drop"),
("P2-02", "Go back to the summer of 1990. At the end of July, oil is about twenty-one dollars a barrel. Then, on the second of August, Iraq invades {Kuwait}.", "A13",
 "G Gulf map: Iraq arrow into Kuwait on 'Kuwait'; label 2 AUG 1990", "2 AUG 1990 · IRAQ INVADES KUWAIT", "VERIFIED · Wikipedia, 1990 oil price shock", "boom on 'Kuwait'"),
("P2-03", "By the middle of October, oil has more than doubled, to about forty-six {dollars}.", "A13",
 "G line chart 1990: JUL $21 → OCT $46; mark x2.2", "$21 → $46", "VERIFIED · Wikipedia", "chart"),
("P2-03b", "Measured month by month, the average price went from seventeen dollars in July to thirty-six in October. Double, in one {season}.", "A13",
 "G bars: JUL 1990 $17 · OCT 1990 $36 (monthly average)", "MONTHLY AVERAGE: $17 → $36", "VERIFIED · Wikipedia", "chart"),
("P2-04", "Then, on the night of the sixteenth of January 1991, the American-led air war begins. Operation Desert {Storm}.", "",
 "G number card 16 JAN 1991 · DESERT STORM BEGINS", "16 JAN 1991 · DESERT STORM", "VERIFIED", "boom"),
("P2-05", "Everyone expected oil to explode. Instead, the next day, it collapsed. Brent fell from about thirty dollars to just under {twenty-one}.", "A14",
 "G price ladder down: $30 → $20.75; bracket -31% IN ONE DAY", "-31% IN ONE DAY", "VERIFIED · Oil & Gas Journal, 21 Jan 1991", "sub hit"),
("P2-05b", "Part of the reason was planning. The International Energy Agency had lined up an emergency release of two and a half million barrels a day from {stockpiles}.", "A33",
 "G number card 2.5M BARRELS A DAY · IEA EMERGENCY RELEASE, JAN 1991", "IEA: 2.5M BARRELS A DAY", "VERIFIED · Oil & Gas Journal, 21 Jan 1991", "counter"),
("P2-06", "At the time, it was the biggest one-day fall in oil {history}. Traders weren't betting on the war. They were betting on the end of the war.", "A14",
 "G card: THEY BET ON THE END OF THE WAR", "BIGGEST 1-DAY FALL (TO THEN)", "VERIFIED · OGJ", "stamp thud"),
("P2-07", "But the damage was already done. The price spike helped push America into a recession, and it took about nine months to fully {fade}.", "A15",
 "G chain: OIL SPIKE → RECESSION → ≈ 9 MONTHS TO FADE", "≈ 9 MONTHS TO FADE", "VERIFIED · Wikipedia", "chain"),
("P2-08", "Now jump to this year. The eighth of April 2026. A two-week ceasefire between America and {Iran}.", "A10",
 "G timeline: 28 FEB WAR · 8 MAR $100 · 8 APR CEASEFIRE", "8 APR 2026 · CEASEFIRE", "REPORTED · Wikipedia", "paper"),
("P2-09", "Overnight, Brent fell almost fifteen dollars, about fourteen {percent}, to ninety-four.", "A10",
 "G bars: 7 APR $109 · 8 APR $94; drop label -13.6% OVERNIGHT", "-13.6% OVERNIGHT", "REPORTED · Reuters, 8 Apr 2026", "sub hit"),
("P2-10", "That's the fast part. Oil is traded on screens. It reacts to a headline in {seconds}.", "",
 "G card: OIL MOVES ON A HEADLINE", "OIL MOVES IN SECONDS", "", "glitch"),
("P2-11", "Now the slow part. A day after that ceasefire, there was still no sign the strait was reopening. Ships were being {stopped} again.", "A11",
 "G Hormuz map: ships stacked at the strait, red X on 'stopped'", "9 APR: SHIPS STOPPED AGAIN", "REPORTED · Wikipedia", "map whoosh"),
("P2-12", "Iran was charging tolls of more than a million dollars a ship. Four days later, talks had failed, and the American blockade {began}.", "A11 A12",
 "G price tag TOLL $1M+ A SHIP; then stamp 13 APR BLOCKADE", "$1M TOLLS · THEN A BLOCKADE", "REPORTED · Wikipedia", "stamp thud"),
("P2-12b", "In June they tried again. A sixty-day extension, and a signed memorandum to negotiate a final deal. On the eighth of July, after more attacks on ships, that truce collapsed {too}.", "A29",
 "G timeline: 17 JUN MoU · 60-DAY EXTENSION · 8 JUL COLLAPSE (red X)", "JUNE DEAL · JULY COLLAPSE", "REPORTED · Wikipedia", "stamp thud"),
("P2-13", "So that's lesson one. Peace on paper moves oil in a night. Peace at sea moves ships in {weeks}, if it holds at all.", "",
 "G split: PEACE ON PAPER · OIL · 1 NIGHT vs PEACE AT SEA · SHIPS · WEEKS", "PAPER: 1 NIGHT · SEA: WEEKS", "", "stamp thud"),
("P2-14", "Running total. Line one. Oil falls in {hours}.", "",
 "G receipt running total line 1: OIL FALLS IN HOURS", "OIL FALLS IN HOURS", "", "printer"),
])

part("Part 3: What falls fast", "~8:20", [
("P3-01", "Part three. What falls fast.", "", "G part card PART 3 · WHAT FALLS FAST", "PART 3 · WHAT FALLS FAST", "", "reverse cymbal + sub drop"),
("P3-02", "Start with the barrel. Before the first bombs fell, on the twenty-seventh of February, Brent closed at about seventy-one {dollars}.", "A07",
 "G number card $70.94 · BRENT, 27 FEB 2026", "BRENT $70.94 · 27 FEB", "REPORTED · S&P Platts", "counter"),
("P3-03", "In March it rose faster than in any month in history. Past a hundred on the eighth of March, and on to a peak of a hundred and twenty-{six}.", "A08 A09",
 "G line chart Brent 2026: FEB 71 · 8 MAR 100 · PEAK 126 · 24 NOV 88", "PEAK $126", "REPORTED · Reuters; Wikipedia", "chart"),
("P3-04", "Today it's back to about eighty-eight. So most of the war is already out of the price. There's about seventeen dollars of fear {left}.", "A06 A07",
 "G stacked bar: $71 PRE-WAR + $17 WAR FEAR = $88", "$17 OF FEAR LEFT", "ILLUSTRATION · our maths", "chart"),
("P3-04b", "Why is there still fear in the price? Because about twenty million barrels a day normally pass through Hormuz, and every week brings another attack or another mine {claim}.", "A34",
 "G Gulf map: tanker streams through Hormuz; counter 20M BARRELS A DAY", "≈ 20M BARRELS A DAY", "REPORTED · Wikipedia", "map whoosh"),
("P3-05", "A barrel is forty-two American gallons, or a hundred and fifty-nine {litres}.", "A27",
 "G barrel splitting into 42 US GALLONS / 159 LITRES", "1 BARREL = 42 GAL = 159 L", "VERIFIED · unit conversion", "pop"),
("P3-06", "Take seventeen dollars off the barrel, and that's about forty cents off every {gallon} in America.", "A28",
 "G price tag US · EVERY GALLON -40¢", "-40¢ A GALLON", "ILLUSTRATION · crude cost only", "register ding"),
("P3-07", "In Britain, about eight pence a litre, and with VAT on top, about {ten}.", "A28",
 "G stacked: CRUDE ≈ 8p + VAT ≈ 2p = ≈ -10p A LITRE", "≈ -10p A LITRE", "ILLUSTRATION · our maths at $1.30/£", "chart"),
("P3-08", "A fifty-five litre tank, about a {fiver} cheaper.", "A28",
 "G price tag 55-LITRE TANK -£5", "-£5 A TANK", "ILLUSTRATION · our maths", "register ding"),
("P3-08b", "In America, some of that is already happening. The average gallon was three seventy-eight on the seventeenth of November, the lowest since March. Back in May, it topped four fifty, a four-year {record}.", "A35",
 "G line chart US GALLON: MAY $4.50+ → 17 NOV $3.78", "US: $4.50+ → $3.78", "REPORTED · AAA; AP", "chart"),
("P3-09", "But here's the catch. Pumps don't move at the speed of {screens}.", "",
 "G card: PUMPS DON'T MOVE AT SCREEN SPEED", "PUMPS ≠ SCREENS", "", "paper"),
("P3-10", "Petrol stations buy their fuel weeks ahead. So a fall in the wholesale price usually takes two to four weeks to reach the {forecourt}.", "A17",
 "G flow: OIL PRICE → WHOLESALE → FORECOURT STOCK → YOUR PUMP; label 2-4 WEEKS", "2-4 WEEKS TO THE PUMP", "REPORTED · PetrolPrices.co.uk; RAC", "chain"),
("P3-11", "And there's an old pattern. A famous American study found that when crude goes up, nearly all of it reaches the pump within four weeks. When crude goes down, it takes about {eight}.", "A16",
 "G bars: PRICE RISE · 4 WEEKS vs PRICE FALL · 8 WEEKS", "UP: 4 WEEKS · DOWN: 8 WEEKS", "VERIFIED · Borenstein & Cameron, NBER", "chart"),
("P3-12", "Economists call it rockets and feathers. Prices go up like a rocket, and float down like a {feather}.", "A16",
 "G split: ROCKET ↑ vs FEATHER ↓ (drawn icons)", "ROCKETS & FEATHERS", "VERIFIED", "whoosh"),
("P3-12b", "Why? Partly stock bought at the old price. But Britain's competition watchdog found something else in 2022: a pattern of prices rising fast and falling slowly, especially for {diesel}.", "A37",
 "G card: CMA 2022 · 'ROCKET AND FEATHER PATTERNS' · WORST IN DIESEL", "CMA: ROCKETS & FEATHERS, 2022", "VERIFIED · CMA road fuel study, July 2023", "paper"),
("P3-13", "And in Britain right now, you're already owed a cut. The AA says wholesale petrol has fallen more than fifteen pence a litre since mid-October, and another ten pence off the pump should be on the {way}.", "A18",
 "G two numbers: WHOLESALE -15p+ · PUMP CUT DUE ≈ 10p", "ALREADY OWED ≈ 10p", "REPORTED · AA, 11 Nov 2026", "counter"),
("P3-14", "So peace would land on top of a cut you're still waiting for. Running total. Line two. Pumps take two to eight {weeks}.", "",
 "G receipt running total line 2: PUMPS TAKE 2-8 WEEKS", "PUMPS: 2-8 WEEKS", "", "printer"),
])

part("Part 4: What falls slow", "~11:30", [
("P4-01", "Part four. What falls slow.", "", "G part card PART 4 · WHAT FALLS SLOW", "PART 4 · WHAT FALLS SLOW", "", "reverse cymbal + sub drop"),
("P4-02", "First, the water itself. Iran is thought to have laid mines in this strait. The Pentagon told Congress clearing them could take up to six months, and that it can't start until the fighting {stops}.", "A19",
 "G calendar 6 months; stamp STARTS AFTER THE FIGHTING STOPS", "UP TO 6 MONTHS TO CLEAR", "REPORTED · Pentagon via Washington Post", "tick clock"),
("P4-02b", "Clearing is slow, careful work. Find an object on the sea floor. Check it. Destroy it. Move to the next one. Laying a mine can take a day. Clearing one can take up to two hundred times as {long}.", "A38",
 "G sea floor drone sweep; label FIND · CHECK · DESTROY · REPEAT", "CLEARING: UP TO 200x SLOWER", "REPORTED · Wikipedia, Naval mine", "tick clock"),
("P4-03", "So peace day is day one of the clean-up, not the {last} day.", "",
 "G card: PEACE DAY = CLEAN-UP DAY 1", "PEACE DAY = DAY 1", "", "stamp thud"),
("P4-04", "Second, insurance. Before the war, cover for a tanker cost one to three percent of the ship's value. Now it's seven and a half to {ten}.", "A20",
 "G bars: BEFORE 1-3% · NOW 7.5-10%; tag ≈ $21M A TRIP", "WAR COVER 7.5-10%", "REPORTED · S&P Global", "chart"),
("P4-05", "Insurers don't cut prices on a headline. They cut them after months without a claim. Months of ships going through and coming out the other {side}.", "",
 "G flow: CEASEFIRE → SAFE TRANSITS → MONTHS → LOWER PREMIUMS", "INSURERS WAIT FOR MONTHS", "ILLUSTRATION · how war cover works", "chain"),
("P4-06", "Third, the traffic jam. In April, about two thousand ships and twenty thousand seafarers were stuck inside the {Gulf}.", "A21",
 "G dot grid 20,000 SEAFARERS · 2,000 SHIPS", "20,000 SEAFARERS STUCK", "REPORTED · IMO, 21 Apr 2026", "pop"),
("P4-07", "Even with the door open, a queue like that takes weeks to clear. Ports clog. Schedules slip. Freight stays {expensive}.", "",
 "G chain: QUEUE → CLOGGED PORTS → LATE SHIPS → HIGH FREIGHT", "THE QUEUE TAKES WEEKS", "ILLUSTRATION", "chain"),
("P4-08", "Fourth, diesel. The world is still short of it. The AA says wholesale diesel has fallen only about four pence since {mid-October}.", "A24",
 "G two numbers: PETROL WHOLESALE -15p · DIESEL WHOLESALE -4p", "DIESEL: ONLY -4p", "REPORTED · AA, 11 Nov 2026", "counter"),
("P4-09", "And diesel moves almost everything you buy. Lorries, tractors, delivery {vans}.", "",
 "G chain: DIESEL → LORRIES → SHOPS → YOUR BASKET", "DIESEL MOVES EVERYTHING", "", "chain"),
("P4-10", "Fifth, fertiliser. Up to thirty percent of the world's traded fertiliser normally sails through Hormuz. Urea, the most common one, was up about half by late {March}.", "A22",
 "G line chart UREA FEB 100 → LATE MAR 150", "UREA +50%", "REPORTED · Wikipedia", "chart"),
("P4-11", "Fertiliser bought this spring grows the wheat harvested next summer and baked the year after that. That bill is already in the {post}.", "A22",
 "G chain: FERTILISER → FIELD → HARVEST → BREAD, label ≈ A YEAR", "BREAD: A YEAR BEHIND", "ILLUSTRATION · the usual lag", "chain"),
("P4-12", "And sixth, the one that surprises people. Your energy bill. Ofgem's price cap goes up twenty-six percent on the first of January, to two thousand one hundred and sixty-six pounds a year for a typical {home}.", "A23",
 "G number card £2,166 · +26% · FROM 1 JAN 2027; faded £1,723", "£2,166 A YEAR · +26%", "REPORTED · Ofgem, 25 Nov 2026", "stamp thud"),
("P4-12b", "Why? Because Europe's gas market is tied to this strait too. Before the war, Europe got about one eighth of its liquefied gas from Qatar, through {Hormuz}.", "A36",
 "G map: LNG route Qatar → Hormuz → Suez → Europe; label 12-14% OF EUROPE'S LNG", "12-14% OF EUROPE'S LNG", "REPORTED · Wikipedia", "map whoosh"),
("P4-12c", "And gas sets the price of electricity on most days in Britain. So when gas jumps, both halves of your energy bill {jump}.", "",
 "G chain: QATAR LNG → GAS PRICE → POWER PRICE → BOTH HALVES OF YOUR BILL", "GAS SETS THE POWER PRICE", "VERIFIED · how the GB power market prices", "chain"),
("P4-13", "That cap is set from wholesale prices in the months before. So a peace deal in December can't touch January's bill. The earliest it could show up is the next cap, in {April}.", "A30",
 "G calendar: DEC PEACE? · JAN CAP LOCKED · APR NEXT CAP circled", "EARLIEST RELIEF: APRIL", "VERIFIED · Ofgem", "pen"),
("P4-14", "Running total. Line three. Insurance, mines, diesel and gas take {months}.", "",
 "G receipt running total line 3: INSURANCE, MINES, GAS: MONTHS", "MONTHS, NOT DAYS", "", "printer"),
])

part("Part 5: Your bill", "~15:00", [
("P5-01", "Part five. Your bill, week by week.", "", "G part card PART 5 · YOUR BILL", "PART 5 · YOUR BILL", "", "reverse cymbal + sub drop"),
("P5-02", "Let's put it on a calendar. This is a scenario, not a forecast. Peace is signed on {day one}.", "",
 "G roadmap: DAY 1 · WEEK 1 · MONTH 1 · MONTH 3 · MONTH 6", "PEACE: DAY 1", "SCENARIO · not a forecast", "riser"),
("P5-03", "Day one. Oil drops. If 1991 and this April are any guide, it could fall ten or fifteen percent in a single {session}.", "A10 A14",
 "G bars: 1991 -31% · APR 2026 -13.6% · DAY 1 ?", "DAY 1: OIL DROPS", "SCENARIO · based on 1991 and Apr 2026", "sub hit"),
("P5-04", "Week one. Nothing at your pump yet. The fuel in the ground was bought at the old {price}.", "A17",
 "G card: WEEK 1 · PUMP UNCHANGED", "WEEK 1: NO CHANGE", "SCENARIO", "paper"),
("P5-05", "Month one. Petrol starts to fall. If oil goes back to its pre-war level, that's up to ten pence a litre, or forty cents a gallon, over the following {weeks}.", "A28 A16",
 "G price tags -10p A LITRE · -40¢ A GALLON", "MONTH 1-2: UP TO -10p", "SCENARIO · ILLUSTRATION", "register ding"),
("P5-06", "Diesel falls less, because the world is still short of {it}.", "A24",
 "G two numbers: PETROL -10p · DIESEL LESS", "DIESEL FALLS LESS", "SCENARIO", "pop"),
("P5-07", "Month three. The first ships with cheaper insurance get through. The first mines are found and cleared. Freight starts to {ease}.", "A19 A20",
 "G chain: CHEAPER COVER → MORE SHIPS → LOWER FREIGHT", "MONTH 3: FREIGHT EASES", "SCENARIO", "chain"),
("P5-08", "April. The next energy price cap. If gas prices have fallen by then, that's the first point your energy bill can come {down}.", "A30",
 "G calendar APR circled: NEXT CAP", "APRIL: FIRST ENERGY RELIEF", "SCENARIO · Ofgem cap cycle", "pen"),
("P5-09", "Month six. The strait is clear, if the clean-up goes well. And food? Food is last. Bread baked from this year's expensive fertiliser is still in the {shops}.", "A19 A22",
 "G chain: MONTH 6 · STRAIT CLEAR → FOOD LAST", "MONTH 6+: FOOD LAST", "SCENARIO", "chain"),
("P5-10", "So, the honest total. A tank of petrol, maybe a fiver cheaper within a couple of months. Your energy bill, higher in January and no relief before {April}.", "A23 A28",
 "G receipt card: PETROL -£5 A TANK (MONTHS) · ENERGY +26% JAN · FOOD: LAST", "THE HONEST TOTAL", "SCENARIO", "printer"),
("P5-10b", "Put it in a year. Say you fill up twice a month. Ten pounds a month back, a hundred and twenty a {year}.", "A28",
 "G price tags: 2 FILL-UPS A MONTH · -£10 A MONTH · -£120 A YEAR", "-£120 A YEAR ON PETROL", "ILLUSTRATION · our maths", "register ding"),
("P5-10c", "Now the energy cap. Up four hundred and forty-three pounds a year, from January. Even with peace, that's more than three times what you'd save at the {pump}.", "A23",
 "G two numbers: PETROL SAVED -£120 · ENERGY CAP +£443", "+£443 vs -£120", "ILLUSTRATION · Ofgem cap vs our fuel maths", "stamp thud"),
("P5-10d", "So for most British homes, even the best case for peace still leaves next year's bills {higher} than this year's.", "",
 "G card: EVEN WITH PEACE, 2027 COSTS MORE", "PEACE STILL COSTS MORE", "SCENARIO", "paper"),
("P5-11", "And in America, gas could drop by up to forty cents a gallon, but diesel and groceries would lag {behind}.", "A28",
 "G price tag US GAS -40¢ · DIESEL + GROCERIES LAG", "US: -40¢ GAS", "SCENARIO", "register ding"),
("P5-12", "Running total. Line four. Peace saves you a fiver a tank, {eventually}.", "",
 "G receipt running total line 4: -£5 A TANK, EVENTUALLY", "-£5 A TANK, EVENTUALLY", "", "printer"),
])

part("Part 6: What could stop it", "~17:40", [
("P6-01", "Part six. What could stop the money coming back.", "", "G part card PART 6 · WHAT COULD STOP IT", "PART 6 · WHAT COULD STOP IT", "", "reverse cymbal + sub drop"),
("P6-02", "First, a peace that's only on paper. That's what happened in April, and again in July, when the truce {collapsed}.", "A12 A29",
 "G timeline: 8 APR CEASEFIRE · 13 APR BLOCKADE · 17 JUN MoU · 8 JUL COLLAPSE", "TWO TRUCES ALREADY FAILED", "REPORTED · Wikipedia", "stamp thud"),
("P6-03", "Second, the mines. A single mine strike after a peace deal would send insurers straight back to war {rates}.", "A19 A20",
 "G card: ONE MINE = BACK TO WAR RATES", "ONE MINE = WAR RATES", "ILLUSTRATION", "boom"),
("P6-04", "And third, the stations themselves. If the pumps keep falling like feathers, the cut you're owed arrives late, or not at {all}.", "A16 A18",
 "G feather icon drifting down slowly next to a falling oil line", "FEATHERS", "VERIFIED · rockets and feathers", "whoosh"),
("P6-04b", "When prices float down slowly, someone keeps the difference for a while. Usually it's the stations and the refiners, not the drivers. In 2022, Britain's competition watchdog found supermarket fuel margins had risen by six pence a {litre}.", "A37",
 "G number card +6p A LITRE · SUPERMARKET FUEL MARGINS 2019 → 2022 (CMA)", "CMA: MARGINS +6p A LITRE", "VERIFIED · CMA road fuel study, July 2023", "counter"),
("P6-04c", "That's exactly what our next video is about. Oil has already fallen. So why hasn't your {bill}?", "",
 "G card: NEXT WEEK · OIL FELL. WHY DIDN'T YOUR BILL?", "NEXT: OIL FELL. WHY DIDN'T YOUR BILL?", "", "riser"),
("P6-05", "So here's what to watch. Do talks actually start? Do ships start moving through the strait? And does your pump price follow the oil price {down}?", "",
 "G checklist: TALKS START? · SHIPS MOVING? · PUMP FOLLOWING OIL?", "WHAT TO WATCH", "", "pen"),
("P6-05b", "And watch Washington on the eleventh of December. That's the day the money question gets {answered}.", "A03",
 "G calendar card 11 DEC circled · FUNDING DEADLINE", "WATCH: 11 DECEMBER", "REPORTED · Al Jazeera", "pen"),
("P6-06", "Wars end on a date. Their bills don't. They taper off for months, and you pay the {tail}.", "",
 "G card: WARS END ON A DATE. BILLS DON'T.", "BILLS DON'T END ON A DATE", "", "stamp thud"),
])

part("The Receipt", "~18:50", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. Peace drops oil in {hours}.", "A10 A14", "G receipt line 1 prints", "OIL: HOURS", "", "printer"),
("RC-03", "Line two. It reaches your pump in two to eight {weeks}.", "A16 A17", "G receipt line 2", "PUMP: 2-8 WEEKS", "", "printer"),
("RC-04", "Line three. Insurance, mines and freight take {months}.", "A19 A20", "G receipt line 3", "SHIPS + INSURANCE: MONTHS", "", "printer"),
("RC-05", "Line four. Your energy bill rises a quarter in January, {regardless}.", "A23", "G receipt line 4", "ENERGY CAP +26% IN JAN", "", "printer"),
("RC-06", "Line five. The prize: about ten pence a litre, or forty cents a {gallon}.", "A28", "G receipt line 5", "-10p A LITRE · -40¢ A GALLON", "", "printer"),
("RC-07", "Wars end on a date. Bills taper. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp PAID IN INSTALMENTS; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: next video tile WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-019 What If the Iran War Ends Tomorrow? Here's Your Bill: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/125:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not a forecast.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-019-iran-peace/INV-019-iran-peace-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
