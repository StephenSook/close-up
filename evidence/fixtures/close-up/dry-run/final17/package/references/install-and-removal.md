# Install and removal

## Checked against

Uliya Skill kit 0.7.7, capability catalog 2.2.0 (2026-11-05), and UGREEN's FAQ for kit 0.7.6.

## Setup

1. Install the close-up folder as a custom Skill in Uliya. Installing changes no files.
2. Name the person's album in UGREEN Photos before the first run, so grouping has time to finish.
3. Pick an existing folder for pages, or use your personal folder. The Skill creates no folders.
4. Set Uliya to the local model. Each calm-time run asks you to confirm it.

## Actions each step relies on

The parent only delegates, and each expert picks its own actions. Expected catalog actions:

| Step | Expert | Actions | Effect |
|---|---|---|---|
| 2 | file-agent | file-workflow get-user-dir | read |
| 3 | file-agent | ug-filesystem ls, then ug-filesystem cat | read |
| 4 | document-agent | ug-document qa, with the caregiver's own request as the query | read |
| 4 | photo-agent | ug-photo vision-ocr on the label photos named | read |
| 5a | photo-agent | ug-photo figure-albums, ug-photo search-picture, ug-photo meta, ug-photo vision-vlm | read |
| 5b | file-agent, photo-agent | ug-filesystem find, ug-photo meta, ug-photo vision-vlm | read |
| 8 | knowledge-agent, file-agent | ug-knowledge save-text after approval, then, on the returned file, ug-filesystem cat | write, then read |
| 9 | photo-agent | ug-photo search-picture narrowed to the picked file name, then ug-photo create-album with its source-ref after approval, then ug-photo albums by the album name and ug-photo album-detail on the one exact match | write, then read |
| E2 | security-monitor-agent | ug-surveillance cameras, ug-surveillance event-timeline, ug-surveillance event-evidence | read |

Step 9 in catalog terms: create-album with the source-ref of a search-picture narrowed to the picked file name, never add-item, which the catalog reserves for picture IDs the user named. NOT VERIFIED, both NAS-day checks in [limits](limits.md): whether a folder file outside the photo library can be added (if not, nothing is created, M15 and M16 follow, the page stays saved), and whether album-detail lists photo items (its catalog summary does not promise it, and none listed gives M26).

Catalog 2.2.0 wording to check on the NAS day, each NOT VERIFIED. save-text takes a path only from the user, and ours is the folder in the approved preview, so an action that asks anyway is waiting_user. search-picture sets a start time only when the user's message holds the year, so step 5a also reads each date taken. vision-vlm takes a path the user gave, so a refusal is the check that cannot read them (M9). album-detail takes an album UUID that "must come from an album list or be explicitly provided by the user", so step 9 lists the albums by the album name first and reads the one exact match (none or more than one: M26). ug-document qa takes as its query "The user's original question, passed verbatim", so step 4 passes the caregiver's own request word for word and asks for the notes file read in full.

Never used: identity lookups, face lists, person-name or known and stranger filters, photo timelines, folder creation, moves and deletes.

## Removal

Removing the Skill leaves your saved pages and albums. Delete them in Files and UGREEN Photos if you want. The Skill changed nothing else.
