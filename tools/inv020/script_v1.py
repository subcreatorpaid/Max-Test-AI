# INV-020 Iran War: Oil Fell. Why Didn't Your Bill? Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Visual kinds: G graphic (spec20) · F clip · S photo.
# Search phrase: "oil fell" + "Iran war" in the title, spoken by 0:15 and once per part.
# Iran follow-up series #3: answer + number inside 30 s, subscribe ask at ~4:30 naming next week's video (blockade a year),
# end screen back to "What Happens If the Iran War Restarts?". Every caption types on with a key sound.
import os
VID = "INV-020"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "OIL -25% · PUMP -4%", "P2": "UP 4 WKS · DOWN 8 WKS", "P3": "OWED ≈ 10p/L", "P4": "DIESEL STUCK ≈ 197p",
          "P5": "ENERGY CAP +26%", "P6": "SHOP AROUND: -19p/L"}

part("Cold open", "0:00", [
("CO-01", "At the end of October, oil was a hundred and seventeen dollars a barrel. Three and a half weeks later, it was eighty-{eight}. A quarter of the price, gone.", "B01 B03",
 "G line chart: 30 OCT $117.64 → 24 NOV $88 falling hard; label -25%", "OIL -25% IN 4 WEEKS", "REPORTED · Visordown; Gulf News", "sub hit"),
("CO-02", "So why is petrol still about a hundred and sixty-seven pence a litre? Down barely four percent from its {peak}?", "B04 B05",
 "G two numbers: OIL -25% vs PETROL -4%", "OIL -25% · PETROL -4%", "REPORTED · RAC; UK government weekly prices", "stamp thud"),
("CO-03", "Here's the short answer. Wholesale petrol has already fallen more than fifteen pence a litre. The AA says about ten pence of that still hasn't reached your {pump}.", "B06 B08",
 "G price tag: STILL OWED ≈ 10p A LITRE", "≈ 10p A LITRE STILL OWED", "REPORTED · AA, 11 Nov 2026", "register ding"),
("CO-04", "That's about five pounds fifty on every tank. And while oil fell, your energy bill was being set to rise by a quarter in {January}.", "B27 B21",
 "G two price tags: £5.50 A TANK OWED · ENERGY CAP +26% IN JANUARY", "£5.50 A TANK · ENERGY +26%", "ILLUSTRATION · our maths; REPORTED · Ofgem", "register ding"),
("CO-05", "Economists have a name for this. Rockets and feathers. In this video, we'll follow the money from the barrel to the {pump}, and find out who's holding it.", "B11",
 "G roadmap: THE FALL · ROCKETS & FEATHERS · WHERE THE 10p IS · DIESEL · YOUR OTHER BILLS", "WHO'S HOLDING YOUR 10p?", "", "riser"),
])

part("Part 1: The fall", "~1:00", [
("P1-01", "Part one. The fall.", "", "G part card PART 1 · THE FALL", "PART 1 · THE FALL", "", "reverse cymbal + sub drop"),
("P1-02", "Start with the barrel. On the thirtieth of October, Brent crude closed at a hundred and seventeen dollars and sixty-four {cents}.", "B01",
 "G number card $117.64 · BRENT CLOSE, 30 OCT 2026", "$117.64 · 30 OCT", "REPORTED · Visordown", "counter"),
("P1-03", "Five days later, on the fourth of November, it fell almost nine percent in a single day, to ninety-four sixty-{two}.", "B01",
 "G bars: 30 OCT $117.64 · 4 NOV $94.62; label -8.7% IN ONE DAY", "-8.7% IN ONE DAY", "REPORTED · Visordown", "sub hit"),
("P1-04", "Around the tenth of November, it dipped below ninety for the first time since {August}.", "B02",
 "G line chart continues: 10 NOV $89.66", "UNDER $90 · FIRST SINCE AUGUST", "REPORTED · PetrolPrices.co.uk", "chart"),
("P1-05", "And on the twenty-fourth, it was about eighty-eight. A three-month {low}.", "B03",
 "G number card $88 · 24 NOV · 3-MONTH LOW", "$88 · 3-MONTH LOW", "REPORTED · Gulf News", "counter"),
("P1-05b", "To be clear, that's not cheap. The day before this war began, back in February, Brent was about seventy-one dollars. At its worst this year, it hit a hundred and twenty-six. So eighty-eight is still about seventeen dollars of war left in the {price}.", "B24 B25",
 "G price ladder: $71 PRE-WAR · $88 NOW · $126 PEAK; bracket $17 OF WAR LEFT", "STILL $17 ABOVE PRE-WAR", "REPORTED · S&P Platts; Wikipedia", "chart"),
("P1-06", "Why? Hopes of a deal. Tankers still moving despite the attacks. Each headline about talks knocked a few more dollars off. And when Iran denied talks were happening, it bounced straight back above {ninety-two}.", "B02",
 "G linechart with headline flags: TALKS? ↓ · DENIAL ↑ $92", "HEADLINES MOVE OIL", "REPORTED · PetrolPrices.co.uk", "glitch"),
("P1-07", "Now look one step down the chain. Wholesale petrol, the price stations pay for a litre, was about seventy-seven pence in mid-October. In November, it was below sixty-{two}.", "B06",
 "G bars: WHOLESALE PETROL · MID-OCT 77p · NOV <62p", "WHOLESALE 77p → 62p", "REPORTED · AA", "chart"),
("P1-08", "That's a fall of more than fifteen pence a litre. Add VAT, and it should be worth more than eighteen pence at the {pump}.", "B06",
 "G stacked: WHOLESALE -15p + VAT -3p = ≈ -18p AT THE PUMP", "SHOULD BE ≈ -18p", "REPORTED · AA", "chart"),
("P1-09", "So what happened at the pump? On the fifth of October, the peak, petrol averaged one seventy-four ninety-four, and diesel just over two {pounds}.", "B04",
 "G price tags: PETROL 174.94p · DIESEL 200.20p · RAC, 5 OCT", "PEAK: 174.94p · 200.20p", "REPORTED · RAC", "register ding"),
("P1-10", "By the middle of November, the government's weekly figure was one sixty-seven for petrol. Diesel? One ninety-six seventy-{seven}.", "B05",
 "G price tags: PETROL 167.07p · DIESEL 196.77p · WEEK OF 16 NOV", "167.07p · 196.77p", "REPORTED · UK government weekly prices", "register ding"),
("P1-11", "Petrol down about eight pence. Diesel down about three and a half. Wholesale down fifteen. The gap is your {money}.", "B27",
 "G three bars: WHOLESALE -15p · PETROL -8p · DIESEL -3.5p; bracket THE GAP", "THE GAP IS YOUR MONEY", "ILLUSTRATION · our maths", "stamp thud"),
("P1-12", "In America it's a little better. The average gallon was three seventy-eight on the seventeenth of November, the lowest since March. But still above where it was before the {war}.", "B23",
 "G number card $3.78 · US AVERAGE GALLON · 17 NOV", "US: $3.78 · LOWEST SINCE MARCH", "REPORTED · AAA", "counter"),
("P1-12b", "Back in May, Americans were paying more than four fifty a gallon, a four-year record. So the fall there has been real. But even in America, economists have spent thirty years measuring the same {delay}.", "B23 B11",
 "G line chart US GALLON: MAY $4.50+ → NOV $3.78", "US: $4.50+ → $3.78", "REPORTED · AP; AAA", "chart"),
("P1-13", "Running total. Line one. Oil down a quarter. Petrol down about {four} percent.", "",
 "G receipt running total line 1: OIL -25% · PETROL -4%", "OIL -25% · PETROL -4%", "", "printer"),
])

part("Break", "~4:20", [
("BR-01", "Quick one. This is part three of our Iran War Bill series. Next week: what happens if the blockade of Iran lasts a whole year. {Subscribe}, so you don't miss it.", "",
 "G subscribe card: 3 OF 4 · NEXT WEEK: WHAT IF THE BLOCKADE LASTS A YEAR?", "SUBSCRIBE · NEXT: A YEAR OF BLOCKADE", "", "soft tick"),
])

part("Part 2: Rockets and feathers", "~4:35", [
("P2-01", "Part two. Rockets and feathers.", "", "G part card PART 2 · ROCKETS AND FEATHERS", "PART 2 · ROCKETS AND FEATHERS", "", "reverse cymbal + sub drop"),
("P2-02", "In the early nineteen-nineties, two American economists asked a simple question. Do petrol prices fall as fast as they {rise}?", "B11",
 "G typed file: BORENSTEIN & CAMERON · 'DO GASOLINE PRICES RESPOND ASYMMETRICALLY?'", "THE QUESTION", "VERIFIED · NBER w4138", "typing"),
("P2-03", "The answer was no. When crude went up, nearly all of it reached the pump within about four {weeks}.", "B11",
 "G rocket line: CRUDE UP → PUMP UP within 4 WEEKS", "UP: ≈ 4 WEEKS", "VERIFIED · NBER", "whoosh"),
("P2-04", "When crude went down, the fall took about eight weeks to pass {through}.", "B11",
 "G feather line: CRUDE DOWN → PUMP DOWN over 8 WEEKS", "DOWN: ≈ 8 WEEKS", "VERIFIED · NBER", "whoosh"),
("P2-05", "Up like a rocket. Down like a feather. And the biggest delay wasn't at the refinery. It was between the wholesale price and the {forecourt}.", "B11",
 "G chain: CRUDE → REFINERY → WHOLESALE → FORECOURT; red pen circle on WHOLESALE → FORECOURT", "THE DELAY IS AT THE FORECOURT", "VERIFIED · NBER", "pen"),
("P2-05b", "Their best guess at why? Short-run market power. When prices are falling, drivers stop shopping around, so a station can wait a little longer before it {cuts}.", "B11",
 "G flow: PRICES FALLING → DRIVERS STOP COMPARING → STATIONS WAIT → MARGIN GROWS", "WHY: SHORT-RUN MARKET POWER", "VERIFIED · Borenstein & Cameron", "chain"),
("P2-06", "Britain has seen this film before. Go back to the summer of 2022, after Russia invaded {Ukraine}.", "B12",
 "G card: SUMMER 2022", "SUMMER 2022", "", "paper"),
("P2-07", "On the third of July 2022, petrol hit a record one ninety-one fifty-three a litre. Diesel had peaked a week earlier at one ninety-nine {oh nine}.", "B12",
 "G price tags: PETROL 191.53p · 3 JUL 2022 · DIESEL 199.09p · 25 JUN 2022", "RECORD: 191.53p · 199.09p", "VERIFIED · RAC", "register ding"),
("P2-08", "Over the next eight weeks, wholesale petrol fell by twenty pence a litre. Pump prices fell by about {nine}.", "B13",
 "G two bars: WHOLESALE -20p vs PUMP -9p", "WHOLESALE -20p · PUMP -9p", "VERIFIED · RAC, 3 Aug 2022", "chart"),
("P2-09", "The RAC called it far too slow. It said drivers were paying nearly nine pounds too much for every {tank}.", "B13",
 "G quote card 'Far too slow' · RAC, Aug 2022; price tag £9 A TANK TOO MUCH", "RAC 2022: £9 A TANK TOO MUCH", "VERIFIED · RAC", "paper"),
("P2-10", "Retailer margins at the time were about twenty pence a litre. More than three times their long-term {average}.", "B13",
 "G bars: LONG-TERM MARGIN ≈ 6p · JULY 2022 ≈ 20p", "MARGINS ≈ 20p · 3x NORMAL", "VERIFIED · RAC", "chart"),
("P2-11", "Then the competition watchdog stepped in. In 2023, the CMA found supermarket fuel margins had risen by six pence a litre between 2019 and {2022}.", "B14",
 "G bars: SUPERMARKET MARGIN 2019 4.6p · 2022 10.8p", "+6p A LITRE · 2019 → 2022", "VERIFIED · CMA, July 2023", "chart"),
("P2-12", "That cost drivers about nine hundred million pounds in a single {year}.", "B14",
 "G number card £900M · EXTRA PAID BY DRIVERS IN 2022", "£900M IN ONE YEAR", "VERIFIED · CMA", "counter"),
("P2-13", "And it found the pattern again in 2023, for diesel. Prices passed on rises faster than {falls}.", "B14",
 "G card: CMA · ROCKETS & FEATHERS · DIESEL 2023", "CMA: IT HAPPENED AGAIN", "VERIFIED · CMA", "stamp thud"),
("P2-13b", "Diesel drivers, it said, paid about thirteen pence a litre more in early 2023 than they would have at normal {margins}.", "B14",
 "G number card +13p A LITRE · DIESEL, JAN-MAY 2023 (CMA)", "DIESEL 2023: +13p A LITRE", "VERIFIED · CMA", "counter"),
("P2-13c", "Its fix was two things. Force stations to publish their prices live, as open data. And set up a permanent fuel price {monitor}.", "B14",
 "G checklist: LIVE OPEN PRICE DATA · A PERMANENT FUEL MONITOR", "THE CMA'S FIX", "VERIFIED · CMA", "pen"),
("P2-14", "So when the RAC said this month that it fears history might be repeating itself, this is the history it {meant}.", "B09",
 "G quote card 'We fear history might be repeating itself' · RAC, 18 Nov 2026", "RAC: 'HISTORY REPEATING?'", "REPORTED · PetrolPrices.co.uk", "paper"),
("P2-15", "Running total. Line two. Up in four weeks. Down in {eight}.", "",
 "G receipt running total line 2: UP 4 WEEKS · DOWN 8 WEEKS", "UP 4 · DOWN 8", "", "printer"),
])

part("Part 3: Where the 10p is", "~8:30", [
("P3-01", "Part three. Where is your ten pence?", "", "G part card PART 3 · WHERE IS YOUR 10p?", "PART 3 · WHERE IS YOUR 10p?", "", "reverse cymbal + sub drop"),
("P3-02", "First, some of it is simply in the {ground}. Stations buy fuel ahead. The petrol you buy today may have been bought at October's price.", "B10",
 "G flow: OCTOBER PRICE → TANK UNDER THE FORECOURT → YOUR CAR TODAY", "TODAY'S FUEL, OCTOBER'S PRICE", "REPORTED · PetrolPrices.co.uk", "chain"),
("P3-03", "That's why the RAC says it normally takes about two weeks for a wholesale change to reach the pump. Two to four, on some {estimates}.", "B10",
 "G calendar: 2-4 WEEKS shaded", "NORMAL LAG: 2-4 WEEKS", "REPORTED · RAC; PetrolPrices.co.uk", "tick clock"),
("P3-04", "But oil started falling at the end of October. Four weeks later, the AA said some forecourts were still charging close to the peak prices of early {October}.", "B08",
 "G quote card 'Still charging close to the peak' · AA, 11 Nov 2026", "AA: 'CLOSE TO THE PEAK'", "REPORTED · AA", "paper"),
("P3-04b", "The AA also said another ten pence off should be on the way, if wholesale prices hold. That's the ten pence we're {chasing}.", "B08",
 "G price tag ANOTHER 10p · 'SHOULD BE ON THE WAY'", "AA: 10p ON THE WAY", "REPORTED · AA", "register ding"),
("P3-05", "Second, some of it is waiting. The watchdog describes stations that hold their prices until a rival cuts first. Nobody wants to start a price {war}.", "B14",
 "G two forecourt signs side by side; neither drops until one does; label WHO BLINKS FIRST?", "WHO CUTS FIRST?", "VERIFIED · CMA", "pen"),
("P3-05b", "And the AA has pointed at the supermarkets, which used to lead price cuts, for not competing hard enough this {time}.", "B30",
 "G card: SUPERMARKETS · NOT LEADING THE CUTS", "AA: SUPERMARKETS NOT LEADING", "REPORTED · AA via PetrolPrices.co.uk", "paper"),
("P3-06", "Third, it depends where you live. On the seventeenth of November, petrol in Northern Ireland was about one fifty-nine, more than five pence below the UK {average}.", "B16",
 "G UK map: Northern Ireland lit; tag 159.2p · -5p", "NORTHERN IRELAND: -5p", "REPORTED · RAC", "map whoosh"),
("P3-07", "That's about four pounds a tank. Same oil. Same wholesale price. The RAC says the gap deserves an {investigation}.", "B16",
 "G price tag -£4 A TANK; stamp 'DESERVES INVESTIGATION'", "SAME OIL · £4 CHEAPER", "REPORTED · RAC", "stamp thud"),
("P3-08", "And the gap between stations is even bigger. One live price tracker had the average at about one fifty-seven this week, and the cheapest station at one thirty-seven point {nine}.", "B15",
 "G bars: AVERAGE 157.1p · CHEAPEST 137.9p", "AVG 157.1p · CHEAPEST 137.9p", "REPORTED · PetrolPrices.co.uk sample, 27 Nov", "chart"),
("P3-09", "That's a nineteen pence difference. More than ten pounds on a single {tank}.", "B29",
 "G price tag 19p A LITRE = £10.50 A TANK", "£10.50 A TANK BETWEEN STATIONS", "ILLUSTRATION · our maths", "register ding"),
("P3-10", "So the honest answer to where your ten pence is: some is in the ground, some is in the margin, and some is at the station two miles away that cut first.", "B10 B14 B15",
 "G stacked: IN THE GROUND · IN THE MARGIN · AT ANOTHER STATION", "GROUND · MARGIN · ELSEWHERE", "ILLUSTRATION", "chart"),
("P3-11", "Running total. Line three. About ten pence a litre still {owed}.", "",
 "G receipt running total line 3: ≈ 10p A LITRE OWED", "≈ 10p OWED", "", "printer"),
])

part("Part 4: Why diesel is stuck", "~11:30", [
("P4-01", "Part four. Why diesel is stuck.", "", "G part card PART 4 · WHY DIESEL IS STUCK", "PART 4 · WHY DIESEL IS STUCK", "", "reverse cymbal + sub drop"),
("P4-02", "If you drive a diesel, you've noticed. It's barely moved. About two pounds at the peak. About one ninety-seven in {mid-November}.", "B04 B05",
 "G two price tags: DIESEL PEAK 200.20p · MID-NOV 196.77p", "DIESEL: 200p → 197p", "REPORTED · RAC; government weekly prices", "register ding"),
("P4-03", "That's not only the stations. Wholesale diesel has fallen only about four pence since mid-October, against fifteen for {petrol}.", "B06 B07",
 "G bars: WHOLESALE PETROL -15p · WHOLESALE DIESEL -4p", "WHOLESALE: -15p vs -4p", "REPORTED · AA", "chart"),
("P4-04", "The reason is a world shortage. Diesel comes from the middle of the barrel, and the Gulf is one of the world's big exporters of the refined {stuff}.", "B19",
 "G barrel cross-section: PETROL top · DIESEL middle highlighted · HEAVY bottom", "DIESEL: THE MIDDLE OF THE BARREL", "REPORTED · PetrolPrices.co.uk", "pop"),
("P4-05", "Britain imports a large share of the diesel it uses. So when the world is short, Britain pays the world {price}.", "B19",
 "G globe: arcs of diesel tankers into the UK; label UK IMPORTS A LARGE SHARE", "THE UK BUYS ABROAD", "REPORTED · PetrolPrices.co.uk", "map whoosh"),
("P4-05b", "So the RAC expects diesel to fall only to about one ninety. Even if every penny is passed on, diesel drivers get the smaller {share}.", "B09",
 "G price ladder down: DIESEL 197p → 190p", "DIESEL → ≈ 190p", "REPORTED · RAC", "register ding"),
("P4-06", "And diesel doesn't just fill vans. It moves food, parcels and building materials. Lorries, tractors, delivery {vans}.", "",
 "G chain: DIESEL → LORRIES → SHOPS → YOUR BASKET", "DIESEL MOVES EVERYTHING", "", "chain"),
("P4-07", "So when diesel sticks, prices in the shops stick with it. That's the bill you don't see at the {pump}.", "",
 "G card: THE BILL YOU DON'T SEE AT THE PUMP", "THE HIDDEN DIESEL BILL", "ILLUSTRATION", "stamp thud"),
("P4-08", "There's one more reason prices fall less than oil. The pound. Fuel is bought and sold in dollars, so if the pound is weak, the saving {shrinks}.", "B18",
 "G flow: OIL IN $ → POUND WEAKER → LESS SAVING IN £", "PRICED IN DOLLARS", "REPORTED · Visordown", "chain"),
("P4-09", "Running total. Line four. Diesel stuck near {two} pounds.", "",
 "G receipt running total line 4: DIESEL ≈ 197p", "DIESEL STUCK", "", "printer"),
])

part("Part 5: Your other bills", "~13:40", [
("P5-01", "Part five. Your other bills.", "", "G part card PART 5 · YOUR OTHER BILLS", "PART 5 · YOUR OTHER BILLS", "", "reverse cymbal + sub drop"),
("P5-02", "First, let's be fair to the stations. About half of every litre is tax that doesn't move with oil {at all}.", "B17 B28",
 "G stacked bar of a 165p litre: DUTY 52.95p · VAT 27.5p · FUEL + MARGIN ≈ 85p", "≈ HALF IS TAX", "ILLUSTRATION · our maths", "chart"),
("P5-03", "Fuel duty is fifty-two point nine five pence a litre, with the five pence cut now extended to July 2027. Then VAT at twenty percent goes on {top}.", "B17",
 "G number card 52.95p · FUEL DUTY · 5p CUT TO JULY 2027", "DUTY 52.95p + 20% VAT", "REPORTED · Budget, 28 Oct 2026", "counter"),
("P5-04", "That's why a quarter off the oil price can never mean a quarter off your petrol. But it should still mean about eighteen pence, not {eight}.", "B06 B27",
 "G two numbers: SHOULD FALL ≈ 18p · HAS FALLEN ≈ 8p", "SHOULD: 18p · DID: 8p", "ILLUSTRATION · our maths", "stamp thud"),
("P5-05", "Now the bill that's going the other way. Ofgem's energy price cap rises twenty-six percent on the first of {January}.", "B21",
 "G number card +26% · ENERGY CAP · 1 JAN 2027", "ENERGY CAP +26%", "REPORTED · Ofgem, 25 Nov 2026", "stamp thud"),
("P5-06", "From one thousand seven hundred and twenty-three pounds a year for a typical home, to two thousand one hundred and sixty-{six}.", "B21",
 "G bars: NOW £1,723 · JAN £2,166", "£1,723 → £2,166", "REPORTED · Ofgem", "chart"),
("P5-07", "That's four hundred and forty-three pounds more a year. The highest since 2023. Cornwall Insight blames high, jumpy gas prices, linked to the conflict in the Middle {East}.", "B21",
 "G price tag +£443 A YEAR; small line HIGHEST SINCE 2023", "+£443 A YEAR", "REPORTED · Cornwall Insight", "register ding"),
("P5-08", "Why is gas up when oil is down? Because before the war, Europe got about an eighth of its liquefied gas from Qatar, through {Hormuz}. And that trade hasn't recovered.", "B26",
 "G map: LNG route Qatar → Hormuz → Europe; label 12-14% OF EUROPE'S LNG", "QATAR'S GAS · HORMUZ", "REPORTED · Wikipedia", "map whoosh"),
("P5-08b", "And in Britain, gas usually sets the price of electricity too. So both halves of your energy bill move with {gas}, not oil.", "",
 "G chain: GAS PRICE → POWER PRICE → BOTH HALVES OF YOUR BILL", "GAS SETS THE POWER PRICE", "VERIFIED · how the GB power market prices", "chain"),
("P5-08c", "There is one small help in that figure. It already includes the cut in VAT on household electricity, which now runs to the end of June {2027}.", "B31",
 "G card: ELECTRICITY VAT CUT · TO 30 JUNE 2027 (ALREADY IN THE £2,166)", "VAT CUT ALREADY INCLUDED", "REPORTED · Cornwall Insight via IBTimes", "paper"),
("P5-09", "And the cap looks backwards. Ofgem sets it every three months from wholesale prices in an earlier window. So even if gas fell today, January's bill is already {locked}.", "B22",
 "G calendar: EARLIER WINDOW → CAP SET → JAN LOCKED · APR NEXT", "JANUARY IS LOCKED", "VERIFIED · Ofgem", "pen"),
("P5-10", "Put the two side by side. If you fill up twice a month and finally get your ten pence, that's about a hundred and thirty pounds a year. The energy cap takes four hundred and forty-{three}.", "B21 B27",
 "G two numbers: PETROL SAVED ≈ £130 A YEAR · ENERGY CAP +£443", "SAVE £130 · PAY £443 MORE", "ILLUSTRATION · our maths", "stamp thud"),
("P5-11", "So oil falling doesn't make your year cheaper. At best, it makes it less {expensive}.", "",
 "G card: OIL FELL. YOUR YEAR STILL COSTS MORE.", "STILL COSTS MORE", "", "paper"),
("P5-12", "Running total. Line five. Energy cap up twenty-six percent, {regardless}.", "",
 "G receipt running total line 5: ENERGY CAP +26%", "ENERGY +26%", "", "printer"),
])

part("Part 6: What you can do", "~16:30", [
("P6-01", "Part six. What happens next, and what you can do.", "", "G part card PART 6 · WHAT YOU CAN DO", "PART 6 · WHAT YOU CAN DO", "", "reverse cymbal + sub drop"),
("P6-02", "The good news first. The RAC says petrol should fall below one fifty a litre in the coming weeks, if the savings are passed on. Diesel, to about one {ninety}.", "B09",
 "G price ladder down: 167p → <150p (PETROL) · 197p → 190p (DIESEL)", "PETROL < 150p? · DIESEL ≈ 190p", "REPORTED · RAC, 18 Nov 2026", "register ding"),
("P6-03", "One campaign group has started a stopwatch. FairFuelUK is tracking prices at seven, fourteen, twenty-one and twenty-eight days after the fall. As its founder put it: oil has crashed, so the clock starts {now}.", "B20",
 "G four clocks: 7 · 14 · 21 · 28 DAYS; quote 'The clock starts now' · FairFuelUK", "THE CLOCK STARTS NOW", "REPORTED · Visordown", "tick clock"),
("P6-04", "The thing that could ruin it is the same thing that caused it. Iran. When Iran denied talks this month, oil jumped back above ninety-two within {hours}.", "B02",
 "G linechart: oil bounce on DENIAL; label ONE HEADLINE", "ONE HEADLINE CAN UNDO IT", "REPORTED · PetrolPrices.co.uk", "glitch"),
("P6-05", "And remember the rule. If oil goes back up, the rocket comes first. You'll see that at the pump within {weeks}.", "B11",
 "G rocket icon climbing fast; feather drifting down slowly", "THE ROCKET COMES FIRST", "VERIFIED · NBER", "whoosh"),
("P6-05b", "If that happens, the fourth video in this series is the one to watch. What happens if the blockade of Iran lasts a whole {year}?", "",
 "G card: NEXT · WHAT IF THE BLOCKADE LASTS A YEAR?", "NEXT: A YEAR OF BLOCKADE", "", "riser"),
("P6-06", "So what can you do? Check before you fill. The government's open fuel price data now shows station prices, and the gap this week was nineteen pence a {litre}.", "B14 B15",
 "G checklist: CHECK LIVE PRICES · DRIVE TO THE CHEAP ONE · DON'T FILL AT THE MOTORWAY", "CHECK BEFORE YOU FILL", "VERIFIED · CMA fuel finder remedy; REPORTED · PetrolPrices.co.uk", "pen"),
("P6-06b", "Avoid motorway services if you can. And if you drive diesel, the cheap stations matter even more, because the national average is falling so {slowly}.", "B15",
 "G two price tags: MOTORWAY · CHEAPEST NEARBY; label DIESEL: SHOP AROUND", "DIESEL: SHOP AROUND", "ILLUSTRATION", "register ding"),
("P6-07", "Every driver who fills up at the cheapest station is a push on the others to cut. Feathers fall faster when someone {blows}.", "",
 "G card: FEATHERS FALL FASTER WHEN SOMEONE BLOWS", "MAKE THE FEATHER FALL", "", "stamp thud"),
])

part("The Receipt", "~18:00", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. Oil, down a {quarter}.", "B01 B03", "G receipt line 1 prints", "OIL -25%", "", "printer"),
("RC-03", "Line two. Petrol, down about four {percent}.", "B04 B05", "G receipt line 2", "PETROL -4%", "", "printer"),
("RC-04", "Line three. About ten pence a litre still {owed}.", "B08 B27", "G receipt line 3", "≈ 10p A LITRE OWED", "", "printer"),
("RC-05", "Line four. Diesel stuck near two {pounds}.", "B05 B07", "G receipt line 4", "DIESEL ≈ 197p", "", "printer"),
("RC-06", "Line five. Energy bills up a quarter in {January}.", "B21", "G receipt line 5", "ENERGY CAP +26%", "", "printer"),
("RC-07", "Prices go up like rockets and come down like feathers. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp STILL WAITING; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: next video tile WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-020 Iran War: Oil Fell. Why Didn't Your Bill?: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/125:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not financial advice.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-020-oil-fell/INV-020-oil-fell-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
