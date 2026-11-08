# Gap rules: design-decision-exhibits

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
| Refuse invented values/IDs or forced completion. | **Refuse / redirect** |
| Refuse ODI money/unsupported winner. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/exhibit_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-EXH-01: non-empty string `question` stating what the exhibit answers.
- V-C6-EXH-02: every series entry has `name`, `source_id` and a non-null `value`.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `decorative_without_question, no_interpretable_question` | V-C6-EXH-01 |
| `invent_exhibit_values, ai_fill_series, odi_to_money_exhibit, force_fake_completeness` | V-C6-EXH-02 |

Flag-only rules that structure cannot prove (truth, identity, authority, validity) are listed as deferred in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
