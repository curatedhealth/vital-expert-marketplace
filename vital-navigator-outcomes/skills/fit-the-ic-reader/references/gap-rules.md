# Gap rules: fit-the-ic-reader

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
| Refuse invented mandate or reader Hold→close. | **Refuse / redirect** |
| Refuse brevity hiding limits. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/reader_fit_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-READER-01: `one_pager.must_do` (alias `reader_must_do`) non-empty string; `asks` alone do not satisfy it.
- V-C6-READER-02: `one_pager.material_limits` is a non-empty list of non-empty strings when `integrity_posture` is set, OR `asks` contains a Hold, OR the reader is IC or board. If `material_limits_source` (alias `prior_limits`, top level or in `one_pager`) is supplied, every prior limit (string, or `{id, text}`) must appear in decision / turns_on / asks / material_limits, by case-insensitive substring of its text or by whole-token id.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `invent_board_mandate, reader_hold_as_close, reader_hold_as_launch_hold, require_reader_ask` | V-C6-READER-01 |
| `brevity_hides_limits, drop_qualifiers_for_length` | V-C6-READER-02 |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
