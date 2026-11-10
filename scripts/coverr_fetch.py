#!/usr/bin/env python3
"""Fetch stock video (and optionally music) from Coverr for a video's B-roll list.

The key is read ONLY from the COVERR_API_KEY environment variable (GitHub Secret in Actions,
or a local env var on Hammad's PC), sent in the x-api-key header. Never printed or saved.

Input: videos/<id>/broll.json (same list as pixabay_fetch.py). Items with "source": "coverr"
are fetched here; if no item names a source, every item is tried and only files not
already fetched by Pixabay are downloaded.
Optional: videos/<id>/music.json -> [{"code": "BED-01", "query": "dark ambient tension"}]
Output: videos/<id>/broll/<code>-coverr<id>.mp4, videos/<id>/music/<code>-coverr<id>.mp3,
        and credits rows in videos/<id>/broll/coverr-credits.md (copy into licences.md).

Coverr API terms (api.coverr.co/docs): show users where videos come from (logo/credit);
the free API is "free as long as you don't ... re-sell or use the videos for commercial use".
CHECK coverr.co/license with Hammad before using Coverr clips in a monetised upload.
"""
import json, os, sys, time, pathlib, urllib.parse, urllib.request

BASE = "https://api.coverr.co"

def call(path, key, params=None, method="GET"):
    url = BASE + path + ("?" + urllib.parse.urlencode(params) if params else "")
    req = urllib.request.Request(url, method=method, headers={"x-api-key": key, "User-Agent": "history-invoice-broll/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
        return json.loads(body) if body else None

def download(url, dest):
    req = urllib.request.Request(url, headers={"User-Agent": "history-invoice-broll/1.0"})
    with urllib.request.urlopen(req, timeout=180) as r:
        dest.write_bytes(r.read())

def main(video_dir, music_only=False):
    key = os.environ.get("COVERR_API_KEY")
    if not key:
        sys.exit("COVERR_API_KEY is not set (add it as a GitHub Secret or a local env var).")
    vd = pathlib.Path(video_dir)
    out = vd / "broll"; out.mkdir(exist_ok=True)
    credits = ["# Coverr credits (check coverr.co/license; credit Coverr in the description)\n",
               "| Code | Query | Coverr id | Title | File |", "|---|---|---|---|---|"]
    items = [] if music_only else (json.loads((vd / "broll.json").read_text()) if (vd / "broll.json").exists() else [])
    named = any("source" in i for i in items)
    for it in items:
        if named and it.get("source") != "coverr":
            continue
        code = it["code"]
        if not named and any(out.glob(f"{code}-*")):
            continue  # Pixabay already covered this shot
        hits = call("/videos", key, {"query": it["query"][:100], "page_size": 5, "urls": "true"}).get("hits", [])
        hit = next((h for h in hits if h.get("duration", 0) >= it.get("min_seconds", 6) and h.get("urls", {}).get("mp4_download")), None)
        if not hit:
            credits.append(f"| {code} | {it['query']} | NOT FOUND | | |"); continue
        fn = f"{code}-coverr{hit['id']}.mp4"
        download(hit["urls"]["mp4_download"], out / fn)
        try:
            call(f"/videos/{hit['id']}/stats/downloads", key, method="PATCH")  # recommended download ping
        except Exception:
            pass
        credits.append(f"| {code} | {it['query']} | {hit['id']} | {hit.get('title','')} | {fn} |")
        time.sleep(1)
    if (vd / "music.json").exists():
        mo = vd / "music"; mo.mkdir(exist_ok=True)
        for it in json.loads((vd / "music.json").read_text()):
            hits = call("/audios", key, {"query": it["query"][:100], "page_size": 5}).get("hits", [])
            hit = next((h for h in hits if not h.get("isPremium") and h.get("urls", {}).get("masterDownload")), None)
            if not hit:
                credits.append(f"| {it['code']} | {it['query']} | NOT FOUND (music) | | |"); continue
            fn = f"{it['code']}-coverr{hit['id']}.mp3"
            download(hit["urls"]["masterDownload"], mo / fn)
            credits.append(f"| {it['code']} | {it['query']} | {hit['id']} | {hit.get('title','')} (music) | music/{fn} |")
            time.sleep(1)
    (out / "coverr-credits.md").write_text("\n".join(credits) + "\n")
    print(f"done -> {out}")

if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        sys.exit("usage: coverr_fetch.py videos/<id> [--music-only]")
    main(args[0], music_only="--music-only" in sys.argv)
