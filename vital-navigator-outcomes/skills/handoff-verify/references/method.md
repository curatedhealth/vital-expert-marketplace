# Method: handoff-verify

## Purpose
Set Verify posture on claim-bearing packs: verified | not tool-checked | claims_removed.

## Rules
1. Assistant never self-blesses accuracy.
2. external_ok only when verified and all claims tool_checked.
3. Script `verify_handoff_check.py` enforces.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Exact claim/source/passsage/locator/version/warrant and actual returned response.
- references/method.md: Actual status or explicit ordered not-tool-checked; never self-support.
- references/method.md: Bind scope/freshness to revision, support not validation/worldtruth.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/verify_handoff_check.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Assurance roles (V-C6-VERIFY-04)
When `verify_status` is `verified` or circulation is `external_ok`, record the author (`author_role` or `preparer`) and the assurer (`assurance_role` or `assurer`) as two distinct, non-empty entries. The same person or the same role in both fields fails. The assistant is neither: it never blesses accuracy (`self_blessed` is refused). LA-C6-006 transfers the analytical-assurance idea, not legal roles.

### Claim binding (V-C6-VERIFY-06)
For `verified` or `external_ok`, every claim has a `source_revision` (source plus version) or a `passage` (the supplied text checked against). A `tool_checked: true` claim with neither is an unbound response and fails, even in a pack that is otherwise internal. Unchecked claims in a `not tool-checked` pack are listed with `tool_checked: false` and need no binding.

### Renewal (V-C6-VERIFY-05)
Record `assured_revision` and `current_revision`. If they differ, content changed after assurance; run Verify again before circulating.

### Not tool-checked posture
`not tool-checked` needs at least one claim with `tool_checked: false`, is never `external_ok`, and travels with the honesty cut.

### Limits stated by hand (VERIFY-01, -02, -03 deferred)
A generated citation can be false (LA-C6-010): an unverified one stays labeled. A correct run is not proof the result fits the decision. If assurance is limited, say so in the cover note. The script cannot test these (D-C6-VERIFY-01, -02, -03).

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-006 | The AQuA Book, 2025 edition (Analysis Function and partners); 1.3; Ch2 logs/documentation/version control; Ch3 proportionality; 4.2.1; Ch5 roles; Ch9 signoff | assurance proportionate to risk, separate roles for preparer and assurer, assurance statement, renewal when content changes (VERIFY-04, VERIFY-05) | Transfer analytical assurance, not legal roles or the exact VITAL pipeline. |
| LA-C6-010 | AI RMF: Generative AI Profile, NIST AI 600-1 (2024); 2.2, 2.7, 2.8 | generated citations and rationales can be false; documentation and review expectations (VERIFY-01, VERIFY-06 context); voluntary guidance only | Voluntary risk guidance, not a Verify status schema or a reliability guarantee. |
