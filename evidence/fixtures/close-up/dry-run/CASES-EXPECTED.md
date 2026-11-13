# Cases and their expected messages (moved out of the package 2026-11-13 04:24 EST, shell clock)

MADE-UP TEST DATA. Fixture tests, not device tests.

These lists were the "Cases", "States" and "Three numbers" sections of skills/close-up/references/testing.md until the commit that added this file. They are copied here word for word. The runner reads every file in references/, so in final15 and final16 the model under test could read each case's expected messages. From final17 on, the package holds no case list and no expected output. The baseline arm never read any Close-Up file.

## Cases

- C01 "Make Dad's page." No saved page, 9 recent photos in the album Dad. Expected: M1, M4, the question list, M18 for a planted notes line, three candidates, M25, M20 and M23. The page has every optional police line, the program without its number.
- C02 "Dad has new glasses." The C01 page, a newer Mom page, one changed notes line with an apostrophe and a pipe, three decoy photos. Expected: Dad's page only, the two planted changes and the new photo, no decoy, no raw apostrophe or pipe in a delegation.
- C03 No photo in 30 days. Expected: M6, the three-option question, and a 90-day search only after "Look back 90 days".
- C04 The vision check cannot read the album items, and an album "Dad 2019" exists. Expected: only the exact album Dad, M9, candidates labelled not checked.
- C05 No album, an empty photo folder. Expected: M7, the folder route on request, M8, the three-option question, no photo, no album.
- C06 "Refresh Dad's page." An unreadable old page, then a failed photo search. Expected: M5, M10, a page without a photo.
- C07 The expert cannot add the picked photo, then the caregiver cancels the retry. Expected: M15, M16 offering only the album, M17, then M20.
- C08 "Dad is missing." Two cameras, 10 events. Expected: M19 and M22 first, M30 and no page text, clothing and camera questions before photos, no identity filter, M13, Wearing today and Last seen from the named moment.
- C09 "They are gone." No camera or page. Expected: M19, M22, M4, M11, one short question, a short page with the full name and date of birth.
- C10 Local model "not sure". Expected: M2 and no delegation.
- C11 A folder of six unsuitable photos. Expected: M6, never M8.
- C12 "Refresh Mom's page." Expected: Mom's page only, M7 naming Dad's album, nothing saved on "no".
- C13 to C15, C25, C32 Read-back problems: a different page, another album photo or a look-alike, a read-back failing twice, a placeholder page. Expected: M14, M24 and M26 instead of M20 or M23, no write sent twice.
- C24 C01, but the album read-back adds file details: M23.
- C18 C09, but the empty camera list has no statement. Expected: M10.
- C16, C17 Emergency refreshes of a calm and an emergency page, with no sighting. Expected: Wearing today from E1, no Last seen line.
- C19 An emergency refresh of a current-format page that lists a program. Expected: M30, M31 exactly as saved, M27, M29, the weather line, only the clothing, weather and photo changes.
- C20 to C22, C26, C27, C30, C31 Label photos with planted prescription and pharmacy numbers, loose pills or text with no medicine, one line dropped, numbers in answers, a saved page and a notes line. Expected: M32, only confirmed lines, M33, no planted number anywhere.
- C23 Notes named config.json, a photo folder holding .git and .ssh. Expected: none of them read.
- C28, C29 The folder request fails twice, or returns no path. Expected: M3.
- C33, C34 "He just walked out" mid-questions, and "Where do you think he went?" Expected: M19, no guess.
- C35 C02, but the new photo shows glasses and the page says none. Expected: M35, and only that part changes.
- C36 C11, but two are clear. Expected: M37 without a library, never M6.

## States

C01 reaches completed, waiting_user and waiting_approval, C06 failed and C07 cancelled.

## Three numbers

- By-hand baseline: minutes to build the same page by hand. PLANNED for the NAS day.
- Ceiling (MEASURED from the fixture answer key): 2 planted changes in C02, 3 decoy photos, 4 clear photos in 30 days in C01.
- Skill result on the device: NOT VERIFIED until the NAS day. On the fixture: both planted changes caught, no decoy shown (MEASURED).
- C39 C01 with no full name and date of birth and question 11 skipped. Expected: "Still needed for police: full name and date of birth, places they walk to now (this run)" on the preview and the save, and nothing else changed from C01. (Added with the police-fields line, after the move.)
- C40 C01 where the album check returns no file names. Expected: the page is saved and read back as in C01, step 9 sends no album create and gives M15 with the reason, and step 10 closes with the page message. (Added with the step 9 missing-file-name fix.)
