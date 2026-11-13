#!/usr/bin/env python3
"""G16 (new) and G21: at E1 no saved-page text is shown, M30 names the file, and M31 copies the full name and
date of birth exactly, only when the saved page has that line. Usage: check_e1.py <case.md> <transcript.md>"""
import json, re, sys
case, tr = sys.argv[1], sys.argv[2]
c = open(case).read()
lines = [l for l in c.splitlines() if "read the newest page named exactly" in l]
read = json.loads(lines[0][lines[0].index("{"):]).get("data", {}).get("read") if lines else None
if not read:
    print("G16/G21 n/a: no saved page"); sys.exit(0)
saved = [l.strip() for l in read["text"].splitlines() if l.strip()]
t = open(tr).read()
cut = t.find("What are they wearing today")
if cut < 0:
    print("G16/G21 FAIL: clothing question not found"); sys.exit(1)
turns = re.split(r"(?m)^(?=T[\d?]+ )", t[:cut])
asst = "\n".join(x for x in turns if re.match(r"T[\d?]+ ASSISTANT TO CAREGIVER", x))
leaked = [l for l in saved if len(l) > 25 and l in asst]
fname = read["file"]
m30 = ("Your saved page from" in asst) and (fname in asst)
m = re.search(r"^Full name and date of birth: (.*) \(You said\)$", read["text"], re.M)
call = re.findall(r"For the call: ([^\n\"]*?)\.?\"?$", asst, re.M)
if m:
    m31 = len(call) == 1 and call[0].rstrip(".") == m.group(1).rstrip(".")
else:
    m31 = len(call) == 0
bad = (len(leaked) > 0) + (not m30) + (not m31)
print("G16/G21 %s: page lines shown %d, M30 names file %s, M31 %s (want %s, got %s)" % (
    "PASS" if bad == 0 else "FAIL", len(leaked), m30, "ok" if m31 else "WRONG",
    repr(m.group(1)) if m else "none", call))
sys.exit(1 if bad else 0)
