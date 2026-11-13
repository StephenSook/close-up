# Round 85 adjudication (Grok, whole package)

The one whole-package round after diff-scoped rounds 82 to 84, on the package at d6590d4. Grok reported 0 CRITICAL, 4 HIGH, 4 MEDIUM and 1 LOW. Each was checked against the package and earlier rounds. Five are adopted, one commit each, and four declined.

| # | Finding | Verdict | Change |
|---|---|---|---|
| 1 | HIGH: in E3, "Then E4" follows only the nothing-found sentence, so after a pick from E3 a small model could fall through step 6 to step 7 | Adopted | E3: "Then step 6, newest first, where "keep" leaves the page photo in place, then E4." e18e061 |
| 2 | HIGH: a calm refresh starts from the last page, so it could carry Wearing today, Dressed for the weather and Last seen from an emergency, and keep a page made in an emergency on the short template | Adopted | Step 7: "A calm page never carries the emergency-only lines (Wearing today, Dressed for the weather, Last seen): leave them out and list each as now removed. A last page made in an emergency becomes a full page from the first-run answers." 9b23ef7 |
| 3 | HIGH: a 90-day or other-source re-run that finds nothing again has no next step, and the question is asked once | Adopted | Step 5: "If the re-run finds nothing again, go to step 7 with no new photo." 5e599fc |
| 4 | HIGH: the notes and label delegates carry no credential skip, and "say so" has no fixed message | Declined | The parent never sends such a file: "Never searched or read, even inside a named folder: credential and system files ... If a named notes file or photo is one of these, do not read it: say so." C23 (a notes file named config.json) passed with no delegation and the caregiver told. Notices the steps name were settled in rounds 66 and 71. |
| 5 | MEDIUM: E2 said what to do on yes only | Adopted | E2: "On no, go to E3." 138c465 |
| 6 | MEDIUM: the do-not-send rule for a path holding a pipe, angle bracket, backtick, double hyphen, ampersand or dollar sign can block a real returned path | Declined | By design: a path the parent cannot pass safely inside the single-quoted delegate line is not passed, and the caregiver is asked for another. Escaping inside the instruction is not something UGREEN's checker or the experts are shown to handle, so it stays NOT VERIFIED rather than assumed. |
| 7 | MEDIUM: the calm Photos looked at line has no form when the vision check did not run (M9) | Adopted | page-format.md: "When the check did not run (M9), Photos looked at also reads "none checked this run"." af6f58b |
| 8 | MEDIUM: E2 collects only "wearing then", so the "wear now" sentence has no input | Declined | That is the rule as written: only clothing the caregiver says they wear now replaces the E1 answer (C08's caregiver says "He has a gray hat on now"), and "wearing then" goes to Last seen. |
| 9 | LOW: "say so" for a camera with no camera_id has no fixed message | Declined | Notices the steps name, settled in rounds 66 and 71. |

Not clean: the loop goes back to diff-scoped rounds on these five changes, Codex first, then one whole-package round.
