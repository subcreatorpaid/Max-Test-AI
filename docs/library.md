# The Invoice: graphics, animation, SFX and B-roll library

**Library v1, 2026-11-04, after INV-002 (Round Two, first 10 min).** Update it after every video (see NUMBERING.md section 4). Never delete entries: mark them `retired` with the reason.

## A. Graphics and animations (code in this folder)
| ID | Function (file) | What it shows | Parameters | First used |
|---|---|---|---|---|
| G01 | `frame()` S1 (look.py) | Terrain relief push-in from the strait to a place, with orange pulse rings | lat/lon, pulse times | INV-002 CO |
| G02 | `frame()` S2 (look.py) | Serif quote card over a blurred, darkened map | quote, speaker, source | INV-002 CO |
| G03 | `island()` (v3_add.py) | Close terrain with markers: weapons red, water cyan, dashed gradient link with flowing pulse, missile range rings | markers | INV-002 CO |
| G04 | HUD reticle + shutter (v3_add.py) | Viewfinder / "one frame" moment | time | INV-002 CO |
| G05 | `stamp_spent()` (v3_add.py) | Crimson Bebas grunge stamp, 140→100% scale, 3-frame shake, ink thud | word | INV-002 CO |
| G06 | shockwave rings (v3.py s9) | Seismic rings, active line lit, earlier lines at 40% | ring list | INV-002 CO |
| G07 | flash transition (v3.py) | Motion-blur push plus optical flash between scenes | t range | INV-002 CO |
| G08 | typewriter text (v3.py) | Left-to-right typing synced to VO, with key clicks | text, start, wpm | INV-002 CO |
| G09 | `s_part` (gfx.py) | PART card: huge faded number, title, serif subline | n, title, sub | INV-002 P1/P2 |
| G10 | `s_nv` (gfx.py) | Teal night-vision perspective terrain with a strike flash | label | graphics pack |
| G11 | `s_targets` (gfx.py) | Glowing Gulf border map with named target dots | targets list | graphics pack |
| G12 | `s_red` (gfx.py) | Iran in red with a ring, two Bebas label strips | s1, s2 | INV-002 P2 |
| G13 | `s_globe` (gfx.py) | Orthographic globe with trade arcs from Hormuz | destinations | INV-002 P1 |
| G14 | `s_time` (gfx.py) | Three-point history timeline (years) | events | INV-002 P2 |
| G15 | `s_chart` (gfx.py) | Area or line price chart with labelled points | points | graphics pack |
| G16 | `g_strait` (ten.py) | Strait terrain with a measure line ("21 MILES") and two glowing shipping lanes | lanes, measure | INV-002 P1 |
| G17 | `g_number` (ten.py) | Big number card: kicker, number, serif line, optional faded comparison, tag | big, sub, kicker, tag, faded | INV-002 P1/P2 |
| G18 | `g_bars` (ten.py) | Two bars (door vs windows) with a flicker and a "WINDOWS HIT" reveal | values | INV-002 P1 |
| G19 | `g_door` (ten.py) | Gulf border map, "only door" ring on Hormuz, side shade, slow push | ring place | INV-002 P1 |
| G20 | `g_war_tl` (ten.py) | Dated event timeline (6 events) that dims the past | events | INV-002 P2 |
| G21 | `g_stack` (ten.py) | Stacked cost bar (munitions / operations / losses) | segments | INV-002 P2 |
| G22 | `g_gdp` (ten.py) | Diverging country bars (IMF growth) | country, value | INV-002 P2 |
| G23 | `g_attacks` (ten.py) | Three big stats in a row | stats | INV-002 P2 |
| G24 | `g_bridge` (ten.py) | Channel name, tagline and subscribe button | | INV-002 BR |
| G25 | `g_photo` (ten.py) | Still image with Ken Burns and overlay text | image, overlay | INV-002 P1 |
| G26 | `overlay()` + `broll()` (ten.py) | Footage grade, slow pan or push, slow-mo if short, text PNG with shade, tag line | clip, lines, tag, move | INV-002 all |

**Planned for v2 (kit quality bar):** count-up numbers with ticks, a light sweep across big type, card drift and push, rotating text positions, and new transitions (flash cut, whip with blur, light-edge wipe, match cut by shape, iris).

## B. SFX map (Motion Graphics MAX kit; files stay on Hammad's PC, never copied into shared folders)
| Moment | Kit sounds | Gain |
|---|---|---|
| Map or terrain shot in | `move/whoosh-deep/whoosh_deep_metal_01` + `tech/scan/scan_01` | 0.08 / 0.035 |
| Footage cut | `move/whoosh/*` (rotate whoosh_deep_01, _02, whoosh_clean_01) + `ui/tick/tick_fine_01` | 0.07 / 0.03 |
| Number card | `move/whip/whip_air_01` + `hit/land/land_card_01` + `tech/data/counter_roll_01` | 0.07 / 0.12 / 0.05 |
| Chart or bars | `move/whoosh/whoosh_clean_01` + `tech/chart/chart_grow_01` | 0.06 / 0.09 |
| PART card | `move/reverse/reverse_cymbal_01` (ending on the cut) + `hit/sub-drop/sub_drop_01` + `hit/land/land_stone_01` | 0.10 / 0.32 / 0.12 |
| Big reveal (red map, "windows hit", "rule broke") | `hit/sub-drop/sub_drop_808_01` + `hit/land/land_stone_01` | 0.28 / 0.12 |
| Into the bridge | `build/riser/riser_air_01` (ending on the cut) | 0.06 |
| Under everything | Synth drone bed (55 + 82.4 Hz + filtered noise), lifted on the bridge | 0.036 |
| Typing | `tech/type/type_soft_keys_01` | |

Mix: VO on top, loudnorm -16 LUFS, peak -1.5 dB.

## C. B-roll library (Hammad's downloads, in C:\Users\hamma\Documents\Picture)
| File id | Shows | Length | Used for | Notes |
|---|---|---|---|---|
| 11395713 | Tanker on a blue sea | 16 s | oil flow numbers | |
| 12399388 | Tankers in a strait with hills | 6.9 s | "1/4 of seaborne oil" | |
| 12816955 | Grey harbour with boats | 7.4 s | ships stuck in the Gulf | |
| 12859924 | Navy ship docked, aerial | 64 s | blockade | |
| 14603999 | Petrol station at night | | "everyone pays the price" | |
| 14807918 | Tanker loading at a terminal | 13.6 s | LNG / exports | |
| 15514264 | Night sea with lightning | 6 s | attacks month | |
| 15786241 | Harbour at night | 7.6 s | "unreliable", crew | Sydney landmarks visible: generic lines only |
| 16323403 | Trading screens | 25 s | world price | |
| 16622542 | Ship at night from above | 15.8 s | ships crossing dark | |
| 18692266 | Refinery at night, aerial | 106 s | bypass / industry | |
| 19217894 | Dark warehouse corridor | 10 s | stockpiles | |
| 4324080 | Oil storage tanks, aerial | 26 s | spare capacity | |
| 4462852 | Drone in the sky | 6.3 s | drone costs | consumer quadcopter: tag ILLUSTRATION |
| 4524511 | Counting dollars | 24 s | currency collapse | |
| 5121751 | Molten metal | 14 s | smelter | |
| 6540588 | Smoke over a city, aerial | 12 s | "the rule broke" | |
| 7317305 | Apartment block at dusk | 15 s | people who pay | |
| Not used yet | 13107027 budget jar · 13154470 dashboard · 14491148 tap · 15730063 airport board · 3010407 gas pump · 4121749 supermarket · 5981292 stressed woman with bills · 6963487 calculator · 7735861 desk with bills · 7821604 credit cards | | Part 5 / Receipt | |
| Stills | `iss064e046338.webp` Gulf from the ISS (NASA, public domain) · DVIDS bridge-crew screenshot (crop the arrows) | | | |

## D. Lessons log
- INV-002: footage with burned-in text overlays and an orange serif line looks premium. Number cards need motion after they build (kit bar). Grain at crf 20 makes huge files, so use crf 23 with maxrate 12M.
