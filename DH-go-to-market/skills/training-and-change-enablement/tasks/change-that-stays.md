# B1 Change that stays

Framework task: DH-02.02.4.1, Part B, task B1. Replaces register task CF-12.02.02.4.1.3 "Change that stays" and the earlier one-line pass rule and owner sections.

## What this task delivers

A change plan: the old step or workaround that should stop, who checks after a number of days the person sets, what happens if it did not stop, and the enablement options laid out with sourced facts (including the design option beside every training option), scored by the person and ranked by the connector, with where a weight change would flip the order, the sequence by dependency, and the stops. It answers "how do we make the old way stop, and which enablement step comes first?"

Why it matters: enablement that ends at the session leaves the old step in place (register CF-12.02.02.4.1.3). For use-related problems, design comes before training in FDA's order of preference (UX-US-33), because training depends on memory and decays (CS77, CS78). Choosing a refresher course by habit locks in the weakest option.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.1 Part B, Change that stays |
| Workflow | The steps below |
| Knowledge | `references/enablement-strategies.md`; `references/training-rules.md` section 3; A1 task cards; A2 coverage; sibling adoption-monitoring results if present |
| Tools | `analytics.mcda` (counted); `verify.build_record` (counted, on release) |
| Prompt | This guide |
| Template | `assets/change-that-stays-output.md` |
| Input | The request and its context: the old step, the site, the options the person is weighing, their criteria, weights and scores, who checks and after how many days, the accountable owner |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides; payments to champions or patients stop for compliance |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people score

The person chooses the criteria, sets the weights and scores each option. The model lays out the sourced facts per option so the scoring is informed, runs the ranking, and shows where the order is fragile. It never scores, never fills a missing score, and never calls an option "recommended". A proposal, if asked for, is labeled "proposed" with the facts behind it.

## Read the request

- **The old step.** The workaround or old system that should stop (a paper log, a phone list, a spreadsheet, the old screen). If not named, ask.
- **The check.** Who checks, after how many days, and what happens if the old step is still in use. All three are the person's. If missing, leave blank and ask.
- **Options.** Take the person's. If they have none, offer a starting list from `references/enablement-strategies.md`, labeled "starting list": a design or workflow change; ongoing or dynamic training; train-the-trainer; champions and early adopters; audit and feedback; formal commitments; staged scale-up.
- **Criteria and weights.** Ask. Offer criteria names only as examples phrased so that higher is better (the connector treats every criterion that way, `references/tools.md`), for example "use-error risk addressed", "users reached", "effort avoided", "resistance to decay".
- **Owners.** Who decides and who owns each option. If not named, "owner not named"; ask.

## Workflow

### Step 1. Name the change

Write the old step, the new step (from the A1 task card), who checks, after how many days, and what happens if it did not stop (register CF-12.02.02.4.1.3). Blank fields stay blank with "ask".

### Step 2. Lay out the facts per option

For each option, list the sourced facts with rows, no scores. Always include:

- design or workflow change: first in the order of preference for use-related problems (UX-US-33); owned by the design owner, and for a device it may need the regulatory owner (UX-US-49);
- any training option: training depends on memory and decays (CS77, CS78); "additional training" alone is not accepted in a submission without data (CS79);
- train-the-trainer and champions: definitions only (CS45, CS46, CS8); no row gives an effect size;
- audit and feedback: needs measures defined first (CS44, CS42), which the sibling adoption-monitoring skill produces;
- staged scale-up and trialability: start small and be able to reverse (CS47, CS5).

If any option pays or gives something of value to clinicians, champions or patients, mark it "stops for compliance" and lay out the CP rows from `governance.md`.

### Step 3. Collect the person's scores

Ask for scores on a 0 to 4 scale (the connector's scale) and weights that sum to 1. Write them back for confirmation. A missing score stops the ranking for that option; say which.

### Step 4. Rank what they scored

Call `analytics.mcda` with `alternatives` (id and scores) and `criteria_weights`. Report each option's value and the largest contribution. Work out the smallest weight change that flips the top two (method in `references/tools.md`) and say it in plain words.

### Step 5. Sequence by dependency

From "Sequencing by dependency" in `references/enablement-strategies.md`, write which step blocks which, with the reason and row. No dates and no urgency.

### Step 6. Stops and owners

List what stops: the choice itself (the person's owner); clinician-facing material (editorial owner); training as a risk control or any training change for a device (regulatory and design owners); payments or gifts (compliance or legal owner); labor or union communications. Name owners as the person gave them, or "owner not named".

## Build the output

Follow `assets/change-that-stays-output.md`. Answer first: the old step and its check, then the ranked result of the person's scores and how robust it is, then the first step in the dependency chain. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The check window, checker and consequence are the person's, or blank with "ask".
- A design option sits beside every training option.
- Every score and weight is the person's; the ranking is described as the result of their scores, never as a recommendation.
- No dates or urgency in the sequence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Enablement choices for the customer's rollout. The product design change itself belongs to the design owner and, for usability evidence, the UX pack; device questions to dh-regulatory-and-quality.
- Measuring whether the old step stopped over time is the sibling skill adoption-monitoring.
- Behavior-change mechanics inside the product belong to the digital therapeutic design pack.
