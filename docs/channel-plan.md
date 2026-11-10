# New channel plan: geopolitical finance documentaries

Prepared 2026-11-04 for Hammad. Sources: the Paycheckology screenshot, the full transcript and the full video (`videoplayback.mp4`, 32:45) in this folder, and the master prompt you pasted.

---

## 1. The short version

- **The formula that works:** a crisis question in the package, the money in the payoff. People click for "what happens if" and stay for "here is what it costs you". The flops in the screenshot did the opposite: they led with the money.
- **The format is very producible for us.** The reference video is about 70% AI-generated cinematic stills with slow camera moves, 20% dark text cards (quotes, big numbers, timelines) and 10% maps and charts. One calm narrator, no face. We can build all of it with code plus AI images, and you only approve.
- **Our channel should not be a Paycheckology clone.** We keep the genre and build our own identity: a recurring "Receipt" at the end of every video, on-screen confidence tags on every number, and a wider topic range than one war.
- **Recommended name:** *The Invoice* (see section 4; you pick on the card I sent).
- **Recommended first video:** "What Happens If the Strait of Hormuz Never Reopens?"
- **Biggest risks:** made-up numbers (the prompt alone cannot stop this), YouTube's AI-disclosure and "inauthentic content" rules, and limited ads on war content. Each has a fix in section 7.

---

## 2. What the reference actually does

### 2.1 The video (What Happens If America Uses a Nuclear Weapon on Iran?)

| Part | Time | What happens |
|---|---|---|
| Cold open | 0:00-1:15 | One physical object (a granite mountain near Natanz), one quote ("10 minutes"), one counter-claim ("the plan is insane"), then an honest caveat ("it's one man's claim"). |
| Subscribe bridge | 1:24-1:43 | "98% of you who watched our last video weren't subscribed." Short, uses a real stat, early. |
| Roadmap | 1:43-2:50 | "We'll follow one bomb outward, ring by ring", then names every ring. The viewer knows the whole journey and stays to finish it. |
| 8 parts | 2:50-31:00 | Mountain → the nuclear line (history) → the wind (people) → the region → the ladder to a wider war → the money → your kitchen table. Each part opens with a "PART N" card. |
| Close | 31:00-32:45 | Back to the mountain. "The ring can still go back to a dot." Full circle. |

What makes it work:
1. **Honesty as a hook.** It keeps separating claim, report and fact ("He named no officials and showed no documents"). That builds trust and lets them use a scary title without being clickbait.
2. **Every abstraction becomes a person or a price.** "360,000 people in Kashan", "every $10 a barrel is about $250 a year for a household", "Bangladesh: 4 of 5 urea plants shut".
3. **Rehooks every 60-90 seconds** with a new question ("So, could this start World War III?", "rung by rung").
4. **The money comes late (about 22:00) and is the payoff**, not the opening.
5. **Practical close.** Six steps (emergency fund, +20% budget test, insurance exclusions, don't trade headlines, pay down variable debt, official emergency advice).

Length: about 4,900 words in 32:45, so about 150 words per minute. That is longer than your prompt asks for (2,800-3,200). Their 206K hit was 17:47 and their 133K hit was 9:31, so length is not what wins. The question and the timing win.

### 2.2 The visual style (from frames every 40 seconds)

- **AI cinematic stills** (the mountain, a baker, a street in Kashan, an LNG tanker, a wheat field, a trading floor) with a slow push or pan. Labelled as illustration where needed.
- **Dark charcoal text cards**: "PART 3" kicker, white headline, one yellow accent line, a giant faint chapter number in the background, a small source line at the bottom ("Source: UNHCR").
- **Quote cards** with big yellow quote marks and the speaker, date and outlet.
- **Big-number cards**: "×32 war-risk cover", "~200 Russian workers on site", ">1M arrivals in Europe".
- **Maps**: teal 3D terrain (they credit AWS Terrain Tiles and Natural Earth, which are free), the country in glowing red, yellow rings and labelled dots.
- **Simple line charts** (Brent, gold) in one yellow line on dark.
- **Recreated newspaper clippings** and a ranked "ladder" table card.
- Almost no real news footage. That keeps them safe from copyright claims.

### 2.3 Hits vs flops in the screenshot

| Video | Views | Age | Why |
|---|---|---|---|
| What Happens If America Uses a Nuclear Weapon on Iran? | 212K | 14h | Future-tense "what if", the scariest live question that week, cinematic thumbnail with no text. |
| The $43 Billion War That's About to Restart | 206K | 6d | News peg ("about to restart"), a dollar number, map thumbnail with 2-3 words ("IRAN WHY AGAIN?"). |
| Iran's Siege Economy: Oil, Gold and a Bank That Doesn't Exist | 133K | 12d | Hot country + a curiosity gap ("a bank that doesn't exist"). Only 9:31 long. |
| How Russia Funds a $200 Billion Ukraine War? | 5K | 9d | Old, crowded topic (covered to death since 2022), no new stakes, face thumbnail. |
| Who got rich from the Iran war? | 1.7K | 2d | Backward-looking and cynical, busy thumbnail (face + four logos + number), posted 12h before the nuke video, which ate its audience. |
| Compound Interest: Why a Penny Beats $1 Million | 714 | 2w | Off-niche personal finance. The audience comes for crises, not for money basics. |

**The lessons we apply:**
1. **Package = stakes, payoff = money.** "What happens if…", "about to…", "why again?" beat "who got rich" and "how X funds Y".
2. **Ride the live question within 24-72 hours.** Their two biggest hits answered the question people were asking that week.
3. **Thumbnail = one map + one country glowing + 2-3 words**, or one cinematic image with no words. No logo collages, no busy faces.
4. **Stay in the lane.** One off-niche video confuses the algorithm about who the channel is for.
5. **Don't post two big videos on the same topic within a day.** They cannibalise each other.

---

## 3. The master prompt: strengths and gaps

### Strengths (keep these)
- The concentric-ring structure (object → system → region → money → your table) is exactly what the reference does.
- The tone rules (calm, no hype, numbers carry the drama) and the banned-cliché list.
- "Never present jargon without translating it into dollars or daily life."
- Demanding visual and audio cues per chapter.
- Separating verified facts, intelligence claims, AIS tracking and speculation.

### Gaps (fixed in `master-prompt-v2.md`)
1. **No research step.** It says "never fabricate" but gives the model no facts to work from. On a live war, any model will invent numbers. Fix: the script may only use facts from a dated **fact pack** with sources, made first with web research.
2. **It copies the reference.** The working title is Paycheckology's own title and they are named as the benchmark. Fix: our own titles; references are named only for style.
3. **The example numbers are treated as facts.** "$10 a barrel ≈ 25-30¢ a gallon" is a bit high (a barrel is 42 gallons, so the direct effect is about 24¢). The Lloyd's percentages and bunker depths are topic-specific. Fix: they become formulas to check, not facts to repeat.
4. **The structure only fits military topics.** Chapters 1-3 assume a strike or a choke point. Fix: one ring framework with three variants (war/strike, choke point/blockade, sanctions/economic war).
5. **No packaging step.** Title and thumbnail are decided after the script. Fix: lock the title and thumbnail promise first, and the hook must pay it off inside 30 seconds.
6. **The retention target is unrealistic.** Over 50% retention at 20 minutes is rare. Fix: realistic targets (over 70% at 0:30, average view percentage 35-45%).
7. **The visual cues don't match what we can make.** "Leaked ledgers" invites fake documents. Fix: a fixed menu of visual types we can actually produce, with a label rule for illustrations.
8. **No safety and policy rules.** Nothing about AI images of real people, gore, YouTube's synthetic-content disclosure, or financial-advice wording. Fix: added.
9. **No outputs beyond the script.** Fix: it also returns a source list, a claims-check table, 3 titles, 3 thumbnail briefs, 3 Shorts cut-downs and a pinned comment.

---

## 4. Positioning: our own channel

**Name (recommended): The Invoice**, tagline *"Every crisis sends a bill. We read it."*
Other options: *Fallout Ledger* (darker, more war), *Second Order* (smarter, more analyst). Check that the handle is free before we lock it.

**Promise:** We take the crisis everyone is watching and follow it until it lands on your bill: fuel, food, rent, savings.

**What makes us different from Paycheckology and the rest:**
1. **The Receipt.** Every video ends on a printed, itemised receipt: what this crisis adds to a typical household per month (US, UK, and a third column for South Asia when it is relevant). It is our signature shot, our end-screen, our Shorts format, and a thumbnail device.
2. **Confidence tags.** Every number on screen carries a small tag: VERIFIED, REPORTED, CLAIM or ESTIMATE. Trust is the brand.
3. **Wider beat than one war.** Choke points (Hormuz, Red Sea, Taiwan Strait, Panama), sanctions and money flows, food and fertilizer, undersea cables, tariffs. Iran is our launch topic, not our whole channel.
4. **Our own look.** Ink-black and warm paper instead of their charcoal and teal. One accent colour (signal orange) instead of yellow and red. Maps in a dark blueprint style with the country in orange. Receipt-paper texture on number cards.

**Audience:** 25-54, US/UK/Canada/Australia first (highest ad rates), working people and small investors who feel the cost-of-living squeeze and don't trust soundbites.

**Voice:** one calm, measured male narrator, always the same AI voice (openly AI, like Max). No face. Note: Max Reed stays on Max Tests AI; this channel is separate.

---

## 5. Production pipeline

You approve three things per video: the topic, the script, and the final cut. Everything else is done by the team.

| Step | What | Who / tool | Your part |
|---|---|---|---|
| 1. Pick | Daily scan of the news and vidIQ for the live question; pick the topic and lock title + thumbnail promise | researcher + strategist (vidIQ, web) | OK the topic |
| 2. Fact pack | 40-80 facts, each with source link, date and confidence tag; formulas checked | researcher (web search) | none |
| 3. Script | AV script from `master-prompt-v2.md`, using only the fact pack | scriptwriter (Opus) | **OK the script** |
| 4. Voice | Narration from the script, one fixed voice, about 140 wpm | ElevenLabs (recommended) or Google TTS | none |
| 5. Visuals | AI stills → 2.5D parallax (depth map + camera move); 3D relief maps from free terrain data; charts, number cards, quote cards and the Receipt from code templates; public-domain footage (US DoD/DVIDS, NASA) where useful | creator (Gemini/Imagen or Flow for stills; code templates rendered in the cloud; your Motion Graphics MAX kit for extras) | none |
| 6. Sound | Low drones, sub-bass hits on numbers, clock ticks, risers, licensed music bed | editor | none |
| 7. Edit | Auto-assemble to the narration timeline, captions, chapter cards, source lines | editor (script + ffmpeg) | **OK the cut** |
| 8. Package | 3 titles + 3 thumbnails, scored with vidIQ | packager | pick one |
| 9. Release | Facts re-checked, disclosure ticked, description with sources, chapters, pinned comment, 2-3 Shorts | guard + publisher | press publish |

Speed target: a news-peg video in **72 hours** from your topic OK. One long video a week to start, plus 2-3 Shorts cut from it (the Receipt and the scariest number make the best Shorts).

---

## 6. First videos

All of these depend on the news on the day we start; step 1 re-checks the peg and the numbers.

| # | Working title | Type | Why |
|---|---|---|---|
| 1 | **What Happens If the Strait of Hormuz Never Reopens?** | Choke point, hot now | The live question; the receipt is easy for viewers to feel (fuel, food, shipping). Different question from anything in the screenshot. |
| 2 | **What Happens If China Blockades Taiwan? (Follow the Bill)** | Choke point, evergreen | The biggest hypothetical in Tier-1 economies: chips → cars, phones, pensions. Gets new views every time Taiwan is in the news. |
| 3 | **The Fertilizer Shock: Why Your Bread Costs More Next Summer** | Food, slow-burn | The hidden 6-9 month lag story; urea through Hormuz. Very "what does this mean for me". |
| 4 | **The $10 Million Insurance Bill That Stops Every Tanker** | Money machine | War-risk insurance explained; nobody else makes this the whole video. Curiosity title. |
| 5 | **What Happens If the Undersea Cables Are Cut?** | Infrastructure | Internet, card payments and markets run through cables Iran has named as targets. |
| 6 | **What Happens If the Gulf Brings Its Money Home?** | Money flows | Gulf sovereign funds hold trillions in Western assets; what a sell-off does to your pension. |

Backup idea for the South Asia audience later: "How a Gulf War Empties Wallets in Pakistan and India" (remittances).

---

## 7. Risks and how we handle them

1. **Made-up numbers.** Fact pack first; the script can only cite it; guard re-checks every on-screen number before release. Every number has a source line on screen.
2. **YouTube AI disclosure.** Photoreal AI scenes of real places or events must be disclosed with YouTube's "altered or synthetic content" setting. We tick it every time, and label scenes "Illustration" on screen.
3. **No AI images of real people.** Politicians appear only through real public-domain or properly licensed photos, or through quote cards. Never a generated face of a real person.
4. **"Inauthentic content" (mass-produced AI) monetisation rule.** We avoid it with real research, a real argument in every script, varied visuals, our own templates and voice, and no templated filler.
5. **Limited ads on war content.** No gore, no corpses, no explosions on people; keep it educational and analytical; thumbnails show maps and machines, not victims.
6. **Financial advice.** Practical steps are general ("emergency fund", "don't panic-sell") with a clear "not financial advice" line. No stock or crypto picks.
7. **Defamation.** Claims about named people or companies come only from cited reporting, with "according to" wording.
8. **Copyright.** No news broadcaster clips; recreated headlines with the outlet credited; licensed music only.

---

## 8. Decisions I need from you

1. **Channel name** (card sent in the thread; I recommend The Invoice).
2. **Narrator voice:** I recommend testing one ElevenLabs narrator (paid plan) against a free Google voice on the first script, then locking one.
3. **First video:** I recommend #1 Hormuz. If you OK it, the researcher builds the fact pack next.
