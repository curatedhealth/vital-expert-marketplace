# Grounding register

One row per asset item of this skill: method step, task card, template, script constant or list, failure-mode detection question, example, eval fixture. Status: VERIFIED-REOPENED (cites registered passages in `verbatim-passages.json`) or ENGINEERING RULE (no external source; the reason and the gap are stated). **No item is UNGROUNDED**; `tools/lint_plugin.py` checks the rows. A "practitioner" mark means a practitioner article that is not a standard. Written 7 November 2026 (upgrade lane C, D, E, G, H).

| Item type | Item | Status | Passage ids or reason |
|---|---|---|---|
| step | step 1 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 2 | VERIFIED-REOPENED | the horizons the filing must discuss are Item 303 (VP-E-001, VP-E-003); the filed going-concern language is quoted from the filing, never judged |
| step | step 3 | VERIFIED-REOPENED | the 12-month and one-year flags are VP-E-001 and VP-E-051; the burn bases and scenarios are the plugin's (ENGINEERING RULE, gap stated: no standard for a burn calculation) |
| step | step 4 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 5 | ENGINEERING RULE | licensor-obligation steps; a redacted term is a GAP with a request (VP-E-012, VP-E-013); the obligation type list is the plugin's; gap stated: no standard |
| step | step 6 | ENGINEERING RULE | contingent commitments and tax attributes are flagged for specialists; recognition criteria are practitioner statements (VP-E-030, VP-E-031) and section 382 and 172 limits are statutory (VP-E-020 to VP-E-024); the flags are the plugin's; the opinions are human only |
| step | step 7 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 8 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 9 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| step | step 10 | ENGINEERING RULE | quality of earnings, net debt, accounting and tax opinions are human only (owner ruling); no source for the practice was found (E13) |
| step | step 11 | ENGINEERING RULE | workflow design choice of this skill; gap stated: no published standard prescribes this step of a drug due diligence |
| task card | 01-liquidity-and-going-concern.md | VERIFIED-REOPENED | Item 303 VP-E-001 to VP-E-003; going-concern horizon VP-E-050, VP-E-051 |
| task card | 02-runway.md | VERIFIED-REOPENED | horizons VP-E-001, VP-E-051; scenario and burn-basis design is the plugin's (ENGINEERING RULE in the constants rows) |
| task card | 03-financing-and-dilution.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 04-licensor-obligations.md | ENGINEERING RULE | card sequence is the plugin's; redaction handling VP-E-010 to VP-E-013; gap stated: no standard |
| task card | 05-commitments-and-tax-flags.md | ENGINEERING RULE | card sequence is the plugin's; tax statutes VP-E-020 to VP-E-025; contingency criteria VP-E-030, VP-E-031 (practitioner, not a standard) |
| task card | 06-claims-crosscheck-and-data-room.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| task card | 07-failure-modes-questions-and-register.md | ENGINEERING RULE | follows the skill's output contract (answer first, then evidence rows); gap stated: no published standard prescribes this card sequence |
| template | financial-register.md | ENGINEERING RULE | section structure is the decision-ready order of anatomy 3.6 with this skill's register fields; a house format, gap stated: no published reporting standard exists for a diligence register |
| constant or list | FIN-HORIZON-12M | VERIFIED-REOPENED | VP-E-001, VP-E-003; unit test matches the wording |
| constant or list | FIN-AUDITOR-1Y | VERIFIED-REOPENED | VP-E-050, VP-E-051; unit test matches the wording (PCAOB page, browser-confirmed) |
| constant or list | FIN-ASC205-40-ISSUE (disabled) | ENGINEERING RULE | rule disabled; gap stated: the FASB text could not be opened (E3, SUMMARY-ONLY); no look-ahead rule is applied |
| constant or list | TAX-382-OWNERSHIP-50PT, TAX-382-TESTING-3Y, TAX-382-LIMIT-FORMULA | VERIFIED-REOPENED | VP-E-020 to VP-E-023; govinfo statute text; unit tests |
| constant or list | TAX-172-NOL-80PCT (flag only) | VERIFIED-REOPENED | VP-E-024; enabled in the grounding lane; the IRS rate source is named (VP-E-025), no rate value is used |
| constant or list | FIN-REDACTED-TERMS (E_REDACTED) | VERIFIED-REOPENED | VP-E-010, VP-E-012, VP-E-013; a redacted term is a GAP with a request for the unredacted agreement; unit test |
| constant or list | MAX_MONTHS = 60 | ENGINEERING RULE | search ceiling of the runway loop; a runway beyond it prints ">60"; reason: a runway above five years is not decision-relevant against a 12-month filing horizon (VP-E-001) and the loop must stop; gap stated: no source sets a ceiling |
| constant or list | BURN_BASES (4) | ENGINEERING RULE | closed set of burn bases the person chooses from; gap stated: no published standard for a burn calculation |
| constant or list | opinion-phrase patterns and human-only fields | ENGINEERING RULE | keep quality of earnings, net debt, accounting and tax opinions human only (owner ruling) |
| constant or list | cross-check result labels (consistent / inconsistent / not found) | ENGINEERING RULE | closed label set; gap stated: no standard |
| detection question | FE-01 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the example filing was not re-registered (FE-01 is [CHECK]); redaction handling is VP-E-012, VP-E-013 |
| detection question | FE-02 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the example filing was not re-registered (FE-02 is [CHECK]) |
| detection question | FE-03 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the failure case is VP-D-090 |
| detection question | FE-04 | ENGINEERING RULE | Detection question written for this skill; gap stated: no published detection checklist; the requirement is VP-E-001, VP-E-003, VP-E-051 |
| example | good-fictional-register.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| example | poor-certification.md | ENGINEERING RULE | fictional asset; each fact pattern is mapped to registered passage ids in the file; real names only in the local appendix docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md |
| eval fixture | good-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | good-runway-input.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval fixture | poor-register.json | ENGINEERING RULE | fictional input built to test one rule; not tied to a real case |
| eval set | evals/evals.json | ENGINEERING RULE | functional evals of this skill's behavior, written by the author; not tied to a real case |
