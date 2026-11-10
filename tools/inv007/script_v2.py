# INV-007 script v2 = v1 + 13 rows for the ~30-minute cut (Hammad OK 2026-11-10: "go ahead make the final video").
# Every new number traces to facts.md (F/H rows). Rows inserted after the code named in INSERT.
import runpy, pathlib
_v1 = runpy.run_path(str(pathlib.Path(__file__).with_name("script_v1.py")))
PARTS = _v1["PARTS"]
INSERT = [
("P1-05", ("P1-05b",
 "And outside the strait, another two hundred and forty ships waited to come in. So a queue formed on both sides of a door that nobody would open. Each of those ships has a crew. Most of them signed on for a normal voyage. Load in the Gulf, sail out, go home at the end of the contract. Nobody signed on for a siege.",
 "F12", "VIDEO: ships waiting at anchor offshore", "240 WAITING OUTSIDE", "CLAIM · Aramco CEO, May 2026", "")),
("P1-07", ("P1-07b",
 "Think about what that means in practice. A ship carries stores for a voyage, not for a siege. Fresh water is made on board by machines that need fuel. Fuel comes by barge, and the barges have to cross the same dangerous water. So by late April, the IMO's warning was simple. On many stranded ships, water, food and fuel were expected to run short.",
 "F33", "STILL: ship stores, crates, hold", "WATER · FOOD · FUEL RUNNING SHORT", "REPORTED · IMO, Apr 2026", "")),
("P2-02", ("P2-02b",
 "Look closer at that number. About eight hundred and fifty-seven thousand are officers, the people who navigate and run the engines. About a million are ratings, the deckhands, cooks, oilers and cleaners who keep a ship alive. And every year, about half a million Filipinos deploy to sea. For their families, that pay packet travels home every month.",
 "F39 F28", "GRAPHIC: crew manifest", "857,540 OFFICERS · 1,035,180 RATINGS", "VERIFIED · ICS", "")),
("P2-04", ("P2-04c",
 "Put that next to your own week. Twenty-three dollars is less than a full tank of petrol in America. It's less than a week's food shop for most families in Britain. It's the legal floor, and many crews earn more. But the floor is what the law guarantees. And right now, the law is what's failing them.",
 "F37 H5", "GRAPHIC: scale, $23 vs a tank / a shop", "$23 A DAY", "ESTIMATE · our maths from ILO minimum", "")),
("P2-07", ("P2-07b",
 "The transport workers' federation says the deal also brings higher pay inside the danger zone, and double compensation if a seafarer is killed or disabled. Double compensation. That's the price the industry agreed for a life lost in this strait. It tells you how seriously the people who run ships take the risk.",
 "F36", "GRAPHIC: pay slip, danger pay, compensation x2", "DEATH / DISABILITY COMPENSATION ×2", "REPORTED · ITF via Al Jazeera", "")),
("P3-03", ("P3-03b",
 "Look at how fast that count moved. In late April, the IMO had verified twenty-nine attacks and at least ten deaths. Six weeks later, forty-six attacks and fourteen deaths. Every few days, another ship. Every couple of weeks, another family told.",
 "F14 F15", "GRAPHIC: tally, Apr vs Jun", "29 → 46 ATTACKS · 10 → 14 DEAD", "VERIFIED · IMO", "")),
("P3-11", ("P3-11b",
 "There's a number from before this war that's hard to say out loud. In 2024, the UN's labour agency recorded four hundred and forty-nine seafarer deaths. Twenty-six of them were suicides. That was a normal year. Nobody has a count for this one yet. If you work at sea and you're struggling, help is listed at the end of this video.",
 "F38", "STILL (shadow): empty deck at night", "", "REPORTED · ILO via The National", "")),
("P4-04", ("P4-04b",
 "Washington agreed to reflag the tankers in March 1987. The escorts ran from July 1987 to September 1988, more than a year of warships walking tankers through the Gulf. It worked for the ships flying the American flag. It did not make the water safe for everyone else.",
 "F57", "GRAPHIC: map, escort dates", "JUL 1987 → SEP 1988", "VERIFIED", "")),
("P5-05", ("P5-05b",
 "Some ships are moving. Bahri, the Saudi tanker company, says it is sending tankers through Hormuz in coordination with the US military. Its ship management chief put it simply. We have to keep moving the energy. So the real question is who gets an escort, and who doesn't.",
 "F05", "VIDEO: tanker under way", "ESCORTED TANKERS ARE MOVING", "REPORTED · Bloomberg", "")),
("P5-07", ("P5-07b",
 "Hapag-Lloyd, the German line, put its extra cost at fifty to sixty million euros a week. Those numbers don't stay with the shipping lines. They come back as surcharges, lines on invoices most of us never see, until they show up in the price of things we do.",
 "F52", "GRAPHIC: ledger book entries", "€50-60M A WEEK", "REPORTED · Lloyd's List", "")),
("P5-09d", ("P5-09d2",
 "Meanwhile, the US has three aircraft carriers in the region. Iran's Revolutionary Guards say their forces are at the ready. So while the diplomats talk, the warships stay. And so do the crews.",
 "F66", "VIDEO: aircraft carrier at sea", "3 US CARRIERS IN THE REGION", "REPORTED · Al Jazeera", "")),
("P6-06", ("P6-06b",
 "And when ships are abandoned, the same countries pay again. In the transport workers' count for 2025, Indian seafarers were eighteen percent of all abandonment cases. The same crews carry the risk twice. Once in the water, and once when the money stops.",
 "F43", "GRAPHIC: donut 18%", "INDIANS: 18% OF ABANDONMENT CASES", "VERIFIED · ITF", "")),
("P3-01", ("P3-01b",
 "This part is about people, so here's how we count. We use the IMO's numbers first, because it's the UN agency that checks each death. Where others say more, we tell you, and we label it a claim. Where counts disagree, we show both.",
 "F17 F27", "GRAPHIC: typed cards, how we count", "", "", "")),
("P6-01", ("P6-01b",
 "This is where the strait meets your kitchen table. We'll go country by country. America, then Britain, then South Asia and the Philippines, where the bill isn't a price at all. Every one of these is an estimate, and we'll show the maths.",
 "H1-H6", "GRAPHIC: roadmap, US · UK · South Asia", "", "", "")),
("P6-09", ("P6-09b",
 "Add it up, and this bill has two halves. One half is money. Small per household, spread across billions of people. The other half is time and lives. Huge per person, carried by a few thousand crews. One half shows up on your receipt. The other half never will, unless someone writes it down.",
 "H1-H6 F17 F21", "GRAPHIC: two halves", "", "", "")),
]
R = []
_ins = {}
for after, row in INSERT: _ins.setdefault(after, []).append(row)
for r in _v1["R"]:
    R.append(r); R.extend(_ins.get(r[0], []))
