#!/usr/bin/env python3
"""Template fidelity: every delegation in a transcript equals one SKILL.md delegate template with its {VALUES} filled.
Usage: check_templates.py <SKILL.md> <transcript> [more transcripts]"""
import re, sys
skill = open(sys.argv[1]).read()
tpls = re.findall(r"`(delegate --target [a-z-]+ --instruction '.*?')`", skill)
assert len(tpls) >= 10, len(tpls)
pats = []
for t in tpls:
    parts = re.split(r"(\{[A-Z_]+\})", t)
    rx = "".join("(.+?)" if re.fullmatch(r"\{[A-Z_]+\}", p) else re.escape(p) for p in parts)
    pats.append((t[:60], re.compile(rx, re.S)))
total = bad = 0
for path in sys.argv[2:]:
    txt = open(path, errors="replace").read()
    turns = re.split(r"(?m)^(?=T[\d?]+ )", txt)
    for tu in turns:
        if not re.match(r"T[\d?]+ ASSISTANT DELEGATE", tu):
            continue
        line = tu.split(":", 1)[1].strip().strip("`").strip()
        line = line.split("\n")[0].strip()
        total += 1
        if not any(p.fullmatch(line) for _, p in pats):
            bad += 1
            print("OFF-TEMPLATE %s: %s" % (path, line[:150]))
print("TEMPLATES %s: %d delegations, %d off-template (%d templates)" % ("PASS" if bad == 0 else "FAIL", total, bad, len(pats)))
sys.exit(1 if bad else 0)
