# Endpoint and outcome assessment rules

Interpretive reference for A1 and B1. Every rule cites the row it comes from in `clinical-study-and-rwe-research.md` (CV), `patient-engagement-research.md` (PE-), `evidence-synthesis-research.md` (ES-) or `spirit-2025-checklist.md` (SP-). FDA guidance is nonbinding ("should" means recommended); ICH guidelines bind only as adopted in each region (CV research file header). Nothing here sets an accuracy threshold, an effect size or a sample size: the sources do not (CV research file scope note), so those stay the person's and their statistician's.

## 1. Start from the question

| Rule | Rows |
|---|---|
| Frame the study question as PICO: population, intervention, comparison, outcome. Not every element needs equal precision. | ES-36 |
| In an EU joint clinical assessment, one PICO is one population, one intervention, one comparator (which may include several treatments) and at least one outcome; scoping aims for the fewest PICOs. Relevant only where the product could be selected for JCA (class IIb or III with an expert panel opinion, ES-146). | ES-167 |
| Benefit means a positive effect on how a person feels, functions or survives; the product should affect a meaningful aspect of health (MAH) that patients care about. | PE-14, CV56 |
| Early patient input can inform which endpoints are meaningful, the population and the duration, and can test whether the digital tool suits participants (digital literacy, access to technology). | CV30, CV25 |

## 2. Define the endpoint precisely

An endpoint definition is complete when it names, for each outcome:

| Element | Source wording | Rows |
|---|---|---|
| Measurement variable | "the specific measurement variable (eg, systolic blood pressure)" | SP-16, CV113 |
| Analysis metric | "change from baseline, final value, time to event" | SP-16, CV113 |
| Method of aggregation | "median, proportion" | SP-16, CV113 |
| Time point | "time point for each outcome" | SP-16, CV113 |
| For a DHT endpoint, also: type of assessment, timing, the tool, and how repeated assessments per participant are combined | CV55 |

Endpoints built from DHT data follow the same principles as any other endpoint (CV54). Use the same data collection method in every arm (CV58).

## 3. Outcome assessment types and their rules (FDA PFDD series)

| Rule | Rows |
|---|---|
| Four clinical outcome assessment (COA) types: patient-reported (PRO), observer-reported (ObsRO), clinician-reported (ClinRO), performance outcome (PerfO). | PE-11 |
| A PRO comes directly from the patient; an ObsRO comes from someone other than the patient or a health professional who observes daily life. | PE-12, PE-13 |
| A COA proposal states the meaningful aspect of health, the concept of interest and the context of use. | PE-15 |
| PFDD Guidance 3 (selecting, developing or modifying fit-for-purpose COAs) is final, October 2025, issued jointly by CDER, CBER and CDRH. It points device sponsors to CDRH's PRO guidance of January 2022, which this skill has not read `[GAP]`. | PE-10, PE-16 |
| PFDD Guidance 4 (incorporating COAs into endpoints) is a draft of April 2023, for comment only. Its meaningful score difference is the difference patients would view as meaningful, often based on meaningful within-patient change; an anchor needs a well-justified definition of meaningful change. Cite as draft. | PE-17, PE-19, PE-20 |
| Avoid missing COA data, and collect the reasons for missing data to inform sensitivity analyses. | PE-21 |
| The FDA DHT guidance does not cover how to select, develop or validate COAs; it points elsewhere. | CV45 |

**Measurement properties of a PROM** [PAPER] COSMIN, Prinsen et al. 2018, DOI 10.1007/s11136-018-1798-3: content validity is the most important property (PE-93); sufficient reliability is ICC or weighted kappa of at least 0.70, sufficient internal consistency needs structural validity evidence and Cronbach's alpha of at least 0.70 per unidimensional scale (PE-95); measurement error is sufficient when SDC or LoA is smaller than the MIC (PE-96). These are COSMIN's rating criteria for published evidence, not a regulator's acceptance bar.

## 4. Is a digital measure fit for purpose?

FDA DHT guidance, final December 2023 (CV42). Fit for purpose means the validation is sufficient to support the use, including interpretability of the data, considering form and function (CV44).

| Question | Rule | Rows |
|---|---|---|
| Device or not? | Verification and validation are needed whether or not the DHT is a device. Device status itself is out of the guidance's scope; it goes to the owner the person names for regulatory status, or owner not named and `dh-regulatory-and-quality` regulatory-pathway-and-classification. | CV46, CV45 |
| Verification | The measured parameter (for example acceleration) is measured accurately and precisely. | CV46 |
| Validation | The DHT appropriately assesses the clinical event or characteristic in the proposed participant population. | CV46 |
| Which population? | V&V may run from bench to healthy volunteers to the study population; an algorithm valid in healthy people may fail in patients (shuffling gait example). | CV48 |
| What evidence? | Comparison against reference measurements, placement and interference effects, calibration, cross-model consistency, remote versus clinic differences. | CV49 |
| Can we reuse data? | V&V data from manufacturers, labeling, or other FDA submissions by right of reference. | CV50 |
| Usability | Usability evaluations show the trial population can use the DHT as intended without errors; FDA calls them critical. | CV51 |
| Specifications | Set minimum technical and performance specifications (accuracy, precision, reliability); specific models or versions may be named. | CV52 |
| Own devices | If participants may use their own DHT, offer sponsor-provided DHTs so no one is excluded for lacking one. | CV53 |
| New endpoint or old one measured remotely? | A DHT that replicates an existing measurement for the same endpoint may need no new endpoint justification, but still needs V&V. A novel endpoint is justified on feels, functions or survives and meaningfulness to patients, among other points. | CV57, CV56 |
| Qualification | DDT or MDDT qualification for a context of use is voluntary and independent of a marketing submission. Program details are not sourced `[GAP]`. | CV64 |
| Design controls | For a DHT used only for remote data collection in an investigation, FDA does not intend to assess design-control compliance when the recommended V&V is done. Not outside investigations. | CV63 |

**V3 framework** [PAPER] Goldsack et al. 2020, DOI 10.1038/s41746-020-0260-4: verification (bench, sensor accuracy and precision against a reference), analytical validation (the algorithm, in human participants, usually by its developer), clinical validation (the measure identifies a meaningful clinical state in the context of use, usually by the sponsor) (CV155 to CV159). V3 is a peer-reviewed framework, not FDA policy; FDA uses two terms, V3 uses three, and they map only roughly (CV research file "Changes and conflicts"). Say which one a statement uses.

In ICH E6(R3) terms, a DHT that acquires participant data for a trial is a data acquisition tool (CV20, CV15).

## 5. AI-enabled products

| Study type | Reporting rule | Rows |
|---|---|---|
| Trial of an AI intervention | SPIRIT-AI adds 15 protocol items, including a plan to analyze performance errors; CONSORT-AI asks for algorithm version, input data handling, human-AI interaction and output use. Both extend the 2013 and 2010 checklists, now superseded. | CV122, CV118 to CV121 |
| Prediction model development or evaluation | TRIPOD+AI, 27 main items (52 subitems): intended purpose and users, health inequalities, sample size justified separately for development and evaluation, performance measures (discrimination, calibration, clinical utility), fairness, thresholds, data shift, code and data availability. [PAPER] DOI 10.1136/bmj-2023-078378. | CV124 to CV128 |

## 6. Comparable trials

A comparable trial is described only by what its registry record or publication states: design, masking, enrollment, registered primary and secondary outcomes with time frames, and the publication's stated primary outcome. Never infer its results, quality or why it chose an endpoint. Where a registry and a publication word the primary outcome differently, report both, verbatim, and point to study design quality monitoring for the check (SP-16, CV114). Use `scripts/registry_endpoints.py` on saved registry records.

## Not sourced here

Accuracy thresholds for digital measures, effect sizes and minimal important differences for named instruments, the CDRH PRO guidance of January 2022, EMA qualification of novel methodologies, and NICE or DiGA evidence requirements (those are Market Access's references). Each is `[GAP]` when asked.
