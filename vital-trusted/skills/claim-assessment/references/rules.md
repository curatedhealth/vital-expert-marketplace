# Primary rules this skill applies

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` is applied as good practice, not cited as a requirement (TR-H8).

Last reviewed: 20 October 2026.

## Why claims must be checkable

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | "Promotion should be capable of substantiation either by reference to the approved labeling or by scientific evidence." Evidence should be made available to healthcare professionals on request. | IFPMA Code of Practice 2019, section 4.3 Substantiation. Effective 1 January 2019, replacing the 2012 code. Official copy at ifpma.org. | International industry code for promotion to healthcare professionals; national codes and law apply on top | Confirmed 20 October 2026 from the official IFPMA PDF, read through a fetch tool that returned the section wording |
| R2 | Promotional information should be accurate, balanced, fair and sufficiently complete, should not mislead "by distortion, exaggeration, undue emphasis, omission or in any other way", and "absolute or all-embracing claims should be used with caution and only with adequate qualification and substantiation." | IFPMA Code of Practice 2019, section 4.2 Accurate and Not Misleading | As R1 | Confirmed 20 October 2026, as R1 |
| R3 | "Any information, claim or comparison must be capable of substantiation." Companies must provide substantiation on request. Information, claims and comparisons must be accurate, balanced, fair, objective and unambiguous, based on an up-to-date evaluation of all the evidence. | ABPI Code of Practice for the Pharmaceutical Industry 2024, clauses 6.1 and 6.2, PMCPA interactive code | UK | Confirmed 20 October 2026 from the PMCPA interactive code page. Effective date of the 2024 code `[CHECK]` |

No US, EU-level or Swiss rule is cited here. In those markets, apply R1 to R3 as good
practice and point to the person's promotional or medical review process (TR-H11).
`[CHECK]` Candidate primary sources, not yet read: EFPIA Code; the Swiss Pharma Code;
FDA regulations on prescription drug advertising (21 CFR 202.1).

## How support is decided

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R4 | `extract_claims` takes text up to 20,000 characters and returns claims with offsets; it never decides support. `check_claim` decides whether a given passage supports a given claim, is called after `qualify_source` has admitted the source, returns a status and the deciding passage, never searches and never judges truth; the passage is quoted, not paraphrased. `verify_text` extracts and checks against named sources or ingested documents in one counted call, returns at most 60 findings, and does not clear a record. | VERIFY connector tool schemas as exposed to this session | Confirmed 20 October 2026 from the schemas (read, not called). Return fields beyond the descriptions `[CHECK]` |
| R5 | A status is word overlap with the supplied passage, not a verdict that the sentence is true in the world. A number, a named person, a quotation, or a compliance or performance claim may stay only when `check_claim` returned it from a quoted passage. An unnamed authority is not a source. If the passage is silent, omit the sentence. Unverifiable means the sentence stays out, not that it is replaced. Statuses: supported, partial, unsupported, contradicted, unverifiable, out_of_scope. | VERIFY connector operating instructions as exposed to this session | Confirmed 20 October 2026 as exposed text. It is the connector's own contract, not an external rule |
| R6 | Status boundaries: supported means the passage states the claim or a stricter version; partial names the supported part and the rest; unsupported needs admissible sources to have been checked; contradicted needs a passage stating the opposite; unverifiable covers a missing or inadmissible source or empty passage; out_of_scope covers normative and definitional claims, which leave the confidence denominator; a bronze-tier passage yields at most partial. | Earlier vital-verify plugin, skills support-decision and claim-decomposition, version 2026-10-19.2 | `[CHECK]` Asserted by a document, not confirmed against the VERIFY service. Applied as this skill's reading guide; VERIFY's returned status always wins |

## How to use these rules in output

- In what the person reads, say the practice in plain words ("a reviewer will ask to see
  where this comes from"), not the clause number, unless they ask (TR-H13).
- R1 to R3 cover promotional material. Do not extend them to a scientific publication or
  a purely internal note; there, checkability is good practice.
- R5 and R6 describe VERIFY's behavior. They are never presented as regulation.
