# B1 Scored comparison and decision record

Framework task: DH-DIL.3.1, Part B, task B1. The judgment step of the old "Compare a portfolio" skill: the ranking that skill could not make without the person's scores.

## What this task delivers

The person's criteria, weights and scores for the companies they compared, ranked with `analytics.mcda`, shown with the weights and scores beside the order; a check that the tool's values match the arithmetic; ties; the weight at which adjacent companies would swap; the companies not ranked and why; and a comparison record that writes down the person's decision, decider and date in their words. Never a recommendation.

Why it matters: a weighted sum looks precise but turns on the weights. Showing where the order flips tells the person how much their choice of weights is doing. The library's MCDA has no robustness view or tie flag (register C17), so the script supplies them.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old file: "Worker: not bound") |
| Skill | DH-DIL.3.1 Part B, Scored comparison and decision record |
| Workflow | The steps below |
| Knowledge | `references/comparison-rules.md` section 5; `references/governance.md`; A2's table |
| Tools | `analytics.mcda` (person's scores only); `scripts/portfolio_table.py swap`; `verify.build_record` once a named person clears the record |
| Prompt | This guide |
| Template | `assets/scored-comparison-output.md` |
| Input | The request and its context: the companies, criteria, weights, the person's scores (0 to 4, higher is better), any pass rule, the decision, decider and date if made |
| Governance | `references/governance.md`; no investment advice, no proposed scores in the tool |
| Catalogue job | none; the `partner-prioritization` job (Commercial) runs the same `analytics.mcda` step for partners and belongs to `dh-go-to-market` channel-and-partner-design |

## Read the request

- **Scores.** Each company needs a score for each criterion, from the person. If none: no ranking; show A2 and ask them to score. If one is missing: that company is "not ranked: score for CRITERION not given".
- **Scale and direction.** `analytics.mcda` takes 0 to 4 and treats every criterion as higher-is-better. If a criterion is a risk ("regulatory risk"), ask the person to rephrase it so 4 is best ("regulatory clarity") or to reverse their scores themselves; do not reverse them silently.
- **Weights.** Must sum to 1. If not, show the sum and ask.
- **Library fields as criteria.** If the person wants "evidence maturity" as a criterion, they turn the library score into a 0 to 4 score themselves; write their rule in their words.
- **Decision.** Record a decision only if the person states it, with the decider and date they give. Otherwise the record says "decision not given".

## Workflow

### Step 1. Check the input

Write the input as `{alternatives: [{id, scores}], criteria_weights}`, save it, and run `python3 scripts/portfolio_table.py swap FILE.json`. It stops on a missing score (the tool would refuse the whole call with HTTP 400) and warns on weights not summing to 1 or scores outside 0 to 4.

### Step 2. Call the library

`analytics.mcda {alternatives, criteria_weights}`. Save the response next to the input and rerun the script on the combined file to confirm "all values match".

### Step 3. Show the order with its basis

Order, value, and each company's scores and the weights beside it. Ties named. Swap points: "COMPANY A stays above COMPANY B unless WEIGHT moves above or below X". Every swap point is computed (quote the `swap` output, or show the arithmetic from the person's own weights and scores); never write "a small change could flip it" without the number. Name any pair where one company scores at least as high on every criterion: that order holds at any weights (the script prints these as "Dominance"). Label: "The order is your scores and weights, computed; it is not a recommendation to invest, pass or price."

### Step 4. Pass rules, if the person gave them

Check each company against the person's pass rule exactly as written ("no company with a recall flag in the last N years", where N is theirs). Mark "meets", "does not meet" or "cannot tell from the record". Never add a rule.

### Step 5. The record

Write the comparison record: companies, sources and retrieval dates, each company's status line from the status step (`references/company-status.md`: a filing or register read with its date, or "`[GAP]`: not read" with the filings to open), criteria and weights (the person's), scores (the person's), the computed order, swap points, companies not ranked, pass-rule results, the decision as stated, the decider and the date as given, open questions. Transaction or data rule facts the person raised are listed with their rows and routed to the owner the person names for legal or compliance questions (or owner not named); the record never says a deal is clear.

## Build the output

Follow `assets/scored-comparison-output.md`. Answer first: the computed order, how solid it is (the nearest swap point), and the decision if the person made one. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every score and weight is the person's; none was proposed into the tool.
- The tool's values match the script's arithmetic; ties and swap points are shown.
- No sentence recommends investing, passing, a valuation, a price or a return.
- The decision, decider and date are the person's words, or "not given".
- A declined invest, pass or valuation question still gets the facts-only record labeled "draft for the owner".
- The words were counted with the script and are at or under 450 in short mode.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The investment memo built on this comparison: `investment-memo-and-decision-record` (this pack).
- Whether the thesis still holds later: `thesis-and-memo-monitoring` (this pack).
- Deal clearance (HSR, CFIUS, DOJ bulk data, EU and Swiss screening): the owner the person names for legal or compliance questions (or owner not named).
