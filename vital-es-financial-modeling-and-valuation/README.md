# VITAL · Financial Modeling & Valuation (pilot blueprint, v0.1, Draft)

CF02 plugin for capability CF-01.02.02 Financial Modeling & Valuation, domain CF-01 Enterprise
Strategy & Portfolio (id 49d2d80e-d9ac-44c3-8dbd-162041276806; CF02 id 7fad2d29-5e96-49e6-bc57-8f8facd467dd).

**Status block (8 November 2026)**
- State: Draft · version `0.1.1-live-test`. Nine skills are fully kitted; Cowork live-test only — not customer Marketplace Done.
- Tier (owner ruling of 8 November 2026): Standard. Full-tier back-test remains retired (`evals/backtest/AMENDMENTS.md`). Filing-fidelity set remains optional method-fidelity, not the Standard gate.
- Known-answer status: Standard KA ceremony **Pass** on run `2026-11-08-val-ka-v2` (independent grader; D-v2-2 signed). Suite + harness + refuse smoke under `evals/known-answer/` and `diligence/`.
- Review: not yet reviewed by a named practitioner; the review pack is in `review/`, results empty.
- Grounding: every method step, script constant, template field and detection question is traced to a registered verbatim passage (`references/verbatim-passages.json`) or labeled ENGINEERING RULE with a reason. A row without a registered passage is [CHECK] and is never scored.
- [CHECK] means a rule, figure or status not re-opened against a dated primary document. [GAP] means a missing fact. Neither is ever filled.
- Claims rule: nothing is called validated, proven or complete without the evidence the register shows.
- Examples are fictional. Their fact patterns cite registered passages; no real transaction is named in the shipped plugin.

**Owner rulings built in (V1 to V9):** this capability owns deal and asset valuation; other valuation competencies are callers and are only named (V1). Scope is deal-level valuation of a development-stage asset or company, markets as in the revenue skill: US, DE, FR, IT, ES, UK (V2). Inputs come from the due diligence plugin and are never rebuilt; a missing input is a [GAP] with its consequence and the skill to run (V3). Risk adjustment and discounting live here and results are ranges with sensitivity, never a point (V4). Human only: the choice of discount rate, the adopted valuation, the final probability of success, any fairness or solvency view, and deal terms; no fairness opinion is ever produced (V5). Navigator and the repo calculators are used where they fit, offline first (V7). The ST03 deal-valuation mission is read-only; this capability feeds it (V8).

## What is in this plugin
| Part | Path | Role |
|---|---|---|
| Recommended agent | agents/valuation-analyst-proposal.md | WORKER: proposes reuse of the existing npv_analyst row; scope, gates; no row is written |
| Capability map | skills/financial-modeling-and-valuation-capability-map/ | 3 missions, 9 competencies, use-when register, callers list, ST03 interface |
| V1 | skills/build-dcf-model/ | CF-01.02.02.1.1: unrisked DCF ranges by scenario and rate; terminal-value share; no probability applied |
| V2 | skills/calculate-risk-adjusted-npv/ | CF-01.02.02.1.2: rNPV with the probability applied once, stage by stage; scenario pairing |
| V3 | skills/validate-valuation-assumptions/ | CF-01.02.02.1.3: nine checks of assumptions before a result is used |
| V4 | skills/design-valuation-scenarios/ | CF-01.02.02.2.1: drivers, pairing rule, named scenarios, coverage; no invented weights |
| V5 | skills/analyze-valuation-sensitivity/ | CF-01.02.02.2.2: swings, tornado ranking, switching values; scales supplied by the team |
| V6 | skills/communicate-valuation-scenarios/ | CF-01.02.02.2.3: decision memo structure with a pointer on every line; refuses recommendation and fairness language |
| V7 | skills/identify-comparable-transactions/ | CF-01.02.02.3.1: screens supplied deals against the team's criteria |
| V8 | skills/compare-deal-terms-to-benchmarks/ | CF-01.02.02.3.2: ranges per term, leave-one-out, subject position (not a verdict) |
| V9 | skills/synthesize-market-standard-terms/ | CF-01.02.02.3.3: ranges side by side with the valuation range, never merged |
| Connectors | connectors.md | Confirmed tool names, use for / never for |
| Commands | commands/val-dcf-check.md; commands/val-scenario-check.md; commands/val-comparables-check.md; commands/val-summary.md | One per mission, plus the valuation summary that assembles the competencies' outputs (closing step; the deal lead decides) |
| Summary template | templates/valuation-summary.md and .schema.json | Section order of the valuation summary |
| Summary tool | tools/assemble_valuation_summary.py, tools/test_assemble_valuation_summary.py | Deterministic assembler: validates every line's register pointer, proposes workstream statuses by stated rules, shows conflicts side by side; no recommendation, no new finding |
| Summary evals | evals/val-summary/ | Functional evals with fictional fixtures; frozen with checksums |
| Filing-fidelity set | evals/known-answer/filing-fidelity/ | Four cases (one held-out) rebuilt from disclosed projections and advisor ranges of public merger filings; anonymized; frozen, not run |
| Retired back-test | evals/backtest/ | Full-tier design, retired before any run (see AMENDMENTS.md); kept add-only; cases and labels stay in a local key file, not shipped |
| Review pack | review/ | Ranked Top 30 first, reviewer profiles without names, results empty |
| Lint | tools/lint_plugin.py | Structure check against the authoring standard |

## Depends on
vital-core-atoms (CF05): extract-requirements-from-source, compare-against-criteria, rank-by-consequence, compose-draft, classify-text-labels. Package: mcps/core_atoms/plugin/vital-core-atoms/ (pilot).
vital-es-target-evaluation-due-diligence (CF-01.02.06): the registers read here (revenue and price ranges, timeline and probability, exclusivity, financial). Package: mcps/due_diligence/plugin/vital-es-target-evaluation-due-diligence/.
Authoring standard: VITAL_SKILL_AUTHORING_STANDARD_v0.1 (in the Market Access pilot folder).

## Not covered
No fairness opinion, solvency view or recommended price is produced: those are an advisor's regulated acts (registered rule texts) and the people named in the registers. No real-options engine is built (the WIPO guide describes the method; no source opened here prescribes inputs). Other valuation competencies (for example brand or portfolio valuation) are callers of this capability and are named in the capability map only. The Market Access pack is read side by side only. Valuation standards behind a paywall were not opened.

The valuation summary is a plugin-level command (/val-summary), not a competency: it assembles the registers and adds no finding of its own; it recommends nothing, and the deal lead decides (human only). Its proposed statuses follow a stated engineering rule and are not a standard.
