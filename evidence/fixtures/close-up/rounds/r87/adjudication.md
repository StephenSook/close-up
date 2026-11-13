# Round 87 adjudication (Grok, diff-scoped)

Diff-scoped round on rounds 85 and 86's changes since Grok's round 85 (d6590d4 to 6845af0). Grok reported 0 CRITICAL, 1 HIGH, 1 MEDIUM and 0 LOW.

| # | Finding | Verdict | Change |
|---|---|---|---|
| 1 | HIGH: "leave them out and list each as now removed" could add Changed rows, with no old value, for emergency-only lines a calm last page never had, against "Never a guess" | Adopted | Step 7: "leave out each one the last page had and list it as now removed, never asked to keep or drop." 33dd958 |
| 2 | MEDIUM: the emergency-last-page rule sat inside the refresh bullet, which starts from the last page, so the short page's Made line and closing line could stay | Adopted | Its own step 7 bullet: "A last page made in an emergency: build the full page from the first-run answers instead of from that page, then compare as above." 1233f32 |

The three self-grade musts (notes query, album from a search narrowed to the picked file, read-back through an album list) were committed while this round ran, and join the next diff-scoped round with these two changes.

Not clean: the next round is Codex, diff-scoped on these changes and the musts.
