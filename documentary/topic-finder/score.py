"""Rank History Invoice topics. Usage: python score.py topics.json > ranked.md"""
import json, sys
d = json.load(open(sys.argv[1] if len(sys.argv) > 1 else "topics.json", encoding="utf-8"))
w = d["weights"]; mx = 5 * sum(w.values())
rows = []
for t in d["topics"]:
    s = sum(t["scores"][k] * w[k] for k in w)
    if t.get("flag"): s -= 5  # overlap / same-story penalty
    rows.append((s, t))
rows.sort(key=lambda r: (-r[0], -r[1]["scores"]["peg"]))
print(f"# Ranked topics ({d['updated']}), max {mx}\n")
print("| Rank | ID | Score | Title | Type | Losses | Peg |")
print("|---|---|---|---|---|---|---|")
for i, (s, t) in enumerate(rows, 1):
    print(f"| {i} | {t['id']} | {s} | {t['title']} | {t['type']} | {', '.join(t['losses'])} | {t['peg']} |")
