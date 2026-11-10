# INV-006 script v4 extension rows (new in v4, marked NEW). Inserted AFTER the given code.
INS = {
"P1-10b": [
("P1-10d","So what are you actually paying for? Ofgem publishes the answer. Take the typical bill right now, one thousand seven hundred and twenty-three pounds a year. Almost half of it, forty-seven percent, is the gas and power itself, bought on the wholesale market. About a quarter is the cost of the pipes and wires that bring it to your door.","F70","Stacked bar builds: wholesale 47%, networks 24%, operating 17%, policy 6%.","WHOLESALE 47% · NETWORKS 24%","VERIFIED · Ofgem cap summary, Oct-Dec 2026","chart grow"),
("P1-10e","Another seventeen percent is the supplier's running costs, including the money it loses when customers can't pay. Six percent is government policy costs. And then there's tax. Since the first of October, household electricity has carried no VAT, and that's now been extended to July 2027. Gas still carries five percent.","F70 F45","Same bar: the VAT slice for electricity empties, gas stays at 5%.","GAS VAT 5% · ELECTRICITY VAT 0% (TO JUL 2027)","VERIFIED · Ofgem; Budget 28 Oct 2026","tick"),
("P1-10f","That first slice is the one that moves. The pipes cost about the same in a war as in peace. The wholesale gas does not. So when a plant in Qatar goes quiet, it's almost half of your bill that starts to swing.","F70","Wholesale slice pulses orange and wobbles; the rest stays grey.","THE SLICE THAT MOVES","VERIFIED · Ofgem","sub hit"),
("P1-10g","The cap itself is younger than most people think. It only started on the first of January 2019. It was meant to stop loyal customers being overcharged. It was never designed for a war.","F75","Timeline card: 2019 cap begins, 2022 crisis, 2026 war.","PRICE CAP SINCE 1 JAN 2019","VERIFIED · Ofgem decision, Nov 2018",""),
],
"P2-11": [
("P2-11d","To see why that matters, go back to 2017. Rough was Britain's big tank then. Fully open, it held around seventy percent of all the gas storage in the country, enough for about nine days.","F71","MAP: North Sea, Rough glows, a tank icon fills to 70%.","ROUGH ≈ 70% OF UK STORAGE (FULLY OPEN)","REPORTED · Centrica via Wikipedia",""),
("P2-11e","In June 2017, its owner said it was too old and too expensive to keep running, and announced it would close. The tank was empty when the next big cold snap arrived.","F71","Stamp CLOSED lands on the Rough tank, June 2017.","CLOSURE ANNOUNCED · JUNE 2017","REPORTED · Centrica via Wikipedia","stamp"),
("P2-11f","First of March 2018. The Beast from the East. Snow across Britain, and a gas system almost forty-eight million cubic metres short of what the country needed that day. National Grid issued a gas deficit warning. Within the day, the gas price hit three hundred pence a therm, a twelve-year high.","F74","Footage: snow storm; then CARD-NUMBER 300p/therm.","1 MAR 2018 · GAS DEFICIT WARNING · 300P/THERM","REPORTED · National Grid via Watt-Logic","wind + sub hit"),
("P2-11g","Analysts pointed at the empty space where Rough used to be. Up to forty-five million cubic metres a day that could have come out of storage, didn't exist.","F74","Gauge: a 45 mcm/day bar drawn as an empty outline.","45 MCM/DAY MISSING","REPORTED · Watt-Logic",""),
("P2-11h","Then came 2022. Rough was partly reopened in October that year, at about a fifth of its old size. Now it's the site that might close again. Twice in ten years, Britain has had to think about winter without its biggest tank. And when the tank is small, the price of the next cargo lands straight on your bill.","F71","Timeline: 2017 closed, 2022 reopened 20%, 2027 at risk.","2017 CLOSED · 2022 REOPENED (20%) · 2027 AT RISK","REPORTED","riser"),
],
"P4-01b": [
("P4-01c","1973 is worth remembering for another reason. On the sixteenth of October, the oil producers' cartel raised its price. The next day, Arab producers cut output and began an embargo on the West.","F76","Typewriter dates on dark: 16 OCT 1973 · 17 OCT 1973.","16-17 OCTOBER 1973","REPORTED · MoneyWeek","typewriter"),
("P4-01d","Oil went from about three dollars a barrel to about twelve. Four times the price, in a few months. The embargo ended in March 1974. The prices did not go back.","F76","CARD-NUMBER: $3 → $12 a barrel.","$3 → $12 A BARREL","REPORTED · MoneyWeek","counter roll"),
("P4-01e","Britain's answer was to dig. North Sea oil and gas turned a shock into fifty years of home supply. That's the history hiding in your boiler. And it's why the end of the North Sea matters now. The last time this little gas came out of British water, the crisis made Britain build a new source. This time there isn't one waiting.","F58 F76","Footage: offshore platform, then UK production line returns to the 1973 marker.","50 YEARS OF NORTH SEA GAS","VERIFIED · DUKES 2026","whoosh-deep"),
],
"P4-05": [
("P4-05b","And it's not the only bill left over from last time. In 2021, before the war in Ukraine even started, gas prices rose so fast that small energy suppliers began to fall over. They had sold you energy at a fixed price they could no longer afford to buy.","F72","Footage: office lights switching off; then a grid of supplier logos (generic blocks) turning grey.","2021: SUPPLIERS COLLAPSE","VERIFIED · National Audit Office, 2022","power down"),
("P4-05c","The National Audit Office counted twenty-eight suppliers failing from June 2021. Almost two and a half million customers were moved to new companies.","F72","Grid of 28 blocks greys out one by one.","28 SUPPLIERS FAILED · 2.4M CUSTOMERS MOVED","VERIFIED · NAO","tick"),
("P4-05d","The biggest was Bulb, with one point six million customers. The government ran it through special administration, budgeting nearly two billion pounds across two years.","F72","CARD-NUMBER: Bulb 1.6M customers · £0.9bn + £1.0bn.","BULB: £0.9BN + £1.0BN BUDGETED","VERIFIED · NAO","counter roll"),
("P4-05e","Ofgem estimated the failures would cost two point seven billion pounds, spread across everyone's bills. About ninety-four pounds per customer. If you paid an energy bill in 2022, you paid for companies you never used.","F72","RECEIPT line prints: SUPPLIER FAILURES ≈ £94.","≈ £94 PER CUSTOMER","ESTIMATE · Ofgem via NAO","receipt printer"),
],
"P5-06b": [
("P5-06c","Let's put the forecasts into one household. If the cap moves from one thousand seven hundred and twenty-three pounds to the low forecast, that's two hundred and seventy-six pounds more over a year. To the high forecast, four hundred and sixty-six.","F42 F43","Household maths card: £1,723 → £1,999 = +£276; → £2,189 = +£466.","+£276 TO +£466 A YEAR","ESTIMATE · our maths from forecasts","counter roll"),
("P5-06d","But the January cap only lasts three months. So the bill for this winter's cold months alone is roughly sixty-nine to one hundred and seventeen pounds extra. That's the number to plan for first. And if spring prices don't fall, it carries on.","F42 F43","Calendar: JAN FEB MAR light up with +£69 to +£117.","JAN-MAR: +£69 TO +£117","ESTIMATE · our maths",""),
],
"RC-05": [
("RC-05b","Here's what that help looked like last winter, so you know what to ask about. The Warm Home Discount took a hundred and fifty pounds off the electricity bill of every household on means-tested benefits. More than six million homes.","F73","Card: £150 WARM HOME DISCOUNT · 6M+ HOMES (WINTER 2025/26).","WARM HOME DISCOUNT · £150","VERIFIED · GOV.UK, 19 June 2025","tick"),
("RC-05c","The Winter Fuel Payment went to pensioners automatically in November and December. Two hundred pounds, or three hundred if someone at home was over eighty, for those with an income of thirty-five thousand pounds or less. Check both are running this winter, and on the same terms.","F77","Card: £200 / £300 (OVER 80) · INCOME ≤ £35,000 (2025/26 RULES).","WINTER FUEL PAYMENT · £200-£300","REPORTED · 2025/26 rules","tick"),
("RC-05d","And there's one thing that costs nothing. Ask your supplier to put you on its Priority Services Register if anyone at home is older, ill, or has young children. It won't lower the price. It means they have to look after you first when things go wrong.","","Card: PRIORITY SERVICES REGISTER · FREE.","PRIORITY SERVICES REGISTER · FREE","GENERAL GUIDANCE",""),
],
}
NEWFACTS = [
("F70","Typical dual-fuel cap Oct-Dec 2026: £1,723/yr; wholesale 47%, networks 24%, operating/debt 17%, policy 6%, gas VAT 5%, electricity VAT 0% from 1 Oct 2026 to 31 Mar 2027.","Ofgem, Summary of changes to energy price cap 1 Oct-31 Dec 2026","Aug 2026","VERIFIED"),
("F71","Rough held ~70% of UK storage capacity when fully open (~9 days' supply); closure announced June 2017; partly reopened 28 Oct 2022 at ~20% capacity.","Wikipedia 'Rough (facility)' citing Centrica","2026","REPORTED"),
("F72","28 suppliers failed from June 2021; ~2.4m customers moved; Ofgem estimate £2.7bn (~£94 per customer); Bulb 1.6m customers, govt £0.9bn in 2021-22 + £1.0bn budgeted 2022-23.","National Audit Office, The energy supplier market","Jun 2022","VERIFIED"),
("F73","Warm Home Discount £150 for every billpayer on means-tested benefits, 6m+ households, winter 2025/26.","GOV.UK press release","19 Jun 2025","VERIFIED"),
("F74","1 Mar 2018: National Grid Gas Deficit Warning, system ~48 mcm short; within-day NBP 300p/th (12-yr high); Rough closure removed up to 45 mcm/d.","Watt-Logic analysis","1 Mar 2018","REPORTED"),
("F75","Ofgem default tariff (price) cap began 1 Jan 2019.","Ofgem decision Nov 2018; Centrica 2019","2019","VERIFIED"),
("F76","16 Oct 1973 OPEC price rise; 17 Oct Arab output cut and embargo; oil ~$3 → ~$12/bbl; embargo ended Mar 1974.","MoneyWeek","2023","REPORTED"),
("F77","Winter Fuel Payment 2025/26: £200, £300 if someone over 80; income £35,000 or less keeps it (England & Wales).","Homebuilding citing DWP","Jun 2025","REPORTED"),
]
INS["P1-10b"][2] = ("P1-10f","That first slice is the one that moves. The pipes cost about the same in a war as in peace. The wholesale gas does not. At the start of this year, wholesale was thirty-seven percent of the typical bill. By October, it was forty-seven. So when a plant in Qatar goes quiet, it's almost half of your bill that starts to swing.","F70 F82","Wholesale slice grows from 37% to 47% and pulses orange; the rest stays grey.","WHOLESALE: 37% (JAN 2026) → 47% (OCT 2026)","VERIFIED · Ofgem","sub hit")
INS["P2-12"] = [
("P2-12b","And the old pipeline route isn't coming back either. On the twenty-sixth of September 2022, explosions tore through the Nord Stream pipelines under the Baltic Sea. Those pipes had been built to carry Russian gas straight into Germany.","F81","MAP: Baltic, two lines from Russia to Germany break with red flashes.","NORD STREAM · 26 SEP 2022","VERIFIED · OSW, 29 Sep 2022","sub hit"),
("P2-12c","So Europe lost the pipe, and now it's banning the ships from the same country. What's left is gas that comes by sea, from whoever will sell it. Every one of those cargoes can go to Europe, or to Asia. Which brings us to the auction.","F81","Map: the Baltic goes dark; ship icons appear on the Atlantic.","WHAT'S LEFT COMES BY SEA","VERIFIED","whoosh-deep"),
]
INS["P5-01b"] = [
("P5-01c","And here's why that number lands so hard in Britain. At the last census, about three in every four homes in England and Wales used mains gas as their only central heating. Not a backup. The only way the radiators get warm.","F80","Footage: radiator; then a 4x4 grid of houses, 3 in 4 light orange.","74% · MAINS GAS ONLY HEATING","VERIFIED · ONS Census 2021","tick"),
("P5-01d","So when the gas price moves, most families can't switch to something else for the winter. They pay it, or they go cold.","F80","Footage: house lights at evening.","PAY IT OR GO COLD","",""),
]
INS["P5-05"] = [
("P5-05b","And many of them are already behind. Ofgem counted three point six million customers in debt or arrears on their energy bills, owing a record four point four eight billion pounds. That was before this war's winter.","F78","CARD-NUMBER: £4.48bn · 3.6M customers.","£4.48BN OWED · 3.6M CUSTOMERS","VERIFIED · Ofgem, Q3 2025","counter roll"),
("P5-05c","By June 2026, the industry group Energy UK put the figure at around six billion pounds. A plan to wipe five hundred million pounds of that debt for the poorest customers has stalled, because it needs new law.","F79","Bars: £4.48bn (Q3 2025) → ~£6bn (Jun 2026); a £500m block greyed out.","≈ £6BN (JUNE 2026) · £500M WRITE-OFF STALLED","REPORTED · Energy UK","chart grow"),
("P5-05d","And here's the part that reaches every household. When debt goes unpaid, suppliers recover it through everyone's prices. Debt costs are already a line in the cap. So even if you pay on time, you help cover the homes that can't.","F78 F82","RECEIPT line prints: UNPAID DEBT (SHARED).","DEBT IS SHARED ACROSS BILLS","VERIFIED · Ofgem","receipt printer"),
]
INS["P5-07"] = [
("P5-07b","The weather is the first dial. In a normal winter, Europe's tanks end the season low but safe. In a cold one, the scenarios we showed you fall below ten percent. A cold January doesn't just make you turn the heating up. It makes every unit you burn cost more.","F15 F16","Dial 1 WEATHER turns to cold; storage gauge drops.","DIAL 1: THE WEATHER","SCENARIO · IEA / ENTSOG","tick"),
("P5-07c","The strait is the second. Eighty-five ships a day used to pass through Hormuz. Now it's around one. Each day that number stays low, the gas that used to sail from Qatar has to be replaced by somebody else's.","F09","Dial 2 STRAIT: 85 → 1.","DIAL 2: THE STRAIT","REPORTED · IMO PortWatch",""),
("P5-07d","And the auction is the third. As long as Asia pays more for a cargo than Europe does, the ships go east, and Europe has to raise its bid. That bid is the wholesale price. And the wholesale price is almost half of your bill.","F25 F70","Dial 3 AUCTION: JKM above TTF, arrow to RECEIPT.","DIAL 3: THE AUCTION","VERIFIED · Platts / Ofgem",""),
("P5-07e","Watch those three, and you'll know your January bill before Ofgem tells you.","","Three dials side by side, all glowing.","WEATHER · STRAIT · AUCTION","",""),
]
INS["RC-07"] = [
("RC-07b","Nineteen seventy-three. Twenty eighteen. Twenty twenty-two. Twenty twenty-six. Every time, the crisis started far away, with a war, an embargo, or a storm. And every time, it ended in the same place. A number on a bill, on a kitchen table, in a home that had nothing to do with it.","F76 F74","Timeline: 1973 · 2018 · 2022 · 2026, each with its bill.","1973 · 2018 · 2022 · 2026","",""),
]
NEWFACTS += [
("F78","Domestic energy debt and arrears (>91 days) record £4.48bn, 3.6m customers in debt or arrears, Q3 2025.","Ofgem State of the Market, Jan 2026","Jan 2026","VERIFIED"),
("F79","Energy UK: ~£6bn energy debt and arrears end June 2026; £500m write-off scheme stalled pending legislation.","Energy UK via Reuters/Cyprus Mail","29 Aug 2026","REPORTED"),
("F80","74% of households in England and Wales used mains gas as their only central heating (Census 2021).","ONS","5 Jan 2023","VERIFIED"),
("F81","Explosions damaged Nord Stream 1 and 2 pipelines in the Baltic on 26 Sep 2022.","OSW analysis","29 Sep 2022","VERIFIED"),
("F82","Wholesale was 37% and debt-related costs 3% of the typical dual-fuel bill in Jan-Mar 2026.","Ofgem State of the Market, Jan 2026","Jan 2026","VERIFIED"),
]

INS["RC-04"] = [
("RC-04b","Here's one more that costs nothing, if you have a combi boiler. Most are set to heat the water in your radiators to around eighty degrees. The innovation charity Nesta tested turning that down to sixty or below. The house still warms up, just a little slower. In 2022, Nesta put the saving at about a hundred and twelve pounds a year, at the prices back then.","F83","Footage: boiler / radiator; card 80°C → 60°C.","COMBI BOILER: 80°C → 60°C","VERIFIED · Nesta, Oct 2022","tick"),
("RC-04c","It only applies to combi boilers. And if anyone at home is vulnerable to the cold, warmth comes first. A smaller bill is never worth a cold home. Check your boiler's manual, or ask an engineer to set it.","F83","Card: COMBI ONLY · WARMTH FIRST.","COMBI ONLY · WARMTH FIRST","GENERAL GUIDANCE",""),
]
INS["P3-12"] = [
("P3-12b","So who won the auction? On paper, Europe did. It got most of America's ships. But winning an auction means paying the top price. Europe kept its tanks filling by outbidding countries that could afford it less. And that top price is exactly what rolls into Britain's cap in January.","F62 F25","Receipt columns: EUROPE column gets a WON stamp, then a price tag flips up.","EUROPE WON · AT THE TOP PRICE","VERIFIED","stamp"),
]
INS["P4-07"] = [
("P4-07b","So the last time leaves two lessons. Help can arrive fast when a government decides to pay. And whatever it pays, households pay back later, in tax and on their bills. This time, the help is small, and the bill is still being written.","","Receipt: two lines, HELP ARRIVES FAST · YOU PAY IT BACK.","TWO LESSONS FROM 2022","",""),
]
INS["P1-12"] = [
("P1-12b","So that's the first line on the receipt. A plant in Qatar goes quiet, a strait almost empties, and the forward price of gas jumps in exactly the months Ofgem uses to set your January cap. But that's only the price. The next question is whether Europe has enough gas to get through the winter at all.","","RECEIPT corner: line 1 printed; camera pushes to a storage tank icon.","LINE 1: THE PRICE","",""),
]
NEWFACTS += [("F83","Lowering combi boiler flow temperature from 80C to 60C or below saves a typical household about £112/yr (2022 prices).","Nesta press release","25 Oct 2022","VERIFIED")]
