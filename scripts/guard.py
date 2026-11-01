#!/usr/bin/env python3
"""Guard: fast checks run before every commit and in CI. Exit 1 on any failure."""
import json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
errors, warnings = [], []

REQUIRED = ["CLAUDE.md", "brain/brand.md", "brain/rules.md", "brain/host.md", "brain/goals.json",
            "brain/status.json", "brain/plan.json", "brain/ideas.json", "brain/learnings.md",
            "brain/accounts.md", "brain/competitors/landscape.md"]
for f in REQUIRED:
    if not (ROOT / f).exists():
        errors.append(f"missing required file: {f}")

for p in list((ROOT / "brain").glob("*.json")) + list((ROOT / "videos").glob("*/spec.json")):
    try:
        json.loads(p.read_text())
    except Exception as e:
        errors.append(f"bad JSON {p.relative_to(ROOT)}: {e}")

try:
    st = json.loads((ROOT / "brain/status.json").read_text())
    if len(st.get("today", [])) > 3:
        errors.append("brain/status.json: more than 3 to-dos today")
except Exception:
    pass

SECRET = re.compile(r"(sk-[A-Za-z0-9_-]{20,}|AIza[0-9A-Za-z_-]{30,}|ghp_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|xox[abp]-[A-Za-z0-9-]{10,})")
for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts or p.suffix.lower() in {".mp4", ".mp3", ".wav", ".jpeg", ".jpg", ".png", ".ttf", ".onnx", ".bin"}:
        continue
    try:
        txt = p.read_text(errors="ignore")
    except Exception:
        continue
    if SECRET.search(txt):
        errors.append(f"possible secret in {p.relative_to(ROOT)}")

LOG = re.compile(r"^\d{4}-\d{2}-\d{2}-\d{4}-[a-z-]+-[a-z0-9-]+\.md$")
for p in (ROOT / "brain/log").glob("*.md"):
    if not LOG.match(p.name):
        warnings.append(f"log file name not in YYYY-MM-DD-HHMM-role-slug.md form: {p.name}")

for v in (ROOT / "videos").glob("*/"):
    if not (v / "brief.md").exists():
        warnings.append(f"{v.name}: no brief.md")
    if (v / "script.md").exists() and not (v / "facts.md").exists():
        warnings.append(f"{v.name}: script without facts.md")
    if (v / "upload.md").exists() and not (v / "licences.md").exists():
        errors.append(f"{v.name}: upload pack without licences.md")
    s = v / "script.md"
    if s.exists() and "[CHECK" in s.read_text():
        warnings.append(f"{v.name}: script still has [CHECK] items")

for w in warnings: print("WARN ", w)
for e in errors: print("ERROR", e)
print(f"guard: {len(errors)} error(s), {len(warnings)} warning(s)")
sys.exit(1 if errors else 0)
