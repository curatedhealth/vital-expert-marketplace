---
name: target-evaluation-due-diligence-capability-map
description: Use first for any target evaluation or due diligence question on a drug asset or a life-sciences company, or when unsure which skill applies. Shows the three missions in Target Evaluation & Due Diligence, the nine competencies and their status, and which skill to use when. US and EU only, except the revenue skill, which is country by country (US, DE, FR, IT, ES, UK).
metadata:
  level: CF02 map
  register_code: CF-01.02.06
  version: 0.1.0
  release_state: Draft
---

# Target Evaluation & Due Diligence: missions and register

**Proof hygiene (8 November 2026).** Competency rows below still say FULL as the *designed* kit surface. Hybrid honesty: Standard KA **eng precheck** green (independent grade pending); Full F→A→B **not frozen**; Marketplace/prod **Deferred**. See `diligence/WORLD_CLASS_TRACKER_DD_C1_C6.md` and `.claude-plugin/plugin.json` `tier_proof_status`.

**Mission statement.** Give the buyer a board-defensible view of whether the asset's clinical evidence
supports its plan, its likely probability and timing of approval, its exclusivity position and the regulatory
routes and legal risks around it. Every gap is named, never filled. Legal opinions and the freedom-to-operate
opinion are human only.

Buyers: pharma business development (licensing, M&A) and life-sciences investors (VC/PE). Units: a single
asset, or a company (run per pipeline asset, then roll up). Markets: US and EU; anything else is [GAP]. The revenue and price skill works country by country (US, DE, FR, IT, ES, UK); there is no "EU" price.

## Mission: Scientific & Clinical Due Diligence (CF-01.02.06.1)
| Step | Competency (CF04) | Status | Use when | Who |
|---|---|---|---|---|
| 1 | Scientific Validity & MOA Assessment (.1.1) assess-scientific-validity-and-moa | FULL | The buyer needs to see how well the target, mechanism and class are supported before the clinical data are read: human genetic or clinical evidence, preclinical translatability, independent reproduction, target-engagement biomarkers, class precedent, differentiation. The scientific go/no-go is a named scientist's judgment | agent, scientist reviews; go/no-go human only |
| 2 | Clinical Data Quality Review (.1.2) review-clinical-data-quality | FULL | Clinical data exist (or are claimed) and the buyer needs a register of what they show | agent, human review |
| 3 | Development Risk & Timeline Estimation (.1.3) estimate-development-risk-and-timeline | FULL | The register is signed off and the buyer needs probability and timing ranges | agent, human owns final number |
| 4 | Decision on fit, terms or bid | n/a | Ranges and register ready | human only |

## Mission: Commercial & Market Assessment (CF-01.02.06.2)
| Step | Competency | Status | Use when | Who |
|---|---|---|---|---|
| 1 | Market Opportunity & Competitive Positioning (.2.1) evaluate-market-opportunity-and-competitive-position | FULL | The buyer needs the patient population with source, year and geography, the standard of care, the competing marketed products and pipeline with dated sources, and the asset's differentiation tied to the clinical and mechanism registers. It states no sales, price or access figure | agent, reviewer signs |
| 2 | Revenue Forecasting & Pricing Analysis (.2.2) forecast-revenue-and-price-ranges | FULL (validated with a Standard-tier known-answer set) | The market register, the timeline ranges and the exclusivity register exist and the buyer needs unrisked, undiscounted revenue and price RANGES country by country (US, DE, FR, IT, ES, UK): list price from dated public sources, net price as a named deal-team assumption, loss-of-exclusivity erosion only from supplied sourced parameters, a sensitivity table for every driver and the probability of success shown beside the ranges. Risk adjustment, discounting and deal value belong to a future valuation capability; the adopted forecast is human only. Market Access outputs appear only as a side-by-side cross-check | agent, reviewer signs; adopted forecast human only |
| 3 | Commercial Viability Determination (.2.3) determine-commercial-viability | FULL | The market register is signed and the buyer wants a peak-sales range from analogs and the option set GO, CONDITIONAL GO, NO-GO with conditions. Price and revenue ranges come from the revenue skill (condition C-RV); coverage and access come from the Market Access pack (a gap until it is Released). The commercial decision is human only | agent, reviewer signs; decision human only |

## Mission: Financial & Legal Due Diligence (CF-01.02.06.3)
| Step | Competency | Status | Use when | Who |
|---|---|---|---|---|
| 1 | Financial Statement & Tax Analysis (.3.1) analyze-financial-statements-and-tax | FULL | The buyer needs cash and runway with the filed going-concern language, financing and dilution, upstream licensor obligations, contingent commitments and tax attributes flagged, from filed documents (company mode), or only the counterparty's ability to perform and inherited license obligations (asset mode). Quality of earnings, net debt, accounting and tax opinions are human only | agent, accountant, tax specialist and counsel review; opinions human only |
| 2 | IP Portfolio & Freedom-to-Operate Assessment (.3.2) assess-ip-portfolio-and-freedom-to-operate | FULL | The buyer needs patents, expiry with extension or SPC, regulatory exclusivities, the license chain and live disputes, with questions for counsel. The freedom-to-operate opinion is a legal act | agent, counsel reviews; opinion human only |
| 3 | Regulatory Pathway & Legal Risk Evaluation (.3.3) evaluate-regulatory-pathway-and-legal-risk | FULL | The clinical register is signed, the ranges and the exclusivity register exist, and the buyer needs the US and EU routes and the legal-and-regulatory risk register | agent, regulatory reviewer and counsel review; route choice and legal opinion human only |

Count: 9 FULL, 0 DRAFT STUB, 0 NOT IN THIS RELEASE = 9 competencies in 3 missions with 3 competencies each [M: count of the three tables above, 7 Nov 2026].

## Closing step: integrated diligence report (plugin-level command, not a competency)
| Step | Command | Use when | Who |
|---|---|---|---|
| Closing | /dd-integrated-report (tools/assemble_report.py, templates/integrated-diligence-report.md) | The registers of the missions exist, in whole or in part, and the buyer wants one report: workstream status (proposed green / yellow / red by a stated rule), top risks, conflicts between workstreams shown side by side, open gaps and what each blocks, and the decision options sign, sign with conditions, do not sign with their conditions | tool assembles; agent checks; the deal lead (BD head or investment lead) confirms the statuses and decides: human only |

The report adds no finding of its own: every line points to a register row of one of the nine skills, and a line without a valid pointer fails. It recommends nothing and certifies nothing. A missing skill output is a GAP for that workstream (status proposed red) with its consequence and the skill to run. The count of nine competencies is unchanged: the command is a plugin-level tool (recorded in the build log as an anatomy proposal).

## Practitioner anchors for the workflow and the decision memo
No published standard prescribes the order of a drug due diligence or the form of its decision memo. The order and the options below follow practitioner articles, which are **not standards and not peer-reviewed** (the registered passages are in `skills/review-clinical-data-quality/references/verbatim-passages.json`, rows M18 to M20 of its method standards). Where no practitioner source applies, the step stays an ENGINEERING RULE.

| Workflow element | Practitioner source | What it supports | Status of the plugin step |
|---|---|---|---|
| An initial screen for fit before in-depth work (intake first, then the registers) | Seimetz 2020, Goethe Business School blog (VP-A-140) | screen first to leave time for assets that match | practitioner label; the plugin's intake is its own format |
| Asset data read by discipline (clinical, nonclinical, safety, regulatory, commercial, legal, IP) | same (VP-A-141) | the eight skills are organised by discipline | practitioner label |
| Findings reported with a traffic-light style severity | same (VP-A-142) | the plugin reports flags and a triggered / not triggered / cannot tell screen, which is similar but not identical | ENGINEERING RULE for the closed answer set |
| A closing recommendation of three options (sign, sign with provisions, do not sign) | same (VP-A-143) | the plugin's GO, CONDITIONAL GO, NO-GO option set in skill H parallels it; the plugin never recommends one, the decision owner decides | the parallel is a practitioner label; "no ranking, no recommendation" is the owner's ruling |
| A pharmacovigilance workstream with phases from document review to targeted safety domains | Youssef and Hammad 2026, Drug Saf (VP-A-130, VP-A-131; peer-reviewed playbook; authors employed by Takeda) | the safety step in skill A | peer-reviewed practice source, not a standard |
| Source hierarchy: primary sources over summaries; deal-killers are data integrity and undisclosed material information | Walker and Hepler, Alacrita blog (VP-A-150, VP-A-151; commercial interest, undated) | the plugin's regulator-record-first rule | practitioner label |
| No honest quantitative probability for a program with no clinical precedent | same (VP-A-152) | the plugin's refusal to fill a probability where no benchmark stratum exists | practitioner label |

The order of the three missions inside the capability map, the use of one signed register per skill before the next skill runs, and the human gates are the owner's rulings, not sourced.

## Relations
- review-clinical-data-quality CAN FOLLOW assess-scientific-validity-and-moa (the mechanism register feeds the clinical register; without it, a register row whose mechanism rationale is a GAP stays a GAP)
- estimate-development-risk-and-timeline REQUIRES review-clinical-data-quality (and reads the class and evidence-chain flags of assess-scientific-validity-and-moa as inputs a person weighs)
- assess-ip-portfolio-and-freedom-to-operate CAN FOLLOW review-clinical-data-quality (it has no hard prerequisite and may run in parallel)
- evaluate-regulatory-pathway-and-legal-risk REQUIRES review-clinical-data-quality, estimate-development-risk-and-timeline and assess-ip-portfolio-and-freedom-to-operate
- analyze-financial-statements-and-tax is standalone in company mode (no hard prerequisite); its licensor obligations are a cross-check for the ownership and license chain of assess-ip-portfolio-and-freedom-to-operate
- assess-scientific-validity-and-moa RECOVERS a clinical-register row whose mechanism rationale is a GAP
- evaluate-market-opportunity-and-competitive-position CAN FOLLOW review-clinical-data-quality and assess-scientific-validity-and-moa (its differentiation claims point to their registers); it has no hard prerequisite
- forecast-revenue-and-price-ranges REQUIRES evaluate-market-opportunity-and-competitive-position, estimate-development-risk-and-timeline and assess-ip-portfolio-and-freedom-to-operate (patients, launch years and approval years, exclusivity end dates); it is unrisked and undiscounted and leaves risk adjustment and discounting to a future valuation capability
- determine-commercial-viability REQUIRES evaluate-market-opportunity-and-competitive-position, reads the signed register of forecast-revenue-and-price-ranges for price and revenue (condition C-RV) and reads review-clinical-data-quality, estimate-development-risk-and-timeline, assess-scientific-validity-and-moa, assess-ip-portfolio-and-freedom-to-operate and evaluate-regulatory-pathway-and-legal-risk (exclusivity and pathway timing)
- /dd-integrated-report READS the registers of all nine skills and REQUIRES none (a missing output becomes a GAP and the report names the skill to run); the deal lead decides, human only
- Coverage and access assumptions are never built here: determine-commercial-viability reads them from the Market Access pack (vital-pharma-market-access) only when that pack is Released; the pack's price figures are only a side-by-side cross-check against forecast-revenue-and-price-ranges (owner ruling R1, 7 November 2026)

## Cleanup note
Navigator catalogue search for level 2 can miss CF-01.02.06 because the row's ont_status is "Approved"
while the default filter is "Active" (inventory section 7.1, cause confirmed). Search by code instead.
