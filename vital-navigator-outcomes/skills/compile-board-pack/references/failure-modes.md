# Failure modes: compile-board-pack

| Id | Failure | Status | Detection / repair |
|---|---|---|---|
| FM-BP-01 | Pack sealed without exhibits | [CHECK] | board_pack_check |
| FM-BP-02 | Assistant marks signed | [CHECK] | Script refuses |
| FM-BP-03 | MLR “approved” language | [CHECK] | Forbidden; READY chairs out of scope |
| FM-BP-04 | Launch gate verdict used | [CHECK] | Rewrite to Proceed / Investigate first / Handle it internally |

## Gap rules

A gap is a fact the decision needs that nobody has supplied or that no source states. Write `[GAP]` with the reason and, where possible, who can close it. Never fill a gap from general knowledge.

| Kind | Example | Wording |
|---|---|---|
| Not supplied | No owner / no baseline extract | `[GAP] … not supplied — ask …` |
| Not measured | Percent without study | `[GAP] … estimate only — not M` |
| Sibling-owned | Launch gate / MLR / valuation | Stop; name sibling plugin |
| Tool unavailable | Verify / steward store down | Label posture; do not fake pass |

Rules: missing catalogue ≠ evidence of absence; owner-stated views are O, not gaps; blocking gaps named first.
