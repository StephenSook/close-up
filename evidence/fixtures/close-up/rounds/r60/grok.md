CRITICAL: none found.

HIGH: none found.

1. **MEDIUM**. `close-up/references/messages.md`, `close-up/SKILL.md` step 5 and step 6. M37 does not have one complete form for a candidate the check did not read, and the unread variant does not combine into one determined line.

M37 is: `"{number}. {date} ({capture or file date}), {library} library. Visible: {traits} (AI description, may be wrong). Shown: {reason}." On the folder route, without ", {library} library". With no date, "date missing" replaces "{date} ({capture or file date})". When the check did not run, "Visible: not checked." replaces the Visible part.`

Step 6 sends that for every candidate: `then M37 for each candidate. Then M25 for the rest (when the check did not run, M9 replaces M25).` Both photo checks end the unread branch with `If the check cannot read them, say so and return the 3 newest.` The pass branch is the one that returns the date, whether it is the capture or file date, the library (album route), what is visible, and why it is shown. The unread branch does not.

The folder-route deletion and the `date missing` replacement commute. Folder plus no date plus unread becomes `{number}. date missing.` plus the Visible sentence plus `Shown: {reason}.` Album plus unread keeps `, {library} library` and `Shown: {reason}.` `{library}` and `{reason}` are not in that return, and `{date}` is not asked for either, so `date missing` can be applied to a photo whose date was simply not returned. `{reason}` has nowhere to come from: "why it is shown" is a pass-check field, and the unread branch only says to "say so" once. Step 6 no longer defines these slots. It only says to send M37.

`Visible: not checked.` also names no exact span. Replacing `Visible: {traits} (AI description, may be wrong)` and keeping the template period yields `Visible: not checked..` The date variant, by contrast, quotes the span it replaces.

C04 requires the unread album case to come out `candidates labelled not checked.` As written, that line still needs a library and a reason the failure return does not supply.

Smallest fix: quote the unread replacement as the exact tail `Visible: {traits} (AI description, may be wrong). Shown: {reason}.` replaced by `Visible: not checked.` In both step 5 failure sentences, change `return the 3 newest` to return each of those three with its date or that the date is missing, whether that date is the capture or file date, and, on the album route, its library.

2. **LOW**. `close-up/references/testing.md`. The C11/C36 line does not state what each case tests.

`- C11, C36 A folder of six photos, none or two of them clear. Expected: M6, never M8, or M37 without a library.`

C11 is none clear: M6, and not M8. C36 is two clear on the folder route: M37 without a library, and not M6. The shared `or` also accepts M6 as C36's expected result and M37 as C11's.

Smallest fix: `C11: a folder of six photos, none clear. Expected: M6, never M8. C36: a folder of six photos, two clear. Expected: M37 without a library, never M6 or M8.`

TOTAL: CRITICAL 0, HIGH 0, MEDIUM 1, LOW 1
