import re, sys
# G27: each save delegation's Text is the page itself, not a summary or a pointer.
# Its length (characters of its non-blank lines) must be within 10% of the length of the
# last preview page block shown before it. Uses the same block rules as check_preview_save.py.
STARTS = ("Save this page", "Folder:", "File name", "File folder", "Album", "Approvals", "Approval", "Two approvals", "(preview", "Preview", "Changes made", "Changes shown", "Change shown", "Change to the page", "One change made", "Replaced in the page", "Character change")
def norm(L):
    out = []
    for l in L:
        s = l.strip().replace('\\"', '"').strip('"').strip()
        if not s or s.startswith("```") or re.match(r"T\d+ |T\? ", s) or s.startswith(STARTS):
            continue
        out.append(s)
    return out
bad = 0; n = 0
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    for m in re.finditer(r"--target knowledge-agent --instruction '.*?Text: (.*)", t):
        n += 1
        sv = m.group(1).rstrip().rstrip("`").rstrip("'")
        sv = sv.replace("'\"'\"'", "'").split("\\n")
        head = t[:m.start()]
        starts = [x.start() for x in re.finditer(r"Close-Up page for ", head)]
        if not starts:
            print(p, "G27 FAIL: no preview before a save"); bad += 1; continue
        a = sum(len(x) for x in norm(head[starts[-1]:].splitlines()))
        b = sum(len(x) for x in norm(sv))
        r = b / a if a else 0
        ok = 0.9 <= r <= 1.1
        bad += not ok
        print(p, "G27", "PASS" if ok else "FAIL", f"save {b} chars, preview {a} chars, ratio {r:.2f}")
print(f"G27 {'PASS' if bad == 0 else 'FAIL'}: {n} save(s), {bad} outside 0.9 to 1.1")
