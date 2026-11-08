# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason is stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks that every step, task card, template, failure mode, constant, example and fixture has a row. Written 7 November 2026; regraded 7 November 2026 in the grounding lane (rows added and converted where a registered passage states the rule; "practitioner" marks a practitioner article that is not a standard).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | the one-message intake with a missing-input rule is the anatomy's house format (3.2); no published standard prescribes diligence intake |
| step | step 2 | ENGINEERING RULE | extracting facts with a locator per fact is a house rule (nothing from memory); the facts are the document's |
| step | step 3 | VERIFIED-REOPENED | applies the four ICH E9(R1) estimand attributes and the five intercurrent-event strategies: VP-A-020 to VP-A-029 |
| step | step 4 | VERIFIED-REOPENED | applies the five RoB 2 domains, judgement levels and the overall rule: VP-A-001 to VP-A-011 |
| step | step 5 | ENGINEERING RULE | replication, safety and precedent labels are house closed sets; US precedent source is the FDA surrogate table (VP-A-050, VP-A-053), the EU statement is [CHECK] (M12); the safety step follows the phases of a peer-reviewed pharmacovigilance playbook (VP-A-130, VP-A-131; practice source, authors disclose employment at Takeda) but that source says no formal framework exists, so the step order is the plugin's |
| step | step 5 (single-arm and externally controlled credibility) | VERIFIED-REOPENED | asks whether the protocol, control data and analysis plan were fixed before the trial and whether the endpoint isolates the treatment effect: FDA draft external-control guidance (DRAFT; VP-A-101, VP-A-104), EMA reflection paper (VP-A-111, VP-A-113, VP-A-114), ICH E10 2.5.2 (VP-A-120 to VP-A-122). The two field names and the label sets are the plugin's |
| step | step 6 | ENGINEERING RULE | the screen uses the closed answer set triggered / not triggered / cannot tell so that no mode ends as a free-text maybe; house rule |
| step | step 7 | ENGINEERING RULE | the script step runs the deterministic checks of this skill; each check is graded in the constants and rules rows below |
| step | step 8 | ENGINEERING RULE | the human gate is the owner's ruling for this skill (the person decides, the skill prepares); not a published standard |
| task card | 01-extract-trial-facts.md | ENGINEERING RULE | the order follows the skill's output contract (answer first, then evidence rows); no published standard prescribes this diligence sequence |
| task card | 02-state-the-estimand.md | VERIFIED-REOPENED | ICH E9(R1) attributes and strategies: VP-A-020 to VP-A-029 |
| task card | 03-judge-risk-of-bias.md | VERIFIED-REOPENED | RoB 2 domains, levels, overall rule: VP-A-001 to VP-A-011 |
| task card | 04-replication-safety-precedent.md | ENGINEERING RULE | house closed label sets; US precedent from the FDA table VP-A-050, VP-A-053; the single-arm part of this card is graded in its own row |
| task card | 04-replication-safety-precedent.md (single-arm credibility check) | VERIFIED-REOPENED | FDA draft guidance VP-A-101, VP-A-104; EMA reflection paper VP-A-110 to VP-A-114; ICH E10 VP-A-120 to VP-A-122; unit tests match the wording |
| task card | 05-screen-failure-modes.md | ENGINEERING RULE | the screen uses the closed answer set triggered / not triggered / cannot tell so that no mode ends as a free-text maybe; house rule |
| task card | 06-validate-and-write.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, no published reporting standard exists for a diligence register |
| template | evidence-register.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, no published reporting standard exists for a diligence register |
| template | register.schema.json | ENGINEERING RULE | machine-readable schema of the register row; fixed by the register template (house format) |
| constant or list | ROB_DOMAINS (5) | VERIFIED-REOPENED | VP-A-003 to VP-A-007; unit test matches each name |
| constant or list | ROB_LEVELS (3) | VERIFIED-REOPENED | VP-A-008; unit test |
| constant or list | ROB_EFFECTS (assignment, adherence) | VERIFIED-REOPENED | VP-A-011 (effect of assignment and effect of adhering) |
| constant or list | ESTIMAND_ATTRIBUTES (4) | VERIFIED-REOPENED | VP-A-020 to VP-A-024; unit test |
| constant or list | IE_STRATEGIES (5) | VERIFIED-REOPENED | VP-A-025 to VP-A-029; unit test |
| constant or list | RoB 2 overall rule | VERIFIED-REOPENED | VP-A-009, VP-A-010 |
| constant or list | MODE_STATES | ENGINEERING RULE | closed answer set so a screen cannot end as a free-text maybe |
| constant or list | SOURCE_TYPES | ENGINEERING RULE | house classification by proximity to the regulatory record; FM-07 (VP-A-083 to VP-A-085) documents why a press release is not that record; a practitioner article states that primary sources are more credible than summaries (VP-A-151, practitioner, not a standard); no published classification of source types for diligence exists |
| constant or list | WEAK_SOURCES | ENGINEERING RULE | company_press and conference_abstract; the Lurie study covers press releases only, so the second type is added by analogy (stated in the code) |
| constant or list | REPLICATION | ENGINEERING RULE | closed label set for classify-text-labels; GAP records absence |
| constant or list | MARKETS | ENGINEERING RULE | owner ruling: US and EU only |
| constant or list | REQUIRED row fields | ENGINEERING RULE | fixed by the register template (house format) |
| constant or list | SAT_PRESPECIFIED labels (true / false / GAP) | ENGINEERING RULE | closed set for the question the FDA draft and the EMA paper ask (VP-A-101, VP-A-104, VP-A-114); the set is the plugin's; the questions are sourced |
| constant or list | EFFECT_ISOLATION labels (unambiguous / not unambiguous / GAP) | ENGINEERING RULE | closed set for the EMA definition of isolating a treatment effect (VP-A-111) and the statement that scenarios without unambiguous isolation are a critical risk (VP-A-113); the three labels are the plugin's |
| constant or list | EXTERNAL_CONTROL_CAUTION flag (no numeric discount) | VERIFIED-REOPENED | ICH E10 2.5.2: external controls need much more extreme significance and much larger estimated differences (VP-A-121) and suit only dramatic effects of a predictable course (VP-A-122). No source gives a number, so the validator sets none (a unit test checks that no discount constant exists); the size of any discount is the reviewer's judgement |
| constant or list | external-control and single-arm guidance status | VERIFIED-REOPENED | the FDA external-control guidance is a DRAFT ("Not for Implementation", VP-A-100 source row M15); the EMA reflection paper is final (adopted 9 September 2024; two reference numbers recorded, M16) |
| detection question | FM-01 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-02 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-03 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-04 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding is registered from the NLM copy of the OIG report (VP-A-160 to VP-A-163), counts as of the report date |
| detection question | FM-05 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-06 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-07 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| detection question | FM-08 | ENGINEERING RULE | Detection question written for this skill: no published detection checklist exists; the finding it screens for is in the failure-modes row (passage ids there, or none where the row is SUMMARY-ONLY) |
| example | good-fictional-two-trials.md | ENGINEERING RULE | fictional asset; each fact pattern traces to a cited real precedent listed in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-press-release-and-unknown.md | ENGINEERING RULE | fictional asset; each fact pattern traces to a cited real precedent listed in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
