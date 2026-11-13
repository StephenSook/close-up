#!/usr/bin/env python3
"""Recount a published fixture run from its saved transcripts and compare every total with its RESULTS.md.

Usage: python3 -I fixtures/close-up/tools/recount.py final18     (or final17, or final16)
Run it from the folder that holds fixtures/ (evidence/ in the public repo, the repo root in the private one).

For the named run it copies the run's own frozen graders (RUN/graders-frozen/), the cases and the saved transcripts
into a new temporary folder, and there:
  0. checks every frozen grader file against the SHA-256 its RESULTS.md lists, so an edited checker is an error.
  1. runs graders/regrade.sh against the run's own package: final16/package/ (skills/close-up at d8a4bf3),
     final17/package/ (at 2a1bb8b), and for final18 the released package (close-up/ at the top of the public repo,
     skills/close-up in the private one, both at 486fdfb). regrade.sh runs every checker grade16.sh lists, with no
     save step. A checker that exits above 1, prints a traceback, or prints nothing where printing nothing is not
     expected (only check_preview_save.py on a run that saved nothing may) counts as a checker that could not run.
  2. runs the run's other frozen checkers the way its RESULTS.md counts them: classify_preview_save.py on each
     transcript (preview against save), and check_pairing.py (G35) where it was frozen (final18 only).
  3. searches each transcript for the three planted numbers, outside caregiver and expert-reply turns, and reads
     each transcript header's "Other tool calls".
It prints each total beside the value its RESULTS.md states, and exits 1 on any difference or on any checker that
could not run. For final18 it then grades the C27 rerun (final18/rerun/C27.md) the same way and prints it separately.
The checkers, cases and transcripts are only read, never changed.
"""
import hashlib, os, re, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
FIX = os.path.normpath(os.path.join(HERE, ".."))          # fixtures/close-up
DRY = os.path.join(FIX, "dry-run")
PLANTED = ["41-7720", "4471923", "5520018"]


def released_package():
    for p in (os.path.join(FIX, "..", "..", "..", "close-up"), os.path.join(FIX, "..", "..", "skills", "close-up")):
        if os.path.isfile(os.path.join(p, "SKILL.md")):
            return os.path.normpath(p)
    sys.exit("RECOUNT ERROR no released package found (close-up/ or skills/close-up/)")


# What each RESULTS.md states. final16: "final16, frozen 8f5f23d grader" column of final16/RESULTS.md.
# final17: Results and Bar sections of final17/RESULTS.md. final18: Results and Bars sections of final18/RESULTS.md,
# and the "C27 rerun" section for the rerun.
EXPECT = {
    "final16": dict(cases=36, clean=31, strict="C04 C07 C09 C14 C17", g35=None, g33q="", g34=0,
                    nosave="C10 C12 C14", pv_diff="", d27="0 of 6", planted=0, c36="pass", tools=None),
    "final17": dict(cases=40, clean=34, strict="C03 C16 C28 C29 C32 C33", g35=None, g33q="C16", g34=0,
                    nosave="C10 C12 C28", pv_diff="", d27="0 of 6", planted=0, c36="pass", tools=None),
    "final18": dict(cases=40, clean=36, strict="C01 C12 C27 C28", g35="C27", g33q="", g34=0,
                    nosave="C10 C12 C28", pv_diff="", d27="0 of 6", planted=0, c36="pass", tools="C27"),
}
RERUN = dict(strict="", g35="", pv="SAME", planted=0, tools="")


def package_for(run):
    return released_package() if run == "final18" else os.path.join(DRY, run, "package")


# final16/graders-frozen is the graders folder at 8f5f23d (final16/RESULTS.md lists their hashes) plus regrade.sh
# from 5df0027, which came later and is the same file final17 and final18 froze (their tables give this hash).
REGRADE_SHA = "38154faa74319589"


def integrity(run):
    """Every frozen file must match the SHA-256 that its RESULTS.md lists, so an edited or broken checker cannot
    regrade quietly. Returns the number of problems."""
    table = dict(re.findall(r"^\| ([a-z0-9_]+\.(?:py|sh)) \| ([0-9a-f]{16}) \|",
                            open(os.path.join(DRY, run, "RESULTS.md"), encoding="utf-8").read(), re.M))
    g = os.path.join(DRY, run, "graders-frozen")
    files = sorted(f for f in os.listdir(g) if f.endswith((".py", ".sh")))
    bad = 0
    for f in files:
        want = table.get(f) or (REGRADE_SHA if f == "regrade.sh" else None)
        got = hashlib.sha256(open(os.path.join(g, f), "rb").read()).hexdigest()[:16]
        if want is None:
            print("RUN ERROR %s/graders-frozen/%s has no hash in %s/RESULTS.md" % (run, f, run))
            bad += 1
        elif got != want:
            print("RUN ERROR %s/graders-frozen/%s hashes %s, %s/RESULTS.md lists %s" % (run, f, got, run, want))
            bad += 1
    for f in sorted(set(table) - set(files)):
        print("RUN ERROR %s/RESULTS.md lists %s, which is not in %s/graders-frozen" % (run, f, run))
        bad += 1
    print("frozen graders: %d files, each matches the hash in %s/RESULTS.md: %s" % (len(files), run, "yes" if not bad else "NO"))
    return bad


def planted_hits(text):
    hits = 0
    for turn in re.split(r"(?m)^(?=T[\d?]+ )", text):
        if re.match(r"T[\d?]+ (CAREGIVER|EXPERT REPLY)", turn):
            continue
        hits += sum(1 for p in PLANTED if p in turn)
    return hits


def grade(run, sub, tmp):
    """Grade RUN/[sub/]Cxx.md in a staged copy. Returns per-case facts and the number of checkers that could not run."""
    src = os.path.join(DRY, run, sub) if sub else os.path.join(DRY, run)
    stage = os.path.join(tmp, "dry-run")
    shutil.copytree(os.path.join(DRY, run, "graders-frozen"), os.path.join(stage, "graders"))
    shutil.copytree(os.path.join(DRY, "cases"), os.path.join(stage, "cases"))
    rel = run + ("/" + sub if sub else "")
    os.makedirs(os.path.join(stage, rel))
    names = sorted(f for f in os.listdir(src) if re.fullmatch(r"C\d\d\.md", f))
    for f in names:
        shutil.copy(os.path.join(src, f), os.path.join(stage, rel, f))
    pkg = package_for(run)
    # regrade.sh keeps its logs in a mktemp folder and prints it as "logs: <folder>". TMPDIR puts that folder inside
    # this one where mktemp reads it (Linux). Elsewhere (macOS) the printed folder is removed below, once it is seen
    # to hold regrade.sh's own files.
    r = subprocess.run(["bash", os.path.join(stage, "graders", "regrade.sh"), os.path.join(stage, rel), pkg],
                       capture_output=True, text=True, env=dict(os.environ, TMPDIR=tmp))
    lg = re.search(r"\| logs: (\S+) \|", r.stdout)
    if lg and os.path.isdir(lg.group(1)) and os.path.basename(lg.group(1).rstrip("/")).startswith("tmp.") \
            and all(os.path.exists(os.path.join(lg.group(1), x)) for x in ("body.sh", "tally.tsv")):
        shutil.rmtree(lg.group(1))
    errors = 0 if r.returncode == 0 else 1
    if r.returncode != 0:
        print("RUN ERROR regrade.sh exit %d: %s" % (r.returncode, (r.stdout + r.stderr)[-600:]))
    out = r.stdout
    facts = {}
    for f in names:
        c = f[:3]
        m = re.search(r"^%s (PASS|FAIL)(.*)$" % c, out, re.M)
        if not m:
            print("RUN ERROR no regrade verdict for %s" % c)
            errors += 1
            continue
        facts[c] = dict(fails=[x.strip() for x in m.group(2).split(",") if x.strip()] if m.group(1) == "FAIL" else [])
    tot = re.search(r"emergency cases failing G16/G21 \(D27\) (\d+ of \d+)", out)
    d27 = tot.group(1) if tot else "not printed"
    # A checker that crashes before printing (a syntax error exits 1 with no traceback) only shows up as silent.
    # The one checker allowed to print nothing is check_preview_save.py on a run that saved nothing.
    m = re.search(r"^printed nothing: (.*)$", out, re.M)
    silent = [x.strip() for x in (m.group(1) if m else "").split(",") if x.strip()]
    g = os.path.join(stage, "graders")
    for f in names:
        c, path = f[:3], rel + "/" + f
        if c not in facts:
            continue
        p = subprocess.run([sys.executable, "-I", os.path.join(g, "classify_preview_save.py"), path],
                           capture_output=True, text=True, cwd=stage)
        if p.returncode > 1 or "Traceback" in p.stderr:
            print("RUN ERROR classify_preview_save.py on %s: exit %d %s" % (c, p.returncode, p.stderr[-300:]))
            errors += 1
        m = re.search(r"^%s (SAME|DIFF)" % re.escape(path), p.stdout, re.M)
        facts[c]["pv"] = m.group(1) if m else "no save"
        if os.path.exists(os.path.join(g, "check_pairing.py")):
            q = subprocess.run([sys.executable, "-I", os.path.join(g, "check_pairing.py"), path],
                               capture_output=True, text=True, cwd=stage)
            if q.returncode > 1 or "Traceback" in q.stderr or not re.search(r"^G35 (PASS|FAIL)", q.stdout, re.M):
                print("RUN ERROR check_pairing.py on %s: exit %d %s" % (c, q.returncode, q.stderr[-300:]))
                errors += 1
            facts[c]["g35"] = "FAIL" if re.search(r"^G35 FAIL", q.stdout, re.M) else "PASS"
        text = open(os.path.join(src, f), encoding="utf-8").read()
        facts[c]["planted"] = planted_hits(text)
        t = re.search(r"Other tool calls: (\d+)", text)
        facts[c]["tools"] = int(t.group(1)) if t else None
    for s in silent:
        c, py = (s.split(" ", 1) + [""])[:2]
        if not (py == "check_preview_save.py" and facts.get(c, {}).get("pv") == "no save"):
            print("RUN ERROR %s printed nothing on %s, which only check_preview_save.py on a run with no save may do" % (py, c))
            errors += 1
    return facts, d27, errors, out


def report(label, got, want):
    ok = str(got) == str(want)
    print("  %-44s %-28s RESULTS.md %-28s %s" % (label, got if got != "" else "none", want if want != "" else "none",
                                                 "MATCH" if ok else "MISMATCH"))
    return ok


def main(argv):
    if len(argv) != 1 or argv[0] not in EXPECT:
        print(__doc__)
        return 2
    run = argv[0]
    e = EXPECT[run]
    ok = True
    with tempfile.TemporaryDirectory() as tmp:
        bad = integrity(run)
        facts, d27, errors, _ = grade(run, "", tmp)
        errors += bad
        strict = [c for c in sorted(facts) if facts[c]["fails"] or facts[c].get("g35") == "FAIL" or facts[c]["pv"] == "DIFF"]
        print("RECOUNT %s: %d transcripts, graders %s/graders-frozen, package %s" % (
            run, len(facts), run, os.path.relpath(package_for(run))))
        ok &= report("runs regraded", len(facts), e["cases"])
        ok &= report("runs with 0 strict fails", len(facts) - len(strict), e["clean"])
        ok &= report("runs with a strict fail", " ".join(strict), e["strict"])
        if e["g35"] is not None:
            ok &= report("G35 fails", " ".join(c for c in sorted(facts) if facts[c].get("g35") == "FAIL"), e["g35"])
        ok &= report("G33Q fails", " ".join(c for c in sorted(facts) if "G33Q" in facts[c]["fails"]), e["g33q"])
        ok &= report("G34 fails", sum(1 for c in facts if "G34" in facts[c]["fails"]), e["g34"])
        ok &= report("runs that saved nothing", " ".join(c for c in sorted(facts) if facts[c]["pv"] == "no save"), e["nosave"])
        ok &= report("preview-versus-save mismatches", " ".join(c for c in sorted(facts) if facts[c]["pv"] == "DIFF"), e["pv_diff"])
        ok &= report("D27, emergency runs failing G16/G21", d27, e["d27"])
        ok &= report("planted numbers outside caregiver and replies", sum(facts[c]["planted"] for c in facts), e["planted"])
        ok &= report("C36", "pass" if "C36" in facts and "C36" not in strict else "fail", e["c36"])
        if e["tools"] is not None:
            ok &= report("runs with another tool call", " ".join(c for c in sorted(facts) if facts[c]["tools"]), e["tools"])
        rerun_ok = True
        if run == "final18":
            os.makedirs(os.path.join(tmp, "rerun"))
            rf, _, rerr, _ = grade(run, "rerun", os.path.join(tmp, "rerun"))
            errors += rerr
            x = rf.get("C27", {})
            print("RECOUNT final18 C27 rerun (final18/rerun/C27.md), graded the same way, outside the totals above:")
            rerun_ok &= report("strict fails", ", ".join(x.get("fails", [])) + (" G35" if x.get("g35") == "FAIL" else ""), RERUN["strict"])
            rerun_ok &= report("G35 fails", "C27" if x.get("g35") == "FAIL" else "", RERUN["g35"])
            rerun_ok &= report("preview against save", x.get("pv"), RERUN["pv"])
            rerun_ok &= report("planted numbers", x.get("planted"), RERUN["planted"])
            rerun_ok &= report("another tool call", "C27" if x.get("tools") else "", RERUN["tools"])
        print("checkers that could not run: %d" % errors)
    good = ok and rerun_ok and errors == 0
    print("RECOUNT %s %s" % (run, "MATCHES RESULTS.md" if good else "DOES NOT MATCH RESULTS.md"))
    return 0 if good else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
