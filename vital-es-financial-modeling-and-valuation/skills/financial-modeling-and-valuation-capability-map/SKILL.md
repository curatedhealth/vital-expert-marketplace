---
name: financial-modeling-and-valuation-capability-map
description: Use first for any valuation question on a development-stage drug asset or company in a deal, or when unsure which skill applies. Shows the three missions in Financial Modeling & Valuation, the nine competencies and their status, which skill to use when, the callers that use this capability and the interface to the ST03 deal-valuation mission. Ranges with sensitivity, never a point; no fairness or solvency view.
metadata:
  level: CF02 map
  register_code: CF-01.02.02
  version: 0.1.0
  release_state: Draft
---

# Financial Modeling & Valuation: missions and register

**Mission statement.** Give the buyer a defensible RANGE for the value of a development-stage asset or company in a deal, from inputs the due diligence registers and the deal team supply, with the sensitivity that shows what moves it. Every gap is named, never filled. The choice of discount rate, the final probability of success, the adopted valuation, any fairness or solvency view and the deal terms are human only. No fairness opinion is ever produced.

Buyers: pharma business development (licensing, M&A) and life-sciences investors (VC/PE). Units: a single asset, or a company (run per pipeline asset, then a roll-up). Markets follow the revenue skill of the due diligence plugin: US, DE, FR, IT, ES, UK. Inputs come from that plugin's registers and are never rebuilt here; a missing input is a [GAP] with its consequence and the skill to run.

## Mission: DCF & Risk-Adjusted NPV Modeling (CF-01.02.02.1)
| Step | Competency (CF04) | Status | Use when | Who |
|---|---|---|---|---|
| 1 | DCF Model Construction & Maintenance (.1.1) build-dcf-model | FULL | The revenue, timeline and exclusivity registers exist and the buyer needs the unrisked present value as a range by scenario and rate, with the terminal share. The rate is a human choice | agent, deal lead confirms; rate human only |
| 2 | Risk-Adjusted NPV Calculation (.1.2) calculate-risk-adjusted-npv | FULL | The DCF exists and the buyer needs the probability of success applied once, stage by stage, with scenario pairing. The final probability is a person's number | agent, deal lead confirms; probability human only |
| 3 | Assumption Documentation & Validation (.1.3) validate-valuation-assumptions | FULL | A model exists and the buyer wants nine checks of its assumptions before the result is used | agent, reviewer signs |

## Mission: Scenario & Sensitivity Analysis (CF-01.02.02.2)
| Step | Competency | Status | Use when | Who |
|---|---|---|---|---|
| 1 | Multi-Scenario Model Design (.2.1) design-valuation-scenarios | FULL | The buyer needs the drivers with ranges, the standard low / mid / high by a stated pairing rule and the named scenarios the team wants. Weights are the team's | agent, deal lead defines scenarios |
| 2 | Sensitivity & Tornado Analysis (.2.2) analyze-valuation-sensitivity | FULL | An rNPV model exists and the buyer needs swings, a tornado ranking and switching values on scales the team supplies | agent, deal lead supplies scales |
| 3 | Decision-Relevant Scenario Communication (.2.3) communicate-valuation-scenarios | FULL | The registers exist and a decision owner needs a memo with a pointer on every line, the decisions needed and their owners. Refuses recommendation and fairness language | agent, reviewer signs; decision human only |

## Mission: Benchmarking & Comparable Analysis (CF-01.02.02.3)
| Step | Competency | Status | Use when | Who |
|---|---|---|---|---|
| 1 | Comparable Transaction Identification (.3.1) identify-comparable-transactions | FULL | A person supplies candidate deals with dated sources and the team has criteria. The skill screens, flags selection bias and fetches nothing | agent, reviewer confirms exclusions |
| 2 | Benchmark Analysis & Term Comparison (.3.2) compare-deal-terms-to-benchmarks | FULL | A screened set of deals with terms exists and the buyer wants ranges per term with leave-one-out and the subject's position (not a verdict) | agent, reviewer signs |
| 3 | Market Standard Synthesis (.3.3) synthesize-market-standard-terms | FULL | Benchmarks and the rNPV range exist and the buyer wants them side by side with thin-data flags and caveats, never merged. Which range informs the negotiation is a person's decision | agent, reviewer signs; decision human only |

Count: 9 FULL, 0 DRAFT STUB, 0 NOT IN THIS RELEASE = 9 competencies in 3 missions with 3 competencies each [M: count of the three tables above, 7 Nov 2026]. "FULL" describes the kit (all files and the calculators with tests); the tier is provisional and no skill is back-tested.

## Closing step: valuation summary (plugin-level command, not a competency)
| Step | Command | Use when | Who |
|---|---|---|---|
| Closing | /val-summary (tools/assemble_valuation_summary.py, templates/valuation-summary.md) | Registers of the missions exist, in whole or in part, and the buyer wants one summary: the model range with its pointer, workstream status (proposed green / yellow / red by a stated rule), conflicts side by side, open gaps and what each blocks, and the decisions needed with owners | tool assembles; agent checks; the deal lead (BD head or investment lead) confirms the statuses and decides: human only |

The summary adds no finding of its own: every line points to a register, and a line without a valid pointer fails. It recommends nothing and certifies nothing.

## Callers (named only; ruling V1)
This capability owns deal and asset valuation. The following competencies call it or may read its registers; none is created, edited or linked by this plugin: CF-01.02.04.1.2 M&A Valuation & Financial Modeling; CF-01.04.02.1.3 Acquisition Valuation & Financial Modeling; CF-01.04.01.2.2 Commercial & Financial Valuation; CF-01.02.05.2.1 Probability-Weighted Portfolio Valuation; CF-01.02.05.2.3 Scenario-Based Valuation & Stress Testing; CF-01.01.01.2.1 Asset Valuation & rNPV Modeling; CF-02.01.03.1.1 Pipeline Valuation & Probability-of-Success Estimation; CF-01.02.01.3.2 Real Option Valuation & Modeling; and, on the due diligence side, CF-01.02.06.2.3 Commercial Viability Determination [M: live inventory, docs/due_diligence/CF-01.02.02_INVENTORY_2026-11-07.md section 4].

## Interface to the ST03 deal-valuation mission (ruling V8)
The ST03 deal-valuation mission is a productization of the Consultation Mission (specification only; implementation pending). It is read-only for this plugin. This capability FEEDS it with registers: the DCF and rNPV ranges (V1, V2), the assumption checks (V3), the scenario and sensitivity registers (V4, V5), the decision memo (V6) and the comparables and benchmark registers (V7 to V9). The mission consumes them by register pointer; it does not replace them, and this plugin edits no ST03 file.

## What is not here
No fairness opinion, solvency view or recommended price. No real-options engine. No deal database. The WIPO valuation text is a guide, not a standard; the IVS text used is the 2025 edition (approaches in IVS 103; the "IVS 105 / 200 / 210" numbering in the brief is corrected to IVS 103 and 210).
