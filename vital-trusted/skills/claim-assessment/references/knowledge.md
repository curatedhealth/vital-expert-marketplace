# Knowledge: claim-assessment

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each rule names its primary source, the date and how it was confirmed. A rule marked
`[CHECK]` is applied as good practice, not cited as a requirement (TR-H8).

Last reviewed: 20 October 2026.

### Why claims must be checkable

| Id | Rule | Primary source | Scope | Status |
|---|---|---|---|---|
| R1 | "Promotion should be capable of substantiation either by reference to the approved labeling or by scientific evidence." Evidence should be made available to healthcare professionals on request. | IFPMA Code of Practice 2019, section 4.3 Substantiation. Effective 1 January 2019, replacing the 2012 code. Official copy at ifpma.org. | International industry code for promotion to healthcare professionals; national codes and law apply on top | Confirmed 20 October 2026 from the official IFPMA PDF, read through a fetch tool that returned the section wording |
| R2 | Promotional information should be accurate, balanced, fair and sufficiently complete, should not mislead "by distortion, exaggeration, undue emphasis, omission or in any other way", and "absolute or all-embracing claims should be used with caution and only with adequate qualification and substantiation." | IFPMA Code of Practice 2019, section 4.2 Accurate and Not Misleading | As R1 | Confirmed 20 October 2026, as R1 |
| R3 | "Any information, claim or comparison must be capable of substantiation." Companies must provide substantiation on request. Information, claims and comparisons must be accurate, balanced, fair, objective and unambiguous, based on an up-to-date evaluation of all the evidence. | ABPI Code of Practice for the Pharmaceutical Industry 2024, clauses 6.1 and 6.2, PMCPA interactive code | UK | Confirmed 20 October 2026 from the PMCPA interactive code page; clause 6.1 and 6.2 text re-read 9 November 2026. The 2024 Code took effect on 1 October 2024, with full force from 1 January 2025 (ABPI page, read 9 November 2026). |

No US, EU-level or Swiss rule is cited here. In those markets, apply R1 to R3 as good
practice and point to the person's promotional or medical review process (TR-H11).
`[CHECK]` Candidate primary sources, not yet read: EFPIA Code; the Swiss Pharma Code;
FDA regulations on prescription drug advertising (21 CFR 202.1).

### How support is decided

| Id | Rule | Primary source | Status |
|---|---|---|---|
| R4 | No tool decides support here. The check is by hand: split the text into claims, pair each claim with an exact quoted passage and a locator, compare, and label every result "not tool-checked". | Owner decision of 9 November 2026 (Option 2, no live tools); TRUSTED hard rules TR-H1, TR-H4 | Owner decision, in force |
| R5 | A result says what the supplied passage says, not that the sentence is true in the world. A number, a named person, a quotation, or a compliance or performance claim stays only when an exact quoted passage with a locator states it, paired with the sentence by hand and shown next to it. An unnamed authority is not a source. When a supplied passage covers the topic and does not state the claim, the result is "not found in your passage": the sentence is removed or rewritten to what the passage states, and listed. When no supplied passage covers the topic, the result is "no passage to compare with": the sentence stays in the revised text with a visible gap and is never filled. One definition: `statuses.md`. | TRUSTED hard rules TR-H1 and TR-H3 | In force |
| R6 | The six results and the boundaries between them are defined once in `references/statuses.md`. No other result words are used. | `references/statuses.md` | In force |

### How to use these rules in output

- In what the person reads, say the practice in plain words ("the code asks that a claim
  be traceable to its source"), not the clause number, unless they ask (TR-H13).
- R1 to R3 cover promotional material. Do not extend them to a scientific publication or
  a purely internal note; there, checkability is good practice.
- R4 to R6 are TRUSTED's own working rules for a hand check. They are never presented as regulation.

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; "Velostra", "Lumivra" and the NORLA registry are
fictional. Pattern ids are for this file only; describe the problem in plain words to
the person (TR-H13).

### Contents

- Splitting and pairing C1–C4, C13, C14
- Reading results C5–C7, C9, C10, C15
- Requests and framing C8, C11, C12

### Splitting and pairing (Part A)

**C1 The cleaned-up sentence.** The text is tidied before it is split, so the check runs
on words the person never wrote.
Why: the result describes a different text; offsets no longer point to the original.
Before: draft says "cuts admissions by 40%"; the check runs on "is associated with fewer
admissions". After: check "cuts admissions by 40%" as written; rewrite only after the
result, and recheck. (TR-H1, R4)

**C2 The bundled claim.** Two facts resting on different passages are checked as one.
Why: a "partly found" result is then unreadable, and the half that is not in the passage survives.
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
Why: memory is not a source; a recollection cannot be quoted back. After: ask for the
material. (TR-H1, TR-H4)

### Reading results (Part B)

**C5 The replacement.** A sentence comes back "no passage to compare with" or "not found in your passage" and is replaced
with a likely value.
Why: the new value has no passage either, and now looks checked.
Before: "approved in March 2025" (passage silent) becomes "approved in early 2025".
After: sentence removed; `[GAP: not supplied; approval date; supply the approval
document]`. (R5, TR-H1)

**C6 Silence read as contradiction.** A passage that does not mention a point is reported
as saying the opposite.
Why: it accuses the draft of being wrong when it is only not found in the passage.
After: "not found in your passage", not "your passage says something different". (R6)

**C7 The figure that survives a partly found result.** The passage supports the comparison but not
the number, and the number stays.
Before: "admissions fell by 40%" against a passage giving 12.0% and 20.0% with an
adjusted hazard ratio of 0.60. After: "admissions within 12 months were 12.0% with
Velostra and 20.0% with standard care (adjusted hazard ratio 0.60)". (R5)

**C9 The simulated status.** Results are written in tool words ("supported", "partial"), as
if a tool ran.
Why: a manual reading presented as a tool result is a fabricated record.
After: the six result words in `statuses.md` and "not tool-checked". (TR-H4)

**C10 The unchecked rewrite.** A sentence is rewritten to match the passage and kept
without a second check.
Why: rewrites drift; a new number or word slips in. After: recheck the rewrite, or label
it "rewritten, not tool-checked". (TR-H4)

**C15 Found read as true.** "Found in your passage" is reported as "verified", "correct" or "true".
Why: the passage may be wrong, old or weak; the reader skips review.
After: "found in your passage", plus the plain-words line on what a match means. (TR-H3,
R5)

### Requests and framing

**C8 The unnamed authority.** "Experts agree", "guidelines recommend", "studies show".
Why: no one can be asked; nothing can be quoted.
After: name and supply the source, or remove the sentence. (R5)

**C11 The fact dressed as opinion.** "We believe Velostra cuts admissions by 40%" filed
as an opinion and skipped.
Why: the figure is still a claim the reader will rely on.
After: check the figure; the "we believe" does not exempt it. (R1)

**C12 "Just mark them all as found."** The person asks for labels without a check.
Why: an unchecked "found" looks identical to a checked one.
After: decline plainly; offer to check now, or list them as "no passage to compare with" so they go to
review as open items.
(TR-H3, TR-H4, TR-H5)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/knowledge.md` (Part 2).

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A claim with no passage in the supplied material; a removed sentence the person may want back |
| `not checkable here` | Whether a sentence matches its passage, when no passage was supplied; a source the person has not named |
| `conflicting` | Two supplied passages disagree on the claim, or the passage says something different from the draft |
| `needs a decision` | Which of two passages governs; whether to keep a recommendation that no passage can settle |
| `out of date or unclear date` | The passage supports the claim but is undated, or says "current" without a date |

How the six results (`statuses.md`) map to gaps:

| Result | Gap, if the sentence is removed or held |
|---|---|
| Found in your passage | None |
| Partly found | `not supplied` for the dropped part, if the person needs it |
| Not found in your passage | `not supplied` |
| Your passage says something different | `conflicting` |
| No passage to compare with | `not supplied` (no passage) or `not checkable here` (source not named) |
| Opinion, recommendation or definition | `needs a decision`, only when the person must decide whether to keep it |

Wording rules:

- Name the exact item: "approval date in Switzerland", not "regulatory details".
- Never hint at a value inside a gap.
- "The passage does not state X" is a finding only for the passage that was quoted. It
  says nothing about the full source unless the full source was supplied and read.
- A gap replaces a removed sentence only when the person needs to see that something is
  missing. Otherwise the sentence simply comes out, and the result lists it.

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CA-01 | Result as world-truth | Was "found in your passage" described as true in the world? | Prove honesty | TR-H3 | VERIFIED |
| FM-CA-02 | Causal verb not in passage | Was "cuts/proves" kept without passage support? | Support | IFPMA 4.2 | PARTIAL |
| FM-CA-03 | Unchecked labeled found | Were claims marked found in your passage without a check? | Honesty | TR-H4 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
