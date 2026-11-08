# Knowledge: claim-assessment

## Migrated rules

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

## Migrated patterns

# Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; "Velostra", "Lumivra" and the NORLA registry are
fictional. Pattern ids are for this file only; describe the problem in plain words to
the person (TR-H13).

## Contents

- Splitting and pairing C1–C4, C13, C14
- Reading results C5–C7, C9, C10, C15
- Requests and framing C8, C11, C12

## Splitting and pairing (Part A)

**C1 The cleaned-up sentence.** The text is tidied before it is split, so the check runs
on words the person never wrote.
Why: the result describes a different text; offsets no longer point to the original.
Before: draft says "cuts admissions by 40%"; the check runs on "is associated with fewer
admissions". After: check "cuts admissions by 40%" as written; rewrite only after the
result, and recheck. (TR-H1, R4)

**C2 The bundled claim.** Two facts resting on different passages are checked as one.
Why: a `partial` result is then unreadable, and the unsupported half survives.
Before: "Velostra cut admissions by 40% in the NORLA trial of nearly 2,000 patients"
paired with the outcome passage only. After: note three parts (effect, design, size)
and pair each. (R6)

**C3 The paraphrased passage.** The assistant writes a summary of the source and checks
the claim against its own summary.
Why: the check compares the draft with the assistant, not with the source.
After: quote the source word for word with a locator. (R4, R5)

**C4 The skipped sentence.** Background or "obvious" sentences are left out of the list,
or a sentence without a reference marker is treated as not a claim.
Why: unmarked sentences are where invented details hide. After: list every factual
sentence at the depth the stakes need. (TR-H12)

**C13 The borrowed passage.** The text cites source A; the passage comes from source B
because B happens to say it.
Why: the reader will look in A and not find it. After: pair with the cited source, or
flag that the citation should change. (TR-H1)

**C14 The remembered passage.** No passage was supplied, so the assistant recalls what
the paper "says".
Why: memory is not a source; VERIFY cannot check a recollection. After: ask for the
material. (TR-H1, TR-H4)

## Reading results (Part B)

**C5 The replacement.** A sentence comes back unverifiable or unsupported and is replaced
with a likely value.
Why: the new value has no passage either, and now looks checked.
Before: "approved in March 2025" (passage silent) becomes "approved in early 2025".
After: sentence removed; `[GAP: not supplied — approval date — supply the approval
document]`. (R5, TR-H1)

**C6 Silence read as contradiction.** A passage that does not mention a point is reported
as saying the opposite.
Why: it accuses the draft of being wrong when it is only unsupported.
After: "your passage does not say this", not "your passage says otherwise". (R6)

**C7 The figure that survives a partial.** The passage supports the comparison but not
the number, and the number stays.
Before: "admissions fell by 40%" against a passage giving 12.0% and 20.0% with an
adjusted hazard ratio of 0.60. After: "admissions within 12 months were 12.0% with
Velostra and 20.0% with standard care (adjusted hazard ratio 0.60)". (R5)

**C9 The simulated status.** Without VERIFY, results are written as "supported" or
"partial", as if a tool ran.
Why: a manual reading presented as a tool result is a fabricated record.
After: manual result words and "not tool-checked". (TR-H4)

**C10 The unchecked rewrite.** A sentence is rewritten to match the passage and kept
without a second check.
Why: rewrites drift; a new number or word slips in. After: recheck the rewrite, or label
it "rewritten, not tool-checked". (TR-H4)

**C15 Supported read as true.** "Supported" is reported as "verified", "correct" or "true".
Why: the passage may be wrong, old or weak; the reader skips review.
After: "your passage says this", plus the plain-words line on what a match means. (TR-H3,
R5)

## Requests and framing

**C8 The unnamed authority.** "Experts agree", "guidelines recommend", "studies show".
Why: no one can be asked; nothing can be quoted.
After: name and supply the source, or remove the sentence. (R5)

**C11 The fact dressed as opinion.** "We believe Velostra cuts admissions by 40%" filed
as an opinion and skipped.
Why: the figure is still a claim the reader will rely on.
After: check the figure; the "we believe" does not exempt it. (R1)

**C12 "Just mark them all supported."** The person asks for labels without a check.
Why: an unchecked "supported" looks identical to a checked one.
After: decline plainly; offer to check now or mark them "not checked" for review.
(TR-H3, TR-H4, TR-H5)
