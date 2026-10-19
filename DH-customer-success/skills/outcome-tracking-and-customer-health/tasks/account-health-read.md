# A2 Account health read

Framework task: DH-02.02.3.1, Part A, task A2. Replaces the earlier "Account health read" section.

## What this task delivers

For each account in scope and one period: each signal's value, the person's target, met, missed, not measured or not comparable, the gap to target, the denominator, and the health view under the person's rule. Beside it, what the figures can and cannot show. It answers "where does each account stand against our targets this period?"

Why it matters: a health read built on mismatched denominators, missing outcome data or an unstated rule turns accounts green that are not. RE-AIM requires a valid denominator (CS27); ACCESS keeps lost-to-follow-up patients in the denominator (CS87), which is the honest way to read an outcome share.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.3.1 Part A, Account health read |
| Workflow | The steps below |
| Knowledge | `references/health-signals.md`; `references/outcome-measures.md` |
| Tools | `scripts/account_health.py attain` and `health` (no connector). No library call: the person's data stays in the conversation |
| Prompt | This guide |
| Template | `assets/account-health-read-output.md` |
| Input | The request and its context: the account file (aggregates per account, period, measure), the targets and health rule (A1 plan or the person's list), optional account meta (go-live, support end, day-one items open), the period |
| Governance | `references/governance.md`; no verdict without the person's target; no score or average the person did not define |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. |

## Read the request

- **Data.** Ask for the account file in the columns the script reads (its header), or a table in the message. Aggregates only.
- **Targets and rule.** From A1 or the person. Without a target a signal gets a number and "no target set". Without a rule, no health status.
- **Period and as-of date.** Default to the latest period in the file and say so.
- **Mode.** Short for "how are our accounts doing"; full for a portfolio review pack.

## Workflow

### Step 1. Take and check the data

Put the person's rows into the account file shape. Check: a numerator above its denominator, a share without its denominator basis, a measure in the file with no target, a target with no data. Blank means not measured: mark `[GAP]` and name the report that would hold it.

### Step 2. Compute

With code execution, run:

- `python3 scripts/account_health.py attain ACCOUNTS.csv --targets TARGETS.json [--period YYYY-MM-DD]`
- `python3 scripts/account_health.py health ACCOUNTS.csv --targets TARGETS.json [--meta META.csv --as-of YYYY-MM-DD]`

Without code execution, compute by hand the same way: value = numerator / denominator; met if at or beyond the person's target in the stated direction; a value whose denominator basis differs from the target's is "not comparable" (CS27), never met or missed; the health status follows the person's rule only. The script applies the day-one rule only if the person adopted it (`adopted_rules`), and reports months since implementation support ended, flagging 6 or more as the RE-AIM maintenance window (CS26, CS30; this skill's analogy from study funding to support).

### Step 3. Read the outcome figures honestly

For every outcome aggregate: state the denominator (starters or those with follow-up), the completeness signal beside it, and the label once: uptake, use and customer-reported outcomes are not clinical evidence; no comparator, so not evidence of effect (CS32). Where follow-up completeness is low, say the outcome share cannot be read on its own. PHQ-9 bands only with CS92.

### Step 4. Implementation before outcome

For an account whose outcome signal misses, show its uptake and use signals first. Proctor's point applies: implementation outcomes are preconditions (CS32), so a missed outcome with low use is first a deployment question. State this as a reading, not a cause.

### Step 5. What it means for the person

Two or three consequences, stated conditionally and tied to the person's own rule. For example: "Under your rule, Lakeside misses on active use (0.416 against 0.5); the day-one rule you adopted would also block a healthy status while its go-live item is open." No cause, no forecast of renewal or churn (not sourced).

## Build the output

Follow `assets/account-health-read-output.md`. Answer first: which accounts meet the person's rule, which miss and on which signal, which cannot be decided and why. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number is from the person's file or a script run on it; the targets' version and date are stated.
- No verdict without the person's target; no health status without the person's rule; no average or color.
- Not comparable and not measured are shown, never folded into met or missed.
- The "not clinical evidence" label appears once.
- No renewal, churn or revenue forecast.
- The person's data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- A read of one period. Whether thresholds still fit and whether notes sent were backed is the monitoring sibling (`value-realization-monitoring`).
- What to show and what to do is B1.
- Payment attainment under an outcomes contract is Market Access `outcomes-contract-monitoring`.
