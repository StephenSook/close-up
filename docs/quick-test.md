# Quick test on a UGREEN AI NAS (about 15 minutes)

For a UGREEN tester with an AI NAS. It uses made-up notes and photos of one consenting adult. Nothing below has run on a real NAS yet. It says what should happen if the package works as written. Things you type are in code style. Words in double quotes are the package's own fixed messages.

## Set up (about 5 minutes)

1. Install the `close-up` folder from the ZIP as a custom Skill in Uliya. Installing changes no files.
2. In UGREEN Photos, make a person album for one consenting adult, for example `Ray`, with 8 to 12 photos taken in the last 30 days. Make three of the newest ones decoys: one with sunglasses, one group photo, and one photo of a printed photo or a screen.
3. Pick an existing folder for the pages, or use your personal folder. Close-Up creates no folders.
4. In that folder, save a notes file `Ray notes.txt` with two made-up lines: `Walks to the corner store most mornings` and `Rx 0000-1234`.
5. Set Uliya to the local model.

## Run 1: a first page

Type `Make Ray's page.`

You should see:
- "This page is about a vulnerable person.", a line about where Uliya processes, then "Is the local model on? (yes / not sure)".
- If you named no pages folder, Close-Up uses your personal folder and asks only if it can't find it. Then "No saved page was found in".
- One list of questions: "Answer these in one reply. You can skip any question." For the album question, answer `Ray`. For the notes question, answer with the full path of `Ray notes.txt` in your pages folder.
- Up to three photos, newest first, each with what is visible and why it was shown, then a count of the rest by the first rule each one failed. None of the three decoys should be among them, unless the check could not read the photos, in which case it says so and shows the three newest.
- A preview of the whole page, then one question: "Save this page and create the album? (yes / no)". Uliya then asks for its own approval before each write.
- After the save is read back: "Your page is saved as", with the file name.
- If the album step works on your NAS, an album holding only the photo you picked, then "To show it to relatives, share it from UGREEN Photos yourself."
- If you skipped the full name and date of birth question, the page ends with a "Still needed for police:" line naming it. If you answered everything and picked a photo, there is no such line.

You should not see:
- A save or an album before your yes.
- `0000-1234` anywhere on the page or in the album name.
- Names from face recognition, or known or stranger labels.
- A photo chosen for you.

## Run 2: a refresh

Add two new photos to the album, change the first line of the notes file, and type `Update Ray's page.`

You should see:
- After the local-model question, "Found the page for Ray from", then questions only about what changed.
- A new dated page that lists each change you confirmed. The first page is still in the folder.

## Run 3: missing now

Type `Ray is missing.`

You should see, before anything else:
- "Call the police now, before you start looking: your local emergency number (911 in the US)."
- A line about where Uliya processes.
- "Your saved page from", with the file to open in Files and print or show to the police.
- "What are they wearing today, with shoes and a coat, and are they dressed for the weather?"
- "Is there a camera that may show which way they went? (yes / no)". UGREEN says the Round 2 test NAS has no cameras, so on yes it should say there are none and go on to the page.

You should not see:
- Any message before the call-police line.
- A camera snapshot on the page or in the album.

## Not verified yet

The NAS behaviours the package relies on are listed, with a fallback for each, in [ROUND2-DEVICE-TESTS.md](../evidence/fixtures/close-up/ROUND2-DEVICE-TESTS.md). Until a NAS run, every one of them is NOT VERIFIED.
