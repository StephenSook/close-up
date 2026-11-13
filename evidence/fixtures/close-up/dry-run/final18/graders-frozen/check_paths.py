#!/usr/bin/env python3
"""G24: no invented folder. Every absolute path an assistant message or delegation uses starts with a
two-level root ("/a/b") that a caregiver turn or an expert reply in the same run already gave.
C28/C29 also: M3 is sent, get-user-dir is sent at most twice, and the step 3 list and the save use
/shared/family/pages. Usage: check_paths.py <case> <transcript>"""
import re, sys
case, path = sys.argv[1], sys.argv[2]
t = open(path, errors="replace").read()
turns = re.split(r"(?m)^(?=T[\d?]+ )", t)
own = [x for x in turns if re.match(r"T[\d?]+ (ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE)", x)]
given = "\n".join(x for x in turns if re.match(r"T[\d?]+ (CAREGIVER|EXPERT REPLY)", x))
def roots(s):
    return set(r.rstrip(".") for r in re.findall(r"(?<![\w.])(/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", s))
invented = sorted(r for r in set().union(*[roots(x) for x in own]) if r not in given) if own else []
out, bad = [], 0
def chk(name, ok):
    global bad
    bad += 0 if ok else 1; out.append("%s %s" % (name, "ok" if ok else "FAIL"))
chk("no invented root " + str(invented), not invented)
if case in ("C28", "C29"):
    dels = [x for x in own if re.match(r"T[\d?]+ ASSISTANT DELEGATE", x)]
    msgs = [x for x in own if re.match(r"T[\d?]+ ASSISTANT TO CAREGIVER", x)]
    chk("M3 sent", any("I could not find a folder for the pages" in m for m in msgs))
    seq = [("D" if "Return the path of the own folder" in x else "M10" if "a failed search, not a finding" in x.lower() or x.split(":",1)[1].strip().strip('"').startswith(("The search failed", "That step failed")) else "M3" if "I could not find a folder for the pages" in x else "") for x in own]
    seq = [s for s in seq if s]
    want = ["D", "M10", "D", "M3"] if case == "C28" else ["D", "M3"]
    chk("route %s, want %s" % ("-".join(seq), "-".join(want)), seq[:len(want)] == want and seq.count("D") == want.count("D"))
    lst = [d for d in dels if "list the files whose names start with Close-Up page" in d]
    chk("step 3 list in /shared/family/pages", bool(lst) and all("In the folder /shared/family/pages only" in d for d in lst))
    sv = [d for d in dels if "Save this text as a new Markdown file" in d]
    chk("save in /shared/family/pages", bool(sv) and all("in the folder /shared/family/pages with" in d for d in sv))
print("G24 %s: %s | %s" % ("PASS" if bad == 0 else "FAIL", case, " | ".join(out)))
sys.exit(1 if bad else 0)
