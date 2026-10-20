# Escalation reference

The packet is input to the record method. It is not a clearance.

| Field | Required content |
|---|---|
| claim | The extracted wording and its offsets |
| status | One of `partial`, `unsupported`, `contradicted`, `unverifiable` |
| tier | The tier from source grading, or `inadmissible` |
| passage | The quoted text, or an explicit statement that none was available |
| locator | Page, section, or URL fragment. Empty only when the passage is empty. |
| question | One question the human can answer without re-running the tools |

Disagreement between two admissible sources is one packet, with both locators, not two silent drops.

The human decisions the clearance officer may later record are `cleared`, `revised`, `removed`, and `escalated`. This skill does not choose among them.


Restated 19 October 2026 from the Verify method.

Last reviewed: 20 October 2026.
