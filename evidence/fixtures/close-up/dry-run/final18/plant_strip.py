#!/usr/bin/env python3
"""Plant test for graders/strip_role_notes.py, run once before final18 run 1.

Usage (from fixtures/close-up/dry-run): python3 -I final18/plant_strip.py
Base: final17/C01.md, a scored run with 0 strict fails, an album step and G30 PASS.
Plants (made up from that run, written to a temp folder, never scored):
 P1 labelled: every delegation and caregiver-message label gets a runner note, as in
    smokeb3/C28. The frozen graders must report the parse failure.
 P2 labelled then stripped: must be byte for byte the base, and pass G30 and G29.
 P3 real ordering fault: the page close message moved before the album create
    delegation, then labelled, then stripped. G30 must still FAIL, on ordering.
Exit 0 only when every expectation holds.
"""
import os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
DRY = os.path.dirname(HERE)
G = os.path.join(DRY, "graders")
sys.path.insert(0, G)
from strip_role_notes import strip  # noqa: E402

BASE = os.path.join(DRY, "final17", "C01.md")


def run(script, path):
    r = subprocess.run([sys.executable, "-I", os.path.join(G, script), path], capture_output=True, text=True)
    return r.returncode, r.stdout


def label(text):
    text = re.sub(r"(?m)^(T[0-9?]+ ASSISTANT DELEGATE):", r"\1 (step note, from the runner):", text)
    return re.sub(r"(?m)^(T[0-9?]+ ASSISTANT TO CAREGIVER):", r"\1 (message note):", text)


def fault(text):
    blocks = re.split(r"(?m)^(?=T[0-9?]+ )", text)
    page = [i for i, b in enumerate(blocks) if b.startswith("T") and "ASSISTANT TO CAREGIVER: Your page is saved as" in b]
    album = [i for i, b in enumerate(blocks) if "ASSISTANT DELEGATE:" in b and "Create one new album" in b]
    assert len(page) == 1 and len(album) == 1 and page[0] > album[0], "base layout changed"
    b = blocks.pop(page[0])
    blocks.insert(album[0], b)
    return "".join(blocks)


def main():
    base = open(BASE, encoding="utf-8").read()
    ok = True
    with tempfile.TemporaryDirectory() as d:
        def w(name, text):
            p = os.path.join(d, name)
            open(p, "w", encoding="utf-8").write(text)
            return p

        rc, out = run("check_g30.py", BASE)
        rc2, out2 = run("check_m36_37.py", BASE)
        good = rc == 0 and "G30 PASS" in out and rc2 == 0
        print("base     G30 %s | G28/G29 exit %d | %s" % (out.split(" G30 ", 1)[-1].strip()[:60], rc2, "ok" if good else "UNEXPECTED"))
        ok &= good

        p1 = w("P1.md", label(base))
        rc, out = run("check_g30.py", p1)
        good = rc == 1 and "no album delegation parsed" in out
        print("P1 label G30 %s | %s" % (out.split(" G30 ", 1)[-1].strip()[:70], "ok (parse failure, as planted)" if good else "UNEXPECTED"))
        ok &= good

        s2, n2 = strip(label(base))
        p2 = w("P2.md", s2)
        rc, out = run("check_g30.py", p2)
        rc2, out2 = run("check_m36_37.py", p2)
        good = s2 == base and rc == 0 and "G30 PASS" in out and rc2 == 0
        print("P2 strip %d labels, byte-identical to base: %s | G30 %s | G28/G29 exit %d | %s"
              % (n2, s2 == base, out.split(" G30 ", 1)[-1].strip()[:40], rc2, "ok" if good else "UNEXPECTED"))
        ok &= good

        s3, n3 = strip(label(fault(base)))
        p3 = w("P3.md", s3)
        rc, out = run("check_g30.py", p3)
        good = rc == 1 and "G30 FAIL (first page message at" in out
        print("P3 fault stripped %d labels | G30 %s | %s"
              % (n3, out.split(" G30 ", 1)[-1].strip()[:70], "ok (ordering fail kept)" if good else "UNEXPECTED"))
        ok &= good
    print("plant test %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
