# Limits

SOURCED means read on a page. NOT VERIFIED names the check that would close it.

## Untested behaviour and its fallback

| Behaviour | Check on the NAS | Fallback |
|---|---|---|
| Album search returns items the vision check can read, newest first | one album search | M9 and the newest, or the folder route on request |
| The exact chosen photo can be added to a new album | one album creation | no album, and why (M15) |
| Album read-back lists its photos | one read-back | M26 when it lists none, M24 only for a different photo |
| The expert saves each \n in the page as a line break | one save, then read | a page that reads back on one line or with \n signs is different (M14) |
| save-text's file name, cleaned and with a time stamp added, still starts with "Close-Up page" and the person's name, so step 3 and E1 find it | one save, then one folder list | step 3 and E1 find no page and ask their questions again, and the file stays where the read-back named it |
| A shared family folder appears in the album search | two accounts | the footer names the libraries reported |
| A camera snapshot is a NAS file or a link | one snapshot | shown as returned, never passed to the vision check, never on the page |
| The file read returns a page word for word, and the folder list gives names with dates | one read | the expert reads each file's date. |
| The notes content read returns every line word for word | one read | without every line, the page gives no line numbers |
| Uliya shows a returned photo in the chat | one pick | the caregiver opens it in UGREEN Photos, or in Files for a folder, before picking |
| Event times are NAS local time | one events call | each event shows its own time |
| The camera list returns names beside identifiers | one list | the events request is not sent without an identifier from the list |
| The OCR read returns label text word for word (NOT VERIFIED: stability and error codes unknown in the catalog) | one label photo | only lines the caregiver confirms reach the page |

## Unsupported

- Sharing the album: no catalog action shares one. The owner shares it from UGREEN Photos.
- Opening the page on a phone: no catalog action does it, so print the page.
- Uliya runs in the NAS PC client and web browser (SOURCED, UGREEN article 850). Phone chat access to a custom Skill is NOT VERIFIED, so make the page in calm time.

## What this Skill is not

Not a tracker, an alert or a way to find anyone. It does not contact police or any registry, recognise faces on cameras, name anyone, or look for medical records (it reads only the notes file and label photos the caregiver names). It never identifies a pill by its look. It runs only when the caregiver asks.

## Privacy

- Reads, writes and the cloud model statement: SKILL.md, "What Close-Up can read and write". UGREEN states a Skill cannot reach external APIs and that vision checks run on the NAS whichever model is chosen (SOURCED, UGREEN technical FAQ items 14 and 5).
- It covers only the libraries the signed-in account can open: its own personal folder and shared folders it was given, never another member's private folder.
- Emergency mode reads the saved page before any local-model answer. Accepted: seconds matter.

## Misuse and mistakes

- A page could be made about someone who did not agree. The Skill uses only an album the family already named, asks whether the person was told and had a say, records the answer, and has no step that sends or shares.
- The vision note can be wrong, so the caregiver picks the photo and confirms each change, and vision notes are labelled "AI description, may be wrong".
- A face-grouped person album falls in a category UGREEN's listing rules review more strictly. The Skill identifies no one. Conditions and medicines on the page are the caregiver's own words or label lines they confirmed.

