# Method: handoff-evidence-steward

## Purpose
Proposal packet for the evidence steward. Never mint evidence ids.

## Rules
1. steward_id stays null until steward assigns.
2. store_available=false requires store_gap_acknowledged.
3. Script `steward_handoff_check.py` enforces.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Actual entity/activity/derivation/agent/tip lineage, not identity proof.
- references/method.md: Pin ID+revision/locator/digest, retain replacement history.
- references/method.md: Rights/access/support separate; empty stays empty; C6 rights unknown.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/steward_handoff_check.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Lineage and responsibility (V-C6-STEWARD-01)
Each item that has a `source` also carries `derived_from` (or `lineage`): what it came from and by what step, and `responsible_party`: the named person or team accountable for it. An item with only a gap note needs neither. LA-C6-008 supports recording derivation and responsibility; provenance supports a judgment about the item and is not proof it is true.

### Pinned versions (V-C6-STEWARD-02)
Give an exact `version` or date. Floating labels (latest, head, main, current, stable, `*`) fail.

### Rights are separate (V-C6-STEWARD-05)
An item marked `reuse_cleared: true` needs a `rights_basis`. Rights are separate from support and access. Quotation rights for new C6 material stay `unknown` until the owner clears them (VP-ON-C6); C4 and C5 internal clearance does not extend. This skill never sets or implies clearance.

### Empty store stays empty (V-C6-STEWARD-07)
If `store_available` is false, no `curator_tip` may appear, and `store_gap_acknowledged` must be true on the proposal. The assistant never mints evidence ids (`minted_ids` refused; `steward_id` stays null until the steward assigns).

### Checksums and catalogue (STEWARD-03, -04, -06 deferred)
A checksum supports byte integrity, not truth or identity. A catalogue entry describes a real resource and is not invented evidence. By hand; the script cannot test these (D-C6-STEWARD-03, -04, -06). LA-C6-009 transfer boundary: not a Curator API or RDF mandate.

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-008 | PROV-DM: The PROV Data Model (W3C, 2013); 2.1-2.2; 5.2-5.3; revision definition 2.2.1.1 | lineage: what an item was derived from and who is responsible; revisions (STEWARD-01, STEWARD-04) | Provenance supports assessments, not identity, truth or immutable storage enforcement. |
| LA-C6-009 | Data Catalog Vocabulary (DCAT) v3 (W3C, 2024); 6.4, 6.5, 6.8.20, 6.17, 9, 11, 13, 14 | catalogue records, versions and checksums describe a resource; they do not prove identity, truth or permission (STEWARD-02, -03, -05) | Not a Curator API or RDF migration mandate; checksum is not identity, truth or permission. |
