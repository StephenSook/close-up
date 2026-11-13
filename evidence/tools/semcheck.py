#!/usr/bin/env python3
"""Catalog-semantics checks the official checker does not do.

Usage: python3 -I semcheck.py <catalog.json> <skill-dir-or-file> [more files...]

Reads SKILL.md and references/*.md (text only, never executes anything).
Reports:
  - every (cli, action) mention and whether it exists in the catalog
  - every --param used on a cli.invoke line and whether it exists for that action
  - state-change actions with their line and whether an approval word sits within
    +-6 lines (heuristic; manual reading decides)
  - delegate --target counts per agent
  - bare action-name mentions (backticked) that match no catalog action
"""
import json
import os
import re
import sys

RENAMED = {("ug-knowledge", "process-materials"): ("ug-knowledge", "collect-evidence")}
APPROVAL_WORDS = re.compile(r"approv|confirm|consent|ask the user|user says|reply ['\"]?(yes|go|save)|permission|explicit", re.I)


def load_catalog(path):
    c = json.load(open(path, encoding="utf-8"))
    acts = {}
    for cl in c["clis"]:
        for a in cl["actions"]:
            acts[(cl["name"], a["name"])] = {
                "params": {p["name"] for p in a.get("parameters", [])},
                "required": {p["name"] for p in a.get("parameters", []) if p.get("required")},
                "effect": a.get("effect"),
                "approval": a.get("approval"),
                "agent": cl.get("agent"),
            }
    clis = {cl["name"] for cl in c["clis"]}
    return acts, clis


def files_of(target):
    out = []
    if os.path.isdir(target):
        for root, _dirs, fs in os.walk(target):
            for f in sorted(fs):
                if f.lower().endswith(".md"):
                    out.append(os.path.join(root, f))
    else:
        out.append(target)
    return out


def main():
    acts, clis = load_catalog(sys.argv[1])
    action_names = {a for (_c, a) in acts}
    files = []
    for t in sys.argv[2:]:
        files += files_of(t)
    cli_alt = "|".join(sorted((re.escape(c) for c in clis), key=len, reverse=True))
    invoke_re = re.compile(r"--cli\s+[`'\"]?(" + cli_alt + r")[`'\"]?\s+--action\s+[`'\"]?([a-z0-9\-]+)")
    prose_re = re.compile(r"\b(" + cli_alt + r")[`'\"]?[\s/:.]+[`'\"]?([a-z][a-z0-9\-]+)")
    deleg_re = re.compile(r"delegate\s+--target\s+[`'\"]?([a-z\-]+)")
    tick_re = re.compile(r"`([a-z][a-z0-9]*(?:-[a-z0-9]+)+)`")
    seen = {}
    bad_params = []
    deleg = {}
    unknown_ticks = set()
    bare = {}
    for f in files:
        lines = open(f, encoding="utf-8", errors="replace").read().splitlines()
        rel = os.path.relpath(f)
        for i, line in enumerate(lines, 1):
            for m in deleg_re.finditer(line):
                deleg.setdefault(m.group(1), []).append(f"{os.path.basename(f)}:{i}")
            found = []
            for m in invoke_re.finditer(line):
                found.append((m.group(1), m.group(2), True, m.end()))
            for m in prose_re.finditer(line):
                found.append((m.group(1), m.group(2), False, m.end()))
            for cli, act, is_inv, end in found:
                key = (cli, act)
                key = RENAMED.get(key, key)
                if not is_inv and key not in acts and act not in action_names:
                    continue  # prose word after a cli name that is not an action name: ignore
                ok = key in acts
                seen.setdefault((cli, act), {"ok": ok, "where": []})["where"].append(f"{os.path.basename(f)}:{i}")
                if is_inv and ok:
                    rest = line[end:]
                    used = set(re.findall(r"(?<![\w-])--([a-z][a-z0-9\-\.]*)", rest))
                    used -= {"cli", "action"}
                    extra = used - acts[key]["params"]
                    if extra:
                        bad_params.append((cli, act, sorted(extra), f"{os.path.basename(f)}:{i}"))
            for m in tick_re.finditer(line):
                w = m.group(1)
                if w in action_names or w in clis:
                    continue
                unknown_ticks.add(w)
            for w in re.findall(r"(?<![\w-])([a-z]+(?:-[a-z0-9]+)+)(?![\w-])", line):
                if w in action_names:
                    bare.setdefault(w, []).append(f"{os.path.basename(f)}:{i}")
            for w in re.findall(r"`([a-z]+)`", line):
                if w in action_names:
                    bare.setdefault(w, []).append(f"{os.path.basename(f)}:{i}")
    print("== actions mentioned")
    for (cli, act), v in sorted(seen.items()):
        info = acts.get(RENAMED.get((cli, act), (cli, act)))
        eff = f"{info['effect']}/{info['approval']}" if info else "NOT IN CATALOG"
        print(f"  {'OK ' if v['ok'] else 'BAD'} {cli} {act} [{eff}] x{len(v['where'])} first {v['where'][0]}")
    print("== params not in catalog for that action (cli.invoke lines)")
    for b in bad_params:
        print("  ", b)
    if not bad_params:
        print("   none")
    print("== state-change actions (check approval gating by reading)")
    for (cli, act), v in sorted(seen.items()):
        info = acts.get(RENAMED.get((cli, act), (cli, act)))
        if info and info["effect"] in ("state-change", "mixed"):
            print(f"  {cli} {act} effect={info['effect']} approval={info['approval']} at {', '.join(v['where'][:8])}")
    print("== delegate --target counts")
    tot = 0
    for a, w in sorted(deleg.items()):
        tot += len(w)
        print(f"  {a}: {len(w)}  ({', '.join(w[:12])})")
    print(f"  TOTAL {tot}")
    print("== bare action-name mentions (no cli prefix); effect from any cli that has that action")
    for w, where in sorted(bare.items()):
        effs = sorted({f"{c}:{v['effect']}/{v['approval']}" for (c, a), v in acts.items() if a == w})
        print(f"  {w} x{len(where)} first {where[0]}  [{'; '.join(effs)}]")
    print("== backticked hyphen-words that are not catalog actions/clis (may be invented actions OR ordinary words)")
    print("  ", ", ".join(sorted(unknown_ticks))[:3000])


if __name__ == "__main__":
    main()
