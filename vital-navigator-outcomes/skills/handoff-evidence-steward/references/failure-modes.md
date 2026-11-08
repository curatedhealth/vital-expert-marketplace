# Failure modes: handoff-evidence-steward

| Id | Failure | Status | Repair |
|---|---|---|---|
| FM-ES-01 | Fabricated record_id | [CHECK] | Delete; [GAP] |
| FM-ES-02 | Used Verify instead of Curator | [CHECK] | Route to handoff-verify for claims |

## Gap rules

A gap is a fact the decision needs that nobody has supplied or that no source states. Write `[GAP]` with the reason and, where possible, who can close it. Never fill a gap from general knowledge.

| Kind | Example | Wording |
|---|---|---|
| Not supplied | No owner / no baseline extract | `[GAP] … not supplied — ask …` |
| Not measured | Percent without study | `[GAP] … estimate only — not M` |
| Sibling-owned | Launch gate / MLR / valuation | Stop; name sibling plugin |
| Tool unavailable | Verify / steward store down | Label posture; do not fake pass |

Rules: missing catalogue ≠ evidence of absence; owner-stated views are O, not gaps; blocking gaps named first.
