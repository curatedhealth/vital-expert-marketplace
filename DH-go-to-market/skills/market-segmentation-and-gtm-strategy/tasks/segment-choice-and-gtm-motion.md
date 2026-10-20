# B1 Segment choice and GTM motion

Framework task: DH-02.01.2.1, Part B, task B1. Replaces the old "Go-to-market motion" task and folds in the segment sequence from "Segment definition" and the separate tool skill "Rank scored options" as it applies to segments.

## What this task delivers

A decision draft: the candidate segments from A1, the person's criteria, weights and scores, a transparent ranking with where it would flip, the segments in scope and out of scope with one reason each, and for each chosen segment a motion: channel, offer, the proof the buyer needs before a meeting, the channel rules it must respect, and the owner the person names. It answers "which segments first, and how do we go to each?"

Why it matters: a motion copied across segments ignores who pays and what the law lets a seller offer in that channel. A scored, written choice can be challenged and rerun when facts change.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.1 Part B, Segment choice and GTM motion |
| Workflow | The steps below |
| Knowledge | A1 output; `references/segment-and-payer-routes.md`; `references/channel-rules.md`; MCDA method as cited by the tool (EVIDEM; ISPOR MCDA good practice) |
| Tools | `analytics.mcda` (ranks segments the person scored); `scripts/gtm_helpers.py swap` (where the ranking flips); A1's tools if no landscape exists |
| Prompt | This guide |
| Template | `assets/segment-choice-output.md` |
| Input | The request and its context; the A1 table; the person's criteria, weights, 0 to 4 scores, targets and named owners |
| Governance | `references/governance.md`; people score and choose; fraud-and-abuse and pricing stops |
| Catalogue job | `partner-prioritization` (`analytics.mcda` on the segments the person scored). The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## The rule that shapes this task: people score and choose

The person sets criteria, weights and scores, and chooses. `analytics.mcda` only ranks what the person scored. If asked to propose scores, each proposed score carries the A1 fact behind it, is marked "proposed", and is not ranked until the person confirms it. A ranking is never presented as the choice.

## Workflow

### Step 1. Start from the landscape

Use A1 from the conversation. If none exists, run A1 in short mode for the person's segments and markets. Segments whose payer route is `[GAP]` stay in, with the gap visible.

### Step 2. Agree the criteria

Offer this default set; the person drops, adds or renames. Keep four to six, each phrased so 4 is best (the tool treats every criterion as higher-is-better, `tools.md`):

| Criterion | Question | A1 facts that inform it |
|---|---|---|
| Payer route | Is there a route that pays in this segment, and do we meet its entry conditions? | Route and conditions with rows (for example CP-US-58, CP-DE-01) |
| Buyer reachability | Can we reach the buyer through a channel the rules allow? | Channel rules (for example CP-UK-12 frameworks closed to new suppliers except a DPS) |
| Evidence fit | Does the evidence we hold match what this buyer asks for? | The person's evidence; route conditions |
| Room in the segment | How much room do listed or authorized peers leave? | Peers on record with dates |
| Launch readiness | How much is left before we can sell here? | Registration, DTAC, BAA, EUDAMED rows |

Write the 0, 2 and 4 anchors for each criterion with the person, in their words, before scoring.

### Step 3. Lay out the facts, then collect weights and scores

Build the segments-by-criteria table with the A1 fact and row in each cell and no score. Ask for weights (sum to 1) and 0 to 4 scores. Write them back for confirmation. A `[GAP]` cell stays visible even if scored.

### Step 4. Rank and test

Call `analytics.mcda` with `{alternatives: [{id, scores}], criteria_weights}`. Report each value and the largest contributing criterion. Then, with code execution, save the call input and output to one file and run `scripts/gtm_helpers.py swap <file>`; without it, work the swap point by hand from the same formula (value = 25 x sum of weight x score; move one weight, keep the others in proportion). State for each adjacent pair the weight at which they would swap, and name the close call. In the live test with illustrative scores, the first segment stayed first unless "competition" rose above 0.36 from 0.15 or "payer route" fell below 0.04 from 0.35 (`examples/live/analytics_mcda_segments_illustrative.json`).

### Step 5. In scope and out of scope

Record the person's choice: segments in scope with their order and one reason each, and segments out of scope with one reason each. If the person has not chosen, show the ranking and ask; do not choose.

### Step 6. Draft the motion per chosen segment

For each in-scope segment, one row (proposed unless the person gave it):

| Cell | Content | Check |
|---|---|---|
| Channel | Direct, partner, or access-led (through a payer route) | A route-led motion names the route and its biller (for example the practitioner for DMHT, CP-US-59) |
| Offer | What the buyer gets | No price (Commercial pricing); no free item or service without the stop below |
| Proof before a meeting | What this buyer asks to see (for example DTAC and DCB0129 evidence for an NHS buyer, CP-UK-01, CP-UK-07; a BAA for a US health system, CP-US-44) | From the rows, not memory |
| Channel rules | The two or three rules that bind this motion | `channel-rules.md` row ids |
| Owner | The person's named owner | "Owner not named" if missing; a motion without an owner is dropped, as the register's method says |

Different segments get different motions unless the person decides otherwise; say so if two rows are the same.

### Step 7. Stops

State what stops, from `governance.md`: any free item to patients or providers; any payment tied to referrals, volume or outcomes (lay out the safe-harbor elements, each cited to its own row: CP-US-09 to CP-US-14, CP-US-25 to CP-US-28; cite CP-US-07 only for 'every condition must be met'; for any free item that could reach Medicare patients, add CP-US-34/35; mark each met, missed or `[GAP]`; never "protected"); any DiGA agreement with a drug or aid maker (CP-DE-07); any motion in which a drug maker is partner, co-promoter or supplier of free items (`drug-digital-combination.md`; AO 19-02 protects only its requestor, CP-US-43); prices; payer-facing wording.

## Build the output

Follow `assets/segment-choice-output.md`. Short mode: the ranking as scored, the close call, the in-scope and out-of-scope list, one motion row per chosen segment, the stops, and the record line. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Scores, weights, choice and owners are the person's, and the output says so.
- Every cell fact and every channel rule carries its row id.
- No price, no forecast of revenue or share, no promise that a route will pay.
- Stops listed; no arrangement called protected.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model ranks what was scored and drafts motions; it does not choose, set targets or name owners.
- Pricing and value messages: Commercial pricing (DH-02.01.3.1). Payer prices, codes and coverage: Market Access pack. Partner selection and deal structure: Commercial channel and partnership (DH-02.01.4.1).
- Drugs, biologics and wellness apps are out of scope.
