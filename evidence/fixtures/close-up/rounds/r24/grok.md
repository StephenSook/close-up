1. HIGH. `close-up/SKILL.md`, completion row: "An empty result alone gets M10." M10 is "The {step} step failed. That is a failed search, not a finding. Try again? (yes / no)". The kit says `result: {}` is valid for `completed` and "does not itself mean there is no business result", and that "Business text can live in `summary`". Its own completed example is a found photo in `summary` with `"result": {}`. Its empty example states the none in `summary` ("found no matching photos"), not in `result`. This row never reads `summary`. A completed reply whose file name, photo, or "say so" is only in `summary` is sent M10, which calls a completed step failed and asks to run it again. The only retry rule is under `failed`: "Offer one retry, of that step only." On the save or the album, that is a second write. The waiting_approval row says "never send it again". A no to M10 is also only handled under `failed` ("a failed photo step means the page goes on without a photo"). On E1, a page read with nothing stated has no written path on to the clothing question, E2, or E4.

Smallest fix: on that row, read `summary` and `result`. A none either one states gets that step's fixed sentence. A fact either one states is used even when `result` is `{}`. When the needed fact is in neither, say the delegation completed without it. Send M10 only for a read, once. Do not send the save or the album again. On no, an emergency page read continues at the album question and the clothing question.

2. MEDIUM. `close-up/SKILL.md` step 2: "No result: M3." E2: "Empty list: M11. No events: M12." M3 says "I could not find a folder for the pages." M11 says "The camera list came back empty." M12 says "No Human events were returned". Those sentences assert an absence. The delegations now ask the expert to "say so", and the completed row sends a true empty result to M10, but these lines still key the none-message off "No result", "Empty list", and "No events". A literal reading of the step text sends M3, M11, or M12 for `result: {}`.

Smallest fix: "If the expert says the folder cannot be found, M3." "If the expert says there are no cameras, M11." "If the expert says there are no events, M12."

3. MEDIUM. `close-up/SKILL.md` step 8: "No read-back, M26." Step 9 sends M26 "if it lists no photo items" and if the read-back fails again. The `failed` row says "a read-back (steps 8 and 9) gets no M10: only the read delegation retries, once, on its own." The completed row still sends every empty result to M10, and M10 asks to retry "{step}". Step 8's step includes the save, and step 9's includes the album create.

Smallest fix: on the completed row, a page or album read-back that brings back no text is M26, and is not M10.

4. MEDIUM. `close-up/SKILL.md` E4: "the Wearing today line (added if missing)". E2 says "Clothing stated with a named moment replaces the E1 answer." The diff removed the words that set that line to the E1 answer or the E2 clothing. A calm page has no Wearing today line, so "added if missing" can add one. An emergency page already has the line (`page-format.md`: "Wearing today: {answer} (You said)"). "added if missing" leaves that line as it stands, so today's E1 answer, including clothing that replaced it in E2, is not written. `testing.md` C17: "Emergency refreshes of a calm and an emergency page, with no sighting. Expected: Wearing today from E1".

Smallest fix: "the Wearing today line (set to the current answer, added if missing)".

5. LOW. `close-up/SKILL.md` waiting_user row: "The platform asks and resumes the same delegation. Run no later step." That matches a child expert's pause. The same label is used before any delegation exists: "Start every calm-time run with M1 ... and wait (waiting_user). Read nothing before the answer." There is no delegation to resume, and M1 is a question the parent sends. The same label is on M3, the pick, the preview, and the E0 "ask who".

Smallest fix: "A question this skill asks: send it and wait for the answer. waiting_user from an expert: the platform asks and resumes that same delegation. Run no later step either way."

6. LOW. `close-up/references/testing.md`: "Full pass on this final text, with kit 0.7.7: 18 cases". The case list defines C01 through C17 (C13 to C15 is three, C16 and C17 are two). C18 appears only inside C09: "M11 (C18: M10 for an unstated empty list)", with no setup.

Smallest fix: give C18 its own case line (unstated empty camera list, expect M10, then the rest of C09), or say 17 cases.

TOTAL: 1 HIGH, 3 MEDIUM, 2 LOW.
