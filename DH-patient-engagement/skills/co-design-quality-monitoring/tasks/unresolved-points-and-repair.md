# B1 Unresolved points and repair

Framework task: DH-02.03.1.2, Part B, task B1. Replaces the register task "Unresolved point" (CF-12.02.03.1.2.3) and the old one-line pass rule and miss owner sections.

## What this task delivers

The repeated points that are still undecided or whose records miss the person's rules, each with its count, age since first capture, the owner the person names and the date the person sets for writing the decision; the trace and fit results from A1 and A2 checked against the person's rules; repairs laid out, labeled "proposed" unless the person chose them; a ranking only on the person's scores; and the stops. It answers "what is still open, who decides it, and what do we fix in how we run co-design?"

Why it matters: a repeated point left only in the transcript is lost (R-24). Without an owner and a date the person sets, the point has no path to a decision (R-23, R-15). A point that touches a safety constraint needs its owner, not a quiet default (R-13).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.2 Part B, Unresolved points and repair |
| Workflow | The steps below |
| Knowledge | `references/quality-criteria.md` (section 4 and R rows); A1 and A2 results; rows R-10, R-13, R-15, R-22 to R-24 |
| Tools | `scripts/insight_tracker.py` (`tally`, `status`); `analytics.rice` or `analytics.mcda` (counted, optional, on the person's scores); `verify.build_record` (counted, when cleared) |
| Prompt | This guide |
| Template | `assets/unresolved-points-output.md` |
| Input | The request and its context: `insights.csv`, `captures.csv`, the as-of date, the person's rules (repeated point, maximum age undecided, trace coverage, participant mix), owners, scores for repairs if they want a ranking |
| Governance | `references/governance.md`; people set rules, owners and dates; the connector ranks only scored items |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## Read the request

- **As-of date.** Ages count to it. Default to the date of the conversation and say so.
- **Their rules.** Repeated-point rule (offer R-10), any maximum time a repeated point may stay undecided, any trace coverage rule from A1, any participant rule from A2. Without rules, report numbers and no verdict.
- **Owners.** Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- **Dates.** The person's. Propose none.
- **Mode.** Short for a direct question; full for a review.

## Workflow

### Step 1. Find the unresolved points

Run `python3 scripts/insight_tracker.py tally captures.csv --repeat N` (the person's N) and `status insights.csv captures.csv --as-of YYYY-MM-DD`. List each repeated point whose status is open, with the count and sessions (R-22), age since first capture, owner (R-23) and decision date (R-15). Add points that exist only in captures with no insight id: these are at risk of staying in the transcript (R-24).

### Step 2. Check against their rules

For each rule the person set, mark pass or miss with the number: for example "I4 open 76 days; your rule: decided within N days; miss if 76 is more than N". Carry in the A1 and A2 results the person wants checked. Without a rule: "no rule set".

If the person's rule counts days from first capture, say once which start you used and, where a point met the repeated rule later than its first capture, give both ages (from first capture and from the capture that made it repeated) and ask which the person means. The start point is the person's.

### Step 3. Causes are hypotheses

Where a miss has a likely cause in the records (no owner named, a safety-touching point waiting on its owner, a point raised only by staff), state it as a hypothesis with what would confirm it. Never state a cause as fact.

### Step 4. Repairs

Lay out repairs that respond to each miss, labeled "proposed": for example "name an owner for I7", "add backlog dates to the changes file so A1 can check R-14", "add a planned carer seat to the next session". Repairs touch the process and the records, not the product decision itself.

### Step 5. Rank only what they scored (optional)

If the person wants an order, ask for RICE inputs (confidence as a whole-number percent) or 0 to 4 scores and weights. Call `analytics.rice` or `analytics.mcda` (read `references/tools.md`). Report the order as the result of their scores, never as a recommendation.

### Step 6. Stops and owners

List: safety-touching open points (R-13) to the clinical safety or risk owner the person names; any "co-designed" public wording to its owner; any participant payment in the records to the compliance owner. Owners as named, or "owner not named".

## Build the output

Follow `assets/unresolved-points-output.md`. Answer first: the open repeated points with age and owner, and which of the person's rules are missed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner, date and score is the person's, and the output says so.
- Causes are labeled hypotheses; repairs are labeled proposed.
- No decision on a point is made by the model.
- Safety-touching points are stops.
- If it leaves the conversation, ask who clears it and call `verify.build_record` with ids only; otherwise label it an uncleared draft.

## Boundaries

- The co-design process and its records. Product decisions on points are made through the sibling skill's B1 by the person's owners.
- Engagement program results go to `engagement-and-advocacy-impact-monitoring`; KPI reliability to `kpi-reliability-monitoring`.
- Clinical safety, human factors and regulatory conclusions belong to their owners and packs.
