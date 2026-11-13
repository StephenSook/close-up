#!/usr/bin/env python3
"""G32: text sent to the caregiver that no package file writes (D49).

Usage: python3 -I check_g32.py <package dir with SKILL.md> <transcript.md> [...]
The package dir is the one the run used: each run is measured against its own package's texts.
Exit 0 when no run has a FAIL item, 1 otherwise, 2 on usage.

What was sent (orchestrator ruling a): in an ASSISTANT TO CAREGIVER turn, quoted text was sent and unquoted
text is the runner annotating. A turn whose body starts with a double quote sent the span from its first to its
last double quote. A turn with no quote at all sent its body, except a line wholly in round brackets.

What is designed: the fixed messages in messages.md (values filled in, with the variants it names), the
questions SKILL.md writes in quotes, the first-run list with its headings, the step 7 preview (M36, then the page
from its title to the save question, which other checks grade), the numbered lines of the candidate, medicine and
change lists, and the lines of a "Changed since your last page" list. Step-named questions with no fixed text
(who the page is for, keep or drop each change, whether another page is this person, who confirmed, the short
emergency question) are designed when they ask what the step names.

Every other piece of sent text is classified (orchestrator rulings of 2026-11-12 and 2026-11-13):
  SENTENCE  it has a verb, or it is longer than 6 words, and is not a question
  QUESTION  the same, ending in a question mark
  LABEL     6 words or fewer with no verb, such as a heading
G32 is reported, not a gate: it prints "designed-only" or "undesigned" with the counts, never a pass or fail
word, so it cannot be counted as a check failure. G32Q gates: its own line reads PASS, or FAIL when the run sent
an undesigned question. Exit 0 when every run sent only designed text, 1 otherwise.
"""
import os, re, sys

VERBS = set("""am is are was were be been being has have had do does did can could will would shall should may
might must answer answered ask asked call called check checked choose chose confirm confirmed drop dropped find
found get give given go goes going help keep kept know let look looks looked make made name named need open opened
hold holds held match matches matched come came comes
pick picked print printed read reads removed save saved say says said see seen send sent show shown skip start
started stay stays take taken tell think try use used wait want wear wears went write written please""".split())


def placeholder_rx(s):
    """A fixed text with {values} as a regex that matches it with any filled values.
    A value that ends the text runs to the end of the line."""
    out, i = [], 0
    ms = list(re.finditer(r"\{[^}]+\}", s))
    for k, m in enumerate(ms):
        out.append(re.escape(s[i:m.start()]))
        last = k == len(ms) - 1 and not s[m.end():].strip(" .")
        out.append(r"[^\n]+" if last else r"[^\n]+?")
        i = m.end()
    out.append(re.escape(s[i:]))
    return "".join(out)


def sentences(s):
    """The sentences of a fixed text, split after . ? or ! that ends a sentence, not inside a {value}."""
    parts, depth, cur = [], 0, ""
    for i, ch in enumerate(s):
        cur += ch
        depth += ch == "{"
        depth -= ch == "}"
        if depth == 0 and ch in ".?!" and (i + 1 == len(s) or s[i + 1] == " "):
            parts.append(cur.strip())
            cur = ""
    if cur.strip():
        parts.append(cur.strip())
    return [p for p in parts if len(p) > 3]


def designed(pkg):
    msgs = open(os.path.join(pkg, "references", "messages.md"), encoding="utf-8").read()
    skill = open(os.path.join(pkg, "SKILL.md"), encoding="utf-8").read()
    frq = open(os.path.join(pkg, "references", "first-run-questions.md"), encoding="utf-8").read()
    texts = []
    for line in msgs.splitlines():
        if not re.match(r"- M\d+ ", line):
            continue
        texts += re.findall(r'"([^"]+)"', line)
    # quoted questions and report lines in SKILL.md, not delegations
    for q in re.findall(r'"([^"\n]{12,})"', skill):
        if not q.startswith(("make ", "Dad ", "Close-Up page")) and "--target" not in q:
            texts.append(q)
    texts.append("or keep the photo from your page")
    # the first-run questions, one by one, without their numbers
    qlines = [re.sub(r"^\s*\d+\.\s+", "", l).strip() for l in frq.splitlines() if re.match(r"\s*\d+\.\s", l)]
    texts += qlines
    # whole texts first, longest first, then each sentence of each text: a sentence a package file writes is
    # designed even when the run sent it apart from the rest of its message
    def literal(t):
        return len(re.sub(r"\{[^}]+\}", "", t).strip(" .,:?"))
    whole = sorted({t for t in texts if literal(t) >= 8}, key=len, reverse=True)
    parts = sorted({p for t in texts for p in sentences(t) if literal(p) >= 8} - set(whole), key=len, reverse=True)
    # step 6's pick question with only the numbers shown, and its keep option inside or after the brackets
    pick = r"Which photo goes on the page\? \((?:\d, )*\d,? (?:or )?none(?:,? or keep the photo from your page)?\)(?:,? or keep the photo from your page)?"
    rx = ([re.compile(pick)] + [re.compile(placeholder_rx(t)) for t in whole],
          [re.compile(placeholder_rx(t) + r"\Z") for t in whole + parts])
    headings = [l.strip() for l in frq.splitlines() if re.match(r"[A-Z][^.?]*:\s*$", l.strip())]
    lines = set(l.strip() for l in frq.splitlines() if re.match(r"\s*\d+\.\s", l)) | set(headings)
    # a package without M36 names the preview header in step 7 instead ("Preview the page, folder, file name
    # hint, album name and the approvals to come"): there, header parts naming those fields are step-named
    extra = []
    if "file name hint, album name and the approvals to come" in skill:
        extra = [re.compile(r"^Preview\b[^?]{0,40}[.:]?$"), re.compile(r"^(Pages )?[Ff]older: \S"),
                 re.compile(r"^File name( hint)?: \S"), re.compile(r"^Album( name)?: "), re.compile(r"\bapprov", re.I)]
    return rx, (lines, headings, extra)


STEP_NAMED = [
    # step 1 and E0: ask who the page is for, or who is missing
    re.compile(r"^Who (is|are) [^.?]{0,40}\?$", re.I),
    # step 7: each difference kept or dropped
    re.compile(r"(keep|drop).*(keep|drop)", re.I),
    # step 3: whether a page for another name is this person
    re.compile(r"\bis (one of them|this|that page|the page for \w+) (the same person|this person|him|her|them)\b", re.I),
    re.compile(r"^Is (that|this|the) page (for )?[^?]{0,30}\?$", re.I),
    re.compile(r"^Is (it|that|this) [A-Z]\w*'s page\?$"),
    # E1 and M7: ask for the person album or a photo folder
    re.compile(r"\b(person album|photo folder)\b[^.]*\?$", re.I),
    # E2: the camera and time window the caregiver picks
    re.compile(r"\bfrom what time\b|\btime window\b", re.I),
    # E4: the short question, also when a run splits it in parts
    re.compile(r"\b(condition police should know|should police call|who police should call)\b", re.I),
    # step 4 on a refresh: each notes difference listed with its source
    re.compile(r"\bnotes?\b.*\bwas\b.*\bnow\b", re.I),
    # step 7: each difference listed for keep or drop, with or without a list mark
    re.compile(r"^[A-Z][^:]{1,60}: was .+, now .+"),
    # M25 with one count or more
    re.compile(r"^\d+ shown, \d+ not shown: [^\n]+\.$"),
    # step 7: who confirmed, when the last page names no one
    re.compile(r"\bwho (confirmed|is confirming|confirms)\b", re.I),
    # E4: the one short question for a page with no saved page
    re.compile(r"date of birth.*condition.*call", re.I),
    # E2: list the cameras returned, and the camera and time window the caregiver picks
    re.compile(r"^Cameras( on this NAS| found| returned)?:", re.I),
    re.compile(r"\bcamera\b.*\btime\b|\btime\b.*\bcamera\b", re.I),
    # E2: the events and snapshots shown, one line each
    re.compile(r"^\d{1,2}:\d{2}( [AP]M)?\b[^.?!]{0,30}snapshot:? ?\S+$"),
    # SKILL.md reads: a named file that is a credential or system file is not read, and the run says so
    re.compile(r"\bnot (be )?read\b.*(system|credential|config\.json|\.env|\.ssh|\.git|key|certificate)", re.I),
    # the delegation rules: a path or name with a character a delegation cannot carry is not sent, and the run says so
    re.compile(r"\b(path|name|folder|file)\b.*\b(pipe|angle bracket|backtick|double hyphen|ampersand|dollar sign)\b"
               r".*\b(not sent|cannot be sent|could not be sent|not be sent)\b", re.I),
    # E2: a camera with no camera_id cannot be checked, and the run says so
    re.compile(r"\bcamera\b.*\b(no camera_id|no identifier|cannot be checked)\b", re.I),
]


def sent_text(turn):
    b = re.sub(r"^T[0-9?]+ ASSISTANT TO CAREGIVER[^:\n]*:[ \t]*", "", turn).strip()
    if not b:
        return ""
    if b.startswith(("\"", "`\"")) and b.count('"') >= 2:
        b = b[b.index('"'): b.rindex('"') + 1]
        b = re.sub(r'"\s+"', "\n", b)
        return "\n".join(l.strip().strip('"').strip() for l in b.splitlines())
    if '"' in b and not b.startswith('"'):
        # a turn that opens unquoted and quotes later: the quoted part is what was sent
        qs = re.findall(r'"([^"]*)"', b)
        if qs and sum(len(q) for q in qs) > 0.5 * len(b):
            return "\n".join(qs)
    return "\n".join(l.strip() for l in b.splitlines() if not re.fullmatch(r"\s*\([^()]*\)\s*", l))


def classify(piece):
    words = re.findall(r"[A-Za-z']+", piece)
    # a question is a sentence, and so is anything with a word from the verb list
    has_verb = piece.rstrip().endswith("?") or any(w.lower() in VERBS for w in words)
    if has_verb or len(words) > 6:
        return "QUESTION" if piece.rstrip().endswith("?") else "SENTENCE"
    # orchestrator ruling 4: a short piece with no verb is a label, with or without a colon
    return "LABEL"


def check(pkg_rx, frq, path):
    frq_lines, headings, extra = frq
    t = open(path, encoding="utf-8").read()
    turns = re.split(r"\n(?=T[0-9?]+ )", t)
    items = []
    for x in turns:
        if not re.match(r"T[0-9]+ ASSISTANT TO CAREGIVER", x):
            continue
        s = sent_text(x)
        # the preview page block, from the title to the save question, is graded by other checks
        s = re.sub(r"Close-Up page for .*?(?=Save this page|\Z)", "\n", s, flags=re.S)
        lines = [l.strip() for l in s.splitlines() if l.strip()]
        for l in lines:
            if l in frq_lines or re.match(r"\d+\.\s", l) or l.startswith("- ") or "Changed since your last page" in l:
                continue
            whole_rx, piece_rx = pkg_rx
            rest = l
            for r in whole_rx:
                rest = r.sub("\n", rest)
            for piece in re.split(r"\n|(?<=[.?!])\s+(?=[A-Z(])", rest):
                piece = piece.strip().strip('"').strip()
                if not piece or not re.search(r"[A-Za-z]", piece):
                    continue
                if any(r.match(piece) for r in piece_rx):
                    continue
                if any(p.search(piece) for p in STEP_NAMED + extra):
                    continue
                # a first-run heading sent shortened, like "Who they were:" for its full heading
                if piece.endswith(":") and any(h.split(" (")[0].rstrip(":") == piece.rstrip(":") for h in headings):
                    continue
                items.append((classify(piece), piece))
    n_s = sum(1 for k, _ in items if k == "SENTENCE")
    n_q = sum(1 for k, _ in items if k == "QUESTION")
    n_label = sum(1 for k, _ in items if k == "LABEL")
    # reported, not a gate (orchestrator ruling of 2026-11-13): no word here may read as a check failure
    print("G32 REPORT %s %s | undesigned sentences %d, undesigned questions %d, labels %d" % (
        "designed-only" if not (n_s or n_q) else "undesigned", path, n_s, n_q, n_label))
    for k, p in items:
        print("   %s: %s" % (k, p[:150]))
    # G32Q gates (orchestrator ruling of 2026-11-13): a question no package file writes and no step names asks the
    # caregiver for something the package never meant to ask
    print("G32Q %s %s | undesigned questions %d" % ("FAIL" if n_q else "PASS", path, n_q))
    return not (n_s or n_q)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    rx, frq = designed(argv[0])
    res = [check(rx, frq, p) for p in argv[1:]]
    return 0 if all(res) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
