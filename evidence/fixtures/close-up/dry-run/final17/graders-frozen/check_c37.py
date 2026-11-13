#!/usr/bin/env python3
"""C37: a first page whose caregiver skipped question 17, so no album or folder is named (Codex round 66 #2).

Usage: python3 -I check_c37.py <transcript.md>
C37.1 No photo step runs: no album search, no folder search or check, no album create and no album read-back.
C37.2 After the first-run list, no assistant question asks for an album or a photo folder.
C37.3 The saved page's photo line is the no-photo line and no line carries a "Photo shows" part.
C37.4 The save question is "Save this page? (yes / no)", never the album form, and M20 closes the run once.
C37.5 The saved page's Photo source line reads none and its Photos looked at line reads "none checked this run".
Exit 0 pass, 1 fail, 2 usage.
"""
import re, sys

NO_PHOTO = "Photo: no recent photo. Take a clear one today. (no photo picked this run)"


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    t = open(argv[0], encoding="utf-8").read()
    turns = [x for x in re.split(r"\n(?=T[0-9?]+ )", t) if re.match(r"T[0-9?]+ ", x)]
    dels = [x for x in turns if re.match(r"T[0-9?]+ ASSISTANT DELEGATE", x)]
    shown = [x for x in turns if re.match(r"T[0-9?]+ ASSISTANT TO CAREGIVER", x)]
    out, ok = [], True

    def chk(name, good):
        nonlocal ok
        ok &= bool(good)
        out.append("%s %s" % (name, "ok" if good else "FAIL"))

    photo = [d for d in dels if re.search(r"Find the person album|Check only these image files|find every image file|"
                                         r"Create one new album|Read the album", d)]
    chk("C37.1 no photo step (%d photo delegations)" % len(photo), not photo)
    # the first-run list is the turn that carries question 17's own words
    li = next((i for i, x in enumerate(shown) if "What is the person album called in UGREEN Photos?" in x), None)
    chk("first-run list sent", li is not None)
    later = shown[li + 1:] if li is not None else []
    asks = [x for x in later if re.search(r"(person album|photo folder|album)[^\n?]*\?", x, re.I)
            and "Save this page" not in x]
    chk("C37.2 no question for an album or folder after the list (%d)" % len(asks), not asks)
    m = re.search(r"delegate --target knowledge-agent[^\n]*Text: (.*)'", t)
    saved = m.group(1).replace("'\"'\"'", "'").replace('\\"', '"').split("\\n") if m else []
    chk("page saved", bool(saved))
    chk("C37.3 no-photo line", NO_PHOTO in saved)
    chk("C37.3 no Photo shows part", bool(saved) and not any("Photo shows" in l for l in saved))
    # C37.5 (Grok round 69): with no album or folder named, Photo source reads none and Photos looked at reads
    # "none checked this run"
    chk("C37.5 Photo source none", any(re.match(r"Photo source: none\b", l) for l in saved))
    chk("C37.5 Photos looked at none checked", any(l.startswith("Photos looked at: none checked this run") for l in saved))
    chk("C37.4 save question without the album", "Save this page? (yes / no)" in t
        and "Save this page and create the album?" not in t)
    m20 = sum(1 for x in shown if "Your page is saved as" in x and "Print it" in x)
    chk("C37.4 M20 once (%d)" % m20, m20 == 1)
    print("C37 %s: %s" % ("PASS" if ok else "FAIL", " | ".join(out)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
