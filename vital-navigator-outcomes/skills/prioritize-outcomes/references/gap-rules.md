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

## Lane A gaps (7 November 2026)

- Calling room scores a representative market study → refuse; set evidence_scope=room_workshop (LA-STRAT-NEEDS).
- Opportunity → money → refuse (LA-STRAT-OPP).

## Round-2 refuses (7 November 2026)

| Trigger | Action | Conflict / finding |
|---|---|---|
| Top-two-box or proportion inputs without documented normalization to 1–10 | **Refuse** compute; `[GAP]` primary protocol | SC-C1C2-R2-03 |
| Request to use unclamped `I+(I−S)` in production compute | **Refuse**; cite `formula_locked` | SC-C1C2-R2-04 |
| Import canvas high/high "table stakes" as plugin band label | **Refuse** automatic relabel; keep `vital_opportunity_bands` | SC-C1C2-R2-05 |
| Synthetic or AI-generated rows in human score pipeline | **Refuse** | WR-C2-R2-009 |
| Missing Importance/Satisfaction with invented fill | **Refuse** | WR-C2-R2-008 |
| Unsupported sampling-error or representativeness claim | **Refuse** | WR-C2-R2-007 |
| Sole LLM pass as construct/content validity certification | **Refuse** as complete proof | WR-C2-R2-011 |

## Deepening refuses (8 November 2026)

| Trigger | Action | Rule |
|---|---|---|
| Top-two-box raw kind or aggregation under any spelling or case (`Top-Two-Box`, `TTB`, `T2B`, `top_2_box`) | **Refuse**; aliases are normalized before the check | SC-C1C2-R2-03 |
| `owner_protocol_ref` written in another case or separator (`vital-odi-ttb-1_10-v0`) | **Refuse**; signed Option A is no conversion | SC-C1C2-R2-03 |
| `allow_unsigned_protocol_for_fixture` on anything but an all-`synthetic_fixture` run with `allow_synthetic_in_rank` | **Refuse**; the flag never applies to human evidence | WR-C2-R2-009 |
| `input_pipeline` stub (missing raw_scale_kind, instrument, respondent_count, field_dates or transformation_steps) | **Refuse**; provenance is stated, not stubbed | WR-C2-R2-004 |
| Locked 1-10 scores with a transformation step; any other raw scale | **Refuse** (needs a signed Option B protocol) | SC-C1C2-R2-03 |
| Any `formula`, `opportunity_mode` or similar key that differs from the locked formula; wording that applies I x S, (I-S) x I or drops max(0) | **Refuse** | V-C2-FORM-01 / SC-C1C2-R2-04 |
| Any money flag (`opportunity_monetized`, `odi_as_dollars`, `opportunity_to_money`, `monetize_opportunity`, `value_at_stake_from_opportunity`, `dollars_per_opportunity_point`, `from_opportunity_score`), a money field on an item or outcome, or wording that prices an opportunity point | **Refuse** (one refusal, three paths) | V-C2-UNIT-01 |
| Shared C-validator adapters missing at import | **Fail closed** (the script raises; it never runs with the gates disabled) | fail-closed |

Signed 8 November 2026: protocol `VITAL-ODI-TTB-1_10-v0` is Option A (no conversion). `landscape_label_mode` is `vital_opportunity_bands` only (SC-05).
