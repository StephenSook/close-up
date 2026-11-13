1. **MEDIUM**: [references/messages.md:40](skills/close-up/references/messages.md:40), M37 requires `"{date} ({capture or file date})"` but has no missing-date form.

   [SKILL.md:87](skills/close-up/SKILL.md:87) explicitly permits: "With no date taken, use the file date given with the path and say so, or say the date is missing." Step 6 nevertheless requires "M37 for each candidate", and messages.md:3 says "Use these as written, values filled in."

   A permitted candidate with no date therefore cannot fit M37 without inventing a date/type or departing from the fixed message. The not-checked variant changes only the Visible part, so it does not cover this case.

   **Smallest fix:** replace `{date} ({capture or file date})` with `{date (capture or file), or date missing}`.

CRITICAL: none found. HIGH: none found. LOW: none found.

TOTAL findings by severity: CRITICAL 0, HIGH 0, MEDIUM 1, LOW 0.