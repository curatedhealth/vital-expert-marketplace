# Method: frame-exhibits-honestly

## Purpose
Honesty screen on charts: zero-based axes, absolute with relative, non-causal titles, or withhold.

## Rules
1. Adapted from TRUSTED honest-framing [CHECK] into investment vocabulary.
2. Withhold is a valid honest outcome when baseline/series missing.
3. Script `chart_scale.py` enforces; never invents series.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Encoding-sensitive baseline and consistent comparisons, not all-axes-zero.
- references/method.md: Supported absolute context/denominator/period/range type, no interval invention.
- references/method.md: Material framing edit invalidates affected support and repeats path.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/chart_scale.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Axis encoding (V-C6-CHART-01)
Bars, waterfalls and areas encode magnitude by length, so the axis starts at zero. A non-zero `axis_min` needs `axis_min_justified: true` and a plain-words reason; an `axis_max` below the largest series value clips the data and fails. Line and scatter cropping is context-dependent (LA-C6-001 transfer boundary), so those kinds get the older non-zero justification gap, not this rule.

### Comparable panels (V-C6-CHART-02)
Panels that invite comparison (`panels_comparable: true`) share `axis_min` and `axis_max`; differing scales need `scale_justification`. Dual axes are labeled and justified or split.

### Intervals and uncertainty (V-C6-CHART-03)
A series may carry `ci_low`/`ci_high` only with `interval_basis` (method, sample, source). Scenario bounds (`interval_kind: scenario`) are never labeled 95 percent. If the team has no interval, say so on the exhibit; do not construct one. LA-C6-002 transfer boundary: no invented interval or scenario-to-CI conversion.

### Absolute context (V-C6-CHART-04)
A relative effect (`relative_effect: true`) is shown beside an absolute effect (`absolute_effect: true`) from the supplied data.

### Denominators, periods, framing (V-C6-CHART-05)
When one thing is compared with another (`comparison: true`), state `denominator` and `period` in plain words, and keep favorable and unfavorable framings equally visible.

### Withhold is a valid outcome
`withhold: true` with a `withhold_reason` is honest. A material framing edit invalidates earlier support; repeat the integrity path (see compile-board-pack, PACK-03).

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-001 | Chart details: Axes and gridlines (ONS); Axis start point; Consistent axis scales; Dual axis charts | axis start point, consistent scales across comparable panels, dual-axis caution (CHART-01, CHART-02) | Ordinary bar/area zero; line/scatter cropping context-dependent. Disclosure not automatic endorsement. |
| LA-C6-002 | Showing uncertainty in charts (ONS); When to show uncertainty; Very high uncertainty; Explaining uncertainty | show or explain uncertainty; never invent an interval (CHART-03) | No invented interval or scenario to CI. |
| LA-C6-003 | Shared decision making, NG197 (NICE, 2021); 1.4.7-1.4.11 and rationale | relative change needs absolute context; denominators, periods and framing for comparisons (CHART-04, CHART-05); transfer from patient communication is by analogy only | Patient communication; not investment law, clinical labeling or MLR approval. |
