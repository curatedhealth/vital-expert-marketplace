# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason and the gap are stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks the rows. A "practitioner" mark means a practitioner article that is not a standard. Written 7 November 2026 (upgrade lane C, D, E, G, H).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 2 | VERIFIED-REOPENED | route criteria and clocks are registered passages (VP-D-001 to VP-D-033); every criterion in pathway-rules.json carries passage_ids; draft status recorded (VP-D-010, VP-D-011) |
| step | step 3 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 4 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 5 | ENGINEERING RULE | statement-versus-record comparison; the finding that press releases omit most concerns is VP-D-050 and VP-D-080 to VP-D-082; the label set (match / no match / contradicts) is the plugin's; gap stated: no standard |
| step | step 6 | ENGINEERING RULE | manufacturing and inspection exposure steps; limits of public inspection data are VP-D-060 to VP-D-063 and data-integrity expectations VP-D-070, VP-D-071; the step order is the plugin's; gap stated: no published diligence standard; practitioner article R20 not re-opened |
| step | step 7 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 8 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 9 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 10 | ENGINEERING RULE | a legal opinion is counsel's act (owner ruling); not a published standard |
| task card | 01-candidate-routes.md | VERIFIED-REOPENED | routes and criteria are VP-D-001 to VP-D-033 with draft status VP-D-010, VP-D-011 |
| task card | 02-match-evidence-to-criteria.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 03-precedent-and-obligations.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 04-statement-vs-record.md | ENGINEERING RULE | comparison labels are the plugin's; the CRL publication route and the finding are VP-D-050 to VP-D-053 and VP-D-080 to VP-D-082; gap stated: no standard |
| task card | 05-manufacturing-and-compliance.md | ENGINEERING RULE | card sequence is the plugin's; inspection limits VP-D-060 to VP-D-063; data integrity VP-D-070, VP-D-071; gap stated: no published diligence checklist |
| task card | 06-litigation-and-legal-questions.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 07-write-map-and-register.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| template | pathway-and-risk.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, gap stated: no published reporting standard exists for a diligence register |
| constant or list | route criteria (19) and clocks (4) in pathway-rules.json | VERIFIED-REOPENED | VP-D-001 to VP-D-033: every criterion and clock carries passage_ids; a unit test checks that the ids resolve and that the clock numbers appear in the passages |
| constant or list | DRAFT flags (R2, R3) | VERIFIED-REOPENED | VP-D-010, VP-D-011; draft status as of 7 November 2026 |
| constant or list | dispositions, risk categories and legal-phrase patterns | ENGINEERING RULE | closed sets and patterns that keep legal conclusions out of the register; the legal opinion is counsel's (owner ruling); gap stated: no standard |
| constant or list | upstream-output requirements (A, B, C signed) | ENGINEERING RULE | the dependency order of the skills is the owner's design |
| detection question | RL-01 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | RL-02 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | RL-03 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | RL-03-OIG | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | RL-04 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | RL-05 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| example | good-fictional-pathway.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-certainty.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-pathway.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-pathway.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
