# Round 78 adjudication (Codex, diff-scoped)

Diff-scoped round on the two changes since Codex's round 76 (3d37365 to e9f55c3): round 76's testing.md sentence and round 77's step 7 sentence on the police line. Codex reported 0 CRITICAL, 1 HIGH, 0 MEDIUM and 1 LOW, checked against the package and earlier rounds.

| # | Finding | Verdict | Change |
|---|---|---|---|
| 1 | HIGH: when the vision check cannot read the photos, 5a and 5b return "up to the 3 newest" unchecked, and step 6 shows them, so a private care photo could be shown | Declined, settled in round 70 with no new evidence | Round 70 #1 raised the same case and adopted it in other words: M9 now ends "Look closely, and skip any private care photo." Returning no candidates would take away the recent photo whenever the vision check fails, often in the emergency the page exists for, and the photos shown are the caregiver's own, to the caregiver only. Nothing is described in that branch. Later briefs list this as settled. |
| 2 | LOW: testing.md says the cases are kept outside the package "so the model under test cannot read them", while the sentence before says it reads one case | Adopted, worded differently | testing.md: "The cases, what each one expects and every result are kept outside this package. The model under test reads only its own case, which holds no expected result." |

Not clean: the next round is Grok, diff-scoped on this change plus the fixed checklist.
