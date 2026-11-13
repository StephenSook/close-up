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
    import difflib
    rows = []
    if not only_save and not only_prev:
        if a != b:
            # same lines, other order or count
            rows.append(("position", "same lines, different order or repeat"))
    used = set()
    for sl in only_save:
        best, bi = 0.0, None
        for k, pl in enumerate(only_prev):
            if k in used:
                continue
            r = difflib.SequenceMatcher(None, sl, pl).ratio()
            if r > best:
                best, bi = r, k
        if bi is not None and best >= 0.8:
            used.add(bi)
            rows.append(("grammar or wording", "preview %r / save %r" % (only_prev[bi], sl)))
        else:
            # a line the save has that the page block lacks, but that the preview turn shows elsewhere
            turns = [x for x in re.split(r"\n(?=T[0-9?]+ )", head) if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x)]
            last_prev = next((x for x in reversed(turns) if "Close-Up page for " in x), "")
            if sl and sl in last_prev.replace('\\"', '"'):
                rows.append(("position", "shown outside the page block: %r" % sl))
            else:
                rows.append(("added line", repr(sl)))
    for k, pl in enumerate(only_prev):
        if k not in used:
            rows.append(("dropped line", repr(pl)))
    if not rows:
        print(p, "SAME")
    for kind, txt in rows:
        print(p, "MISS", kind, "|", txt[:220])
