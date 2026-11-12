# Testing

Tags: MEASURED (a command or count), PLANNED, NOT VERIFIED. Nothing here has run on a NAS yet.

## A three-minute check, no NAS needed

Unzip the package and run UGREEN's own checker from the Uliya Skill kit on the close-up folder. Expected: 0 errors, 0 warnings.

## Cases

- C01 "Make Dad's page." No saved page, 9 recent photos in the album Dad. Expected: M1, M4, the question list, M18 for a planted notes line, three candidates, M25, the preview, both read-backs, M20 and M23.
- C02 "Dad has new glasses." The C01 page, a newer Mom page in the same folder, one changed notes line with an apostrophe and a pipe, and three decoy photos. Expected: Dad's page only, one refresh question, the two planted changes and the new photo, no decoy shown, no raw apostrophe or pipe in a delegation.
- C03 No photo in 30 days. Expected: M6 and the three-option question, a 90-day search only after "Look back 90 days", and no wider search on the other two options.
- C04 The vision check cannot read the album items, and an album "Dad 2019" exists. Expected: only the album named exactly Dad, M9, and candidates labelled not checked.
- C05 No album, an empty photo folder. Expected: M7, the folder route on request, M8, the three-option question, no photo, no album.
- C06 "Refresh Dad's page." An unreadable old page, then a failed photo search. Expected: M5, M10, a page without a photo.
- C07 The expert cannot add the picked photo, then the caregiver cancels the retry. Expected: M15, M16 offering only the album, M17, then M20.
- C08 "Dad is missing." Two cameras, 10 events. Expected: M19 and M22 first, the page, clothing and camera questions before photos, no identity filter, M13, and Wearing today and Last seen from the moment the caregiver named.
- C09 "They are gone." No camera or page. Expected: M19, M22, who is missing, M4, the album question, clothing, the camera question and M11, photos, one short question, a short page.
- C10 Local model "not sure". Expected: M2 and no delegation.
- C11 A folder of six unsuitable photos. Expected: M6, never M8, then the three-option question.
- C12 "Refresh Mom's page." Expected: Mom's page only, M7 naming Dad's album without using it, nothing saved on "no".
- C13 to C15 Read-back problems: a different page, another album photo, a read-back failing twice. Expected: M14, M24 and M26 instead of M20 or M23, no write sent twice.
- C18 C09, but the empty camera list has no statement. Expected: M10.
- C16, C17 Emergency refreshes of a calm and an emergency page, with no sighting. Expected: Wearing today from E1, no Last seen line.

## States

| State | Case that reaches it |
|---|---|
| completed | C01 |
| failed | C06 |
| cancelled | C07 |
| waiting_user | C01 |
| waiting_approval | C01 |

## Three numbers

- By-hand baseline: minutes to build the same page by hand from the same test folders. PLANNED for the NAS day.
- Ceiling (MEASURED from the fixture answer key): 2 planted changes in C02, 3 decoy photos, 4 clear photos in 30 days in C01.
- Skill result on the device: NOT VERIFIED until the NAS day. On the fixture: both planted changes caught, no decoy shown (MEASURED).

## Fixture dry run (fixture test, not a device test)

A Claude Haiku model played the Uliya parent against written expert replies, mostly from a test world OpenAI Codex wrote without reading this package. Each case ran in one pass, all answers visible, so it tests whether a small model follows the steps, not whether it waits.

MEASURED. 30 defects found, 29 fixed. Final pass: 17 of 18 cases passed their case checks (one run misformatted its delegations), 16 of 16 saves matched the approved preview. Not removed: in 8 of 19 emergency runs from an older-format saved page, the page first shown differed from the saved one (2 of 3 in the final pass), once changing the saved page too.
