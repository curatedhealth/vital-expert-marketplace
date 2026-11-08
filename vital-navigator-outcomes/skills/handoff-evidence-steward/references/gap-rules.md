# Gap rules: handoff-evidence-steward

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
| Refuse invented tip/latest-changing pack. | **Refuse / redirect** |
| Refuse hash as truth/identity or inherited rights. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/steward_handoff_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-STEWARD-01: each item with a `source` carries `derived_from` (or `lineage`) AND `responsible_party`.
- V-C6-STEWARD-02: `version` not a floating label (latest, head, main, ...).
- V-C6-STEWARD-03: an item with `checksum`/`hash`/`content_hash` fails if `proves` is truth / identity / acceptance / world_truth, or `checksum_proves_truth` is true.
- V-C6-STEWARD-04: `provenance_role` of truth (or `provenance_proves_truth` true) fails; `judgment_support_only: true` is the documented ok path and `false` with provenance present fails.
- V-C6-STEWARD-06: `catalogue_record_id` must equal `resource_id` when both are given; `presented_as_returned_tip` true needs `store_available` true and `curator_tip` equal to a supplied `store_tip`.
- V-C6-STEWARD-05: `reuse_cleared` true needs `rights_basis`. (This check never sets or implies clearance; VP-ON-C6 stays `reuse_cleared: unknown`.)
- V-C6-STEWARD-07: no `curator_tip` when `store_available` is false.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `invent_curator_tip, fabricate_tip_when_empty` | V-C6-STEWARD-07 |
| `checksum_as_truth` | V-C6-STEWARD-03 |
| `rights_from_c4_c5_clearance` | V-C6-STEWARD-05 |
| `floating_latest_without_pin` | V-C6-STEWARD-02 |
| `provenance_proves_truth` | V-C6-STEWARD-04 |
| `invent_catalogue_evidence` | V-C6-STEWARD-06 |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
