# Topic scan, 2026-11-06 (first run)

Sources used: vidIQ (Paycheckology uploads, 2 outlier searches, rising + question keywords, 2 keyword volumes; 35 credits, about 960 left), web search (oil week 45, S&P food warning, rare earths, Hormuz shipping). Google Trends, Quora and Reddit were not reachable from the cloud and Hammad's PC was offline, so `pc_trends.py` has not run yet. **Every number below is a lead, not a fact-pack fact. Re-verify before scripting.**

Already in production (not re-scored): INV-003 Pickaxe Mountain, INV-004 Siege Economy.

## What the market is saying
- Our niche is hot: Paycheckology's "What Happens If America Uses a Nuclear Weapon on Iran?" is at **634K views in 3 days** (849x its channel average). "The $43 Billion War..." 211K. Their off-niche videos (budget, compound interest, AI bubble) did 200-770 views. **The lane works; leaving it doesn't.**
- "What happens if..." + a world-scale fear wins: "What Would Happen to the World Economy If World War III Began?" 176K from a 1.6K-sub channel (434x).
- Human-loss documentaries do well next to money ones: BBC "Trapped under Houthi siege" 317K, "Who Are the Houthis?" 457K, "Toxic Battlefields" 122K.
- Search demand rising: "food security" +156%, "food inflation" +82%, "rare earth metals" +92%, "rare earth minerals" +51% (vidIQ, month).
- News pegs: Brent fell ~8% in the week to 3 Nov on an unconfirmed draft-peace report, while ~490 ships still wait outside Hormuz and 4 ships were hit 30 Oct-2 Nov. China's rare-earth control suspension expires **10 Nov**. S&P warned on 19 Oct that Hormuz + diesel + fertilizer + El Nino could bring a food crisis that lands mostly in 2027.

## Top 5 (score out of 50)
| # | Title (working) | Score | Losses on the bill | Why now | Format |
|---|---|---|---|---|---|
| 1 | **The War Might End. Your Bill Won't.** | 44 | money, time | Peace talk + falling Brent; everyone asks "will prices come down?" History of 1991/2022 says prices fall slower than they rise. | Flagship |
| 2 | **The Hunger Bill: Why Hormuz Reaches Your Plate in 2027** | 43 | food, lives, money | S&P warning; Bangladesh urea plants shut; food-security search +156% | Flagship |
| 3 | **What Would World War III Cost Your Family?** | 42 | lives, rights, food, money | Biggest demand signal (434x outlier). Built from 1914/1939 history, sober, claim vs fact | Flagship |
| 4 | **The Prisoners of Hormuz: 20,000 Sailors Nobody Counts** | 39 | lives, time, rights | Ships still being hit; nobody tells the crew story (big gap) | Receipt (8-12 min) |
| 5 | **What Happens If China Stops Selling Rare Earths?** | 38 | jobs, safety, money | Hard date 10 Nov; best as "what changed" once the decision is out | Receipt (8-12 min) |

Next in the bench: Second door (Houthis / Bab el-Mandeb) 38, The Winter Bill 37, The 1973 Invoice 37, The water-and-air invoice 34. Full details: `topics.json`.
Excluded: anything about the midterm result (partisan politics), money basics (off-niche).

## Suggested calendar (every other day, alternating formats)
| Date | Video |
|---|---|
| per current plan | INV-003 Pickaxe Mountain, then INV-004 Siege Economy |
| next slot | #1 The War Might End. Your Bill Won't. |
| +2 days | #5 Rare earths, "what changed after 10 Nov" (Receipt) |
| +4 days | #2 The Hunger Bill |
| +6 days | #4 Prisoners of Hormuz (Receipt) |
| +8 days | #3 WW3 family bill |

## To re-verify before any script
Brent close and draft-peace status; UKMTO incident count; IMO trapped-ship/crew count (May figure is old); rare-earth outcome after 10 Nov; S&P numbers from the original report; Bangladesh urea plants.

## Update 06:55 UTC: PC trend pull merged (Google Trends RSS 6 countries + YouTube/Google autocomplete)
- **Re-ranked:** T01 Bill Won't 46, T02 Hunger Bill 45, T03 WW3 family 42, **T07 Winter Bill up to 41** (GB trending "weather polar vortex" 1000+, "heating bills going up / this winter"), T04 Prisoners of Hormuz 39. New: T11 China-Taiwan 2027 (36, crowded). Full table: `ranked.md`.
- Strongest live searches in our lane: "will gas prices go down soon / this week", "strait of hormuz open or closed / tracker / status today", "diesel shortage uk / us / canada / australia / india", "food crisis 2026 / 2027", "heating bills this winter", "china taiwan 2027", "tariffs refund", "russia ukraine war casualties".
- Searches show non-money losses people fear: access (strait open?), fuel supply, heat, food, safety, lives.
- Reddit blocks unauthenticated requests (403); Quora blocks bots. Question demand comes from autocomplete + vidIQ questions instead.
- Script fixes: whole-word theme filter (sports names no longer match), loss words added (casualties, shortage, refugees, blackout, evacuation, invasion, territory, heritage), 4 new seeds.
