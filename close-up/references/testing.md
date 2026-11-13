# Testing

Tags: MEASURED (a command or count), PLANNED, NOT VERIFIED. Nothing here has run on a NAS yet.

## A three-minute check, no NAS needed

Run UGREEN's own checker from the Uliya Skill kit on the unzipped close-up folder. Expected: no errors and no warnings.

## How it was tested

Fixture tests, not device tests. A small model played Uliya with this Skill loaded, against written cases with made-up caregiver answers and made-up expert replies. Each case ran in one pass with every answer visible, so a run shows whether a small model follows the steps, not whether it waits. The model under test reads this package and one case. The cases, what each one expects and every result are kept outside this package. The model under test reads no other case, and its own case holds no expected result.

## Not verified

- Every expert call on a real NAS: the names, the parameters and the replies. The NAS-day list is in [install and removal](install-and-removal.md).
- Time saved against building the same page by hand. PLANNED for the NAS day.
