# Signal read rules: complaints, events, use errors and efficacy drift after release

Interpretive reference for A4 (folded in from DH-01.06.2.2 Safety & Efficacy Compliance Assessment & Therapeutic Quality Monitoring). Every rule cites its row in `safety-and-engagement-research.md` (SE). This skill reads signals against thresholds the person set before launch and lays out the definitions the rules use. Whether an event is reportable under 21 CFR 803 or 806 or MDR Articles 87 to 89, and by when, is the call of the owner the person names for vigilance reporting, or owner not named; the reporting work itself is `dh-regulatory-and-quality` audit-capa-and-complaints.

## 1. Indicators and thresholds are set before launch

| Rule | Rows |
|---|---|
| Suitable indicators and threshold values ("limits beyond which action should be taken") are established in the premarket phase; PMS data feed back into risk management and are used to re-evaluate them. MDCG 2025-10 is guidance, not legally binding. | SE63, SE60 |
| "Proactive" PMS means actively seeking information, not waiting for complaints. | SE61 |
| Sources the guidance names: customer surveys, clinical experience, user feedback, literature, registers, post-market studies; feedback through internet or digital sales channels and customer service is a PMS input (app store reviews fit here). | SE62, SE64 |
| PMS is proportionate to risk class, part of the QMS, and gathers quality, performance and safety data over the device's lifetime. | SE50, SE51 |
| PMS data are used to update benefit-risk, risk management, the clinical evaluation, and to find ways to improve usability, performance and safety. | SE52 |
| DHAC 2025 (advisory): postmarket monitoring "should mirror evidence generation in the premarket space"; data may include engagement, adherence and symptom reports. | SE27 |

So the A4 read compares only against thresholds the person set before launch (or before the period, if they say so). A threshold set after the data were read is labeled so and its comparison is reported as exploratory. Without a threshold, A4 reports counts and rates without a verdict.

## 2. Signal categories and what the rules say about each

| Category | What the sources say | Rows |
|---|---|---|
| Adverse event | US manufacturer reportable event: information that reasonably suggests a marketed device may have caused or contributed to a death or serious injury, or malfunctioned in a way likely to do so if it recurred. "Caused or contributed" includes failure, malfunction, design, labeling and user error. | SE38, SE39 |
| Serious injury (US) | Life-threatening, permanent impairment or damage, or needing intervention to prevent it. | SE41 |
| Malfunction (US) | Failure to meet performance specifications or perform as intended; performance specifications include all claims made in the labeling. | SE40 |
| Use error | FDA's reSET summary names "use error / improper device use", mitigated by labeling; FDA encourages voluntary reports of use errors and therapeutic failures. | SE12, SE13, SE49 |
| Efficacy drift | No source sets a drift threshold. The labeling-claims part of the malfunction definition (SE40) and the PMS duty to update the clinical evaluation (SE52) are the rules that touch it. The efficacy measure, its threshold and its period are the person's. | SE40, SE52 |
| Expected side-effects (EU) | Side-effects clearly documented in the product information and quantified in the technical documentation go to trend reporting rather than individual serious-incident reports; unquantified ones are not excluded. | SE59; research file "Changes and conflicts" 6 |
| Complaint or feedback | A digital-channel complaint or review is a PMS input. | SE64 |
| Software therapy harm types named by MHRA | AI chatbots enabling suicidal thoughts or delusions; a VR malfunction causing disorientation or anxiety; a tool failing to alert a clinician at a set threshold (a reportable-incident example); an adult-only tool used on a 15-year-old (inadequate description of the intended population). | SE35, SE36, SE37 |
| Reporting gap | MHRA cites a study finding only 26 percent of digital mental health trials reported adverse events in the primary results paper (secondary citation; the study itself was not read). | SE34; research file "Changes and conflicts" 12 |

The category of each event is the person's (or the owner they name). The skill counts by the category the person assigned and never reclassifies an event.

## 3. Duties that follow a signal (context; the call is the owner's)

| Duty | Rows |
|---|---|
| 21 CFR 803.50(b): investigate each event and evaluate its cause; explain incomplete reports. | SE42 |
| 803.12 and 803.20: electronic submission; patient, event, device and initial-reporter content. | SE43, SE44 |
| 803.22: no report if the information is erroneous, but documentation is kept. | SE45 |
| 21 CFR 806.2: "risk to health" for a correction or removal; 806.10(c) report content; 806.10(d) amended report within 10 working days when a correction is extended to more versions. | SE46, SE47, SE48 |
| MDR Art. 83(4): preventive or corrective action means informing competent authorities and, where applicable, the notified body. | SE53 |
| MDR Art. 84 to 86: PMS plan in the technical documentation; PMS report for class I; PSUR content and frequency (IIb and III at least annually, IIa at least every two years). | SE54 to SE58 |
| MDCG 2022-21: PSUR data periods start at MDR certification (or 26 May 2021) and run contiguously. | SE65, SE66 |
| UK: the Yellow Card site was edited to make clear digital mental health technology issues can be reported there; MHRA SaMD vigilance guidance updated 15 January 2025. | SE33, SE68 |

The skill lays these out as the rule text states. It never says an event "is reportable", "is not reportable", or "meets" a definition. Deadlines from an awareness date are computed in `dh-regulatory-and-quality` audit-capa-and-complaints.

## 4. What the precedents' records state (context only)

| Product | What the record states | Rows |
|---|---|---|
| reSET (DEN160018) | Risks named: device software failure leading to delayed access; use error, mitigated by labeling and a user guide with screenshots. Trial: 13 percent any adverse event; none in the reSET arm adjudicated device-related. | SE11 to SE14 |
| reSET and reSET-O (PWE) | Two Class II recalls of 7 June 2021 describing a software issue in the contingency management reward (`precedents.md`, live record of 20 October 2026). MAUDE counts are reports, not confirmed events. | `examples/live/connector_calls_2026-10-20.json` |
| EndeavorRx (DEN200026) | Risk table: seizure, screen addiction, decreased sleep quality, frustration and other tolerability risks. Pivotal: 6.7 percent of device-arm children had treatment-related AEs; pooled 9.3 percent of 538 users, no serious AEs, three discontinuations. Labeling: pause on frustration, stop and call the provider on seizure. | SE16 to SE20 |

A precedent shows what was recorded for that product. Its bearing on the person's product is never judged; a precedent's adverse event rate is not a threshold.

## 5. Special controls as context for what a design named

The special controls for software therapies name safety elements (hazard analysis, adverse event evaluation, warnings, display testing): 882.5801, 882.5803, 882.5804, 882.5705, 886.5500, 880.5735, 876.5960, 890.5800 (SE1 to SE10). Adverse event wording differs by regulation: "capture all", "evaluate all", "relevant", "all device-related ... observed" (research file "Changes and conflicts" 2); quote the exact regulation for the product code the person names. Whether a regulation applies to the person's product is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question.

## Never

- Decide reportability, seriousness, causality or device-relatedness.
- Call the product or a mechanic "safe", "effective" or "compliant", or an event rate "acceptable".
- Supply a threshold, a period, an awareness date or a category the person did not give.
- Put identifiable patient data into a library call.
