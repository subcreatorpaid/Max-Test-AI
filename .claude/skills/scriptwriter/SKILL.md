---
name: scriptwriter
description: Write the full long-form script for a Max Tests AI video with retention structure and chapters. Use Opus.
---

# scriptwriter

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

Base: `docs/script-template-original.md` (4-beat structure), adapted for Max (an on-screen AI host, not a faceless narrator), and handbook ch.3.

## Output `videos/<slug>/script.md`
- **Packaging first:** 3 titles (< 60 chars, mark favourite) + thumbnail concept (Max's face + result + 2-3 words, never repeats the title).
- **3 hook options**, then the script:
  1. 0:00-0:05 click confirmation: show the result, say the promise. Max on screen. No greeting.
  2. 0:05-0:25 belief challenge + open loop.
  3. Chapters (4-6), each answering one question; a re-hook line every 35-45 s.
  4. Payoff: verdict (score or clear yes/no, who it's for, cost), one takeaway, tease next video, sign-off "I'm Max. I test AI so you don't waste your time."
- Format each line: `[MAX]` (on camera) or `[VO]` (voice over screen) + text. Add `[SCREEN: recording id]`, `[CARD: ...]`, `[ZOOM: ...]` cues every 2-3 sentences.
- 8-12 min = 1,200-1,800 words at 150 wpm. Short sentences, plain words, written for the ear.
- `[CHECK: claim]` for anything not yet in `facts.md`. Never invent numbers or quotes.
- Spoken disclosures: "I'm an AI host" in the intro; affiliate/sponsor line where a link is mentioned.
- Also write `videos/<slug>/narration.txt`: the spoken words only, one paragraph per beat (for TTS).
Then run **script-qa**.
