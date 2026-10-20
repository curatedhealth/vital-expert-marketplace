# Primary rules this skill applies

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` is applied as good practice, not cited as a requirement (VR-H8).

Last reviewed: 20 October 2026.

## Why support must be checkable

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | Promotion should be capable of substantiation by approved labeling or scientific evidence; evidence should be available to healthcare professionals on request. | IFPMA Code of Practice 2019, section 4.3 Substantiation. Effective 1 January 2019. Official copy at ifpma.org. | International industry code for promotion to HCPs; national codes and law apply on top | Confirmed 20 October 2026 from the official IFPMA PDF (via TRUSTED claim-assessment rules, same wording) |
| R2 | Promotional information should be accurate, balanced, fair and sufficiently complete; it should not mislead by distortion, exaggeration, undue emphasis or omission. | IFPMA Code of Practice 2019, section 4.2 | As R1 | Confirmed 20 October 2026, as R1 |
| R3 | Any information, claim or comparison must be capable of substantiation; companies must provide substantiation on request. | ABPI Code of Practice 2024, clauses 6.1 and 6.2 (PMCPA interactive code) | UK | Confirmed 20 October 2026 from the PMCPA interactive code page. Effective date of the 2024 code `[CHECK]` |

No US, EU-level or Swiss rule is cited here. In those markets, apply R1–R3 as good
practice and point to the person's promotional or medical review process (VR-H11).
`[CHECK]` Candidate primary sources, not yet read for this pack: EFPIA Code; Swiss Pharma
Code; FDA 21 CFR 202.1.

## How support is decided (VERIFY contract)

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R4 | `check_claim` decides whether a given passage supports a given claim after `qualify_source` has admitted the source; returns a status and the deciding passage; never searches and never judges truth; the passage is quoted, not paraphrased. `verify_text` extracts and checks against named sources in one counted call (at most 60 findings) and does not clear a record. | VERIFY connector tool schemas as of 19–20 October 2026 | Confirmed from schemas and `mcps/verify` service behavior. Return fields beyond the descriptions `[CHECK]` |
| R5 | A status is word overlap with the supplied passage, not a verdict that the sentence is true in the world. Numbers, named persons, quotations, and compliance or performance claims stay only when the deciding passage states them. An unnamed authority is not a source. | VERIFY operating instructions | Confirmed as connector contract, not an external regulation |
| R6 | Status boundaries and bronze→at most partial: see `statuses.md`. Statuses: supported, partial, unsupported, contradicted, unverifiable, out_of_scope. | Verify method `statuses.md` + service mapping, 19 October 2026 | `[CHECK]` Applied as this skill's reading guide; VERIFY's returned status always wins |

## How to use these rules in output

- Say the practice in plain words to the person, not clause numbers, unless they ask (VR-H13).
- R1–R3 cover promotional material. Do not extend them to a purely internal note without
  saying it is good practice.
- R5 and R6 describe VERIFY's behavior. Never present them as regulation.
