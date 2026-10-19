# A2 Contract performance

Framework task: DH-03.01.2.2, Part A, task A2 (old name: Contract Performance Monitoring).

## What this task delivers

From the person's own data, per contract, route or code and period: claims paid and denied, unresolved claims, realized versus agreed price, volume against discount tiers, and the outcome component at stake and earned. It answers "is the contract paying what we agreed, and where is money lost?"

Why it matters: a contract can look healthy at list level while denials, price leakage, a crossed discount tier or a missed outcome component take a share of every unit. Since 1 January 2026 at least 20 percent of a German DiGA amount depends on outcomes (DE2); in ACCESS half the Medicare portion is withheld until reconciliation (US32).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.2 Part A, Contract performance |
| Workflow | The steps below |
| Knowledge | `references/contract-measures.md`; `references/coding-pricing-sources.md`; `references/outcomes-contracting-sources.md` (cite only) |
| Tool | None from the library: it holds no claims or contract data. `scripts/contract_performance.py` |
| Prompt | This guide |
| Template | `assets/contract-performance-output.md` |
| Input | The request and its context; the person's counts and amounts per period; contract terms (agreed amount, tiers, outcome share and definition) |
| Governance | `references/governance.md`; the person's data stays in the conversation |

## Read the request

- **Contracts and periods.** Which payer, route or code, and which periods.
- **Data.** Ask for aggregates in the form held: claims submitted, paid, denied; amount paid; agreed amount per unit; units so far in the contract year; outcome share and attainment as the contract defines them. Never ask for patient-level data.
- **Contract terms.** The tiers and outcome definition come from the person's contract. If absent, say which statutory floors exist (DE2, DE3) and label them as statute.

## Workflow

### Step 1. Agree the measures

Propose the measures from `references/contract-measures.md`. Let the person drop or rename. Write each definition in one line, including the unit (claim, prescription, month).

### Step 2. Take the numbers

Put them in one table or a CSV with the columns in `scripts/contract_performance.py`. Blank is not measured: `[GAP]`, with who holds it (remittance advice, billing system, payer statement, outcome data provider). Check consistency: paid plus denied above submitted usually means different periods. Where an outcome share and attainment are given, compare realized per unit with agreed x (1 - share x payer portion x (1 - attainment)), where payer portion is 1 unless the outcome share applies to part of the amount (for ACCESS 0.8: the withhold is 50 percent of the Medicare portion, 80 percent of the allowed amount; outcomes file, "ACCESS: Medicare portion and payment basis"); if they differ, say so with both figures and ask whether the outcome settlement is inside the paid amount, paid later, or on another base. Do not report the price shortfall and the unearned outcome component as separate losses until this is settled.

### Step 3. Compute

Run `scripts/contract_performance.py data.csv` (add `--rules` when B1 has rules). Without code execution, compute the same formulas and show them. Name the largest loss in money terms where the data allows: denied claims, price shortfall (agreed minus realized times units), or outcome component not earned.

### Step 4. Put sourced rules beside it

For each measure, the rule that gives it meaning: the statutory outcome floor (DE2), volume floors from 1 January 2027 (DE3), ACCESS withhold and thresholds (US32, US33), G0552 contractor pricing (US19), Medicare amounts before geographic adjustment (US9). For realization against a Medicare national amount, say geographic adjustment alone can explain a difference.

### Step 5. Trend

If more than one period is given, show the change per measure. Do not extrapolate or forecast a tier crossing date.

### Step 6. Next measurements

Name at most three measurements that would locate the loss: denial reason codes, days to payment, attainment per outcome measure, units by month.

## Build the output

Follow `assets/contract-performance-output.md`. Answer first: where money is lost and how much, on the person's numbers.

## Before you hand it over

- Every figure is the person's or computed from theirs; formulas are shown.
- No verdict without a rule the person set (that is B1).
- Outcome-component attainment is described as a contract measure, not clinical evidence.
- Confidential figures are not put in any tool call or shared record.

## Boundaries

- Measurement only; pass or miss is B1.
- No legal reading of a contract clause; point to the person's counsel.
- Drugs, biologics and wellness apps are out of scope.
