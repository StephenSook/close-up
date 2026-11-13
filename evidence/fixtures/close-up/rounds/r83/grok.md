The photo-keep edits agree with step 6, the failed row, E3, E4, and the no-photo line on "none". Two control-flow gaps remain.

**CRITICAL:** none found.

1. **HIGH.** `SKILL.md` line 66, and the emergency path that calls it. Step 3 says a second missing folder "gets M17", and M17 reads "Stopped. Already saved: {what exists, or nothing}. Nothing more will be saved or created." Nothing in that branch says the run ends. M17 is not itself a stop: the cancelled row sends M17 and then step 10. E1 reads the page "with step 3" and then continues: "No page, or an unreadable one: M4 or M5, then ask for the person album or photo folder (waiting_user). Either way, ask [what they are wearing]." E4 on yes still "run[s] step 8". After two missing folders the parent can say nothing more will be saved and then keep asking and save. The retry cap itself is fine: one M3 wait, one more step 3, then M17, and that count is separate from step 2's own M3. Smallest fix: on that second miss, send M17 and end the run, in calm time and in E1, with no M4 and no E4 save.

2. **MEDIUM.** `SKILL.md` line 90, against line 52, `page-format.md` line 55, and E3. The calm question is still "go on without a photo?" The same sentence now routes that answer to "step 7 with no new photo", and line 52 keeps "the last page photo ... when no new photo was shown". Line 55 prints "Photo: no recent photo..." only "With no photo picked and no last page photo kept", so a kept photo also keeps "a recent photo" off Still needed. E3 states the other half in the open: "M21 and keep the page photo when the page has one", and M21 says "Use the photo from your page." The calm question says the page will have no photo. Smallest fix: when the last page has a photo, ask "go on with the photo from your page?"; ask "go on without a photo?" only when it does not.

**LOW:** none found.

Checked and consistent: "none" still prints the no-photo line; a failed photo step keeps the last page photo only if there is one; step 3 waits once on its own M3 and stops at the second miss; M17's "or nothing" covers a stop before any save; both Last seen lines still end with "(You said, from a camera moment this run)" and drop heading and wearing without a stray comma. Checklist items 1 through 15 hold apart from item 6, which is finding 1.

TOTAL: 0 CRITICAL, 1 HIGH, 1 MEDIUM, 0 LOW.
