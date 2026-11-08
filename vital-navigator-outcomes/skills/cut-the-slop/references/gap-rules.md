# Gap rules: cut-the-slop

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
| Refuse specificity through invented facts. | **Refuse / redirect** |
| Refuse lost caveats/dissent. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/substance_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-SUB-01: non-empty string `reader_need` (alias `user_need`) states what the reader needs; missing or blank fails.
- V-C6-SUB-02: `after` introduces a person name (titled name or two capitalized words) absent from `before` and not in `attributed_names` ([CHECK] heuristic).
- V-C6-SUB-03: numbers new in `after`; qualifier/dissent markers in `before` with none left in `after` ([CHECK] heuristic).

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `invent_facts_while_shortening, new_facts_in_after` | V-C6-SUB-03 |
| `invent_accountable_person` | V-C6-SUB-02 |
| `drop_dissent_or_qualifier` | V-C6-SUB-03 |
| `ignore_user_need` | V-C6-SUB-01 |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
