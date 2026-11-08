# Gap rules: frame-exhibits-honestly

# Gap rules

A gap is a fact this skill needs that nobody supplied or no source states. Write `[GAP]` with reason and who can close it. Never fill from memory.

| Kind | Example | Wording |
|---|---|---|
| Not supplied | No owner / no next skill | `[GAP] … not supplied — ask …` |
| Not measured | Percent without study | `[GAP] … estimate only — not M` |
| Sibling-owned | Launch gate / MLR / valuation | Stop; name sibling plugin |
| Tool unavailable | Verify / steward store down | Label posture; do not fake pass |
| Schema fail | Script exit 1 | Fix team inputs; re-run script |

Rules: owner-stated views are O, not gaps; blocking gaps first; teaching figures never close a gap.

## C6 Governance absorb (8 November 2026)

| Situation | Action |
|---|---|
| Refuse hidden truncated bars/relative-only distortion. | **Refuse / redirect** |
| Refuse scenario-as-CI/stale approvals. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/chart_scale.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-CHART-01: bar/waterfall/area with non-zero `axis_min` and no `axis_min_justified`; `axis_max` below the largest series value.
- V-C6-CHART-02: `panels` with `panels_comparable` true and differing `axis_min`/`axis_max` without `scale_justification`.
- V-C6-CHART-03: series `ci_low`/`ci_high` without `interval_basis`; scenario bounds labeled 95%.
- V-C6-CHART-04: `relative_effect` without `absolute_effect`.
- V-C6-CHART-05: `comparison` true without `denominator` and `period`.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `hidden_truncated_ordinary_bars` | V-C6-CHART-01 |
| `inconsistent_panel_scales, dual_axis_exaggeration` | V-C6-CHART-02 |
| `invent_confidence_interval, scenario_bounds_as_95ci` | V-C6-CHART-03 |
| `relative_only_hide_absolute` | V-C6-CHART-04 |
| `denominator_period_framing_hide` | V-C6-CHART-05 |
| `stale_green_after_material_edit` | V-C6-CHART-01/PACK |

Flag-only rules that structure cannot prove (truth, identity, authority, validity) are listed as deferred in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
