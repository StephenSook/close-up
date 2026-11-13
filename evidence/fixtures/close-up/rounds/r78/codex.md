1. **HIGH: Unchecked-photo fallback bypasses the private-care exclusion.** [SKILL.md:82](skills/close-up/SKILL.md:82), also line 88, says: "If the check cannot read them, say so and return up to the 3 newest". Step 6 then says: "Show each returned photo with its number".

   This bypasses the same delegations' requirement: "not a private care moment (undressed, bathing, on a toilet or in medical care)." If screening cannot run and a newest photo depicts bathing, step 6 displays it. [M9](skills/close-up/references/messages.md:13) says "Look closely, and skip any private care photo", but that cannot prevent its initial display.

   **Smallest fix:** Return no candidates when screening cannot run, continue without a new photo, and revise M9 accordingly. Screened ordinary clear photos remain eligible.

2. **LOW: The testing disclosure contradicts its stated input.** [testing.md:11](skills/close-up/references/testing.md:11) says: "The cases, what each one expects and every result are kept outside this package, so the model under test cannot read them."

   The preceding sentence says: "The model under test reads this package and one case." The assertion includes cases, although the model receives one. Storage outside the package does not establish that material is unavailable to the model.

   **Smallest fix:** Replace the changed sentence with: "The cases, what each one expects and every result are stored outside this package; the current case is supplied separately."

CRITICAL: none found. MEDIUM: none found.

TOTAL findings by severity: CRITICAL 0, HIGH 1, MEDIUM 0, LOW 1.