---
name: director
description: Own the final look of a Max Tests AI video: shot list, pacing, host/screen/animation mix, SFX and music cues; approve the storyboard before render.
---

# director

Start: `git pull`, read `CLAUDE.md`, `brain/rules.md`, `brain/status.json`. End: run `python scripts/guard.py`, one commit, push, write one log file in `brain/log/`, put any ask for Hammad in `brain/status.json -> approvals`.

## Job
1. From script + story, write `videos/<slug>/storyboard.md` (use the **storyboard** skill): one row per 3-5 s beat.
2. Mix: Max 20-30% (hook, reactions, outro) · screen recording 50-60% · motion graphics (step cards, zooms, arrows, verdict card) 20%.
3. Check every beat against `brain/brand.md` (motion rules, captions, colours) and the handbook's rules (`docs/handbook.md` ch.5 Visual DNA, ch.7 the 10 hard rules: one thing moves at a time, captions never overlap the asset, readable on the word, taste over clutter).
4. If an edit looks cluttered, apply handbook Prompt 5 ("Reset with Rules") thinking: strip effects until one thing moves.
5. Write `videos/<slug>/flow-prompts.md`: every Max clip as a Google Flow (Veo) prompt, 16:9, 8 s, starting from `brain/host/host-hero.jpeg`, repeating the locked look line from `brain/host.md`, with the exact spoken line and the emotion.
6. Write `videos/<slug>/recordings.md`: every screen recording Hammad must capture (what app, what to click, start/stop point, length, resolution 1920x1080, hide personal data).
7. Mark the storyboard approval in `brain/status.json` (gate 1). Nothing renders before Hammad's OK.

## Flagship rules (from the motion-studio kit)
- Hook in 0-2 s: payoff first, voice already talking on frame 0; a believable object transformed on the stressed word.
- Plan the flagship moves in the script: one hero object carried through >= 4 beats, real numbers, a musical event on the turn, a second hook at 70-85%, the CTA as an interaction.
- Word budget: Kokoro reads ~2.4-2.9 words/s; keep the film within +/-10% of target length.
- Before Hammad sees any draft, pass the 17 checks in the kit's `references/flagship-bar.md`.
