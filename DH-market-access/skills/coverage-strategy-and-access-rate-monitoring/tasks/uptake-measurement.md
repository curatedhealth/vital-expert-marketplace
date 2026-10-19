# A2 Uptake measurement

Framework task: DH-03.01.4.2, Part A, task A2.

## What this task delivers

A stage-by-stage picture of how many eligible patients actually get, start and keep using the product in each covered market, built from the person's own data, with official national figures beside it for context. It answers "is coverage turning into patients using it, and where do they drop out?"

Why it matters: a listing is a right to be paid, not a patient. In Germany 18 percent of issued DiGA codes were never redeemed, and 83 percent of people did not use a DiGA again after the usual 90 days. Where a product loses its patients decides what to fix.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.2 Part A, Uptake measurement |
| Workflow | The steps below |
| Knowledge | `references/uptake-measures.md` (stages, definitions, national figures); `references/access-after-listing.md` (how access works per country) |
| Tools | None from the library: it holds no uptake data. `scripts/access_funnel.py` (optional) |
| Prompt | This guide |
| Template | `assets/uptake-output.md` |
| Input | The request and its context; the person's counts per market and period (a table, a file, or numbers in the message); A1 output if present, for which markets are covered |
| Governance | `references/governance.md`; the person's data stays in the conversation |

## Read the request

- **Which markets and periods.** Only markets where the product is covered (A1, or the person's statement).
- **What data they have.** Ask for counts per stage in the form they hold them. Do not ask for patient-level data; aggregates are enough and safer.
- **Mode.** Short for a direct question, full for a report.

## Workflow

### Step 1. Agree the stages

Propose the stages for each market from `references/uptake-measures.md`, using that country's access mechanics (for Germany: prescribed or approved, code redeemed, still using, repeat prescription). Let the person rename, merge or drop stages to match their data. Write the agreed definition of each stage in one line, including what counts as "still using" (for Germany, the official dropout definition is three weeks without use for products used 90 days or more).

### Step 2. Take the counts

Put the person's numbers into one table: market, period, count per stage. Blank means not measured; mark it `[GAP]` and say who would hold it. Check the numbers make sense (a later stage larger than an earlier one usually means different periods or units; ask).

### Step 3. Compute conversion

For each market and period, compute each stage as a share of the stage before it, and of the first stage. With code execution, run `scripts/access_funnel.py` on a CSV of the counts. Name the stage with the largest drop.

### Step 4. Put national figures beside it

Add the official figure for the same stage and market where one exists (`references/uptake-measures.md`), labeled with its period and base. Where the base differs from the person's stage, say so. Where none exists, say "no official figure".

### Step 5. What each drop means

Say what each drop costs, using sourced mechanics from `references/access-after-listing.md` and `references/lapse-signals.md`, not opinion. For Germany: the manufacturer can bill only once the code is redeemed, so unredeemed codes are unpaid prescriptions; since 1 January 2026 at least 20 percent of a negotiated price depends on outcomes, and from 15 April 2027 permanent DiGA report usage and dropout, so early dropout will become visible to payers. Keep it to facts that follow from the rules.

### Step 6. Name the next measurements

List the two or three measurements that would locate the loss more precisely, for example: codes issued by the fund (splits "never sent to the fund" from "issued but not redeemed"), prescribed versus approved, days from prescription to activation, and the week in which users stop. These are the inputs B1 needs to test hypotheses.

### Step 7. Trend

If more than one period is given, show the change per stage. Do not extrapolate.

## Build the output

Follow `assets/uptake-output.md`. Answer first: the market and stage where most patients are lost, with the number and what that loss costs. Then the funnel table per market, the national context, the next measurements, and the gaps in the data.

## Before you hand it over

- Every count is the person's; every national figure has its source, period and base.
- No cause is stated for a drop. Possible causes go to B1 as hypotheses.
- Units are not mixed.
- Confidential figures are not put into any tool call or shared record without the person's say.

## Boundaries

- Measurement only; no judgment of pass or miss (that is B1, against the person's rules).
- Uptake is use, not clinical effect.
- Drugs, biologics and wellness apps are out of scope.
