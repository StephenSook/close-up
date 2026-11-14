# Evidence: everything behind the numbers

Every test, run and review number in the README, the Devpost write-up and the PDF comes from a file in this folder. The caregiver and wandering figures cite their own published sources. Nothing here has run on a real UGREEN NAS. These are fixture runs: a small model (Claude Haiku, model ID claude-haiku-5-5, from each runner's task log) plays Uliya, and written replies stand in for the NAS experts. All people and data in them are made up.

## What is here

| Folder or file | What it is |
|---|---|
| fixtures/close-up/dry-run/final16/ | The full run before the last fixes: one transcript per case, RESULTS.md, the package it tested (package/) and its frozen graders (graders-frozen/). In this run and earlier ones, the model playing Uliya could read references/testing.md, which then listed each case's expected messages. final17 runs without that list |
| fixtures/close-up/dry-run/final17/ | The first run without that list, on the package before its last two fixes, with its package and graders. It missed its pass bar, and RESULTS.md says how |
| fixtures/close-up/dry-run/final18/ | The release run, on the released package (close-up/ at the top of this repo), with its graders. Its RESULTS.md holds the ship rule written before run 1, the miss at C01, the C27 safety fail, the one rerun I chose after seeing that fail (in rerun/), and a correction to my first account of it |
| fixtures/close-up/dry-run/baseline/ | The same model on the same cases without Close-Up, its harm checks, the rules fixed before the first run, and CLOSEUP-ARM.md, the same checks counted on final17 and final18 |
| fixtures/close-up/dry-run/cases/ | Each case: what the caregiver says and what the experts reply |
| fixtures/close-up/dry-run/RUNNER.md | The prompt every runner got |
| fixtures/close-up/dry-run/DEFECTS.md | Every defect found, its fix or its Round 2 plan, and the totals |
| fixtures/close-up/world/ | The test world, written by Codex without reading the package |
| fixtures/close-up/rounds/ | Every Codex and Grok review report and its verdicts, plus LEDGER.md |
| fixtures/close-up/tools/ | ledger.py rebuilds LEDGER.md from the round files, and recount.py regrades a run with that run's own graders and package |
| tools/semcheck.py | Checks every action the steps expect against UGREEN's capability catalog (run it with the catalog from the kit the main README downloads) |
| fixtures/close-up/ROUND2-DEVICE-TESTS.md | The NAS behaviours the package relies on, with the fallback where one exists, all NOT VERIFIED until a NAS run |

## Recount it yourself

Needs Python 3. Run from this folder.

```sh
python3 -I fixtures/close-up/tools/ledger.py --check
python3 -I fixtures/close-up/tools/recount.py final18
```

The first command rebuilds the review ledger from the round files and exits non-zero if it differs from LEDGER.md. The second regrades the saved release-run transcripts with that run's frozen graders and prints the same totals as final18/RESULTS.md, with the C27 rerun shown on its own. Replace final18 with final17 or final16 to recount those runs. It exits non-zero on any total that differs from RESULTS.md, any grader file whose hash differs from the one RESULTS.md lists, or any check that could not run.

## What this public copy leaves out

- Three sentences in baseline/PREREG.md that named another hackathon entry and its published numbers. The file says where.
- In each round's brief-inline.md, the catalog, kit and package text pasted below the first "=====" line. The opening that ledger.py reads is kept.
- The package copies and diffs inside each round folder. The package itself is close-up/ at the top of this repo.
