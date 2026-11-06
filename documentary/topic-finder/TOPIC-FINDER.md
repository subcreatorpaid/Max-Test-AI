# The History Invoice: topic finder (the standing process)

Set 2026-11-06 for Hammad: "search online, analyse competitors, find trends from YouTube, Google and Quora searches, and suggest topics. We upload every other day."
This replaces nothing. It feeds **Stage 0 (Topic pick)** in `master-prompt-v3.md`, then the normal pipeline (`pipeline/PROCESS.md`) takes over.

## 1. The channel lane (a topic must pass this gate first)
A topic is in the lane only if it is **geopolitics, war, sanctions, a choke point, a power struggle or the history of one**, and it can be followed **ring by ring until it reaches an ordinary household**.
Out of lane: partisan domestic politics (elections, parties), personal-finance basics, celebrity news, pure military gear videos.

## 2. The invoice is not only money (Hammad, 2026-11-06)
Every topic names the losses it puts on the bill. Money is one line, never the only line. Use these loss tags:
`money` · `lives` · `health` · `home` (displacement, refugees) · `food` · `water` · `land` (environment) · `jobs` · `time` (queues, waiting, delays) · `rights` (freedom, curfews, conscription) · `heritage` (culture, memory) · `trust` (in money, in leaders, in safety) · `safety`
A strong topic has **at least two kinds of loss**, and one of them is felt by a family, not a government.

## 3. Where the signals come from
| Signal | Tool | Who runs it | What we take |
|---|---|---|---|
| Competitor uploads + outliers | vidIQ `channel_videos`, `outliers` (5 credits each) | Claude, cloud | Videos >3x their channel average in the last 30 days, our niche |
| YouTube search demand | vidIQ `keyword_research` (research / questions / rising) | Claude, cloud | Monthly searches, growth %, question searches |
| Google Trends + autocomplete | `pc_trends.py` | Hammad's PC (cloud is blocked) | Trending searches in US/GB/CA/AU/IN/PK, YouTube + Google autocomplete for seed questions |
| Quora-style questions | `pc_trends.py` (Reddit question posts) + a manual Quora look | PC / Hammad (Quora blocks bots) | Real "why / will / what happens if" questions people ask |
| News pegs | Web search (Reuters, AP, FT, Bloomberg, UKMTO, IEA, S&P, FAO) | Claude, cloud | What happened in the last 72 h, and known dates in the next 2 weeks |

Competitor watch list (style reference only, never copy titles or lines): Paycheckology, Zeihan on Geopolitics, VisualPolitik EN, Money Matters, Why X, The Reconstruction Desk, Fred - Money Historian, DW News (The Dip), FT Film, Valuetainment history, BBC World Service docs. Add a channel when it shows up twice in outliers.

vidIQ budget: about 40 credits per scan (8 calls). The plan has 2,000 a month; 995 were left on 2026-11-06 (resets 30 Nov).

## 4. Scoring (each 0-5, then weighted, max 50)
| Score | Weight | 5 means |
|---|---|---|
| **Peg** | x2 | Happened in the last 72 h, or a hard date in the next 14 days |
| **Loss** | x2 | Two or more kinds of household loss, at least one human (lives, health, home, food) |
| **Demand** | x2 | Outliers in our niche >3x in the last 30 days, plus rising or question searches |
| Gap | x1 | The big channels have not taken this angle |
| Fact depth | x1 | Enough VERIFIED/REPORTED facts for the length |
| Visual fit | x1 | Maps, number cards, charts and downloadable stock B-roll cover it |
| Evergreen | x1 | Still true and watchable in 6 months (script rule: no "this week / yesterday") |

Rules: overlap with a video in production costs 5 points. A tie goes to the stronger peg. No two big videos on the same story within a week unless the second is a clear "what changed". `score.py topics.json` prints the ranking.

## 5. Keeping the pipeline full at every-other-day pace
- **Ready queue: always 4 topics with a locked title + thumbnail promise** (8 days of uploads), plus 6 more scored ideas in `topics.json`.
- **Scan twice a week** (Monday and Thursday): refresh pegs, re-score, drop stale ones, add new ones. A big breaking event triggers an extra scan the same day.
- **Mix every 2 weeks (7 uploads):** about 3 news-pegged, 2 history ("the last time this happened"), 2 human-loss stories (sailors, refugees, winter, hunger). History and human stories are the evergreen tail when the news is quiet.
- **Format mix (see section 6):** alternate the 18-20 min flagship with a shorter 8-12 min "Receipt" episode.

## 6. Production capacity (honest note)
Every other day is about 15 videos a month. One 18-20 min flagship currently takes: fact pack + script, 3 OKs from Hammad, Kokoro VO, storyboard, B-roll download by Hammad, render, review rounds and a 4K master. INV-003 alone has had 4 draft rounds over 3 days. At that pace, 15 flagships a month is not realistic, and rushed videos would break the trust and quality that make the channel work.
Recommended: **upload every other day, but alternate formats**: flagship 18-20 min (about 2 a week) and a "Receipt" episode of 8-12 min built from one template (one hero map, number cards, one story) on the days between. The reference channel's 9:31 Siege Economy did 133K, so shorter can win. Shorts (2-3 per flagship) fill the gaps. Step up only once the template renders without manual fixes.

## 7. Each scan's output
1. `scans/YYYY-MM-DD-scan.md`: top 5 with scores, loss tags, peg, evidence (with view counts), title, thumbnail promise, and what to re-verify.
2. Updated `topics.json` and the ranked table from `score.py`.
3. A one-line log in the thread: the top pick and whether Hammad needs to OK it.
Hammad OKs the topic, then Stage A (fact pack) starts.
