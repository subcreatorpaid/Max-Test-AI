# INV-023 shot plan v1: code -> shots. ("G",) graphic from spec23 · ("F", what) video · ("S", what) photo. Second entry = cutaway.
# Every cutaway matches the words on its half of the line (clips already picked by eye for INV-011/012/017, reused here).
import runpy, pathlib
R = runpy.run_path(str(pathlib.Path(__file__).parent / "script_v1.py"))["R"]
# code -> (source video folder, source clip name, what it shows)
SRC = {'P1-08': ('INV-011-russia-fuel', 'P3-11x', 'tanker under way'), 'P2-06': ('INV-011-russia-fuel', 'P6-03x', 'motorway traffic'), 'P2-07': ('INV-011-russia-fuel', 'P3-09bx', 'city traffic'), 'P5-05': ('INV-017-nuclear-satellite', 'P3-10x', 'power lines'), 'P6-06': ('INV-011-russia-fuel', 'CO-03x', 'petrol station at night')}
PHOTO = {'P4-07': ('INV-017-nuclear-satellite', 'P6-09x', 'kitchen, household bills')}
V = {}
for r in R:
    code = r[0]
    if code in SRC: V[code] = [("G",), ("F", SRC[code][2])]
    elif code in PHOTO: V[code] = [("G",), ("S", PHOTO[code][2])]
    else: V[code] = [("G",)]
if __name__ == "__main__":   # copy the picked clips in and write picks.json (URLs for the 1080p cloud render)
    import json, shutil
    root = pathlib.Path(__file__).resolve().parents[2] / "videos"; me = root / "INV-023-1979-oil"
    picks = {}
    for code, (vid, name, what) in SRC.items():
        src = root / vid / "clips" / "picked" / f"{name}.mp4"; shutil.copy(src, me / "clips" / "picked" / f"{code}x.mp4")
        pj = json.load(open(root / vid / "clips" / "picks.json"))["picks"]; p = dict(pj[name]); p["what"] = what; p["from"] = f"{vid}/{name}"; picks[f"{code}x"] = p
    for code, (vid, name, what) in PHOTO.items():
        shutil.copy(root / vid / "storyboard" / "picks" / f"{name}.jpg", me / "storyboard" / "picks" / f"{code}x.jpg")
    json.dump({"picks": picks}, open(me / "clips" / "picks.json", "w"), indent=1); print(len(picks), "clips", len(PHOTO), "photos")
