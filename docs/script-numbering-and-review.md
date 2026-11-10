# The Invoice: script numbering + review system

The rule (Hammad, 2026-11-04): **whenever Hammad gives a script, number it, review it with this system, and update the library (graphics, animations, SFX, B-roll) every time.**

## 1. Video numbers
Each video gets `INV-NNN`, numbered in order of production, plus a short slug.

| No. | Slug | Title | Status |
|---|---|---|---|
| INV-001 | hormuz-never-reopens | What Happens If the Strait of Hormuz Never Reopens? | script v1 (merged into INV-002) |
| INV-002 | round-two | Round Two: The War That Already Spent Our Savings | first 10 min cut v1 |

Script files are named `INV-NNN-<slug>-script-vN.docx`, and every new version goes up by one (v1, v2...). Old versions are never overwritten.

## 2. Numbering inside a script
Each paragraph of narration gets a code, and that code is used everywhere: script, voiceover timing, storyboard, shot list, B-roll list and review notes.

`INV-002 · P1 · 07`, meaning video · part · paragraph.

- **Parts:** `CO` cold open, `BR` subscribe bridge, `P1`–`P9` parts, `RC` the Receipt / close.
- **Paragraphs:** 01, 02... inside each part, about 8–25 s of narration each (20–60 words).
- **Shot numbers:** one paragraph can hold 1–3 shots, coded `P1-07a`, `P1-07b`, `P1-07c`.
- **Facts:** every number in a paragraph points to a fact pack row, for example `[F23]`.
- **B-roll codes** follow the part: `CO-01`, `P1-03`, `P2-11` (same as the download list Hammad gets).

The numbered script is a table:

| Code | Narration | Words / sec | Facts | Shot(s) | Visual | On-screen text | Tag + source | SFX |

## 3. Script review (run on every script Hammad gives, before voice)
Score each part, and return a list of fixes with paragraph codes.

**A. Facts (hard checks: any fail blocks the voice step)**
1. Every number has a fact pack row with a source and date, and its tag (VERIFIED / REPORTED / ESTIMATE / ILLUSTRATION) is correct.
2. No invented specifics. AI drafts and pasted scripts are re-checked line by line.
3. No lines copied from Paycheckology or any other channel.
4. Claims vs reports are said out loud where it matters.

**B. Story and retention**
5. The hook pays off the title within 30 s. First line: a place, a time and a sound or number.
6. There's a rehook every 60–90 s, and each part ends with a specific question.
7. Each military or finance term turns into people, dollars or daily life within 2 sentences.
8. Sentences are under 20 words, and the pace is 130–145 wpm.
9. Nothing from the banned list (master-prompt-v3 section 6).

**C. Makeability (every paragraph must be showable)**
10. Each paragraph has a visual the library can make, or a B-roll a free stock site can give. If not, rewrite it for a map, chart or number card.
11. Every key number gets a number card, chart or on-screen text.
12. One hero (place or object) is carried through each part.

The output is a verdict per part (PASS / FIX), a list of fixes as `code · problem · fix`, and the updated numbered table.

## 4. After every video: update the library
After the final cut:
1. Add each new graphic or animation to `LIBRARY.md` (name, function, what it shows, parameters, first used in).
2. Add new kit SFX picks and their use to the SFX map.
3. Add the B-roll clips used, with search terms, so they can be reused.
4. Add one lesson line: what looked or sounded best, and what to drop.
5. Bump the library version and date at the top.
