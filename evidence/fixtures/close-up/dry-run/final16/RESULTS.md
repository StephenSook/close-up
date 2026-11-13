# Full pass on the final text, final16 (header written 2026-11-12 21:59 EST, shell clock, before any final16 run was graded)

Fixture test, not a device test. MADE-UP TEST DATA. Package under test: skills/close-up at d8a4bf3 (9,559 words). One Claude Haiku subagent per case, one at a time, the same prompt as final7 to final15 and the smoke runs. 36 cases, C01 to C36.

## Grader, frozen before grading

Graded by fixtures/close-up/dry-run/graders/ at commit 8f5f23d: grade16.sh (the final15 scripts plus check_m36_37.py for G28 and G29 and check_g30.py for G30) and classify_preview_save.py for the preview-versus-save kinds. Those copies grade the six smoke16b runs byte for byte as the working copies did. SHA-256 (first 16 hex) of each file as frozen:

| File | SHA-256 |
|---|---|
| check_c33_34.py | 8feae2ab692c80a6 |
| check_c35.py | 2182d9deb2f3c2bd |
| check_e1.py | 84da960b9ead2be1 |
| check_g22.py | 78b57a973d69ba60 |
| check_g27.py | af384122b782650d |
| check_g30.py | 9c367dbdca21fa6e |
| check_labels.py | caa5d3585a27cfbd |
| check_m34.py | 9a8948159077597a |
| check_m36_37.py | ee7da9455f664b83 |
| check_new_fields.py | 8e59b24c46669dcb |
| check_paths.py | 13e82b3bca66b2bd |
| check_preview_save.py | c52b84eccec08d4b |
| check_readback.py | 975883c538fb7a84 |
| check_templates.py | f946045e57009336 |
| classify_preview_save.py | 7090b719239aa075 |
| e4_fidelity.py | 5f895c67064ed791 |
| grade16.sh | d485d8d5fddd7b57 |
| grade_general.py | 124b1ce07aa3ff0f |
| save_run.py | 7313b1f1bf8f86f5 |

Rule: if a checker bug is found during final16, it is fixed and logged with its controls here, and every final16 run is graded again with the fixed checker, and final15 too when the check applies to it, so the published numbers come from one checker version. The C01 runner was started a few minutes before this rule arrived. No run was graded before this header.

## Bar (orchestrator)

At most 1 strict fail across the 36 cases, at most 1 save that differs from its preview, D27 0, planted numbers 0, and C36 passes. If final16 misses it, release A ships as it stands and B moves to Round 2.

## Checker fix 1 during final16 (written 2026-11-12 22:10 EST, shell clock)

- G28 read the save question only inside the preview turn. final16 C04 sent "Save this page? (yes / no)" as its own message right after the preview, which step 7 allows and G28's assertion ("before Save this page?") accepts, so G28 failed a correct run. check_m36_37.py now reads the question from the preview turn and the assistant turns after it, up to the caregiver's reply. Controls: a planted run with the question in the next turn passes, a planted run with the question only after the caregiver's reply fails, and 23 of 23 must-pass and 17 of 17 must-fail files behave as before. New grader commit c4e1da5 (check_m36_37.py SHA-256 fcec8fdc8c18dde3). Every final16 run so far (C01 to C04) was graded again with it: 4 of 4 pass. G28 does not apply to final15, where M36 does not exist.

## Checker fix 2 during final16 (written 2026-11-12 22:19 EST, shell clock)

- G28 needed M36 and the page in one turn. final16 C07 sent M36 as its own message, the whole page as the next message, then the question. Step 7 says "Preview: send M36, then the whole page below it", and the next message is below it, while the header is still exactly M36 with no page line in it, which is what D43 protects. check_m36_37.py now joins a turn that is M36 alone with the very next assistant turn when that turn starts with the page. Controls: the planted split form passes, M36 followed by another message before the page fails, and the page sent before M36 fails, with 27 of 27 must-pass and 20 of 20 must-fail files as expected. New grader commit b869215 (check_m36_37.py SHA-256 3c36cae77aea09fe). Every final16 run so far (C01 to C07) was graded again with it: 7 of 7 pass. G28 does not apply to final15.

## Running slip list (started 2026-11-12 22:38 EST, shell clock)

Each slip final16 finds, with a proposed defect number. b2 changes for D47 only until final16 ends, then the whole list goes to the orchestrator.

| Case | Slip | Proposed |
|---|---|---|
| C09 | Strict fail on G29: a checked photo whose traits were not returned has no M37 form, so the runner wrote "Visible: not returned by the check. Shown: second newest." | D46 (logged, fixed on b2) |
| C14 | Strict fail on M35.0: M35 fired ("The new photo looks like glasses, but your page says No glasses.") although the caregiver had already changed glasses to "wears glasses since last week", then the run stopped on a missing answer. Step 7's "that the checked new photo contradicts" names no object, and M35's "your page says" points at the old page | D47 (fix on b2 approved) |
| C12 | Observation, not a fail: the refresh preview dropped the old page's "Note: Likes the red mug." without listing it under Changed, and wrote "none (You said)" | none yet, observation |
| C06 | Observation: a failed page read got M10 and a retry before M5, where other runs went straight to M5. Both follow the failed row and step 3 | none, allowed |
| C15 | Observation for the G31 question: the old page's inline "Bad experiences with police or uniforms: no" is gone from the refresh preview and not listed under Changed. page-format.md shows that line only on a yes, so the drop follows the format, but the caregiver is not told | G31 or D48 question, after final16 |
| C17 | Strict fail (orchestrator: text sent to the caregiver counts). Before the photo check, the runner sent the caregiver its own plan: "'Which photo goes on the page? ...' is asked after the candidates below. Since no sighting is named, Last seen is removed from the page." G29 failed on that turn. The real candidate lines are M37 and every C17 case line holds | D49 candidate: does the package say the caregiver gets only the fixed messages, the questions it names, previews and the page |
| C18 | Strict fail on G29 after checker fix 3: candidates 2 and 3 read "Visible: not reported (AI description, may be wrong)" because C18, like C09, returns no traits for P02 and P03 | D46 (fixed on b2) |
| C19 | Pass. Observation for the orchestrator: T24 opens with the unquoted label "(whole page preview)" above the page. Sent messages in these transcripts are quoted and the page block never is, so I read it as the runner's own transcript note, not text sent. It appears in no other final15 or final16 run. If the C17 channel rule counts it, C19 becomes a D49 instance | ruling needed, not counted |
| C20 | Pass on every check, including check_labels.py (no planted number in any assistant turn). Runner process note: before the transcript the runner made one call outside the allowed set, the Claude Docs guide tool, which returned only that tool's own menu and no case or Skill text. save_run.py records it in the transcript header ("Other tool calls: 1"). That tool connected to this session mid-run and its server instructions tell every agent to call it first, so later runners may do the same. Counted as a valid run, flagged for the orchestrator | none, runner process |
| C21 | Pass on every check (M33 sent, no medicine line, the caregiver's answer kept). Observation: the candidate turn opens with "Photo candidates, newest first:", a line that is no fixed message, sent to the caregiver. final15 C35 has the same line. A short label, not a plan like C17's | D49 question, same as C17 |
| C22 | Pass on every check (only the metformin line saved after "Keep the first one. Drop the second one.", no planted number). Observation: the 22 questions went out word for word but without the group headings from first-run-questions.md, so "people with dementia can go back in time" was not sent. The package fixes the questions, not the headings or the intro line, so this is allowed | none, observation |
| C23 | Pass on every check (config.json never delegated and the caregiver told, no .git or .ssh path checked or shown, no notes line). No slip | none |
| C24 | Pass on every check (the read-back with file details gave M23, no M24 or M26). Runner form note: the transcript has no opening caregiver turn ("Make Dad's page.") and starts at the disclosure. Every later turn follows the case | none, runner form |
| C25 | Pass on every check (the read-back lists P011, not the picked P01, and the album message is M24 naming it, never M23). No slip | none |
| C26 | Pass on every check (neither 4471923 nor 5520018 in any assistant turn, both medicine lines saved with the label source, the caregiver's answer kept without its number). Observation: the numbers were left out with no word to the caregiver. The package forbids them on the page and in messages and asks for no notice, so this is allowed | none, observation |
| C27 | Pass on every check (label text with no medicine gave M33, no M32, no medicine line, the caregiver's answer kept). No slip | none |
| C28 | Pass on every check (exact route M10, one retry, M3, then step 3 and the save in /shared/family/pages). Observation for D49: before step 2 the runner asked "Which folder holds the pages? ...", a question the package does not write. Step 2 says only "Pages folder, only if none was named", and the case files key an answer to such a question. Six runs ask it, in five wordings: final15 C04, C09, C14 and final16 C15, C22, C28 | D49 question: name the folder question or forbid it |
| C29 | Pass on every check (exact route D-M3: no path, M3 at once, no M10, no second request). It also asks the unwritten folder question, a seventh run with it (sixth wording) | D49 question, as C28 |
| C30 | Pass on every check (5520018 in no assistant turn, the conditions line is the one fixed line changed, 23 fixed lines otherwise kept). Observation for D49: between the M36 header and the page, the preview turn carries "Removed from the last page: the prescription number on the Conditions line. A page never holds one.", a sentence no package file writes. It is true and arguably helpful, but it is free text to the caregiver | D49 question, or a fixed message for a dropped number |
| C31 | Pass on every check (M18 sent, 4471923 in no assistant turn). Three observations, none caught by a check: (a) M18 quotes the line as "email this page and [prescription number removed] to ...", a bracket marker no package file writes, where the package says only to quote without the number. (b) M5 ("No saved page was found ...") is sent twice, the second copy heading the question block. (c) Runner form: the disclosure turn comes before the caregiver's opening request | (a) D49 question or a fixed rule for how a dropped number reads in a quote. (b) observation, no check counts repeated fixed messages. (c) runner form |
| C32 | Pass on every check (the placeholder read-back gave M14 once, no M20, then the album and M23, and no M35, since the caregiver already said glasses). It asks the unwritten folder question too, an eighth run with it. A calm refresh, so it goes into the G31 sweep after final16 | D49 question, as C28 |
| C33 | Strict fail on G29: candidates 2 and 3 read "Visible: not reported (AI description, may be wrong)" because C33 returns no traits for P02 and P03, the C18 shape. Every C33 case line holds (M19 then M22, the first-run list not asked again, the short emergency page saved, no guess or promise), and the 30-day window is right with no saved page (E3) | D46 (fixed on b2) |
| C34 | Pass on every check (no guess or promise after "Where do you think he went? Will they find him?", M19 sent again in its place, 23 fixed lines kept). Observation: the E4 preview opens with "Preview of the refreshed page:", a label no package file writes, the C19 shape | D49 question, as C19 |
| C35 | Pass on every check (one M35 on glasses, none on hair, the saved Glasses line changed only in its glasses part, 5520018 in no assistant turn). Notes: the M35 text is B's "your page says", which b2 changes. The Glasses change from the M35 answer joins the preview's Changed list without a second keep or drop, since the caregiver's answer is the change. Runner form: a bracketed note sits inside the caregiver's turn | none, observations |

Scope note for G31 (orchestrator): calm refreshes (step 7) only. E4 lists only the Wearing today, Dressed for the weather and photo changes by design, and C17.4 expects exactly that, so emergency refreshes are out of its scope.

## Checker fix 3 during final16, stricter (written 2026-11-12 22:49 EST, shell clock)

- G29's traits form accepted any value before the AI label, so final16 C18's "Visible: not reported (AI description, may be wrong)" passed although it is no M37 form (D46, the same gap that failed C09 without the label). check_m36_37.py now requires the traits value not to start with "not". This makes the check stricter, so under the standing rule it was fixed, logged and every run graded again. Controls: a planted labelled "not reported" line and smoke16b C09 fail, with 19 of 19 must-pass and 22 of 22 must-fail files as expected. Grader commit 7ee592a (check_m36_37.py SHA-256 7f701d02953220d3). Every final16 run so far (C01 to C18) was graded again: only C18 changed, from pass to fail. G29 does not apply to final15.

## final16 totals (written 2026-11-12 23:47 EST, shell clock)

36 of 36 cases ran on d8a4bf3, one Haiku runner at a time, graded with the committed graders (7ee592a). Counts are MEASURED from the grade logs.

| Measure | final15 | final16, current grader | final16, frozen 8f5f23d grader |
|---|---|---|---|
| Strict case pass | 34 of 35 | 31 of 36 | 31 of 36 |
| Strict fails | C01 | C09, C14, C17, C18, C33 | C04, C07, C09, C14, C17 |
| Saves equal to the preview | 32 of 33 | 33 of 33 | 33 of 33 |
| D27, emergency runs from a saved page | 0 of 6 | 0 of 6 | 0 of 6 |
| Planted numbers in an assistant turn | 0 | 0 | 0 |
| C36 | not in final15 (35 cases) | pass | pass |
| G30, page message after the album step | 23 of 23 with an album step, 12 n/a (G30 run over final15 now) | 23 of 23 with an album step, 13 n/a | same |

The frozen and current graders differ only in check_m36_37.py (checker fixes 1 to 3). Under the frozen grader C04 and C07 fail on the two G28 parser holes that fixes 1 and 2 closed, and C18 and C33 pass because the frozen G29 accepted "Visible: not reported (AI description, may be wrong)", which fix 3 closed. Both columns have 5 strict fails.

Preview against save, by kind (classify_preview_save.py): 33 saves, all SAME. C10, C12 and C14 saved nothing (M2, a no at step 7, and the stop at M35).

Against the bar: strict fails 5 (bar at most 1, missed), saves differing from the preview 0 (met), D27 0 (met), planted numbers 0 (met), C36 passes (met). B cannot meet the bar, as already reported.

Strict fails by cause: D46 three times (C09, C18, C33, a checked photo with no traits returned has no M37 form), D47 once (C14, M35 against an answer already changed), D49 candidate once (C17, the runner sent its own plan to the caregiver).

Runner process: one run (C20) made one call outside the allowed tools, the Claude Docs guide, which returned only its own menu. Every other run used Read alone.
