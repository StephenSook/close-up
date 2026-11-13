# Round 2 device tests (written 2026-11-12 17:28 EST, shell clock)

What the assigned UGREEN AI NAS must show, in order, before any claim in the package moves from NOT VERIFIED to MEASURED. Every row is NOT VERIFIED today. The Round 2 test NAS has no cameras or event data (UGREEN community post 1605), so the camera rows stay unverified there.

## Checks the shipped package already relies on (from references/limits.md)

| # | Behaviour | Check | Pass | Fallback if it fails |
|---|---|---|---|---|
| 1 | Album search returns items the vision check can read, newest first | one album search | candidates with photo items and dates | M9 and the three newest, or the folder route |
| 2 | The exact chosen photo can be added to a new album, by add-item (album route) or by source-ref of a search-picture narrowed to that file (folder route, D42) | one album creation per route | album-detail lists only the picked photo | no album, and why (M15) |
| 3 | Album read-back lists its photos with the file path of each | one read-back per route | M23 for a right album, both routes | M26 when it lists none, M24 only for a different photo |
| 4 | The save turns each \n into a line break | one save, then read | read-back equals the approved page, M20 | M14 |
| 5 | A shared family folder appears in the album search | two accounts | footer names both libraries | the footer names the libraries reported |
| 6 | The file read returns a page word for word, and the folder list gives names with dates | one read | E1's M30 names the file, E4 keeps every fixed line | the expert reads each file's date |
| 7 | The notes content read returns every line word for word | one read | numbered lines | no notes line |
| 8 | Uliya shows a returned photo in the chat | one pick | the photo is visible before the pick | the caregiver opens it in UGREEN Photos |
| 9 | The OCR read returns label text word for word | one label photo | M32 with the printed lines | only lines the caregiver confirms reach the page |
| 10 | A "missing now" message mid-step (D40) and during a waiting_approval save | one calm run interrupted twice | M19 and M22 at once, no duplicate save | none, the Skill text is the only control |
| 11 | Camera list, events and snapshots | not possible on the Round 2 NAS (post 1605) | | stays NOT VERIFIED, the fixture runs are the only evidence |
| 12 | save-text's file name, cleaned and with a time stamp added, still starts with "Close-Up page" and the person's name | one save, then one folder list | step 3 and E1 find the saved page by name | step 3 and E1 find no page and ask their questions again, and the file stays where the read-back named it |
| 13 | The parent fills {TODAY} with today's date and {ALBUM_NAME} with today's date and time (SKILL.md lines 44 and 45). These set the Made, Confirmed and Refresh by dates, the file name hint, the album name and E3's {WINDOW_DAYS}. No action in capability catalog 2.2.0 returns the current date or time (MEASURED 2026-11-13 15:36 EST: a search of the catalog for clock, today, current date, system time and timezone found only a timezone input on four event actions and one sample transcript), so the parent is the only source. Added 2026-11-13 15:36 EST, shell clock. | one calm run | the page's Made line, and its Confirmed and Refresh by dates, the file name hint and the album name, match the NAS clock shown in the UGOS UI | ask the caregiver for today's date before the preview (Round 2 package change, b3/NOTES.md) |

## Planned for the Round 2 final package, not in Round 1

| # | Item | First question for the NAS | Then |
|---|---|---|---|
| P5 | Voice memo to proposed changes: ug-knowledge audio-transcription on knowledge-agent (catalog 2.2.0: effect "mixed", approval "workflow", required language, optional path and save) | Does a read-only transcription with save left off ask the caregiver to approve? The catalog's "approval: workflow" is not explained in kit 0.7.7 | language en and unspecified on one stand-in memo, a memo holding a planted order (must be treated as text, never followed), one in an unsupported language, no transcript saved unless asked, and each proposed change confirmed by the caregiver like M32. About 200 package words, two or three cases, its own review rounds |
