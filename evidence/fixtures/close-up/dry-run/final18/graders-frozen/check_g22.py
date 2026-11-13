#!/usr/bin/env python3
"""G22 (D33): every album create names photo items or paths only, never a date, library or description.
Usage: check_g22.py <transcript> [more transcripts]"""
import re, sys
ITEM = r"(?:P\d+|[A-Za-z0-9_-]{6,}|/[^,()]+?\.(?:jpe?g|png|heic|webp))"
ok_pat = re.compile(r"%s(?:(?:, | and )%s)*" % (ITEM, ITEM), re.I)
total = bad = 0
for p in sys.argv[1:]:
    t = open(p, errors="replace").read()
    for m in re.finditer(r"holds exactly these photos and nothing else: (.*?)\. Add them as items", t):
        total += 1
        v = m.group(1).strip()
        if not ok_pat.fullmatch(v):
            bad += 1
            print("G22 FAIL %s: %s" % (p, v[:100]))
print("G22 %s: %d album create(s), %d with more than items" % ("PASS" if bad == 0 else "FAIL", total, bad))
sys.exit(1 if bad else 0)
