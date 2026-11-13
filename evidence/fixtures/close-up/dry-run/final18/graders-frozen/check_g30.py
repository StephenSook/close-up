#!/usr/bin/env python3
"""G30: when the album step runs, the page close message comes after it.

Usage: python3 -I check_g30.py <transcript.md> [...]
The page close message is M20 ("Your page is saved as"), M14 ("The page was saved as") or the
page form of M26 ("The page may be saved"). The album step is every album create and album
read-back delegation. If the run sends any album delegation, the first page close message must
come after the last of them. Runs with no album delegation or no page close message are not checked.
Exit 0 when every file passes, 1 otherwise, 2 on usage.
"""
import re, sys

PAGE = re.compile(r"Your page is saved as|The page was saved as|The page may be saved")
ALBUM = re.compile(r"T[0-9]+ ASSISTANT DELEGATE:\s*`?\s*delegate --target photo-agent --instruction '(Create one new album|Read the album)")


def check(path):
    t = open(path, encoding="utf-8").read()
    pages = []
    for m in re.finditer(r"(?:^|\n)(T[0-9?]+ [A-Z][A-Z ]+?:)(.*?)(?=\nT[0-9?]+ [A-Z]|\Z)", t, re.S):
        if m.group(1).startswith("T") and "ASSISTANT TO CAREGIVER" in m.group(1):
            hit = PAGE.search(m.group(2))
            if hit:
                pages.append(m.start(2) + hit.start())
    albums = [m.start() for m in ALBUM.finditer(t)]
    if not albums and "Create one new album" in t:
        print("%s G30 FAIL (album text found but no album delegation parsed: check the transcript form)" % path)
        return False
    if not pages or not albums:
        print("%s G30 n/a (page messages %d, album delegations %d)" % (path, len(pages), len(albums)))
        return True
    ok = pages[0] > albums[-1]
    print("%s G30 %s (first page message at %d, last album delegation at %d)" % (path, "PASS" if ok else "FAIL", pages[0], albums[-1]))
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
