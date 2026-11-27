# INV-024 What If the Iran War Spreads to the Gulf? Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Iran follow-up series #7.
import os
VID = "INV-024"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "QESHM · BAHRAIN · KUWAIT", "P2": "KUWAIT: 90% WATER = DESAL", "P3": "QATAR = 1/5 OF WORLD LNG",
          "P4": "DUBAI PASSENGERS -31%", "P5": "+6p/L PER $10", "P6": "WATCH: RAS LAFFAN"}

part("Cold open", "0:00", [
("CO-01", "This month, the Iran war started reaching across the water again. Drones over Bahrain. Drones over Kuwait. And an American strike on an Iranian {island}.", "G02 G03 G05",
 "G map: Gulf with Bahrain, Kuwait, Qeshm pins", "THE WAR REACHES THE GULF", "REPORTED · Al Jazeera", "sub hit"),
("CO-02", "Iran's army chief says the next response will know no geographical {boundaries}.", "G07",
 "G quote card", "'NO GEOGRAPHICAL BOUNDARIES'", "REPORTED · Fars via AFP", "stamp thud"),
("CO-03", "The Gulf isn't just oil. It's a fifth of the world's liquefied gas, the world's busiest international airport, and cities that drink the {sea}.", "G28 G37 G18",
 "G three stats: 1/5 OF WORLD LNG · 95M PASSENGERS · 90% WATER FROM THE SEA", "OIL, GAS, FLIGHTS, WATER", "REPORTED", "riser"),
("CO-04", "So what happens if the war spreads to the Gulf states themselves? The short answer: your petrol, your heating and your holiday all get dearer. In the worst case, about twenty-two pence more on a litre, and ninety cents more on a {gallon}.", "G47",
 "G two price tags: +22p A LITRE · +90¢ A GALLON", "WORST CASE: +22p · +90¢", "ILLUSTRATION · our maths if Brent returns to $126", "register ding"),
("CO-05", "We'll look at what happened this month, why the Gulf is a glass house, the gas, the flights, your bill, and what to watch. Let's open the {invoice}.", "",
 "G roadmap: THIS MONTH · GLASS HOUSE · THE GAS · THE FLIGHTS · YOUR BILL · WHAT TO WATCH", "THE GULF INVOICE", "", "riser"),
])

part("Part 1: What happened this month", "~1:00", [
("P1-01", "Part one. What happened this {month}.", "", "G part card PART 1 · THIS MONTH", "PART 1 · THIS MONTH", "", "reverse cymbal"),
("P1-02", "Some background first. The war began on the twenty-eighth of February, when the United States and Israel attacked Iran. Iran answered by firing at its {neighbours}.", "G01",
 "G timeline: 28 FEB 2026 WAR BEGINS", "28 FEB: THE WAR", "REPORTED · AP", "whoosh"),
("P1-03", "In the first week alone, Iran's Revolutionary Guard said it fired two hundred and thirty drones at bases hosting American troops, including in {Kuwait}.", "G13",
 "G dots: 230", "230 DRONES IN ONE DAY", "CLAIM · IRGC via Al Jazeera", "tick"),
("P1-04", "An eleven-year-old girl in Kuwait was killed by falling {shrapnel}.", "G13", "G card", "KUWAIT, 4 MARCH", "REPORTED · Kuwait Health Ministry", "soft hit"),
("P1-05", "A projectile hit Ras Tanura, Saudi Arabia's biggest domestic {refinery}.", "G14", "G map: Ras Tanura pin", "RAS TANURA HIT", "REPORTED · Reuters via Al Jazeera", "impact"),
("P1-06", "By the middle of March, the United Arab Emirates alone had intercepted more than three hundred ballistic missiles and over sixteen hundred {drones}.", "G16",
 "G three stats: 314 · 15 · 1,672", "UAE: 2,000 INTERCEPTS", "REPORTED · IntelliNews", "tick"),
("P1-07", "Then, on the eighth of April, a ceasefire. And for most of the autumn, the Gulf went {quiet}.", "G17", "G timeline: 8 APR CEASEFIRE · SEPT LAST ATTACK", "A QUIET AUTUMN", "REPORTED", "whoosh"),
("P1-08", "Until the thirteenth of November. Iran attacked Bahrain, its first attack on a Gulf country since early September. Then again. Four attacks in six {days}.", "G04",
 "G calendar: 13-18 NOV, four marks", "BAHRAIN: 4 ATTACKS IN 6 DAYS", "REPORTED · Al Jazeera", "tick"),
("P1-09", "On the seventeenth, drones went for an American radar at a Bahraini air base. Iran said it was answering American drones in its {airspace}.", "G02",
 "G map: Bahrain pin SHEIKH ISA AIR BASE", "TARGET: US RADAR, BAHRAIN", "REPORTED · Al Jazeera", "impact"),
("P1-10", "Hours later, the United States struck a missile launch site on Qeshm, an Iranian island in the Strait of {Hormuz}.", "G03",
 "G map: Qeshm pin in the strait", "US STRIKES QESHM", "REPORTED · US official via Al Jazeera", "impact"),
("P1-11", "The next day, Kuwait switched on its air defences for the first time since September. Iran claimed it had hit American Patriot missile systems at Ali Al Salem air {base}.", "G05",
 "G map: Kuwait pin ALI AL SALEM", "KUWAIT: AIR DEFENCES ON", "CLAIM · Iran's military via The National", "impact"),
("P1-12", "In the strait, a UAE state oil company ship was hit. Eleven crew injured, one missing. A gas tanker caught {fire}.", "G09",
 "G two number cards: 11 INJURED · 1 MISSING", "ADNOC SHIP HIT", "REPORTED · Khaleej Times", "impact"),
("P1-13", "A third American aircraft carrier arrived. And this week, more drones over Kuwait. Falling debris killed two Italian {citizens}.", "G08 G12",
 "G stats: 3 CARRIERS · 2 KILLED", "THIS WEEK: KUWAIT AGAIN", "REPORTED · Gulf News", "soft hit"),
("P1-14", "Kuwait called it a dangerous escalation. Saudi Arabia condemned Iran in the strongest terms. And Qatar's attempts to mediate have {stalled}.", "G06 G11",
 "G checklist: KUWAIT · SAUDI · GCC · QATAR MEDIATION STALLED", "THE GULF IS ANGRY", "REPORTED", "pen"),
("P1-15", "Meanwhile, in Yemen, the Houthis are firing cruise missiles at Riyadh, and now hold the whole Red Sea {coast}.", "G10",
 "G map: Yemen Red Sea coast highlighted", "HOUTHIS: THE RED SEA COAST", "REPORTED · AFP", "whoosh"),
("P1-15b", "Iran isn't only aiming at bases. Earlier this year, a drone hit fuel tanks at Kuwait's main airport, Kuwait cut its oil output as a precaution, and Saudi Arabia shot down a drone heading for the Shaybah oil {field}.", "G51",
 "G checklist: KUWAIT AIRPORT FUEL · KUWAIT OIL CUT · SHAYBAH DRONE", "OIL AND AIRPORTS, NOT JUST BASES", "REPORTED · AFP", "pen"),
("P1-16", "So the question isn't whether the Gulf is in this war. It already is. The question is how much {further} it goes.", "",
 "G card: NOT IF. HOW FAR.", "NOT IF. HOW FAR.", "", "soft hit"),
("P1-17", "Line one on the {receipt}.", "", "G running receipt line 1", "LINE 1 · THE GULF IS IN IT", "", "printer"),
])

part("Break", "~4:00", [
("BR-01", "Quick one. This is part seven of our Iran War Bill series. If you want the next one when it lands, {subscribe}.", "",
 "G sub card: 7 OF THE IRAN WAR BILL · SUBSCRIBE", "SUBSCRIBE", "", "soft tick"),
])

part("Part 2: A glass house", "~4:15", [
("P2-01", "Part two. A glass {house}.", "", "G part card PART 2 · A GLASS HOUSE", "PART 2 · A GLASS HOUSE", "", "reverse cymbal"),
("P2-02", "Here's the thing most people don't know about the Gulf. Most of it has almost no fresh water. So it makes its own, from the {sea}.", "G18",
 "G card: THE GULF DRINKS THE SEA", "THE GULF DRINKS THE SEA", "", "soft hit"),
("P2-03", "About ninety per cent of Kuwait's drinking water comes from desalination plants. About eighty-six per cent in Oman. About seventy per cent in Saudi {Arabia}.", "G18",
 "G bars: KUWAIT 90 · OMAN 86 · SAUDI 70", "DRINKING WATER FROM DESALINATION", "REPORTED · AP", "tick"),
("P2-04", "And it's concentrated. A CIA analysis found that more than ninety per cent of the Gulf's desalinated water comes from just fifty-six {plants}.", "G19",
 "G dots: 56", "56 PLANTS", "REPORTED · CIA 2010 via AP", "tick"),
("P2-05", "A leaked American cable from two thousand and eight said that if one big plant at Jubail were badly damaged, Riyadh would have to evacuate within a {week}.", "G20",
 "G quote card: 'EVACUATE WITHIN A WEEK'", "RIYADH: 'WITHIN A WEEK'", "REPORTED · 2008 US cable via AP", "stamp thud"),
("P2-05b", "On the second of March, Iranian strikes on Dubai's Jebel Ali port landed about twelve miles from one of the biggest desalination plants in the {world}.", "G55",
 "G map: Jebel Ali pin; label 12 MILES", "12 MILES AWAY", "REPORTED · AP", "impact"),
("P2-06", "This year, those plants became {targets}.", "", "G card", "THIS YEAR: TARGETS", "", "soft hit"),
("P2-07", "In March, Iranian drones damaged a desalination plant in Bahrain. Officials said the water kept {flowing}.", "G21", "G map: Bahrain pin", "BAHRAIN, MARCH", "REPORTED · AFP", "impact"),
("P2-08", "In April, two Kuwaiti power and water plants suffered serious damage. In July, another {one}.", "G22 G23",
 "G timeline: APR 2 PLANTS · JUL 1 PLANT", "KUWAIT: APRIL · JULY", "REPORTED · Al Jazeera; AP", "impact"),
("P2-09", "Many of these plants make electricity and water together. Hit the power, and you can lose the water {too}.", "G24",
 "G chain: POWER STATION · DESALINATION · TAPS", "POWER = WATER", "REPORTED · AP", "whoosh"),
("P2-10", "Kuwait has been here before. In nineteen-ninety-one, Iraqi forces wrecked its power and water. Full recovery took {years}.", "G25",
 "G timeline: 1991", "1991: YEARS TO RECOVER", "REPORTED · AP", "soft hit"),
("P2-11", "And Iran says it has suffered the same thing. It claims an American strike on Qeshm cut water to thirty villages. The US hasn't acknowledged {it}.", "G26",
 "G card", "IRAN: 30 VILLAGES", "CLAIM · Iran via AP", "stamp thud"),
("P2-11b", "Iran knows what a water crisis looks like. In March, Tehran's reservoirs fell to about ten per cent, and its own president warned the capital might have to be {evacuated}.", "G56",
 "G gauge 10% · TEHRAN RESERVOIRS", "TEHRAN: 10%", "REPORTED · AP", "tick"),
("P2-12", "Why does a Kuwaiti water plant matter to you? Because a Gulf state without water can't keep pumping oil, can't keep shipping gas, and can't keep its airports {open}.", "",
 "G chain: WATER · PEOPLE · OIL · GAS · FLIGHTS", "NO WATER, NO OIL", "ANALYSIS", "riser"),
("P2-12b", "And if a Gulf state has to choose between keeping its people supplied and keeping its export terminals running, the people come {first}.", "",
 "G split: PEOPLE · EXPORTS", "PEOPLE FIRST", "ANALYSIS", "soft hit"),
("P2-13", "The Gulf is a glass house. And this month, stones started flying {again}.", "", "G card", "A GLASS HOUSE", "", "soft hit"),
("P2-14", "Line two on the {receipt}.", "", "G running receipt line 2", "LINE 2 · 56 PLANTS", "", "printer"),
])

part("Part 3: The gas", "~7:30", [
("P3-01", "Part three. The {gas}.", "", "G part card PART 3 · THE GAS", "PART 3 · THE GAS", "", "reverse cymbal"),
("P3-02", "Ras Laffan, in Qatar, is the biggest liquefied gas plant on earth. Qatar makes about a fifth of all the LNG the world {buys}.", "G28",
 "G map: Qatar Ras Laffan pin", "QATAR: 1/5 OF WORLD LNG", "REPORTED · Al Jazeera; Argus", "sub hit"),
("P3-03", "On the second of March, Iranian drones hit it. Qatar stopped making gas {altogether}.", "G27",
 "G typed card: PRODUCTION HALTED · 2 MARCH 2026", "LNG HALTED", "REPORTED · QatarEnergy via Al Jazeera", "stamp thud"),
("P3-04", "That day, wholesale gas in Britain and the Netherlands jumped almost fifty per {cent}.", "G30",
 "G number card +50% IN A DAY", "+50% IN A DAY", "REPORTED · Al Jazeera", "impact"),
("P3-04b", "At the same time, traffic through the Strait of Hormuz fell eighty-six per cent. About seven hundred ships sat {idle}.", "G52",
 "G number card -86%; sub 700 SHIPS IDLE", "HORMUZ -86%", "REPORTED · Anadolu via Al Jazeera", "tick"),
("P3-04c", "Analysts at ING warned European gas could head towards eighty to a hundred euros if Qatar stayed offline for a long {time}.", "G53",
 "G card: €80-100/MWh?", "ING: €80-100?", "REPORTED · City AM", "stamp thud"),
("P3-05", "On the eighteenth of March, Iranian missiles hit Ras Laffan again. This time, extensive {damage}.", "G31", "G map", "18 MARCH: HIT AGAIN", "REPORTED · QatarEnergy", "impact"),
("P3-06", "European gas hit seventy-four euros a megawatt hour, the highest since January twenty-twenty-three. About double where it was before the {war}.", "G31",
 "G ladder: ≈ €37 → €74", "€74/MWh · DOUBLE", "REPORTED · Reuters", "whoosh"),
("P3-07", "And here's the line that matters for years, not weeks. Qatar's energy chief said seventeen per cent of its export capacity was damaged, and repairs would take three to five {years}.", "G32",
 "G number card 3-5 YEARS; sub 17% OF CAPACITY", "REPAIRS: 3-5 YEARS", "REPORTED · QatarEnergy CEO via Reuters", "stamp thud"),
("P3-08", "Europe gets about twelve to fourteen per cent of its LNG from Qatar. Britain buys on the same market, so when Europe pays more, so do {we}.", "G29",
 "G map: Qatar to Europe LNG route", "EUROPE: 12-14% FROM QATAR", "REPORTED · City AM", "whoosh"),
("P3-09", "And Europe's gas stores were low. Under twenty-nine per cent full in March, the lowest for that date in four {years}.", "G33",
 "G gauge 28.8%", "EU STORAGE 28.8%", "REPORTED · Argus", "tick"),
("P3-10", "That's part of why your energy price cap goes up to two thousand, one hundred and sixty-six pounds in {January}.", "G34",
 "G number card £2,166 · FROM 1 JAN; faded £1,723", "£2,166 FROM JANUARY", "REPORTED · Ofgem", "register ding"),
("P3-11", "The cap is set from earlier prices, so it lags. A gas shock this winter lands on your bill in the {spring}.", "G34",
 "G calendar: JAN · APR circled", "SHOCK NOW, BILL IN APRIL", "REPORTED · Ofgem", "pen"),
("P3-12", "In March, Donald Trump warned that if Iran hit Qatar's gas again, he would massively blow up the entirety of Iran's South Pars gas {field}.", "G50",
 "G quote card", "'BLOW UP SOUTH PARS'", "REPORTED · Reuters", "stamp thud"),
("P3-13", "Gas for gas. That's the escalation ladder that matters most for your heating {bill}.", "", "G card: GAS FOR GAS", "GAS FOR GAS", "ANALYSIS", "soft hit"),
("P3-14", "Line three on the {receipt}.", "", "G running receipt line 3", "LINE 3 · GAS × 2", "", "printer"),
])

part("Part 4: The flights", "~11:00", [
("P4-01", "Part four. The {flights}.", "", "G part card PART 4 · THE FLIGHTS", "PART 4 · THE FLIGHTS", "", "reverse cymbal"),
("P4-02", "Dubai International is the busiest airport in the world for international travel. Ninety-five million passengers last {year}.", "G37",
 "G number card 95.2M · 2025", "95.2M PASSENGERS", "REPORTED · AP", "tick"),
("P4-03", "In the first days of the war, more than twenty-one thousand flights were cancelled at seven big Gulf airports. By mid-March, more than thirty-seven {thousand}.", "G36",
 "G bars: 3 MAR 21,300 · MID-MAR 37,000+", "37,000+ FLIGHTS CANCELLED", "REPORTED · Flightradar24; Emerging Travel", "tick"),
("P4-04", "Washington told Americans in fourteen countries, including the Emirates, Qatar and Saudi Arabia, to depart {now}.", "G38",
 "G typed card: 'DEPART NOW'", "'DEPART NOW'", "REPORTED · US State Dept via Al Jazeera", "stamp thud"),
("P4-05", "Charter flights from Dubai to Europe went for more than two hundred thousand {dollars}.", "G39", "G pricetag $200,000+", "$200,000 CHARTERS", "REPORTED · Fortune", "register ding"),
("P4-06", "In March, Dubai's passenger numbers fell by two-thirds. Over the first half of the year, down thirty-one per {cent}.", "G40",
 "G bars: H1 2025 45.8M · H1 2026 31.5M", "DUBAI: -31%", "REPORTED · Dubai Airports via AP", "tick"),
("P4-07", "Why should you care if you're not flying to Dubai? Because Dubai and Doha are how millions of people get from Britain to Asia and {Australia}.", "",
 "G map: London → Gulf → Asia routes", "THE WORLD'S CONNECTING HUB", "ANALYSIS", "whoosh"),
("P4-08", "When the Gulf carriers stopped, bookings and fares on routes like Hong Kong to London jumped. Gulf fares rose thirty-five to forty-five per cent, and they're still above where they {were}.", "G41 G42",
 "G number card +35-45%", "FARES +35-45%", "REPORTED · Reuters; VIDEC via Gulf News", "register ding"),
("P4-09", "Middle Eastern airlines are expected to go from a seven billion dollar profit last year to a four billion dollar loss this {year}.", "G43",
 "G two numbers: 2025 +$7.2BN · 2026 -$4.3BN", "+$7.2BN → -$4.3BN", "REPORTED · IATA", "tick"),
("P4-10", "Dubai's hotels were barely half full in the first half of the year. Its stock market fell about seventeen per cent in the war's first {weeks}.", "G44",
 "G two numbers: HOTELS 56% · STOCKS -17%", "HOTELS 56% · STOCKS -17%", "REPORTED · Gulf News; KPMG", "tick"),
("P4-10b", "Tourism was about twelve per cent of the Emirates' economy. Ryanair's boss predicted Gulf tourism would falter for the next year or {two}.", "G54 G58",
 "G gauge 12% · OF THE UAE ECONOMY", "TOURISM: 12% OF THE UAE", "REPORTED · Statista; Fortune", "tick"),
("P4-11", "And British expats who fled home were warned they might suddenly owe UK {tax}.", "G45", "G card", "EXPATS: A TAX BILL TOO", "REPORTED · IntelliNews", "soft hit"),
("P4-12", "That was the cost of one round of Gulf strikes. A wider, longer war would cost more, and the hit would land hardest on Kuwait and {Bahrain}.", "G49",
 "G card", "A WIDER WAR COSTS MORE", "ANALYSIS · VIDEC via Gulf News", "soft hit"),
("P4-12b", "So far the Gulf states have held back. But in April, Saudi Arabia talked about its right to self-defence, and the Emirates said they were ready to join any American effort to secure the {strait}.", "G57",
 "G split: SAUDI: SELF-DEFENCE · UAE: READY TO JOIN", "PATIENCE RUNNING OUT", "REPORTED · Al Jazeera", "soft hit"),
("P4-12c", "We've seen the Gulf pulled in before. In the tanker war of the nineteen-eighties, Kuwait's tankers sailed under the American flag to get an {escort}.", "G60",
 "G timeline: 1987 KUWAITI TANKERS REFLAGGED", "1987: UNDER THE US FLAG", "VERIFIED · Wikipedia", "whoosh"),
("P4-13", "Line four on the {receipt}.", "", "G running receipt line 4", "LINE 4 · FLIGHTS -31%", "", "printer"),
])

part("Part 5: Your bill", "~14:00", [
("P5-01", "Part five. Your {bill}.", "", "G part card PART 5 · YOUR BILL", "PART 5 · YOUR BILL", "", "reverse cymbal"),
("P5-02", "First, the rule of thumb. Every ten dollars on a barrel of oil is about six pence on a litre of petrol, and about twenty-four cents on a US {gallon}.", "G47",
 "G three stats: $10 · 6p · 24¢", "$10 ≈ 6p ≈ 24¢", "ILLUSTRATION · our maths", "tick"),
("P5-03", "Right now, Brent is about eighty-eight dollars. Here are three ways a Gulf war could {go}.", "G46", "G three cards: CONTAINED · ENERGY HIT · WATER WAR", "THREE WAYS", "SCENARIO", "riser"),
("P5-04", "Way one. Contained. Drones and interceptions, like this month, but no big energy site goes down. Oil drifts up to around a hundred. That's about seven pence a litre, for a few {weeks}.", "G47",
 "G pricetags: OIL ≈ $100 · +7p A LITRE", "CONTAINED: ≈ +7p, BRIEFLY", "SCENARIO · our maths", "register ding"),
("P5-04b", "On a fifty-five litre tank, that's under four pounds a fill. Annoying, not {painful}.", "G61",
 "G pricetag ≈ £3.85 A TANK", "≈ £3.85 A TANK", "ILLUSTRATION · our maths", "register ding"),
("P5-05", "Way two. An energy hit. A refinery, an oil field or Ras Laffan goes down again. Oil back to this year's peak of a hundred and twenty-six. About twenty-two pence a litre, twelve pounds a tank, ninety cents a {gallon}.", "G46 G47",
 "G three price tags: +22p · +£12 · +90¢", "ENERGY HIT: +22p · +£12 · +90¢", "SCENARIO · our maths", "register ding"),
("P5-05b", "Fill up twice a month, and that's about two hundred and ninety pounds over a {year}.", "G61",
 "G pricetag ≈ £290 A YEAR", "≈ £290 A YEAR", "ILLUSTRATION · our maths", "register ding"),
("P5-06", "And gas would follow. In March, one strike doubled Europe's gas price. Your heating bill would feel it at the next cap {change}.", "G31 G34",
 "G calendar: APR 2027 circled", "GAS: AT THE NEXT CAP", "SCENARIO", "pen"),
("P5-07", "Way three. A water war. If desalination plants go down at scale, whole cities could struggle to stay open. That's when oil and gas output itself is at risk, and nobody can put a sensible number on {that}.", "G19 G20 G24",
 "G card: NO SENSIBLE NUMBER", "WATER WAR: OFF THE SCALE", "SCENARIO", "stamp thud"),
("P5-08", "For America, an energy hit takes the average gallon from three seventy-eight to about four sixty-{eight}.", "G48 G47",
 "G pricetags: NOW $3.78 · ENERGY HIT ≈ $4.68", "US: $3.78 → $4.68", "ILLUSTRATION · our maths", "register ding"),
("P5-09", "And the rest arrives slowly. Dearer flights to Asia. Dearer shipping. Dearer {insurance}.", "G41",
 "G chain: FLIGHTS · SHIPPING · INSURANCE · SHOPPING", "THE SLOW BILL", "ANALYSIS", "whoosh"),
("P5-10", "Remember the rule from our earlier video. Prices go up like a rocket and come down like a {feather}.", "",
 "G rocket and feather lines", "UP FAST · DOWN SLOW", "VERIFIED · NBER", "whoosh"),
("P5-11", "Line five on the {receipt}.", "", "G running receipt line 5", "LINE 5 · +7p TO +22p", "", "printer"),
])

part("Part 6: What to watch", "~16:30", [
("P6-01", "Part six. What to {watch}.", "", "G part card PART 6 · WHAT TO WATCH", "PART 6 · WHAT TO WATCH", "", "reverse cymbal"),
("P6-02", "Four things. One. Ras Laffan. Any attack on Qatar's gas means your heating bill, {first}.", "G27", "G checklist item 1", "1 · RAS LAFFAN", "", "pen"),
("P6-03", "Two. Water plants. A hit on a big desalination plant is the step that changes everything {else}.", "G19", "G checklist item 2", "2 · WATER PLANTS", "", "pen"),
("P6-04", "Three. Saudi Arabia. So far it has condemned and intercepted. If it starts firing back, this becomes a regional {war}.", "G06", "G checklist item 3", "3 · SAUDI ARABIA", "", "pen"),
("P6-05", "Four. Qatar's mediation. If talks restart, the risk premium {fades}.", "G11", "G checklist item 4", "4 · THE TALKS", "", "pen"),
("P6-05b", "And one more, for Britain and Europe. The winter. Gas stores started this year low. A cold snap plus a hit on Qatar is the combination that bites {hardest}.", "G33",
 "G card: COLD SNAP + QATAR HIT", "THE WINTER RISK", "REPORTED · Argus; ANALYSIS", "soft hit"),
("P6-05c", "If none of those four move, the bill stays where it is. If two of them move at once, expect it to {jump}.", "",
 "G roadmap: RAS LAFFAN · WATER · SAUDI · TALKS", "WATCH THE FOUR", "", "pen"),
("P6-06", "Right now, the Gulf is in the war, but not yet at war. The difference between those two is your {bill}.", "",
 "G split: IN THE WAR · AT WAR", "IN IT, NOT AT WAR", "", "soft hit"),
])

part("The Receipt", "~17:30", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. The Gulf is already in this {war}.", "G04 G05", "G receipt line 1 prints", "THE GULF IS IN IT", "", "printer"),
("RC-03", "Line two. Fifty-six plants that make the Gulf's {water}.", "G19", "G receipt line 2", "56 WATER PLANTS", "", "printer"),
("RC-04", "Line three. One strike that doubled Europe's {gas}.", "G31", "G receipt line 3", "GAS × 2", "", "printer"),
("RC-05", "Line four. Dubai's passengers down by almost a {third}.", "G40", "G receipt line 4", "FLIGHTS -31%", "", "printer"),
("RC-06", "Line five. Seven to twenty-two pence a litre, depending how far it {goes}.", "G47", "G receipt line 5", "+7p TO +22p", "", "printer"),
("RC-07", "The Gulf is a glass house, and this month the stones came back. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp PENDING; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-024 What If the Iran War Spreads to the Gulf?: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/128:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not financial advice.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-024-gulf-spread/INV-024-gulf-spread-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
