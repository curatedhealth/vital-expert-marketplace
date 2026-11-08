# Gap rules

A gap is a fact the outcome work needs that nobody has supplied or no source states. Write `[GAP]` with the reason and what would close it. Never fill a gap from general knowledge; never let a gap become an assumption silently.

| Kind | Example | How to word it |
|---|---|---|
| No party | "Faster responses" | "[GAP] Party not named: faster for whom?" |
| Not yet an outcome | Cannot be put in the standard form | "Not yet an outcome: [person's words]. Does not go to scoring." |
| No driver | Outcome links to no value driver | "[GAP] Contributes to no value driver yet; its value cannot be counted." |
| Driver with no outcome | A chosen driver nothing contributes to | "[GAP] No outcome contributes to [driver]; it cannot be proven." |
| No measure | Outcome held to, no measure | "[GAP] No measure yet for [outcome]." |
| No baseline | Measure with no today's level | "[GAP] No baseline for [measure]; first step is to measure it." |
| No owner | Measure with no owner | "[GAP] No owner for [measure]." |
| Not scored | A scorer did not return the sheet | "[GAP] Not scored by [name]; no score was filled in." |
| Room only | Top outcomes scored only in the room | "Scored in the room; not field-verified." (a label, not a gap, unless the field-test rule applies) |
| Not readable | Library links at levels 1 or 2 | "[GAP] The library's links are readable only at mission level." |

Rules:

- A missing library row is never evidence that an outcome does not matter.
- A missing baseline is normal at this stage; it is still listed.
- In the full report list every gap, most blocking first; merge gaps that close the same way. In a direct answer, at most three.

## Round-2 gaps and refuses (8 November 2026)

| Trigger | Action |
|---|---|
| No `evidence_basis` on the outcome set | `[GAP]` label workshop_hypothesis, elicited or quantified (WR-C2-R2-001) |
| "Validated market need" or "complete list of needs" on a workshop hypothesis | **Refuse** until elicited or quantified human evidence exists |
| Syntax lint offered as proof of validity | **Refuse**; pretest wording with intended respondents (WR-C2-R2-003) |
| Fielding without a comprehension review | `[GAP]` / refuse to field |
| Role tags missing or outside executor / buyer / influencer / other | `[GAP]`; one person may hold several roles (WR-C2-R2-002) |
| Feature request written as an outcome | **Refuse**; restate solution-independent (WR-014) |
| Job map built from operational process steps | **Refuse**; a job map is not a process map (WR-011) |
| Job steps used as investment gates | **Refuse** (WR-012) |
| Interview opened away from the execution step | `[GAP]`; start at Execute, then expand (WR-013) |
| Synthetic outcomes counted as human unmet-need evidence | **Refuse** unless `human_confirmed` (WR-C2-R2-009) |

Offline: `scripts/outcome_statement_check.py round2`.
