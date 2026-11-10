# Parallel render "bots" (set up 2026-11-10 for INV-006, reusable for every video)

Hammad asked for several bots working side by side so videos come out fast. This is how it works.

## The bots
| Bot | Where it runs | What it does | Trigger |
|---|---|---|---|
| Clip fetcher | GitHub Actions `broll.yml` | Pixabay (+ Coverr) video clips, shrunk to 1080p/15 s, committed to `videos/<ID>/broll/` | push `videos/<ID>/broll.json` |
| Photo fetcher | GitHub Actions `stills.yml` | Pixabay photos for slow-push (Ken Burns) shots, committed to `videos/<ID>/storyboard/stills/` | push `videos/<ID>/storyboard/stills.json` |
| Part renderers (1 per part, all at once) | GitHub Actions `render-video.yml` (INV-006 used `render.yml`) | Kokoro voice for that part, then graphics + footage + photos with crossfades, final 1080p grade | push `videos/<ID>/render/go.json` |
| Stitch + sound | Claude's cloud session | joins parts, in-house music bed, sparing kit SFX (kit WAVs stay on the PC, never on GitHub), -16 LUFS, review | after the parts land |

## For a new video (INV-007 and on)
1. Copy `tools/inv006/` to `tools/inv007/`. Replace `script_v4.py` with the new script rows `(code, narration, facts, visual, on-screen, tag, sfx)` and put the graphics for each row in `spec6.py` (`SPEC[code] = lambda o,t: number(...)/bars/line/map_/receipt/card/part/headline/still`).
2. In `render_part.py`, edit `FOOT_FULL` (rows that are footage-only) if needed. The mix is automatic: rows over 6.5 s are split 50/50 into graphic + footage, and footage slots rotate 3 video : 2 photo, which gives about 50% graphics, 30% video and 20% photos.
3. Push the clip list (`videos/<ID>/broll.json`) and the photo list (`videos/<ID>/storyboard/stills.json`). Reuse the shared libraries `videos/INV-006-lib/broll` (77 themed clips) and `videos/INV-006-photos/storyboard/stills` (44 photos). Clip names start with a theme word (ship, gas, winter, home, money, city, power, land, misc), which the renderer matches to the narration.
4. Push `videos/<ID>/render/go.json`:
   `{"tools":"tools/inv007","script":"tools/inv007/script_v1.py","parts":["CO","P1","BR","P2","P3","P4","P5","RC"],"clipdirs":["videos/<ID>/broll","videos/INV-006-lib/broll","videos/INV-006-photos/storyboard/stills"]}`
5. When all parts are in `videos/<ID>/render/parts/`, Claude pulls them and runs `tools/inv006/mix6.py <parts> <kit sfx dir> mix.wav` (music bed made in code, so no licence issue), then muxes, reviews and delivers.

## Rules baked in
- 1080p, never 4K. Final encode `-crf 23 -maxrate 12M -bufsize 24M`.
- Smooth transitions: crossfade, dissolve and smooth slides; a fade through black into PART cards.
- SFX only on PART cards, big number reveals, map entries, receipts and stamps, at most one every 18 s, and never in place of the music. Music bed runs the whole video at about -31 LUFS (VO -16), dropping to silence just before each PART card.
- Footage is labelled "ILLUSTRATIVE FOOTAGE". Credits are in each `credits.md` and `stills-credits.md`.
- Keys stay in GitHub Secrets. Kit SFX are never committed.
