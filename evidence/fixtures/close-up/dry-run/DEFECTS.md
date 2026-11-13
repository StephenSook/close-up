# Dry-run defects (fixture test, not a device test)

| # | Case | Step | What SKILL.md said | What broke | Fix | Re-run |
|---|---|---|---|---|---|---|
| D1 | C01 | 7, page footer | page-format.md: "Photo source: {album or folder}" | The page said "Photo source: Dad" and "from Dad", so a refresh or E3 cannot tell the album route from the folder route | page-format.md now asks for "person album {name}" or "photo folder {path}" in both the photo line and the footer | C02 and C08 read this line |
| D2 | C01 | rules block | "Messages: three short lines and one question at most" | The first-run list, the candidate list and the preview cannot fit three lines, so the rule contradicts steps 4, 6 and 7 | the rule now exempts those three lists, and G6 is read the same way | all cases |
| D3 | C02 | 4 and 7 | "If a notes file is named, read it and quote changed lines with their source" | Changed against what: the last page held no notes lines, so the walk-time change (16:00 to 15:30) was never found | step 4 now puts the notes lines that help searchers on the first page, quoted with line numbers, and on a refresh compares them with the file; page-format.md gains a "From your notes" line (no asked-not-followed lines, a pipe written as a slash) | C02 run 2 |
| D4 | C02 | 7 | footer "Confirmed {TODAY} by {caregiver name}", with the name asked only in the first-run list | The refresh path never says where the confirmer's name comes from, so the run stopped | step 7: on a refresh the confirmer is the name on the last page unless the caregiver says otherwise, shown in the preview | C02 run 2 |
| D5 | C03 | 8 and 9, completion table | "waiting_approval: Say what waits and where it goes. Report success only after completed." | After the caregiver approved, the parent sent the same save and the same album delegation a second time (T32, T40). On a device a second send could make a second file or album | the waiting_approval row now says the approval belongs to that same delegation: never send it again, wait for its result. Assertion G12 added | C04 on, and the final re-run of every case |
| D6 | C04 | 6 | "Then M25 for the rest" | With the vision check not run there are no counts by failed rule, so the parent could not send M25 and stopped before the pick | step 6: when the check did not run, M9 replaces M25 and each candidate says not checked | C04 run 2 |
| D7 | C04 | 7, M20 | "Save this page and create the album?"; M20 "Print it, with the photo" | With no photo picked, the question offered an album that would not be made and M20 mentioned a photo that did not exist | step 7 asks "Save this page? (yes / no)" when no new photo was picked; M20 says "with the photo if there is one" | C05, C06, C11 |
| D8 | C06 | completion table, failed | "Stop steps that need it. Offer one retry." | After "no" to the retry of a failed photo search, the parent ended the whole run, though the page does not need the photo (the minimum path says so) | the failed row now says: if the caregiver says no, stop only the steps that need it; a failed photo step means the page goes on without a photo | C06 run 2 |
| D9 | C07 | completion table, cancelled | "Send M17 with what already exists." | After the album retry was cancelled the run ended with M17 only, so the caregiver whose page was saved never got M20 (print it, refresh by) | the cancelled row now sends M20 after M17 when the page was saved | final re-run of C07 |
| D10 | C08 | 6 | the pick question "(1, 2, 3 or none)", with "keep" described only as an accepted answer | In emergency mode the caregiver was never told "keep" was possible | the question now adds "or keep the photo from your page" on a refresh or in emergency | C08, C09 in the final re-run |
| D11 | C09 | E1 | "show it at once. Then ask What are they wearing today? No page: M4, then ask for the person album or photo folder." | With no saved page the parent took the "No page" branch and never asked about clothing | E1: "No page: M4, then ask for the person album or photo folder. Either way, ask What are they wearing today?" | C09 run 2 |
| D12 | C09 | E4 | "run steps 7 and 8" | In an emergency with no saved page, step 7 had no answers, so the parent sent the full 19-question first-run list at the worst moment | E4: with no saved page, one short question for the name they answer to and who police should call; the page holds only those, the photo, what they wear today and "has dementia"; the full list waits for calm time | C09 run 2 |
| D13 | C09 | 6 | "adding or keep the photo from your page on a refresh or in emergency" | In an emergency with no saved page, "keep" was offered with no page photo to keep | the question adds "or keep the photo from your page" only when the last page has a photo | final re-run |
| D14 | C12 | 7 | "On a refresh, the confirmer is the name on the last page unless the caregiver says otherwise." | The old page named no one, so the footer read "Confirmed ... by not given" | step 7 adds "If the last page names no one, ask." | final re-run |
| D15 | C08 final re-run | E4 | "On yes, run steps 7 and 8" (step 7 asks keep or drop per changed line, then the preview question) | In emergency mode the caregiver answered three yes or no questions in a row (save a refreshed page, keep the changes, save and create the album) | E4: the preview's yes also confirms the clothing line and the new photo, no separate keep or drop | C08 run after D15 and D16 |
| D16 | C09 final re-run | E4 | "the page holds only those, the photo, what they wear today and has dementia" | The short emergency page carried no line saying who confirmed it and when | E4 adds the confirmed line to the short page | C09 run after D15 and D16 |

## Round 4 re-run (after review rounds 3 and 4)

| ID | Case | What failed | Fix |
|---|---|---|---|
| D17 | C01 | A first page showed "First page." without the "Changed since your last page" label, because page-format.md did not say the label stays | page-format.md now says the block reads "Changed since your last page: First page" |
| D18 | C02 | After Dad's page was found, step 3 still asked whether a Mom page was this person, because the round 3 lookup always lists every page | step 3 asks only when no page for the person came back (regression from round 3 fix 1) |
| D19 | C02 | The photo date label had two forms (source line versus template), so runs differed | the template now uses the source line form |
| D20 | C03 | The photo line read "file name not returned" because the template asked for a file name and the album route returns a photo item | the template takes the photo item or file name returned |
| D21 | C03 | A quoted pipe became the word "slash" (round 4 fix 20 said "in words") | "replace a pipe with the / sign" |
| D22 | C05 | M7 had no wording for zero albums found, so the run stopped rather than invent names | M7 reads "Albums found: {names, or none}" |
| D23 | C05 | A calm-time preview showed a Wearing today line that the save left out, so the saved page differed from the approved one | the whole line is conditional: {only in an emergency: Wearing today: ...} |
| D24 | C06 | The parent asked for approval itself before sending the save, so the caregiver approved twice | the waiting_approval row: only after an expert returns it, and send the write at once after the preview yes |
| D25 | C08 | E4 swapped in a new photo but kept the old photo's "Photo shows: no glasses", so the page described the wrong photo | E4 replaces every Photo shows part from the new photo |
| D26 | C15 | The failed row says send M10 and offer a retry, while step 8 retries a read-back on its own | the failed row names the read-back exception too |

## Final pass on the final text (package at 729a6e1)

No new package defects: 15 cases, 0 package defects, 15 of 15 passed their own assertions. Details in final/RESULTS.md.

## Re-runs after review rounds 20 and 21 (package at 86e55ce, then 6677772)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D27 | C16 (run 1, final4/C16-run1.md) | E1 said only "show it at once", and the parent showed a rewritten page: a made-up footer ("none in this step", "not yet checked this run") and four saved lines dropped | E1 says "show it at once, as saved" |

Fix 1 ("show it at once, as saved", 6677772) did not hold: D27 recurred in C16 (final4/C16-run2.md). Fix 2 ("show the returned text at once, word for word", 2e903b3) held in C16, C17 and C08, checked by a script (G16). Final runs at 2e903b3: 4 cases, 0 package defects, 4 of 4 passed. Details in final4/RESULTS.md.

## Re-runs after Grok round 22 (package at e462227)

D27 recurred once in C08 (final5/C08.md): at E1 the parent brought the older-format fixture page's photo line up to the current template. It is kept as a residual and not fixed further: 3 of 11 emergency runs with a saved page, 1 of 6 since the word-for-word wording, all on the older-format fixture page, and every run saved the right page. testing.md states it. Details in final5/RESULTS.md.

## Full pass on the kit 0.7.7 text (package at d6299d0, then the D28 fix)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D28 | C04, C05 (final6) | page-format.md said only that a skipped answer reads "not given", so the parent saved "What upsets or scares them: not given" with no source label (C03 wrote "(You said)") | a skipped answer reads "not given (You said)"; C03 to C05 run again on the fixed text |

## Final pass on the final text (package at e2ebf58, after Codex round 35 returned no findings)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D29 | C05 (final7) | The template's changed line always shows the dated form "Changed since your last page ({LAST_PAGE_DATE}):", and the first-page rule sits in the paragraph below it, so the parent saved "Changed since your last page (Nov 12, 2026): First page (this run)" for a page with no earlier page | Not fixed, residual: 1 of 23 saved first pages across every pass. The fix would make the template line itself conditional in page-format.md |

D27 recurred in C16 and C17 (final7). In C16 it reached the saved page for the first time: the E1 display rewrote the older-format photo line, and the refresh kept the rewritten line on "keep". Since the word-for-word wording: 12 emergency runs with a saved page, 6 G16 failures, all on the older-format fixture pages, 1 of 12 with a changed saved line. Details in final7/RESULTS.md.

## Full pass on the final text (package at 5b68b27)

D29 is fixed in 01d959a (page-format.md: the dated changed block only if the last page was read, "First page (this run)" only with no last page). D30 is fixed in 5b68b27:

| ID | Case | Defect | Fix |
|---|---|---|---|
| D30 | C13, C14 (final8); C02 (final6, final7) | Step 7 compared the last page with "the new answers" only, and the photo is not an answer, so a refresh that picked a new photo left the photo change out of "Changed since your last page" in 4 of 12 such runs | Step 7 compares the last page "with the new answers and the picked photo" |

Measured in final9: 0 of 6 first pages dated, 4 of 4 refreshes with a new photo list the photo change, 17 of 18 cases passed (C14 failed on a one-run slip: its save changed one line from the approved preview). Totals over every run: 30 defects found, 29 fixed, D27 reduced and not removed. Details in final9/RESULTS.md.

## Full pass on the final text (package at ef325ef, after Codex round 39 returned no findings, written 2026-11-12 09:07 EST, shell clock)

No new package defect. 17 of 18 cases passed every case line. C12 failed G3 on a one-run slip (delegations not in the delegate line form). D29 0 of 6 first pages dated, D30 4 of 4 new-photo refreshes list the photo change, 16 of 16 saves equal the approved preview. D27 recurred in C08 and C16 (2 of 3), so 8 of 19 emergency runs with a saved page since the word-for-word wording (all 19 from the older-format fixture pages of C08, C16 and C17), 1 of 19 with a changed saved line. Both new failures touch the older-format "First page" line (n=2, cause not proven). Approvals to come left out of 3 of 12 calm previews. Totals over every run stay 30 found, 29 fixed, D27 reduced and not removed. Details in final10/RESULTS.md.

## Partial pass on the fields, labels and credential text (package at 644fe5f, stopped after C07; written 2026-11-12 12:24 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D31 | C01 (final12) | The hand line was saved as "Right-handed (You said)", dropping the "Right- or left-handed:" label, because the template label repeats the answer | The page label is "Dominant hand: {answer}". C19's saved page and the checker label follow |
| D32 | C06, C07 (final12) | Cases that answer questions 1 to 19 stalled at step 4 waiting for the new optional questions 20 to 22 ("T? MISSING"), while C03 to C05 treated them as skipped | first-run-questions.md: "An unanswered question counts as skipped." |

D27 is no longer a residual: E1 never retypes the page (51459c1), and 8 of 8 runs passed the new G16 (e1fix). Totals over every run: 32 found, 32 fixed once D31 and D32 are measured in final13.

## Full pass final13 (package at eeda669, 23 cases; written 2026-11-12 13:24 EST, shell clock)

Measured in final13 (see final13/RESULTS.md). D31: 5 of 5 saved pages that answer the hand question carry "Dominant hand: ...". D32: 0 of 23 runs stopped on an unanswered question. D27: 0 page lines shown in 4 of 4 emergency runs with a saved page, 0 of 12 with e1fix. No new package defect. 22 of 23 cases passed every case line (C15 failed G3 on a one-run note after a delegate line), and 21 of 21 saves equal the approved preview. Totals over every run: 32 found, 32 fixed.

## D33, found on the orchestrator's review of final13 (written 2026-11-12 13:30 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D33 | C07 (final13), and by script over the final passes, r4 and e1fix: 9 of 110 album create delegations in 7 runs (r4 C07, final C03, final4 C09, final6 C01, final7 C01 run 1, final8 C09, final13 C07) | The album create named the photo with its date, library and sometimes its description ("P02, taken 2026-11-06 (from photo data), shared library") instead of the item alone. The catalog's create-album takes add-item as picture IDs, so on a NAS this could fail the create or add the wrong items. The fixtures read back the bare item, so all 5 completed creates still got M23, and the defect was logged as a one-run slip in final13 instead of counted | The values row and step 6 define {CHOSEN_PHOTOS} as "the picked photo item or path alone, no date, library or description". New check G22 (check_g22.py) flags all 9 old item lists and passes the clean ones |

The final13 paragraph above ("No new package defect") was written before D33 was counted. Totals over every run: 33 found, 32 fixed until G22 passes on the reruns.

## D34, found by the new template check (written 2026-11-12 13:59 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D34 | final13 C03, C04, C13 and post44 C07 run1 (4 of 26 page read-backs in those two passes) | The page read-back delegation left out its conditional clause "(in the folder {PAGES_FOLDER} when it is a name, not a full path)" whenever the saved path was already full. The request still worked, but the parent was editing a delegate template, which the Skill forbids, and nothing caught it because G3 and G4 check only the line form and the characters | {PAGE_FILE} is now defined as a full path ("the full path of a page file an expert returned, {PAGES_FOLDER} put before a bare name"), so the template carries no conditional clause. M20 and M30 drop the now repeated "in {PAGES_FOLDER}". New check G23 (check_templates.py) compares every delegation with the SKILL.md templates |

Totals over every run: 34 found, 32 fixed until the reruns pass G22 and G23.

## D35, found in postd34 C26 (written 2026-11-12 14:10 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D35 | C26 (postd34), 1 of 34 runs in final13, post44 and postd34 | The page left out every banned number, but the preview's list of changes named them: "prescription number 5520018 left out ... transmitter number 41-7720 left out". That breaks C01.18 (41-7720 in no assistant text), because the package banned the numbers only "on the page" and the parent read "Show each change in the preview" as listing what it removed | page-format.md: "Never put ... number on the page or in a message." The change can still be named without its digits |

Totals over every run: 35 found, 32 fixed until the reruns pass G22, G23 and the C26 checks.

## D36 and D37, on the orchestrator's decisions after postd35 (written 2026-11-12 14:35 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D36 | many runs: final9 4 of 27 waiting_approval replies, final10 8 of 27, final13 6 of 35, postd35 7 of 13 (C26, C27, C29, C19, C20) | No message after an expert's waiting_approval, though the table row said "say what waits and where it goes". Free wording was followed unevenly and was logged as an observation for several passes | New fixed message M34 ("Waiting for your approval: {the page file in its folder, or the album in UGREEN Photos}. Nothing is written until you approve.") and the row reads "Only after an expert returns it: send M34 first." Check G26 |
| D37 | C19 (postd35), 1 of 13 emergency runs from a saved page | The E4 preview showed only the changed lines, so the caregiver approved a save without seeing the whole page, which contradicts the package's own claim that the caregiver approves the whole page. The preview sentence ("Preview it") sat after the short-page sentence, so for a refreshed page it had no clear object | E4: "Preview the whole page, refreshed or short, and ask ...". E1's ban is scoped: "never show or retype its text before the E4 preview". Check G25 |

Paid for under the 9,300 ceiling by shortening the Goal paragraph, which repeated the description, and the first-run header's restatement of the page format's "not given" rule. Totals over every run: 37 found, 32 fixed until the next full pass measures D33 to D37 on the final text.

## D38 and D39, from final14 (written 2026-11-12 16:28 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D38 | C19 (final14), 1 of about 200 save delegations across every saved pass | The save delegation's Text was a placeholder ("[the full approved page above, ... exactly as previewed]"), not the page. The read-back reply in the case file returns "exactly the text that was saved", and the run compared that with what it had sent, called it the same text and sent M20. On a NAS the caregiver would be told a placeholder file is their page. Two gaps: "its real value, unchanged" did not rule out a pointer to the value, and step 8 compared with "{PAGE_TEXT}, the approved page" without saying the comparison is against the preview and never against the text sent | Rules: "Fill every value with its real value, unchanged, never a summary or a pointer to it." Step 8: "compare its returned text, not its date, line by line with {PAGE_TEXT}, the page as previewed, never with the text sent" and "Any other text, even a placeholder, M14." New check G27 (the save's length within 10 percent of the preview's) and new case C32 (the saved file reads back as that placeholder: M14, never M20) |
| D39 | C13 and C16 (final14), final13 C15 | A delegate line that is not alone: a note before it (C16), a note after its closing quote (final13 C15), or no closing quote (C13). Each fails G3 and G23 though the command inside is right | Rules: the delegation "stays on one line, with nothing else on it." Measured by G3 and G23 in final15 |

Paid for under the 9,300 ceiling: step 10 no longer restates step 9's album messages, the rules drop "Label dates taken or file date" (step 6 and the page format already say it), the M25 example is shorter, testing.md's States table is one sentence, several case lines lose detail the fixtures keep, and limits.md drops a SOURCED line that the NOT VERIFIED sentence beside it already presumes. The same edit corrects limits.md's "Conditions and medicines on the page are the caregiver's own words", which label lines made untrue: "or label lines they confirmed". Totals over every run: 39 found, 32 fixed until final15 measures D33 to D39 on the final text.

## D40 and D41, from the orchestrator's research audit (written 2026-11-12 16:33 EST, shell clock)

Found by reading the package against another project's emergency rules, not by a run. Each gets a case so final15 measures it.

| ID | Case | Defect | Fix |
|---|---|---|---|
| D40 | none yet, C33 added | Step 0 ("If the person is missing now, go to E0.") sits at the start of the calm workflow, so a caregiver who says "he just walked out" while answering the first-run questions has no stated route to E0 | "0. Whenever the person is missing now, even mid-step, go to E0." Case C33 |
| D41 | none yet, C34 added | SKILL.md bars made-up expert results, but nothing bars Uliya's own words in missing-person mode, such as a guess of where they went or a promise they will be found | The Emergency line: "Never guess where they went or say they will be found." Case C34. The Skill tells Uliya this; nothing on the NAS enforces it |

Paid for by rewriting testing.md's results paragraph (it still gave final13's numbers) to final14's measured numbers in fewer words, and by shorter case lines. A third proposal, showing "not given" on the Full name and date of birth and Dressed for the weather lines, was not taken here: line 54 of page-format.md already makes those lines "only if answered" on purpose, G18 and G19 assert it, and changing it would change M31's condition and about 12 expected pages without a defect shown. Totals over every run: 41 found, 32 fixed until final15 measures D33 to D41 on the final text.

## D42, from a blind grade the orchestrator checked against catalog 2.2.0 (written 2026-11-12 17:06 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D42 | none, found by reading the catalog | The album create said "Add them as items, never by a search or a description." Catalog 2.2.0's create-album takes add-item ("A small set of picture IDs the user named explicitly ... Search results must use source-ref") or source-ref ("The resultRef returned by the previous search-picture ... After filtering, use the latest filtered resultRef"). The folder route hands the album a file path, not a picture ID, and the delegation forbade the one route a path has: a search-picture narrowed by folder and file name, then source-ref. On a NAS the folder-route album could have had no legal route | "Add them as items, or from a search that returns only them, never by a description." The expert keeps "If these exact photos cannot be added, create nothing and say why", and the album read-back still sends M24 for any album holding other photos. install-and-removal.md step 9 lists "add-item, or source-ref of a search-picture narrowed to them". Which route the NAS takes stays NOT VERIFIED, under the existing limits.md row "The exact chosen photo can be added to a new album" |

Round 45's call stands for the album route: the caregiver names the one photo, which is what add-item describes. This fix only stops forbidding the narrowed search. Paid for by dropping "(the page travels inside a delegation)" from page-format.md and two repeated "three-option question" entries from testing.md. Totals: 42 found, 32 fixed until final15 measures D33 to D42.


## Measured in final15 (written 2026-11-12 20:17 EST, shell clock)

final15 ran the full 35-case pass on 83d0581, the text that carries every fix through D42 (final15/RESULTS.md, tally.txt). Each open defect was measured by its own check: D33 by G22 (all 24 album creates name the item alone), D34 by G23 (every delegation equals its template, 35 of 35 runs), D35 by the planted-number check (0 of 35 runs put 41-7720, 4471923 or 5520018 in any assistant message or delegation), D36 by G26 (M34 after every waiting_approval), D37 by G25 (the emergency previews in C08, C16, C17 and C19 equal their saves, C16's one extra preview line being the runner's note after the closing quote, not a page line), D38 by G27 (33 of 33) and C32, D39 by G3 and G23 (0 of 257 delegate lines with a note), D40 by C33, D41 by C34 and every emergency run, D42 by G22 with the new wording. No new package defect.

Totals over every run: 42 found, 42 fixed.

Not counted as defects, as in earlier passes: one-run slips against rules the package already states. The C01 reruns on the same text (c01rerun/RESULTS.md) show two: a preview that leaves out the approvals to come (r2, C01.10, seen since final6) and candidate lines with the AI label moved into one header in other words (r3, C01.8). final15 C01's own miss, the changed line shown above the page, recurred 0 of 3. A planned change turns the preview header and the candidate line into fixed text, the pattern that fixed D36. If it lands, both slips are numbered then.


## D43 and D44, from the C01 reruns (written 2026-11-12 20:27 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D43 | c01rerun r2, and earlier final6 5 of 13 calm previews, final7 8 of 17, final8 C01, final10 3 of 12, final13 2 of 16 | The step 7 preview header was free wording ("Preview the page, folder, file name hint, album name and the approvals to come"), so the parent sometimes left out the approvals to come, and in final15 C01 it put a page line ("Changed since your last page") in the header instead of the page | M36, a fixed header with a page-only variant: "Preview. Folder: {PAGES_FOLDER}. File name hint: Close-Up page {PERSON} {TODAY}. Album: {ALBUM_NAME}, with the photo you picked. Approvals to come: the page save, then the album." Step 7: "Preview: send M36, then the whole page below it." No photo ID in the header. Check G28 |
| D44 | c01rerun r3 | The step 6 candidate line was described, not fixed, so the parent moved the "AI description, may be wrong" label into one header in other words and left it off each line | M37, a fixed candidate line: "{number}. {date} ({capture or file date}), {library} library. Visible: {traits} (AI description, may be wrong). Shown: {reason}." No library on the folder route, "Visible: not checked." when the check did not run. No photo ID in the line. Check G29 |

Both follow the pattern that fixed D36: the parent fills values into fixed text instead of composing the line. Paid for under the 9,470 ceiling (orchestrator's go): step 6 loses its own description of the line and the "not checked" clause M37 now carries. Totals over every run: 44 found, 42 fixed until final16 measures D43 and D44 on the final text.


## D45, from the smoke runs on 198fcbf (written 2026-11-12 22:14 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D45 | smoke16 C01 and C02 on 198fcbf, 2 of 2 runs that created an album (0 of 26 such runs on the text before M36 and M37), and before that final10 C18 and final14 C21 | The page message M20 went out right after the page read-back, before the album create, although step 10 closes with the page message and then the album message. Step 8 said only "The result picks one closing message for step 10" | Step 8: "The result picks one closing message, sent only at step 10, after step 9: ..." (d8a4bf3), ceiling 9,560 on the orchestrator's go. Check G30 (check_g30.py). Measured: smoke16fix 3 of 3 runs and smoke16b 4 of 4 runs that created an album send M20 after the album step. Codex round 65 clean on the diff |

Totals over every run: 45 found. D43 to D45 are fixed in the package (9835212, 3c50a67, 5a64cd4, 992350e, c688532, 198fcbf, d8a4bf3) and pass the smoke runs (smoke16b 6 of 6). final16 measures them on all 36 cases, after which the totals read 45 found, 45 fixed if they hold.


## D46, from final16 C09 (written 2026-11-12 22:27 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D46 | final16 C09 (strict fail on G29), smoke16b C09 and final15 C09 (the same gap in other words) | M37 has no form for a photo that passed the check but came back with no traits. C09's fixture passes P02 and P03 with only "shown because second newest", and the parent improvised: "Visible: not returned by the check. Shown: second newest." (final16), "Visible: not reported (AI description, may be wrong)" (smoke16b). Neither is fixed text, and the second puts the AI label on a non-description | Not fixed in d8a4bf3. Planned: an M37 variant, 'With no traits returned, "Visible: not returned." replaces "Visible: {traits} (AI description, may be wrong)".', with its own review round and a C09 rerun |

## D47, from final16 C14 (written 2026-11-12 22:39 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D47 | final16 C14 (strict fail on M35.0), with C14 0 M35 in final13, final14 and final15 | Step 7 sent M35 "for each of hair colour, hair length, glasses and hearing aid that the checked new photo contradicts", which names no object, and M35 said "but your page says {answer}". The runner compared the photo with the old page ("No glasses") although the caregiver had already changed glasses this run, sent M35, and stopped on a missing answer | On b2 (55ba951): "where the checked new photo contradicts the caregiver's current answer", and M35 "The new photo looks like {trait}, but the new page says {answer}. What is true now?". Checked by check_c35.py (C35 fires with the new text, C14's path sends none) |

## D48, from final16 C12 and C15 and final15 C15 (written 2026-11-13 00:06 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D48 | final16 C15 and final15 C15 (the old page's inline "Bad experiences with police or uniforms: no" left the saved page with no Changed item), final16 C12 (the old-format "Note: Likes the red mug." left the preview with no Changed item) | Step 7 says "Compare {LAST_PAGE_TEXT} with the new answers and the new photo line yourself and list each difference", which a runner read as answers and photo only: a last-page line the new page leaves out, because the page format no longer holds it or the runner dropped it, went unlisted, so the police page changed without the caregiver seeing it | Step 7 adds: "A last-page line the new page drops or changes is a difference too, "now removed" when dropped." Check: G31 (check_g31.py, gates): fails final15 C15, final16 C12 and C15 and two planted drops, and passes the other calm refreshes and C15 with a Changed item naming the line. Ceiling 9,710 to 9,727. Waits for the B2 smoke list (C12, C15) and final17 |

## D49, from final16 C17 and the G32 counts over final15 and final16 (written 2026-11-13 00:09 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D49 | final16: 21 of 36 runs sent text no package file writes (G32, MEASURED), and final15 25 of 35. Mostly an intro of the runner's own before the first-run list (29 pieces in final16), then the pages-folder question no step writes (5 runs in each final, 8 in all with 6 wordings), then narration such as C30's "Removed from the last page: the prescription number on the Conditions line. A page never holds one." | Nothing told the runner that the caregiver gets only designed text, the question list had no fixed intro, and the required input listed "a pages folder (default: the account folder)" beside what to ask for | messages.md adds M38 "Answer these in one reply. You can skip any question.", step 4 sends it before the list, the required input reads "a pages folder (step 2 finds it, never asked)", and the rules add: "The caregiver gets only the fixed messages, the questions the steps name, those lists and the preview. Add nothing of your own." The folder is asked only in step 2's failure branch, by M3. Check: G32 (check_g32.py, reported, not a gate): on the b2 package a planted M38 intro counts as designed and a runner's own intro does not, and on d8a4bf3 the same M38 line is undesigned. Ceiling 9,727 to 9,766. Codex round 66 amended two parts: the rule now reads "the questions and notices the steps name", and the required input now reads "a pages folder (step 2 finds it, asked only with M3)", since M3 asks in step 2's failure branch and in step 3. Waits for final17's G32 line |

## D50, from C31 in final14, final15 and final16 (written 2026-11-13 00:11 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D50 | C31 in final14 ("Rx# [number withheld]"), final15 ("Rx# [number removed]") and final16 ("[prescription number removed]"), 3 of 3 runs. Each kept 4471923 out of M18 but put its own marker in the number's place inside the quoted notes line | The page format said to keep the number out and that this outranks word-for-word rules, but not what goes in its place, so each runner wrote a marker no package file writes | page-format.md now reads "It outranks word-for-word rules: leave out the number and the word naming it, with nothing in their place." Check: check_labels.py for C31 now also requires M18 to quote the rest of the line ("email this page" and "page-drop@example.invalid") with no bracket, no "Rx#" and none of removed, withheld, redacted or number. It fails C31 in final14, final15 and final16 and a planted quote that loses the rest of the line, passes two planted quotes with nothing in the number's place, and leaves C20 to C30 in final16 as they were. Ceiling 9,766 to 9,780. Waits for final17 |

## D51, found by reading (written 2026-11-13 01:31 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D51 | No run yet. Found by reading: a dementia caregiver's photos include care moments, and nothing kept a clear-face photo of one from passing the check, being shown as a candidate and having its traits described | The vision check's pass rule named only face, framing and print or screen, so a private care moment could pass, be shown and be described: a dignity failure | Steps 5a and 5b add to the pass rule: "not a private care moment (undressed, bathing, on a toilet or in medical care). Count that one only as a private care moment, never described." C38 (new) puts one such photo among the album check's results, with the expert even adding "him in the bath". Check: check_c38.py (not named or described, counted once, the rule sent), proven on planted copies both ways. In the unread branch no photo is read or described, so the rule cannot apply there. NOT VERIFIED until the NAS day: whether the vision model sorts such photos reliably |

## D52, catalog contract notes found by reading the catalog (written 2026-11-13 01:32 EST, shell clock)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D52 | No run. Three lines in catalog 2.2.0, each read by the orchestrator and checked here: save-text's path, "Pass it only when the user gives a real NAS directory ... otherwise the Action asks for a directory" (line 5231); search-picture's start time, "fill only when the user's original message also contains the same four-digit year or YYYY-MM-DD" (line 6790); vision-vlm's path, "The absolute image path the user explicitly gave in the message (single)" (line 7574) | The package did not say what happens if an expert holds to that wording, and step 5a, unlike 5b, did not read each photo's date taken, so a search without a start time could let older photos in | install-and-removal.md adds a short note marking all three NOT VERIFIED until the NAS day and saying what Close-Up does in each case: the approved preview names the folder and an action that asks is waiting_user, 5a reads each date taken, and a vision refusal is the unread branch (M9). Step 5a now reads "From its photos taken in the last {WINDOW_DAYS} days (read the date taken of each and leave out older ones), newest first". Doc and wording only, no new case |

Totals over every run: 52 found. D43 to D45 are fixed in the package and pass the smoke runs. D46 to D52 are fixed on b2 and wait for final17.

## Measured in final17 and final18 (written 2026-11-13 15:47 EST, shell clock)

final17 ran all 40 cases on 2a1bb8b (B2, which carries D46 to D52) and final18 ran all 40 on 486fdfb (B3, which adds D53 and D54). Counts are MEASURED by regrading each run's saved transcripts with its own frozen graders and its own package (regrade.sh, the same totals as final17/RESULTS.md and final18/RESULTS.md, run errors 0). The C27 rerun in final18 is not in these counts. D43 to D45 were last measured on the smoke runs, so they are measured here too.

| ID | Check | final17 (2a1bb8b) | final18 (486fdfb) | Status |
|---|---|---|---|---|
| D43 | G28 (check_m36_37.py) | 29 of 29 previews pass | 29 of 29 previews pass | fixed |
| D44 | G29 (check_m36_37.py) | 80 of 87 candidate lines pass. The 7 fails, in C03, C32 and C33, are the date words that became D54, not the AI label | 87 of 87 pass | fixed |
| D45 | G30 (check_g30.py) | 24 of 24 album runs send the page message after the album step | 23 of 24. C01 sent M20 before the album step and again after it, a one-run slip against step 8 and step 10, which both state the order (listed below) | fixed, one recurrence in final18 |
| D46 | G29 on C09 | "Visible: not returned." on both no-traits photos, G29 pass | the same | fixed |
| D47 | check_c35.py on C14 and C35 | C14 sends no M35, C35 sends one M35 on glasses, pass | the same | fixed |
| D48 | G31 (check_g31.py) | 7 of 7 runs it applies to pass | 6 of 7. C12 failed on a kept removal, a different gap, numbered D55 below | fixed |
| D49 | G32Q gates, G32 reports | G32Q 0 fails. Runs with any undesigned text: 4 of 40 (C06, C08, C23, C30), against 21 of 36 in final16 | G32Q 0 fails. 6 of 40 | fixed (G32 is reported, not a gate) |
| D50 | check_labels.py on C31 | M18 quotes the rest of the line with nothing in the number's place, pass | the same | fixed |
| D51 | check_c38.py on C38 | pass | pass | fixed in the package, NOT VERIFIED on a NAS |
| D52 | no run check (doc and wording). Step 5a's template is checked by G23 | text in the package | text in the package, 40 of 40 runs on template | fixed in the package, NOT VERIFIED on a NAS |

## D53 and D54, the two B3 package edits (written with the section above)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D53 | final17 C16 (strict fail on G33Q) | The emergency refresh page carried "Still needed for police" although E4 removes it. The template line in page-format.md that builds it began "{only if any of the five is empty:" and did not say calm page, so the rule was not where the line is built | page-format.md line 45 begins "{only on a calm page, and only if any of the five is empty:" (486fdfb). Measured in final18: G33Q 0 fails in 40 runs, C16 passes |
| D54 | final17 C03, C32 and C33 (strict fails on G29) | M37 wrote the date kind as "({capture or file date})", and runners filled it as "(from photo data)" or "(capture)" | M37 reads "{date} ({capture date or file date})" and says the brackets hold the words capture date or the words file date, never other words, and the date-missing sentence matches (486fdfb). Measured in final18: G29 87 of 87 candidate lines pass, C03, C32 and C33 pass |

## D55, from final18 C12 (written with the section above)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D55 | final18 C12 (strict fail on G31). final17 C12 passed on the same text | Step 7 lists a dropped last-page line as "now removed" and asks the caregiver to keep or drop each changed line, but does not say what keeping a removal does to the page. The caregiver said "keep", and the run kept the old Note line on the preview and wrote "Changed since your last page: none (You said)", which is no page-format form | Not fixed. Round 2: one line in step 7 saying a kept removal leaves the line off the page and lists it as now removed, with a C12 rerun and G31 |

## D56, found by reading, like D51 and D52 (written with the section above)

| ID | Case | Defect | Fix |
|---|---|---|---|
| D56 | No run. Found by reading | {TODAY} and {ALBUM_NAME} come only from the parent (SKILL.md lines 44 and 45) and set the Made, Confirmed and Refresh by dates, the file name hint, the album name and E3's {WINDOW_DAYS}. No action in capability catalog 2.2.0 returns the current date or time, and the package does not say what happens when the parent gives no date | Not fixed. Round 2: when the parent gives no date, ask the caregiver for today's date before the preview. Device check: ROUND2-DEVICE-TESTS.md row 13, NOT VERIFIED |

## One-run slips in final18 (not package defects, Round 2 items in b3/NOTES.md)

Each breaks a rule the package already states, so none is numbered, as in earlier passes.
- C01: M20 sent before the album step and again after it (G14, G30). Step 8 and step 10 both state the order.
- C15 (hand): an early Changed list with a placeholder line, and a reworded M26 with a runner note inside it. M26 is fixed text.
- C17 (hand, E4): the refresh dropped the last page's notes line without listing it. E4 says "change only" and the notes line is not on its list.
- C28: the runner wrote T? MISSING for the caregiver's yes after M10, although the case file's catch-all answer covers it. A runner slip against the fixture, not the package.

Totals over every run: 56 found, 54 fixed, 2 open for Round 2 (D55, D56). Fixed means the package carries the fix and its own check passes on the release run (final18), apart from one-run slips against rules the package already states, the rule earlier passes used. Under that rule D45 counts as fixed with one recurrence: final18 C01 sent M20 before the album step (G30 23 of 24 album runs). D51 and D52 are fixed in the package and stay NOT VERIFIED until a NAS run.
