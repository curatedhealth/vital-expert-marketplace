# A2 Implementation outcomes

Framework task: DH-02.02.1.2, Part A, task A2. Takes the measurement part of the old register task "Site score" (CF-12.02.02.1.2.2).

## What this task delivers

Implementation outcomes per site, computed from the person's own site file and milestone file, each with a named definition and row: setting adoption, patient and provider penetration, usage against the profile agreed at commissioning, fidelity to the milestone plan (all and core), milestone and go-live slippage, months since go-live; pooled figures beside per-site figures; data checks. It answers "how is the rollout going, in numbers?"

Why it matters: implementation outcomes are preconditions for clinical or service outcomes (CS32). A site with 20 percent of eligible patients using the product cannot show the product's effect, and saying so separates a deployment problem from a product one.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.2 Part A, Implementation outcomes |
| Workflow | The steps below |
| Knowledge | `references/outcome-definitions.md`; CS rows |
| Tools | `scripts/implementation_outcomes.py`; `verify.qualify_source` and `verify.check_claim` (counted, optional, Step 5) |
| Prompt | This guide |
| Template | `assets/implementation-outcomes-output.md` |
| Input | The request and its context: the site file and milestone file (aggregates, columns in the script header), the as-of date, the usage profile agreed at commissioning, any targets the person set |
| Governance | `references/governance.md`; the person's data stays in the conversation; usage is not clinical evidence |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Data.** A site file (one row per site approached) and, for fidelity and slippage, a milestone file with the baseline dates the site agreed. Columns are in `scripts/implementation_outcomes.py`. A table in the message works too. Aggregates only: counts of eligible and active patients, never patient lists.
- **Denominators.** Eligible patients means the eligible population at the site, not those who expressed interest (CS27). Providers expected means trained in or expected to deliver (CS39). Ask how they counted.
- **Usage profile.** The expected usage agreed at commissioning and its unit (CS61). Without it, usage has no reference: `[GAP]`.
- **As-of date.** Default to the conversation date and say so.
- **Their targets.** Ask. Without targets, numbers and no verdict.
- **Mode.** Short for a direct question; full for a portfolio review.

## Workflow

### Step 1. Take the data and check it

Put the person's figures into the two files. The script flags active above eligible and delivering above expected; resolve these before reporting. A blank is "not measured `[GAP]`" with the record that would hold it.

### Step 2. Compute

With code execution: `python3 scripts/implementation_outcomes.py SITES.csv --milestones MILESTONES.csv --as-of YYYY-MM-DD`. Without it, compute by hand with the formulas in `outcome-definitions.md`. Report per site, with the definition used:
- adoption at setting level (CS28);
- patient penetration (CS39, first formula) and provider penetration (CS39, second formula);
- usage against the agreed profile (CS61);
- fidelity to plan and core fidelity (CS9, CS4, CS48);
- go-live and milestone slippage from baseline, and the count of re-baselined milestones;
- months since go-live.

### Step 3. Pooled beside per site

Give the pooled penetration and the site range, never a single average score. Name the definition used where terms overlap (penetration versus reach; adoption's two definitions).

### Step 4. Against their targets, if any

For each target, met or missed. Without a target, "no target set". Published or other customers' figures are context, never targets.

### Step 5. Published definition check (optional)

If the person needs a definition checked against its paper for an external document: `verify.qualify_source {doi: "10.1007/s10488-010-0319-7"}`, then `verify.check_claim` with the passage quoted in CS39. Read `references/tools.md`: Verify returned "supported" for a distorted claim, so read the passage yourself.

### Step 6. What it means for the person

Two or three consequences, conditional and from the rows. Examples: "At Clinic D, 58 of 290 eligible patients used the product; outcome data from that site describe a fifth of its eligible population (CS32, CS39)." "Clinic E is 42 days past its agreed go-live date with configuration open; training scheduled after it will move too."

## Build the output

Follow `assets/implementation-outcomes-output.md`. Answer first: the two or three figures that stand out, with numbers and the as-of date. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number is from the person's data or the script run on it.
- Each outcome names its definition and row.
- No cause stated; causes are hypotheses for B1.
- No usage figure presented as clinical benefit, savings or reimbursement proof.
- No sites averaged into a score.
- The person's data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Implementation outcomes only. Patient-reported and clinical outcomes the customer agreed to see are Customer Health & Value Realization (DH-02.02.3.x); outcome-linked payments are Market Access (outcomes-contract-monitoring).
- Training effectiveness is DH-02.02.4.2.
