# Method: compile-board-pack

## Purpose
Assemble the non-gate board pack mapped to the 10-part decision record. Prepare ≠ signed.

## Rules
1. Integrity order: ground → cut → verify posture → exhibits locked → seal check.
2. Close vocabulary: Proceed / Investigate first / Handle it internally only.
3. Forbidden: MLR approved language; Launch Pass/Hold vocabulary; assistant signed=true.
4. Script `board_pack_check.py` enforces.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Owner ordered current-revision ground/cut/Verify-or-fallback/frame/pack links.
- references/method.md: Pinned manifest of claims/exhibits/evidence/QA/limits/concerns, draft distinct from authorization.
- references/method.md: Material change invalidates checks; actual human approval not green flags.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/board_pack_check.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Integrity revisions (V-C6-PACK-03)
The integrity path is ground-the-numbers, then cut-the-slop, then handoff-verify or an explicit not-tool-checked fallback, then frame-exhibits-honestly. The pack carries `integrity_revisions`: non-empty revision ids for `ground`, `cut`, `verify` (or `verify_fallback`) and `frame`. Booleans are not revisions. Order is checked by the trailing integer of each id, so `ground <= cut <= verify|fallback <= frame`. If `last_material_edit_rev` is newer than any stamp, the earlier green is stale: repeat the owner path from the first stale step. LA-C6-006 grounds versioned logs and renewal.

### Prior challenge preserved (V-C6-PACK-01)
List earlier challenge ids in `prior_challenges` and the ids the pack carries in `pack_challenges`. A challenge in the first and not the second is a gap. LA-C6-004 asks that boards see prior challenge, not only conclusions.

### Human approval only (V-C6-PACK-04)
The assistant never signs or seals (`signed` is refused). If a seal is requested (`seal_requested: true`), a named non-AI `approved_by` is required. Earlier C1 to C5 triage does not authorize C6 Marketplace or production.

### Tick-box governance (V-C6-PACK-02, deferred)
All flags green with missing underlying evidence is still a failure. By hand: for each gate, can the owner show the evidence behind it? Tracked as D-C6-PACK-02.

### Vocabulary and exhibits
Close vocabulary is one of Proceed, Investigate first, Handle it internally. At least one locked exhibit of an allowed type. No Launch gate wording and no MLR approved-language claim.

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-004 | Corporate Governance Code Guidance (FRC, 2024); Executive summary; Decision-making; Outcomes; board papers | board papers expose prior challenge and reasons, not only polished conclusions; governance is not a tick-box (PACK-01, PACK-02) | Nonmandatory guidance, not a universal page limit, register or signer count. |
| LA-C6-006 | The AQuA Book, 2025 edition (Analysis Function and partners); 1.3; Ch2 logs/documentation/version control; Ch3 proportionality; 4.2.1; Ch5 roles; Ch9 signoff | versioned logs, proportionate assurance and sign-off by named roles (PACK-03, PACK-04) | Transfer analytical assurance, not legal roles or the exact VITAL pipeline. |
