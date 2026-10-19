# B1 Site review and repair

Framework task: DH-02.02.1.2, Part B, task B1. Replaces the old register task "Deployment repair" (CF-12.02.02.1.2.3) and the judgment part of "Site score" (CF-12.02.02.1.2.2). The old one-line pass rule and miss owner become Steps 1 and 4.

## What this task delivers

Per site: the result against each rule the person set (from A1 and A2), the open items, a site score only if the person has a scale, labeled hypotheses for each miss with what would confirm them, candidate repairs labeled "proposed", a ranking of repairs the person scored, and for each open item the owner, limited-launch status and recheck date the person sets. It answers "which sites miss our rules, what stays open, who owns it, and what do we fix first?"

Why it matters: the register's rule is that a deployment is not closed while a day-one workflow item is open, and the bar is not rescored after go-live to make it pass. A repair list without owners and recheck dates is not a repair plan.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.2 Part B, Site review and repair |
| Workflow | The steps below |
| Knowledge | `references/repair-strategies.md`; `references/deployment-evidence.md`; A1 and A2 outputs |
| Tools | `analytics.rice` or `analytics.mcda` (counted, optional, Step 6); `verify.build_record` |
| Prompt | This guide |
| Template | `assets/site-review-output.md` |
| Input | The request and its context: A1 and A2 results, the person's rules and any site scale, owners, limited-launch decisions, recheck dates, scores for repairs |
| Governance | `references/governance.md`; the person decides, the connector ranks only their numbers |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## Read the request

- **Results.** From A1 and A2, or as the person gives them.
- **Rules.** The pass rule for the bar and targets for outcomes. Without rules, no verdict; ask.
- **Scale.** "Score our sites" needs the person's scale with definitions. Without one, show rules met and missed per site, no score.
- **Owners, limited launch, recheck dates.** Ask; never pick.
- **Mode.** Short for a direct question; full for a review pack.

## Workflow

### Step 1. Check against their rules (formerly "pass rule")

For each site and rule: the number, the rule, met or missed. With a scale, apply it exactly as defined and show the evidence ids behind each level. Never rescore the bar or move a baseline after go-live to make a site pass (register rule).

### Step 2. Open items

List open bar items and missed outcomes per site. Flag any open day-one workflow item: the deployment is not closed while it is open (register rule).

### Step 3. Hypotheses, labeled

For each miss, one or two hypotheses from `repair-strategies.md` section 1, labeled "hypothesis", with the record that would confirm each. CFIR and NASSS name what to check; they are not causes (CS3, CS51).

### Step 4. Owner, limited launch, recheck (formerly "miss owner")

For each open item: the owner (use the owner or role the person names, in their words; only if they named none, write 'owner not named' and ask; never suggest a job title), whether the site stays in limited launch (the person's decision, facts in `repair-strategies.md` section 4), and the recheck date (the person's; blank until given).

### Step 5. Candidate repairs, proposed

Map each miss to ERIC strategies (`repair-strategies.md` section 2) with rows, labeled "proposed". Say where a repair is only more training for a workflow fault: training is the weakest control and decays (CS77, CS78).

### Step 6. Rank what they scored (optional)

If the person wants an order, ask for their numbers. RICE: `analytics.rice {initiatives: [{id, reach, impact, confidence, effort}]}` with confidence as a percent (0 to 100), not a fraction (`references/tools.md`). Or MCDA with their criteria, weights and 0 to 4 scores. Report the ranking as the result of their numbers and what change would swap the top two. Never fill a number.

### Step 7. Stops

List what stops: telling the customer a site is live or performing; closing the deployment with a day-one item open; staff-identifying reports; outcome-linked credits or penalties (Market Access); anything free to lift usage (compliance owner). Draft only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/site-review-output.md`. Answer first: the sites that miss the person's rules and the open day-one items. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every verdict uses the person's rule; every score uses the person's scale.
- Every hypothesis is labeled and has a confirming record.
- Every repair is "proposed"; every ranking is of the person's numbers.
- Owners, limited launch and recheck dates are the person's or blank.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Deployment review and repair. Training redesign is DH-02.02.4.x; renewal risk and customer health are DH-02.02.2.x and DH-02.02.3.x; outcome-linked payments are Market Access.
- No staff ranking; no clinical judgment on the product.
