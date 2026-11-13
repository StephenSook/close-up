1. **HIGH** — `close-up/SKILL.md`, step 0 and the `waiting_approval` row.

Quote: "Whenever the person is missing now, even mid-step, go to E0."

Also: "The approval belongs to that same delegation: never send it again, wait for its result."

And E4: "On yes, run step 8, then step 9 only if a new photo was picked, then step 10."

Step 0 now applies in the middle of step 8 or 9, including while that save or album create is in `waiting_approval`. The approval row says to wait on that same delegation and not send it again. Nothing says which rule wins, or what happens to the write. One reading leaves the delegation waiting, never reaches E0, and does not send M19 while the person is missing. The other reading goes to E0, stops watching the delegation, and never checks its terminal result (the kit requires that check; resume is not success). E1 can then start a file read while the write is still waiting, which is a parallel delegation during `waiting_approval`. On a later yes, E4 runs step 8 again and sends a second save. The first write can still be approved and land as a file with no read-back, so neither M20 nor M14 is chosen for it.

Smallest fix: add to step 0, "If the save or the album create is already sent, send M19 and M22, leave that delegation waiting, and do not send another save or create until it returns; then do its read-back before E1."

2. **MEDIUM** — `close-up/SKILL.md`, steps 7 and 8.

Quote: "Preview the page, folder, file name hint, album name and the approvals to come."

And: "compare its returned text, not its date, line by line with {PAGE_TEXT}, the page as previewed, never with the text sent."

And: "Any other text, even a placeholder, M14."

Step 7 defines the preview as the page plus the folder, the file name hint, the album name, and the approvals. Step 8 tells the parent to compare the file with "the page as previewed." The file from the read-back is only the page body. A line-by-line compare against that whole preview treats the folder, file name, album name, and approval lines as extra text. The new rule then sends M14 for a save that matches the approved page. `{PAGE_TEXT}` is defined as "the approved page," and the old wording named that. "As previewed" points back at the five-part preview.

This does not conflict with the write rule. That rule matches a listed page to `{PAGE_TEXT}`, the approved page. "The text sent" is the one-line delegation (line breaks written as `\n`, or a placeholder). The write rule never compares against that string.

Smallest fix: replace "the page as previewed" with "the approved page body `{PAGE_TEXT}` alone: the lines of the page, after the character replacements, with its line breaks. Leave the folder, file name hint, album name, and approval lines out of the compare."

**Checked, no defect:**

- Step 10's "the one step 9 picked" still sends M23, M24, and M26. Step 9 still picks M23 for an exact `{CHOSEN_PHOTOS}` list, M24 for other photos, and M26 when the list has no photo items or the read-back fails twice (the create had already completed, so "created" is true). An album that was never created still gets M15, M16, M17, or M26 from the write rule, which is outside step 10's gate, as before.
- Removing "Label dates taken or file date." leaves the photo-date labels in place: step 6 still says "date and whether it is the capture or file date," and the photo line still says "(Photo taken {date})" or "(file date {date})." Page modified dates in M30 and the step 3 report are not capture-or-file dates.
- "Never guess where they went or say they will be found" does not block M29, M19, M27, the E2 questions, or the Last seen line. M29 quotes Found before lines; it does not invent a place or say the person will be found. E1 still says to send M29 when that line exists.
- `testing.md` and `limits.md` match the skill and the pass described with this diff. The M25 example adds up (3 shown, 2 not shown). C24's file details stay M23; a look-alike stays in the M24 group. The states sentence matches the old mapping. The results paragraph says the 31-case numbers are from before these four fixes. Limits now says medicines are the caregiver's words or label lines they confirmed, which is step 4 and the page format, and the phone-album sentence is only a NOT VERIFIED claim.

**Checklist (whole package):** delegate lines are one line, single-quoted, and aimed at the five allowed experts. Message ids used in `SKILL.md` exist; M1 plus M22 is one complete message. Workflow `{VALUE}`s are defined and set before use. The five terminal and waiting states are covered, except the step 0 conflict in finding 1. Each write waits and is sent once, except that same conflict. E0 to E4 connects, with no dead end on its own. Page lines name a source. Banned numbers and credential files stay out.

**CRITICAL:** none found.
**LOW:** none found.

TOTAL: 0 CRITICAL, 1 HIGH, 1 MEDIUM, 0 LOW
