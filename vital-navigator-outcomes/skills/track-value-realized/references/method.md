# Method: the rules the Organizational Learning skills apply

Shared by *Value Realization* and *Portfolio Review*. Sources read 19 October 2026. Rules marked OWNER are Cowork recommendations adopted under the owner's instruction to proceed (19 October 2026), open to change; rules marked H are skill practice.

| Source key | Document | Version and status |
|---|---|---|
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft |
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L2 | Desired Outcomes | 3.3 |
| EOS-L5 | Organizational Intelligence | 2026-08-14 |
| TOOLS | Connector tools at commit e23025f6e: `value_range`, `realized_value`, `review_trace`, `rescore_note`, `readiness_check`, `scaling_plan` | code read by Cowork from the owner checkout; tools session build record (M) |

## L1 Value is proven at the bottom

"Value is declared at the top and proven at the bottom." Value is counted only when a value realization record shows the outcome achieved (GOV-02 §6; GOV-00 R3). "Expected value shall be stated as a range with its assumptions. Value shall be counted as realized only when the outcome is measured as achieved" (GOV-06 6.3.2).

## L2 Met means measured, and unmet is zero

An outcome is met when its evaluation passes, "not when an output merely exists"; "an unmet evaluation realizes zero value, never partial value" (GOV-02 R-MEASURE). OWNER ruling 1: value counts only for outcomes measured as achieved.

## L3 The realized figure is measured

OWNER ruling 2: the realized figure carries a source and a date (class M); an estimate, forecast or owner's impression is not realized value. The figure is in the same unit and period as the declared range.

## L4 Placing, not judging

The connector places one realized number against the stored range: below, inside or above; it "does not choose a result" (TOOLS). OWNER ruling 3: placement describes; the owner decides what it means.

## L5 Contribution, not proof

OWNER ruling 4 (H): the report lists what else changed in the period that could explain the result (other programs, market changes, staffing), as the owner states them, so a contribution is not read as proof of cause.

## L6 Every activity traces to an outcome

"Every walk shall reach at least one outcome before the work it leads to is counted. Work that reaches no outcome shall be restated against one or retired" (GOV-06 6.2.3). The review tool records stop, keep or fix with a reason, and "traces to none" when no outcome is given (TOOLS). OWNER ruling 5.

## L7 Learning order and stewardship

"Learning shall follow the order: measure performance, then retain what is worth keeping, then change the model. A loop shall not act on raw performance data" (GOV-06 6.9.3). "No learning loop shall change the model without a recorded decision by a named steward, stating the evidence it rests on. AI may prepare that decision; it shall not make it ... each shall be decided individually, with a reason; none shall be adopted automatically ... A change to direction shall need two named people" (GOV-06 6.9.2). Re-scoring outcomes is the outcomes loop (EOS-L2 §6, Arc 1; GOV-02 `ArcActivationDecision`). The re-score tool records the steward and never changes a score (TOOLS). OWNER rulings 6 and 9.

## L8 Readiness re-run

The readiness tool stores factors the person names, scored 1 to 10, and returns no index; it does not invent factors (TOOLS). OWNER ruling 7: a re-run re-scores the strategic capability gaps (*Strategic Readiness*) and any named factors (for example data readiness, change capacity, risk appetite); no combined index.

## L9 Scaling what works

A scale note or scaling plan attaches only to an activity marked keep; the person supplies what is scaled, the owner and the order; the tool does not write the plan (TOOLS). OWNER ruling 8 (H on the second clause): scale only when the activity's outcome was measured as achieved; otherwise keep and watch.

## L10 Compounding is a design intent

"A claim that the model compounds value shall be stated as a design intent until it is measured" (GOV-06 6.9.7).

## L11 Facilitated, then one report

One question per turn, then one full report (references/facilitation.md).

## C5 absorb — realization tracking (7 November 2026)

Lane A: LA-C5-001/002 (Teal19/IPA BRM), LA-C5-007 (QPIE), LA-C5-008 (Magenta Annex A — theory-based ≠ precise effect size).

### Measurement contract (WR-C5-001,005–008)
Link existing benefit profile / owner / range to comparable observations (unit, period, scope, metric/baseline versions, previous value, evidence). Cashable requires explicit `realization_action` with human-confirmed evidence — hours×salary ≠ cash.

### Observation ≠ contribution ≠ causal ROI (WR-C5-013–015,018,022)
Separate measured result, evaluation status, contribution notes / other influences (owner-stated), and economic claims. No arbitrary attribution %. AI may ask about other influences; must not invent confounders. Pilot/target reach ≠ causal ROI or scale.

### Owner L2 recognition (WR-C5-019,025)
Unmet evaluation → **recognized** value zero; preserve raw `measured_figure`. Missing / not-yet-evaluated must **not** be rewritten as a measured zero or granted partial credit. Field/status map (inspected runtime + OWNER rulings 1–9): [`references/owner-l2-recognition-field-map-2026-11-08.md`](../../../references/owner-l2-recognition-field-map-2026-11-08.md). Native `realization_check` distinguishes not-measured (deferred count) from not-achieved (Owner L2 zero).

### Facilitation
- What exactly was measured, in which unit and period, against which approved baseline version?
- What evidence distinguishes observation from a claim the investment caused it?

Catalogue: `references/lane-a-sources-c5-2026-11-07.md`. Offline contracts: `references/proposed-record-contracts-c5-2026-11-07.yaml`.

## C5 deepen — content rules, prospective measurement, closure (8 November 2026)

`realization_check.py` now detects these on the data; it does not rely on the team declaring a flag. Exit code 1 means `problems` is non-empty; 2 means the input could not be read.

| Rule | What the script reads | Gap when |
|---|---|---|
| V-C5-REAL-01 (WR-C5-001) | per outcome `direction`, `baseline`, `target`; range `basis` | direction unknown, baseline/target missing or not numbers, target equal to baseline or moving the wrong way, range with no basis |
| V-C5-REAL-03 (WR-C5-006) | `unit` and `period` on range, realized figure and each measured result | any period missing or unrecognised; realized period differs from range period or an outcome result period differs from the realized period, unless `period_reconciliation` has both `basis` and `approved_by`; unit differs |
| V-C5-REAL-04 (WR-C5-008) | outcome `owner`, `operations_owner`, `project_closed` | no owner, a delivery-only role, or a closed project with no operations owner |
| V-C5-REAL-05 (WR-C5-012) | `closed_outcomes`, `prior_outcomes`, inline `closed` | closure without reason, closer, date, `final_status` or retained history; a prior outcome absent from the current list with no closure record |
| V-C5-REAL-07 | `realized.source`, `source_date`, `kind`, `value` | no source or valid date, a forecast/estimate kind, or a zero with no source |

### Prospective measurement (no contemporaneous record exists)
When the starting point or the result was never recorded, the figure is a `[GAP]`, not a back-cast. Agree the metric, unit, period, source, owner and review date now (the benefit profile as a measurement agreement, WR-C5-001), measure forward, and say so in the report: the realized figure counts only from the first period that has a baseline, a dated source and a matched unit and period. A forecast stays a forecast until a measured, dated actual replaces it. Limitation to state: a prospective baseline cannot show what happened before it began.

### Closure keeps its history (WR-C5-012)
Internal method note (VP-ON-C5-001, cleared `owner_internal_pack_yes`; not for external redistribution): "Note that a benefit is not closed simply because the associated work is completed." A closure therefore names why (achieved, not achieved, superseded, abandoned or not realizable), who closed it, when, and where the measurement history is kept. The script treats `closure_basis: work_completed` as a gap and refuses a silent drop of an outcome that was in the previous review.

### Contribution is not proof (WR-C5-014)
Internal method note (VP-ON-C5-002, cleared `owner_internal_pack_yes`): "Contribution analysis does not provide definitive proof that the intervention has had a causal effect". The report lists owner-stated other influences; `other_changes` entries stated by a model are refused (V-C5-ATTR-03).

### Medical Affairs baseline-then-review (WR-C5-024)
Realization is read against a baseline that existed before tracking began and that has its own review process (`rebuild-baselines`, V-C5-BASE-05). Ask for the approved baseline version before placing any figure.
