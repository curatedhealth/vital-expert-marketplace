# B2 Portfolio decision record

Framework task: DH-01.03.3.1, Part B, task B2. Replaces the old "Governance decision" task (CF-12.01.03.3.1.3) and keeps its method: for each item record continue, stop or delay; name who decided and the date; name the capacity the continue items consume; do not continue every item.

## What this task delivers

A decision record for one forum sitting: for each item, the decision as the person states it, the rule and rank it was taken against, any difference between the decision and what the rule implied (with the person's stated reason), the decider and date, the capacity the continue items use against the named capacity, conditions, dissent, and open items with owners. It answers "what did we decide, by what rule, and what does it commit?"

Why it matters: the sibling skill `product-portfolio-review` can only audit a decision that names its rule, rank, decision and person (old pass rule, CF-12.01.03.3.2.1). A continue with no rule or a stop with no record cannot be checked later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.1 Part B, Portfolio decision record (CF-12.01.03.3.1.3) |
| Workflow | The steps below |
| Knowledge | A1 and B1 outputs; `references/licensing-and-deal-flags.md`; `references/governance.md` |
| Tools | `scripts/portfolio_rank.py capacity` and `words`; `verify.build_record` once the named person clears it |
| Prompt | This guide |
| Template | `assets/decision-record-output.md` |
| Input | The request and its context: decisions per item, decider, date, attendees, dissent, conditions, capacity named, open items and owners as the person states them; A1 and B1 outputs |
| Governance | `references/governance.md`; the person decides; the model records |
| Catalogue job | none |

## The rule that shapes this task: record what was decided, as decided

The model writes the decision, decider, date and reasons exactly as the person gives them. It never decides, never names a decider or owner the person has not named, and never judges a decision that departs from the rule; it writes both side by side.

## Workflow

### Step 1. The rule and the rank

Bring the confirmed rule and the rank from B1. If there is none, say the record will show "no rule recorded" against each item (a fail under the review's pass rule) and offer B1 first.

### Step 2. Decisions per item

For each item, write the decision (continue, stop, delay, or the person's words) and the condition attached, verbatim. Where a decision differs from what the rule implied, write both, with the person's stated reason; if no reason is given, write "reason not given" and ask. Never fill.

### Step 3. Decider, date, attendees, dissent

Write them exactly as the person gives them. Missing: "not given"; ask. Dissent is written in the dissenter's words as the person gives them.

### Step 4. Capacity

With the capacity the person named (amount, unit, period) and each continue item's use, run `python3 scripts/portfolio_rank.py capacity FILE` (or sum by hand in the person's rank order). Report the total for continue items against the named capacity, and the first continue item past it, if any. Missing capacity: "capacity not given"; no check. If every item is continue, write that the old method's check ("do not continue every item") was put to the person and their answer.

### Step 5. Licensing and partnered items

For each continue item that rests on a license, partnership or acquisition, carry A1's flag block as an open item for the owner the person names for legal, or owner not named, with the facts that matter, each by source name and date then row: Regulation (EU) 2026/877 of 16 April 2026, in force 1 May 2026 (SP-135); the 20% combined (competitors) or 30% per-party (non-competitors) condition on any relevant market beside the person's figure or "not given" (SP-136); the transition to 30 April 2027 only for agreements in force on 30 April 2026 (SP-137); GDPR Article 9 if health data moves (DL-101, DL-105, DL-106). Add the company status line (`licensing-and-deal-flags.md` section 3, DL-135 to DL-168): the dated filings read for a covered company, or "Company status [GAP]: not read" with the filings to open; an unnamed licensor gets a request for its name. Deal facts for a memo route to `investment-memo-and-decision-record` (this pack). Never write that a license is exempt.

### Step 6. Open items

For each gap, unmet condition and legal flag: what it is, the owner the person names (or owner not named), what it blocks by dependency, and the date the person sets to read it again (or "reread date not given"; ask). The decider is not the default owner of an open item. These items feed `product-portfolio-review` (this pack).

### Step 7. Clear the record

If the record leaves the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by.name`. The model is never the clearer (`examples/live/verify_build_record_refusal.json`).

## Build the output

Follow `assets/decision-record-output.md`. Answer first: decisions by count (continue, stop, delay), decider and date, the capacity check, and the open item that blocks most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Before you hand it over

- Every decision, decider, date, reason and owner is the person's, and the record says so.
- Each item shows its rule and rank, or "no rule recorded".
- Capacity checked against the person's figure, or "capacity not given".
- Licensing items carry open items for the legal owner; no license called exempt.
- The record is labeled "decision record draft for the owner".
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model records; it does not decide, approve or veto.
- Auditing the decision later and repairing drift: `product-portfolio-review` (this pack).
- Stage gate records for the items: `dh-clinical-development` clinical-product-lifecycle-and-stage-gates.
- Any external wording (board, investors, partner, press) stops for the owner the person names.
