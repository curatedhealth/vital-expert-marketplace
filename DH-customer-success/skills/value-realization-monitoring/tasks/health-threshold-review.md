# A1 Health threshold review

Framework task: DH-02.02.3.2, Part A, task A1. Replaces the earlier "Health threshold review" section.

## What this task delivers

A review of the person's health targets across periods and versions: per signal, how many accounts met the target each period; targets no account has met; signals with no data in the latest period or for some accounts; shares whose denominator is not the one the target needs; and every target change between versions with the accounts it turned to met. It answers "do our thresholds still match the offer, and has any change made accounts look healthier without anything changing?"

Why it matters: the register's rule is "Do not lower a threshold only to turn accounts green". A target eased after the results were seen changes the health read without any change in use or outcome. NICE asks that the usage profile be agreed at commissioning (CS61), so a changed profile is a change to what the customer agreed.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.2 Part A, Health threshold review |
| Workflow | The steps below |
| Knowledge | `references/value-evidence-rules.md`; `references/health-signals.md`; `references/outcome-measures.md` |
| Tools | `scripts/account_health.py thresholds` (no connector). No library call |
| Prompt | This guide |
| Template | `assets/health-threshold-review-output.md` |
| Input | The request and its context: the account file across at least two periods, the current target file, the previous target version if any (with dates and who set them), the product's stored fields |
| Governance | `references/governance.md`; the model shows changes and their effect; whether a change stands is the person's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Periods.** At least two, so "never met" and "no longer stored" mean something. With one period, say the review is a single-period snapshot.
- **Target versions.** Ask for the previous version and the date of each. Without it, changes cannot be shown: say so.
- **Stored fields.** The product's data dictionary or field list (NICE ESF Std 19 asks the company for one, CS64).
- **Mode.** Short for a direct question; full for a governance review pack.

## Workflow

### Step 1. Fix the frame

Write back: periods, accounts, current and previous target versions with dates and who set them. Confirm.

### Step 2. Compute

With code execution: `python3 scripts/account_health.py thresholds ACCOUNTS.csv --targets CURRENT.json --previous PREVIOUS.json`. Without it, compute by hand: per signal and period, accounts meeting the target of those measured; then flags; then, for each target that changed, accounts meeting it under the old and new value in the latest period.

### Step 3. Read the flags

For each flag, state the fact and its basis (`value-evidence-rules.md`):

- Never met by any account: the target may not match the offer, or deployment fails everywhere. Show the implementation signals beside it (CS32) before reading it either way.
- No data in the latest period, overall or for named accounts: is the field still stored or the report still received? Outcome shares without data cannot be read (CS87 logic).
- Denominator basis differs: the share is not reach (CS27); it was excluded from met and missed.
- Target eased, turning named accounts to met: report the old and new value, the dates, who set them, and the accounts turned. Do not say whether the change was justified.
- Account-specific targets: list them; an override that turns one account green is shown the same way.
- Maintenance window: accounts 6 or more months past the end of implementation support can be checked for setting-level maintenance (CS26, CS30, this skill's analogy).

### Step 4. Hypotheses, not verdicts

For each flag, offer hypotheses with what would confirm each, labeled. For example: "Activation target eased from 0.5 to 0.4 on 15 July 2026, after Q2 results: possible reasons include a revised eligible population or a revised offer; confirm from the decision record." Never state a reason the record does not show.

## Build the output

Follow `assets/health-threshold-review-output.md`. Answer first: targets no account met, signals missing data, target changes that turned accounts green, with numbers. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every count is from the person's files or a script run on them; versions and dates are stated.
- Target changes are shown with their effect; no judgment of whether they were justified.
- Not comparable and not measured are shown separately.
- No proposed new target values.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Review of thresholds; reading a single period's accounts is the sibling's A2.
- Notes sent to customers are A2; corrections and owners are B1.
- Payment thresholds in an outcomes contract are Market Access `outcomes-contract-monitoring`.
