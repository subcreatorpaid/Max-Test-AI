#!/usr/bin/env python3
"""Fetch stock B-roll (video, or stills as a fallback) from Pixabay for a video's coded B-roll list.

The key is read ONLY from the PIXABAY_API_KEY environment variable (a GitHub Secret in Actions,
or a local env var on Hammad's PC). It is never printed, logged or written to disk.

Input: videos/<id>/broll.json  ->  [{"code": "P1-03", "query": "oil tanker sea", "min_seconds": 8, "type": "video"}, ...]
Output: videos/<id>/broll/<code>-pixabay<id>.mp4|.jpg  +  videos/<id>/broll/credits.md (licence log for licences.md)

Note: the Pixabay API serves images and videos only. Music and SFX are not in the API,
so they still come from the YouTube Audio Library / our own synthesized SFX / the licensed kit.
Pixabay API rules: cache results, no hotlinking, no mass downloading: keep lists to what the video needs.
"""
import json, os, sys, time, pathlib, urllib.parse, urllib.request

API = {"video": "https://pixabay.com/api/videos/", "image": "https://pixabay.com/api/"}

def get(url):
    req = urllib.request.Request(url, headers={"User-Agent": "history-invoice-broll/1.0"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()

def search(key, kind, query, n=5):
    params = {"key": key, "q": query[:100], "per_page": max(3, n), "safesearch": "true"}
    if kind == "image":
        params.update({"image_type": "photo", "orientation": "horizontal", "min_width": 1920})
    return json.loads(get(API[kind] + "?" + urllib.parse.urlencode(params))).get("hits", [])

def pick_video(hits, min_s):
    for h in hits:
        if h.get("duration", 0) >= min_s:
            v = h["videos"]
            for size in ("large", "medium"):
                if v.get(size, {}).get("url") and v[size].get("width", 0) >= 1920:
                    return h, v[size]["url"]
    return None, None

def main(video_dir):
    key = os.environ.get("PIXABAY_API_KEY")
    if not key:
        sys.exit("PIXABAY_API_KEY is not set (add it as a GitHub Secret or a local env var).")
    vd = pathlib.Path(video_dir)
    items = json.loads((vd / "broll.json").read_text())
    out = vd / "broll"; out.mkdir(exist_ok=True)
    credits = ["# Pixabay B-roll credits (Pixabay Content License; log these in licences.md)\n",
               "| Code | Query | Pixabay id | Creator | Page | File |", "|---|---|---|---|---|---|"]
    for it in items:
        code, q = it["code"], it["query"]
        kind = it.get("type", "video")
        hit, url = None, None
        if kind == "video":
            hit, url = pick_video(search(key, "video", q), it.get("min_seconds", 6))
        if not url:  # still-image fallback (the process allows stills when no clip exists)
            hits = search(key, "image", q)
            if hits:
                hit, url, kind = hits[0], hits[0].get("largeImageURL"), "image"
        if not url:
            credits.append(f"| {code} | {q} | NOT FOUND | | | |"); continue
        ext = ".mp4" if kind == "video" else ".jpg"
        fn = f"{code}-pixabay{hit['id']}{ext}"
        (out / fn).write_bytes(get(url))
        credits.append(f"| {code} | {q} | {hit['id']} | {hit.get('user','')} | {hit.get('pageURL','')} | {fn} |")
        time.sleep(1)  # stay well under the rate limit
    (out / "credits.md").write_text("\n".join(credits) + "\n")
    print(f"done: {len(items)} items -> {out}")

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else sys.exit("usage: pixabay_fetch.py videos/<id>"))
