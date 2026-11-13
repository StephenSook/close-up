#!/usr/bin/env python3
"""C01.20 (B2): the page's photo line names the file, the album gets the picture ID alone.

Usage: python3 -I check_c01_20.py <transcript.md> [...]
In the page-save delegation, the Photo line names IMG_0107.jpg and does not give P01 as the photo
name. In the album create delegation, the photos are P01 alone: no file name, no path.
Exit 0 when every file passes, 1 otherwise, 2 on usage.
"""
import re, sys


def check(path):
    t = open(path, encoding="utf-8").read()
    out, ok = [], True
    save = re.search(r"delegate --target knowledge-agent --instruction '[^\n]*", t)
    if not save:
        ok = False
        out.append("no page-save delegation")
    else:
        m = re.search(r"Photo: ([^,\\]*)", save.group(0))
        name = m.group(1).strip() if m else ""
        good = "IMG_0107.jpg" in name and "P01" not in name
        ok &= good
        out.append("photo line %s (%r)" % ("PASS" if good else "FAIL", name))
    alb = re.search(r"Create one new album named [^\n]*?nothing else: ([^.]*(?:\.jpg)?[^.]*)\.", t)
    if not alb:
        ok = False
        out.append("no album create")
    else:
        items = alb.group(1).strip()
        good = items == "P01"
        ok &= good
        out.append("album items %s (%r)" % ("PASS" if good else "FAIL", items))
    print("%s C01.20 %s | %s" % (path, "PASS" if ok else "FAIL", " | ".join(out)))
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(0 if all([check(p) for p in sys.argv[1:]]) else 1)
