# A2 Cohort renewal and expansion figures

Framework task: DH-02.02.2.2, Part A, task A2. Replaces the earlier "Cohort score" section (CF-12.02.02.2.2.2).

## What this task delivers

The figures for one period, computed from the person's account file on the definitions written in A1: the cohort and what was excluded, renewed, lost and open counts with contract ids, the account renewal rate, and, if value fields exist, starting value, value lost, contraction, expansion and value retained with and without expansion. Every number carries its formula and denominator. Losses are listed by recorded reason, kept apart. It answers "what are our renewal and retention numbers for this period, and how were they computed?"

Why it matters: a figure without its formula cannot be checked or repeated. Keeping open accounts and unclassified statuses visible stops a rate from improving because the hard cases were left out (SR18).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.02.2.2 Part A, Cohort renewal and expansion figures |
| Workflow | The steps below |
| Knowledge | `references/renewal-measures.md`; `references/reading-results.md` (reasons) |
| Tools | `scripts/renewal_metrics.py cohort` (local); no library call |
| Prompt | This guide |
| Template | `assets/cohort-figures-output.md` |
| Input | The request and its context: the account file, the A1 definitions file (or the definitions stated in the conversation), the period, the person's rules for each figure if any |
| Governance | `references/governance.md`; figures for a board, investors or customers stop for the owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## The rule that shapes this task: no definition, no figure

The script refuses to compute when a definition is missing and names it. Follow the same rule by hand. If A1 has not been run, run it in short mode first, or take the definitions the person states and write them into the card before computing. Never compute on an assumed definition.

## Read the request

- **Period.** Start and end dates in full.
- **Definitions.** From A1. If the person names a measure the definitions do not cover (for example "NRR including mid-term upsells"), stop and return to A1 for that measure.
- **Rules.** Any threshold or target the person holds for each figure. Without one, no verdict.
- **Mode.** Short for "what is our renewal rate"; full for a quarterly or annual review.

## Workflow

### Step 1. Run the computation

With code execution:

`python3 scripts/renewal_metrics.py cohort ACCOUNTS.csv DEFINITIONS.json`

Without code execution, compute by hand in the same order and show each count. Check: the counts of renewed, lost, open, excluded and unclassified add up to the accounts in the period.

### Step 2. Report the figures with their formulas

Report each figure exactly as computed, with the formula and the denominator, using the person's names for the measures. If the person calls "value retained with expansion" their NRR, write "NRR (your definition): (start - lost - contraction - open + expansion) / start = ...". Never round the formula away.

### Step 3. Show what sits outside the figures

List, with contract ids: excluded accounts and the rule that excluded them; open accounts and whether they are in the denominator; statuses the definitions do not cover (counted nowhere); open accounts past their renewal date (check the record); accounts with missing values (value figures not computed, `[GAP]`). If open accounts are in the denominator, also show each figure with the open accounts renewed at their current value, labeled 'if open accounts renew flat, for reading only'. This is arithmetic on the person's file, not a forecast.

### Step 4. Losses by recorded reason

List lost accounts with contract id, renewal date and recorded reason. Keep reasons apart, never merged: a loss on price is not a loss on an open implementation (SR17; CS32 [PAPER], DOI 10.1007/s10488-010-0319-7). Where no reason is recorded, `[GAP]`. Name where each reason routes, from `references/reading-results.md`, in one line each.

### Step 5. Check against the person's rules

For each figure with a rule, write met or missed. For figures without a rule, the number and "no rule set". No industry comparison: none is sourced.

### Step 6. Say what it means for the person

Two lines, from the computation only. Examples: "Open account ACC-08 holds 110,000 USD of the 765,000 USD base; until it signs, your definition counts it as not retained, which is about 14 points of value retention." "Both losses had different recorded reasons; neither repeats."

## Build the output

Follow `assets/cohort-figures-output.md`. Answer first: the account renewal rate and, if computed, value retained with and without expansion, each with its formula, plus the count of open and unclassified accounts. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every figure has its formula and denominator; the counts add up.
- Ask once for the person's pass rule for each figure if none was given (do not supply one).
- The definitions are labeled owner-stated (O).
- Open, excluded and unclassified accounts are listed, not dropped.
- No benchmark, no "good" or "bad" without the person's rule.
- No figure is presented as clinical or product effectiveness.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. Board or investor use stops for the owner.

## Boundaries

- Figures on the person's file only. The offer review is B1; running renewals is the sibling skill (`account-growth-and-renewal`).
- No revenue recognition or accounting judgment.
- Customer health and value realization are the Customer Health skills.
