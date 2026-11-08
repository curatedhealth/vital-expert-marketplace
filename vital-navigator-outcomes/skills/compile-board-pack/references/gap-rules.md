# Gap rules: compile-board-pack

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
| Refuse skipped gates/AIseal. | **Refuse / redirect** |
| Refuse stale approvals/erased concerns/oldPass→prod. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/board_pack_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-PACK-03: `integrity_revisions` object with non-empty revision-id strings for `ground`, `cut`, `verify` (or `verify_fallback`), `frame`; bare `ground_the_numbers`/`cut_the_slop` booleans fail; ids must not run out of order (ground ≤ cut ≤ verify|fallback ≤ frame by trailing integer); `last_material_edit_rev` newer than any stamp is stale.
- V-C6-PACK-01: every id in `prior_challenges` must appear in `pack_challenges`.
- V-C6-PACK-02: `seal_requested` true, or `ground_the_numbers` + `cut_the_slop` + `verify_status` all present, needs a non-empty list of non-empty string `underlying_evidence_refs`.
- V-C6-PACK-04: `seal_requested` true needs a named, non-AI `approved_by`.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `ai_seal, ai_proceed` | V-C6-PACK-04 |
| `delete_prior_challenge` | V-C6-PACK-01 |
| `tickbox_governance_only` | V-C6-PACK-02 |
| `boolean_integrity_without_revisions, skip_integrity_path, stale_green_after_material_edit` | V-C6-PACK-03 |
| `inherit_c1_c5_triage_as_c6_prod` | V-C6-PACK-04 |
| `signed, mlr_approved_language, launch_gate_vocabulary` | legacy [GAP] refuses |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
