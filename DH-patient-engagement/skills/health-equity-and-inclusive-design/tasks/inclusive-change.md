# B1 Inclusive change

Framework task: DH-02.03.4.1, Part B, task B1. Replaces the earlier "Inclusive change" section (CF-12.02.03.4.1.2) and folds in the owner rule.

## What this task delivers

A decision draft: for a group the person can see, the barrier at the step, the change options with their sourced basis, the person's scores and the ranking from them, the change the person picks, the version that carries it, the owner, and what the sibling monitoring skill will need to check that it reached the group. It answers "which change do we ship, for which group, in which version, owned by whom?"

Why it matters: a change with no version does not ship, and a change with no evidence definition cannot be shown to have reached anyone. The register's method: state the group and the barrier at that step, state the change, name the version that carries it; never propose a change that cannot ship in a named version.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Health Equity & Digital Access Lead (`health-equity-access-lead`) |
| Skill | DH-02.03.4.1 Part B, Inclusive change |
| Workflow | The steps below |
| Knowledge | A1 output; `references/inclusive-change-and-partners.md`; `references/equity-frames.md`; PE rows |
| Tools | `analytics.mcda` (counted) for options the person scored; `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/inclusive-change-output.md` |
| Input | The request and its context; A1 (group, step, barrier); the person's options, criteria, weights, 0 to 4 scores, owner and version |
| Governance | `references/governance.md`; people score, choose, own and set the version |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people score, choose and own

The model lays out the options with their basis, ranks only what the person scored, and labels any suggestion "proposed". The owner and the version are the person's. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Workflow

### Step 1. Group, step, barrier

Take them from A1. If A1 is not in the conversation, ask for the three in one line each and note "A1 not run". A group the data cannot see goes to A2, not here: the register's change is "for a group you can see".

### Step 2. Options with their basis

List the person's options. If they have none, list change types from `references/inclusive-change-and-partners.md` that answer the barrier, each labeled "proposed" with its row (for example human review of machine-translated clinical text, PE-108). For accessibility fixes, point to the dh-user-experience accessibility skills for the conformance work.

For each option, lay out the facts the person needs to score: the barrier it answers, the row behind it, whether a duty may attach (with "if your legal owner treats you as covered"), what the person said about effort, and what evidence exists. No score from the model.

### Step 3. Criteria, weights, scores (the person's)

If the person wants a ranking, ask for criteria phrased so higher is better ("group reach expected", "effort avoided"), weights summing to 1, and 0 to 4 scores per option. Then call:

```
analytics.mcda {alternatives: [{id: "<option>", scores: {"<criterion>": <0-4>, ...}}, ...], criteria_weights: {"<criterion>": <weight>, ...}}
```

Report each `value_estimate` and its `contributions`. The tool returns no robustness view: if two options are close, say which criterion's contribution separates them and that a different weight could change the order; compute a swap weight only if you show the arithmetic. Without scores, no ranking.

### Step 4. The choice, the version, the owner

Record the option the person picks, the version or release that carries it, and the owner. Missing: "version not set" or "owner not named"; ask. No dates proposed by the model.

### Step 5. What monitoring will need

Write the evidence definition the sibling skill (`health-equity-monitoring`, A1) will check: the change, the group, the record that shows use (for example "enrollment completed with the Spanish flow"), the denominator (the group's eligible count), and the first period. Mark anything the person's systems do not record as `[GAP]`.

### Step 6. Stops

State what stops for the accountable owner: any public claim that the change makes the product accessible or equitable; any statement of Section 1557 compliance; any partner payment or free item to patients; any DAP content. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/inclusive-change-output.md`. Answer first: the change the person chose (or the top-ranked option on their scores), the group, the version, the owner, and the one decision still open. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every score, weight, choice, owner and version is the person's, and the output says so.
- Every option has its basis (a row, or "your evidence").
- The ranking is reported with values and contributions, from the tool, on the person's scores only.
- The evidence definition for monitoring is written.
- No equity, accessibility or compliance claim. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Does not build the change, test conformance or judge mitigation adequacy under 92.210.
- Pricing, coverage and reimbursement effects of a change are dh-market-access.
- Usability evidence for the changed flow is dh-user-experience 4.x.
