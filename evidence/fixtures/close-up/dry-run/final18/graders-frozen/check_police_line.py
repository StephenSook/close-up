#!/usr/bin/env python3
"""G33 (reported) and G33Q (gates): the "Still needed for police" line on each page a run shows or saves.

Usage: python3 -I check_police_line.py <transcript> [...]

A calm page (no "in an emergency" in its Made line and no Wearing today line) names, in this fixed order, each of
these five fields that the page itself shows empty, and nothing else:
  "full name and date of birth"            no Full name and date of birth line
  "a recent photo"                         the no-photo line ("Photo: no recent photo")
  "places they walk to now"                the line is missing or reads "not given"
  "places they talk about going back to"   the line is missing or reads "not given"
  "conditions and medicines"               the Conditions line is missing or reads "not given", and there is no
                                           Medicines from bottle labels line
G33, reported (orchestrator ruling of 2026-11-13, like G32): the line reads exactly
"Still needed for police: {the names, separated by ", "} (this run)", once, and with none empty there is no line.
Its lines say "exact" or "differs" and carry no pass or fail word.
G33Q, gates: no line names a field the page has, no line carries anything beyond the five fixed names, and no
emergency or short page carries the line. A missing line or a wrong order is a G33 difference, not a G33Q fail.
Every preview and every save is checked. Exit 1 only when G33Q fails.
"""
import re, sys

ORDER = ["full name and date of birth", "a recent photo", "places they walk to now",
         "places they talk about going back to", "conditions and medicines"]
LABEL = "Still needed for police:"


def turns(t):
    out = []
    for x in re.split(r"\n(?=T[0-9?]+ )", t):
        m = re.match(r"T[0-9?]+ (CAREGIVER|ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE|EXPERT REPLY|END|MISSING)[^:\n]*:\s*", x)
        if m:
            out.append((m.group(1), x[m.end():]))
    return out


def pages(ts):
    out = []
    for i, (k, b) in enumerate(ts):
        if k == "ASSISTANT TO CAREGIVER":
            ls = [l.strip().strip('"').strip() for l in b.splitlines()]
            start = next((j for j, l in enumerate(ls) if l.startswith("Close-Up page for")), None)
            if start is not None:
                out.append(("preview", i, [l for l in ls[start:] if l]))
        elif k == "ASSISTANT DELEGATE" and "knowledge-agent" in b:
            m = re.search(r"Text: (.*)'", b, re.S) or re.search(r"Text: (.*)", b, re.S)
            if m:
                ls = [l.strip() for l in m.group(1).replace("'\"'\"'", "'").replace('\\"', '"').split("\\n")]
                if ls and ls[0].startswith("Close-Up page"):
                    out.append(("save", i, [l for l in ls if l]))
    return out


def empty(lines, label):
    l = next((x for x in lines if x.startswith(label)), None)
    return l is None or l[len(label):].strip().lower().startswith("not given")


def expected(lines):
    missing = []
    if not any(l.startswith("Full name and date of birth:") for l in lines):
        missing.append(ORDER[0])
    if any(l.startswith("Photo: no recent photo") for l in lines):
        missing.append(ORDER[1])
    if empty(lines, "Places they walk to now:"):
        missing.append(ORDER[2])
    if empty(lines, "Places they talk about going back to:"):
        missing.append(ORDER[3])
    if empty(lines, "Conditions and medicines police should know:") and \
            not any(l.startswith("Medicines from bottle labels:") for l in lines):
        missing.append(ORDER[4])
    return ("%s %s (this run)" % (LABEL, ", ".join(missing))) if missing else None


def items(line):
    body = line[len(LABEL):].strip()
    if body.endswith("(this run)"):
        body = body[:-len("(this run)")].strip()
    return [x.strip() for x in body.split(",") if x.strip()]


def check(path):
    ts = turns(open(path, encoding="utf-8").read())
    ps = pages(ts)
    if not ps:
        print("G33 REPORT n/a %s | no page shown or saved" % path)
        print("G33Q PASS %s | no page" % path)
        return True
    bad = []
    for kind, i, lines in ps:
        got = [l for l in lines if l.startswith(LABEL)]
        emerg = any("in an emergency" in l for l in lines if l.startswith("Made ")) or \
            any(l.startswith("Wearing today:") for l in lines)
        want = None if emerg else expected(lines)
        exact = (got == [want]) if want else (got == [])
        print("G33 REPORT %s %s %s at turn %d | %s page | want %s | got %s" % (
            "exact" if exact else "differs", path, kind, i, "emergency" if emerg else "calm", want or "no line",
            "; ".join(got) if got else "no line"))
        empties = items(want) if want else []
        for g in got:
            if emerg:
                bad.append("%s at turn %d: the line on an emergency page" % (kind, i))
                continue
            for x in items(g):
                if x not in ORDER:
                    bad.append("%s at turn %d: %r is not one of the five fields" % (kind, i, x))
                elif x not in empties:
                    bad.append("%s at turn %d: names %r, which the page has" % (kind, i, x))
    print("G33Q %s %s | %s" % ("FAIL" if bad else "PASS", path, "; ".join(bad) if bad else "no wrong statement"))
    return not bad


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    return 0 if all([check(p) for p in argv]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
