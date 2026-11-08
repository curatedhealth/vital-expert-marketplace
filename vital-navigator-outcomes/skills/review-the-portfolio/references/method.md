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

## C5 absorb — portfolio benefits review (7 November 2026)

Lane A: LA-C5-001 (review cadence/closure), LA-C5-006/009 (APM review / lead-lag commentary — blog≠full BS audit).

### Evidence packet (WR-C5-007,011)
Outcome/benefit links, compatible measurements, original vs current reference, dependencies/disbenefits, mandatory constraints. Cadence follows benefit nature — no universal monthly rule invented here.

### Leading / lagging as roles (WR-C5-016,022)
Record indicator role relative to named objective, expected lag, and review implication. Not a datatype taxonomy (qual≠lead, quant≠lag). Green lead signal → human review, **not** realized credit, Proceed, or scale.

### Human disposition & steward (WR-C5-017)
Stop / keep / fix requires human choice, rationale, named steward for model change, follow-up. AI disposition refused. Raw KPI must not mutate portfolio scores. Benefits-on-track does not waive MLR/Launch/domain mandatory constraints. Stop/keep/fix ≠ Proceed / Investigate first / Handle it internally ownership (C6).

### Facilitation
- What evidence age and dependencies should shape this review disposition?
- Who is the named steward if any assumption or model must change?

Catalogue: `references/lane-a-sources-c5-2026-11-07.md`.

## C5 deepen — cross-work contributions, responsibility, closure (8 November 2026)

`review_check.py` content rules (exit 1 on any flag at any level):

| Rule | Reads | Flag when |
|---|---|---|
| V-C5-REV-02 (WR-C5-011) | `outcome`, `contributes_with`, `cross_work_reviewed` + `cross_work_note`, `depends_on`, `dependency_resolution`, `counted_realized_value`, `overlap_resolved` | two or more activities share an outcome with no mutual acknowledgement; a dependency names an activity not in the review; an activity is stopped while a kept or fixed activity depends on it; two activities both count realized value on one outcome with no `overlap_resolved` |
| V-C5-REV-03 (WR-C5-016) | `indicator_role`, `counted_as_realized`, `outcome_status`, `lagging_evidence`, `realized_place` | a leading indicator is counted as realized, or "achieved" rests on it with no lagging evidence |
| V-C5-REV-04 (WR-C5-017) | `decided_by`, `reason`, `outcome`, steward, approvers | no named person, or a role in place of one, accepts the disposition, the steward or a direction change |
| V-C5-REAL-05 (WR-C5-012) | `closed_activities`, `prior_activities`, inline `closed` | closure without reason, closer, date and retained history; a prior activity missing with no closure record |

REV-01 (review frequency follows the benefit and its evidence) stays Deferred: no cadence is invented here, so the script does not test one.

### Cross-work and double counting
A portfolio review reads contributions across work, not activity by activity. Two activities that serve the same outcome list each other, or record a reviewed note on how they relate; when both claim realized value on that outcome, the review records how the overlap is resolved so the total is not counted twice.

### Closure retention (WR-C5-012)
Stop is a disposition; closure is a record. A closed activity keeps its reason, who closed it, the date and a pointer to its history. Dropping an item between reviews without that record is a flag, whatever the disposition said.
