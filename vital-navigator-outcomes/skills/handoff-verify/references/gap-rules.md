# Gap rules: handoff-verify

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
| Refuse support without response. | **Refuse / redirect** |
| Refuse stale result/hidden tools/quote→worldtruth. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/verify_handoff_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-VERIFY-01: a claim with `citation_generated` true, or `rationale_source` in model / ai / assistant / generated, fails when `verify_status` is `verified`, or when that claim is `tool_checked` with no `independent_check_note`.
- V-C6-VERIFY-02: `verified` + `external_ok` needs `decision_fit_attested_by`, a named person (not AI).
- V-C6-VERIFY-03: `assurance_limits` (string or list of strings) is required when `verify_status` is `not tool-checked`, any claim has `tool_checked` false, or `assurance_level` is limited/partial.
- V-C6-VERIFY-04: for `verified` or `external_ok`, distinct non-empty `author_role` (or `preparer`) and `assurance_role` (or `assurer`).
- V-C6-VERIFY-06: for `verified` or `external_ok`, every claim has `source_revision` or `passage`; any `tool_checked` claim with neither fails.
- V-C6-VERIFY-05: `assured_revision` differs from `current_revision`.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `ai_generated_citation_as_true` | V-C6-VERIFY-01 |
| `execution_ok_as_decision_fit` | V-C6-VERIFY-02 |
| `hide_limited_assurance` | V-C6-VERIFY-03 |
| `stale_verify_after_edit` | V-C6-VERIFY-05 |
| `invent_verify_status, unchecked_labeled_supported, bind_mismatch_claim_source` | V-C6-VERIFY-06 |
| `self_blessed` | legacy [GAP] refuse |

A content check proves structure, not truth, identity, authority or validity. Per-rule dispositions are in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
