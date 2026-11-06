"""Run on Hammad's PC (the cloud cannot reach Google/Reddit/YouTube).
Pulls: Google Trends daily trending searches (US, GB, CA, AU, IN, PK),
YouTube + Google autocomplete for our seed questions, and Reddit question
posts (Quora-style "why / will / what happens" questions).
Usage:  python pc_trends.py            -> writes trends-YYYY-MM-DD.json next to this file
Only the Python standard library is used."""
import json, re, datetime, pathlib, urllib.request, urllib.parse, xml.etree.ElementTree as ET

UA = {"User-Agent": "history-invoice-topic-finder/1.0"}
GEOS = ["US", "GB", "CA", "AU", "IN", "PK"]
SEEDS = ["what happens if", "will gas prices", "why is food", "strait of hormuz", "iran war",
         "world war 3", "oil price", "rare earth", "sanctions", "red sea", "diesel shortage",
         "food crisis", "heating bill", "tariffs", "china taiwan", "russia ukraine", "cost of war", "casualties", "shortage", "refugees"]
# Reddit blocks unauthenticated requests (403, 2026-11-06); kept for when an official API app exists.
SUBS = ["geopolitics", "economics", "AskEconomics", "worldnews", "explainlikeimfive", "UKPersonalFinance"]
THEME = re.compile(r"\b(?:war|iran|israel|russia|ukraine|china|taiwan|oil|gas|fuel|diesel|hormuz|red sea|houthi|"
                   r"sanction|tariff|price|inflation|food|wheat|fertili[sz]er|rare earth|nuclear|strike|missile|"
                   r"ship|tanker|opec|dollar|gold|recession|refugee|famine|blockade|embargo|casualt(?:y|ies)|refugee|shortage|blackout|evacuat\w*|displaced|destroyed|invasion|territory|heritage|conscript\w*)(?:s|es)?\b", re.I)

def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=20) as r:
        return r.read().decode("utf-8", "replace")

def trends(geo):
    root = ET.fromstring(get(f"https://trends.google.com/trending/rss?geo={geo}"))
    ns = {"ht": "https://trends.google.com/trending/rss"}
    out = []
    for it in root.iter("item"):
        t = it.findtext("title"); tr = it.findtext("ht:approx_traffic", default="", namespaces=ns)
        news = [n.findtext("ht:news_item_title", namespaces=ns) for n in it.findall("ht:news_item", ns)]
        out.append({"q": t, "traffic": tr, "news": news[:2], "on_theme": bool(THEME.search(t + " " + " ".join(filter(None, news))))})
    return out

def suggest(q, yt):
    url = "https://suggestqueries.google.com/complete/search?client=firefox&hl=en" + ("&ds=yt" if yt else "") + "&q=" + urllib.parse.quote(q)
    return json.loads(get(url))[1]

def reddit(sub):
    d = json.loads(get(f"https://www.reddit.com/r/{sub}/top.json?t=week&limit=50"))
    qs = []
    for c in d["data"]["children"]:
        p = c["data"]; t = p["title"]
        if ("?" in t or re.match(r"(why|how|will|what|is|are|could|should)\b", t, re.I)) and THEME.search(t):
            qs.append({"q": t, "score": p["score"], "comments": p["num_comments"], "sub": sub})
    return qs

res = {"date": datetime.date.today().isoformat(), "trends": {}, "yt_suggest": {}, "google_suggest": {}, "questions": [], "errors": []}
for g in GEOS:
    try: res["trends"][g] = trends(g)
    except Exception as e: res["errors"].append(f"trends {g}: {e}")
for s in SEEDS:
    for yt, key in ((True, "yt_suggest"), (False, "google_suggest")):
        try: res[key][s] = suggest(s, yt)
        except Exception as e: res["errors"].append(f"{key} {s}: {e}")
for s in SUBS:
    try: res["questions"] += reddit(s)
    except Exception as e: res["errors"].append(f"reddit {s}: {e}")
res["questions"].sort(key=lambda x: -x["comments"])
out = pathlib.Path(__file__).with_name(f"trends-{res['date']}.json")
out.write_text(json.dumps(res, indent=1, ensure_ascii=False), encoding="utf-8")
on = [t["q"] for g in res["trends"].values() for t in g if t["on_theme"]]
print(f"saved {out}\non-theme trending searches: {len(on)}: {', '.join(dict.fromkeys(on))[:600]}")
print(f"top questions: {[q['q'] for q in res['questions'][:8]]}\nerrors: {len(res['errors'])}")
