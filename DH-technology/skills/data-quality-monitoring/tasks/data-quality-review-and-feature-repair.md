# B1 Data quality review and feature repair

Framework task: DH-01.04.4.2 Part B, task B1. Carries the old one-line task "DH-01.04.4.2.3 Feature repair" ("Assign a failed check") with the pass-rule and owner steps of the old competency.

## What this task delivers

For each check that failed against the person's limit in A2: the count behind it, the owner the person names, the repair the person chooses (feature removed, redefined, stopped, or accepted with a reason), the new dataset version, and the recheck date the person sets; the checks without a limit listed apart; the repair-log rows that do not match a failed check; and the decisions the review surfaces (which version may be used for training, whether a test set already used must be replaced, whether a rule changes), each with its facts, all left to the person. It answers "by our own rules, what failed, who fixes it, and which version do we use?"

Why it matters: the old task is explicit: "Do not train on the failed version." A repair without a new version, or a failed check without an owner, leaves the next model trained on the same fault.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `data-engineering-manager-health` (old DH-01.04.4.2.3). Work as a data quality analyst who checks the repair log against the failed checks |
| Skill | DH-01.04.4.2 Part B, Data quality review and feature repair |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/data-quality-requirements.md` section 6; rows DA-68, DA-71, DA-73, DA-99 to DA-101, CV87 |
| Tools | `scripts/dq_check.py review`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/data-quality-review-and-feature-repair-output.md` |
| Input | The request and its context: A2 results (or the person's run), the repair log, the owners, actions, versions and recheck dates the person sets |
| Governance | `references/governance.md`; the person judges, assigns and closes |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the limits, names the owners, chooses the repair, names the new version and sets the recheck dates. The model reads the results against the rules and the repair log and writes down what is missing. It never calls the data fit for training, never names an owner the person has not named and never closes a failed check. Where a limit's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the limits

Write each limit back verbatim from the rules, with the version and date written. A check without a limit: "limit not given"; report its count, mark nothing.

### Step 2. Join failed checks with the repair log

Run `python3 scripts/dq_check.py review --results RESULTS.json --log REPAIRS.csv`. Report per failed check: field, count of denominator, owner (the person's or "owner not named"), action, new version, recheck date, flags R1 to R5; and R6 for log rows that do not match a failed check (for example a repair logged for a check that passed in this run).

### Step 3. Owners, repairs and versions for each failed check (old "Feature repair")

For each failed check: the owner the person named (or "owner not named"; ask), whether the feature is removed or redefined (or "not given"; ask), the new dataset version (or "not given"), the recheck date (or "not given"; ask). A repair naming the failed version itself (R4) is stated as a fact. A recheck date earlier than the read date is a fact, never urgency. A failed check stays open until the person closes it with a rerun on the new version.

### Step 4. Sequence the repairs

Order by dependency: key uniqueness and relational failures before completeness and plausibility on joined data; a leak repair before any retraining. State the order as a fact from the failing checks, not as a priority the model sets.

### Step 5. What the person must decide

List the decisions, each with its facts: which version may be used for training (the old task: not the failed one); whether a redefined feature means a model already evaluated on a test set needs a new independent test set (EMA paper, medicinal products, context: DA-73); whether the transformations and their impact are documented (CV87, drug submissions, context) and provenance kept (FAIR R1.2, DA-100, a guide); whether a limit changes, and the date the new limit is written so later runs use it. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/data-quality-review-and-feature-repair-output.md`. Answer first: how many checks failed on which version, how many have an owner, a repair, a new version and a recheck date, and the gap that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/dq_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Limits, owners, repairs, versions and dates are the person's, and the record says so.
- No "fit for training", no closed check, no owner the person did not name.
- Checks without a limit are not marked.
- The review is labeled "data quality review draft for the owner".
- `python3 scripts/dq_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Redefining a feature at design (window, source, missing code): `data-preparation-and-analytics-methods` (this pack).
- Retraining and performance after repair: `model-performance-and-drift-monitoring` (this pack).
- Document and change control for the dataset in a regulated product: `dh-regulatory-and-quality` document-and-change-control.
