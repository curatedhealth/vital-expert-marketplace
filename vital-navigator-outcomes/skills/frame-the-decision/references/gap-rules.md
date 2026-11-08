# Gap rules

A gap is a fact the decision needs that nobody has supplied or that no source states. Write it as `[GAP]` with the reason and, where possible, who or what would close it. Never fill a gap from general knowledge, and never let a gap silently become an assumption.

## The four kinds of gap in framing

| Kind | Example | How to word it |
|---|---|---|
| Not supplied by the person | No owner named; no goal stated | "[GAP] Decision owner not named. A decision without an owner cannot proceed to scoring." |
| Not scored | A scorer did not return the sheet | "[GAP] Not scored by [name]. Listed as missing; no score was filled in." |
| Not in the catalogue | No value theme matches the goal | "[GAP] No catalogue value theme matched; the goal is kept as stated." |
| Not stated by the method | No numeric threshold maps sizing to a session format | "[GAP] The method gives signals, not thresholds; the owner chooses the format." |

## Rules

- A missing catalogue row is never evidence that the value does not exist. It is a limit of the catalogue.
- A view from the room is owner-stated, not a gap and not a measurement. Label it O.
- A gap that blocks the next step is named first, with what unblocks it.
- In a direct answer give at most three gap lines. In the full report list every gap, most blocking first.

## Lane A gaps (7 November 2026)

- Missing purpose, scope, or perspective → `[GAP]` (LA-SDG-FRAME).
- Group authority without resolution_rule → `[GAP]` (LA-BAIN-RAPID).
- `treat_driver_as_authorized` → refuse (LA-DACI).

## Round-2 gaps and refuses (7 November 2026)

| Trigger | Action |
|---|---|
| Material givens unstated when scope depends on them | `[GAP]` — what is being held fixed? (rule id V-C1-GVN-01) |
| Frame changed without `frame_revisions` entry | `[GAP]` — record human-approved revision |
| `assistant_dq_percent` or AI DQ completeness score | **Refuse** (WR-C1-R2-004) |
| Six DQ evidence/gap links missing at frame exit | **`[GAP]` / refuse leave Direction** (V-C1-DQ-01); gaps allowed, percent refused. Opt-out: `require_dq_links=false` for intake scratch only |
| Agree constraints treated as negotiable preferences | **Refuse**; list mandatory constraints separately |
| Decider claims MLR/legal waiver via R/A escalation alone | **Refuse** (WR-006) |

## Rule-id split (8 November 2026)

- **V-C1-GVN-01** — givens must be a non-empty list of strings when the frame is revised or `require_givens` is true.
- **V-C1-R2-02** — Agree roles and mandatory constraints only (waiver, preference framing, unmet-but-passed).
- Content paths: WR-001 (solution-verb or embedded-solution statement), WR-003 (decoy, duplicate, reference-only options), V-C1-R2-01 (AI actor as decider).
