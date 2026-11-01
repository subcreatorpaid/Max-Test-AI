# Max Tests AI: the brain

**Read this first, every session.** Then read `brain/rules.md`, `brain/status.json`, and the role skill you are running.

## The business in one paragraph
Max Tests AI is a long-form YouTube channel (English, US accent) hosted by **Max Reed**, a realistic AI host who is openly an AI. Max tests and reviews AI tools, then builds something real with them: a video, an ad, an edit, or a workflow bot. Explainer style, 8-12 minutes, mostly screen recordings and clean motion graphics, with Max on screen only for the hook, reactions and outro. Audience: beginners and side-hustlers, 18-40, US/UK/South Asia. Owner: Hammad. He reviews and presses OK; the team does the rest.

## Goal
1 long video a week (first one live by 2026-11-08). Shorts (3-4 per video) start 1-2 weeks after launch. 90-day goal and numbers: `brain/goals.json`. Judge on views per video and subscribers per 1,000 views.

## Team (role skills in `.claude/skills/`)
| Role | Job |
|---|---|
| researcher | trends, topic demand (vidIQ), competitor uploads, fact checks |
| strategist | picks next videos, angle, packaging promise, monthly plan |
| storyteller | story arc, hook-to-payoff, open loops (Opus) |
| director | final look: shot list, pacing, host vs screen vs animation mix, SFX/music cues; approves storyboard |
| scriptwriter | full script, retention structure, chapters (Opus) |
| creator | motion graphics (Motion Graphics MAX kit, on Hammad's PC), placeholder voice, assets |
| editor | the full edit on Hammad's PC: assembles Max clips, screen recordings, narration, graphics, sound, captions; delivers the upload-ready MP4 + CapCut edit list |
| packager | 3 titles + 3 thumbnails, scored before choosing |
| publisher | description, chapters, tags, end screens, scheduling (after OK only) |
| guard | release checks: facts, copyright, AI disclosure, links, specs |
| money | affiliates, sponsors, AdSense, products, monthly report |
| secretary | morning briefing (max 3 to-dos), dashboard, approvals queue |
Helpers: goal-lock, competitor-analysis, hook-lab, script-qa, storyboard, analytics-review.

## Where everything lives
- `brain/brand.md` voice, look, never-list, video standard
- `brain/host.md` Max Reed character bible; reference images in `brain/host/`
- `brain/rules.md` approvals, safety, compliance, budgets
- `brain/goals.json` goal + latest numbers · `brain/status.json` to-dos, approvals, pipeline
- `brain/plan.json` content calendar · `brain/ideas.json` idea queue · `brain/learnings.md` what works
- `brain/competitors/` one file per competitor + `landscape.md` · `brain/research/` dated research
- `brain/accounts.md` accounts and tools (never passwords) · `brain/log/` one file per run
- `videos/<slug>/` brief, script, storyboard, spec.json, recordings list, flow prompts, title-thumb, upload
- `scripts/` guard.py, tts.py, render.py · `.github/workflows/` automations
- `docs/handbook.md` the automation handbook (source material), `docs/blueprint.md` the system blueprint, `docs/pipeline.md` the step-by-step

## How every run behaves
1. `git pull`; read this file, `brain/rules.md`, `brain/status.json`, then the role skill.
2. Do only that role's job. Results go into `brain/` or `videos/` files, not chat.
3. Run `python scripts/guard.py` before committing. One commit per run. Push.
4. Write ONE new log file `brain/log/YYYY-MM-DD-HHMM-<role>-<slug>.md` with one line: `date time | role | what was done | what needs the owner`. Never edit a shared log.
5. If Hammad is needed, add it to `brain/status.json -> approvals` (max 3 to-dos a day).
6. Unattended runs never: publish, send messages, accept terms, create accounts, enter passwords/payment, change security settings, spend paid credits beyond budget, delete data.

## Models and token saving
- Sonnet for routine work. Opus only for final scripts, hooks/titles, storytelling, hard design.
- Mechanical jobs go to scripts/GitHub Actions; Gemini only for research and trend scans.
- Fewer tokens when quality is equal; batch steps; don't re-read big files or re-render without need.

## Talking to Hammad
He may write in Urdu/Hindi: open with one English line summarising what he said, then answer in short plain English. Ask questions as a clickable form (recommended option preselected, A/B/C + Other box).

## Current state (keep short)
- 2026-11-01: brain built. First video `videos/claude-capcut-edit/` in progress (script + storyboard waiting on gate 1).
- Production split: Max clips by Hammad in Google Vids (`vids-scenes.md`); screen narration = one file recorded by Hammad (`voiceover.md` -> `audio/voiceover.mp3`); animations by Claude with the kit on Hammad's PC; full edit by Claude (editor skill) -> final MP4. Max's voice is pending (Google Vids voice, round 5); Kokoro is placeholder only. GitHub Actions: guard + previews.
