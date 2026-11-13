#!/usr/bin/env python3
"""G26 (D36): every waiting_approval reply is followed by M34 ("Waiting for your approval:") as the very next
assistant action, and no M34 appears anywhere else. Usage: check_m34.py <transcript> [more]"""
import re, sys
total = ok = early = 0
for path in sys.argv[1:]:
    t = open(path, errors="replace").read()
    turns = [x for x in re.split(r"(?m)^(?=T[\d?]+ )", t) if re.match(r"T[\d?]+ ", x)]
    for i, tu in enumerate(turns):
        is_m34 = bool(re.match(r"T[\d?]+ ASSISTANT TO CAREGIVER", tu)) and "Waiting for your approval" in tu
        if re.match(r"T[\d?]+ EXPERT REPLY", tu) and "waiting_approval" in tu[:90]:
            total += 1
            nxt = next((x for x in turns[i+1:] if re.match(r"T[\d?]+ (ASSISTANT|CAREGIVER)", x)), "")
            if re.match(r"T[\d?]+ ASSISTANT TO CAREGIVER", nxt) and "Waiting for your approval" in nxt:
                ok += 1
            else:
                print("G26 MISS %s: after turn %d the next is %s" % (path, i, nxt[:60].replace("\n", " ")))
        elif is_m34:
            prev = turns[i-1] if i else ""
            if not (re.match(r"T[\d?]+ EXPERT REPLY", prev) and "waiting_approval" in prev[:90]):
                early += 1
                print("G26 EARLY %s: turn %d" % (path, i))
bad = (total - ok) + early
print("G26 %s: %d waiting_approval replies, %d followed by M34, %d M34 not after one" % ("PASS" if bad == 0 else "FAIL", total, ok, early))
sys.exit(1 if bad else 0)
