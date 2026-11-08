# VITAL · Target Evaluation & Due Diligence (pilot blueprint, v0.1, Draft)

CF02 plugin for capability CF-01.02.06 Target Evaluation & Due Diligence, domain CF-01 Enterprise
Strategy & Portfolio (id 49d2d80e-d9ac-44c3-8dbd-162041276806).

**Status block (8 November 2026 — hybrid honesty)**
- State: Draft **0.1.2-on-dd-e2e**. Nine skills fully kitted; ON↔DD use-case packs + return loop; **Cowork operator-ready**; E2E B1–B8 green (8 November 2026). Not Studio Marketplace Done.
- Tier design (owner ruling 7 November 2026): Full proof scoped to chain F → A → B; Standard KA for C, D, E, G, R, H (+ integrated report).
- Proof status: **Standard KA Pass** on ceremony `2026-11-08-standard-ka-v9` (D-v2-2 signed; scorecard in `diligence/smoke-archive/`). **Full F→A→B deferred** (Option C — SEC packs absent). ASC/FC defaults stay disabled. Substrate binding `20261107110000` applied 8 November 2026 after MA `20261107100000`. Do not read “tier: Full” in plugin.json as Full Done.
- Owner closeout: `diligence/OWNER_PRODUCT_CLOSEOUT_2026-11-08.md`. Pre-live audit: `diligence/PRE_LIVE_TEST_AUDIT_2026-11-08.md`. Cowork handover: `diligence/HANDOVER_COWORK_DD_LIVE_TEST_2026-11-08.md`.
- World-class research: diligence prompts DD-C1…C6 authored; absorb still **Partial** across clusters.
- Review: not yet reviewed by a named practitioner (Q8 pending). Living gaps: `diligence/HONEST_GAP_REGISTER.md`.
- Grounding: every method step, script constant, template field and detection question in all nine skills is traced to a registered verbatim passage (`references/verbatim-passages.json`) or labeled ENGINEERING RULE with a reason. A row without a registered passage is [CHECK] and is never scored.
- [CHECK] means a rule, figure or status not re-opened against a dated primary document. [GAP] means a missing fact. Neither is ever filled.
- Claims rule: nothing is called validated, proven or complete without the evidence the register shows.
- Examples are fictional. Their fact patterns cite registered passages; the real names behind them are kept in a local, non-shipped appendix.

**Owner rulings built in:** buyers are pharma business development (BD) and life-sciences investors;
units are a single asset or a company (company = one run per pipeline asset, then a roll-up); markets
are US and EU only, anything else is [GAP]; the revenue and price skill (R) works country by country (US, DE, FR, IT, ES, UK), never as one EU price.

## What is in this plugin
| Part | Path | Role |
|---|---|---|
| Recommended agent | agents/bd-due-diligence-lead.md | WORKER: reuses an existing agent row; scope, gates |
| Capability map | skills/target-evaluation-due-diligence-capability-map/ | 3 clusters as mission SOPs; all 9 competencies and their status |
| Full skill A | skills/review-clinical-data-quality/ | CF-01.02.06.1.2: builds the evidence register |
| Full skill B | skills/estimate-development-risk-and-timeline/ | CF-01.02.06.1.3: probability and timeline ranges (needs A) |
| Full skill C | skills/assess-ip-portfolio-and-freedom-to-operate/ | CF-01.02.06.3.2: exclusivity register (patents, extension or SPC, regulatory exclusivities, license chain, disputes); no freedom-to-operate conclusion |
| Full skill D | skills/evaluate-regulatory-pathway-and-legal-risk/ | CF-01.02.06.3.3: US and EU pathway map and legal-and-regulatory risk register (needs A, B and C); no legal opinion |
| Full skill E | skills/analyze-financial-statements-and-tax/ | CF-01.02.06.3.1: financial register (runway with filed going-concern language, financing and dilution, licensor obligations, commitments, tax flags); company, asset and investor modes; no accounting or tax opinion |
| Full skill F | skills/assess-scientific-validity-and-moa/ | CF-01.02.06.1.1: mechanism register (target, human evidence, preclinical translatability, reproduction, biomarkers, class precedent, differentiation); feeds A and B; no scientific go/no-go |
| Full skill G | skills/evaluate-market-opportunity-and-competitive-position/ | CF-01.02.06.2.1: market register (population with source, year and geography; competitors with dated sources; differentiation tied to registers A and F); no sales, price or access figure |
| Full skill R | skills/forecast-revenue-and-price-ranges/ | CF-01.02.06.2.2: unrisked, undiscounted revenue and price RANGES country by country; list price from dated public sources, net price as a named deal-team assumption, erosion only from supplied sourced parameters, sensitivity for every driver, probability of success shown not applied; needs G, B, C; Market Access side by side only; adopted forecast human only |
| Full skill H | skills/determine-commercial-viability/ | CF-01.02.06.2.3: peak-sales range from analogs and the option set GO, CONDITIONAL GO, NO-GO (needs G); reads A, B, C, D, F; reads the revenue register (condition C-RV) and the Market Access hand-off for coverage and access; no decision |
| Connectors | connectors.md | Confirmed tool names, use for / never for |
| Commands | commands/dd-clinical-risk-check.md; commands/dd-legal-risk-check.md; commands/dd-finance-check.md; commands/dd-commercial-check.md; commands/dd-integrated-report.md | Start the Scientific & Clinical mission (mechanism register first); start the IP and regulatory-legal steps; start the financial register; start the market register then the viability options; assemble the integrated diligence report from the eight outputs (closing step; deal lead decides) |
| Automation | automations/regulatory-precedent-watch.md | Recurring watch of regulatory precedent sources |
| Report template | templates/integrated-diligence-report.md and .schema.json | Section order of the integrated report (answer in three lines, proposed status table, top risks, conflicts side by side, open gaps, decision options, sign-off) |
| Report tool | tools/assemble_report.py, tools/test_assemble_report.py | Deterministic assembler: validates every line's register pointer, proposes statuses and checks conflicts by stated rules (team-set defaults, client may override); no recommendation, no new finding |
| Report evals | evals/dd-integrated-report/ | Five functional evals with fictional fixtures (all clear, conflicts, missing output, company mode, attempted recommendation); frozen with checksums |
| Lint | tools/lint_plugin.py | Structure check against the authoring standard, including the integrated-report files |

## Depends on
vital-core-atoms (CF05): extract-requirements-from-source, compare-against-criteria, rank-by-consequence,
compose-draft, classify-text-labels. Package: mcps/core_atoms/plugin/vital-core-atoms/ (pilot).
Authoring standard: VITAL_SKILL_AUTHORING_STANDARD_v0.1 (in the Market Access pilot folder).

## Not covered
Risk adjustment, discounting, deal value and valuation are not covered: Revenue Forecasting & Pricing Analysis (CF-01.02.06.2.2) is built as unrisked, undiscounted ranges only and hands off to a future valuation capability. Local and regional coverage and access stay with the Market Access pack (cross-check only). Valuation of intangible assets (the IVSC standards and the AICPA
in-process R&D guide) was not opened and is not used.

The integrated diligence report is a plugin-level command (/dd-integrated-report), not a competency: it assembles the registers and adds no finding of its own; it recommends nothing, and the deal lead decides (human only). Its status colors are proposed by a stated engineering rule and are not a standard.
