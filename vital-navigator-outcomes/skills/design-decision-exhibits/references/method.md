# Method: design-decision-exhibits

## Purpose
Lock decision-ready exhibits from team-entered series. Prefer withhold over fake waterfalls.

## Rules
1. Allowed types: options_matrix, sensitivity_tornado, value_waterfall, delivery_dependency, portfolio_placement.
2. Every series needs source_id; locked=true before board seal.
3. value_waterfall with baseline_required and not baseline_present → gap (withhold).
4. Script `exhibit_check.py` enforces; never invents chart values.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Question/canonical ID/eligible model/data/source/limits.
- references/method.md: Encoding contract: scale/unit/range/source/gap, no decorative plots.
- references/method.md: Only current5 exhibit contracts; no scoring/dollarization/auto-select.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/exhibit_check.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Interpretable question (V-C6-EXH-01)
Every exhibit states the question it answers in one sentence, in the `question` field, before any series is drawn. A decorative chart has no question and does not lock. The question names the decision it informs, not the chart type. LA-C6-002 supports withholding a display when uncertainty is too high to interpret.

### Sourced series, no invented values (V-C6-EXH-02)
Each series entry has `name`, `source_id` and a non-null `value`. A missing source or a null is a gap, never a plausible fill. Exhibit type is one of the five contracts (`sensitivity_tornado`, `value_waterfall`, `options_matrix`, `delivery_dependency`, `portfolio_placement`); do not force an exhibit into a type to look complete.

### Baseline and lock
A `value_waterfall` with `baseline_required: true` is withheld until `baseline_present` is true. `locked: true` is set by the owner after review; the assistant prepares and never locks silently.

### Scale handoff
Axis, interval and denominator questions belong to frame-exhibits-honestly; hand the locked series there before a pack seal.

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-002 | Showing uncertainty in charts (ONS); When to show uncertainty; Very high uncertainty; Explaining uncertainty | choose an exhibit only where an interpretable question exists; very high uncertainty may mean no chart (EXH-01) | No invented interval or scenario to CI. |
| LA-C6-001 | Chart details: Axes and gridlines (ONS); Axis start point; Consistent axis scales; Dual axis charts | scale and axis disclosure for the exhibit types that plot quantities (EXH-02 context, with frame-exhibits-honestly) | Ordinary bar/area zero; line/scatter cropping context-dependent. Disclosure not automatic endorsement. |
