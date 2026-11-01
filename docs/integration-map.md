# Integration map: brain blueprint + existing system

How the new brain repo reuses the work already done in this project. Rule: **reuse, don't duplicate.** Each existing piece gets one home in the repo.

Sources merged:
- **Blueprint**: `brain-setup/youtube-brain-blueprint.md` (repo structure, team roles, OK gates, bots)
- **Handbook**: `give me the complete handbook ... .docx` (12 chapters: niche test, 4-beat script, Visual DNA, Motion kit, editing rules, model tiers, pipeline.py, autopilot_manager.py, 7 master prompts, runbook, troubleshooting)
- **Script template**: `scripts/claude-script-project-instructions.md`
- **Channel plan doc**: "AI Influencer YouTube Channel: Full Plan" (https://claude.ai/artifact/BZbssLMGYpcn7p7WcE4462): persona, tools, workflow, pillars, 20 ideas, schedule, competitors, monetisation, 90-day plan

## 1. Where each existing piece goes in the repo

| Existing piece | Goes to | Used by role |
|---|---|---|
| Handbook ch.1 niche litmus test + outlier rule (>=2.5x median) | `.claude/skills/goal-lock/` + `researcher` skill | researcher, strategist |
| Handbook ch.2 economics, Tier-1 targeting, policy defence | `brain/rules.md` (compliance) + `money` skill | guard, money |
| Handbook ch.3 packaging triangle + 4-beat script | `brain/brand.md` video standard + `scriptwriter`, `packager` skills | scriptwriter, packager |
| Script template (scripts/…md) | base of `scriptwriter` SKILL.md, adapted from faceless narrator to the AI host | scriptwriter |
| Handbook ch.4 operator model, folder + naming standard | `CLAUDE.md` "how every run behaves" + `videos/<slug>/` layout | all |
| Handbook ch.5 cinematic stack, Visual DNA anchor, character consistency | `brain/brand.md` visual section + `director`, `creator` skills | director, creator |
| Handbook ch.6 Claude Motion System kit (Chat 1 + Chat 2) | `creator/animator` skill + Motion Studio setup | creator, director |
| Handbook ch.7 editing rules (5 basics, 10 hard rules) | `brain/brand.md` video standard + `director` skill + guard checks | director, guard |
| Handbook ch.8 model tiers + 7-step brain setup | `CLAUDE.md` model rules (Opus = Architect, Sonnet = Daily Driver, scripts/Gemini = Apprentice) | all |
| Handbook ch.9 pipeline.py (360p draft -> upscale -> master) | `scripts/pipeline.py` = the review-render / final-render step | creator |
| Handbook ch.9 autopilot_manager.py (SEO + staging) | `scripts/autopilot_manager.py` = publisher helper (stage as private/unlisted only) | publisher |
| Handbook ch.10 Prompt 1 (Master Director) | `director` skill | director |
| Handbook ch.10 Prompts 2-3 (Motion) | `creator/animator` skill | creator |
| Handbook ch.10 Prompt 4-5 (editing, reset with rules) | `director` skill | director |
| Handbook ch.10 Prompt 6 (pre-flight safety audit) | `guard` skill | guard |
| Handbook ch.10 Prompt 7 (multi-platform packaging) | `publisher` skill (Shorts phase) | publisher |
| Handbook ch.11 daily runbook | `docs/pipeline.md`, merged with blueprint section 2 | all |
| Handbook ch.12 troubleshooting matrix | `brain/learnings.md` seed rules | strategist, guard |
| Plan doc: persona (Nova), character bible steps | `brain/host.md` (new file) + `brain/brand.md` | director, creator |
| Plan doc: tool stack table | `brain/accounts.md` (tools part) | all |
| Plan doc: pillars + 20 first ideas | `brain/ideas.json` + `brain/plan.json` | strategist |
| Plan doc: posting schedule | `brain/rules.md` schedule + `publisher` | publisher, secretary |
| Plan doc: competitors + underdog videos | `brain/competitors/*.md` + `landscape.md` (refresh, not redo) | researcher |
| Plan doc: monetisation table | `money` skill + `brain/goals.json` milestones | money |
| Plan doc: rules to stay monetised + 90-day plan | `brain/rules.md` + `brain/goals.json` | guard, secretary |
| Existing skills goal-lock, opportunity-check (other channel) | copy the pattern, rewrite for this channel's goal | strategist, researcher |

## 2. Questionnaire items now answered by existing material

| Q | Answer from existing material |
|---|---|
| 3 viewer | beginners and side-hustlers, 18-40, US/UK/South Asia (plan doc) |
| 4 goal | 90-day plan; YPP milestones; judge on views/video and subs per 1,000 views (plan doc) |
| 5 type | hands-on tutorial with a visible result; no AI news (plan doc) |
| 6 length/rhythm | 1 long video + 4-5 Shorts a week (plan doc); length conflict, see 3 |
| 7 visual | screen recording + animation + host 20-30% of screen time (plan doc) |
| 8 host | AI influencer, working name Nova, openly AI (plan doc) |
| 10 sound | YouTube Audio Library (plan doc) |
| 11 captions | burned-in kinetic captions (handbook ch.7/9) |
| 12-13 competitors | 7 channels already profiled, AI Playbook = closest rival (plan doc) |
| 17 budget | $0 start, free tools (plan doc + memory) |
| 18 schedule | Tuesday 3pm US Eastern long video; Shorts Wed/Thu/Sat/Sun (plan doc) |
| 20 monetisation | affiliates from video 1, products/services at ~1K subs, sponsors at 5-10K (plan doc) |
| 21 compliance | altered/synthetic content box, value layer, no fake income claims (plan doc) |

## 3. Conflicts to decide (Hammad)

1. **Channel scope.** Blueprint: "AI to automate work and create" (Claude, Gemini, Flow, workflows, bots). Plan doc: "make YouTube videos with free AI". Recommendation: plan doc's angle as the core promise, with automation/bots as one pillar (the brain system itself is great content).
2. **Length.** Blueprint asks 15-25 min; plan doc says 8-12 min. Recommendation: 10-15 min.
3. **Voice.** Blueprint: Kokoro; handbook: edge-tts; plan doc: Google AI Studio / ElevenLabs. Recommendation: test Kokoro + edge-tts (both free, run in GitHub Actions) against one AI Studio voice, pick one, never change.
4. **Where rendering runs.** Handbook: local PC (GPU upscale, CapCut). Blueprint: GitHub Actions. Recommendation: GitHub Actions for 360p drafts, captions and assembly; upscale step optional (skip or run on PC) since screen recordings are already 1080p.
5. **Talking-host clips.** Plan doc: HeyGen/Hedra free tier or Veo. Keep, but budget a cap per week.
