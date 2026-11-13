#!/usr/bin/env python3
"""E4 rebuild fidelity: every saved-page line E4 may not change must appear unchanged in the refreshed save.
Usage: e4_fidelity.py <case.md> <transcript.md>"""
import json, re, sys
case, tr = sys.argv[1], sys.argv[2]
c = open(case).read()
m = re.search(r'"text":\s*("(?:[^"\\]|\\.)*")', c)
old = json.loads(m.group(1)).split("\n")
t = open(tr).read()
s = re.search(r"delegate --target knowledge-agent[^\n]*Text: (.*)'", t)
if not s:
    print("no save"); sys.exit(0)
saved = s.group(1).replace("'\"'\"'", "'").replace('\\"', '"').split("\\n")
ALLOWED = ("Made ", "Confirmed ", "Refresh by", "Photo source", "Wearing today", "Dressed for the weather", "Last seen",
           "Photos looked at", "Not checked", "Photo:", "Hair:", "Glasses, hearing aids", "Changed since", "- ",
           "Still needed for police")  # E4 removes it
fixed = [l for l in old if l.strip() and not l.startswith(ALLOWED)]
missing = [l for l in fixed if l not in saved]
print("%s fixed lines %d, changed or missing %d" % (tr, len(fixed), len(missing)))
for l in missing:
    print("   OLD: " + l[:150])
