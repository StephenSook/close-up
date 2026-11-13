#!/usr/bin/env python3
"""Builds the BASELINE harm table from HAND-REVIEW.md and checks it.

Usage: python3 -I baseline/table.py [--check] [HAND-REVIEW file]   (run from fixtures/close-up/dry-run)

The file defaults to baseline/HAND-REVIEW.md (the BASELINE arm). The Close-Up arm's files, baseline/HAND-REVIEW-final17.md
and baseline/HAND-REVIEW-final18.md, use the same section form and are built the same way.

Each case section of HAND-REVIEW.md gives one verdict per H: a count, "not assessable" or "does not apply". This prints
one row per case and the column totals, and checks that every case has all eight verdicts and that each section's
"Total for" line equals the sum of its counts and its not-assessable list. With --check it exits 1 on any mismatch.
"""
import re, sys

HS = ["H%d" % i for i in range(1, 9)]


def parse(text):
    rows, errs = {}, []
    for sec in re.split(r"\n## ", text)[1:]:
        case = sec[:3]
        v = {}
        for line in sec.splitlines():
            m = re.match(r"- (H\d(?:, H\d)*(?: and H\d)?) (do not apply|does not apply)\b", line)
            if m:
                for h in re.findall(r"H\d", m.group(1)):
                    v[h] = "n/a"
                continue
            m = re.match(r"- (H\d) (\d+)\b", line)
            if m:
                v[m.group(1)] = int(m.group(2))
                continue
            m = re.match(r"- (H\d) (not assessable|does not apply)\b", line)
            if m:
                v[m.group(1)] = "NA" if m.group(2) == "not assessable" else "n/a"
        missing = [h for h in HS if h not in v]
        if missing:
            errs.append("%s: no verdict for %s" % (case, ", ".join(missing)))
        t = re.search(r"Total for %s: (\d+) counted.*?, (none|\d+) not assessable" % case, sec)
        if not t:
            errs.append("%s: no Total line" % case)
        else:
            counted = sum(x for x in v.values() if isinstance(x, int))
            na = sum(1 for x in v.values() if x == "NA")
            if int(t.group(1)) != counted:
                errs.append("%s: Total says %s counted, verdicts sum to %d" % (case, t.group(1), counted))
            if (0 if t.group(2) == "none" else int(t.group(2))) != na:
                errs.append("%s: Total says %s not assessable, verdicts give %d" % (case, t.group(2), na))
        rows[case] = v
    return rows, errs


def main(argv):
    path = next((a for a in argv if not a.startswith("--")), "baseline/HAND-REVIEW.md")
    text = open(path, encoding="utf-8").read()
    rows, errs = parse(text)
    print("| Case | " + " | ".join(HS) + " | Counted | Not assessable |")
    print("|---|" + "---|" * (len(HS) + 2))
    tot = {h: 0 for h in HS}
    na = {h: 0 for h in HS}
    dna = {h: 0 for h in HS}
    for case in sorted(rows):
        v = rows[case]
        cells = []
        for h in HS:
            x = v.get(h, "?")
            if isinstance(x, int):
                tot[h] += x
                cells.append(str(x))
            elif x == "NA":
                na[h] += 1
                cells.append("not assessable")
            else:
                dna[h] += 1
                cells.append("does not apply")
        c = sum(x for x in v.values() if isinstance(x, int))
        print("| %s | %s | %d | %d |" % (case, " | ".join(cells), c, sum(1 for x in v.values() if x == "NA")))
    print("| Total | " + " | ".join(str(tot[h]) for h in HS) + " | %d | %d |" % (sum(tot.values()), sum(na.values())))
    print("| Runs not assessable | " + " | ".join(str(na[h]) for h in HS) + " | | |")
    print("| Runs where it does not apply | " + " | ".join(str(dna[h]) for h in HS) + " | | |")
    print("CASES %d, counted harms %d, runs with zero counted %d" % (
        len(rows), sum(tot.values()), sum(1 for v in rows.values() if not any(isinstance(x, int) and x for x in v.values()))))
    for e in errs:
        print("CHECK", e)
    return 1 if ("--check" in argv and errs) else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
