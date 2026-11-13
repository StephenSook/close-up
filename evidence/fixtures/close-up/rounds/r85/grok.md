CRITICAL: none found.

1. **HIGH.** `SKILL.md`, step E3 and step 6. Line number could not be verified: the paste has no line numbers, and the disk was not opened.
   Quote: "Then step 6, newest first, where "keep" leaves the page photo in place. Nothing found: M21 and keep the page photo when the page has one, otherwise M6 (M8 for an empty folder) and no photo, with no 90-day question. Then E4."
   Step 6 ends: "None or keep: step 9 does not run." The next numbered step is step 7: "Build the page from [page format](references/page-format.md)."
   E4 is the emergency builder: "the Still needed for police line, removed" and "List only the Wearing today, Dressed for the weather and photo changes", then "On yes, run step 8, then step 9 only if a new photo was picked". The calm template still has "{only if any of the five is empty: Still needed for police: ...}".
   "Then E4" comes after the nothing-found sentence. The success path is a jump to step 6, and step 6 points at step 9, not back to E4. A small parent that finishes step 6 continues at step 7 and can save the calm page, with "Still needed for police" on it, and never apply E4's shorter change list. The nothing-found branch does reach E4.
   Smallest fix: at the end of step 6, add "If this pick was started from E3, go to E4." Delete the calm fall-through for that call.

2. **HIGH.** `SKILL.md`, step 4 and step 7, against `references/page-format.md`. Line numbers could not be verified.
   Quote: "On a refresh, start from the last page and change only what this run changes."
   Quote: "Wearing today is not question 4."
   Quote: "{only in an emergency: Wearing today: {answer} (You said)}" and "{only in an emergency, and only if answered: Dressed for the weather: ...}".
   E4 puts those lines on a saved page, plus Last seen. The next calm run does not ask them again. "Change only what this run changes" leaves them in place, so a later calm page still says "Wearing today" for clothes from the emergency. The same refresh rule starts a short emergency page from the short template ("Make a full page in calm time. (this run)") after step 4 has collected the full first-run list, so those answers have no lines on that template.
   Smallest fix: one calm-refresh sentence: leave out Wearing today, Dressed for the weather, and Last seen, list each as "now removed", and if the last page is the short emergency page, build the full calm template from the first-run answers.

3. **HIGH.** `SKILL.md`, step 5 results. Line number could not be verified.
   Quote: "After M8 or M6, in calm time only, ask once "Look back 90 days, use another album or folder, or go on without a new photo?" (waiting_user), and re-run only the route chosen, or go to step 7 with no new photo. Widen to 90 days only on that option."
   "Go to step 7" is only the third answer. A 90-day re-run, or a re-run of the album or folder they name, that again ends in M6 or M8 has no next step. "Ask once" forbids a second question. Completed-empty is "A stated none gets its fixed sentence", which only sends M6 or M8 again. The page is never built.
   Smallest fix: add "If that re-run returns M6 or M8, or they give no name, go to step 7 with no new photo."

4. **HIGH.** `SKILL.md`, "What Close-Up can read and write" and step 4. Line numbers could not be verified.
   Quote: "Never searched or read, even inside a named folder: credential and system files (.env files, .git and .ssh folders, config.json, key and certificate files). If a named notes file or photo is one of these, do not read it: say so."
   Quote: "The caregiver gets only the fixed messages, the questions and notices the steps name, those lists and the preview. Add nothing of your own."
   The notes delegate says "Read the full content of the file {NOTES_FILE}, and only that file". The label delegate says "Read the printed text on each of these image files with OCR, one file at a time: {LABEL_PATHS}." Neither has a skip. The folder delegate does: "Skip .env files, .git and .ssh folders, config.json, and key and certificate files." No message id exists for the refusal, so "say so" is a sentence the fixed-message rule forbids. A parent that runs the step 4 delegates passes a named `.env`, `config.json`, or key file to document-agent or photo-agent.
   Smallest fix: add one message, for example "That file is a credential or system file. Name a different one.", and put the same skip on both step 4 delegates: if the named file is one of these, do not read it and send that message.

5. **MEDIUM.** `SKILL.md`, step E2. Line number could not be verified.
   Quote: "in missing-person mode, cameras only if asked and events and snapshots only from the camera picked."
   Quote: "E2. Ask "Is there a camera that may show which way they went? (yes / no)" (waiting_user). On yes, list the cameras the expert returned..."
   The two `security-monitor-agent` delegates sit in E2 with no "only after yes". There is no "On no, go to E3." A "no" can stall or still list every camera.
   Smallest fix: move both delegates under "On yes", and add "On no, go to E3."

6. **MEDIUM.** `SKILL.md`, delegation rules, against steps 3, 5b, 8, and 9. Line numbers could not be verified.
   Quote: "Fill every value with its real value, unchanged, never a summary or a pointer to it. If one is missing, do not send."
   Quote: "If a path or name holds a pipe, an angle bracket, a backtick, a double hyphen, an ampersand or a dollar sign, do not send: tell the caregiver and ask for another (waiting_user)."
   Step 3 must send `{PAGES_FOLDER}`. Step 5b must send `{PHOTO_FOLDER}` and then `{FOLDER_PATHS}`. Step 8 must send `{PAGE_FILE}`. Step 9 must send `{CHOSEN_PHOTOS}` when that value is a path. A real folder such as "Mum & Dad" is a value those steps require and this rule forbids. "Ask for another" cannot replace a path the expert just returned.
   Smallest fix: limit the do-not-send rule to names the caregiver typed (`{PERSON}`, album name, notes name). For a returned path, keep the real path and escape it inside the instruction.

7. **MEDIUM.** `references/page-format.md`, Photos looked at line, against `SKILL.md` step 5 and M9. Line numbers could not be verified.
   Quote: "Photos looked at: {checked} checked in {album or folder}, of {total} only if the expert gave a total."
   Quote: "Check not run: M9 at step 6, never M6." M9 says "The photo check could not read these photos, so it did not run."
   E4 has the missing calm sentence: "none checked this run" when no check ran. The calm line does not. Filling `{checked}` with the three newest makes the page say they were checked. An officer reading the page would treat the vision rules as done.
   Smallest fix: on the calm page, when M9 fired, set Photos looked at to "none checked this run".

8. **MEDIUM.** `SKILL.md`, step E2. Line number could not be verified.
   Quote: "Clothing the caregiver says they wear now replaces the E1 clothing answer, never the weather answer."
   Quote: "Is one of these them? If so, at what time, which way were they going, and what were they wearing then?"
   E2 never asks what they wear now. E1 already asked that. The only clothing words E2 collects are "wearing then", which the Last seen line prints "only if said". Treating those words as "wear now" replaces today's clothes with the earlier sighting. Leaving them unused means the replacement sentence has no input.
   Smallest fix: replace the E1 clothing answer only when the caregiver says the camera clothes are what the person is wearing now. Otherwise put those words only on Last seen.

9. **LOW.** `SKILL.md`, step E2. Line number could not be verified.
   Quote: "A camera with no camera_id cannot be checked: say so and go on without it."
   Quote: "The caregiver gets only the fixed messages... Add nothing of your own."
   M11 is "The camera list came back empty." It does not cover a camera that was listed with no `camera_id`. "Say so" has no message text. The run can continue, so this is not a dead end.
   Smallest fix: add a fixed line, for example "That camera has no identifier, so it was not checked."

Checklist items with no defect in the pasted text: delegate shape and targets, message ids and M1, value table order, the five terminal states on the global table, one approval and one send per write except the stated nothing-written retry, page-line sources, step 9 reaching one page message (M20, M14, or M26) plus at most one album message, photo line file name or path and `{CHOSEN_PHOTOS}` limited to id or path, M35 only on a contradicting checked photo, pages folder asked only with M3, private-care photos failing the check and counted only as "a private care moment", and "Still needed for police" limited to the five calm-page fields when E4 or the short template is actually used.

TOTAL: CRITICAL 0 (none found), HIGH 4, MEDIUM 4, LOW 1.
