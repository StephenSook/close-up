#!/usr/bin/env python3
"""G35: a run never uses an expert reply whose delegation it did not send first.

Usage: python3 -I check_pairing.py <transcript.md> [...]

On a real NAS no reply exists without its delegation, so a run that answers from a case
file's reply it never asked for is acting on data it does not have (final17 C13: "Found the
page for Dad" with no page lookup sent). Two checks per transcript:
 A. every EXPERT REPLY turn follows a delegation, or a caregiver approval after a
    waiting_approval reply;
 B. every message to the caregiver that uses a kind of reply comes after a delegation of
    that kind.
Prints "G35 PASS <file>" or "G35 FAIL <file> | <reason>" per file. Exit 1 on any FAIL.
"""
import re, sys

KINDS = {  # kind: (delegation marker, markers of caregiver messages that use that kind of reply)
    "page lookup": ("list the files whose names start with Close-Up page",
                    ["Found the page for", "No saved page was found", "Your saved page from",
                     "Your saved page could not be read"]),
    "notes": ("--target document-agent", ["Asked, not followed:"]),
    "labels": ("with OCR", ["From the labels, I read", "No medicine could be read"]),
    "photo check": ("one photo at a time, with the local vision model", ["Which photo goes on the page"]),
    "cameras": ("List every camera on this NAS",
                ["The camera list came back empty", "Cameras:", "Cameras found:", "Cameras on this NAS:"]),
    "events": ("list events of the type Human", ["Is one of these them?"]),
    "save": ("--target knowledge-agent",
             ["Your page is saved as", "may be saved, but it could not be checked", "but it reads back differently"]),
    "page read-back": ("in full and return its text word for word and its modified date",
                       ["Your page is saved as", "but it reads back differently"]),
    "album create": ("Create one new album named", ["was created in UGREEN Photos", "was made, but it does not hold"]),
    "album read-back": ("Read the album named exactly", ["was created in UGREEN Photos", "was made, but it does not hold"]),
}


def turns(text):
    out = []
    for x in re.split(r"(?m)^(?=T[\d?]+ )", text):
        m = re.match(r"T[\d?]+ (CAREGIVER|ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE|EXPERT REPLY|END|MISSING)", x)
        if m:
            out.append((m.group(1), x))
    return out


def check(path):
    ts = turns(open(path, encoding="utf-8").read())
    bad = []
    pending = waiting = False
    for i, (k, x) in enumerate(ts):
        if k == "ASSISTANT DELEGATE":
            pending = True
        elif k == "EXPERT REPLY":
            if not (pending or waiting):
                bad.append("reply at turn %d follows no delegation" % i)
            waiting = x.split(":", 1)[1].strip().lower().startswith("waiting_approval")
            pending = False
    for kind, (dmark, msgs) in KINDS.items():
        sent = [i for i, (k, x) in enumerate(ts) if k == "ASSISTANT DELEGATE" and dmark in x]
        for i, (k, x) in enumerate(ts):
            if k != "ASSISTANT TO CAREGIVER":
                continue
            for mm in msgs:
                if mm in x and not any(d < i for d in sent):
                    bad.append("%s message at turn %d (%r) with no %s delegation before it" % (kind, i, mm, kind))
    print("G35 %s %s%s" % ("FAIL" if bad else "PASS", path, (" | " + "; ".join(bad)) if bad else ""))
    return not bad


def main(argv):
    if not argv:
        print(__doc__)
        return 2
    return 0 if all([check(p) for p in argv]) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
