#!/usr/bin/env python3
"""Strip runner notes from turn role labels, and nothing else (final18 ship-rule helper).

Usage: python3 -I strip_role_notes.py <transcript.md> <stripped-copy.md>

Some runners write a note inside a role label, for example
"T3 ASSISTANT DELEGATE (step 9, album create):". The frozen graders look for
"ASSISTANT DELEGATE:", so such a label can make G29 or G30 report a parse failure.
This script removes only a parenthetical note that sits between the role and the
colon at the start of a turn line, so that line becomes "T3 ASSISTANT DELEGATE:".
No other byte changes. The stripped copy is written to a new file, and the scored
transcript is never touched. Prints how many labels were stripped.

Under the final18 ship rule, a run whose G29 or G30 parse failure passes on the
stripped copy still counts as a strict-fail run (classed transcript-form). A G30
ordering fail, or a stripped copy that still fails, stays a behaviour fail.
"""
import re, sys

LABEL = re.compile(
    r"(?m)^(T[0-9?]+ (?:CAREGIVER|ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE|EXPERT REPLY|END|MISSING)) \([^()\n]*\):")


def strip(text):
    return LABEL.subn(r"\1:", text)


def main(argv):
    if len(argv) != 2:
        print(__doc__)
        return 2
    src, dst = argv
    if src == dst:
        print("refusing to overwrite the scored transcript")
        return 2
    text = open(src, encoding="utf-8").read()
    out, n = strip(text)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(out)
    print("stripped %d role-label notes: %s -> %s" % (n, src, dst))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
