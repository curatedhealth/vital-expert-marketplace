# Gap rules

A gap is a fact the review needs that nobody has supplied or no source states. Write `[GAP]` with the reason and what would close it. Never fill one from general knowledge.

| Kind | How to word it |
|---|---|
| No declared range | "[GAP] No value range was declared; realized value cannot be placed." |
| Realized figure not measured | "[GAP] The figure is an estimate, not a measurement; not counted as realized." |
| No source or date | "[GAP] The realized figure has no source and date." |
| Unit or period mismatch | "[GAP] The realized figure is in [unit/period], the range in [unit/period]." |
| Outcome not measured | "[GAP] The outcome has no measured result; value cannot be counted." |
| Activity traces to no outcome | "Traces to no outcome: restate against one or retire." |
| No reason | "[GAP] [activity]: no reason for stop, keep or fix." |
| No steward | "[GAP] No named steward for the re-score; nothing changes." |
| Direction change with one name | "[GAP] A change to direction needs two named people." |

Who said it: the owner's statements are O; another named person's are O with their name; a relayed view is "relayed by [name]".

In the full report list every gap, most blocking first; merge those that close the same way. In a direct answer, at most three.

## C6 Governance absorb (8 November 2026)

| Situation | Action |
|---|---|
| Refuse AI Proceed/seal or Launch close. | **Refuse / redirect** |
| Refuse erased dissent/invented authorization. | **Refuse / redirect** |
| AI Proceed / seal | **Refuse** (V-C6-CLOSE / PACK) |
| Launch Pass/Hold as Navigator close | **Refuse** (V-C6-CLOSE-05) |
| Invented Verify status / empty Curator tip | **Refuse** (V-C6-VERIFY / STEWARD) |

## Confess flags (secondary)

Content and structure checks in `scripts/record_check.py` are primary: every mandatory C6 rule below fails on the packet itself with no flag set. Confess flags are secondary, an extra way for a caller to admit a refused behavior; they never replace or relax a content check, and an absent flag proves nothing.

Content checks (primary):

- V-C6-CLOSE-01: `prior_dissent_present` true or `prior_dissent_ids` not carried into section 8 dissent; section 8 empty with erase markers (`erased`, `erased_by`, `redacted`, ...); an entry whose text is only a redaction marker.
- V-C6-CLOSE-02: `requires_reopen_conditions` true with no non-empty `reopen_conditions` (top level, section 6 or section 7).
- V-C6-CLOSE-03: assumption `expires_on` needs `review_by` no later than expiry.
- V-C6-CLOSE-04 / -05: result chosen by a named non-AI person; result in the bounded vocabulary.
- V-C6-PACK-03 (close link): a close packet (signers, a chosen result, or `require_integrity_link`) needs a complete `integrity_revisions` object.

Flag names (secondary):

| Flag(s) | Rule |
|---|---|
| `dissent_erased, erase_dissent` | V-C6-CLOSE-01 |
| `erase_reopen` | V-C6-CLOSE-02 |
| `skip_integrity_link` | V-C6-PACK-03 (close link) |
| `ai_proceed, ai_seal, invent_authorization` | V-C6-CLOSE-04 |
| `launch_lex_pass_hold_as_close, launch_gate_vocabulary, reader_hold_as_close` | V-C6-CLOSE-05 |

Flag-only rules that structure cannot prove (truth, identity, authority, validity) are listed as deferred in `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.
