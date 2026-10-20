# B1 Screen criteria and short list

Framework task: DH-DIL.1.1, Part B, task B1. Replaces the old "Rank only by those criteria" boundary of "Screen a market" and turns it into the judgment task of the competency.

## What this task delivers

A short-list draft: the person's thesis criteria and pass rules written back, each candidate from A1 and A2 marked pass, fail or not measurable against the pass rules, a ranking of the candidates the person scored with where the order would flip, the candidates not ranked and why, and the deal and data rules to flag for the owner the person names for legal questions. It answers "which candidates meet our thesis, in our own order, and what must legal look at?"

Why it matters: a written pass rule and a scored, testable order make a short list arguable and repeatable when the facts change. Flags with their dates keep a deal question in front of the person who decides it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | not bound (diligence suite, not a CF-12 row) |
| Skill | DH-DIL.1.1 Part B, Screen criteria and short list |
| Workflow | The steps below |
| Knowledge | A1 and A2 output; `references/screening-rules.md`; `references/deal-and-data-flags.md` (DL-044 to DL-106, DL-134); MCDA method as cited by the tool (EVIDEM) |
| Tools | `analytics.mcda` (ranks only the candidates the person scored); `scripts/screen_helpers.py swap` (where the order flips); A1's tools if no screen exists |
| Prompt | This guide |
| Template | `assets/short-list-output.md` |
| Input | The request and its context; A1 and A2 results; the person's criteria, pass rules, weights, 0 to 4 scores and named owners; deal facts the person gives (data volumes, acquirer, deal size) |
| Governance | `references/governance.md`; people score and decide; no investment advice; deal rules stop for the owner the person names for legal questions |
| Catalogue job | none |

## The rule that shapes this task: people score and decide

The person writes the criteria and pass rules, sets weights and scores, and decides the short list. `analytics.mcda` only ranks what the person scored. If asked to propose criteria or scores, each is marked "proposed", carries the A1 or A2 fact behind it, and is not applied or ranked until the person confirms it. A ranking is never presented as a recommendation to invest, and no candidate is ever called a good or bad investment.

## Workflow

### Step 1. Start from the facts

Use the A1 screen and any A2 checks in this request. If none exists, run A1 in short mode for the person's segment and jurisdictions. Candidates with `[GAP]` cells stay in, with the gap visible.

### Step 1b. Company status

Every candidate on the short list carries one status line from the A2 status step (`screening-rules.md` section 5): the status as a primary filing or register entry states it, with form or item, date and source, or "Status: [GAP]: not read" with the exact filings to open. Never infer status from press, memory or a missing filing. A status the person must still check stays visible beside the candidate; it is never a pass rule unless the person writes one.

### Step 2. Write the criteria and pass rules back

Number the person's criteria and pass rules in their words. Mark which pass rules can be checked from A1 and A2 facts (for example "at least one FDA authorization on record", "a registered study naming the brand") and which need facts the registers do not hold (revenue, contracts, data volumes): those are "not measurable from the record" and stay with the person. A criterion that uses the library's evidence maturity score is allowed only if the person sets it; say what the score counts (`screening-rules.md` section 3).

### Step 3. Apply the pass rules

For each candidate and pass rule: pass, fail or not measurable `[GAP]`, with the fact, its source and retrieval date. With code execution, `scripts/screen_helpers.py table <screen.json> --min-authorizations N --min-score N` applies the two numeric rules it supports, labeled "your rule". Never drop a candidate for a `[GAP]`; list it as not measurable.

### Step 4. Rank what was scored

Collect weights (sum to 1) and 0 to 4 scores for the candidates that passed, each criterion phrased so 4 is best. Drop any candidate missing a score before the call (a missing score returns HTTP 400 for the whole call) and list it as "not ranked: score missing". Call `analytics.mcda` with `{alternatives: [{id, scores}], criteria_weights}`. Report each value and the largest contributing criterion. Then save input and output to one file and run `scripts/screen_helpers.py swap <file>`; without code execution, work the swap point by hand (value = 25 x sum of weight x score; move one weight, rescale the others in proportion). In the saved illustrative run, the top two swapped if the weight on the first criterion fell from 0.50 to 0.286 or the third rose from 0.20 to 0.385 (`examples/live/mcda_illustrative_partnership_screen.json`; illustrative scores, not an assessment of those companies). Name the close call. Every statement of what would change the order is computed, not estimated: quote the `swap` output or show the arithmetic from the person's own weights and scores; never write "a small change could flip it" without the number.

### Step 5. Flag deal and data rules

From `deal-and-data-flags.md`, flag each rule whose trigger appears in the person's facts or the record, in the form given there, with row ids and dates. Typical triggers in digital health: identifiable health or genetic data in the product (CFIUS DL-056 to DL-058; DOJ bulk thresholds DL-066 to DL-068, countries of concern DL-069); a foreign acquirer or a board seat (DL-062 to DL-065); an EU target (DL-072 to DL-078); a Swiss target in the health sector with a state-controlled acquirer (DL-083, DL-084); US deal size (HSR 2026, DL-044 to DL-048). Where the facts needed are "not given", list the question for the owner the person names for legal questions. Where a deal-size, data-volume or share threshold is involved, put the threshold and the person's figure side by side in the flags table without saying in prose whether the deal is under or over it, and include every flag the rows support for the data involved (GDPR Article 9, DL-099 to DL-106, for health data of EU residents; HIPAA breach rules, DL-086 to DL-098). Never say a deal is or is not caught.

### Step 6. Record the person's short list

Write the short list as the person decides it, in their order, with one reason each in their words, and the candidates out with one reason each. If the person has not decided, show the ranking and ask; do not choose.

## Build the output

Follow `assets/short-list-output.md`. Short mode: pass rules and results, one status line per candidate, the ranking as scored with the close call, candidates not ranked, the flags for the owner the person names for legal questions, the decision the person needs to make, and the record line. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Criteria, pass rules, weights, scores and the short list are the person's, and the output says so; proposals are labeled.
- No recommendation to invest or pass, no valuation, price, multiple, return or market size.
- Every flag carries its row id and date and says "for the owner you name for legal questions; not assessed here".
- Facts from the person's confidential material are labeled "from your material".
- Each candidate has a status line from a primary record, or "Status: [GAP]: not read" with the filings to open; no status taken from press or memory.
- Word count run (`scripts/screen_helpers.py wordcount <answer.md>`, or by hand): short mode at or under 450 words without the calls list and source columns.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model filters, ranks what was scored and flags; it does not choose targets or advise on investment.
- Deeper work on a short-listed company: `company-and-evidence-assessment`, then `funding-and-portfolio-comparison`, then `investment-memo-and-decision-record` (this pack).
- Whether a deal is reportable or compliant: the owner the person names for legal or compliance questions.
