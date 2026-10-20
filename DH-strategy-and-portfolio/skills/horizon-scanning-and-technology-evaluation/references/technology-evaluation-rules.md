# Technology evaluation: readiness, fit and feasibility facts

Interpretive reference for task A2. Rows: SP (`strategy-and-portfolio-sources.md`), CS (`customer-success-implementation-research.md`, NICE ESF rows CS56 to CS68 only), PL (`product-lifecycle-research.md`, IDEAL-D rows PL110 to PL121 only), US, EU, UK (`ai-ml-regulation-research.md`). [PAPER] rows carry their DOI; [WF] rows are flagged.

The person decides whether a technology is fit for purpose and feasible. This skill lays out the facts per criterion, proposes a readiness level in the source's own words, and labels every level and reading "proposed".

## 1. Technology readiness level (TRL): EU wording verbatim

The EU Horizon Europe Work Programme 2026 to 2027 (General Annexes, Annex XV) defines nine levels, applied where a call requires a TRL unless otherwise specified (SP-028). Quote the level verbatim; `scripts/horizon_helpers.py trl N` prints it.

| Level | EU wording (verbatim quote) | Row |
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

Rules:
- NASA uses the same nine levels (SP-032 to SP-034), but its levels 7 to 9 assume a space environment and flight ("demonstrated in a space environment", "flight proven", SP-035). For a health product use the EU "operational environment" wording; never NASA's flight terms.
- The level is "proposed". Name the fact behind it (for example "a cleared device in use" is a register fact; whether that is "proven in an operational environment" is the person's reading).
- A TRL is not a regulatory status, a clinical evidence level or a reimbursement status. Keep them in separate columns.
- No source maps TRL to device classes, IDEAL stages or NICE ESF tiers. Do not create a crosswalk.

## 2. Is it an innovation, and what kind (Oslo Manual 2018)

Use only when the person asks how to label an item (OECD/Eurostat, 4th edition, DOI 10.1787/9789264304604-en, read from a copy hosted by the Hungarian research office, SP research Method).

| Term | Definition (paraphrase; quote in the row) | Row |
|---|---|---|
| Innovation | New or improved product or process, significantly different from the unit's previous ones, made available to users or brought into use | SP-036 |
| Product innovation | New or improved good or service introduced on the market | SP-038 |
| Business process innovation | New or improved business process for one or more business functions, brought into use | SP-039, SP-042 |
| Innovation activities | Developmental, financial and commercial activities intended to result in an innovation | SP-040 |
| Two types, not four | The 2018 edition replaced product, process, organizational and marketing with two types | SP-041 |

ISO 56002:2019 gives guidance, not requirements, for an innovation management system and covers all innovation types from incremental to radical; ISO 56001:2024 is the certifiable requirements standard (SP-044, SP-045, SP-047, all [WF]: read through a summarizer, re-check before external use).

## 3. What kind of digital intervention it is (WHO classification, second edition 2023)

Classify by the digital health intervention, a discrete capability of digital technology (SP-055), on three axes: health system challenges, digital health interventions, digital services and application types (SP-056). The second edition renamed "Systems Categories" to "Services and Application types" (SP-057). The code tables themselves were not copied into the research file: name the axis, and write the code as `[GAP]: look up in the WHO classification (SP-054)`.

## 4. Conditions the WHO 2019 guideline attaches (where the technology is one of these intervention types)

| Intervention | Condition in the recommendation | Row |
|---|---|---|
| Any | Digital interventions are not a substitute for functioning health systems | SP-049 |
| Client-to-provider telemedicine | Complements, rather than replaces, face-to-face care; safety, privacy, traceability, accountability and security can be monitored | SP-051 |
| Provider-to-provider telemedicine | Safety, privacy, traceability, accountability and security can be monitored | SP-052 |
| Health worker decision support | Only for tasks already within the worker's scope of practice | SP-053 |

The WHO global strategy lists the dimensions of appropriate use: health promotion and prevention, patient safety, ethics, interoperability, intellectual property, data security, privacy, cost-effectiveness, patient engagement and affordability (SP-062). The person may adopt these as evaluation criteria; if the skill proposes them, they are labeled "proposed criteria (from SP-062)".

## 5. Evidence and deployment facts per market

- **England (NICE Evidence Standards Framework, ECD7, last updated 9 August 2022, CS56).** 21 standards in 5 groups, with 3 deployment standards for all tiers (CS57). Standards that bear on a technology evaluation: pilot-site statements (CS59), silent-mode local performance checks for products affected by local factors such as AI (CS60), agreed usage and performance-change reporting (CS61, CS62), implementation costs (CS63), deployment data requirements (CS64), communication such as a model card (CS65), load testing (CS66), the 16-standard early-deployment subset (CS67), and the DTAC link (CS68). ESF tier names are not copied in this skill's sources: write "tier `[GAP]`" and route tiering to `dh-access-and-value` reimbursement-evidence-support.
- **Planning evidence (NHS AI and Digital Regulations Service).** Plan evidence early, consistent with the intended purpose and value proposition (SP-127); one study can serve regulators and commissioners (SP-128); whether the technology is a medical device is the developer's responsibility to determine (SP-129).
- **Device development stage (IDEAL-D, [PAPER] Marcus 2022, DOI 10.1097/SLA.0000000000004907).** IDEAL is idea, development, exploration, assessment, long-term follow-up, with development and evaluation in order (PL111); a preclinical stage 0 precedes first in human (PL112); the riskier the device, the more proof before stage 1 (PL113); study perspectives (system, patient, clinician, device) depend on risk (PL116, PL117); high-risk devices without unmet need or economic viability may not be appropriate for stage 1 (PL118). The 2016 original is abstract-only [WF] (PL121). The IDEAL stage named is "proposed".

## 6. Early clinical and regulatory routes a feasibility read can name

Facts only; whether the person's technology qualifies is for the owner the person names for regulatory matters, and pathway work routes to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

| Route | Facts | Rows |
|---|---|---|
| FDA early feasibility study (EFS) | Final guidance October 2013; limited investigation early in development, typically before design freeze, generally fewer than 10 initial subjects; appropriate when changes are expected and information cannot practically come from nonclinical tests; not powered but needs purposes, subjects and endpoints; broader changes under 5-day notice; guidance predates the QMSR (effective 2 February 2026) | SP-109 to SP-116, SP-118 |
| FDA EFS Program | Contact a representative, then a Pre-Submission before the IDE; open to PMA, 510(k), De Novo and HDE devices | SP-119, SP-120 |
| FDA TAP pilot | Early, frequent FDA communication; expanded 1 July 2026 to all OHTs for Breakthrough and STeP devices | SP-121, SP-122 |
| CMS and FDA RAPID | Medicare coverage pathway for Breakthrough devices, announced 23 April 2026; coverage questions route to `dh-access-and-value` coverage-pathway-and-access-strategy | SP-123 |
| MHRA IDAP | Pilot closed to new applicants; UCNA lets non-UKCA or non-CE devices onto the GB market for a set period with conditions | SP-124 to SP-126 |
| MHRA AI Airlock | Regulatory sandbox for AI-enabled devices; phase 3 announced 6 October 2026 | UK-06 to UK-08 |
| MHRA Innovation Office | Takes queries on products that challenge the framework; not a substitute for Scientific Advice | SP-025, SP-026 |
| EHDS secondary use | Data access may be granted for development and innovation and for training, testing and evaluating algorithms including medical devices and AI systems; Chapter IV applies from 26 March 2029 | SP-071, SP-072 |

No FDA program is called a sandbox; the only device sandbox on an official page read is the MHRA AI Airlock (SP research, "Not sourced").

## 7. Feasibility scoring: the person's criteria, applied with the MCDA rules

If the person scores feasibility, the criteria and scores are theirs. The ISPOR MCDA task force (Report 2, [PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]) asks that criteria capture all relevant factors (SP-076), avoid double counting (SP-077) and be preference independent (SP-078); swing weighting or decompositional methods give weights that act as scaling constants, while direct rating tends to give flatter weights (SP-079). Point out overlaps (for example "regulatory risk" and "time to market" scored on the same fact) as questions, not corrections. Ranking runs in B1 only on the person's scores.

## 8. What the model never supplies

A readiness verdict, a fit-for-purpose verdict, a feasibility score, a probability of clearance or adoption, a market size, a price, or a statement that a technology is safe, effective, compliant or "validated". Each stays with the person or the owner they name; the model lays out facts and labels proposals.
