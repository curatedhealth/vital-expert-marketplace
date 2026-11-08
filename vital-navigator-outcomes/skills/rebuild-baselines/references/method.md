# Method: rebuild-baselines

## Purpose
Establish or refuse baselines for value tracking. Never backcast from memory.

## Rules
1. Provenance: extract | time_study | gap. Gap forbids numeric value.
2. Extract/study requires source_id + source_date; extract prefers class M or V.
3. Optional low/mid/high must satisfy low ≤ mid ≤ high and low ≠ high.
4. Offline script `baseline_check.py` validates; never fills cells.

## Outputs
Baseline rebuild sheet. Carry gaps into `size-value-at-stake` / `track-value-realized`.

## Lane A absorb — two baselines & no memory backcast (7 November 2026)

Keep **observed starting point** distinct from **counterfactual BAU** (benefits guidance / Crosswalk). Refuse `memory_backcast` and baselines filled from satisfaction scores (`baseline_check.py`; LA-TEAL-19, LA-STRAT-NEEDS).

## C5 absorb — provenance, rebuild, no recollection (7 November 2026)

Lane A: LA-C5-001 (Teal19 baseline), LA-C5-002 (IPA rebase), LA-C5-003/004 (Teal22/23 change/traceability), LA-C5-007 (QPIE observation vs attribution).

### Roles kept distinct (WR-C5-002,013,020)
1. Observed starting point — contemporaneous evidence of pre-change state.
2. Counterfactual BAU — model/evidence of without-intervention path; **not** observed truth by default.
3. Approved target/range — intended result, not counterfactual.
4. Revised forecast — updated expectation; does not erase original promise.
5. Corrected observation — source-backed correction with retained old value/reason/version.

### Controlled rebuild (WR-C5-003,004)
Record trigger, old/new values+versions, impact, human approval, effective date. Silent overwrite refused. Memory_backcast / recollection refused; ODI/satisfaction substitution refused; teaching figures not live evidence.

### Facilitation
- Which contemporaneous record supports this baseline and the period it represents?
- What changed enough to justify a revised baseline rather than a revised forecast?

Catalogue: `references/lane-a-sources-c5-2026-11-07.md`.

## C5 deepen — baseline-then-review, prospective measurement (8 November 2026)

`baseline_check.py` content rules (exit 1 on any gap):

| Rule | Reads | Gap when |
|---|---|---|
| V-C5-BASE-01 | `provenance`, `gap_reason` / `prospective_plan`, `period`, `source_date` | a gap row gives neither a reason nor a plan to measure forward; a measured row has an unrecognised period or a non-ISO source date |
| V-C5-BASE-04 | `baseline_role`, `labeled_as_observed`, `observed_baseline_id`, `source_id` | modelled BAU labelled observed, or BAU reusing the observed source |
| V-C5-BASE-05 (WR-C5-024) | `review_process` (`cadence`, `reviewer`, `next_review`), `tracking_start` | no review process, a role instead of a named reviewer, an invalid next review date, a baseline whose `source_date` is after `tracking_start`, or a next review before tracking starts |
| unit / period | `unit`, `period` across rows | the same metric appears in two units; the same metric, period and role appears twice outside a rebase |

### Baseline-then-review (WR-C5-024)
Medical Affairs measurement starts by understanding the baseline before tracking and assessing value or impact. In practice: capture the baseline from a contemporaneous record, date it, then fix who reviews it, how often, and when the next review falls. A baseline captured after tracking has begun is a first observation, not a baseline.

### Prospective measurement when the record is missing
If no contemporaneous record exists, keep `provenance: gap` and add a `prospective_plan` (method, start date, owner): a time study, an extract from the next system release, or a defined sample. State the limitation: the baseline will describe the state from the start date, not the pre-change period, so benefits earlier than that cannot be measured. Never fill the gap from recollection (`memory_backcast`, V-C5-BASE-06), a satisfaction score, or an ODI opportunity score (V-C5-BASE-01).
