1. **MEDIUM: `{REQUEST}` can make the notes delegation invalid.** [SKILL.md:73](<skills/close-up/SKILL.md:73>) says: "Use this question, unchanged, as the query: {REQUEST}." Its [definition](<skills/close-up/SKILL.md:29>) requires "word for word as typed".

   A request such as `Refresh Mom's page && use her notes.` retains `&&` after the required apostrophe escaping. The supplied [checker, line 501](<uliya-skill-kit/scripts/check-lib.mjs:501>) explicitly rejects it with ``/\$\(|`[^`]+`|\|\||&&|\s[|<>]\s/``. A multiline request likewise produces more than one physical line. [SKILL.md:50](<skills/close-up/SKILL.md:50>) checks prohibited characters only in "a path or name" and encodes only "each line break of the page". Neither covers `{REQUEST}`.

   Rewriting the request would violate the [catalog, line 4628](<uliya-skill-kit/data/capability-catalog.json:4628>): "The user's original question, passed verbatim without rewriting." The same promise appears in [install-and-removal.md:32](<skills/close-up/references/install-and-removal.md:32>): "step 4 passes the caregiver's own request word for word". Thus any notes-reading entry path can encounter conflicting requirements.

   **Smallest fix:** capture the triggering request at run entry and validate it before step 4. For unsupported characters or line breaks, ask for a compatible single-line replacement request and wait, or let the caregiver continue without notes. Pass the replacement verbatim; do not silently sanitize it.

CRITICAL: none found. HIGH: none found. LOW: none found.

TOTAL findings by severity: CRITICAL 0, HIGH 0, MEDIUM 1, LOW 0.