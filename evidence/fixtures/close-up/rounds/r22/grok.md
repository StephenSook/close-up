CRITICAL
none found

HIGH
none found

MEDIUM
1. **SKILL.md** (E4) and **references/page-format.md** (both Wearing today lines). Quoted text: `the Wearing today line (the E1 answer, or the clothing the caregiver stated in E2 when naming a camera moment, added if missing)` and, on the short page, `Wearing today: {answer} (You said)`.

When E2 names no moment (no camera, empty list, camera with no `camera_id`, no events, or a no to "Is one of these them?"), this is determined: Wearing today is the E1 answer, and Last seen is removed. Last seen is also determined when a moment is named: the surgical clause sets it, and the short-page template includes it only in that case.

The yes that names a moment and states clothing is not determined. `or` accepts either the E1 answer or the E2 clothing, so a fuller E1 answer ("navy jacket, grey trousers") and a later sighting ("dark jacket") can each be dropped and the line still matches the sentence. The same bullet sends the no-page and unreadable-page path to the short emergency page, whose `Wearing today: {answer}` never points at that E1-or-E2 rule. On that page `{answer}` follows the E1 question, so the clothing stated while naming the moment is left off the first page police would get.

Smallest fix: in E4, write `set Wearing today to the clothing the caregiver stated in E2 when they named a camera moment and stated clothing, otherwise set it to the E1 answer, and add the line if it is missing`. Use that same value for `{answer}` on both Wearing today lines in `page-format.md`.

LOW
2. **references/testing.md**. Quoted text: `Later upgrades and fixes were tested in the five cases they touch, two of them new: 1 more defect found and fixed, then the four emergency cases passed on this final text.`

The Cases list still stops at C15. No C16 or C17 is defined, and C08 only expects a Wearing today line and a Last seen line from the moment named. A pass of "four emergency cases" does not record the no-moment outcomes (E1 kept, old Last seen removed) or which clothing wins when both answers exist, on a calm-time page or an earlier emergency page.

Smallest fix: add the two cases to the Cases list and state the expected Wearing today and Last seen for each E2 outcome on both page types.

TOTAL: 0 CRITICAL, 0 HIGH, 1 MEDIUM, 1 LOW
