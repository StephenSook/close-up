CRITICAL: none found.

1. **HIGH: The page-read delegation omits the credential-file exclusion.**

   [SKILL.md:67](skills/close-up/SKILL.md:67) instructs the expert to:

   > "read in full the newest one whose name is Close-Up page {PERSON} followed by a date"

   It neither restricts candidates to page-file extensions nor carries the prohibition from [SKILL.md:14](skills/close-up/SKILL.md:14):

   > "Never searched or read, even inside a named folder: credential and system files"

   A newest matching file named `Close-Up page Dad 2026-11-12.key` therefore satisfies the delegated selection rule. Selection and reading happen inside one delegation, before the parent can inspect the chosen path. The catalog describes the content-read action as "Read file content by path and optional byte range" with approval `"none"` ([catalog:2154](uliya-skill-kit/data/capability-catalog.json:2154), [2183](uliya-skill-kit/data/capability-catalog.json:2183)); it documents no credential exclusion.

   **Smallest fix:** Put the existing credential/system exclusions inside step 3's delegation, before selection or reading, and restrict page candidates to `.md`, `.markdown` or `.txt`.

2. **MEDIUM: M35 still lacks a defined binding to one atomic fact.**

   [messages.md:38](skills/close-up/references/messages.md:38) says:

   > "The new photo looks like {trait}, but your page says {answer}. What is true now?"

   Neither placeholder is defined in the SKILL.md values table. [SKILL.md:91](skills/close-up/SKILL.md:91) only says:

   > "The reply changes only that fact"

   But the sources combine facts: question 3 asks "Hair: colour and length?" ([first-run-questions.md:8](skills/close-up/references/first-run-questions.md:8)), and the page has one combined "Glasses, hearing aids, what they wear or carry" answer ([page-format.md:18](skills/close-up/references/page-format.md:18)).

   For `Hair: short brown`, a photo showing short grey hair and a reply of `grey` still leave unspecified whether colour alone or the whole Hair answer is replaced. The message also never selects between the saved answer and a replacement already accepted during step 4.

   **Smallest fix:** Define the M35 values and targeted component explicitly: hair colour, hair length, glasses or hearing aids. Take `{trait}` only from the newly picked photo's completed check, and `{answer}` from that component's current working answer after accepted caregiver changes. Replace only that component; preserve the others. Without a checked photo, do not send M35.

3. **LOW: E0's timing requirement cannot hold on the new mid-step route.**

   [SKILL.md:59](skills/close-up/SKILL.md:59) says:

   > "Otherwise go to E0 at once, and let a running expert finish before E1."

   Yet [SKILL.md:108](skills/close-up/SKILL.md:108) requires:

   > "Before any expert runs, send M19, then M22"

   When the interruption arrives during an expert's `waiting_user`, an expert has already run. E0's literal ordering is impossible, although step 0 clearly intends immediate messages.

   **Smallest fix:** Change E0's opening to "On entry, send M19, then M22 at once, without waiting for an answer." Retain step 0's existing wait before E1.

TOTAL findings by severity: CRITICAL 0, HIGH 1, MEDIUM 1, LOW 1.