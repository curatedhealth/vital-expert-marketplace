# A1 Coverage status tracking

Framework task: DH-03.01.4.2, Part A, task A1.

## What this task delivers

A dated view of where the product stands in each market it was meant to reach, what has changed since the strategy was set, which clocks are running, and how similar products fared on the same route. It answers "where are we on coverage now, and what is about to move?"

Why it matters: coverage is not a one-time event. Trials expire, early-funding years end, evidence periods close, prices reset. A plan built on last quarter's status can be wrong today without anyone noticing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.2 Part A, Coverage status tracking |
| Workflow | The steps below |
| Knowledge | `references/lapse-signals.md`; `references/access-monitoring-sources.md`; the strategy or pathway map if the conversation holds one |
| Tools | `list_schemes`, `get_market_matrix`, `get_reimbursement_status`, `get_status_history`, `find_scheme_precedents`, `watch_scheme` (only on request); `scripts/coverage_clocks.py` (optional) |
| Prompt | This guide |
| Template | `assets/status-tracking-output.md` |
| Input | The request and its context: product, target markets, the baseline (the plan, an earlier run, or "as of" a date) |
| Governance | `references/governance.md` |

## Read the request

- **Product and markets.** If the conversation holds a pathway map or access strategy (from the coverage pathway skill), take the markets from it. Otherwise ask which markets the plan targets.
- **Baseline.** What to compare against: an earlier run of this task, a status the person states, or the plan's assumptions. Without a baseline, the output is a current snapshot and says so.
- **Mode.** A direct question gets short mode. A document for a review meeting gets full mode.

## Workflow

### Step 1. Know what the library can see

Call `list_schemes` (free). Note for each target market whether the library holds that scheme and when it was last loaded. A market the library does not hold is "scheme not loaded" for the whole task; say so once and move on.

### Step 2. Current status per market

Call `get_market_matrix` with the product name for a multi-market view, or `get_reimbursement_status` per scheme for one or two markets. Record per market: status in plain words, listed date, price where stated, source page, retrieval date. Classify every absence with `references/gap-rules.md`.

### Step 3. History and change

Call `get_status_history` for each market where the product is listed.

- If the person gave a baseline, compare and state what changed, with dates.
- If the library holds one row only, say the change date is `[GAP]`. Never read `listed_on` or "durability days" as the date a status changed (see `references/tools.md`).
- If the stored status and the stored passage disagree, quote both and say "check the register".

### Step 4. Running clocks

For each listed market, find the clock that applies in `references/lapse-signals.md` and count from the listed date (or the stated end date if one is stored). With code execution, run `scripts/coverage_clocks.py` on the saved tool output. Report each clock as a signal to check, for example "listed on trial 20 months ago: past the 12-month period; check whether an extension was granted or a decision is pending". For Germany, always add that an expired trial stays listed until BfArM decides.

### Step 5. How comparable products fared

Call `find_scheme_precedents` on the same scheme, narrowed by indication in the register's language or by ICD code. From the rows, report how many comparable products are on trial, permanent or deleted, and for deleted ones the time from listing to deletion. Add the national context from `references/access-monitoring-sources.md` (for Germany: of 60 trial listings to the end of 2025, 34 became permanent, 16 were deleted, 10 were still on trial; trials averaged 20 months). This is context for the person's own judgment, not a prediction for their product.

### Step 6. What it means for the person

Close the facts with their consequence for the person's position, using only sourced mechanics. For their own product: which clock decides the next move and what has to be ready by then. For a competitor: what each outcome would change, for example that a German trial DiGA made permanent moves to a negotiated price from month 13 (trial DiGA that became permanent saw an average price cut of 51 percent, `access-monitoring-sources.md` DE-10), or that the same manufacturer holds another listing in the indication. State consequences as conditional ("if it is made permanent…"), never as a prediction.

### Step 7. Watch, only if asked

If the person wants to hear about future changes, call `watch_scheme` with the scheme and product and record the snapshot hash and time. Say changes appear after the library's next refresh and that watches are not yet separated by customer, so avoid confidential names.

## Build the output

Follow `assets/status-tracking-output.md`. Answer first: the one or two things that changed or are about to. Then the market table, the clocks, the comparables, what it means for the person, and what to check at the authority. A direct question gets short mode: keep it under about 450 words and put the rules behind each clock in one line each, not a section per outcome.

## Before you hand it over

- Every status has its source page and retrieval date.
- No change date is inferred; no clock is stated as a lapse.
- Comparables are described as what happened to them, never as a forecast for this product.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Status tracking only. Whether the strategy is working is B1; how many patients use the product is A2.
- No legal reading of a court case or a deletion notice; point to the authority and the person's counsel.
- Drugs, biologics and wellness apps are out of scope.
