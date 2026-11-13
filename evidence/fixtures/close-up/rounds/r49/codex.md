1. **HIGH: The emergency handoff can endorse a page that just failed verification.**

   [SKILL.md:59](skills/close-up/SKILL.md:59) says: "Wait for a sent write and its read-back before E1."

   Step 8, line 92, selects "Any other text, even a placeholder, M14", but defers that message to step 10. E1, line 109, instead reads the newest page through step 3 and says "send M30 at once".

   **Failure path:** Missing-now arrives while the calm save waits for approval. The save completes with a placeholder; its read-back selects M14. The handoff then enters E1 before the interrupted run's step 10. Step 3 reads that newly saved, readable placeholder, and M30 tells the caregiver to print it. E4 can subsequently use it as the saved-page baseline.

   The references directly contradict this endorsement:

   - [messages.md:18](skills/close-up/references/messages.md:18): M14 says, "Check it before printing."
   - [messages.md:33](skills/close-up/references/messages.md:33): M30 says, "Open it in Files now, and print it or show it to the police."
   - [limits.md:12](skills/close-up/references/limits.md:12) likewise requires M14 for malformed saved text.

   **Smallest fix:** Preserve and deliver the interrupted write's verification outcome before E1. Exclude a file that received M14 from E1's usable saved pages; use the previous usable page or the no-usable-page branch. Do not send M30 for the rejected file.

2. **MEDIUM: The new wait requires a read-back on branches where read-back is forbidden or impossible.**

   [SKILL.md:59](skills/close-up/SKILL.md:59) unconditionally requires: "Wait for a sent write and its read-back before E1."

   But step 8, line 92, says: "Read back only a save that completed as saved with a file". Step 9, line 98, similarly requires a create "that completed as created with an identifier". The write rule, line 129, permits terminal outcomes without either artifact: "a cancel that wrote nothing gets M17", and an unresolved create gets M26.

   **Failure path:** Missing-now arrives during a `waiting_approval` save; the caregiver rejects it and it returns cancelled with nothing written. There can be no permitted read-back, so step 0's prerequisite for E1 cannot be satisfied. A blocked or cancelled album create without an identifier has the same gap.

   The references confirm these are terminal outcomes, not pending checks: [messages.md:21](skills/close-up/references/messages.md:21) defines M17 as "Stopped", and [messages.md:30](skills/close-up/references/messages.md:30) defines M26 as "could not be checked".

   **Smallest fix:** Require the sent write's terminal outcome and **any applicable** recovery/read-back steps before E1. Explicitly allow E1 after a no-write cancellation, rejection, or terminal M26 outcome.

CRITICAL: none found. LOW: none found.

TOTAL: 0 CRITICAL, 1 HIGH, 1 MEDIUM, 0 LOW.