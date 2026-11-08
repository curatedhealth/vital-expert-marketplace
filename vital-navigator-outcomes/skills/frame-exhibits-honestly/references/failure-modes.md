# Failure modes: frame-exhibits-honestly

| Id | Failure | Status | Detection / repair |
|---|---|---|---|
| FM-FE-01 | Cropped axis dramatizes sensitivity | [CHECK] | chart_scale / visual check |
| FM-FE-02 | Relative-only value story | [CHECK] | Require absolute |
| FM-FE-03 | Missing model owner | [CHECK] | Script [GAP] |

## Gap rules

A gap is a fact the decision needs that nobody has supplied or that no source states. Write `[GAP]` with the reason and, where possible, who can close it. Never fill a gap from general knowledge.

| Kind | Example | Wording |
|---|---|---|
| Not supplied | No owner / no baseline extract | `[GAP] … not supplied — ask …` |
| Not measured | Percent without study | `[GAP] … estimate only — not M` |
| Sibling-owned | Launch gate / MLR / valuation | Stop; name sibling plugin |
| Tool unavailable | Verify / steward store down | Label posture; do not fake pass |

Rules: missing catalogue ≠ evidence of absence; owner-stated views are O, not gaps; blocking gaps named first.
