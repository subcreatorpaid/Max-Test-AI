# YouTube reference guides (adopted 2026-11-10)

Adapted from claude-youtube by Daniel Agrici (MIT, see `LICENSE-claude-youtube.txt`). We copied the reference guides only, not the plugin: its catch-all "youtube" skill would override our role skills and skip the OK gates.

**Order of authority:** `brain/rules.md` > `docs/script-rulebook-v1.md` > `brain/brand.md` > `docs/master-prompt-v3.md` > these guides. Every statistic in these guides is unsourced industry data: treat it as REPORTED and never put it in a script or on screen.

## Who reads what
| Guide | Used by | For |
|---|---|---|
| `retention-scripting-guide.md` | storyteller, hook-lab, scriptwriter, script-qa | first-30s structure, pattern interrupts, open loops, CTA timing |
| `seo-playbook.md` + `pre-publish-checklist.md` | packager, publisher, guard | title/description/chapters/hashtag limits, final check before Gate 5 |
| `thumbnail-ctr-guide.md` | packager | thumbnail rules and manual scoring while vidIQ is out of credits |
| `analytics-guide.md` + `algorithm-guide.md` | analytics-review, strategist | impressions-to-watch-time funnel, retention graph shapes, traffic-source health |
| `shorts-playbook.md` + `repurposing-guide.md` | shorts | Shorts length, loops, hooks, linking to the long video |

## Known clashes (ours wins)
- **AI narration "70% lower retention"** (retention guide): unsourced. Kokoro voice stays (Hammad's decision). The lesson we take: the visuals and story must carry more, which the rulebook already does.
- **Pattern interrupt every 30 s:** read as a visual change (new shot, card, map move, SFX hit), never as a tone change. Calm narrator stays.
- **"Join the family" / hype CTAs:** off-brand. Use the subscribe bridge in master prompt Stage B (about 1:30, max 15 s).
- **Repurposing to blog, LinkedIn, X, email, podcast:** out of scope. We only make Shorts and the pinned comment. A community post is public, so it needs Hammad's OK.
- **Publish-time and cadence advice:** goes through strategist and `brain/plan.json`. Nothing goes public without a gate OK.
- **Thumbnail faces/emotion advice:** we are faceless; war thumbnails show maps and machines, never victims (`brain/rules.md`).
- DataForSEO, NanoBanana and the YouTube API scripts from the original repo were **not** adopted (paid tools or API keys).
