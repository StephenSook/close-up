import re, sys
# For each transcript: lines of the last page block shown to the caregiver before the save
# versus the lines of the save delegation's Text. Prints counts of lines in one and not the other.
for p in sys.argv[1:]:
    t = open(p, encoding="utf-8").read()
    m = re.search(r"--target knowledge-agent --instruction '.*?Text: (.*)'", t)
    if not m:
        continue
    save_at = m.start()
    sv = m.group(1).rstrip("`").rstrip("'")
    sv = sv.replace("'\"'\"'", "'").replace('\\"', '"').split("\\n")
    head = t[:save_at]
    starts = [x.start() for x in re.finditer(r"Close-Up page for ", head)]
    if not starts:
        print(p, "no preview found"); continue
    blk = head[starts[-1]:].splitlines()
    import re as _re
    def norm(L):
        out = []
        for l in L:
            s = l.strip().replace('\\"', '"').strip('"').strip()
            if not s or s.startswith("```") or _re.match(r"T\d+ |T\? ", s):
                continue
            if s.startswith(("Save this page", "Folder:", "File name", "File folder", "Album", "Approvals", "Approval", "Two approvals", "(preview", "Preview", "Changes made", "Changes shown", "Change shown", "Change to the page", "One change made", "Replaced in the page", "Character change")):
                continue
            out.append(s)
        return out
    a, b = norm(blk), norm(sv)
    only_save = [l for l in b if l not in a]
    only_prev = [l for l in a if l not in b]
    tag = "SAME" if not only_save and not only_prev else "DIFF"
    print(p, tag, "save-only:", len(only_save), "preview-only:", len(only_prev), ("| " + (only_save[:1] or only_prev[:1])[0][:90]) if tag == "DIFF" else "")
