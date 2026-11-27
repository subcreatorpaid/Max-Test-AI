# INV-023 The Last Time Iran Shut the Oil: 1979. Script v1 source (27 Nov 2026).
# Row: (code, narration, facts, visual, on_screen, tag_source, sfx)
# {curly} words are SYNC CUES (braces stripped for the voice). Visual kinds: G graphic (spec23) · F clip · S photo.
# Iran follow-up series #6 (history): answer + number inside 30 s, subscribe ask ~4 min, end screen back to the hit video.
import os
VID = "INV-023"
PARTS = []
def part(title, start, rows): PARTS.append((title, start, rows))
CORNER = {"P1": "1978: 6M → 1.5M BPD", "P2": "SUPPLY -4% · PANIC", "P3": "$15.85 → $39.50", "P4": "UK INFLATION 22%",
          "P5": "RATES 20%", "P6": "1986: < $10"}

part("Cold open", "0:00", [
("CO-01", "In November 1978, thirty-seven thousand oil workers in Iran walked off the job. In days, the country's output fell from about six million barrels a day to about one and a {half}.", "E01",
 "G ladder: 6M BPD → 1.5M BPD; kicker NOV 1978", "6M → 1.5M BARRELS A DAY", "VERIFIED · Wikipedia (Time, 13 Nov 1978)", "sub hit"),
("CO-02", "Within a year and a half, the price of oil had gone from under sixteen dollars a barrel to nearly {forty}.", "E05",
 "G ladder: $15.85 → $39.50", "$15.85 → $39.50", "VERIFIED · Wikipedia", "whoosh"),
("CO-03", "Americans queued for hours to buy petrol. Inflation in Britain hit twenty-two percent. And American interest rates went to {twenty}.", "E06 E25 E20",
 "G three number cards: QUEUES · UK INFLATION 22% · US RATES 20%", "QUEUES · 22% · 20%", "VERIFIED · Wikipedia", "stamp thud"),
("CO-04", "That's the last time Iran's oil stopped flowing. This year, it's stopped again. Under a US blockade, Iran's exports have effectively {ceased}.", "E29",
 "G split: 1978 · STRIKES | 2026 · BLOCKADE", "1978 · 2026", "REPORTED · Wikipedia", "glitch"),
("CO-05", "So here's the short answer to what 1979 teaches us about your bill. The shortage was small. The panic was huge. And the bill lasted for {years}.", "E04",
 "G checklist: SMALL SHORTAGE · HUGE PANIC · BILL FOR YEARS", "SMALL SHORTAGE, LONG BILL", "VERIFIED · Wikipedia", "pen"),
("CO-06", "Let's open the invoice from 1979, line by line, and see what it says about the one arriving {now}.", "",
 "G roadmap: THE STRIKE · THE PANIC · THE PRICE · BRITAIN · THE LONG BILL · THE LESSON", "THE 1979 INVOICE", "", "riser"),
])

part("Part 1: The strike", "~1:00", [
("P1-01", "Part one. The strike.", "", "G part card PART 1 · THE STRIKE", "PART 1 · THE STRIKE", "", "reverse cymbal + sub drop"),
("P1-02", "In 1978, Iran was ruled by the Shah, and it was one of the biggest oil exporters on {Earth}.", "E01",
 "G map: Iran highlighted; label 1978 · ONE OF THE BIGGEST EXPORTERS", "IRAN, 1978", "VERIFIED · Wikipedia", "map whoosh"),
("P1-03", "That autumn, protests against him spread from the streets into the oil {fields}.", "E02", "G timeline: AUTUMN 1978 · PROTESTS → OIL STRIKES", "PROTESTS REACH THE OIL", "VERIFIED · Wikipedia", "map whoosh"),
("P1-04", "In November, thirty-seven thousand refinery workers went on strike. Output fell to a quarter of its normal {level}.", "E01",
 "G bars: BEFORE 6M · STRIKE 1.5M (barrels a day)", "OUTPUT FELL BY THREE-QUARTERS", "VERIFIED · Wikipedia", "counter"),
("P1-05", "The government sent in navy personnel to keep the oil moving. By the end of the month, output was close to normal {again}.", "E02",
 "G bars: 1.5M climbs back toward 6M; label NAVY SENT IN", "BACK TO NORMAL... BRIEFLY", "VERIFIED · Wikipedia", "whoosh"),
("P1-06", "It didn't last. The strikes came back and turned into a general strike across the {country}.", "E02", "G card: GENERAL STRIKE", "GENERAL STRIKE", "VERIFIED · Wikipedia", "stamp thud"),
("P1-07", "On the sixteenth of January 1979, the Shah left Iran. On the first of February, Ayatollah Khomeini returned from exile. Ten days later, the monarchy was {gone}.", "E03",
 "G timeline: 16 JAN SHAH LEAVES · 1 FEB KHOMEINI RETURNS · 11 FEB MONARCHY FALLS", "THE SHAH FALLS · FEB 1979", "VERIFIED · Wikipedia", "map whoosh"),
("P1-07b", "A new government was taking over the oil fields in the middle of a revolution. For months, nobody outside Iran knew how much of its oil would come back on the {market}.", "E02 E03",
 "G card: HOW MUCH WILL COME BACK? NOBODY KNEW", "NOBODY KNEW", "ANALYSIS", "glitch"),
("P1-07c", "And in oil markets, not knowing is often more expensive than not {having}.", "", "G card: NOT KNOWING COSTS MORE THAN NOT HAVING", "NOT KNOWING COSTS MORE", "ANALYSIS", "stamp thud"),
("P1-08", "A revolution in one country. But the shock was about to travel to every petrol station in the western {world}.", "", "G chain: IRAN · OIL MARKET · YOUR PUMP", "NEXT STOP: YOUR PUMP", "", "riser"),
("P1-09", "Running total. Line one. Iran's output, down three-quarters in a {month}.", "", "G running receipt line 1", "LINE 1 · OUTPUT -75%", "", "printer"),
])

part("Bumper", "~3:30", [
("BR-01", "Quick one. This is part six of our Iran War Bill series. If you want the next one, {subscribe}, so you don't miss it.", "",
 "G sub card: 6 OF THE IRAN WAR BILL · SUBSCRIBE", "SUBSCRIBE", "", "soft tick"),
])

part("Part 2: The panic", "~3:45", [
("P2-01", "Part two. The panic.", "", "G part card PART 2 · THE PANIC", "PART 2 · THE PANIC", "", "reverse cymbal + sub drop"),
("P2-02", "Here's the surprising part. Over the whole of 1979, world oil supply fell by only about four {percent}.", "E04",
 "G gauge 4% · OF WORLD SUPPLY LOST, 1979", "SUPPLY FELL ONLY ≈ 4%", "VERIFIED · Wikipedia", "counter"),
("P2-03", "In America, oil sales that year were just three and a half percent below the record set the year {before}.", "E08",
 "G bars: 1978 RECORD 100 · 1979 96.5", "SALES ONLY -3.5%", "VERIFIED · Wikipedia", "whoosh"),
("P2-04", "So why did it feel like the end of the world? Because people {panicked}.", "", "G card: PEOPLE PANICKED.", "PEOPLE PANICKED", "", "stamp thud"),
("P2-05", "At the end of March, a nuclear accident at Three Mile Island in Pennsylvania made Americans even more nervous about energy. Drivers started filling up whenever they {could}.", "E06",
 "G timeline: 28 MAR 1979 · THREE MILE ISLAND → PANIC BUYING", "28 MAR 1979: PANIC BUYING", "VERIFIED · Wikipedia", "map whoosh"),
("P2-06", "Half-full tanks were topped up. Queues formed. And the queues made people panic {more}.", "E06", "G chain: TOP UP · QUEUES · MORE PANIC · LONGER QUEUES", "QUEUES MADE MORE QUEUES", "VERIFIED · Wikipedia", "pen"),
("P2-07", "One estimate says cars idling in those queues burned up to a hundred and fifty thousand barrels of oil a {day}.", "E07",
 "G number card 150,000 · BARRELS A DAY BURNED IN QUEUES", "150,000 BARRELS A DAY IN QUEUES", "ESTIMATE · Wikipedia", "counter"),
("P2-08", "Several states brought in odd-even rationing. If your number plate ended in an odd number, you could fill up on odd days. Even, on even {days}.", "E10",
 "G calendar: odd and even days highlighted; label ODD PLATES · EVEN PLATES", "ODD-EVEN RATIONING", "VERIFIED · Wikipedia", "pen"),
("P2-09", "The federal government even printed ration coupons. They were never {used}.", "E10", "G document card: RATION COUPON · PRINTED · NEVER USED", "COUPONS PRINTED, NEVER USED", "VERIFIED · Wikipedia", "stamp thud"),
("P2-10", "In May, a poll asked Americans whether the shortage was real. Thirty-seven percent said yes. Fifty-four percent said it was a {hoax}.", "E09",
 "G bars: REAL 37% · HOAX 54%", "54% SAID 'HOAX'", "VERIFIED · Wikipedia (AP/NBC poll)", "counter"),
("P2-11", "In July, President Carter went on television and gave what became known as his crisis of confidence {speech}.", "E11",
 "G quote card: 'CRISIS OF CONFIDENCE' · 15 JULY 1979", "15 JULY 1979: THE SPEECH", "VERIFIED · Wikipedia", "pen"),
("P2-11b", "America also had a strange extra problem: price controls. Oil from American wells was held at about six dollars a barrel, while the world price was around thirty. That kept prices down on paper, and made shortages worse in {practice}.", "E27",
 "G two numbers: US CONTROLLED $6 · WORLD $30", "CONTROLLED $6 vs WORLD $30", "VERIFIED · Wikipedia", "stamp thud"),
("P2-11c", "Carter started lifting those controls in April 1979. They were fully gone by January {1981}.", "E05 E27",
 "G timeline: APR 1979 DECONTROL BEGINS · JAN 1981 CONTROLS END", "CONTROLS END · JAN 1981", "VERIFIED · Wikipedia", "map whoosh"),
("P2-12", "A four percent shortage had turned into a national mood. And moods move {prices}.", "E04", "G card: 4% SHORTAGE → NATIONAL MOOD", "MOODS MOVE PRICES", "", "glitch"),
("P2-13", "Running total. Line two. A four percent shortage, a hundred percent {panic}.", "", "G running receipt line 2", "LINE 2 · 4% SHORT, 100% PANIC", "", "printer"),
])

part("Part 3: The price", "~7:00", [
("P3-01", "Part three. The price.", "", "G part card PART 3 · THE PRICE", "PART 3 · THE PRICE", "", "reverse cymbal + sub drop"),
("P3-02", "In April 1979, crude was fifteen dollars and eighty-five cents a {barrel}.", "E05", "G number card $15.85 · APRIL 1979", "$15.85 · APRIL 1979", "VERIFIED · Wikipedia", "counter"),
("P3-03", "Twelve months later, it was thirty-nine fifty. Two and a half times as {much}.", "E05 E31",
 "G ladder: $15.85 → $39.50; bracket ×2.5", "$39.50 · ×2.5", "VERIFIED · Wikipedia", "whoosh"),
("P3-04", "Adjusted for inflation, that stayed the highest oil price ever recorded until {2008}.", "E05", "G card: A RECORD UNTIL 2008 (REAL TERMS)", "RECORD UNTIL 2008", "VERIFIED · Wikipedia", "stamp thud"),
("P3-05", "And then the politics got worse. In November 1979, students seized the American embassy in Tehran. Fifty-two Americans were held for four hundred and forty-four {days}.", "E12 E32",
 "G number card 444 DAYS · 52 HOSTAGES", "444 DAYS", "VERIFIED · Wikipedia", "stamp thud"),
("P3-06", "Carter banned imports of Iranian oil. In January, he declared that any attempt to control the Persian Gulf would be treated as an attack on America's vital {interests}.", "E12",
 "G quote card: THE CARTER DOCTRINE · JAN 1980", "THE CARTER DOCTRINE", "VERIFIED · Wikipedia", "pen"),
("P3-07", "That idea is still with us. It's one reason American warships are in the Gulf {today}.", "E12", "G split: 1980 CARTER DOCTRINE | 2026 US BLOCKADE", "1980 → 2026", "ANALYSIS", "glitch"),
("P3-08", "Then, in September 1980, Iraq invaded Iran. The war knocked out another seven percent of the world's oil {production}.", "E13",
 "G map: Iraq → Iran arrow; label SEPT 1980 · -7% WORLD OUTPUT", "1980: ANOTHER -7%", "VERIFIED · Wikipedia", "map whoosh"),
("P3-09", "Between 1978 and 1980, the American oil benchmark rose two hundred and fifty {percent}.", "E14", "G number card +250% · WTI 1978-80", "+250% IN TWO YEARS", "VERIFIED · Wikipedia", "counter"),
("P3-10", "Compare that with this year. From seventy-one dollars before the war to a hundred and twenty-six at the peak. About one point eight times. Painful. But 1979 was {worse}.", "E28 E31",
 "G bars: 1979-80 ×2.5 · 2026 ×1.8", "1979: ×2.5 · 2026: ×1.8", "ILLUSTRATION · our maths", "stamp thud"),
("P3-10b", "Not everyone lost. Oil states like Texas, Oklahoma, Louisiana and Alaska boomed. When the price of something doubles, somebody is on the other side of that {bill}.", "E36",
 "G map: US oil states highlighted; label BOOM STATES", "THE OTHER SIDE OF THE BILL", "VERIFIED · Wikipedia", "map whoosh"),
("P3-11", "Running total. Line three. Oil, two and a half times the price in a {year}.", "", "G running receipt line 3", "LINE 3 · OIL ×2.5", "", "printer"),
])

part("Part 4: Britain", "~10:00", [
("P4-01", "Part four. Britain.", "", "G part card PART 4 · BRITAIN", "PART 4 · BRITAIN", "", "reverse cymbal + sub drop"),
("P4-02", "Britain went into the oil shock already in trouble. The winter of 1978 to 79 became known as the Winter of {Discontent}.", "E23",
 "G timeline: SEPT 1978 → FEB 1979 · WINTER OF DISCONTENT", "THE WINTER OF DISCONTENT", "VERIFIED · Wikipedia", "map whoosh"),
("P4-03", "Workers went on strike against a five percent limit on pay rises, during the coldest winter in sixteen {years}.", "E23",
 "G two numbers: PAY LIMIT 5% · COLDEST WINTER IN 16 YEARS", "5% PAY LIMIT", "VERIFIED · Wikipedia", "stamp thud"),
("P4-04", "Just before Christmas, tanker drivers walked out too, and petrol supplies {tightened}.", "E23", "G calendar: 18 DEC 1978 circled; label TANKER DRIVERS STRIKE", "18 DEC: TANKER DRIVERS OUT", "VERIFIED · Wikipedia", "pen"),
("P4-04b", "Ford's workers won a seventeen percent pay rise, against the five percent limit. Lorry drivers wanted up to forty. When prices are rising fast, everyone tries to catch {up}.", "E33",
 "G bars: LIMIT 5% · FORD 17% · LORRY DRIVERS ASKED 40%", "5% LIMIT · 17% · 40%", "VERIFIED · Wikipedia", "counter"),
("P4-04c", "When the prime minister played down the chaos, one newspaper summed it up in a headline that stuck. Crisis? What {crisis}?", "E34",
 "G document card: 'CRISIS? WHAT CRISIS?' · THE SUN, JAN 1979", "'CRISIS? WHAT CRISIS?'", "VERIFIED · Wikipedia", "stamp thud"),
("P4-05", "In March, the government lost a vote of confidence by a single vote. In May, Margaret Thatcher won the general {election}.", "E24",
 "G timeline: 28 MAR LOST BY 1 VOTE · MAY 1979 THATCHER WINS", "LOST BY ONE VOTE", "VERIFIED · Wikipedia", "map whoosh"),
("P4-05b", "When Thatcher took over, inflation was about ten percent and about one and a half million people were out of work. Both numbers were about to get much {worse}.", "E35",
 "G two numbers: INFLATION ≈ 10% · UNEMPLOYED ≈ 1.5M; kicker MAY 1979", "MAY 1979: 10% · 1.5M", "VERIFIED · Wikipedia", "stamp thud"),
("P4-06", "Then the oil shock hit prices. British inflation climbed, and in 1980 it peaked at twenty-two {percent}.", "E25",
 "G line chart UK inflation: 1979 ≈10 · 1980 22 · 1983 4", "UK INFLATION: 22%", "VERIFIED · Wikipedia", "whoosh"),
("P4-07", "Twenty-two percent means something that cost a hundred pounds at the start of the year cost a hundred and twenty-two by the {end}.", "E25",
 "G two price tags: JAN £100 · DEC £122", "£100 → £122 IN A YEAR", "ILLUSTRATION · our maths", "register ding"),
("P4-08", "To bring it down, governments squeezed hard. By January 1982, twelve and a half percent of British workers had no {job}.", "E26",
 "G gauge 12.5% · UK UNEMPLOYMENT, JAN 1982", "12.5% UNEMPLOYED", "VERIFIED · Wikipedia", "counter"),
("P4-09", "By the summer of 1984, unemployment hit a record three point three {million}.", "E26", "G number card 3.3M · UNEMPLOYED, SUMMER 1984", "3.3 MILLION OUT OF WORK", "VERIFIED · Wikipedia", "counter"),
("P4-10", "Inflation did come down. Below ten percent by 1982, and four percent by the spring of 1983. But the bill for getting there was paid in {jobs}.", "E25 E26",
 "G line chart: inflation falls 22 → 4 while unemployment rises", "PAID FOR IN JOBS", "VERIFIED · Wikipedia", "stamp thud"),
("P4-11", "Running total. Line four. Twenty-two percent inflation, three million out of {work}.", "", "G running receipt line 4", "LINE 4 · 22% · 3.3M", "", "printer"),
])

part("Part 5: The long bill", "~13:00", [
("P5-01", "Part five. The long bill.", "", "G part card PART 5 · THE LONG BILL", "PART 5 · THE LONG BILL", "", "reverse cymbal + sub drop"),
("P5-02", "In America, inflation peaked at fourteen point eight percent in March {1980}.", "E19", "G number card 14.8% · US INFLATION, MAR 1980", "US INFLATION: 14.8%", "VERIFIED · Wikipedia", "counter"),
("P5-03", "A new chairman at the Federal Reserve, Paul Volcker, decided the only cure was expensive {money}.", "E20", "G card: PAUL VOLCKER · FED CHAIR FROM AUG 1979", "THE CURE: EXPENSIVE MONEY", "VERIFIED · Wikipedia", "pen"),
("P5-04", "The Fed's key rate went from about eleven percent to twenty percent by June 1981. The rate banks charged their best customers hit twenty-one and a {half}.", "E20",
 "G ladder: 11% → 20%; bracket PRIME 21.5%", "RATES: 11% → 20%", "VERIFIED · Wikipedia", "whoosh"),
("P5-05", "That meant crushing mortgage and loan payments for families, and businesses that couldn't afford to {borrow}.", "E20", "G chain: 20% RATES · MORTGAGES · LOANS · BUSINESSES", "MORTGAGES · LOANS · JOBS", "ANALYSIS", "pen"),
("P5-06", "By late 1982, American unemployment hit ten point eight percent. The highest since the Great {Depression}.", "E21",
 "G number card 10.8% · US UNEMPLOYMENT, DEC 1982", "10.8%: HIGHEST SINCE THE 1930s", "VERIFIED · Wikipedia", "stamp thud"),
("P5-07", "The World Bank called 1982 a global recession. And economists still trace it back to an energy crisis mostly caused by the revolution in {Iran}.", "E22",
 "G chain: IRAN 1979 · OIL ×2.5 · INFLATION · RATES 20% · RECESSION 1982", "IRAN 1979 → RECESSION 1982", "VERIFIED · Wikipedia", "riser"),
("P5-07b", "The banks felt it too. Between 1980 and 1983, a hundred and eighteen American savings and loan companies failed, holding forty-three billion dollars of {assets}.", "E41",
 "G number card 118 · SAVINGS & LOANS FAILED · $43BN", "118 LENDERS FAILED", "VERIFIED · Wikipedia", "counter"),
("P5-08", "So the 1979 bill wasn't just petrol. It came in three instalments. First the pump. Then prices on everything. Then interest rates and {jobs}.", "",
 "G receipt: INSTALMENT 1 PUMP · 2 PRICES · 3 RATES & JOBS", "THREE INSTALMENTS", "ANALYSIS", "printer"),
("P5-09", "People changed how they lived. Japanese cars went from nine percent of American sales in 1976 to twenty-one percent by 1980. Smaller, thriftier {cars}.", "E16",
 "G bars: 1976 9% · 1980 21%", "JAPANESE CARS: 9% → 21%", "VERIFIED · Wikipedia", "whoosh"),
("P5-10", "Between 1979 and 1981, oil use in America, Europe and Japan fell thirteen {percent}.", "E17", "G number card -13% · OIL USE 1979-81", "OIL USE -13%", "REPORTED · Wikipedia", "counter"),
("P5-10b", "America cut its dependence on foreign oil. Imports fell from almost half of what it used in 1977, to just over a quarter by {1982}.", "E42",
 "G bars: 1977 46.5% · 1982 28% (imports share)", "IMPORTS: 46.5% → 28%", "VERIFIED · Wikipedia", "whoosh"),
("P5-10c", "And then people forgot. The solar panels President Carter put on the White House were taken down in {1986}.", "E37",
 "G card: WHITE HOUSE SOLAR PANELS · REMOVED 1986", "PANELS REMOVED, 1986", "VERIFIED · Wikipedia", "glitch"),
("P5-11", "Running total. Line five. The bill came in three instalments, over three {years}.", "", "G running receipt line 5", "LINE 5 · 3 INSTALMENTS", "", "printer"),
])

part("Part 6: The lesson", "~15:30", [
("P6-01", "Part six. The lesson.", "", "G part card PART 6 · THE LESSON", "PART 6 · THE LESSON", "", "reverse cymbal + sub drop"),
("P6-02", "Here's how it ended. Higher prices made people use less oil, and made it worth drilling everywhere else. Prices didn't get back to pre-crisis levels until the mid-{1980s}.", "E15 E17",
 "G line chart: 1979 SPIKE · 1980 PEAK · MID-80s BACK DOWN", "BACK TO NORMAL: MID-1980s", "VERIFIED · Wikipedia", "whoosh"),
("P6-03", "And then they collapsed. In 1986, oil fell from twenty-seven dollars to under ten. Too much oil, not enough {buyers}.", "E18",
 "G ladder: $27 → < $10; label 1986", "1986: $27 → UNDER $10", "VERIFIED · Wikipedia", "whoosh"),
("P6-03b", "The collapse sent its own bills. American drilling rigs fell from about two thousand three hundred to barely a thousand in a year. Mexico went into a debt crisis. The Soviet Union lost an estimated twenty billion dollars a {year}.", "E39 E40",
 "G checklist: US RIGS 2,300 → 1,000 · MEXICO DEBT CRISIS · USSR -$20BN A YEAR", "THE GLUT SENT BILLS TOO", "VERIFIED / REPORTED · Wikipedia", "pen"),
("P6-03c", "And OPEC, the producers' club that had looked all-powerful, saw its share of the market fall from about half to under a {third}.", "E38",
 "G bars: 1970s ≈ 50% · 1985 29%", "OPEC: 50% → 29%", "VERIFIED · Wikipedia", "whoosh"),
("P6-04", "So what does 1979 tell us about the bill arriving now? Three {things}.", "", "G card: THREE LESSONS", "THREE LESSONS", "", "stamp thud"),
("P6-05", "Lesson one. Panic moves prices more than barrels. A four percent shortage became a crisis because people expected one. Watch the mood, not just the {supply}.", "E04 E06",
 "G checklist item 1: PANIC > BARRELS", "1 · PANIC > BARRELS", "ANALYSIS", "pen"),
("P6-06", "Lesson two. The pump is only the first instalment. In 1979, the big bills came later, through prices and interest rates. In Britain, this January's energy cap is already up twenty-six {percent}.", "E30",
 "G checklist item 2: THE PUMP IS INSTALMENT ONE · ENERGY CAP +26%", "2 · THE PUMP IS JUST THE START", "REPORTED · Ofgem", "pen"),
("P6-07", "Lesson three. It ends, but slowly. 1979's shock took years to unwind, and the people who paid most were the ones who lost their {jobs}.", "E21 E26",
 "G checklist item 3: IT ENDS, SLOWLY", "3 · IT ENDS, SLOWLY", "ANALYSIS", "pen"),
("P6-07b", "Some things are different now. In 1979, it was Iran's own workers who stopped the oil. In 2026, it's an American blockade, and a strait where traffic is still about sixty-five percent below normal. The cause is different. The bottleneck is the {same}.", "E29 E43",
 "G split: 1979 · STRIKES INSIDE IRAN | 2026 · BLOCKADE + A NERVOUS STRAIT", "DIFFERENT CAUSE, SAME BOTTLENECK", "REPORTED · UKMTO; Wikipedia", "glitch"),
("P6-07c", "And some things never change. Then and now, pump prices shot up fast and came down slowly. Economists call it rockets and feathers, and it was measured in exactly this kind of {shock}.", "E44",
 "G rocket and feather lines", "ROCKETS AND FEATHERS, THEN AND NOW", "VERIFIED · NBER", "whoosh"),
("P6-07d", "If there's one thing to take from 1979, it's this. Don't judge the bill by the first month at the pump. Judge it by what happens to prices, wages and interest rates over the next two {years}.", "",
 "G checklist: PUMP (MONTH 1) · PRICES (YEAR 1) · RATES & JOBS (YEAR 2)", "JUDGE IT OVER TWO YEARS", "ANALYSIS", "pen"),
("P6-08", "This year's oil shock has been smaller so far. Prices have fallen back from the peak. But the last time Iran's oil stopped, the real bill didn't arrive until two years {later}.", "E28 E22",
 "G split: 1979 · BILL ARRIVED 1981-82 | 2026 · ?", "THE REAL BILL CAME LATER", "ANALYSIS", "glitch"),
])

part("The Receipt", "~17:15", [
("RC-01", "So here's the receipt.", "", "G receipt rises, title THE RECEIPT", "THE RECEIPT", "", "printer"),
("RC-02", "Line one. Iran's output, down three-quarters in a {month}.", "E01", "G receipt line 1 prints", "OUTPUT -75%", "", "printer"),
("RC-03", "Line two. A four percent shortage, a hundred percent {panic}.", "E04", "G receipt line 2", "4% SHORT · 100% PANIC", "", "printer"),
("RC-04", "Line three. Oil, two and a half times the price in a {year}.", "E05", "G receipt line 3", "OIL ×2.5", "", "printer"),
("RC-05", "Line four. Twenty-two percent inflation, three million out of {work}.", "E25 E26", "G receipt line 4", "22% · 3.3M", "", "printer"),
("RC-06", "Line five. The bill came in three instalments, over three {years}.", "", "G receipt line 5", "3 INSTALMENTS", "", "printer"),
("RC-07", "The oil came back in months. The bill took years. Every crisis sends a bill. History keeps the {receipts}.", "",
 "G receipt final line crimson + stamp PAID IN FULL, 1983; then tagline", "EVERY CRISIS SENDS A BILL", "", "stamp thud"),
("RC-08", "If you haven't seen what a restart of the Iran war would cost you, that's the video on screen now. And subscribe, so the next invoice reaches you first.", "",
 "G end card: next video tile WHAT HAPPENS IF THE IRAN WAR RESTARTS? + subscribe", "WATCH NEXT · SUBSCRIBE", "", "soft tick"),
])

R = [r for _, _, rs in PARTS for r in rs]
def clean(s): return s.replace("{", "").replace("}", "")
if __name__ == "__main__":
    wc = sum(len(clean(r[1]).split()) for r in R)
    out = ["# INV-023 The Last Time Iran Shut the Oil: 1979: script v1 (2026-11-27)", "",
           f"Words: {wc} (≈ {wc/128:.1f} min at the narrator's pace)", "",
           "Tags: VERIFIED / REPORTED / CLAIM / ESTIMATE / SCENARIO / ILLUSTRATION. Facts: facts.md. Not financial advice.", ""]
    for t, st, rows in PARTS:
        out += [f"## {t} ({st})", ""]
        for c, n, fx, v, osd, tg, sfx in rows:
            out += [f"**{c}** {clean(n)}", f"> Visual: {v}  ", f"> On screen: {osd} · Tag: {tg or '-'} · Facts: {fx or '-'} · SFX: {sfx}", ""]
    p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../videos/INV-023-1979-oil/INV-023-1979-oil-script-v1.md")
    open(p, "w").write("\n".join(out)); print("words", wc, "rows", len(R))
