#!/usr/bin/env python3
"""G31 (D48): in a calm refresh, every line of the saved page that was read either comes back unchanged in the
preview and in the save, or their Changed list names it. Emergency runs (M19) are out of scope (e4_fidelity).
The saved page is the one in the case whose person matches the run's own preview or save title, in the current
format or the old one ("Close-Up page Mom", "Note: ..."). Old-format rebuilt lines (Saved, Person, Photos) are
skipped.

Usage: python3 -I check_g31.py <case.md> <transcript.md>
Exit 0 pass or not in scope, 1 fail, 2 usage.

Compared part: for the Hair and Glasses lines only the part before " Photo shows:" (the photo part follows the
photo picked this run). Lines that are rebuilt every run are skipped: the title, Made, Photo, Changed and its
items, Confirmed, Photos looked at, Not checked, Photo source, Refresh by, Still needed for police, and the told-about-this-page line is
compared like any other. A From your notes line counts as named when the Changed list has an item starting
"Notes" or "From your notes".
"""
import json, re, sys

SKIP = ("Close-Up page", "Made ", "Photo:", "Changed since", "- ", "Confirmed ", "Photos looked at",
        "Not checked", "Photo source", "Refresh by", "MADE-UP TEST DATA", "Still needed for police",
        # old page format: rebuilt lines
        "Saved:", "Person:", "Photos:")


def label(line):
    return line.split(":", 1)[0].strip() if ":" in line else line.strip()


def core(line):
    if line.startswith(("Hair:", "Glasses, hearing aids")):
        return line.split(" Photo shows:", 1)[0].rstrip(". ").strip()
    return line.strip()


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    case, tr = argv
    c = open(case, encoding="utf-8").read()
    t = open(tr, encoding="utf-8").read()
    # saved pages in the case, current format ("Close-Up page for X") or the old one ("Close-Up page X")
    texts = []
    for x in re.findall(r'"text":\s*("(?:[^"\\]|\\.)*")', c):
        x = json.loads(x)
        tl = next((l for l in x.split("\n") if l.startswith("Close-Up page")), None)
        if tl:
            texts.append((re.sub(r"^Close-Up page (for )?", "", tl).strip(), x))
    if not texts:
        print("G31 n/a %s (no saved page in the case)" % tr)
        return 0
    # the person comes from the run's own preview or save title, never from a runner note
    who = None
    s0 = re.search(r"delegate --target knowledge-agent[^\n]*Text: Close-Up page for ([^\\']+)\\n", t)
    if s0:
        who = s0.group(1).strip()
    else:
        for x in re.split(r"\n(?=T[0-9?]+ )", t):
            if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x):
                mt = re.search(r"^\s*\"?Close-Up page for ([^\n\"]+)$", x, re.M)
                if mt:
                    who = mt.group(1).strip()
    pick = [x for n, x in texts if who and n == who]
    if who and not pick:
        print("G31 n/a %s (the run's page is for %s, no saved page for that person in the case)" % (tr, who))
        return 0
    page_text = (pick or [texts[0][1]])[0]
    if "Call the police now" in t:
        print("G31 n/a %s (emergency run, E4 is checked by e4_fidelity)" % tr)
        return 0
    old = [l for l in page_text.split("\n") if l.strip()]
    pages = []
    s = re.search(r"delegate --target knowledge-agent[^\n]*Text: (.*)'", t)
    if s:
        pages.append(("save", s.group(1).replace("'\"'\"'", "'").replace('\\"', '"').split("\\n")))
    # the last step 7 preview: from the title to the save question, in the caregiver channel
    pv = [x for x in re.split(r"\n(?=T[0-9?]+ )", t) if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x) and "Close-Up page for" in x]
    if pv:
        body = pv[-1].split("Close-Up page for", 1)[1].split("Save this page", 1)[0]
        lines = ["Close-Up page for" + body.split("\n", 1)[0]] + body.split("\n")[1:]
        pages.append(("preview", [l.strip().strip('"').strip() for l in lines]))
    if not pages:
        print("G31 n/a %s (no preview and no save)" % tr)
        return 0
    worst = 0
    for kind, saved in pages:
        worst = max(worst, compare(tr, kind, old, saved))
    return worst


def compare(tr, kind, old, saved):
    changed = [l[2:] for l in saved if l.startswith("- ")]
    named = {label(x).lower() for x in changed}
    saved_core = {core(l) for l in saved if l.strip()}
    bad = []
    n = 0
    for l in old:
        if l.startswith(SKIP):
            continue
        n += 1
        if core(l) in saved_core:
            continue
        lab = label(l).lower()
        ok = lab in named or (lab == "from your notes" and any("notes" in x.lower() for x in changed))
        if not ok:
            # a Changed item may name the label with extra words, such as "Glasses" for the Glasses line
            ok = any(lab.startswith(x) or x.startswith(lab) for x in named if len(x) >= 5)
        if not ok:
            bad.append(l)
    good = not bad
    print("G31 %s %s %s | old lines compared %d, changed or dropped without a Changed item %d" % (
        "PASS" if good else "FAIL", tr, kind, n, len(bad)))
    for l in bad:
        print("   OLD: " + l[:160])
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
