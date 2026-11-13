#!/usr/bin/env python3
"""C24/C25: the album message (C32: the page message) after a read-back carrying file details. Usage: check_readback.py <case> <transcript>"""
import re, sys
case, path = sys.argv[1], sys.argv[2]
t = open(path).read()
turns = re.split(r"(?m)^(?=T[\d?]+ )", t)
msgs = [x for x in turns if re.match(r"T[\d?]+ ASSISTANT TO CAREGIVER", x)]
m23 = [x for x in msgs if "was created in UGREEN Photos" in x]
m24 = [x for x in msgs if "does not hold exactly the photo you picked" in x]
out = []
if case == "C24":
    ok = len(m23) == 1 and not m24
    out.append("M23 once, no M24: %s (M23 %d, M24 %d)" % ("ok" if ok else "FAIL", len(m23), len(m24)))
elif case == "C25":
    ok = len(m24) == 1 and not m23 and "P011" in m24[0]
    out.append("M24 once naming P011, no M23: %s (M23 %d, M24 %d)" % ("ok" if ok else "FAIL", len(m23), len(m24)))
elif case == "C32":
    m14 = [x for x in msgs if "reads back differently from what you approved" in x]
    m20 = [x for x in msgs if "Your page is saved as" in x]
    ok = len(m14) == 1 and not m20 and len(m23) == 1 and not m24
    out.append("M14 once, no M20, M23 once: %s (M14 %d, M20 %d, M23 %d, M24 %d)" % ("ok" if ok else "FAIL", len(m14), len(m20), len(m23), len(m24)))
else:
    sys.exit("case must be C24, C25 or C32")
print("READBACK %s: %s | %s" % ("PASS" if ok else "FAIL", case, " | ".join(out)))
sys.exit(0 if ok else 1)
