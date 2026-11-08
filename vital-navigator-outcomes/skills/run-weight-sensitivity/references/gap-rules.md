# Gap rules: run-weight-sensitivity

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

## C3 refusals — sensitivity (SEN; 7 November 2026)

| Refusal | Trigger | Response shape |
|---|---|---|
| GP-SEN-01 Rank-swap-as-choice | "Option B wins after weight change — Proceed" | Refuse; sensitivity is diagnostic only; owner chooses route |
| GP-SEN-02 Unapproved bounds | Assistant invents weight intervals | Refuse; request human-approved range and redistribution rule |
| GP-SEN-03 Hidden normalization | Weight change without stating renormalization | Refuse; show base weights, changed inputs, rule |
| GP-SEN-04 Global robustness | Partial numeric model claimed to settle whole decision | Refuse; retain qualitative criteria and dissent |
| GP-SEN-05 Tornado confusion | `methods_risk_tornado` treated as MCDA weight sweep | Refuse conflation; name tool and question type |
| GP-SEN-06 Stability as success % | Rank stability presented as implementation confidence | Refuse; no success probability from sensitivity |

## Rule-ID SSOT (8 November 2026)

The rule ids that scripts raise and the offline validator tests are the `V-C3-*` ids in `scripts/offline_c_validator/rule_register.csv` (behavior in `vital_validate.py`; live-schema mapping in `live_adapters.py`). Where this file or a known-answer case disagrees on an id, the register wins. The `GP-*` labels in this file are descriptive gap patterns, not rule ids.

| V-C3 id | Rule | Script content check (`sensitivity_exhibit.py`) | Gap pattern(s) |
|---|---|---|---|
| V-C3-SEN-01 | Exhibit names model version, score matrix, output metric, units and a qualitative-limitations reference | all five fields required | none |
| V-C3-SEN-02 | Diagnostic only; no choice | `choose_winner`, `auto_proceed`, `selected_option`, `close_disposition`, any `recommendation` field, choosing language in free text | GP-SEN-01 |
| V-C3-SEN-03 | Weights normalized, bounded, redistribution declared | weights sum to 1; redistribution check when declared | GP-SEN-02, GP-SEN-03 |
| V-C3-SEN-04 | Weight-only sweep with frozen scores and anchors | `scores_frozen` and `anchors_frozen` must both be true; `frozen_options_snapshot` must equal `options` | none |
| V-C3-SEN-05 | No whole-decision robustness claim from a partial model | `partial_model` + claim flag; robustness wording on a partial or limitation-free exhibit | GP-SEN-04 |
| V-C3-SEN-06 | A risk tornado is a different question from an MCDA weight sweep; name the tool and the question type (added 8 November 2026) | `tool` / `method` / `engine_tool` set to `methods_risk_tornado` or `risk_tornado`; `tornado_as_weight_sweep` true; free text that equates a risk tornado with the weight sweep. A weight sweep drawn as tornado-shaped bars (`sensitivity_tornado` exhibit) is allowed; wording that says it is not a risk tornado passes | GP-SEN-05 |
| V-C3-SEN-07 | Rank stability under weight changes is not a success probability or implementation confidence (added 8 November 2026) | `success_probability`, `implementation_confidence`, `success_percent`, `stability_as_success` set; free text that turns a stability percentage into a chance or probability of success or implementation. Descriptive counts ("held at 3 of 4 tested weight sets") and negated wording pass | GP-SEN-06 |

`GP-SEN-05` and `GP-SEN-06` now map to V-C3-SEN-06 and V-C3-SEN-07 (additive register rows, `D-C3-GP-UNMAPPED` absorbed 8 November 2026). The wording checks are vocabulary screens marked [CHECK]; a person can still phrase either mistake in other words.
