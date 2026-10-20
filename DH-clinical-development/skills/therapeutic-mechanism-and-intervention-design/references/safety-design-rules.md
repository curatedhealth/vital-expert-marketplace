# Safety-by-design rules

Interpretive reference for A4 (safety by design). Every rule cites its row in `safety-and-engagement-research.md` (SE) or `therapeutic-mechanism-research.md` (TM). A4 lists the risks to health that the mechanism (A1), the components (A2) and the engagement mechanics (A3) can create, the mitigations the person proposes, and the labeling elements that the special controls name. It does not hold the risk file, rate severity or probability, decide that a risk is acceptable, or decide that a classification applies. Those belong to `dh-regulatory-and-quality` design-controls-and-risk-management and to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

A4 never calls a product, a component or a mechanic "safe". It reports a hazard, the mitigation the person chose, and the open items.

## 1. Where risks to health come from (hazard sources the records name)

| Hazard source | What the record or source states | Rows |
|---|---|---|
| Software failure | reSET: "Device software failure, leading to delayed access", mitigated by software verification and validation that the therapy is correctly implemented and accessible when needed. | SE11 |
| Ineffective treatment | reSET: mitigated by a validated therapy method, clinical data, software V&V that the model was correctly implemented, and labeling. | TM139 |
| Use error | reSET: use error mitigated by labeling, including a user guide with screenshots. | SE12, SE13 |
| Displacement of face-to-face care | reSET: the adjunct warning exists because patients "typically have medical and psychiatric comorbidities that may be detected and addressed in face-to-face clinician therapy sessions". | SE12 |
| Displacement of more effective interventions, inappropriate advice, data sharing | Digital interventions can harm in these ways. | SE89 (Michie 2017, DOI 10.2196/jmir.7126) |
| Engagement mechanics | EndeavorRx risk table: seizure, screen addiction, decreased sleep quality; frustration, emotional reaction, dizziness, nausea, headache, eye-strain or joint pain. | SE16, SE17 |
| Reward logic | reSET and reSET-O recalls of 7 June 2021 (Class II): wheel spin granted "regardless of the UDS results". | `examples/live/connector_calls_2026-10-20.json` (`search_safety_events {product_code: "PWE"}`) |
| Missed escalation | MHRA example of a reportable incident: a mental health tool fails to alert a clinician when the user's status reaches a predetermined clinical threshold. | SE36 |
| Wrong population | MHRA example: an assessment tool that inadequately describes its intended population, used on a 15-year-old with evidence only in adults. | SE37 |
| AI conversation | MHRA: chatbots might enable suicidal thoughts or delusions; a VR malfunction could cause disorientation or anxiety. | SE35 |
| Labeling, design and user error as contributors | 21 CFR 803.3: "caused or contributed" includes failure, malfunction, improper or inadequate design, labeling and user error; a malfunction includes failing any claim made in the labeling. | SE39, SE40 |

How to apply: walk the A1 chain, the A2 components and the A3 mechanics. For each, ask the person which of these sources could apply, and write the hazard in their words, tied to the link, component or mechanic it comes from. The model may list candidate hazards labeled "proposed". Severity, probability and acceptability are the person's and go into the risk file, not into A4.

## 2. What the special controls name (context for design)

Special controls in 21 CFR are binding for the device type they name. Whether one applies to the person's product is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question. Adverse-event wording differs by regulation: quote the exact one (research file "Changes and conflicts" 2).

| Regulation (device type) | Safety and labeling elements it names | Rows |
|---|---|---|
| 882.5801 computerized behavioral therapy, psychiatric | Software verification, validation and hazard analysis; labeling with instructions and images showing how to interact, compatible devices, a warning that it does not replace medication; validated model as implemented | SE1, TM120, TM121, TM122 |
| 882.5803 ADHD digital therapy | Capture of all adverse events; labeling with minimum operating system and a warning that it is not a standalone therapeutic device | SE2, TM123 |
| 882.5804 fibromyalgia (codified 26 June 2026) | Evaluation of relevant adverse events; hazard analysis showing the device performs as intended; labeling with a clinical summary including adverse events | SE3 |
| 882.5705 sleep disturbance | Validated measure of increased disturbed sleep or sleepiness; minimum operating system and computing requirements | SE4 |
| 886.5500 amblyopia (codified 22 April 2026) | Evaluation of all adverse events; display compatibility testing; labeling of minimum hardware and validated display models | SE5, SE6 |
| 880.5735 diabetes (codified 24 July 2026) | Clinical data showing no adverse impact on health outcomes; hazard analysis of all device-related adverse events showing minimal patient risk; limiting statements (not standalone, not a substitute, not for unstable psychiatric disorders) | SE7, SE8 |
| 876.5960 gastrointestinal | Evaluation of all adverse events; a warning to seek care for thoughts of harming oneself or others | SE9 |
| 890.5800 VR for pain | Warnings on nausea, motion sickness and discomfort; EMC and electrical, mechanical and thermal safety testing | SE10 |

FDA described earlier special controls for these devices as device-specific: clinical data, non-clinical testing, software and labeling (SE24). The DHAC Executive Summary is not draft or final guidance (SE22).

## 3. Mitigation patterns the records show (precedent context, not a requirement)

| Pattern | Record | Rows |
|---|---|---|
| Pause and stop instructions | EndeavorRx labeling: pause on frustration or physical symptoms; on seizure, stop and contact the provider; cautions for photosensitive epilepsy, color blindness and physical limits. | SE20 |
| Session limits | EndeavorRx regimen enforced by lock-out and reminders. | TM142 |
| Adjunct framing | reSET warning that it is not standalone; 880.5735 limiting statements. | SE12, SE8 |
| Escalation plan | DHAC (non-binding): a pre-existing escalation plan with the clinician; an in-app single-tap escalation for additional support. | SE25 |
| Role disclosure for AI | DHAC (non-binding): make clear the AI is not a human therapist; labeling with overuse warnings and crisis information. | SE28 |
| Children | DHAC (non-binding): monitor and limit screen time; monitor adverse events in trials and real-world use. | SE29 |

## 4. Decisions that link design to post-market monitoring

| Rule | Rows |
|---|---|
| EU: expected side-effects clearly documented in the product information and quantified in the technical documentation go to trend reporting, not individual serious-incident reports; unquantified ones are not excluded. Whether to document and quantify a side-effect (for example frustration in a game therapy) is a design decision for the person and their regulatory owner. | SE59; research file "Changes and conflicts" 6 |
| EU (MDCG 2025-10, not legally binding): indicators and threshold values that trigger action are set in the premarket phase and re-evaluated with post-market data. | SE60, SE63 |
| US: a malfunction is a failure to meet performance specifications, which include all labeling claims. | SE40 |
| Adverse events in published digital mental health trials are under-reported: MHRA cites a study finding 26 percent reported them in the primary paper (MHRA's citation of Gomez-Bergin 2023; the study itself was not read). | SE34 |

The person sets the indicators and thresholds in A4. Reading them after launch is `dh-clinical-development` mechanism-validation-monitoring (A4 there); whether an event is reportable is the person's or their regulatory owner's call, routed to `dh-regulatory-and-quality` audit-capa-and-complaints.

## 5. What precedents' safety records state (record facts only)

| Product | What the record states | Rows |
|---|---|---|
| reSET | Any adverse event 13 percent overall (11.5 percent treatment as usual, 14.5 percent device arm); none in the reSET arm adjudicated device-related; events watched included suicidal ideation and attempts. | SE14 |
| reSET | Not evaluated: benefit beyond 12 weeks, relapse prevention, benefit without contingency management incentives. | SE15 |
| EndeavorRx | Pivotal: "Twelve of the AEs (12/180, 6.7%) were within the EndeavorRx group", mostly transient and mild, and "No AEs led to treatment discontinuation". Pooled: 50 of 538 users (9.3 percent) with treatment-related adverse events, no serious adverse events, three discontinuations. | SE18, SE19 |

Describe these only as the records state them. Never compare them with the person's product or use them as a target.
