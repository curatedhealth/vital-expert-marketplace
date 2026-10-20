# A2 Data completeness check

Framework task: DH-03.01.1.2, Part A, task A2.

## What this task delivers

A count of what is missing (baselines, follow-up values, values outside the window, self-reported values the contract does not accept, patients lost to follow-up), and what each gap does to attainment under the contract's rules. It answers "how much of our result is data rather than outcome, and where is the data being lost?"

Why it matters: under a patient-level all-or-nothing rule with dropouts in the denominator, every missing value is a failure. Under a population-average rule, missing values drop out and can flatter the result. Either way, the result cannot be read without knowing the completeness behind it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.2 Part A, Data completeness check |
| Workflow | The steps below |
| Knowledge | `references/data-completeness.md` (checks, rule effects, self-report limits); `references/attainment-rules.md`; `references/access-monitoring-sources.md` rows DE-16 to DE-19 for DiGA outcome measurement |
| Tools | `scripts/attainment.py` (completeness table and the two-way rate); no library call |
| Prompt | This guide |
| Template | `assets/data-completeness-check-output.md` |
| Input | The request and its context; the contract's rules (from A1 if run); the person's de-identified patient data, ideally with collection days and a self-report flag |
| Governance | `references/governance.md`; no imputation; patient data stays in the conversation |

## Read the request

- **The rules for missing data.** Missing counts as failure, or is excluded? Lost and unaligned patients in or out of the denominator? Windows for baseline and final values? Self-report allowed for which measures? If A1 ran, reuse its rules.
- **What the data can show.** Without collection days, window checks are impossible; without a self-report flag, self-report checks are impossible. Say so as `[GAP]` and name who holds the field.
- **For a DiGA.** Whether the product is in AbEM scope (permanent listing; DE-17) and whether PROM items are voluntary in the person's workflow (they are under DiGAV § 23a).

## Workflow

### Step 1. Count completeness per measure

Patients; baseline present; baseline on time (for ACCESS, within 60 days); final present; final in window (for ACCESS, by day 425); both present; self-reported finals; required measures with no column in the data (for ACCESS BH, PGIC); unalignment reason per unaligned patient; values older than their validity window (for ACCESS BP, weight and PROMs, 15 days). `scripts/attainment.py` prints the first columns; add the timing checks by hand if the person gives collection dates.

### Step 2. Count status

Active, completed, lost to follow-up, unaligned. State whether the contract keeps each in the denominator.

### Step 3. Show the effect on attainment

Report the attainment rate two ways: under the contract's missing-data rule, and under the other treatment (`scripts/attainment.py` prints both). The difference is what completeness is worth under this contract. Under a patient-level rule, say how many failures are missing data and how many are targets not met. Under a population rule, say how many values dropped out of each average and that selective dropout can raise it.

### Step 4. Locate where data is lost

Group the missing values by stage: never baselined, baselined but no final, final out of window, final self-reported where not allowed. Name the stage with the most loss. For DiGA PROMs, note that participation is voluntary and only one reminder is allowed, which bounds what follow-up can recover (OC Germany "AbEM: voluntary patient participation").

### Step 5. Self-report limits

List measures where finals were self-reported, and whether the contract (or ACCESS, if it applies) accepts self-report for them. Flag any measure where accepted self-report is the only verification, as a question for the contract owner.

### Step 6. Name the next measurements

Two or three fields that would make the next check sharper (collection date per value, self-report flag, reason for loss to follow-up). These feed B1's hypotheses.

## Build the output

Follow `assets/data-completeness-check-output.md`. Answer first: how many of the failures are missing data, the rate both ways, and the stage where most data is lost.

## Before you hand it over

- No value imputed; no patient dropped that the contract keeps.
- Every rule cited as the contract's or as a public rule the contract uses, with its row.
- No cause stated for missing data; possible causes go to B1 as hypotheses.
- Patient-level rows stay in the conversation.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Measurement only; no pass or miss verdict (that is B1).
- Missing data is not evidence about the product's effect.
- Drugs, biologics and wellness apps are out of scope.
