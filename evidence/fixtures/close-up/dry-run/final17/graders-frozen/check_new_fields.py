#!/usr/bin/env python3
"""G18, G19 and C01.18 for the police fields. Usage: check_new_fields.py <case> <transcript>"""
import re, sys
case, path = sys.argv[1], sys.argv[2]
t = open(path).read()
LABELS = ["Full name and date of birth", "Dressed for the weather", "Programs they", "Dominant hand", "Direction they tend to head", "Found before at", "Car:", "Phone and trackers they carry"]
EXPECT = {"C01": set(LABELS) - {"Dressed for the weather"}, "C20": set(LABELS) - {"Dressed for the weather"}, "C21": set(LABELS) - {"Dressed for the weather"}, "C22": set(LABELS) - {"Dressed for the weather"},
          "C09": {"Full name and date of birth"},
          "C19": set(LABELS)}
for _c in ("C24", "C25", "C26", "C27", "C28", "C29", "C37", "C38", "C40"):  # built from C01, C20 and C21, which answer every police field
    EXPECT[_c] = set(LABELS) - {"Dressed for the weather"}
EXPECT["C31"] = set(LABELS) - {"Dressed for the weather"}
EXPECT["C30"] = set(LABELS)
EXPECT["C34"] = set(LABELS)
EXPECT["C33"] = {"Full name and date of birth", "Dressed for the weather"}
EXPECT["C39"] = set(LABELS) - {"Dressed for the weather", "Full name and date of birth", "Direction they tend to head"}  # C01 with no full name and date of birth, question 11 skipped
want = EXPECT.get(case, set())
m = re.search(r"delegate --target knowledge-agent[^\n]*", t)
saved = m.group(0) if m else ""
out, bad = [], 0
if not saved:
    out.append("no save delegation")
for lab in LABELS:
    has = lab in saved
    ng = bool(re.search(re.escape(lab) + r"[^\\\n]{0,40}not given", saved))
    ok = (has == (lab in want)) and not ng
    if saved and not ok:
        bad += 1
    out.append("%s %s%s" % (lab, "present" if has else "absent", " NOT-GIVEN" if ng else ""))
m27 = len(re.findall(r"Your page says they are in", t))
m29 = len(re.findall(r"Places they were found before, from your page", t))
ok27 = (m27 == 1 and m29 == 1) if case in ("C19", "C30", "C34") else (m27 == 0 and m29 == 0)
bad += 0 if ok27 else 1
out.append("M27 count %d, M29 count %d" % (m27, m29))
if case in ("C08", "C09", "C16", "C17", "C18", "C19", "C30", "C33", "C34"):
    m19 = "give their full name, date of birth and any tracking program they are in" in t
    bad += 0 if m19 else 1
    out.append("M19 call line %s" % m19)
turns = re.split(r"(?m)^(?=T[\d?]+ )", t)
nonc = "\n".join(x for x in turns if not re.match(r"T[\d?]+ CAREGIVER:", x))
num = "41-7720" in nonc
if num:
    bad += 1
out.append("transmitter number in assistant or delegate text: %s" % num)
print("G18/G19 %s: %s | %s" % ("PASS" if bad == 0 else "FAIL", case, " | ".join(out)))
