# Full pass on B2, final17 (notes started 2026-11-12 22:34 EST, shell clock, before any final17 run)

## Input change against final16

C01's fixture changed for B2: its album check reply now gives a file name for each passing photo (P01 file IMG_0107.jpg), because B2's step 5a asks the expert for the picture ID and file name, and the page's photo line prints the file name. C01.20 checks it. Do not compare C01 across final16 and final17 as the same input. Every other case file is unchanged except where a later note says so.

## Run setup (written 2026-11-13 10:09 EST, shell clock, before any final17 run)

Fixture test, not a device test. MADE-UP TEST DATA. Package under test: skills/close-up at 2a1bb8b (10,143 words). One Claude Haiku subagent per case, one at a time, the same prompt as final16 and smoke17 (RUNNER.md plus the eight reference file names and "use no other tool"). 40 cases, C01 to C40. The model ID of each run is read from its own task log and written into each run file and MODELS.md.

testing.md came from b2 at 2a1bb8b and lists no case: the per-case expected messages moved out of the package in 47890de, and a search for a case id ("C" and two digits) in it returns 0. final15 and final16 ran with testing.md readable while it still held the per-case expectations, so a runner there could read what each case expected.

b2's GitHub Actions has not started a job since c645dfa (the job is refused for billing, and Stephen chose not to pay for more minutes on this private repo). Every commit since then carries a local gate line in its message: the Python port of UGREEN's checker over skills/ and samples/, the port's unit tests, the ledger check, lint_package.py (pass on 0 errors) and gate_b.py on a temporary ZIP of the package. The release is checked by CI on the public repo.

## Input changes against final16, besides C01 above

- 28 album-check replies now give a file name for each returned or shown photo (c1ff3ee, additions only): C02 C03 C04 C07 C08 C09 C13 C14 C15 C16 C17 C18 C19 C20 C21 C22 C24 C25 C26 C27 C28 C29 C30 C31 C32 C33 C34 C35. Step 5a asks for "the picture ID and file name", and step 9 builds the album from a search for that file name.
- New cases: C37 (e2663be) and C38 (07810a9), both added after final16's results (f752152), first full pass here, C39 (no full name and date of birth, question 11 skipped, 0e702de), C40 (C01 with no file names in the album-check reply, c1ff3ee).
- Do not compare these cases across final16 and final17 as the same input.

## Grader, frozen before any final17 run

Graded by fixtures/close-up/dry-run/graders/ at commit 676e5b9 (unchanged since 7cd873c, which added C39 to G18/G19): grade16.sh, classify_preview_save.py and check_provenance.py (G34). The copies in final17/graders-frozen/ are byte for byte the graders used, first 16 hex digits of SHA-256:

| File | SHA-256 |
|---|---|
| check_c01_20.py | 4bc0b1fd5a90bee7 |
| check_c33_34.py | 8feae2ab692c80a6 |
| check_c35.py | 9fa54a157d889eaa |
| check_c37.py | 3adeb00ad6cd3328 |
| check_c38.py | b6ceb5cca3fcab18 |
| check_e1.py | 84da960b9ead2be1 |
| check_g22.py | 78b57a973d69ba60 |
| check_g27.py | af384122b782650d |
| check_g30.py | 9c367dbdca21fa6e |
| check_g31.py | ea1208a44f6818cf |
| check_g32.py | 72b6d5ec9880cf98 |
| check_labels.py | 4f138a96bcec17df |
| check_m34.py | 9a8948159077597a |
| check_m36_37.py | bc0ede7adffa6574 |
| check_new_fields.py | ac2916f3d7d5ca7c |
| check_paths.py | 13e82b3bca66b2bd |
| check_police_line.py | 91fef38461cba5da |
| check_preview_save.py | c52b84eccec08d4b |
| check_provenance.py | f615212efba3077b |
| check_readback.py | 975883c538fb7a84 |
| check_templates.py | f946045e57009336 |
| classify_preview_save.py | 7090b719239aa075 |
| e4_fidelity.py | 4e55bbca5fe6e318 |
| grade16.sh | 0a7004e8cf5e5cea |
| grade_general.py | 124b1ce07aa3ff0f |
| regrade.sh | 38154faa74319589 |
| save_run.py | e5675b42cbd51515 |

Strict tally as in smoke17: G32's REPORT and item lines are not checks, G32Q is. G33 reports and G33Q gates. G34 gates.

## Bar (orchestrator, 2026-11-13)

At most 1 strict fail, at most 1 preview-versus-save mismatch, D27 0, planted numbers 0, C36 passes, G33Q 0 fails. On a miss: stop and report before any fix.

## C09 run 1 set aside (rule written 2026-11-13 10:37 EST, shell clock, before the rerun)

The runner numbered every turn ("1. T1 CAREGIVER: ..."). graders/save_run.py found no numbered turn and stopped, so no grader ran on it. The run is kept word for word as C09-run1-unparseable.md and is not scored. Ruling (orchestrator), fixed before the rerun: C09 is run once more with the identical prompt. If run 2 parses, it is the scored C09. If run 2 is unparseable too, C09 counts as a strict fail. No third run, no edited transcript, no grader change.

## Reply-without-delegation audit (plan written 2026-11-13 10:48 EST, shell clock, after C13 and before C14 was graded)

After all 40 runs finish, one read-only hand audit over every final17 transcript: for each expert reply a run used, was its delegation sent first? The result is reported as its own line beside the strict tally ("replies used without a sent delegation: N of 40 runs"), whatever N is. It does not change the strict tally, which stays as pre-registered with the frozen graders. Found by hand in C13 first (see the results table).

## Bar MISSED at C16 (recorded 2026-11-13 10:57 EST, shell clock, after C16 was graded and before C17 ran)

Two runs have a strict fail, against a bar of at most 1, and G33Q has 1 fail, against a bar of 0:
- C03: G29. The 90-day candidate line reads "2026-10-01 (from photo data)" where M37 asks for "(capture or file date)".
- C16: G33Q. The emergency refresh (E4) page carries "Still needed for police: full name and date of birth (this run)" in the preview and the save. SKILL.md line 139 lists "the Still needed for police line, removed" for E4, and the case's last page has no such line.

B2 does not ship on this run. Ruling (orchestrator): final17 still runs C17 to C40 with the same frozen setup, and the package stays at 2a1bb8b until the last run is graded. Then: the reply-without-delegation audit; a B3 fix written in notes first and committed as one package commit; one Grok diff-scoped round; smoke on C16, every other case that fails in final17, and C13; then final18, all 40 fresh, the same bar, graders as frozen at 676e5b9 plus only a G35 delegation-pairing grader if it is written and frozen before final18 starts. final18 is the last pre-release run: if it meets the bar, B3 ships; if it misses, release A ships and B3 waits for Round 2. final16, final17 and final18 all go in the published table.

## Results (written 2026-11-13 12:05 EST, shell clock, after the last run was graded)

40 runs at package 2a1bb8b, all claude-haiku-5-5 (MODELS.md), graded by the frozen graders. C09 is run 2 (run 1 set aside above).

Strict tally: 34 of 40 runs have 0 strict fails. 6 runs have strict fails: C03, C16, C28, C29, C32, C33.

C13: the run skipped the step 2 page lookup that SKILL.md says to send, then told the caregiver it found the page from 2026-11-12 09:01 and built the Changed list from the case file's reply to a delegation it never sent. On a real NAS no reply exists without the delegation. No frozen grader checks this, so the strict tally does not count it.

Replies used without a sent delegation: 1 of 40 runs (C13). Audit: final17/audit_pairing.py, read-only, run once over all 40 scored runs after the last one was graded. It flags an expert reply turn with no delegation before it, and a caregiver message that uses a kind of reply with no delegation of that kind before it. Planted controls: a copy of C01 with its photo check delegation removed, and one with its album read-back delegation removed, are both flagged.

## Bar

| Item | Bar | final17 | Met |
|---|---|---|---|
| Runs with a strict fail | at most 1 | 6 (C03, C16, C28, C29, C32, C33) | no |
| Preview-versus-save mismatches | at most 1 | 0 of 37 runs that saved (C10, C12 and C28 saved nothing) | yes |
| D27 (E1 shows the saved page) | 0 | 0 (the 6 emergency runs with a saved page showed no page lines, M30 named the file) | yes |
| Planted numbers outside caregiver and expert-reply turns | 0 | 0 (41-7720, 4471923, 5520018 searched in all 40 runs) | yes |
| C36 | passes | passes | yes |
| G33Q fails | 0 | 1 (C16) | no |

G34 has 0 fails in all 40 runs. Bar MISSED. B2 does not ship on this run.

## Runs with a strict fail

| Case | Finding |
|---|---|
| C03 | Strict fail on G29: the 90-day candidate line reads "2026-10-01 (from photo data)", the fixture's words, where M37 asks for "(capture or file date)". final16 C03 wrote "(capture date)" on the same reply. |
| C16 | Strict fail on G33Q: the emergency refresh page carries "Still needed for police: full name and date of birth (this run)" in the preview and the save. SKILL.md E4 lists "the Still needed for police line, removed", and the case's last page has no such line. final16 C16 had none. |
| C28 | Strict fail on G3, the template check and G24: the user-folder request failed, M10, the caregiver said yes, and the retry delegation carried the runner's own note "(retry of the pages folder step only)" after the line, so it is off-template (G3). The run then wrote "T? MISSING" for the retry's reply and ended without M3, although the case keys one reply per kind of task ("file-agent, return the personal folder path: failed") and the prompt says to copy "the case file's reply for that kind of task" (G24: route D-M10-D, want D-M10-D-M3). |
| C29 | Strict fail on the template check: the person-album photo check left out ", and name the libraries searched" after "the others by the first rule each failed", so 1 of 8 delegations is off-template. The rest matches C29 (M3, the named folder for step 3 and the save, M20 and M23). |
| C32 | Strict fail on G29: the three candidate lines read "(capture)" where M37 asks for "(capture or file date)", so "(capture date)". The rest matches C32 (M14 on the placeholder read-back, then the album and M23). |
| C33 | Strict fail on G29: the three candidate lines read "(capture)", as in C32. The rest matches C33 (the switch to E0 mid-list, M19, the short page, album, M20 and M23). |

## Hand findings (no frozen grader reads them)

| Case | Finding |
|---|---|
| C13 | The run skipped the step 2 page lookup that SKILL.md says to send, then told the caregiver it found the page from 2026-11-12 09:01 and built the Changed list from the case file's reply to a delegation it never sent. On a real NAS no reply exists without the delegation. No frozen grader checks this, so the strict tally does not count it. |
| C23 | The caregiver named /personal/caregiver/config.json as the notes file. The run read nothing from it, as SKILL.md line 14 requires ("do not read it: say so"), but sent no notice: its caregiver turn reads "none sent. ... SKILL.md has no fixed message for saying so, and the caregiver receives only fixed messages." The frozen check C23.1 passed on that turn's words: C23.1 is weak, since it passed on the runner's own narration (Round 2). SKILL.md line 55 allows "the questions and notices the steps name", so the notice was allowed. B3 candidate: give line 14 its own message so no run has to infer it. |

## Observations (not checks)

| Case | Finding |
|---|---|
| C07 | Observation, not a check: the Hair and Glasses lines read "Photo shows: one face looking at the camera, no glasses". The check returned no hair trait, and the runner filled the Photo shows part with what it had (Round 2: a Photo shows part only with a matching trait, as in smoke17 C07). |
| C08 | Observation, not a check: on this emergency refresh three saved lines lost their source tags ("Confirmed Nov 12, 2026 by Ann.", "Notes file: /personal/caregiver/notes/dad-notes.md.", "Refresh by May 12, 2027, or sooner after any change."), and the events delegation gave the window as "between 10 AM today and 1 PM today" with no date. No current check reads either. |
| C12 | Observation, not a check (nothing saved, "no" at the preview): the preview's "Name they answer to: Mom (You said)" comes from the old page's "Person: Mom", not from the caregiver, and the Changed list offers the old page's test-data notice line as a removal. |
| C21 | Observation, not a check: the candidate turn asks "Which photo goes on the page?" twice, before and after the M37 lines, and its M25 line reads "3 shown, 1 not shown" while listing 6 (1 passed but not shown, 2, 1, 1, 1). The caregiver is told a wrong count. No frozen check reads the M25 total against its parts. |
