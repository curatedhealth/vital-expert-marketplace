# Study question and design: interpretive reference

How the sourced rows apply when framing a real-world outcomes study for a digital health product. Every rule names its row; the quotes are in the three `*-sources.md` files (read 19 October 2026). This file interprets; where it and a row disagree, the row wins.

## 1. Declare the study type first

| Rule | What it means for the study | Row |
|---|---|---|
| A HETE (hypothesis evaluating treatment effectiveness) study tests a specific hypothesis in a specific population; exploratory studies do not prespecify an effect. | The person chooses which one this is before anything else. A study cannot become HETE after outcomes are seen. | HE-025 [PAPER] Berger et al. 2017, DOI 10.1002/pds.4297 |
| Declare HETE or exploratory a priori. | The declaration goes in the protocol and in the execution record (A2). | HE-026 (DOI 10.1002/pds.4297) |
| Post the HETE protocol and analysis plan on a public registration site before analysis. | Registration date is checked against first outcome access in A2. | HE-027 (DOI 10.1002/pds.4297) |
| Test the hypothesis on a different data source and population from the one that generated it, unless not feasible. | If the idea came from your own app data, test it in claims or EHR data, or say why that is not feasible. | HE-029 (DOI 10.1002/pds.4297) |
| Include stakeholders, among them HTA bodies, payers and patients, in design, conduct and dissemination. | Ask who was consulted; record it. Patient input on DHT suitability also appears in CV25 and CV30. | HE-030, CV25, CV30 |

The Berger report's recommendation 4 is not among the sourced rows. Do not cite a fourth recommendation `[GAP]`.

## 2. Frame the question

- **PICO.** Population, intervention, comparison, outcome; not every element needs equal precision (ES-36). For a patient-facing digital product, the ISPOR Digital Health SIG framework PICOTS-ComTeC adds timing, setting, communication, technology and context: 9 domains, 32 optional subcategories (HE-032, [PAPER] Zrubka et al. 2024, abstract only; a SIG report, not a task force good practice report).
- **Estimand (ICH E9(R1)).** Five attributes: treatment condition and comparator, target population, variable, handling of intercurrent events, population-level summary (CV33, CV34). Intercurrent events are events after treatment start that change the meaning or existence of a measurement, such as stopping the app or adding medication (CV32). Strategies: treatment policy (CV35), hypothetical (CV36), composite (CV37), while on treatment (CV38), principal stratum (CV39). The protocol defines a primary estimand; protocol and analysis plan prespecify the main estimator and a sensitivity analysis (CV40). Missing data are defined against a specific estimand (CV41).
  - For an app, discontinuation is the common intercurrent event. Which strategy fits is the person's choice: treatment policy answers "what happens to people offered the app", while on treatment answers "what happens while they use it". Lay out both; do not choose.
  - E9(R1) is written for trials; applying the estimand vocabulary to an observational study is a framing choice, and the output says so.
- **Causal question in observational data.** For causal objectives, EMA's reflection paper says target trial emulation should be considered (CV107). A feasibility assessment is recommended before the protocol; it does not replace protocol and analysis plan (CV106). The EMA paper covers non-interventional studies; RWD inside trials is out of its scope (CV105).
- **Is it a trial?** If the study prospectively assigns people to the product to study a health outcome, it meets the ICMJE definition of a clinical trial (CV133) and registration rules for trials apply (CV132, CV141). Trial design belongs to dh-clinical-validation (DH-01.02.1.1); say so and point there (dh-clinical-validation `study-protocol-and-endpoint-design`).

## 3. Is the data fit for the question?

Name the framework you apply; the three sources define reliability differently (CV "Changes and conflicts").

| Framework | Reliability | Relevance | Row |
|---|---|---|---|
| ICH E6(R3) Annex 2 (trials with RWD; EU effective 15 January 2027) | accuracy, completeness, provenance, traceability | key data elements (exposure, outcomes, covariates) available for the specific question and method | CV23, CV2 |
| FDA EHR and claims guidance, drugs and biologics (July 2024) | accuracy, completeness, traceability | data on key variables and enough representative patients | CV78, CV79 |
| FDA CDRH device RWE guidance (final 18 December 2025) | accrual, quality, integrity | availability, timeliness, generalizability; linkage may fill gaps | CV88, CV91, CV92 |

Further data rules:
- Each key variable needs a conceptual definition (clinical criteria) and an operational definition (often a code algorithm) (CV80), validated with sensitivity, specificity, PPV and NPV against a reference standard (CV81).
- Claims studies address continuity of coverage and of care (CV83).
- Traceability, for example an audit trail, establishes provenance (CV82).
- Reusing a registry needs consent that covers the use, or re-consent (CV84, CV85).
- Device RWD sources include DHT data alongside EHR, claims and registries (CV89). Whether collecting RWD on a marketed device needs an IDE depends on the facts; normal-course use likely does not (CV93). That determination stays with the owner the person names for device regulatory status, or owner not named (dh-regulatory-strategy `regulatory-pathway-and-classification`).
- Linkage between sources is prespecified in the protocol, including how inconsistencies are resolved (CV24).
- App-generated measures used as outcomes need verification and validation whether or not the app is a device (CV46); a novel DHT endpoint is justified by whether it reflects how a patient feels, functions or survives (CV56); a precise endpoint definition states assessment type, timing, tool and how repeats are combined (CV55).

## 4. Outcome measures, including utilities

Which outcome a decision maker values differs by market. Match the measure to the person's target decision makers; the model does not choose the market.

| Market and body | Rule | Row |
|---|---|---|
| England, NICE | QALYs; EQ-5D preferred in adults; patients report, carers if patients cannot, not clinicians. | HE-043, HE-044 |
| England, NICE, new topics since 27 August 2026 | EQ-5D-5L with the UK 5L value set (Rowen et al. 2026) for all adult reference-case utilities; 3L data mapped to the UK 5L set with the DSU/EEPRU model; no 3L utilities in sensitivity or scenario analyses. HealthTech evaluations needing cost-utility analysis included. | HE-057 to HE-061, HE-059 |
| England, NICE, topics started before 27 August 2026 | Keep mapping 5L data to 3L utilities. PMG36 section 4.3.16 still says 3L online; PMG51 replaces it for new topics. | HE-062, HE-063, HE-046 |
| France, HAS | EQ-5D-5L with the French 5L value set in force (Andrade et al. 2020); 3L only as a transitional fallback, then mapping. | HE-106, HE-128 |
| Germany | The German 5L value set is Ludwig et al. 2018. IQWiG's reference perspective is the SHI-insured community. | HE-128, HE-110 |
| United States, ICER | EQ-5D-5L values preferred if available; two US 5L value sets exist (Pickard et al. 2019 TTO; Craig and Rand 2018 DCE). For digital health technologies ICER-PHTI emphasizes budget impact over long-term cost-effectiveness, horizon 1 year with 2 to 5 year scenarios. | HE-120, HE-129, HE-115, HE-121, HE-122 |
| NICE Evidence Standards Framework | Standard 13: describe expected health, cost and resource impacts against current care, all tiers. | HE-086 |

Which German value set a German payer expects for a DiGA is not sourced `[GAP]` (HE "Not sourced": DiGA economics not in IQWiG methods).

If the study will feed an economic model, CHEERS 2022 item 4 asks whether a health economic analysis plan exists and where (HE-006); model work belongs to dh-health-economics 2.x.

## 5. Where real-world evidence sits for decision makers

- NICE early-use HealthTech guidance can recommend use while further evidence is generated, paid from core NHS funding; listed uncertainties must be resolvable within 3 years of publication (HE-071, HE-072). The ESF early deployment subset (16 standards) is for evidence-generation programs (HE-092).
- A body of non-randomized evidence starts at low certainty in GRADE (ES-90); sound non-randomized studies are generally graded low even with ROBINS-I (ES-100). Low risk of bias due to confounding is exceptional (ES-79). Say this when the person asks what a real-world study can carry.
- EU joint clinical assessment is clinical only; economic evaluation stays national (HE-093, HE-094).
