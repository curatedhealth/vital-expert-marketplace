# Gap rules: ground-the-numbers

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

## Lane A gaps (7 November 2026)

- opportunity_score_as_money / satisfaction_as_operational_baseline / released_hours_labeled_cash without realization → `[GAP]`.

## C6 Governance absorb (8 November 2026)

| Situation | Action |
|---|---|
| Refuse invented values/sources/ODI money. | **Refuse / redirect** |
| Refuse provenance as truth or C5 rewrite. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/grounding_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-GROUND-01: each claim with `action` keep and non-empty `numbers` carries a non-empty `methods`, `data_assumptions` or `assumption_note`.
- V-C6-GROUND-02: each such claim also carries a non-empty string `warrant`, `inferential_warrant` or `limits` (a `source_id` or citation is evidence, not a warrant); a claim with `citation_as_truth`, `provenance_as_truth` or `provenance_proves_truth` true is refused.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `invent_figures, ai_invented_numbers, odi_to_money, opportunity_as_money, option_a_ttb_conversion, rewrite_c5_recognition` | V-C6-GROUND-03 |
| `citation_as_truth, provenance_proves_truth, missing_warrant` | V-C6-GROUND-02 |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
