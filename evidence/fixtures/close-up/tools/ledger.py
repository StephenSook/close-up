#!/usr/bin/env python3
"""Review ledger: one row per committed review round folder, counted only from the round's own files.

Usage:
  python3 fixtures/close-up/tools/ledger.py            print the ledger
  python3 fixtures/close-up/tools/ledger.py --write    write fixtures/close-up/rounds/LEDGER.md
  python3 fixtures/close-up/tools/ledger.py --check    exit 1 unless LEDGER.md has a row for every round folder that
                                                       holds a reviewer report, every row equals what the files give,
                                                       and the totals line equals the column sums

Sources, per round folder rN:
- reviewer and findings: codex.md or grok.md (r2: grok-b.md, the only report with a TOTAL line). Findings are the sum
  of the severity counts on the report's last TOTAL line. A round is clean when that sum is 0.
- effort: the model and effort line of effort.txt, written from round 66 on. Earlier rounds: not recorded.
- scope: the opening of brief.md or brief-inline.md ("WHOLE PACKAGE" or "DIFF-SCOPED"). Otherwise: not recorded.
- adopted and declined: adjudication.md. A clean round is 0 and 0 from its report. Otherwise each finding's verdict is
  read from a table row or a numbered line ("Adopted", "Adopted in part", "Adopted in other words", "adopted in
  substance" count as adopted; "Declined" and "not adopted" as declined). When the verdicts read do not add up to the
  findings, both counts are "not recorded". Nothing is filled in from memory.
A round folder with no reviewer report yet (a review still running) gets no row.
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROUNDS = os.path.normpath(os.path.join(HERE, "..", "rounds"))
LEDGER = os.path.join(ROUNDS, "LEDGER.md")
SEV = ("critical", "high", "medium", "low")
NR = "not recorded"


def read(p):
    return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def total_line(text):
    lines = re.findall(r"(?im)^.*\bTOTAL\b.*$", text or "")
    if not lines:
        return None
    line = lines[-1]
    counts = {}
    for a, b in re.findall(r"(\d+)\s+(critical|high|medium|low)\b|(?:critical|high|medium|low)\s+(\d+)", line, re.I) and [] or []:
        pass
    for m in re.finditer(r"(\d+)\s+(critical|high|medium|low)\b", line, re.I):
        counts[m.group(2).lower()] = int(m.group(1))
    for m in re.finditer(r"\b(critical|high|medium|low)\s+(\d+)", line, re.I):
        counts.setdefault(m.group(1).lower(), int(m.group(2)))
    if not counts:
        return None
    return sum(counts.values()), line.strip()


# Rounds whose adjudication states one verdict for the whole round instead of one per finding. Each entry is
# (adopted, declined, the verdict sentence). The sentence must appear word for word in that round's adjudication.md,
# or the round reads "not recorded".
WHOLE_ROUND = {
    "r40": (1, 0, "Fix: the evidence, not the package."),
    "r41": (2, 0, "Both checked at their cited lines and adopted."),
    "r50": (3, 0, "Not adopted as proposed; resolved by a smaller design instead."),
}


def verdicts(r, adj):
    """(adopted, declined, how) read from an adjudication, or None when no verdict is readable."""
    if not adj:
        return None
    if r in WHOLE_ROUND:
        a, d, quote = WHOLE_ROUND[r]
        return (a, d, "whole-round verdict quoted") if quote in adj else None
    rows = []
    for l in adj.splitlines():
        m = re.match(r"\|\s*\d+\s*\|.*\|\s*(Adopted[^|]*|Declined[^|]*)\|", l)
        if m:
            rows.append(m.group(1).strip().lower())
            continue
        # one finding per line: "Finding 1 (...)" or "1. MEDIUM, ..."
        if re.match(r"\s*(Finding \d+\b|\d+\.\s+(?:CRITICAL|HIGH|MEDIUM|LOW)\b)", l, re.I):
            if re.search(r"\bNOT ADOPTED\b|,\s*not adopted\b", l):
                rows.append("declined")
            elif re.search(r"\badopted\b", l, re.I):
                rows.append("adopted")
            else:
                rows.append("unreadable")
    if not rows or "unreadable" in rows:
        return None
    a = sum(1 for v in rows if v.startswith("adopted"))
    d = sum(1 for v in rows if v.startswith("declined") or v.startswith("not adopted"))
    if a + d != len(rows):
        return None
    return a, d, "per finding"


def rows():
    out = []
    names = sorted((d for d in os.listdir(ROUNDS) if re.fullmatch(r"r\d+", d)), key=lambda x: int(x[1:]))
    for r in names:
        d = os.path.join(ROUNDS, r)
        rep, src = None, None
        for f in ("codex.md", "grok.md", "grok-b.md"):
            t = read(os.path.join(d, f))
            if t is not None and total_line(t):
                rep, src = t, f
                break
        if rep is None:
            continue
        reviewer = "Codex" if src.startswith("codex") else "Grok"
        n, line = total_line(rep)
        eff = read(os.path.join(d, "effort.txt"))
        effort = NR
        if eff:
            m = re.search(r"effort (max|ultra|xhigh|high|medium|low)\b", eff)
            effort = m.group(1) if m else NR
        brief = read(os.path.join(d, "brief.md")) or read(os.path.join(d, "brief-inline.md")) or ""
        head = brief[:300]
        scope = "whole package" if "WHOLE PACKAGE" in head else "diff" if re.search(r"DIFF-SCOPED", head, re.I) else NR
        adj = read(os.path.join(d, "adjudication.md"))
        if n == 0:
            adopted, declined, from_ = 0, 0, src
        else:
            v = verdicts(r, adj)
            if v and v[0] + v[1] == n:
                adopted, declined, from_ = v[0], v[1], src + ", adjudication.md" + (
                    " (whole-round verdict)" if v[2] == "whole-round verdict quoted" else "")
            else:
                adopted, declined, from_ = NR, NR, src + (", adjudication.md (verdicts not readable)" if adj else "")
        out.append(dict(round=r, reviewer=reviewer, effort=effort, scope=scope, findings=n, adopted=adopted,
                        declined=declined, clean="yes" if n == 0 else "no", source=from_))
    return out


def render(rs):
    def num(x):
        return str(x)
    lines = ["# Review ledger", "",
             "One row per review round, counted only from the files in that round's folder by fixtures/close-up/tools/ledger.py. "
             "\"not recorded\" means the files do not give that count. Nothing is filled in from memory. "
             "Regenerate with `python3 fixtures/close-up/tools/ledger.py --write` and check with `--check`.", "",
             "| Round | Reviewer | Effort | Scope | Findings | Adopted | Declined | Clean | Counted from |",
             "|---|---|---|---|---|---|---|---|---|"]
    for x in rs:
        lines.append("| %s | %s | %s | %s | %s | %s | %s | %s | %s |" % (
            x["round"], x["reviewer"], x["effort"], x["scope"], num(x["findings"]), num(x["adopted"]),
            num(x["declined"]), x["clean"], x["source"]))
    lines += ["", totals(rs), ""]
    return "\n".join(lines)


def totals(rs):
    f = sum(x["findings"] for x in rs)
    rec = [x for x in rs if x["adopted"] != NR]
    a = sum(x["adopted"] for x in rec)
    d = sum(x["declined"] for x in rec)
    c = sum(1 for x in rs if x["clean"] == "yes")
    nr = len(rs) - len(rec)
    rec_f = sum(x["findings"] for x in rec)
    return ("Totals: %d rounds, %d findings, %d clean rounds. Adopted and declined are recorded for %d rounds holding "
            "%d findings: %d adopted, %d declined. %d rounds with findings have no readable verdicts." % (
                len(rs), f, c, len(rec), rec_f, a, d, nr))


def main(argv):
    rs = rows()
    text = render(rs)
    if "--write" in argv:
        open(LEDGER, "w", encoding="utf-8").write(text)
        print("wrote", LEDGER, len(rs), "rows")
        return 0
    if "--check" in argv:
        have = open(LEDGER, encoding="utf-8").read() if os.path.exists(LEDGER) else ""
        bad = []
        if have != text:
            bad.append("LEDGER.md differs from what the round files give (regenerate with --write)")
        got = re.findall(r"^\| (r\d+) \|", have, re.M)
        want = [x["round"] for x in rs]
        if got != want:
            bad.append("rows %s, round folders with a report %s" % (len(got), len(want)))
        # the totals line equals the column sums of the committed table
        tot = re.search(r"^Totals: (\d+) rounds, (\d+) findings, (\d+) clean rounds\. .* for (\d+) rounds holding (\d+) "
                        r"findings: (\d+) adopted, (\d+) declined\. (\d+) rounds", have, re.M)
        cells = [l.split("|")[1:-1] for l in have.splitlines() if re.match(r"\| r\d+ \|", l)]
        if not tot or not cells:
            bad.append("no totals line or no rows")
        else:
            n = [int(c[4]) for c in cells]
            ad = [c[5].strip() for c in cells]
            de = [c[6].strip() for c in cells]
            recn = [int(c[4]) for c in cells if c[5].strip() != NR]
            sums = (len(cells), sum(n), sum(1 for c in cells if c[7].strip() == "yes"),
                    sum(1 for v in ad if v != NR), sum(recn), sum(int(v) for v in ad if v != NR),
                    sum(int(v) for v in de if v != NR), sum(1 for v in ad if v == NR))
            if tuple(int(g) for g in tot.groups()) != sums:
                bad.append("totals line %s, column sums %s" % (tot.groups(), sums))
        print("LEDGER %s: %d rows%s" % ("FAIL" if bad else "PASS", len(got), (" | " + " | ".join(bad)) if bad else ""))
        return 1 if bad else 0
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
