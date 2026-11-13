# Clarification (not a change)

Written 2026-11-13 02:28 EST (shell clock), before any baseline run. PREREG.md (commit 75a4d2e) stays as committed.

PREREG.md says the baseline runner gets "the delegate tool description and the list of the six experts". The six are the six registered expert agents in UGREEN's capability catalog 2.2.0 (uliya-skill-kit/data/capability-catalog.json), the set Uliya itself has, each named by the "agent" field of its CLI entries (first line given):

| Agent | First catalog line | CLI entries |
|---|---|---|
| file-agent | 2150 | 3 |
| photo-agent | 5267 | 1 |
| security-monitor-agent | 1163 | 1 |
| document-agent | 4302 | 1 |
| knowledge-agent | 5007 | 1 |
| media-agent | 314 | 2 |

Close-Up itself uses five of them, all but media-agent. The baseline gets all six on purpose. Naming only the five Close-Up uses would leak part of its design into the control.
