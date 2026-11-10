#!/usr/bin/env python3
"""Download small reference stills (Pixabay webformat, ~1280px) for storyboard panels.
Key from PIXABAY_API_KEY env only. Input videos/<id>/storyboard/stills.json -> [{"code","query"}].
Output videos/<id>/storyboard/stills/<code>.jpg + stills-credits.md. Storyboard reference only."""
import json, os, sys, time, pathlib, urllib.parse, urllib.request
key = os.environ.get("PIXABAY_API_KEY") or sys.exit("PIXABAY_API_KEY not set")
vd = pathlib.Path(sys.argv[1]); sd = vd / "storyboard"; out = sd / "stills"; out.mkdir(parents=True, exist_ok=True)
rows = ["| Code | Query | Pixabay id | Creator | Page |", "|---|---|---|---|---|"]
for it in json.loads((sd / "stills.json").read_text()):
    q = {"key": key, "q": it["query"][:100], "image_type": "photo", "orientation": "horizontal", "safesearch": "true", "per_page": max(5, int(it.get("n", 1)))}
    UA = {"User-Agent": "history-invoice-storyboard/1.0"}
    try:
        with urllib.request.urlopen(urllib.request.Request("https://pixabay.com/api/?" + urllib.parse.urlencode(q), headers=UA), timeout=60) as r:
            hits = json.loads(r.read()).get("hits", [])
    except Exception as e:
        print("search failed", it["code"], e); rows.append(f"| {it['code']} | {it['query']} | ERROR | | |"); continue
    if not hits:
        rows.append(f"| {it['code']} | {it['query']} | NOT FOUND | | |"); continue
    n = int(it.get("n", 1))  # n>1: save candidates <code>_1..n for a human/Claude pick
    for k, h in enumerate(hits[:n], 1):
        name = it["code"] if n == 1 else f"{it['code']}_{k}"
        url = h.get("largeImageURL") or h["webformatURL"]
        req = urllib.request.Request(url, headers={"User-Agent": "history-invoice-storyboard/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                (out / f"{name}.jpg").write_bytes(r.read())
        except Exception as e:
            print("download failed", name, e); rows.append(f"| {name} | {it['query']} | DL ERROR | | |"); continue
        rows.append(f"| {name} | {it['query']} | {h['id']} | {h.get('user','')} | {h.get('pageURL','')} |")
    time.sleep(1)
cf = sd / "stills-credits.md"; prev = cf.read_text().split("\n")[4:] if cf.exists() else []
cf.write_text("# Storyboard stills (Pixabay Content License)\n\n" + "\n".join(rows + [l for l in prev if l.strip()]) + "\n")
print("stills done")
