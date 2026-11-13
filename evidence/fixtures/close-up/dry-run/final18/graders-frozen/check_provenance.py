#!/usr/bin/env python3
"""G34: the three input-provenance contracts from the catalog, checked on every delegation that uses them.

Usage: python3 -I check_provenance.py <transcript> [...]

- Notes (ug-document qa, query "The user's original question, passed verbatim without rewriting"): every
  document-agent delegation starts "Use this question, unchanged, as the query: " followed by the caregiver's first
  message in the run, word for word.
- Album write (create-album: add-item is for picture IDs the user named, search results use source-ref): every album
  create says "search the photos for the file name {file} only", where {file} is an image file name, creates "from
  that search result (its resultRef, as source-ref)", and never adds a picture ID as an item.
- Album read-back (album-detail's UUID "must come from an album list or be explicitly provided by the user"): every
  read-back starts "Read the album named exactly {name}:" with the name the create used, and lists the albums first.
Prints one PASS or FAIL line per delegation checked and "G34 n/a" when the run has none. Exit 1 on any FAIL.
"""
import re, sys


def turns(t):
    out = []
    for x in re.split(r"\n(?=T[0-9?]+ )", t):
        m = re.match(r"T[0-9?]+ (CAREGIVER|ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE|EXPERT REPLY|END|MISSING)[^:\n]*:\s*", x)
        if m:
            out.append((m.group(1), x[m.end():].strip()))
    return out


def norm(s):
    return s.replace("'\"'\"'", "'").replace('\\"', '"').strip().strip('"').strip()


def check(path):
    ts = turns(open(path, encoding="utf-8").read())
    first = next((norm(b) for k, b in ts if k == "CAREGIVER"), None)
    dels = [(i, norm(b)) for i, (k, b) in enumerate(ts) if k == "ASSISTANT DELEGATE"]
    ok, n, created = True, 0, []
    for i, d in dels:
        if "--target document-agent" in d:
            n += 1
            want = "Use this question, unchanged, as the query: " + (first or "")
            good = first is not None and want in d
            ok &= good
            print("G34 %s %s notes at turn %d | query is the first caregiver message %r" % ("PASS" if good else "FAIL", path, i, first))
        elif "--target photo-agent" in d and "Create one new album" in d:
            n += 1
            name = re.search(r"Create one new album named (.+?) that holds", d)
            f = re.search(r"search the photos for the file name (\S+?) only", d)
            good = bool(f and re.search(r"\.(jpe?g|png|heic|webp|gif|tiff?)$", f.group(1), re.I)) and \
                "from that search result (its resultRef, as source-ref)" in d and "never adding a picture ID as an item" in d
            if name:
                created.append(name.group(1))
            ok &= good
            print("G34 %s %s album create at turn %d | file %s, source-ref %s" % (
                "PASS" if good else "FAIL", path, i, f.group(1) if f else "none", "yes" if "as source-ref" in d else "no"))
        elif "--target photo-agent" in d and "Read the album" in d:
            n += 1
            m = re.search(r"Read the album named exactly (.+?): list the photo albums with that keyword", d)
            good = bool(m) and (not created or m.group(1) == created[-1])
            ok &= good
            print("G34 %s %s album read-back at turn %d | name %s, matches the create %s" % (
                "PASS" if good else "FAIL", path, i, m.group(1) if m else "none", (m.group(1) == created[-1]) if (m and created) else "n/a"))
    if not n:
        print("G34 n/a %s | no notes read, album create or album read-back" % path)
    return ok


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    return 0 if all([check(p) for p in argv]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
