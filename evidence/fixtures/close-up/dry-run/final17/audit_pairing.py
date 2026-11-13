#!/usr/bin/env python3
"""Read-only audit: was each expert reply a run used preceded by its delegation?
Two checks per transcript:
 A. every EXPERT REPLY turn follows a delegation (or a caregiver approval after a waiting_approval reply);
 B. every caregiver message that depends on a kind of reply comes after a delegation of that kind.
Usage: audit_pairing.py <transcript.md> [...]   prints one line per file, exit 0 always (it is an audit, not a gate)."""
import re, sys
KINDS = {  # kind: (delegation marker, message markers that use that kind of reply)
 "user folder": ("Return the path of the own folder", []),
 "page lookup": ("list the files whose names start with Close-Up page", ["Found the page for", "No saved page was found", "Your saved page from", "Your saved page could not be read"]),
 "notes": ("--target document-agent", ["Asked, not followed:"]),
 "labels": ("with OCR", ["From the labels, I read", "No medicine could be read"]),
 "photo check": ("one photo at a time, with the local vision model", ["Which photo goes on the page"]),
 "cameras": ("List every camera on this NAS", ["The camera list came back empty", "Cameras:", "Cameras found:", "Cameras on this NAS:"]),
 "events": ("list events of the type Human", ["Is one of these them?"]),
 "save": ("--target knowledge-agent", ["Your page is saved as", "may be saved, but it could not be checked", "but it reads back differently"]),
 "page read-back": ("in full and return its text word for word and its modified date", ["Your page is saved as", "but it reads back differently"]),
 "album create": ("Create one new album named", ["was created in UGREEN Photos", "was made, but it does not hold"]),
 "album read-back": ("Read the album named exactly", ["was created in UGREEN Photos", "was made, but it does not hold"]),
}
def turns(t):
    out = []
    for x in re.split(r"(?m)^(?=T[\d?]+ )", t):
        m = re.match(r"T[\d?]+ (CAREGIVER|ASSISTANT TO CAREGIVER|ASSISTANT DELEGATE|EXPERT REPLY|END|MISSING)", x)
        if m: out.append((m.group(1), x))
    return out
def audit(path):
    ts = turns(open(path, encoding="utf-8").read())
    bad = []
    pending = waiting = False
    for i, (k, x) in enumerate(ts):
        if k == "ASSISTANT DELEGATE": pending = True
        elif k == "EXPERT REPLY":
            if not (pending or waiting): bad.append("A: reply at turn %d follows no delegation" % i)
            body = x.split(":", 1)[1].strip().lower()
            waiting = body.startswith("waiting_approval"); pending = False
        elif k == "CAREGIVER" and waiting: pass
    for kind, (dmark, msgs) in KINDS.items():
        dels = [i for i, (k, x) in enumerate(ts) if k == "ASSISTANT DELEGATE" and dmark in x]
        for i, (k, x) in enumerate(ts):
            if k != "ASSISTANT TO CAREGIVER": continue
            for mm in msgs:
                if mm in x and not any(d < i for d in dels):
                    bad.append("B: %s message at turn %d (%r) with no %s delegation before it" % (kind, i, mm, kind))
    return bad
n = 0
for p in sys.argv[1:]:
    b = audit(p)
    n += bool(b)
    print("%s %s%s" % ("USED-WITHOUT-DELEGATION" if b else "ok", p, "".join("\n   " + y for y in b)))
print("replies used without a sent delegation: %d of %d runs" % (n, len(sys.argv) - 1))
