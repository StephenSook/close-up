# Round 40 adjudication (written 2026-11-12 09:12 EST, shell clock)

Grok round 40 (grok-4.7, xhigh, inline brief, tools off, scope: the testing.md results paragraph rewritten from final10): exit 0, 7-line report read in full, 1 MEDIUM.

MEDIUM, "in 8 of 19 emergency runs from an older-format saved page". Grok: the evidence says the 8 failures were on older-format pages, not that all 19 runs were, so the paragraph defines the measured set more narrowly than the evidence.

Checked. The claim is true, and the evidence record did not say so. The only emergency cases with a saved page are C08, C16 and C17 (C09 and C18 have none). In each case file the saved page has the old print wording "Print it with this page" and not the current "Print the full-size original" (grep counts old=1, new=0 for each). So all 19 runs started from an older-format page.

Fix: the evidence, not the package. final10/RESULTS.md and DEFECTS.md now state that all 19 runs used the older-format fixture pages and how that was checked. The testing.md wording stays: it carries the scope a reader needs, that D27 was measured only on pages older than this package's format. Grok's proposed wording ("with a saved page") is also true but drops that scope. Package unchanged, 8,000 words.
