# Failure modes: cut-the-slop

| Id | Failure | Status | Detection / repair |
|---|---|---|---|
| FM-CS-01 | Fluff cut but a new figure added to “strengthen” | [CHECK] | Diff against grounded draft |
| FM-CS-02 | So-what invented beyond material | [CHECK] | [GAP] or owner rewrite |
| FM-CS-03 | Empty framework (2x2) left with no content | [CHECK] | Delete or fill from supplied only |

## Gap rules

A gap is a fact the decision needs that nobody has supplied or that no source states. Write `[GAP]` with the reason and, where possible, who can close it. Never fill a gap from general knowledge.

| Kind | Example | Wording |
|---|---|---|
| Not supplied | No owner / no baseline extract | `[GAP] … not supplied — ask …` |
| Not measured | Percent without study | `[GAP] … estimate only — not M` |
| Sibling-owned | Launch gate / MLR / valuation | Stop; name sibling plugin |
| Tool unavailable | Verify / steward store down | Label posture; do not fake pass |

Rules: missing catalogue ≠ evidence of absence; owner-stated views are O, not gaps; blocking gaps named first.
