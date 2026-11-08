# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason and the gap are stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks the rows. A "practitioner" mark means a practitioner article that is not a standard. Written 7 November 2026 (upgrade lane C, D, E, G, H).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 2 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 3 | ENGINEERING RULE | ownership and license chain steps; gap stated: no standard prescribes them; practitioner anchor for chain of title VP-C-130 (WIPO SME article, not a standard) and the failure case VP-C-120 to VP-C-122 |
| step | step 4 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 5 | VERIFIED-REOPENED | dates are computed from the statutes and regulations registered in VP-C-001 to VP-C-081; each rule id points to its passages and a test matches the number to the passage text |
| step | step 6 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 7 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 8 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 9 | ENGINEERING RULE | the freedom-to-operate opinion is human only (counsel); a landscape is not an FTO opinion (VP-C-100, VP-C-101); the human-only boundary is the owner's ruling |
| task card | 01-patent-family-table.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 02-ownership-and-license-chain.md | ENGINEERING RULE | chain-of-title steps follow the practitioner IP map (VP-C-130, not a standard) and the failure case VP-C-120 to VP-C-122; the card fields are the plugin's; gap stated: no standard |
| task card | 03-disputes-and-challenges.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 04-exclusivity-dates.md | VERIFIED-REOPENED | statutory and regulatory periods VP-C-001 to VP-C-081; conventions are labeled CONVENTION in the output |
| task card | 05-failure-modes-and-questions.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 06-write-register.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| template | exclusivity-register.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, gap stated: no published reporting standard exists for a diligence register |
| constant or list | US exclusivity periods (NCE 5y, NCI 3y, ODE 7y, PED +6m) | VERIFIED-REOPENED | VP-C-001, VP-C-050, VP-C-020, VP-C-021; unit test matches each number |
| constant or list | US biologics (12y, 4y filing bar, +6m pediatric) | VERIFIED-REOPENED | VP-C-030, VP-C-031, VP-C-033; known-answer tests |
| constant or list | US GAIN (+5y; stacks with pediatric; not for 262(a)) | VERIFIED-REOPENED | VP-C-040, VP-C-041, VP-C-042; known-answer tests (enabled in the grounding lane) |
| constant or list | US PTE rules (half testing phase, 14-year cap, 5-year cap, 60-day filing, one patent, diligence reduction) | VERIFIED-REOPENED | VP-C-010 to VP-C-017; unit tests |
| constant or list | EU data and market protection (8y, 10y, 11y) | VERIFIED-REOPENED | VP-C-070 to VP-C-073; unit tests |
| constant or list | EU orphan (10y, 12y with PIP, 6y) | VERIFIED-REOPENED | VP-C-080, VP-C-081, VP-C-065; unit tests |
| constant or list | EU SPC (duration, 5-year maximum, +6m pediatric, 6-month filing) | VERIFIED-REOPENED | VP-C-060 to VP-C-064; unit tests (original OJ text; the consolidated text was not opened) |
| constant or list | US-NCE1-4Y (disabled) | ENGINEERING RULE | rule disabled; gap stated: the closing condition of 355(j)(5)(F)(ii) was not registered (S19); no rule is applied |
| constant or list | date conventions (whole days, calendar months, testing half rounded down) | ENGINEERING RULE | the statutes do not fix these conventions; each output marks them CONVENTION; gap stated: counsel confirms to the day |
| constant or list | claim-type list and FTO-phrase patterns | ENGINEERING RULE | closed claim types and phrase patterns that detect an FTO assertion; the opinion is human only (VP-C-101 says an FTO report is a legal opinion) |
| constant or list | REQUIRED row fields | ENGINEERING RULE | fixed by the register template (house format) |
| detection question | IP-01 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the finding is VP-C-110 to VP-C-112 |
| detection question | IP-02 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | IP-03 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist exists; the finding it screens for is in the failure-modes row |
| detection question | IP-04 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the failure case is VP-C-120 to VP-C-122 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-fto-assertion.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-exclusivity-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
