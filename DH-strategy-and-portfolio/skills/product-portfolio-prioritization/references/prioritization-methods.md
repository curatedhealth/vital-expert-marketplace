# Prioritization methods for a product portfolio

Interpretive reference. Every rule cites its row in `strategy-and-portfolio-sources.md` (SP rows, read 20 October 2026). Rows marked [PAPER] carry their DOI; rows marked [WF] were read through a summarizer and are said to be so whenever applied. Nothing here sets a weight, a score, a threshold, a probability or a target: those are the person's.

## 1. The decision problem comes first

The ISPOR MCDA Emerging Good Practices Task Force, Report 2 (Marsh et al. 2016, DOI 10.1016/j.jval.2015.12.016; [PAPER], [WF]) sets eight steps: defining the decision problem; selecting and structuring criteria; measuring performance; scoring alternatives; weighting criteria; calculating aggregate scores; dealing with uncertainty; reporting and examining findings (SP-074). For a product portfolio forum this means, in order:

| Step | In this skill | Row |
|---|---|---|
| Decision problem | A1: the forum, the period, the items asking to continue, stop or delay | SP-074 |
| Criteria | B1 step 2: the person's criteria, complete, without double counting, preference-independent | SP-076, SP-077, SP-078 |
| Performance | A1 facts beside each item, with source; `[GAP]` stays visible | SP-074 |
| Scores and weights | The person's, 0 to 4, weights summing to 1; written back for confirmation | SP-074, SP-081 |
| Aggregate | `analytics.mcda` (EVIDEM weighted sum) or `analytics.rice` on the person's numbers | `tools.md` |
| Uncertainty | Swap points; `analytics.scenario-modeler` and `analytics.risk-tornado` on the person's inputs and ranges | SP-074, `tools.md` |
| Reporting | B1 output: rank, contributions, flips, the item placed last | SP-074, SP-075 |

Checks the task force states, applied as questions to the person (all [PAPER] [WF], DOI 10.1016/j.jval.2015.12.016):
- Criteria "should capture all factors relevant to the decision" (SP-076) and "be defined to avoid double counting" (SP-077). Example of double counting in a portfolio: "evidence readiness" and "probability of technical success" both scored from the same pivotal readout.
- Preference independence: "how much one cares about the performance on a criterion should not depend on the performance of other criteria" (SP-078).
- Weighting: swing weighting and decompositional approaches best produce weights that act as scaling constants; direct rating "tend[s] to produce flatter weight distributions" (SP-079). Say which method the person used; the method is theirs.
- Validation in each step, reported (SP-075); consistency can be tested by eliciting preferences more than once and presenting results back (SP-081).
- MCDA is "a tool to help decision makers reach a decision: their decision, not the tool's decision" (SP-080; the row joins "decision" and "their decision" with a dash, replaced here by a colon).

ISPOR Report 1 (definitions and approach types) was not read: `[GAP]` (sources file, "Not sourced").

## 2. Write the rule before ranking

The old skill's method (register CF-12.01.03.3.1.2): state the rule, apply it to the choice list, show the item the rule placed last, and "do not change the rule after you see the rank you prefer". In this skill the rule is written back and confirmed before any calculator is called, and the confirmation is kept in the output. A rule the person changes after seeing a rank is recorded as a new rule with its reason, beside the first; both ranks are shown.

A rule has three parts, all the person's: the criteria and weights (or RICE inputs), the decision rule that turns a rank into continue, stop or delay (for example "continue the top items until the named capacity is used"), and the capacity with its unit and period.

## 3. RICE as an alternative

`analytics.rice` returns reach x impact x confidence / effort ("RICE Prioritization", the tool's citation McClure 2016, Intercom: a vendor method note, not a sourced row). Use it only when the person's rule is RICE. Confidence goes in as a percent (`tools.md`, register N5). RICE carries no evidence, regulatory or capacity criterion unless the person folds one into impact or effort: say so.

## 4. Option appraisal language (UK public-sector guidance)

The UK Green Book 2026 (HM Treasury, updated 5 February 2026, earlier editions withdrawn, SP-088) is UK central-government guidance. When a company uses its terms, label them "UK public-sector guidance, applied by analogy":
- Appraisal assesses "the costs, benefits and risks of different options for achieving government objectives"; it does not set objectives (SP-089).
- Longlist to shortlist, with one shortlisted option labeled the "preferred way forward" (SP-094); the options framework filter is recommended, not mandated (SP-095). In this skill a preferred way forward is always "proposed" and the person's to name.
- Business as usual is the baseline: "the outcome that is expected if current arrangements continue" (SP-093). Offer "stop" or "continue as now" as the baseline item when the person compares options for one program.
- Optimism bias: appraisals adjust by "increasing estimated costs and timeframes, and decreasing estimated benefits" (SP-096). Without its own historical evidence, a public body can use the generic values in the supplementary guidance (Green Book 2026, SP-171). That guidance (HM Treasury, "Green Book supplementary guidance: optimism bias", gov.uk page of 21 April 2013, never updated, not withdrawn; the content is a 2003 document built on a 2002 Mott MacDonald review, SP-170) gives these values:

| Project type (Table 1) | Works duration, upper / lower | Capital expenditure, upper / lower | Row |
|---|---|---|---|
| Equipment/development (includes software, systems and ICT development, SP-173) | 54% / 10% | 200% / 10% | SP-172, SP-173 |
| Standard buildings | 4% / 1% | 24% / 2% | SP-172 |
| Non-standard buildings | 39% / 2% | 51% / 4% | SP-172 |
| Standard civil engineering | 20% / 1% | 44% / 3% | SP-172 |
| Non-standard civil engineering | 25% / 3% | 66% / 6% | SP-172 |
| Outsourcing | n/a | 41% / 0% (operating expenditure) | SP-172 |

  How the guidance says to use them: the upper bounds are the average historic bias at outline business case stage for traditionally procured projects, "indicative starting values", and earlier stages may need more (SP-174); start at the upper bound and reduce it by a mitigation factor between 0.0 and 1.0 for each contributory factor managed, aiming for the lower bound by contract award (SP-175); there are no sound bounds for operating costs (except outsourcing) or for benefits shortfall, so use sensitivity analysis and switching values instead (SP-176). For a company these are UK public-sector guidance, applied by analogy, built on 2002 data: context, never the person's adjustment. If the person wants an adjustment, the project type, the mitigation and the size are theirs, and the run is labeled theirs (`analytics.scenario-modeler`, `tools.md`).

## 5. Development benchmarks: context with their counting method

| Figure | Counting method and dataset | Row | DOI |
|---|---|---|---|
| 13.8% of drug development programs reach approval | Path-by-path, 406,038 trial entries, 2000 to 2015 | SP-082 | 10.1093/biostatistics/kxx069 |
| Oncology 3.4% in the sample, against 5.1% in prior studies | Same paper; the paper says only "prior studies" for the 5.1%, and separately that extant literature uses the phase-by-phase method (SP-085) | SP-083, SP-085 | 10.1093/biostatistics/kxx069 |
| Biomarker-selected trials had higher success probabilities | Same paper | SP-084 | 10.1093/biostatistics/kxx069 |
| Path-by-path against phase-by-phase: a model must state its basis | Method definition | SP-085 | 10.1093/biostatistics/kxx069 |
| Oncology/immunology longest average study duration, 3.9 years | Top 30 pharma, clinicaltrials.gov, 2000 to 2020 | SP-086 | 10.1186/s40545-023-00612-6 |
| Higher phases correlated with longer duration (+0.36) | Same dataset | SP-087 | 10.1186/s40545-023-00612-6 |

All [PAPER]. These are drug-program figures; no row gives a success rate for software, SaMD, DTx or medtech programs `[GAP]`. Rules: quote a figure only with its method and dataset; never present it as the person's probability; never mix figures from different methods in one model (SP-085); never use a benchmark as a target. When the person supplies their own probability, it is labeled "yours" in every table.

## 6. Readiness levels (EU wording for health products)

EU TRL definitions, Horizon Europe Work Programme 2026-2027, General Annexes, Annex XV, applying "where the specific call/topic conditions require a Technology Readiness Level (TRL)" (SP-028). Apply verbatim:

| Level | EU wording | Row |
|---|---|---|
| 1 | "Basic principles observed" | SP-029 |
| 2 | "Technology concept formulated" | SP-029 |
| 3 | "Experimental proof of concept" | SP-029 |
| 4 | "Technology validated in a lab" | SP-029 |
| 5 | "Technology validated in a relevant environment (industrially relevant environment in the case of key enabling technologies)" | SP-030 |
| 6 | "Technology demonstrated in a relevant environment (industrially relevant environment in the case of key enabling technologies)" | SP-030 |
| 7 | "System prototype demonstration in an operational environment" | SP-031 |
| 8 | "System complete and qualified" | SP-031 |
| 9 | "Actual system proven in an operational environment (competitive manufacturing in the case of key enabling technologies, or in space)" | SP-031 |

NASA's nine levels share the scale but tie levels 7 to 9 to space and flight ("demonstrated in a space environment", "flight proven", SP-035); do not copy NASA's terms for a health product. A TRL is a technology maturity scale, not a regulatory or evidence status: device status routes to `dh-regulatory-and-quality` regulatory-pathway-and-classification, evidence to `dh-clinical-development` literature-and-real-world-evidence-review. The level assigned to an item is "proposed" until the person confirms it, and the fact behind it is shown.

## 7. Delay options: routes that buy information

When the person considers "delay pending evidence", these sourced routes can be listed as facts for the option, never as advice:
- FDA early feasibility study: "a limited clinical investigation of a device early in development, typically before the device design has been finalized", generally fewer than 10 initial subjects (SP-110); appropriate when device changes are expected and the information cannot practically come from more nonclinical testing (SP-111); not statistically powered but needs specified purposes and meaningful endpoints (SP-115). The guidance predates the QMSR (SP-118). Program steps start with a Pre-Submission (SP-119); open to PMA, 510(k), De Novo and HDE routes (SP-120).
- FDA TAP Pilot, expanded on 1 July 2026 to all OHTs for Breakthrough and STeP devices; 159 devices enrolled as of 7 October 2026 (SP-122; the count is dated and changes).
- MHRA IDAP pilot: closed to new applicants (SP-124).
- NHS AI and Digital Regulations Service: plan evidence early, consistent with intended purpose and value proposition (SP-127); one study can serve regulator and commissioner (SP-128); device status is the developer's call (SP-129).

Which route applies to an item is for `dh-regulatory-and-quality` regulatory-pathway-and-classification and the person's regulatory owner.

## 8. Value of information

When the person asks what new evidence is worth before a delay decision, that is a value of information analysis. Its source rows are not copied into this skill `[GAP]`; the model is built in `dh-access-and-value` economic-model-development.

## Not sourced here

Portfolio size targets, hit rates for digital health companies, innovation maturity targets (sources file, "Not sourced"), OKRs, stage-gate and real-options papers, AstraZeneca 5R full text, ISPOR MCDA Report 1: `[GAP]`. Optimism bias values for operating costs (other than outsourcing) and for benefits shortfall do not exist in the guidance (SP-176). The person supplies any such figure, labeled theirs.
