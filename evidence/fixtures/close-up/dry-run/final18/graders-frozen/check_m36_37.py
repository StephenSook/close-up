#!/usr/bin/env python3
"""G28 and G29 for the fixed preview header (M36) and candidate line (M37).

Usage: python3 -I check_m36_37.py <transcript.md> [...]
G28: in a calm run (no M19), every step 7 preview header, the text in the preview turn
     before "Close-Up page for", is M36 word for word with values filled, and the variant
     matches the question: the album variant with "Save this page and create the album?",
     the no-photo variant with "Save this page?".
G29: in the turn that asks "Which photo goes on the page?", every numbered candidate line
     is M37: date with capture or file date, or "date missing", the library on the album route only, the Visible part
     with the AI label or "Visible: not checked.", and Shown.
Exit 0 when every file passes, 1 otherwise, 2 on usage.
"""
import re, sys

M19 = "Call the police now"
DATE = r"(?:[A-Z][a-z]{2} \d{1,2}, \d{4})"
CDATE = r"(?:[A-Z][a-z]{2} \d{1,2}, \d{4}|\d{4}-\d{2}-\d{2})"
HDR_ALBUM = re.compile(r"^Preview\. Folder: \S[^\n]*?\. File name hint: Close-Up page \S[^\n]*? " + DATE + r"\. "
                       r"Album: Close-Up page \S[^\n]*? " + DATE + r" \d{1,2}:\d{2} [AP]M, with the photo you picked\. "
                       r"Approvals to come: the page save, then the album\.$")
HDR_PAGE = re.compile(r"^Preview\. Folder: \S[^\n]*?\. File name hint: Close-Up page \S[^\n]*? " + DATE + r"\. "
                      r"Approvals to come: the page save\.$")
CAND = re.compile(r"^\d\. (?:" + CDATE + r" \((?:capture|file) date\)|date missing)(?P<lib>, [a-z]+ library)?\. "
                  r"(?:Visible: (?!not )[^\n]+ \(AI description, may be wrong\)\. Shown: [^\n]+\.|Visible: not checked\. Shown: one of the newest\.|Visible: not returned\. Shown: [^\n]+\.)$")


def turns(text):
    return re.split(r"\n(?=T[0-9?]+ )", text)


def body(turn):
    b = re.sub(r"^T[0-9?]+ ASSISTANT TO CAREGIVER[^:\n]*:\s*", "", turn)
    return "\n".join(l.strip().strip('"').strip() for l in b.splitlines())


def check(path):
    t = open(path, encoding="utf-8").read()
    ts = turns(t)
    asst = [body(x) for x in ts if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x)]
    emergency = any(M19 in a for a in asst)
    out = []
    ok = True
    if not emergency:
        # each preview turn, with the assistant turns that follow it before the caregiver answers
        # (the save question may be its own message)
        prev = []
        for i, x in enumerate(ts):
            if not re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x):
                continue
            a = body(x)
            start = i + 1
            # M36 may be its own message when the very next assistant turn starts with the page
            if a.lstrip().startswith("Preview") and "Close-Up page for" not in a and i + 1 < len(ts) \
                    and re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", ts[i + 1]) \
                    and body(ts[i + 1]).lstrip().startswith("Close-Up page for"):
                a = a.rstrip() + "\n\n" + body(ts[i + 1])
                start = i + 2
            if "Close-Up page for" in a and a.lstrip().startswith("Preview"):
                tail = a
                for y in ts[start:]:
                    if not re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", y):
                        break
                    tail += "\n" + body(y)
                prev.append(tail)
        saved = "delegate --target knowledge-agent" in t
        if not prev:
            if saved:
                ok = False
                out.append("G28 FAIL a page was saved but no step 7 preview starting with M36 was found")
            else:
                out.append("G28 no calm preview and no save (nothing to check)")
        for a in prev:
            hdr = " ".join(a.split("Close-Up page for")[0].split())
            album_q = "Save this page and create the album?" in a
            page_q = "Save this page? (yes / no)" in a
            rx = HDR_ALBUM if album_q else HDR_PAGE
            good = bool(rx.match(hdr)) and (album_q or page_q)
            ok &= good
            out.append("G28 %s %s | %s" % ("PASS" if good else "FAIL", "album" if album_q else "page", hdr[:160]))
    else:
        out.append("G28 skipped (emergency run, E4 preview unchanged)")
    # candidate lines may sit in the question turn or in assistant turns between the photo check and it
    pick = []
    start = None
    route = None
    for i, x in enumerate(ts):
        m = re.match(r"T[0-9]+ ASSISTANT DELEGATE:\s*`?\s*delegate --target photo-agent --instruction '(Find the person album|Check only these image files)", x)
        if m:
            start = i
            route = "album" if m.group(1).startswith("Find") else "folder"
        if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x) and "Which photo goes on the page?" in x:
            span = ts[(start + 1 if start is not None else i):i + 1]
            pick.append((route, "\n".join(body(y) for y in span if re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", y))))
            start = None
    for route_here, a in pick:
        album_route = (route_here == "album") if route_here else ("Find the person album" in t)
        lines = [l.strip() for l in a.splitlines() if re.match(r"\s*\d\. ", l)]
        if not lines:
            ok = False
            out.append("G29 FAIL no numbered candidate line")
        for l in lines:
            m = CAND.match(l)
            good = bool(m) and (bool(m.group("lib")) == album_route)
            ok &= good
            out.append("G29 %s %s" % ("PASS" if good else "FAIL", l[:160]))
    print("%s %s" % (path, "PASS" if ok else "FAIL"))
    for o in out:
        print("   " + o)
    return ok


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    res = [check(p) for p in argv]
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
