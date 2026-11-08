# Method: the rules Close the Decision applies

Sources read 19 October 2026. Rules marked OWNER are Cowork recommendations adopted under the owner's instruction to proceed, open to change.

| Source key | Document | Version and status |
|---|---|---|
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| REG-54 | Open-items register item 54, owner decisions 18 October 2026 | O |
| TOOLS | Connector tools at commit e23025f6e: `decide_attach_scores`, `decide_release_scores`, `decide_record_dissent`, `decide_build_record`, `decide_verify_record`, `decide_prepare_signoff` | code read by Cowork from the owner checkout; tools session build record (M) |

## D1 The record

"The client-owned record of one decision taken in a decision session, in eight sections and an annex" (GOV-06 3.20; Annex A.4). The eight sections (GOV-04 §7; GOV-06 A.4): 1 Decision; 2 Value at stake (a range, and the cost of a wrong decision); 3 Outcome priorities; 4 Capability and gap register; 5 Options considered, always including doing nothing or doing it internally; 6 Recommendation and route; 7 Assumptions and risks; 8 Dissent. OWNER ruling 3: the record assembles the earlier reports into these sections; a missing section stays `[GAP]`, never filled.

## D2 People score; release by a named person

"Outside critical decision points, AI shall not give scores or sign on anyone's behalf" (GOV-06 6.6.3). Scores are given privately before discussion (GOV-06 6.1.4). Attached scores are stored unreleased; a stage read returns "[GAP] unreleased"; release stores the releaser's name; a missing name or an AI author does not release (TOOLS). OWNER ruling 1: release only once every scorer has submitted.

## D3 Dissent

"Dissent shall be recorded and shall not be averaged away. A dissent field that is present and empty shall be distinguishable from one that is absent" (GOV-06 6.6.5). The dissent tool takes text, or an attestation of none, with the person's name; both at once, or an AI author, is refused (TOOLS). OWNER ruling 2: every record carries one or the other; dissent gathered in earlier stages is carried in by its holders' names.

## D4 The result is the owner's

Results: Proceed · Investigate first · Handle it internally (GOV-04 §9). "The calculator does not choose the result"; verification "cannot choose" (TOOLS). At a critical decision point "a named, qualified person shall decide and accept responsibility" (GOV-06 6.6.2).

## D5 A valid gate

A review gate is valid only if it shows the evidence trail, names a qualified reviewer, offers dissent as a structured field, and records the decision and who carries responsibility (GOV-06 6.6.4; GOV-02 R-GATE). Gates of a decision session: "Gate 1 Decision Contract · Gate 2 priorities attested · Gate 3 record signed by two people, one of them the decision-owner" (GOV-04 §9); gates 1 to 3 are always critical (GOV-02 §11.3).

## D6 Prepared here, signed in the app

The connector prepares and reads back; the governed record, scoring and signing live in the app's session flow; connector briefs are labeled drafts (REG-54, owner decision 1, 18 October 2026). The sign-off tool names who the record is prepared for and never writes "signed" (TOOLS). OWNER ruling 5: the skill prepares the record for two named signers, one of them the owner, and states that signing happens in the Navigator app.

## D7 Verification

The verify tool checks the built record; it cannot choose the result (TOOLS). The skill's script checks the eight sections, the result wording, dissent, release and signers before preparing sign-off (OWNER ruling 4).

## D8 Facilitated, then one report

One question per turn, then one full report (references/facilitation.md).

## Lane A absorb — authority, log, DQ checklist (7 November 2026)

| Rule | Source | Plugin action |
|---|---|---|
| Record Decide authority; group needs resolution rule | Bain RAPID 2023 — LA-BAIN-RAPID | `record_check.py` authority block |
| Close with durable decision log / consequential recap | Bain 2011 — LA-BAIN-LOG / WR-008 | Closing block in record template |
| Optional six-requirement completeness; never AI DQ % | SDG — LA-SDG-SIX / WR-002 | `decision_quality_checks` |
| Process quality ≠ outcome luck | SDG — LA-SDG-LUCK / WR-009 | Hand to portfolio review separately |

Owner close vocabulary (Proceed / Investigate first / Handle it internally) remains OWNER — not Bain/SDG.

## C6 Governance absorb (8 November 2026)

Integrity path (locked): ground-the-numbers → cut-the-slop → handoff-verify **or** explicit not-tool-checked → frame-exhibits-honestly → compile-board-pack / close-the-decision.

### Method inserts
- references/method.md: Human close/scope/reasons/issues/actual authorization, separate from AI draft.
- references/method.md: Preserve dissent, active assumptions, validity/reopen conditions and human review.
- references/method.md: Link current ground/cut/Verify-or-fallback/frame/pack revisions.

Lane A: `references/lane-a-sources-c6-2026-11-08.md`. Quotation rights for C6 are **unknown** until owner clears VP-ON-C6 — do not inherit C4/C5 internal clearance.

## C6 validator-aligned method (C6 Phase 1, 8 November 2026)

Each named section below matches a content check in `scripts/record_check.py`. The check fails on the packet itself with no confess flag; flags are secondary (see `gap-rules.md`). Rule ids and dispositions: `diligence/V_C6_RULE_CODE_CONTENT_MATRIX_2026-11-08.md`.

### Dissent preserved (V-C6-CLOSE-01)
Dissent is a record field, never prose that can quietly disappear. Carry in earlier dissent by holder name. `prior_dissent_present: true` or `prior_dissent_ids` means section 8 must hold those entries (same `id`, named `by`). A present-but-empty dissent list with an erase marker (`erased`, `erased_by`, `redacted`, ...), an entry whose text is only a redaction word, or a 'none' attestation while earlier dissent exists all fail. LA-C6-004 supports keeping reasons and issues in the record; its guidance is nonmandatory, so the rule here is a house rule.

### Reopen conditions (V-C6-CLOSE-02)
Compression for the board must not strip the conditions under which the decision is reopened. When the decision needs them (`requires_reopen_conditions: true`), a non-empty `reopen_conditions` must sit at the top level or in section 6 or 7. CLOSE-01 and CLOSE-02 are separate rules and separate gaps: erased dissent is not the same failure as dropped reopen conditions.

### Assumption lifespan (V-C6-CLOSE-03)
Each section 7 assumption that can expire carries `expires_on` and a `review_by` no later than that date (ISO dates). Name an owner for each. LA-C6-006 treats an assumptions log with version control as part of analytical documentation.

### Human close and vocabulary (V-C6-CLOSE-04, V-C6-CLOSE-05)
The result is one of Proceed, Investigate first, Handle it internally, chosen by a named person who is the decision owner; two different named signers, one of them the owner. A reader's Hold is a register entry, not a Navigator result. Signing happens in the Navigator app.

### Integrity revisions link (V-C6-PACK-03, close link)
A close packet (signers present, a chosen result, or `require_integrity_link: true`) carries `integrity_revisions` with non-empty ids for `ground`, `cut`, `verify` or `verify_fallback`, and `frame`. Copy them from the board pack; do not mint ids.

### Lane A cites (C6 catalogue)

Catalogue: `references/lane-a-sources-c6-2026-11-08.md`. Cited by id and locator only; no passage is reproduced. Quotation rights for C6 stay `unknown` until the owner clears VP-ON-C6.

| Id | Source | Used for | Transfer boundary |
|---|---|---|---|
| LA-C6-004 | Corporate Governance Code Guidance (FRC, 2024); Executive summary; Decision-making; Outcomes; board papers | decision records keep reasons and issues; challenge survives compression (CLOSE-01, CLOSE-02) | Nonmandatory guidance, not a universal page limit, register or signer count. |
| LA-C6-006 | The AQuA Book, 2025 edition (Analysis Function and partners); 1.3; Ch2 logs/documentation/version control; Ch3 proportionality; 4.2.1; Ch5 roles; Ch9 signoff | assumption log with review conditions; roles separate preparation from authority; sign-off (CLOSE-03, CLOSE-04, PACK-03 close link) | Transfer analytical assurance, not legal roles or the exact VITAL pipeline. |
