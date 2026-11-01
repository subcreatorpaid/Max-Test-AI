# Making Max in Google Vids (step by step)

Checked 2026-11-01 against Google's own pages (sources at the bottom). Re-check if a menu name differs.

## How the work is split (Hammad's plan, 2026-11-01)
1. **Max's clips:** Claude writes the scene prompts (`videos/<slug>/vids-scenes.md`). Hammad makes each scene in Google Vids with the Max avatar, and hands back **one MP4 per scene**, with Max's own voice and lip sync already in it.
2. **Screen narration:** a separate audio file for all the `[VO]` lines (`videos/<slug>/voiceover.md`). Hammad makes it in one go.
3. **Animations:** made locally with Claude (Motion Graphics MAX kit).
4. **Edit:** CapCut. Claude assembles the edit from the files and returns the final video for Hammad's OK.

## What Google Vids can and can't do
| | |
|---|---|
| Custom avatar from an image | Yes: **AI avatar > Design a custom avatar > Upload image**. Best with a 16:9 picture, clear well-lit face, plain background. |
| Custom avatar from a form | Yes: **Build from scratch** (gender, age, background, outfit) then **Refine selected** with words. |
| Length | Up to **60 s per avatar video**. Split longer lines into scenes. |
| Monthly limit | Google says many users get about **25 avatar generations a month**. A video needs about 6-9, plus retakes. |
| Voices | Google's own Gemini voices only (pick with **Select voice**). You **can't** upload our Kokoro voice. Pace, pauses and emotion via audio tags: type `[` in the script. |
| Acting | Newer feature: custom avatars can be put into generated clips and told to walk, talk, use objects. |
| Reuse | The avatar is saved **inside that Vids file**. To reuse, **make a copy** of the master file. |
| Plan | Works on Google AI Pro (Hammad's Gemini plan). |
| "Personal avatar" | Not for Max. That one scans **your own** face and voice by phone, English only, and is not offered in the UK/EEA. |
| Quality | Third-party reviews report 720p, 16:9 or 9:16. Fine for a host inset; screen recordings stay 1080p. |

## One-time setup (about 20 minutes)

### Step 1. Make Max's 16:9 reference picture (Gemini app, Nano Banana)
`brain/host/host-hero.jpeg` is tall (9:16). Vids wants wide. In the Gemini app, upload `host-hero.jpeg` and paste the prompt for the look Hammad picked:

- **A. Brand-blue Max:** `Same man as this photo, same face, hair and stubble. Now wearing an open electric-blue (#2f6bff) overshirt over a plain white crew-neck tee. Seated at a clean white desk in a bright modern home studio: laptop, a monitor behind him showing a software screen, one green plant, a soft blue glow on the back wall. Chest-up, centred, looking straight at the camera, warm slight smile, mouth closed. Natural daylight, sharp, no text, no logos. Wide 16:9 landscape.`
- **B. Tech-lab Max:** `Same man as this photo, same face, hair and stubble. Now wearing thin clear-frame glasses and a plain black crew-neck tee. Darker modern tech studio behind him with a blue LED rim light on one side and a warm yellow light on the other, shelves softly out of focus. Chest-up, centred, looking straight at the camera, calm slight smile, mouth closed. Sharp, no text, no logos. Wide 16:9 landscape.`
- **C. Today's Max:** `Same man, same clothes and same room as this photo. Recompose as a wide 16:9 landscape: chest-up, centred, looking straight at the camera, slight smile, mouth closed, window and plants behind him. Natural daylight, sharp, no text.`

**Hammad picked A (2026-11-01).** Make 3-4, pick the one that looks most like the face in `host-hero.jpeg`. Save it as `max-vids-ref.png` and send it to Claude (it goes into `brain/host/`).

### Step 2. Create the avatar (Google Vids, Chrome on a computer)
1. Open **vids.google.com** > new blank video. Name the file **Max master**.
2. Click **AI avatar** > **Design a custom avatar** > **Upload image** > **Upload** > choose `max-vids-ref.png`.
3. If it doesn't look like Max, click **Recreate**. When close, **Refine selected** and type small fixes, e.g. `keep the same face; slightly shorter beard; keep the shirt exactly the same`.
4. **Select voice:** play the male voices, pick a calm, warm, mid-pitch American one (closest to our sample `brain/host/voice-sample-michael.mp3`). Write the voice name down and tell Claude; it goes in `brain/host.md`.
5. Name it **Max Reed** > **Save** > **Select**.
6. Test line: `Max here. Yes, I'm an AI. Let's see if it actually works.` > **Play preview** > **Insert**. If face or voice is off, fix now; every video copies from this file.

## Every video (about 30-45 minutes)
1. Open `videos/<slug>/vids-scenes.md` (Claude writes it with the script).
2. In Drive: **Max master** > **Make a copy** > name it `<slug> Max`.
3. For each scene in the table: **AI avatar** > **Change** > pick **Max Reed** > paste the **Line**, add the audio tags shown (type `[` to choose them) > **Play preview** > **Insert**. One scene per Vids scene.
4. If a line comes out wrong, edit the script, then **Current scene** > **Update** (it costs a generation, so check the text first).
5. Download each scene as its own MP4 (**File > Download**, or download the whole video and tell Claude; Claude can cut it into scenes). Name them exactly like the table: `max-01-hook.mp4`, `max-02-intro.mp4` ...
6. Put them with the screen recordings and the narration audio, and tell Claude.

## Narration (separate audio)
`videos/<slug>/voiceover.md` has every `[VO]` line in order as one block. Make it in one go with the **same Google voice as Max** (Hammad picked "one Google voice everywhere", 2026-11-01). If the `GEMINI_API_KEY` secret is set, `scripts/tts.py` can also make it automatically, export one audio file `voiceover.mp3` (or one per chapter).

## Rules that still apply
- Every upload ticks YouTube's "altered or synthetic content" box; About page says Max is an AI.
- Max's look, set and voice are locked in `brain/host.md`. Changes need Hammad's OK.
- Never type real people's names into an avatar prompt or make Max look like a real person.

## Sources
- Use AI avatars in Google Vids: https://support.google.com/docs/answer/16334946
- Create and refine custom avatars (Apr 2026): https://workspaceupdates.googleblog.com/2026/04/create-and-refine-custom-avatars-in-Google-Vids.html
- Enhanced AI avatars (Jun 2026): https://workspaceupdates.googleblog.com/2026/06/enhanced-ai-avatars-vids.html
- Personal avatar (Jul 2026): https://support.google.com/docs/answer/16970930
- 720p / 16:9-9:16 (third party): https://www.aicloudit.com/blog/news/custom-avatars-and-veo-3-1-strategic-breakdown-of-google-vids/
