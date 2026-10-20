# Precedents: what named products' records state

Facts about named products, from the FDA De Novo decision summaries (TM131 to TM144, read 20 October 2026), the connector (calls of 20 October 2026, `examples/live/connector_calls_2026-10-20.json`) and the CTN-0044 registry and abstracts (direct reads, 20 October 2026). Describe a product only by these records. A precedent shows what was stated for that product; it is never evidence for the person's product.

## reSET (Pear Therapeutics), DEN160018

| Fact | Source |
|---|---|
| De Novo granted 14 September 2017 (received 16 May 2016); created 21 CFR 882.5801; product code PWE; Class II | TM131; `regulatory-dh.get_authorization {reference: "DEN160018"}` (same dates, class "2", status "DENG") |
| Indication: cognitive behavioral therapy as an adjunct to a contingency management system, adults in outpatient treatment under a clinician | TM132 |
| Therapy model: the community reinforcement approach (CRA), a CBT variant, with contingency management | TM133 |
| Structure: 61 lessons (31 core, 30 supplemental); core lessons unlock sequentially; 4 lessons per week recommended, 10 to 20 minutes each | TM134 |
| Contingency management in software: virtual rewards for lesson completion and negative drug screens | TM135 |
| Pivotal trial NIDA CTN-0044: multi-site, unblinded RCT, 12 weeks; the control arm had no contingency management | TM136 |
| Primary outcomes abstinence weeks 9 to 12 (missing = failure) and retention; abstinence odds ratio 2.22 (all comers) and 3.17 (excluding primary opioid users) | TM137 |
| No abstinence benefit in self-identified primary opioid users (5.7 percent vs 15.9 percent): a labeled limitation | TM138 |
| FDA mitigation for ineffective treatment: validated therapy method, clinical data, software V&V that the model was correctly implemented, labeling | TM139 |
| Safety events on PWE: two Class II recalls of 7 June 2021 (reSET and reSET-O apps): "patients with a urine drug screen (UDS) received access to a contingency management wheel spin for potential rewards regardless of the UDS results"; MAUDE: 2 reports (2022: 1, 2025: 1), "counts are reports, not confirmed events" | `regulatory-dh.search_safety_events {product_code: "PWE"}` |
| reSET-O, K173681, 510(k) decided 10 December 2018, in the same product code; predicates `[GAP]` in the store | `regulatory-dh.find_predicates {product_code: "PWE"}` |
| Risks named in the decision summary: "Device software failure, leading to delayed access" (mitigated by software verification and validation); "Use error / improper device use" (mitigated by labeling, including a user guide with screenshots); the adjunct warning exists because SUD patients' comorbidities "may be detected and addressed in face-to-face clinician therapy sessions" | SE11 to SE13 |
| Trial safety: any adverse event 13 percent (n=66); none in the reSET arm adjudicated device-related; events watched included suicidal ideation and attempts | SE14 |
| Stated evidence limits: abstinence benefit not evaluated beyond 12 weeks; relapse prevention after discontinuation not studied; benefit without contingency management incentives not evaluated | SE15 |

Conflict to state when counts matter: the decision summary says 61 lessons (31 core) for the device and "all 32 core modules" for the trial (research file "Changes and conflicts" 1). The CTN-0044 main paper's abstract says "TES consists of 62 computerized interactive modules" (PMID 24700332). Three counts; none is corrected here.

## CTN-0044 records (the trial behind reSET's De Novo)

| Fact | Source |
|---|---|
| Registered as NCT01104805 ("NIDA-CTN-0044: Web-delivery of Evidence-Based, Psychosocial Treatment for Substance Use Disorders Using the Therapeutic Education System (TES)"), sponsor New York State Psychiatric Institute, completed | `literature.find_trial {nct_id: "NCT01104805"}` |
| First submitted 14 April 2010; start April 2010; primary completion June 2012 (actual); 507 enrolled (actual); masking none | ClinicalTrials.gov API, read 20 October 2026 (`examples/live/nct01104805.json`) |
| Registered primary outcome: "Reduced Substance Use and Improved Treatment Retention", time frame "12-week Treatment Phase" | same |
| Registered secondary outcomes include "Coping Skills" (12-week treatment phase, 3- and 6-months post treatment): the mediator was a prespecified outcome | same |
| Experimental arm: TES "comprised of a web-based version of the Community Reinforcement Approach and contingency management" replacing about 2 hours of standard treatment | same |
| Main paper (Campbell 2014, DOI 10.1176/appi.ajp.2014.13081055) abstract: "Additional research is needed ... to differentiate the effects of the community reinforcement approach and contingency management components of TES." The two components were not separated in this trial. | Europe PMC abstract, PMID 24700332 (`examples/live/epmc_pmid24700332.json`) |
| Mediation analysis (Levesque 2017, DOI 10.1016/j.addbeh.2016.09.012) abstract: "The effect of TES intervention on abstinence was no longer significant after controlling for coping strategies scores at week 12. Our results support the importance of coping skills as a partial mediator ..." | Europe PMC abstract, PMID 27776269; `verify.qualify_source` gold; `verify.check_claim` "partial" (see `tools.md`) |

`literature.find_trial` with the main paper returned "no linked registration found"; with the NCT id it listed five papers, not including the main paper or the mediation paper (N8).

## EndeavorRx (Akili), DEN200026

| Fact | Source |
|---|---|
| De Novo granted 15 June 2020 (received 16 April 2020); created 21 CFR 882.5803; product code QFT | TM141; `regulatory-dh.get_authorization {reference: "DEN200026"}` |
| Mechanism as described: adaptive closed-loop algorithms adjust difficulty per patient; regimen about 25 minutes per day, 5 days per week, enforced by lock-out and reminders | TM142 |
| Control: matched reward and engagement, different stimuli, no adaptive algorithms | TM143 |
| Pivotal STARS-ADHD: 348 children, primary endpoint TOVA API, 0.93 vs 0.03 (p=0.006); indication says behavioral symptoms such as hyperactivity may not improve | TM144 |
| Safety events on QFT: no recalls returned; MAUDE 2 reports (2023: 2) | `regulatory-dh.search_safety_events {product_code: "QFT"}` |
| Risk table includes seizure, screen addiction, decreased sleep quality, and frustration, emotional reaction, dizziness, nausea, headache, eye-strain or joint pain | SE16, SE17 |
| Pivotal adverse events: 12 of 180 (6.7 percent) in the device group; mostly transient and mild, 3 moderate; none led to discontinuation | SE18 |
| Pooled: 50 of 538 users (9.3 percent) had treatment-related adverse events; no serious adverse events; three led to discontinuation | SE19 |
| Labeling: stop and contact the provider on seizure; no contraindications, cautions for photosensitive epilepsy, color blindness or physical limitations | SE20 |

## Not in the store or not read

- The 2026 classifications (882.5804 fibromyalgia, 880.5735 diabetes, 886.5500 amblyopia): `regulatory-dh.search_devices {query: "fibromyalgia", jurisdiction: "US"}` returned no device; the decision summaries were not read (research file "Not sourced"). Device names for these `[GAP]`.
- Intended-use text: `get_authorization` returns no intended use (register P5); intended use comes from the decision summary rows.
- Somryst, Rejoyn and other 882.5801 clearances: not read `[GAP]`.
