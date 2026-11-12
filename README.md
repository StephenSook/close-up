# Close-Up

When you ask, Close-Up makes the page you'd hand to police if someone with dementia went missing, with a recent close-up photo you pick, from the family photos on your UGREEN NAS.

Close-Up is a Markdown-only Skill for Uliya, the assistant on UGREEN AI NAS. It is my entry in the UGREEN Hackathon 2026 on AI NAS. Write-up: https://devpost.com/software/close-up

**Who it's for:** the son, daughter, husband or wife caring for someone with dementia at home, whose family photos are on a UGREEN NAS.

**Check it yourself, no NAS needed:** [![UGREEN checker](https://github.com/StephenSook/close-up/actions/workflows/ugreen-checker.yml/badge.svg)](https://github.com/StephenSook/close-up/actions/workflows/ugreen-checker.yml)

Every push downloads UGREEN's own Skill kit 0.7.7 from the official starter-kit link, checks the kit's SHA-256, and runs UGREEN's checker on the folder inside the exact ZIP I submitted ([release/close-up.zip](release/close-up.zip), SHA-256 `e340e7f063998eba43e2424a21d0d217e9bc17e09133f3fd63e1d0ee583bd513`). The result is 0 errors and 0 warnings. To run the same check on your own computer:

```sh
curl -L -o kit.zip "https://cdn.shopify.com/s/files/1/0630/9416/1602/files/uliya-skill-kit-0.7.7-en.zip?v=1794462613"
shasum -a 256 kit.zip      # e3a9c6a7b80b5790865aa1eea310a942904993693a021888b5f9d580f35d8a67
unzip -q kit.zip
unzip -q release/close-up.zip -d rel
node uliya-skill-kit/scripts/check-skill.mjs rel/close-up
```

![A sample page with made-up details](docs/images/sample-page.png)

*A sample page. Every detail on it is made up.*

## Why

In Xi'an in 2019, a 78-year-old woman with Alzheimer's went for a walk and couldn't remember her address. Her family searched all night, showing her photo to strangers. She was found the next day at a rescue center, about 9 km away (CGTN, 2020).

The Alzheimer's Association says six in 10 people living with dementia will wander at least once, and it tells families to keep a recent, close-up photo on hand to give to police. Here in Cobb County, where I go to school, Marietta police ask caregivers to update a registry every six months. Six months is a long time when someone's glasses, hair or walks change, and the newest photos are all over everyone's phones.

## The people who shaped it

- **John Clark, Georgia Emergency Search and Rescue**, who trains police in search and rescue: "Don't look for them first. Call the police first." So when someone is missing, the first thing Close-Up says is "Call the police now, before you start looking." He also said "The photo needs to be as fresh as possible," and "You have to know who that person was, not who they are now," which is why the page asks about old names, old jobs, old homes and places they used to go.
- **Sgt. W. D. Nerio, Cobb County Police Department, Community Affairs Unit**, sent the list officers need: full name and date of birth, a recent photo, exactly what they were last wearing, familiar places, places they're drawn to, and medical conditions. "Clothing information is particularly important, not only to help identify and locate the missing person but also to assess potential safety risks." The next version, in testing now, adds full name and date of birth, whether they're dressed for the weather, and any tracking program like Project Lifesaver.
- **A 2025 study from KSU researchers** (Akintomide, Zhang and others, OBM Geriatrics) interviewed 15 dementia caregivers and found they end up having to memorize and recall what they learn. Close-Up writes it down ahead of time.

Both quotes are used with permission.

## What it does

- Searches the caregiver's photos on the NAS, starting from the person album UGREEN Photos already made, then checks up to nine with the NAS's local vision model for one clear, front-facing face.
- Shows up to three photos, each with the reason it was shown. The caregiver picks one. It never picks for them.
- Reads the last page word for word and asks what changed, like new glasses or a new place they walk to. Each change is a yes or no.
- Saves a new dated page after the caregiver approves it, then an album with the picked photo, which waits for approval too. Old pages stay.
- When someone is missing, it says to call the police first, then brings up the saved page, asks what they're wearing today, and can help check a camera on the NAS for which way they went.
- If it can't find something, it says so. It never fills a gap with a guess.

![The caregiver's steps](docs/images/flow.png)

## How it works

A Uliya Skill is plain Markdown. Uliya reads [SKILL.md](close-up/SKILL.md) and hands each step to one of its local expert agents. SKILL.md has 12 delegations to five of the six experts. These are the catalog actions I expect each step to use (from [install-and-removal.md](close-up/references/install-and-removal.md)):

| Step | Expert | Expected actions | Effect |
|---|---|---|---|
| Find the pages folder | file-agent | file-workflow get-user-dir | read |
| Read the last page | file-agent | ug-filesystem ls, file content read | read |
| Read a notes file | document-agent | ug-document qa | read |
| Find and check photos | photo-agent | ug-photo figure-albums, search-picture, meta, vision-vlm | read |
| Photos from a folder | file-agent, photo-agent | ug-filesystem find, ug-photo meta, vision-vlm | read |
| Save the page | knowledge-agent, file-agent | ug-knowledge save-text after approval, then a read-back | write, then read |
| Make the album | photo-agent | ug-photo create-album after approval, then album-detail | write, then read |
| Camera check (missing only) | security-monitor-agent | ug-surveillance cameras, event-timeline, event-evidence | read |

Never used: identity lookups, face lists, person-name filters, known or stranger labels, photo timelines, folder creation, moves and deletes.

## What's in the package

| File | What it holds |
|---|---|
| [SKILL.md](close-up/SKILL.md) | The steps, each delegation, and what to do on every end state |
| [first-run-questions.md](close-up/references/first-run-questions.md) | The questions, asked once |
| [page-format.md](close-up/references/page-format.md) | The page, line by line, with a source on every line |
| [messages.md](close-up/references/messages.md) | Every fixed message Close-Up shows |
| [limits.md](close-up/references/limits.md) | What it can't do |
| [testing.md](close-up/references/testing.md) | The test cases and results |
| [sources.md](close-up/references/sources.md) | Where each rule came from |
| [install-and-removal.md](close-up/references/install-and-removal.md) | Setup, the expected actions, removal |
| [disclosures.md](close-up/references/disclosures.md) | AI tools used, third-party components (none), test data |

## How I tested it

UGREEN's official checker runs on every push (the badge above). Before submitting, I dry-ran 18 test cases, every example prompt in SKILL.md among them. A small model (Claude Haiku) played Uliya, and the experts answered with written replies, mostly from a test world Codex wrote without reading the package. Across the runs they found 30 defects, and I fixed 29. In the final pass, 17 of 18 cases passed their checks, and all 16 saves matched the preview the caregiver approved. The one I didn't fix: in 8 of 19 emergency runs from an older-format saved page, the page shown first didn't match the saved page exactly. The next version removes that by naming the saved file instead of retyping it. Nothing has run on a real UGREEN NAS yet.

## Where it could go wrong

- **The wrong photo.** Vision can misread a face, so a person always picks the photo and confirms every change.
- **An old page.** Every page carries the date it was last confirmed and by whom. A full page also has a refresh-by date.
- **Privacy.** Close-Up's own steps call no outside service and have no sync or sharing step. Before it reads anything in calm time, it asks you to confirm Uliya's local model is on.
- **A page about a real person.** The opening questions include "Have they been told about this page, and did they have a say in it?"

## Sources

- CGTN, June 17 2020: https://news.cgtn.com/news/2020-06-17/App-developers-help-find-missing-persons-through-crowdsourcing--RopozAARAQ/index.html
- Alzheimer's Association, Wandering: https://www.alz.org/help-support/caregiving/stages-behaviors/wandering
- Spectrum News, Marietta Vulnerable Person Registry: https://spectrumlocalnews.com/ga/georgia/news/2026/09/03/marietta-pd-urging-caregivers-to-enroll-in-vulnerable-person-registry
- Interview with John Clark, Georgia Emergency Search and Rescue, Nov 11 2026, quoted with his permission
- Email from Sgt. W. D. Nerio, Cobb County Police Department, Community Affairs Unit, Nov 12 2026, quoted with his permission
- Akintomide, Zhang, Iwuagwu and Ramos, "Experiences and Support Needs of Informal Caregivers in Managing Behavioral Symptom of Dementia", OBM Geriatrics, 2025: https://doi.org/10.21926/obm.geriatr.2502306

## AI tools

I used Claude Code, Codex and Grok for research, drafting, review and the dry-run tests. Every tool and what it did is listed in [disclosures.md](close-up/references/disclosures.md).

## License

[MIT](LICENSE). UGREEN's Skill kit is not included here. The CI downloads it from UGREEN's official link on each run.
