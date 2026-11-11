# INV-010 Nvidia spy scandal: script v1 source. Run: python3 script_v1.py -> md in videos/INV-010-nvidia-spy/
# Each row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# Visual codes as INV-009 (kit.py / kit2.py). Grade: [SHADOW] [CALM] [COLOUR] [INTENSE].
# Legal: no charges reported against anyone. Every claim about a named person is attributed.
import os, re
VID = "INV-010"
PARTS = []

def part(title, start, rows):
    PARTS.append((title, start, rows))

part("Cold open", "0:00", [
("CO-01", "The most valuable chip company on Earth has just admitted its CEO had an affair. American intelligence officials believe the woman was working for China.", "F06 F01",
 "D document: a recreated staff-memo page (no logo), the line 'I was unfaithful' highlighted; red pen circle. Then a typed card: 'US OFFICIALS BELIEVE...' stamp REPORTED.", "NOV 8, 2026 · THE MEMO", "REPORTED · NYT, Oct 29 2026; AP, Nov 8 2026", "paper slide, pen scratch"),
("CO-02", "This is the Nvidia spy scandal. And at one point on Monday the ninth of November, it had wiped nearly four hundred billion dollars off the company.", "F16",
 "N ledger number: -$400,000,000,000 counts down fast; stock line falls behind it.", "NVIDIA SPY SCANDAL · ≈ -$400BN · NOV 9", "REPORTED · Bloomberg via TNW", "ticker rattle, sub hit"),
("CO-03", "If you have a pension or a 401(k) in an index fund, some of that was yours. About seven cents of every dollar in an S&P 500 fund sits in this one company. On an average 401(k), that's around ten thousand dollars.", "F18 F32 H1 H4",
 "Coin graphic: a dollar splits, 7 cents turn green with NVDA; then ledger number ≈ $10,000; 2 s flash of the final Receipt.", "7¢ OF EVERY $1 · ≈ $10,000 IN AN AVERAGE 401(k)", "REPORTED · SPDR via Decrypt; Fidelity / ILLUSTRATION · our maths", "receipt printer burst"),
("CO-04", "Nobody has been charged with anything. Nvidia says no secrets were lost. China calls it a smear. We'll show you what's confirmed, what's reported, and what's only suspected.", "F07 F14",
 "T typed card: three tags stamp down in turn: CONFIRMED · REPORTED · SUSPECTED.", "NO CHARGES · NVIDIA DENIES · CHINA DENIES", "", "stamp x3"),
("CO-05", "By the end, you'll see the whole bill. We'll count the money, sit at one dinner in Taipei, open some boxes in Malaysia, follow an investigation that stopped, and come back to your account.", "",
 "Roadmap: five icons light in a row (coins, dinner table, crate, file, receipt).", "THE MONEY · THE DINNER · THE BOXES · THE PROBE · YOUR ACCOUNT", "", "riser"),
])

part("Part 1: The $400 billion morning", "~1:00", [
("P1-01", "Part one. The four hundred billion dollar morning.", "", "P part card PART 1 · THE $400 BILLION MORNING", "PART 1 · THE $400 BILLION MORNING", "", "reverse cymbal + sub drop"),
("P1-02", "Sunday, the eighth of November 2026. Jensen Huang, the man who co-founded Nvidia in 1993 and has run it ever since, sends a memo to his staff. He says he was unfaithful to his wife.", "F06 F24",
 "STILL [CALM] Ken Burns: Nvidia headquarters exterior in Santa Clara (Wikimedia, licence logged); paper label.", "SUN 8 NOV 2026", "REPORTED · AP; Al Jazeera", "low drone"),
("P1-02b", "In thirty-three years, he took Nvidia from a graphics-card start-up to the company whose chips nearly every AI system on Earth is trained on. He's one of the most recognisable business leaders in the world, and he's never been accused of a crime.", "F24",
 "Timeline strip: 1993 FOUNDED → GAMING CARDS → AI DATA CENTRES → 2026; leather-jacket silhouette (cut-paper, not a photo).", "1993 → 2026", "REPORTED · Decrypt", "tick x4"),
("P1-03", "The same day, Nvidia's board opens an independent investigation. Not into the affair. Into whether its CEO was the target of a foreign intelligence operation.", "F07",
 "X folder: an index card types INDEPENDENT REVIEW · FOREIGN INTELLIGENCE?", "BOARD PROBE OPENED", "REPORTED · Nvidia board via Al Jazeera", "typewriter"),
("P1-04", "The board says it has no reason to believe national security or company secrets were compromised. It says it still has confidence in him.", "F07",
 "D document: board statement page; 'no reason to believe' highlighted.", "'NO REASON TO BELIEVE'", "REPORTED · Nvidia board", "pen scratch"),
("P1-05", "Monday morning, the market opens. The S&P 500 goes up. Nvidia goes down. At its worst, about nine percent. Close to four hundred billion dollars of value, gone at one point in a few hours.", "F16 F18",
 "W mini-chart tiles: S&P 500 tile green +1.5%, NVDA tile red -8.8%.", "S&P 500 ▲ · NVDA ▼ 8.8% AT THE LOW", "REPORTED · Bloomberg; Decrypt", "tick, then sub hit"),
("P1-06", "To put that in size. Four hundred billion dollars is more than the whole yearly economy of most countries on Earth. It vanished on a memo about a marriage.", "F16",
 "L footage [SHADOW]: trading screens, red numbers, no faces.", "≈ $400BN IN HOURS", "REPORTED · Bloomberg", "low pulse"),
("P1-07", "And it came on top of a bad month. From early October to early November, Nvidia had already lost about one point three trillion dollars of value, in a wider sell-off of AI stocks.", "F17",
 "Stock line chart (kit2 one-off: falling stair line) from $5.78T on Oct 6 to $4.51T on Nov 6.", "$5.78T → $4.51T · OCT 6 - NOV 6", "REPORTED · YCharts via Decrypt", "slide down"),
("P1-07b", "That's a company that took in about two hundred and sixteen billion dollars of revenue in its last full year, and kept about a hundred and twenty billion of it as profit. More than nine in every ten dollars came from data centres, the warehouses where AI is trained.", "F37",
 "B split-flap: REVENUE $215.9BN · PROFIT ≈ $120BN · FY2026.", "$215.9BN REVENUE · ≈ $120BN PROFIT", "VERIFIED · Nvidia results via The Register", "split-flap clatter"),
("P1-08", "Why does any of this touch you? Because Nvidia isn't just a company. It's about seven percent of the S&P 500, the index most pensions and 401(k)s follow.", "F18 F19",
 "Pie of the S&P 500: Nvidia slice 6.93% lifts out; next to it the Magnificent Seven ring ≈ 30%.", "NVIDIA 6.93% OF THE S&P 500 · BIG 7 ≈ 30%", "REPORTED · SPDR via Decrypt; Yardeni via Fortune", "fill swell"),
("P1-09", "More than half of American households have a 401(k). And most of them sit in target-date funds that buy companies by size. The bigger Nvidia gets, the more of your money goes into it, automatically.", "F20",
 "K cut-paper figures: a row of houses, 54% light up; arrow from each into one big NVDA box.", "54% OF US HOUSEHOLDS HAVE A 401(k)", "REPORTED · Federal Reserve via Fortune", "paper slide x3"),
("P1-10", "Fidelity says the average 401(k) holds about a hundred and forty-four thousand dollars. If all of that tracked the S&P 500, about ten thousand would be Nvidia. At the worst point of that Monday, that slice was down about eight hundred and eighty dollars.", "F32 H1 H2",
 "N ledger number: $144,400 → $10,000 slice → -$880 in red.", "≈ $10,000 SLICE · ≈ -$880 AT THE LOW", "REPORTED · Fidelity Q3 2025 / ILLUSTRATION · our maths", "sub hit"),
("P1-11", "In Britain and across the world it's the same story. Global index funds hold Nvidia as their single biggest company. You don't have to buy one share to own a piece of this scandal.", "F36",
 "M navy map: world, dots light on UK, Canada, Australia; each dot labels 'NVDA = No.1 HOLDING'.", "NVIDIA ≈ 5% OF THE GLOBAL INDEX", "REPORTED · MSCI ACWI via Crypto Briefing (verify)", "pin drops x3"),
("P1-12", "So who is the woman at the centre of all this? And how did she end up at the CEO's table?", "",
 "Push in on an empty chair at a dinner table (cut-paper).", "", "", "riser"),
])

part("Subscribe bridge", "~4:00", [
("BR-01", "If you want to see every line of a bill like this before it lands in your account, subscribe. Next, we follow it from the boardroom to your pension statement.", "",
 "Paper card with the channel's running invoice; end-screen tile of INV-009 Taiwan 2027.", "SUBSCRIBE · EVERY CRISIS SENDS A BILL", "", "soft tick"),
])

part("Part 2: The dinner in Taipei", "~4:15", [
("P2-01", "Part two. The dinner in Taipei.", "", "P part card PART 2 · THE DINNER IN TAIPEI", "PART 2 · THE DINNER IN TAIPEI", "", "reverse cymbal + sub drop"),
("P2-02", "Her name is Alice Huang, also known as Huang Le. She's a Chinese citizen. She is not related to Jensen Huang. They only share a surname.", "F01",
 "T typed card (dossier, no photo): NAME · HUANG LE ('ALICE') · CHINESE CITIZEN · NOT RELATED.", "ALICE HUANG (HUANG LE)", "REPORTED · NYT; Al Jazeera", "typewriter"),
("P2-03", "In March 2023, a Singapore company called 7Road International changed its name to Megaspeed. Filings show she became a managing director. Megaspeed builds the computing power that AI runs on.", "F27",
 "D document: recreated Singapore filing card; '7ROAD → MEGASPEED · MAR 2023' highlighted.", "7ROAD → MEGASPEED · MAR 2023", "REPORTED · Singapore filings via Open Magazine", "pen scratch"),
("P2-04", "In June 2024, she was photographed beside Jensen Huang at a tech gathering in Taipei. Every year, the chip world flies there for a trade show called Computex.", "F28",
 "STILL [COLOUR] Ken Burns: Taipei skyline with Taipei 101 at dusk; paper label.", "TAIPEI · JUNE 2024", "REPORTED · Open Magazine", "city air"),
("P2-05", "On the twenty-second of May 2025, during Computex, he hosted a dinner in Taipei. Reports say she was there too.", "F05",
 "Calendar card (kit2 one-off: menu card): 22 MAY 2025 · DINNER · TAIPEI.", "22 MAY 2025 · THE DINNER", "REPORTED · Al Jazeera", "glass clink (soft)"),
("P2-05b", "For a chip boss, that's an ordinary night. Customers, suppliers and partners all want a seat at his table. Nvidia says meetings like that are not unusual, and Megaspeed was a customer.", "F13",
 "Cut-paper figures: a long table with many empty chairs, name cards face down.", "'NOT UNUSUAL'", "CLAIM · Nvidia via NYT", "glass clink (soft)"),
("P2-05c", "But US officials weren't watching him. According to the Times, they were watching her. And surveillance of her showed a close relationship with Nvidia's CEO.", "F02",
 "Lights dim on the table; a single orange spotlight falls on one chair.", "THEY WERE WATCHING HER", "REPORTED · NYT", "low pulse"),
("P2-06", "Then, on the twenty-ninth of October 2026, the New York Times published what US officials had concluded. That she was a Chinese intelligence asset, passing information back to Beijing.", "F01",
 "D document: recreated headline card credited 'The New York Times, Oct 29 2026'; key words circled.", "NYT · OCT 29, 2026", "REPORTED · NYT", "paper slide"),
("P2-07", "The Times and the Financial Times reported that China's Ministry of State Security had recruited her, to gather information on Jensen Huang, and possibly to steer Nvidia's chip sales to China.", "F29",
 "M navy map: line from Beijing to Taipei to Santa Clara draws in red thread; one 'MSS?' tag.", "'TO GATHER INFORMATION' · 'POSSIBLY INFLUENCE SALES'", "REPORTED · NYT; FT", "string twang"),
("P2-08", "What did she learn? Nobody outside the intelligence services knows. The report says it's unclear what she passed on, or what it was worth. And her whereabouts are unknown.", "F02",
 "X folder: three index cards stamped UNKNOWN: WHAT SHE LEARNED · WHAT IT WAS WORTH · WHERE SHE IS.", "THREE UNKNOWNS", "REPORTED · NYT; Al Jazeera", "stamp x3"),
("P2-09", "Singapore says it never investigated her. But its police confirm they are investigating Megaspeed. China's foreign ministry calls the whole story an unsubstantiated smear.", "F30 F14",
 "Two typed cards side by side: SINGAPORE · 'NO SUCH INVESTIGATION' / CHINA · 'SMEARS'.", "SINGAPORE · CHINA RESPOND", "REPORTED · Open Magazine; TNW", "stamp x2"),
("P2-10", "Now, this isn't the first time a story like this has been told. History has a name for it.", "",
 "Lights-out beat: frame dims for 1 s.", "", "", "pause, low note"),
])

part("Part 3: History keeps the receipts", "~7:00", [
("P3-01", "Part three. The oldest trick in the file.", "", "P part card PART 3 · THE OLDEST TRICK", "PART 3 · THE OLDEST TRICK", "", "reverse cymbal + sub drop"),
("P3-02", "Spy agencies call it cultivation. You build a relationship with someone close to power, and you wait. Sometimes it's a friendship. Sometimes it's more. The tabloids call it a honeypot.", "",
 "X folder: index card types CULTIVATION; a second card underneath reads 'HONEYPOT' in pencil.", "CULTIVATION", "", "typewriter, pencil"),
("P3-03", "In December 2020, Axios reported that a suspected Chinese operative called Christine Fang had spent years building ties with American local politicians, including helping raise money for a congressman. He was never accused of wrongdoing.", "F34",
 "D document: recreated Axios headline card credited 'Axios, Dec 2020'; 'not accused' highlighted.", "AXIOS · DEC 2020", "REPORTED · Axios (verify)", "paper slide"),
("P3-04", "In January 2022, Britain's MI5 took the rare step of warning Parliament about a London lawyer, Christine Lee. It said she was acting for a Chinese Communist Party influence department.", "F35",
 "STILL [SHADOW] Ken Burns: Palace of Westminster at night (no faces).", "MI5 ALERT · JAN 2022", "REPORTED · MI5 via BBC (verify)", "Big Ben-style low bell (soft)"),
("P3-05", "Those were politicians. This time, officials believe the target was a businessman. But not just any businessman. The man who decides who gets the chips that power artificial intelligence.", "F04",
 "Three cut-paper figures in a row: POLITICIAN · POLITICIAN · CHIP CEO; the third lights up orange.", "THIS TIME: A CHIP CEO", "", "sub hit"),
("P3-06", "And here's what makes it different from every case before it. American officials told the President about this a year ago.", "F03",
 "Split-flap: OCT 2025 · PRESIDENT BRIEFED.", "OCT 2025 · BRIEFED", "REPORTED · NYT", "split-flap clatter"),
("P3-07", "According to the Times, the President chose not to act, reportedly wary of disrupting chip sales and trade with China. Jensen Huang himself was never given the formal warning officials call a defensive briefing.", "F03 F04",
 "D document: recreated NYT paragraph; 'chose not to act' highlighted, red pen circle.", "'CHOSE NOT TO ACT'", "REPORTED · NYT", "pen scratch"),
("P3-07b", "When the President was first told, officials reportedly didn't believe Jensen Huang knew who she was. The Times says some senior officials now doubt that. Nvidia's board says it has seen nothing to suggest secrets were lost.", "F04 F07",
 "Two index cards: THEN · 'HE DIDN'T KNOW' / NOW · 'SOME DOUBT IT'.", "THEN vs NOW", "REPORTED · NYT; Nvidia board", "card flip"),
("P3-08", "On the eighth of November, the President defended him. He called him an honourable guy, said he hadn't heard he'd done anything wrong, and said he'd still take him on his trip to China.", "F15",
 "Typed quote card: 'I HAVEN'T HEARD HE'S DONE ANYTHING WRONG' · NOV 8 2026.", "'HONOURABLE GUY'", "REPORTED · TNW; Al Jazeera", "typewriter"),
("P3-09", "So why would a spy service care about one company's sales? To answer that, you have to open some boxes.", "",
 "Push to a stack of shipping crates in the dark.", "", "", "riser"),
])

part("Part 4: The boxes in Malaysia", "~9:30", [
("P4-01", "Part four. The boxes in Malaysia.", "", "P part card PART 4 · THE BOXES IN MALAYSIA", "PART 4 · THE BOXES IN MALAYSIA", "", "reverse cymbal + sub drop"),
("P4-02", "Nvidia's best chips are the engines of the AI race. America bans its very top chips, the Blackwell line, from being sold to China.", "F25",
 "L footage [COLOUR]: server racks with blinking lights in a data centre, slow dolly; paper label.", "BLACKWELL: BANNED FOR CHINA", "REPORTED · Al Jazeera", "server hum"),
("P4-03", "In December 2025, the President allowed sales of an older chip, the H200, about six times more powerful than the one China could buy before. Washington takes a twenty-five percent cut of certain sales.", "F25",
 "N ledger number: H20 → H200 = ×6; then '25% TO WASHINGTON' on a beige tag.", "H200 ≈ 6× H20 · 25% CUT", "REPORTED · Al Jazeera; NYT", "sub hit"),
("P4-03b", "China matters to Nvidia, but less than it used to. In the summer of 2026, its first H200s shipped to China, and they made up less than one percent of eighty-nine billion dollars of data-centre sales. Nvidia's next forecast assumed no Chinese data-centre money at all.", "F38 F39",
 "W mini-chart tiles: DATA CENTRE $89BN tile; a thin sliver labelled CHINA H200 < 1%.", "CHINA H200 < 1% OF $89BN", "REPORTED · TNW, Aug 2026", "tick"),
("P4-04", "So every top chip that reaches China by the back door is worth a fortune. And that's where Megaspeed comes in.", "",
 "M navy map: Singapore and Malaysia glow; a dotted line hints north to China.", "", "", "whoosh"),
("P4-05", "In late 2024, an American official visited a data centre in Malaysia and saw Nvidia equipment still sitting in its boxes. That visit started a Commerce Department investigation.", "F08",
 "L footage [SHADOW]: warehouse aisle of sealed boxes, low light, no faces.", "MALAYSIA · LATE 2024 · STILL IN THE BOX", "REPORTED · NYT", "low drone"),
("P4-06", "Trade records show a Megaspeed sister company in Malaysia bought at least four point eight billion dollars of AI equipment with Nvidia chips inside, between June 2024 and February 2026.", "F09 F31",
 "B split-flap board flips to $4.8 BN · JUN 2024 - FEB 2026.", "≥ $4.8BN OF NVIDIA-CHIP EQUIPMENT", "REPORTED · ImportGenius via NYT", "split-flap clatter"),
("P4-07", "That's purchases, not proof that anything was smuggled. But the Times reports Megaspeed rents computing power to Chinese firms, mainly Alibaba, and buys some equipment through the American arm of a Chinese server maker whose parent is blacklisted.", "F10 F31",
 "Flow diagram (kit2 one-off: three linked crates): INSPUR US ARM → MEGASPEED → RENTED TO ALIBABA (dotted).", "PURCHASES ≠ PROOF", "REPORTED · NYT", "string twang x2"),
("P4-08", "Megaspeed denies smuggling. Nvidia says it's like any regional customer, that earlier smuggling claims were checked and debunked, and that it follows the law. Nvidia still lists Megaspeed as a cloud partner.", "F13",
 "Two typed cards: MEGASPEED · 'NO SMUGGLING' / NVIDIA · 'LIKE ANY REGIONAL CUSTOMER'.", "BOTH DENY", "CLAIM · Megaspeed; Nvidia", "stamp x2"),
("P4-09", "Here's the half-receipt so far. Nearly four hundred billion off the company in a morning. About ten thousand dollars of an average 401(k) riding on it. And almost five billion dollars of chips in the question.", "F16 H1 F09",
 "R half-receipt prints three lines.", "SO FAR · ≈ $400BN · ≈ $10K · ≈ $4.8BN", "", "receipt print x3"),
("P4-10", "And then the investigation into those boxes stopped.", "", "A file closing on its own (cut-paper).", "", "", "file thud"),
])

part("Part 5: The probe that stopped", "~12:00", [
("P5-01", "Part five. The probe that stopped.", "", "P part card PART 5 · THE PROBE THAT STOPPED", "PART 5 · THE PROBE THAT STOPPED", "", "reverse cymbal + sub drop"),
("P5-02", "For months, agents at the Bureau of Industry and Security, the part of the Commerce Department that polices chip exports, worked the Megaspeed case.", "F11",
 "X folder: CASE FILE · MEGASPEED · BIS; index cards slide in.", "COMMERCE · BIS · MEGASPEED FILE", "REPORTED · NYT via TNW", "paper slide"),
("P5-03", "In August 2025, according to the Times, Nvidia's top lawyer emailed those agents. He said a senior Commerce official had approved him reaching out.", "F11",
 "D document: recreated email card (no real addresses): 'approved the outreach' highlighted.", "AUG 2025 · THE EMAIL", "REPORTED · NYT", "keyboard clicks"),
("P5-04", "The agents refused to meet. They sent the emails up the chain. Later, the Justice Department asked Commerce to pause its work, and Commerce did. The case is reported to be a criminal inquiry now.", "F11",
 "Timeline strip (kit2 one-off: relay baton): EMAIL → REFUSED → DOJ: PAUSE → CRIMINAL INQUIRY?", "PAUSED · MOVED TO DOJ", "REPORTED · NYT via TNW", "tick x4"),
("P5-05", "Commerce says it handled everything strictly by the book. Nvidia says it talks to officials to answer questions and share what it sees in the field.", "F11",
 "Two typed cards: COMMERCE · 'BY THE BOOK' / NVIDIA · 'WE ANSWER QUESTIONS'.", "BOTH SAY: BY THE BOOK", "CLAIM · Commerce; Nvidia", "stamp x2"),
("P5-06", "One more number. Other agencies proposed putting Megaspeed on the government's blacklist of companies. It hasn't happened. In fact, Commerce hasn't added a single company to that list in over a year.", "F12",
 "N ledger number: ENTITY LIST ADDITIONS · LAST 12 MONTHS: 0.", "0 ADDED IN 12+ MONTHS", "REPORTED · TNW", "sub hit, silence"),
("P5-06b", "Officials quoted by the Times say the close relationship between the President and Jensen Huang has stalled some investigations and proposed sanctions at Commerce. The White House declined to comment on the report.", "F41",
 "D document: recreated NYT paragraph; 'stalled' highlighted, red pen circle.", "'STALLED'", "REPORTED · NYT via GV Wire", "pen scratch"),
("P5-07", "Now it's in the open. On the ninth of November, shareholders filed a proposed class action, saying Nvidia and its CEO hid his ties to a suspected spy.", "F21",
 "D document: recreated court-filing card 'PROPOSED CLASS ACTION · NOV 9 2026'.", "SHAREHOLDER SUIT · NOV 9", "REPORTED · Reuters", "stamp"),
("P5-08", "In Congress, three House committee chairs want a closed-door briefing on the eighteenth of November. Senator Elizabeth Warren is demanding answers and tighter export laws.", "F22 F23",
 "STILL [CALM] Ken Burns: US Capitol dome, daylight.", "CONGRESS · NOV 18", "REPORTED · Open Magazine; Al Jazeera", "low swell"),
("P5-09", "And the day before that, Nvidia reports its quarterly results. Two dates, back to back, that will move the money in your fund.", "F22",
 "Calendar card: 17 NOV RESULTS · 18 NOV CONGRESS.", "17 NOV · 18 NOV", "REPORTED · TNW; Decrypt", "tick x2"),
("P5-10", "So what happens to your account from here?", "", "Push to a pension statement on a kitchen table (cut-paper).", "", "", "riser"),
])

part("Part 6: What happens next", "~14:30", [
("P6-01", "Part six. What happens next.", "", "P part card PART 6 · WHAT HAPPENS NEXT", "PART 6 · WHAT HAPPENS NEXT", "", "reverse cymbal + sub drop"),
("P6-02", "Path one. The review clears him, and he stays. That's what the board and the President both say they want. Analysts say Nvidia has no obvious successor. One called him not replaceable.", "F24 F15",
 "Three-door graphic (kit2 one-off): door 1 lights: STAYS.", "PATH 1 · HE STAYS", "REPORTED · Decrypt (Dan Ives)", "door creak (soft)"),
("P6-03", "Path two. He leaves. Jensen Huang is sixty-three and has run the company for more than thirty years. One market strategist said a departure could mean an absolute bloodbath for the shares.", "F24",
 "Door 2 lights: LEAVES; the stock line behind it drops.", "PATH 2 · HE LEAVES", "REPORTED · Decrypt (Chris Weston)", "sub hit"),
("P6-03b", "Why would one man matter so much? Because he holds the biggest customer relationships, the supplier deals in Taiwan, and the phone line to Washington. Analysts say he built the company around himself.", "F24",
 "Web diagram (kit2 one-off: hub and spokes): centre HUANG; spokes CUSTOMERS · TSMC · WASHINGTON.", "ONE MAN, THREE LINES", "REPORTED · Decrypt", "string twang x3"),
("P6-04", "Nobody can tell you which path. These are scenarios, not forecasts. But the more of your fund sits in one company, the more one man's private life becomes your business.", "",
 "T typed card: SCENARIOS, NOT FORECASTS.", "SCENARIOS, NOT FORECASTS", "SCENARIO", "stamp"),
("P6-05", "Path three is the slow one. Washington tightens the rules on who can buy these chips, and where they end up. Every extra check adds cost and delay. And the AI companies who pay for the chips pass those costs on.", "F23 F25",
 "Door 3 lights: TIGHTER RULES; a toll gate graphic drops across a chip conveyor.", "PATH 3 · TIGHTER RULES", "REPORTED · Al Jazeera (analysts)", "gate slam"),
("P6-05b", "You can already see where that ends. Nvidia has told its customers server prices will rise by more than fifteen percent from early 2027. Those servers run the chatbots, the cloud storage and the apps many of us now pay for every month.", "F40",
 "L footage [COLOUR]: phone on a kitchen table showing a generic subscription screen (no brand); price tag +15% slides on.", "SERVERS +15% · EARLY 2027", "REPORTED · TNW, Aug 2026", "price tag click"),
("P6-05c", "That rise was announced before any of this scandal. Tighter rules would only add to it. It's a small line on your bill, but it arrives every month.", "F40",
 "N ledger number: +15% then a small '+?' tag beside it.", "+15% ... AND RISING?", "SCENARIO", "sub hit"),
("P6-06", "And here's the part no model prices. If officials are right, a foreign service got close to the man who decides where the world's most wanted chips go. And the people told about it a year ago chose to wait.", "F01 F03",
 "STILL [SHADOW] Ken Burns: an empty boardroom at night, city lights through glass.", "THE PART NO MODEL PRICES", "REPORTED · NYT", "quiet piano note"),
("P6-07", "And let's be honest about what nobody knows. What, if anything, she learned. Whether he knew who she was. Whether any chips really reached China. And whether anyone will ever be charged.", "F02 F04 F31",
 "X folder: four index cards stamped UNKNOWN, one by one.", "FOUR THINGS NOBODY KNOWS", "", "stamp x4"),
("P6-08", "So, line by line, what does it come to in your account?", "", "Receipt printer warms up.", "", "", "riser"),
])

part("The Receipt", "~17:00", [
("RC-01", "The Receipt. The Nvidia spy scandal, for an example saver with an average 401(k). These are illustrations, not forecasts.", "",
 "R receipt prints: header THE RECEIPT · THE NVIDIA SPY SCANDAL.", "THE RECEIPT · ILLUSTRATION", "ILLUSTRATION", "receipt printer"),
("RC-02", "Line one. Your Nvidia slice. About seven cents of every dollar in an S&P 500 fund. On an average 401(k), about ten thousand dollars.", "F18 F32 H1",
 "R line 1.", "YOUR SLICE · ≈ $10,000", "ILLUSTRATION · our maths", "receipt print"),
("RC-03", "Line two. One bad morning. At the low on the ninth of November, about eight hundred and eighty dollars off that slice.", "F16 H2",
 "R line 2.", "ONE MORNING · ≈ -$880 AT THE LOW", "ILLUSTRATION · our maths", "receipt print"),
("RC-04", "Line three. The chip trail. Four point eight billion dollars of equipment under question. Your cost: not known yet.", "F09",
 "R line 3; cost cell reads 'NOT KNOWN'.", "THE CHIP TRAIL · $4.8BN · COST NOT KNOWN", "REPORTED · NYT", "receipt print"),
("RC-04b", "Line four. Your subscriptions. Nvidia's servers rise more than fifteen percent from early 2027. How much reaches your phone bill or your cloud plan: not priced yet.", "F40",
 "R line; price cell 'NOT PRICED'.", "YOUR APPS · SERVERS +15% · NOT PRICED", "REPORTED · TNW", "receipt print"),
("RC-05", "Line five. The dates to watch. The seventeenth of November, results. The eighteenth of November, Congress.", "F22",
 "R line 4 with two dates; stamp WATCH.", "WATCH · 17 NOV · 18 NOV", "REPORTED", "receipt print + stamp"),
("RC-06", "What can you do? This is not financial advice. But a few things make sense in any market. Open your pension statement and see how much sits in the biggest five or ten companies. You might be surprised.", "",
 "X folder + index cards: CHECK YOUR TOP 10 HOLDINGS.", "NOT FINANCIAL ADVICE", "", "card slide"),
("RC-07", "If you're close to retirement, ask your provider what your fund does when one giant falls. And don't trade on headlines. A memo can move a market in a morning, and a board statement can move it back.", "",
 "Index cards: ASK YOUR PROVIDER · DON'T TRADE HEADLINES.", "", "", "card slides x2"),
("RC-08", "Tell us in the comments. Should one company be this big a part of everyone's retirement? And where are you watching from?", "",
 "Comment prompt card; end screen to INV-009 Taiwan 2027.", "SHOULD ONE COMPANY BE THIS BIG?", "", "riser air"),
("RC-09", "Somewhere, a woman whose whereabouts are unknown may hold the answer. Until then, the bill is already in your account. Every crisis sends a bill. History keeps the receipts.", "F02",
 "Return to the empty dinner chair; slow fade to black; tagline in plain type.", "EVERY CRISIS SENDS A BILL. HISTORY KEEPS THE RECEIPTS.", "", "silence, then one low note"),
])

def words(t): return len(re.findall(r"[A-Za-z0-9'’.\-]+", t))

def build():
    out = []
    total = sum(words(r[1]) for _, _, rows in PARTS for r in rows)
    out.append(f"# {VID} The Nvidia spy scandal: script v1\n")
    out.append("v1, 2026-11-11. Search phrase: **Nvidia spy scandal** (spoken in CO-02 at ~0:10, again in RC-01). Lead title: **Nvidia's Spy Scandal Just Hit Your Pension** (43 chars).\n")
    out.append(f"Narration: **{total} words, about {total/132:.0f} minutes** of voice at 132 wpm; with part cards and pauses the cut runs about {total/132+1.5:.0f}-{total/132+2.5:.0f} min. Every number points to a row in `facts.md` (F = fact, H = household maths). No charges have been reported against anyone: every claim about a named person is attributed ('according to', 'officials believe', 'reported').\n")
    out.append("Visual key: N ledger number · L footage + paper label · D document (highlight + red pen, never a magnifier) · T typed card + stamp · B split-flap · K cut-paper figures · M navy map · P part card · R receipt · W mini-chart tiles · X folder + index cards · 'kit2 one-off' = a new type for this video. Footage/stills grade in brackets: [SHADOW] [CALM] [COLOUR] [INTENSE]. All graphics on the dark ledger background, beige cards, colour shots at x0.8 brightness. No photos of Alice Huang or Jensen Huang (rights + fairness): dossier cards and buildings instead.\n")
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
    dst = "/mnt/project-files/the-history-invoice/videos/INV-010-nvidia-spy/INV-010-nvidia-spy-script-v1.md"
    open(dst, "w").write(md + "\n\n" + extra)
    print(total)
