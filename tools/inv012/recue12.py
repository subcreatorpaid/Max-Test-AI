# recompute {cue} times from the script without re-recording the voice (same formula as vo12: char offset within the sentence span)
import sys, re, json, runpy
P = runpy.run_path(sys.argv[1])["PARTS"]; jp = sys.argv[2]; data = json.load(open(jp))
for _, _, rows in P:
    for r in rows:
        code = r[0]; part = code.split('-')[0]; sg = data['segs'][part]
        sents = sg['sents'][code]; ss = [x for x in re.split(r'(?<=[.!?])\s+', r[1]) if x.strip()]
        assert len(ss) == len(sents), (code, len(ss), len(sents))
        cues = []
        for (t0, t1), s_ in zip(sents, ss):
            plain = s_.replace('{', '').replace('}', ''); L = max(1, len(plain)); dur = t1 - t0
            for m in re.finditer(r'\{([^}]*)\}', s_):
                ci = m.start() - 2*sum(1 for _ in re.finditer(r'\{[^}]*\}', s_[:m.start()]))
                cues.append(round(t0 + 0.06 + dur*ci/L, 3))
        sg['cues'][code] = cues
json.dump(data, open(jp, 'w'), indent=1); print("recued")
