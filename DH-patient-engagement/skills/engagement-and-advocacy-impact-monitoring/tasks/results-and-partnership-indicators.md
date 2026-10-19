# A2 Results and partnership indicators

Framework task: DH-02.03.2.2, Part A, task A2. Replaces the earlier "Activity score" section (CF-12.02.03.2.2.2) and adds the attrition, support and partnership indicators the sourced rows make possible.

## What this task delivers

From the person's own logs, as of a stated date: the result per activity against its definition, activities unscored for lack of a record, claims used off the allowed list, the attrition curve with usage half-life and dropout attrition, support value per patient per calendar year against the year's safe-harbor figure with cash-equivalent and recommendation flags, and partnership flags (support before an agreement, no stated purpose, not disclosed). It answers "what happened, in numbers, and what do the records show?"

Why it matters: an activity with no record is not a zero (old rule); usage half-life and the split between dropout and nonusage attrition show where people leave (PE-102, PE-103); support above $623 per patient in 2026 (CP-US-27) and support before a written agreement (PE-71, PE-80) are facts the compliance owner needs to see.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.03.2.2 Part A, Results and partnership indicators |
| Workflow | The steps below |
| Knowledge | `references/indicators.md`; `references/result-definitions.md`; A1 definitions |
| Tools | `scripts/engagement_monitor.py` (local); `literature.search_literature` (optional, counted) |
| Prompt | This guide |
| Template | `assets/results-and-partnership-indicators-output.md` |
| Input | The request and its context: A1 definitions, the as-of date, the person's logs (activity results, participant start and last-active dates, support items, partner records) as files or aggregates, targets if set |
| Governance | `references/governance.md`; support findings stop for the compliance owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **As-of date and period.** Required. Ask if missing.
- **Logs.** Files in the column layouts of `scripts/engagement_monitor.py`, or aggregates the person types. Pseudonymous ids only.
- **Targets.** The person's, per activity, or none.
- **Codes.** Whether the company is bound by the EFPIA or ABPI Code (for partnership flags).
- **Mode.** Short for a direct question; full for a program review.

## Workflow

### Step 1. Activity results

With code execution, run `python3 scripts/engagement_monitor.py activities FILE`. Without it, compute by hand the same way. Report per activity: result count, share of the stated denominator, the person's target (or "not set"), met or missed only where a target exists. List unscored activities by name with "no record". List off-list claims for the review owner.

### Step 2. Attrition

Run `attrition FILE --as-of DATE --step DAYS` (the step is a display choice; ask or use 7). Report the curve, the usage half-life and dropout attrition, and say how "active" was read from the person's data. State the step in the answer (for example, "usage half-life day 21 at a 7-day step; it resolves only to the step") and cite PE-103 [PAPER] for the half-life (doi:10.2196/jmir.7.1.e11). A small number of participants makes the curve unstable; say how many were observable at each point.

### Step 3. Support per patient

Run `support FILE --year YEAR --cap FIGURE`. For 2026 the figure is $623 (CP-US-27); for another year write `[GAP]` and ask the person to supply OIG's figure. Report patients above the figure, items marked cash or cash equivalent, items without a recorded recommendation. Then write the stop: these are elements for the compliance owner; the draft does not say support is or is not protected.

### Step 4. Partnership flags

Run `partners FILE`. Report each flag with its row, labeled [INDUSTRY], and only for codes the company is bound by. Disclosure timing per code from `references/indicators.md` section 4.

### Step 5. Published context (optional)

If the person asks how their attrition compares, call `literature.search_literature` with the condition and "attrition" or "engagement" and a `date_from` the person accepts, `limit` 5. Read `references/tools.md`. Name a paper only by what it states, after reading it; if a figure is quoted, run `verify.qualify_source` then `verify.check_claim` with the passage read, and accept only a same-direction passage (register N3). Label any rate "context, not a target".

## Build the output

Follow `assets/results-and-partnership-indicators-output.md`. Answer first: the two or three indicators that stand out, with numbers and the as-of date. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number comes from the person's data or a saved run; denominators and the as-of date are stated.
- Unscored activities are named, not zeroed.
- No sentence says support is protected or that the program improved health.
- Published rates are labeled context.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Indicators on the person's program records. KPI reliability across the pack is Patient Engagement 3.2; equity of reach is Patient Engagement 4.x.
- Decisions on what to change are B1.
