# Dry-run runner (fixture test, not a device test)

Design (single pass, chosen 2026-11-11 because a turn-by-turn run of 12 cases would take about 170 round trips):
- One subagent per case, on model haiku (the smallest model available here), plays the Uliya parent model AND plays the caregiver and the experts only by looking up the written answers in the case file. It reads the package files and one case file, nothing else.
- It returns the whole run as a numbered transcript. The builder checks every assertion in ASSERTIONS.md against that transcript and marks PASS or FAIL with the turn number. A FAIL becomes a row in DEFECTS.md.
- Limit, stated in testing.md: because the subagent sees the case file's answers up front, this tests whether a small model can follow SKILL.md's order, messages, values and branches, not whether it can wait for answers it has not seen.
- The package is read from the live files when each case starts, so a fix is in effect from the next case on. After the last fix, every case runs again.

## Prompt given to each subagent (verbatim, with the case file name filled in)

You are testing a Skill by playing the assistant that follows it. Read these files with the Read tool and nothing else:
- skill-check/skills/close-up/SKILL.md
- every file in skill-check/skills/close-up/references/
- the case file: skill-check/fixtures/close-up/dry-run/cases/{CASE}.md
Do not open any other file.

You are Uliya, the assistant on a family's UGREEN NAS, and the Skill close-up is loaded. Follow SKILL.md exactly, using the references when it says to. You cannot touch the NAS yourself.

Produce the whole run as numbered turns, in this form:
- "T1 CAREGIVER: ..." for the caregiver's words, taken from the case file.
- "T2 ASSISTANT TO CAREGIVER: ..." for each message you send, word for word.
- "T3 ASSISTANT DELEGATE: ..." for each delegation, the exact delegate line with every value filled in.
- "T4 EXPERT REPLY: ..." for the expert's state and result, copied from the case file's reply for that kind of task. (From C02 on: the state, then "as in the case file" plus only the values used next.)
- "T5 END: ..." with the state the run ends in.
One action per turn. When the case file has no caregiver answer or expert reply for what you need, write "T? MISSING: ..." saying what you needed, then end the run. Never invent an answer or a reply. Do not judge your own run. Return only the transcript.
