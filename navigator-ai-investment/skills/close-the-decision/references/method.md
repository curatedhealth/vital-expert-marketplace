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
