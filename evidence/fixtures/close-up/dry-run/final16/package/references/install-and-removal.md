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
| 3 | file-agent | ug-filesystem ls, then the ug-filesystem file content read | read |
| 4 | document-agent | ug-document qa | read |
| 4 | photo-agent | ug-photo vision-ocr on the label photos named | read |
| 5a | photo-agent | ug-photo figure-albums, ug-photo search-picture, ug-photo meta, ug-photo vision-vlm | read |
| 5b | file-agent, photo-agent | ug-filesystem find, ug-photo meta, ug-photo vision-vlm | read |
| 8 | knowledge-agent, file-agent | ug-knowledge save-text after approval, then the ug-filesystem file content read of the returned file | write, then read |
| 9 | photo-agent | ug-photo create-album after approval (add-item, or source-ref of a search-picture narrowed to them), then ug-photo album-detail on the returned album | write, then read |
| E2 | security-monitor-agent | ug-surveillance cameras, ug-surveillance event-timeline, ug-surveillance event-evidence | read |

Never used: identity lookups, face lists, person-name or known and stranger filters, photo timelines, folder creation, moves and deletes.

## Removal

Removing the Skill leaves your saved pages and albums. Delete them in Files and UGREEN Photos if you want. The Skill changed nothing else.
