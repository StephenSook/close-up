1. **MEDIUM: An emergency switch can restore a photo the caregiver declined.** [SKILL.md:52](skills/close-up/SKILL.md:52) allows the last photo to be kept `"when no new photo was shown, or after a failed photo step"`.

   The contradicting choice is at [line 90](skills/close-up/SKILL.md:90): `"go on without a photo?"` leads to `"step 7 with no photo"`. If the caregiver then reports the person missing before saving, E1 reads the old saved page again. An empty E3 search explicitly says `"M21 and keep the page photo when the page has one"` ([line 128](skills/close-up/SKILL.md:128)). E4 also keeps it `"when no photos were shown"`. The earlier opt-out has no stated precedence over these fallback instructions.

   **Smallest fix:** Treat "go on without a photo" as an explicit no-photo choice that survives an emergency switch and overrides empty/failed-search retention until the caregiver changes it.

2. **MEDIUM: The new M3 branch has an unbounded prompt loop.** [SKILL.md:66](skills/close-up/SKILL.md:66) says `"M3 (no folder: wait, then run step 3 with the folder named)"`.

   M3 asks `"Name a folder that already exists."` ([messages.md:7](skills/close-up/references/messages.md:7)). If that replacement also does not exist, step 3 sends M3 again, without a limit or terminal branch. This bypasses the bounded recovery elsewhere: `"Offer one retry, of that step only"` ([SKILL.md:149](skills/close-up/SKILL.md:149)). A completed result stating that the folder is absent does not enter that failed-state rule. E1 inherits the loop through `"Read the page with step 3"`.

   **Smallest fix:** Route missing-folder recovery through step 2, allow one M3 replacement attempt per run, and end with M17 if that replacement is also missing.

CRITICAL: none found. HIGH: none found. LOW: none found.

TOTAL findings by severity: CRITICAL 0, HIGH 0, MEDIUM 2, LOW 0.