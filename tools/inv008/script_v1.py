# INV-008 The 1973 Invoice: script v1 source. Run: python3 script_v1.py -> md in videos/INV-008-1973-invoice/
# Each row: (code, narration, facts, visual, on_screen, tag_source, sfx)
import os, re
VID = "INV-008"
PARTS = []

def part(title, start, rows):
    PARTS.append((title, start, rows))

part("Cold open", "0:00", [
("CO-01", "Oregon, the winter of 1973. A green flag hangs on a petrol pump. Green means you can buy fuel. Yellow means rationed. Red means there's nothing left.", "F21",
 "ARCHIVE-PD still (NARA DOCUMERICA, Oregon station / queue), slow push; flag tinted green → yellow → red.", "OREGON · WINTER 1973", "VERIFIED · Wikipedia; PDX Monthly", "low drone in, three soft ticks on the colours"),
("CO-02", "This was the 1973 oil crisis. In a few months, the price of a barrel of oil went up about four times. By February 1974, one American petrol station in five had nothing to sell.", "F07 F22",
 "CARD-NUMBER $2.90 → $11.65 counter; then 5 pump icons, 1 goes dark.", "1973 OIL CRISIS · $2.90 → $11.65 · 1 IN 5 STATIONS DRY", "VERIFIED · Fed. Reserve History / REPORTED", "counter, sub hit on 11.65"),
("CO-03", "Here's the strange part. In the 1973 oil crisis, the world lost about four and a half million barrels a day. In 2026, it lost more than fourteen million. Three times as much. And the queues never came.", "F11 F61 H8",
 "Two bars grow side by side: 4.5 (1973) vs 14+ (2026); 2026 bar in orange.", "4.5M vs 14M+ BARRELS A DAY LOST", "REPORTED · Majalla citing IEA, Sep 2026", "chart grow, silence after 'never came'"),
("CO-04", "But the bill did. A gallon of petrol in America costs about a dollar more than it did a year ago. In 1974, it rose forty-three percent in thirteen months.", "F65 F14",
 "CARD-NUMBER +$1 / GALLON (2026) under +43% (1974); 2 s flash of the final RECEIPT with two columns.", "+43% IN 13 MONTHS (1974) · +$1 A GALLON (2026)", "VERIFIED · AAA, Nov 2026 / REPORTED", "receipt printer"),
("CO-05", "Some of these numbers are old government records. Some are reporting from this year that can still change. We'll tell you which is which, every time.", "",
 "Tag cards fan out: VERIFIED · REPORTED · ESTIMATE.", "WHAT'S CONFIRMED · WHAT'S REPORTED", "", "tick"),
("CO-06", "By the end, you'll see the full invoice from 1973, line by line, next to ours. We'll start with the week it began, stand in the queue, sit in the dark in Britain, follow the long bill, see what the world fixed, and come back to your table.", "",
 "Roadmap: six icons light in a row (calendar, pump, candle, chart, shield, table).", "THE WEEK · THE QUEUE · THE DARK · THE LONG BILL · THE FIX · YOUR TABLE", "", "riser"),
])

part("Part 1: The week it started", "~1:30", [
("P1-01", "Part one. The week it started.", "", "s_part PART 1 · THE WEEK IT STARTED", "PART 1 · THE WEEK IT STARTED", "", "reverse cymbal + sub drop"),
("P1-02", "In August 1973, Saudi Arabia's King Faisal and Egypt's President Sadat met in Riyadh. They agreed that oil could be used as a weapon.", "F01",
 "MAP-3D: Riyadh glows orange, a line to Cairo.", "RIYADH · AUG 1973 · 'THE OIL WEAPON'", "REPORTED · Wikipedia", "whoosh-deep"),
("P1-03", "On the sixth of October, war broke out between Israel, Egypt and Syria. Within a week, the United States began flying weapons to Israel.", "F02",
 "Timeline card: 6 OCT war · ~12-14 OCT US airlift; map arrows only, no combat footage.", "6 OCT 1973 · WAR", "VERIFIED · Office of the Historian", "low pulse"),
("P1-04", "Then came the oil. On the sixteenth of October, Gulf producers raised their price by about seventy percent, in one day.", "F03",
 "CARD-NUMBER: +70% stamped over a 1973 price board.", "+70% IN ONE DAY", "REPORTED · Wikipedia (verify)", "sub hit"),
("P1-05", "On the seventeenth, Arab producers cut output by five percent. And they said they would cut five percent more, every month, until their demands were met.", "F04",
 "Clock graphic: a barrel shrinks 5% per tick.", "-5% · EVERY MONTH", "VERIFIED · OAPEC, 17 Oct 1973", "clock tick"),
("P1-06", "Two days later, President Nixon asked Congress for two point two billion dollars in emergency aid for Israel. Libya announced an embargo on the United States that same day. Saudi Arabia followed the next.", "F05",
 "CARD-HEADLINE style timeline: 19 OCT $2.2bn aid · LIBYA EMBARGO · 20 OCT SAUDI.", "19-20 OCT 1973 · EMBARGO", "VERIFIED · Fed. Reserve History", "card land x3"),
("P1-07", "The embargo hit the US and the Netherlands first. Later Portugal, Rhodesia and South Africa were added. No oil from Arab producers was to reach them.", "F06",
 "World map: US and Netherlands turn red, then three more.", "EMBARGOED", "VERIFIED · Office of the Historian", "whoosh"),
("P1-08", "Why did it bite so hard? Because there was almost no slack. Before the embargo, the world had about one percent of spare production. America's own oil fields were already pumping flat out.", "F08 F09",
 "Gauge graphic: spare capacity needle at 1%.", "SPARE CAPACITY ≈ 1%", "REPORTED · Majalla / VERIFIED · Fed (Burns)", "tick"),
("P1-09", "So the price did what prices do when there is no slack. A barrel cost about two dollars ninety before the embargo. By January 1974, it cost eleven sixty-five. Four times as much.", "F07",
 "Line chart: $2.90 → $11.65, Oct 73-Jan 74.", "$2.90 → $11.65 · ×4", "VERIFIED · Fed. Reserve History", "chart grow + sub"),
("P1-10", "In today's money, that's roughly twenty-two dollars a barrel, rising to about eighty. Keep that eighty in mind. We'll come back to it.", "H6",
 "CARD-NUMBER: $22 → $80 (2026 dollars), faded original numbers behind.", "≈$22 → ≈$80 IN 2026 DOLLARS", "ESTIMATE · our maths, BLS CPI", "soft hit"),
("P1-11", "At the pump, the jump was slower but it was real. In May 1973, an American gallon of petrol cost thirty-eight and a half cents. By June 1974, fifty-five cents. Forty-three percent in thirteen months.", "F14",
 "STOCK/ARCHIVE: old pump dial rolling; CARD 38.5¢ → 55.1¢.", "38.5¢ → 55.1¢ · +43%", "REPORTED · contemporary data (verify EIA)", "counter"),
("P1-12", "Take a family that bought sixty gallons a month. That's an example, not an average. They paid about ten dollars more a month. In today's money, about sixty-eight dollars. Every month, for fuel alone.", "H3",
 "RECEIPT corner line 1 prints: FUEL +$68/MONTH (2026 $). Label ILLUSTRATION.", "EXAMPLE FAMILY · +$68 A MONTH", "ILLUSTRATION · our maths", "receipt print"),
("P1-13", "But money wasn't the first thing people lost. The first thing was time. So where did the time go?", "",
 "Clock hand sweeping over a queue of car silhouettes.", "", "", "riser"),
])

part("Subscribe bridge", "~4:05", [
("BR-01", "If you want to see how today's crises reach your bill, that's what this channel does, every video. Subscribe, and next we'll follow the war to your dinner plate.", "",
 "Simple card, subscribe button animation; next-video teaser frame (The Hunger Bill).", "NEXT: THE HUNGER BILL", "", "soft whoosh"),
])

part("Part 2: The queue", "~4:20", [
("P2-01", "Part two. The queue.", "", "s_part PART 2 · THE QUEUE", "PART 2 · THE QUEUE", "", "reverse cymbal + sub drop"),
("P2-02", "On the seventh of November 1973, the White House announced Project Independence. The goal was for America to need no foreign oil. That was the plan for later. The problem was the winter.", "F15",
 "CARD-HEADLINE: PROJECT INDEPENDENCE · 7 NOV 1973.", "PROJECT INDEPENDENCE", "VERIFIED · Office of the Historian", "card land"),
("P2-03", "On the twenty-fifth of November, Nixon went on television. He warned that the shortage could reach seventeen percent.", "F18",
 "CARD-QUOTE: 'could run as high as 17 percent' · Nixon · 25 Nov 1973. No image of Nixon's face.", "SHORTAGE UP TO 17%", "VERIFIED · UCSB Presidency Project", "tick"),
("P2-04", "He asked stations to close from nine on Saturday night to midnight on Sunday. He asked homes to turn the heating down to sixty-eight degrees. Home heating oil would be cut by fifteen percent.", "F16 F17 F19",
 "Three focus cards: CLOSED SAT 9PM-SUN · 68°F · HEATING OIL -15%.", "CLOSED SUNDAYS · 68°F · -15% HEATING OIL", "VERIFIED · UCSB, 25 Nov 1973", "tick x3"),
("P2-05", "About nine in ten station owners went along with the weekend closing. So everyone tried to fill up on the other days, at the same time.", "F20",
 "STOCK/ARCHIVE: line of 1970s cars at a station (NARA).", "90% COMPLIED", "REPORTED · Wikipedia", "room tone, engine idle"),
("P2-06", "Some states turned to odd and even days. If your licence plate ended in an odd number, you bought fuel on odd dates. Even numbers, even dates.", "F21",
 "Plate graphic: last digit flips 3 → 4, calendar highlights odd/even.", "ODD PLATES · ODD DAYS", "VERIFIED · Wikipedia", "flip"),
("P2-07", "In the last week of February 1974, one station in five across the country had no fuel at all. People left home before dawn to queue. Some brought something to read.", "F22",
 "ARCHIVE-PD still: queue at dawn, slow pan. Five pump icons, one dark.", "1 IN 5 STATIONS · NO FUEL · FEB 1974", "REPORTED · Wikipedia (verify)", "slow tick"),
("P2-08", "The speed limit came down. Nixon first asked for fifty miles an hour. Congress made it fifty-five, nationwide. That limit would stay for more than twenty years.", "F25 F24",
 "Road-sign graphic: 70 → 50 → 55; '1974 → 1995'.", "55 MPH · 1974-1995", "VERIFIED · UCSB; Office of the Historian", "whoosh"),
("P2-09", "In January 1974, the clocks went forward for the whole year. Daylight saving in winter. Children walked to school in the dark, to save power in the evening.", "F26",
 "STOCK: dark morning street, streetlights on; clock hand jumps forward.", "YEAR-ROUND DAYLIGHT SAVING · JAN 1974", "VERIFIED · Wikipedia", "clock tick"),
("P2-10", "And people did drive less. American road fuel use fell nearly four percent in a year. That doesn't sound like much. It was enough to change how a country lived.", "F28",
 "Bar pair 110.4 → 106.3 billion gallons.", "-3.7% FUEL USED · 1973 → 1974", "VERIFIED · FHWA", "chart grow"),
("P2-11", "Part of the reason was the cars. In 1973, the average American vehicle did about twelve miles to the gallon. Every queue was full of cars that drank fuel fast.", "F27",
 "STOCK/ARCHIVE: big 1970s sedan at the pump; CARD 11.9 MPG.", "11.9 MPG · 1973", "VERIFIED · FHWA", "soft hit"),
("P2-12", "On the invoice, line two isn't money. It's hours in a queue, a colder house and darker mornings. America was angry. But Britain had it worse. Why?", "",
 "RECEIPT corner line 2 prints: TIME · QUEUES · 68°F.", "LINE 2 · TIME", "", "receipt print + riser"),
])

part("Part 3: The dark", "~6:45", [
("P3-01", "Part three. The dark.", "", "s_part PART 3 · THE DARK", "PART 3 · THE DARK", "", "reverse cymbal + sub drop"),
("P3-02", "Britain wasn't on the embargo list. But in 1973, oil supplied almost half of the country's energy. And at the same time, its coal miners were in a pay dispute.", "F38 F31",
 "MAP-3D: UK in orange; two icons, oil drop + coal lump, meet.", "OIL ≈ 46% OF UK ENERGY", "REPORTED · RAC Foundation", "whoosh-deep"),
("P3-03", "In November, the government asked drivers to keep to fifty miles an hour, and to stay off the roads at weekends. By December, the fifty limit was law.", "F35",
 "Road sign 50 on a wet British road (STOCK).", "50 MPH · DEC 1973", "VERIFIED · RAC Foundation", "tick"),
("P3-04", "On the twenty-ninth of November, petrol ration books were handed out to every motorist in the country. They were never used. In July 1975, people were told they could throw them away.", "F34",
 "STILL: ration-book style card (recreated, no real crest), slow push; stamp NEVER USED.", "RATION BOOKS · 29 NOV 1973 · NEVER USED", "VERIFIED · RAC Foundation; Hansard", "paper rustle, stamp"),
("P3-05", "Then, on the thirteenth of December, Prime Minister Edward Heath announced the three-day week. From the first of January 1974, businesses could use electricity on just three days a week.", "F29",
 "Calendar graphic: 7 days, 4 go dark. CARD 'THREE-DAY WEEK'.", "THREE-DAY WEEK · 1 JAN 1974", "VERIFIED · Wikipedia", "light switch off x4"),
("P3-06", "Television had to stop at half past ten every night. The government told families to heat only one room. Shops worked by candlelight and paraffin lamps.", "F30 F33",
 "STOCK: candle on a kitchen table; TV screen fading to a dot at 22:30.", "TV OFF AT 10:30 PM · HEAT ONE ROOM", "VERIFIED / REPORTED", "TV power-down, candle"),
("P3-07", "And the price at the pump doubled. In mid-1973, a gallon of British petrol cost thirty-six pence. By the end of 1974, seventy-two.", "F36",
 "CARD-NUMBER: 36p → 72p, ×2.", "36p → 72p A GALLON · ×2", "VERIFIED · RAC Foundation", "counter + sub"),
("P3-08", "In January, the miners voted to strike. Eighty-one percent said yes. Heath called an election and asked, in effect, who runs the country.", "F31 F32",
 "Ballot graphic 81% YES.", "81% VOTED TO STRIKE · JAN 1974", "VERIFIED · Wikipedia", "tick"),
("P3-09", "He lost his majority. Harold Wilson formed a minority government. The three-day week ended in March. The oil shock and the coal strike had brought down a government in under four months.", "F32 F29",
 "Parliament silhouette; seat bar flips from blue majority to hung. No faces.", "FEB 1974 · HUNG PARLIAMENT", "VERIFIED · Wikipedia", "low hit"),
("P3-10", "Across the sea, the Netherlands was on the embargo list. From the fourth of November 1973, Sundays were car-free. People skated and rode horses on empty motorways.", "F39 F06",
 "STOCK/ARCHIVE: empty motorway, cyclists; map NL in red.", "CAR-FREE SUNDAYS · 4 NOV 1973", "VERIFIED · Jalopnik; Wikipedia", "wind, bicycle bell"),
("P3-11", "Several other European countries banned driving, flying or boating on Sundays too.", "F40",
 "Map: several countries tick on with a SUNDAY icon.", "SUNDAY BANS ACROSS EUROPE", "REPORTED · Wikipedia", "tick x4"),
("P3-12", "Japan got about nine tenths of its oil from the Middle East. When its trade minister asked people to save paper, a rumour spread that toilet paper was running out. People rushed the shops, and the rumour made itself true.", "F41 F42",
 "MAP: Japan glowing; STOCK: empty supermarket paper shelf.", "JAPAN · 90% FROM THE MIDDLE EAST", "REPORTED · Wikipedia; Asahi via Asia Economy", "crowd murmur low"),
("P3-13", "Line three on the invoice: power. Lights, heat, and in Britain, a government. But the queues and the candles ended in a few months. The bill didn't. What came after?", "",
 "RECEIPT corner line 3 prints: POWER · 3-DAY WEEK · PETROL ×2.", "LINE 3 · POWER", "", "receipt print + riser"),
])

part("Part 4: The long bill", "~9:20", [
("P4-01", "Part four. The long bill.", "", "s_part PART 4 · THE LONG BILL", "PART 4 · THE LONG BILL", "", "reverse cymbal + sub drop"),
("P4-02", "The embargo ended in March 1974. The price didn't go back. Oil stayed at the new level, and by November 1974 it was around fifteen dollars a barrel.", "F12 F37",
 "Line chart continues past MAR 1974 flat-high to $15.", "EMBARGO ENDS · PRICE STAYS", "VERIFIED / REPORTED · RAC Foundation", "chart grow"),
("P4-03", "Oil goes into almost everything. Fuel for the lorry that brings the food. Plastic for the packet. Heat for the factory. So the price moved through every shelf.", "",
 "Chain graphic: barrel → lorry → packet → factory → shelf.", "OIL IS IN EVERYTHING", "", "whoosh x4"),
("P4-04", "In America, prices rose about six percent in 1973. In 1974, eleven percent.", "F44",
 "Bar chart US CPI: 6.2% → 11.0%.", "US INFLATION · 6.2% → 11.0%", "VERIFIED · BLS", "chart grow + sub"),
("P4-05", "For a family spending three thousand dollars a month, that means the same shopping costs about three hundred and thirty dollars more a month, a year later. That's an example, not an average.", "H5",
 "RECEIPT corner line 4 prints: PRICES +$330/MONTH (on $3,000). ILLUSTRATION.", "EXAMPLE · +$330 A MONTH", "ILLUSTRATION · our maths, BLS", "receipt print"),
("P4-06", "In Britain it was worse. In the twelve months to June 1975, prices rose twenty-six percent. Something that cost a pound now cost a pound and twenty-six pence.", "F48",
 "CARD-NUMBER 26.1%; coin graphic £1.00 → £1.26.", "UK PRICES +26.1% · TO JUNE 1975", "VERIFIED · Hansard, 7 Aug 1975", "sub hit"),
("P4-07", "Then the jobs went. America was in recession from November 1973 to March 1975. About two point three million jobs were lost.", "F45 F46",
 "Timeline bar NOV 73 → MAR 75; job icons fall away.", "RECESSION · NOV 1973-MAR 1975 · 2.3M JOBS", "VERIFIED · NBER / REPORTED · BLS", "low pulse"),
("P4-08", "Unemployment kept rising even after the recession ended. It peaked at nine percent in May 1975. It didn't fall below six percent again until June 1978.", "F47",
 "Line chart unemployment → 9% peak, slow fall.", "9% · MAY 1975", "VERIFIED · BLS", "chart grow"),
("P4-09", "In Britain, the economy shrank by around four percent and took three and a half years to recover.", "F49",
 "Bar: UK GDP -3.9%; '14 QUARTERS'.", "UK GDP ≈ -3.9% · 14 QUARTERS", "REPORTED · Wikipedia", "tick"),
("P4-10", "Here's the honest part. Oil didn't start this fire on its own. In mid-1973, before the embargo, American factory prices were already rising more than ten percent a year. Economists still argue how much of the 1970s was oil.", "F50",
 "CARD-QUOTE style note: 'already rising above 10%' · Fed. Reserve History (Burns, 1974).", "PRICES WERE ALREADY RISING", "VERIFIED · Fed. Reserve History", "silence beat"),
("P4-11", "What oil did was pour fuel on it. And it showed every government the same thing. A country that can't do without oil can be squeezed by whoever controls it.", "",
 "MAP: Gulf glowing, lines out to US, Europe, Japan tighten.", "", "", "low drone"),
("P4-12", "Here is the invoice so far. Fuel, about sixty-eight dollars a month in today's money for our example family. Hours in queues. Power cuts and a fallen government. Prices up eleven percent in America and twenty-six in Britain. Millions of jobs.", "H3 F44 F48 F46",
 "HALF-RECEIPT: four lines + running total, prints and holds.", "THE INVOICE SO FAR", "ILLUSTRATION / VERIFIED", "receipt print, pause"),
("P4-13", "So what did the world do, so that it would never get a bill like this again? And did it work?", "",
 "Shield icon outline draws in.", "", "", "riser"),
])

part("Part 5: The fix", "~11:50", [
("P5-01", "Part five. The fix.", "", "s_part PART 5 · THE FIX", "PART 5 · THE FIX", "", "reverse cymbal + sub drop"),
("P5-02", "In 1974, the big oil-buying countries set up the International Energy Agency. Each member had to keep oil in storage equal to at least ninety days of its imports.", "F53",
 "Tank graphic fills to '90 DAYS'.", "IEA · 1974 · 90 DAYS OF STOCKS", "VERIFIED · IEA", "fill sound"),
("P5-03", "In 1975, America created its Strategic Petroleum Reserve, a stock of oil in underground salt caverns. The same law set the first fuel economy rules for cars.", "F56",
 "Cross-section graphic: salt cavern filling; CARD 'SPR · CAFE · 1975'.", "STRATEGIC PETROLEUM RESERVE · 1975", "VERIFIED · Office of the Historian", "low rumble"),
("P5-04", "And slowly, the world learned to do more with less. In 1973, it took a little under one barrel of oil to make a thousand dollars of world output. By 2019, it took less than half a barrel.", "F58",
 "Barrel graphic shrinks to 0.43; line chart 1973 → 2019.", "-56% OIL PER $1,000 OF GDP", "VERIFIED · Columbia CGEP, 2021", "chart grow"),
("P5-05", "The biggest change was in America itself. After 1973, it imported more and more. In 1977, OPEC supplied seventy percent of its oil imports. Then shale changed everything. In 2020, America sold more oil products abroad than it bought, for the first time since at least 1949.", "F60 F59",
 "Flow arrows reverse direction on a US map; CARD 'NET EXPORTER · 2020'.", "NET EXPORTER · 2020", "VERIFIED · EIA", "whoosh reverse"),
("P5-06", "So the 1973 oil crisis left the world a toolkit. Storage, efficiency, and new supply. The emergency stocks have been used together six times. The sixth, in March 2026, was the largest.", "F54",
 "Ladder card: 1991 · 2005 · 2011 · 2022 · 2022 · 2026 (largest, orange).", "6 EMERGENCY RELEASES · 2026 THE LARGEST", "VERIFIED · IEA", "tick x6"),
("P5-07", "Which brings us to the question in the title. 2026 took three times more oil off the market than 1973. So why does our bill look so different? And is it really smaller?", "F61",
 "Back to the CO-03 bars, now with a question mark.", "1973 vs 2026", "", "riser"),
])

part("Part 6: 1973 vs 2026", "~13:25", [
("P6-01", "Part six. 1973 against 2026.", "", "s_part PART 6 · 1973 vs 2026", "PART 6 · 1973 vs 2026", "", "reverse cymbal + sub drop"),
("P6-02", "In 2026, losses of oil from the Gulf peaked above fourteen million barrels a day. Brent crude went from about seventy-two dollars before the war to a peak above a hundred and twenty-six. A rise of about seventy-four percent.", "F61 F62",
 "Line chart Brent 2026: $72.48 → $126+.", "$72 → $126 · +74%", "REPORTED · Majalla (IEA), Sep 2026", "chart grow"),
("P6-03", "In 1973, a much smaller loss quadrupled the price. That's the first difference. The world uses less than half as much oil for each dollar it earns, and it had stocks ready. The IEA released four hundred million barrels in March.", "F58 F55",
 "Split screen 1973 ×4 / 2026 +74%; tank icon releasing 400M.", "×4 vs +74% · 400M BARRELS RELEASED", "VERIFIED / REPORTED", "tick"),
("P6-04", "But remember that eighty dollars? The 1974 peak, in today's money. On the tenth of November 2026, even after falling on hopes of a deal, Brent was about eighty-nine. By our maths, oil now costs a little more, in real terms, than at the height of the 1973 oil crisis.", "H6 F63",
 "CARD: $80 (1974, in 2026 $) vs $89 (10 NOV 2026); 2026 bar slightly taller.", "1974 PEAK ≈ $80 · NOV 2026 ≈ $89", "ESTIMATE · our maths / REPORTED · Trading Economics", "sub hit, silence"),
("P6-05", "We just don't queue for it. In 1973, the price was held down by rules, so the fuel ran out. In 2026, the price is allowed to rise, so the fuel is there. We pay at the till, instead of in the queue.", "",
 "Two scenes: queue (1973) vs price board ticking up (2026).", "1973 PAID IN TIME · 2026 PAID IN PRICE", "", "tick"),
("P6-06", "So how big is our bill? American petrol was about four dollars a gallon on the ninth of November 2026. At Thanksgiving last year, it was about three dollars and six cents.", "F65",
 "CARD-NUMBER $3.06 → $4.01.", "$3.06 → $4.01 A GALLON", "VERIFIED · AAA, Nov 2026", "counter"),
("P6-07", "Our same example family, buying sixty gallons a month, pays about fifty-seven dollars more a month. In 1974, in today's money, it was about sixty-eight. Close. Not the same, but close.", "H4 H3",
 "Two receipt columns: 1974 $68 · 2026 $57.", "FUEL · 1974 ≈ $68 · 2026 ≈ $57", "ILLUSTRATION · our maths", "receipt print"),
("P6-08", "And a 1974 gallon, in today's money, cost about three dollars seventy-seven. The gallon you buy now costs more than that.", "H2 F65",
 "CARD: $3.77 (1974 in 2026 $) vs $4.01.", "1974 ≈ $3.77 · NOV 2026 $4.01", "ESTIMATE · our maths, BLS CPI", "soft hit"),
("P6-09", "Prices overall are a different story. In the year to September 2026, US prices rose three point seven percent, and petrol rose thirty-four percent. In 1974, prices overall rose eleven percent. Our oil bill is similar. Our price rise is much smaller, so far.", "F64 F44",
 "Bar pair 11.0% (1974) vs 3.7% (SEP 2026); petrol +34.2% bar in orange.", "INFLATION · 11.0% vs 3.7%", "VERIFIED · BLS", "chart grow"),
("P6-10", "For our three-thousand-dollar family, that's about a hundred and eleven dollars more a month, against three hundred and thirty in 1974.", "H5",
 "Receipt columns: PRICES 1974 +$330 · 2026 +$111.", "PRICES · +$330 vs +$111", "ILLUSTRATION · our maths", "receipt print"),
("P6-11", "Now the worry. America's emergency reserve fell in 2026 to about two hundred and eighty-five million barrels, its lowest since 1982. The cushion that saved us this time is thinner for the next one.", "F57",
 "Cavern graphic draining; CARD 284.6M · LOWEST SINCE 1982.", "SPR · 284.6M BARRELS · LOWEST SINCE 1982", "REPORTED · Majalla, Sep 2026", "low drone"),
("P6-12", "And 1973 had a sequel. Six years later, in 1979, a second shock pushed oil even higher. The World Bank's bad case for 2026 has world growth falling to one point three percent.", "F52 F66",
 "Timeline 1973 → 1979 (second spike); CARD 1.3% ADVERSE.", "1979: THE SEQUEL", "REPORTED · Wikipedia; World Bank", "riser low"),
("P6-13", "In March 2026, the toilet paper rumour came back in Japan. The paper makers had to tell people that supply was normal. Fifty-three years later, people still remember the queue.", "F43",
 "STOCK: full supermarket shelf; CARD 'SUPPLY NORMAL · MAR 2026'.", "THE RUMOUR CAME BACK · MAR 2026", "REPORTED · Asahi via Asia Economy", "soft"),
("P6-14", "So what does the full invoice look like, then and now?", "", "Receipt printer starts.", "", "", "riser"),
])

part("The Receipt", "~16:45", [
("RC-01", "The Receipt. Two columns. 1974 on the left, in today's money. 2026 on the right. Our example family. These are illustrations, not averages.", "",
 "RECEIPT with two columns prints in.", "THE RECEIPT · 1974 vs 2026", "ILLUSTRATION", "receipt printer"),
("RC-02", "Line one. Fuel. About sixty-eight dollars more a month in 1974. About fifty-seven in 2026.", "H3 H4",
 "RECEIPT line 1.", "FUEL · $68 · $57", "ILLUSTRATION", "receipt print"),
("RC-03", "Line two. Prices. About three hundred and thirty dollars more a month in 1974. About a hundred and eleven in 2026, so far.", "H5",
 "RECEIPT line 2.", "PRICES · $330 · $111", "ILLUSTRATION", "receipt print"),
("RC-04", "Line three. Time. In 1974, hours in queues. In 2026, none, because we pay in price instead.", "",
 "RECEIPT line 3.", "TIME · HOURS · NONE", "", "receipt print"),
("RC-05", "Line four. Jobs. Two point three million in America in the 1970s. In 2026, not counted yet.", "F46",
 "RECEIPT line 4; 2026 cell reads 'NOT YET'.", "JOBS · 2.3M · NOT YET", "REPORTED · BLS", "receipt print"),
("RC-06", "Line five. The cushion. In 1973, no emergency stocks. In 2026, stocks, but the American reserve at its lowest since 1982.", "F53 F57",
 "RECEIPT line 5.", "CUSHION · NONE · THIN", "VERIFIED / REPORTED", "receipt print + stamp"),
("RC-07", "What can you do? This is not financial advice. But some things are always sensible. Keep a buffer of three to six months of essential bills. Test your budget with fuel and food twenty percent higher.", "",
 "Focus cards: BUFFER 3-6 MONTHS · +20% STRESS TEST.", "NOT FINANCIAL ADVICE", "", "tick x2"),
("RC-08", "If your next car or boiler is due, look at what it burns. The 1970s family with the twelve-mile-a-gallon car paid the most. And don't trade on headlines. Oil falls fast on talk of a deal, and it can rise just as fast.", "F27 F63",
 "Focus cards: WHAT DOES IT BURN? · DON'T TRADE HEADLINES.", "", "", "tick x2"),
("RC-09", "Tell us in the comments. Do you remember 1973, or do your parents? Or what did your last fill-up cost? Country and number.", "",
 "Comment prompt card; end screen to The Hunger Bill.", "DO YOU REMEMBER 1973?", "", "riser air"),
("RC-10", "In Oregon, the flags came down in the spring of 1974. The price never did. Every crisis sends a bill. History keeps the receipts.", "F21 F12",
 "Return to CO-01 pump still, flag gone; slow fade to black; tagline.", "EVERY CRISIS SENDS A BILL. HISTORY KEEPS THE RECEIPTS.", "", "silence, then one low note"),
])

def words(t): return len(re.findall(r"[A-Za-z0-9'’.\-]+", t))

def build():
    out = []
    total = sum(words(r[1]) for _, _, rows in PARTS for r in rows)
    out.append(f"# {VID} The 1973 Invoice: script v1\n")
    out.append(f"v1, 2026-11-10. Search phrase: **1973 oil crisis** (spoken at ~0:10 in CO-02, and in P5-06, P6-04). Lead title: **1973 Oil Crisis: What It Cost Your Family, Then and Now** (55 chars).\n")
    out.append(f"Narration: **{total} words, about {total/132:.0f} minutes** of voice at 132 wpm; with part cards and pauses the cut runs about {total/132+1.5:.0f}-{total/132+2.5:.0f} min. Every number points to a row in `facts.md` (F = fact, H = household maths). Example-family figures are labelled ILLUSTRATION on screen.\n")
    for title, start, rows in PARTS:
        out.append(f"\n## {title} (starts {start})\n")
        out.append("| Code | Narration | Words | Facts | Visual | On-screen text | Tag + source | SFX |")
        out.append("|---|---|---|---|---|---|---|---|")
        for c, n, f, v, o, t, s in rows:
            out.append(f"| {VID} · {c} | {n} | {words(n)} | {f} | {v} | {o} | {t} | {s} |")
    return "\n".join(out), total

if __name__ == "__main__":
    md, total = build()
    extra = open(os.path.join(os.path.dirname(__file__), "script_v1_extras.md")).read()
    dst = "/mnt/project-files/the-history-invoice/videos/INV-008-1973-invoice/INV-008-1973-invoice-script-v1.md"
    open(dst, "w").write(md + "\n\n" + extra)
    print(total)
