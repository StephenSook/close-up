The missing-now rule still has two readings after a page save has been dispatched, so those moments do not have one route. Before any save is dispatched, the route is E0. The 90-day question is only in that earlier stretch, so it does not stay up. Step 0 fires only when the caregiver says the person is missing now. Both album routes have a catalog-legal create. A search cannot pass the read-back as M23, but a correct folder album also cannot.

1. **HIGH.** `close-up/SKILL.md`. "Otherwise send M19 and M22, then finish this run, with no E1 to E4." Also: "It is not done until you approve." And: "gets M15, then M16 and one retry. A no, a second such answer or a cancel that wrote nothing gets M17, then the step 8 page message." And E4: "On yes, run step 8, then step 9 only if a new photo was picked, then step 10."

   "Finish this run" is not defined anywhere in the package. "No save was sent" is not tied to dispatch, and M34 says the save is not done until approval. While the save waits for approval, after it completes, during the album, and during an emergency run's own E4 save, one reading is: send M19 and M22 and stop. That drops the write rule, the read-back, and step 10, so the caregiver never hears M20, M14, or M26, and a search album never gets M24. The other reading is: keep the calm run. That leaves them on M10 (the save retry) or M16 (the album retry) while the person is missing. M16 matters: the page message is sent only after they answer it, and on the success path step 10 sends it only after the album create. "With no E1 to E4" while the run is already in E4 can also be read as aborting the step 8 to step 10 work E4 just started. The 90-day question does not have this problem: it is asked only after M6 or M8, which is before any save, so that message takes E0 and the question is dropped.

   Smallest fix: "If the page-save delegation has not been dispatched, go to E0. If it has, even while approval is open or after it fails, send M19 and M22 without waiting, keep that same delegation, follow the write rule and steps 8 to 10, and send the step 8 page message before any album question. Do not start E0 to E4 again."

2. **MEDIUM.** `close-up/SKILL.md`. "even mid-step, go to E0 if no save was sent." Against: "An expert's: the platform asks and resumes it. Run no later step." The kit says wait and resume the same delegation, and do not start a parallel replacement.

   During an expert's `waiting_user`, those are two routes. The caregiver's "he is missing" can be taken as the expert's answer. The parent is also told to start E0, which is a new delegation, while the table says to run no later step. Nothing says to send M19 before that expert returns. The same clash hits the album create's `waiting_user` after a save was dispatched: step 0 says finish the run, and the table says run no later step, so the read-back and M24 are not ordered.

   Smallest fix: add to step 0, "If an expert is in waiting_user, send M19 and M22 and let that same delegation finish. Apply the E0 or finish choice only after it reaches a terminal state. Do not dispatch another expert while it waits."

3. **MEDIUM.** `close-up/SKILL.md`. "Add them as items, or from a search that returns only them, never by a description." With: "{CHOSEN_PHOTOS} ... the picked photo item or path alone" and "M23 if it lists exactly {CHOSEN_PHOTOS}, M24 if it lists others". Catalog: add-item is "picture IDs the user named explicitly"; source-ref is "the resultRef returned by the previous search-picture". `limits.md`: "M24 only for a different photo".

   The album route is catalog-legal: add-item of the one returned picture id. The folder route is catalog-legal: search-picture narrowed with `dir` and `file-name-contains` taken from the path, then create-album `source-ref`, and create nothing if that search is not only that file. `search-picture` has no picture-id parameter. An extra photo in the read-back is "others", so it does not pass as M23. The hole is the success case. A folder create stores a library item, and {CHOSEN_PHOTOS} is still the file path. Nothing says a listed item equals that path, so a correct folder album fails "exactly {CHOSEN_PHOTOS}" and falls through to M24. That contradicts the limits line that M24 is only for a different photo.

   Smallest fix: "M23 when every listed photo is the chosen item, or the expert says it is the chosen path, and no other photo is listed. M24 when any listed photo is neither."

4. **LOW.** `close-up/references/testing.md`. "C05 ... Expected: M7, the folder route on request, M8, no photo, no album." Against `SKILL.md`: "After M8 or M6, in calm time only, ask once 'Look back 90 days, use another album or folder, or go on without a photo?'"

   C03 still expects that question after M6. C05 is the only M8 case, and the edit removed the question from it. A run that skips the question after an empty folder now passes C05.

   Smallest fix: add "the three-option question" back to C05 only.

CRITICAL: none found.

TOTAL: 1 HIGH, 2 MEDIUM, 1 LOW.
