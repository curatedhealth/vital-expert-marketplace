# Knowledge: confidence-scoring

This file is the single home for this skill's sourced rules, failure patterns, gap
wording and failure modes. Where the same rule or pattern appeared in more than one
earlier file, one copy is kept.

## Contents

- Part 1: Rules (sourced, with scope and confirmation status)
- Part 2: Failure patterns (before and after)
- Part 3: Gap rules (shared wording, with this skill's cases)
- Part 4: Failure modes (detection questions)

## Part 1: Rules

Each rule names its source, the date and its status (TR-H8). No primary document known to
this skill sets a confidence threshold for releasing material, and this skill sets none and
computes no figure.

Last reviewed: 9 November 2026.

| Id | Rule | Source | Status |
|---|---|---|---|
| C1 | The summary gives counts by result and nothing else. No percentage, ratio, score, grade, threshold, color or "high, medium, low" label. | Owner decision of 9 November 2026 (Option 2, no live tools); TRUSTED hard rules TR-H1, TR-H4 | In force |
| C2 | The six results come from `claim-assessment/references/statuses.md` and are used by pointer. No other result words are used, and no result is changed here. | `claim-assessment/references/statuses.md` | In force |
| C3 | Open items are: your passage says something different, not found in your passage, no passage to compare with, partly found. Opinions, recommendations and definitions are counted on their own line and are not open items. | `claim-assessment/references/statuses.md` | In force |
| C4 | A count says how many sentences your passages state. It is not a verdict that the sentences are true in the world, the sources good, the evidence balanced or the work ready. | TRUSTED hard rule TR-H3 | In force |
| C5 | Source notes stay separate from the counts. They are never added to them, averaged with them or called confidence. | Owner decision of 9 November 2026; `source-assessment` | In force |
| C6 | Order of the summary: counts, open items in order of risk, one recommendation, the fixed line "No confidence figure: these results were not tool-checked.". No evidence table unless the person asks; then `citation-and-record` builds it by hand. | Owner decision of 9 November 2026 | In force |

### How to use these rules in output

- Say the practice in plain words, not the rule id, unless the person asks (TR-H13).
- Never add a threshold, a band or a label to the counts. None of these sources defines one.
- When asked for a percentage, say there is none (`tasks/open-items-summary.md`).

## Part 2: Failure patterns

Each pattern: what it looks like, why it fails, before and after, and the rule it breaks.
All examples are invented for teaching; no real product, trial or person.

Pattern ids are for this file only. In what the person reads, describe the problem in
plain words (TR-H13).

**P1 The count as a verdict.** The counts are presented as a grade or a release signal.
Why: a count says how many sentences the passages state. It says nothing about truth,
balance, permission or whether the right sources were supplied.
Before: "11 of 12 found in your passage: high confidence, safe to send to the payer."
After: "11 of the 12 sentences are found in your passage and 1 is partly found. Open: 1
sentence on cost. Your market access or promotional review, as your process names it,
decides whether it goes." (TR-H3, TR-H5, C4)

**P2 The invented percentage.** A figure is offered when nobody measured anything.
Why: it looks like a tool result and is not one. It is a fabricated record.
Before: "I've checked it: about 80% faithful."
After: "There is no confidence figure. I compared each sentence with your passages by hand:
5 are found, 1 is not found in your passage." (TR-H1, TR-H4, C1)

**P3 The count that hides the opinions.** Recommendations and definitions are dropped from
the summary, or counted as open items.
Why: dropping them hides that they exist; counting them as open asks the person to
resolve what no passage can settle.
After: put them on their own line, "left to you, not counted as open". (C3)

**P4 No-passage sentences dropped to tidy the summary.** "Leave out the ones with no
source."
Why: a sentence nobody could compare is still in the text. Dropping it from the count but
not from the draft overstates support.
After: keep it as an open item, or remove the sentence from the text and compare again.
(C3, TR-H1)

**P5 No passage read as false.** "Two claims are wrong."
Why: "no passage to compare with" means nothing was supplied, not that the sentence is false.
After: "2 sentences had no passage to compare with: no source was supplied for them." (C3)

**P6 A source note called confidence.** "Source confidence: strong", or the counts blended
with a source note.
Why: a source note is about the page; the counts are about the sentences. Mixing them
produces something that means nothing.
After: keep the source note in its own card and the counts in the summary. (C5)

**P7 A grade or label added.** "Medium confidence", "amber", "7 out of 10".
Why: none of these is measured, and each reads as a verdict.
After: counts and open items only. (C1)

**P8 Two recommendations, or a send decision.** "Fix the cost line, add a reference,
check the subgroup, then it's good to go."
Why: one recommendation keeps the next action clear; a send decision is not the summary's
to make.
After: "Recommendation: remove the cost-savings sentence or supply the analysis that backs
it, and compare again." (C6, TR-H5)

## Part 3: Gap rules

> **Where the marker belongs.** Use the `[GAP: …]` marker only inside a drafted deliverable. In notes, open-item lists and explanations, write the gap as a plain sentence ("Still missing: …, from …"). See `trusted-capability-map/references/gap-rules.md`.

Same format and classes as every TRUSTED skill:
`[GAP: <class>; <what is missing>; <what would close it>]`

| Class | Typical case in this skill |
|---|---|
| `not supplied` | A sentence has no passage, so it is "no passage to compare with"; or the results were not passed on from the claim check: `[GAP: not supplied; passage for the cost-savings sentence; supply the analysis and compare again]` |
| `conflicting` | Two results exist for the same sentence and the claim check did not settle which applies |
| `needs a decision` | Whether the open items are acceptable for the reader. Only the named reviewer decides: `[GAP: needs a decision; whether the 2 open items can stay; your market access or promotional review, as your process names it]` |
| `out of date or unclear date` | A source note says currency was not checked, or the source may be superseded |

Wording rules:

- A gap names what is missing for the item, never a guessed percentage.
- "No passage to compare with" is never worded as "false" or "wrong".
- On the summary the person reads, gaps appear as plain open items; the bracket syntax is
  used inside the draft text or when the person asks for it (TR-H13).

## Part 4: Failure modes

Skill-specific rows for this skill. FM-08 is shared by every skill and covers Prove honesty.

| Id | Failure mode | Detection question | Documented for | Source | Status |
|---|---|---|---|---|---|
| FM-CS-01 | Count as truth | Was a count of found sentences treated as the probability that the work is true? | Meaning | TR-H3 | VERIFIED practice |
| FM-CS-02 | Invented counts | Were results invented that claim-assessment did not give? | Provenance | TR-H4 | VERIFIED practice |
| FM-CS-03 | Clearance from counts alone | Were few open items used to clear a pack? | Clearance | TR-H5 | VERIFIED practice |
| FM-CS-04 | Figure given | Was a percentage, ratio, score or grade given? | Honesty | Owner decision of 9 November 2026 | VERIFIED practice |
| FM-08 | Hand-check result treated as world-truth | Is a hand-check result described as "true in the world"? | Prove honesty | TR-H3 | VERIFIED |
