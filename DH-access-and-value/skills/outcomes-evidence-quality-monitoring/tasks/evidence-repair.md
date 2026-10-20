# B1 Evidence repair

Framework task: DH-01.07.3.2, Part B, task B1. Replaces the earlier "Evidence repair" section (CF-12.01.07.3.2.3), and carries the evidence rule ("pass rule") and the gap owner ("miss owner") as steps.

## What this task delivers

A repair draft for the evidence behind a decision: each result checked against the evidence rule the person sets, the weakest point named, the repair options that can and cannot fix it with their rows, the work each option belongs to, and the owner the person names. It answers "is our evidence good enough for what we want to do with it, and if not, what would fix it and who owns that?"

Why it matters: some weaknesses can be repaired by analysis or disclosure; some cannot be repaired at all without a new study (prespecification after the fact, critical risk of bias). Knowing which is which saves a re-analysis that changes nothing (HE-026, ES-77).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.2 Part B, Evidence repair |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/repair-routes.md`; `references/rigor-checks.md` |
| Tool | A1 and A2 if not yet run; `verify.build_record` for sign-off |
| Catalogue job | none |
| Prompt | This guide |
| Template | `assets/evidence-repair-output.md` |
| Input | The request; A1 fact sheets and the A2 tally; what the evidence is for (internal decision, NICE, EU JCA, payer); the person's evidence rule and named owners |
| Governance | `references/governance.md`; people set the rule and name owners; dossier decisions stop for the owner |

## Read the request

- **What the evidence is for.** It decides which rows matter (RoB 1 for JCA randomized results, ES-163; ROBINS-I at outcome level, ES-164; NICE validated tool, ES-131).
- **The rule and the owners.** Whether the person has them. If not, Step 2 writes them.
- **What exists.** A1 and A2 outputs in the conversation, or papers and judgments to run them.

## The rule that shapes this task: people judge

The person writes the evidence rule in their own words and names an owner for each gap. The model checks results against that rule, names the weakest point, and lays out repair options with their rows. It never sets the rule, never says a study is good enough for an HTA body, and never names an owner the person has not named. Any suggested rule is marked "proposed" and not applied until confirmed.

## Workflow

### Step 1. Gather the evidence

Use A1 (facts per domain, prespecification, currency) and A2 (overall levels under the person's rule). If missing, run them first in short mode. A repair plan without A1 says the facts were not checked.

### Step 2. Write the evidence rule with the person

Offer this shape, filled in their words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Overall level | "No result we cite at serious or critical risk" | A2 |
| Prespecification | "Primary results prespecified, with a public protocol" | A1 step 4 |
| Currency | "No retracted or corrected paper uncited" | A1 step 5 |
| Data fitness | "Outcome definitions validated against a reference" | A1 step 4 |
| Independence | "Funder's role stated" | A1 step 5 |

Write the rules and owners back for confirmation before checking.

### Step 3. Check each rule

Met, not met, or not measurable `[GAP]`, each with the fact behind it. A result at critical risk is excluded from any synthesis regardless of the rule (ES-77).

### Step 4. Find the weakest point

Name the first rule that fails for the result that matters most to the decision, and whether it is a design weakness (fixed only by a new study) or a disclosure or analysis weakness (repairable now). Use `references/repair-routes.md`, "What cannot be repaired after the fact", first.

### Step 5. Lay out repair options, not a choice

For each weakness, list the options from `references/repair-routes.md` with rows, what each would change, and what it would not. Label likely causes as hypotheses, never findings.

### Step 6. Route and name owners

Each option goes to the work that can deliver it: a new study (`real-world-outcomes-research`), a deviation statement and sensitivity analysis (the study team), a review update (dh-clinical-development `literature-and-real-world-evidence-review`), an economic model change (dh-access-and-value 2.x), a submission change (dh-access-and-value `payer-engagement-and-hta-submission`). Name the owner the person gave; if none, "owner not named" and ask.

## Build the output

Follow `assets/evidence-repair-output.md`. Short mode: the answer (rule met or not, the weakest point, whether it is repairable now or needs a new study, the decision needed), one table of rules with fact, verdict and owner, at most three repair options, the record line. Full mode adds the per-result table, all repair options with rows, routing and the certainty context.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the fact behind it, from A1 or A2.
- Unrepairable weaknesses are named as such; no re-analysis is offered as a fix for prespecification.
- Dossier inclusion, submissions and external wording stop for the owner the person names, or owner not named.
- Every [PAPER] row carries its DOI beside the row id (ES-75: 10.1136/bmj.i4919; HE-025 to HE-030: 10.1002/pds.4297).
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- The model checks and structures; it does not judge people, teams or authors.
- No forecast of how an HTA body or payer will rate the evidence.
- Drugs, biologics and wellness apps are out of scope.
