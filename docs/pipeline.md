# Pipeline: one video, start to finish

Hammad types one command, e.g. "Make a video about X". The team runs the chain and stops only at the 3 OK gates.

| # | Step | Role / skill | Output | Gate |
|---|---|---|---|---|
| 1 | Research demand, competitors, facts | researcher | `brain/research/<date>_<topic>.md`, `videos/<slug>/facts.md` | |
| 2 | Brief + goal-lock + hooks | strategist, goal-lock, hook-lab | `brief.md` | |
| 3 | Story arc | storyteller | `story.md` | |
| 4 | Script + narration | scriptwriter, script-qa | `script.md`, `narration.txt` | |
| 5 | Storyboard, recordings list, Flow prompts | director, storyboard | `storyboard.md`, `recordings.md`, `flow-prompts.md` | **1: storyboard OK** |
| 6 | Hammad records screens (`recordings.md`), makes Max clips in Google Vids (`vids-scenes.md`), records the narration (`voiceover.md`) | Hammad | `footage/R*.mp4`, `footage/max-*.mp4`, `audio/voiceover.mp3` | |
| 7 | Motion graphics + SFX/music (kit, on Hammad's PC) | creator | `footage/G*.mp4`, SFX track | |
| 7b | Full edit: `edit.json` -> preview | editor | `preview_480p.mp4`, `edit-list.md` | |
| 8 | Hammad watches the preview | Hammad | | **2: review OK** |
| 9 | Final render 1080p, on Hammad's PC | editor | `final_1080p.mp4`, `final.srt` | |
| 10 | Titles + thumbnails scored | packager | `title-thumb.md` | |
| 11 | Guard + pre-flight audit | guard | table in `upload.md` | |
| 12 | Upload pack, upload as private/scheduled | publisher | `upload.md` | **3: final upload OK** |
| 13 | 48 h + 7 day review | analytics-review | `review-*.md`, `brain/learnings.md` | |

Footage Hammad supplies goes in `videos/<slug>/footage/` (or a shared Drive folder until the repo is private). Narration: Hammad's one file `audio/voiceover.mp3` (Max's voice). Kokoro placeholder only for early previews. CapCut: no API and encrypted drafts, so Claude delivers the finished MP4 + `edit-list.md` for any manual tweak in CapCut.

The Motion Graphics MAX kit and its sounds live on Hammad's PC only (licence + public repo). Previews: GitHub Actions. Graphics, sound pass and final render: Hammad's PC.
