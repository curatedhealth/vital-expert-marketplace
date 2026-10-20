# A4 Safety by design

Framework task: DH-01.01.2.1, Part A, task A4. Folds in the earlier "Safety-by-Design Implementation" task (DH-01.06.2.1.2, register CF-12.01.06.2.1.2) from the DH-01.06.2 heading "Safety & Efficacy". Old worker: `behavior-change-designer`; the binding of this skill is unchanged.

## What this task delivers

A hazard list built from the design: for each A1 link, A2 component and A3 mechanic, the risks to health it could create, the mitigation the person chose (design, software check, labeling or clinician step), the labeling elements the special controls name for the device type identified by the owner the person names for regulatory status (or owner not named), and the indicators and thresholds the person sets now for reading after launch. The risk file itself, with severity, probability and acceptability, is `dh-regulatory-and-quality` design-controls-and-risk-management's; A4 is the design input it receives.

Why it matters: FDA's records for software therapies name risks that come from the design itself, not only from bugs: software failure leading to delayed access (SE11), use error (SE12), screen addiction and decreased sleep quality from an engaging game (SE16). In the EU, thresholds that trigger action are set before launch (SE63, MDCG 2025-10, not legally binding), and a side-effect is excluded from individual serious-incident reports only if it is documented and quantified (SE59).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.1 Part A, Safety by design |
| Workflow | The steps below |
| Knowledge | `references/safety-design-rules.md`; `references/precedents.md`; rows TM120 to TM130, TM139, TM142, SE1 to SE20, SE22 to SE29, SE34 to SE37, SE39, SE40, SE59, SE60, SE63, SE89 |
| Tools | `regulatory-dh.get_authorization` and `regulatory-dh.search_safety_events` for a named precedent; `scripts/mechanism_map_check.py` |
| Prompt | This guide |
| Template | `assets/safety-by-design-output.md` |
| Input | The request and its context; A1 chain, A2 components and A3 mechanics (run the missing ones in short mode first, or work from the person's feature list and say so); the users and setting; the device type or regulation named by the owner the person names for regulatory status, or "not given" |
| Governance | `references/governance.md`; the person decides the hazards accepted into the list, the mitigations, labeling wording and the indicators and thresholds |
| Catalogue job | none (no saved `list_jobs` output shows a safety-design job) |

## Read the request

- **Design.** A1, A2 and A3 outputs, or the feature list. Which version?
- **Users and setting.** Age group, condition, with or without a clinician, in the person's words. Crisis risk (self-harm, psychosis) is named only if the person or a record names it.
- **Device type.** Has the person, or the owner they name for regulatory status, named a regulation or product code? If not, A4 shows the special controls as context and marks applicability `[GAP]`.
- **Existing risk file.** If one exists, A4 adds design-sourced hazards to it; it does not rewrite it.

## Workflow

### Step 1. Walk the design for hazard sources

For each link, component and mechanic, ask the hazard questions in `references/safety-design-rules.md` section 1: software failure delaying access (SE11), ineffective delivery (TM139), use error (SE12, SE13), displacement of face-to-face or more effective care (SE12; SE89, Michie 2017, DOI 10.2196/jmir.7126), harms from the mechanics (SE16, SE17), reward logic failure (PWE recalls), missed escalation (SE36), use outside the intended population (SE37), AI conversation harms (SE35). Write each hazard in the person's words, tied to its source in the design. Candidates the model suggests are labeled "proposed".

### Step 2. Mitigation per hazard

For each hazard, write the mitigation the person chose and its type (design, software verification, labeling, clinician step). Where the person has none, write "mitigation not given" and ask. Show precedent patterns as context only (section 3: pause and stop instructions SE20, lock-out TM142, adjunct framing SE12 and SE8, escalation SE25, AI role disclosure SE28, children's screen time SE29; DHAC rows are committee advice, non-binding).

### Step 3. Safety and labeling elements the special controls name

If the person or the owner they name for regulatory status named a regulation, list its elements from section 2 in two groups: "Safety controls" (software verification, validation, hazard analysis, validated model) and "Labeling". Software controls are never listed as labeling. Quote each element, quoting the exact adverse-event wording of that regulation (research file "Changes and conflicts" 2). If none is named, show the table as context and write "applicability `[GAP]`: `dh-regulatory-and-quality` regulatory-pathway-and-classification". Labeling wording itself stops for the accountable owner.

### Step 4. Indicators and thresholds for after launch

For each hazard the person wants watched, write the indicator (complaint type, event, use error, efficacy drift on the A1 outcome) and the threshold the person sets now (SE63). The model never sets a threshold. For an EU product, ask whether the person and the owner they name for regulatory status (or owner not named) will document and quantify any expected side-effect (SE59); that is their decision. These feed `dh-clinical-development` mechanism-validation-monitoring (A4 there).

### Step 5. Precedent safety records (when the person names one)

Call `regulatory-dh.get_authorization {reference: "<DEN or K number>"}` and `regulatory-dh.search_safety_events {product_code: "<code>"}`. Quote the record: for reSET, the risk rows (SE11, SE12, TM139), the trial adverse events (SE14) and the PWE recalls of 7 June 2021; for EndeavorRx, the risk table and adverse events (SE16 to SE19) and the QFT search (no recalls returned; MAUDE 2 reports, which are reports, not confirmed events). The saved outputs are in `examples/live/connector_calls_2026-10-20.json`. Describe only what the record states; do not judge its relevance to the person's product. If the connector is unavailable, say in the answer body, not only in the calls list: "saved records of 20 October 2026, not rechecked live".

### Step 6. Hand off

List what goes to the risk file (`dh-regulatory-and-quality` design-controls-and-risk-management), what goes to human-factors validation (`dh-regulatory-and-quality` regulatory-submission-and-dossier), what goes to usability work (`dh-patient-and-user-experience` clinical-workflow-ux-design), and the indicators that go to monitoring (mechanism-validation-monitoring A4). B1 reads the hazards whose mitigation is untested as assumptions.

### Step 7. Check the structure (optional, with code execution)

Add the hazards to the map JSON in the shape of `evals/files/mechanics_safety_illustrative.json` and run `python3 scripts/mechanism_map_check.py MAP.json`. It lists hazards with no design source, no mitigation, and no indicator or threshold. Its marks are structure checks, not findings.

## Build the output

Follow `assets/safety-by-design-output.md`. Answer first: the hazards the design creates (count and the top ones the person marks), the open mitigations, the safety and labeling elements (or applicability `[GAP]`), and who decides. Where no owner is named, write "owner not named" in the answer and ask, before the record line: "Who owns the hazard list, the mitigations and the thresholds, and who owns regulatory status, and who clears this draft? A name or role in your words." Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Nothing is called "safe", "effective" or "compliant"; no severity, probability or acceptability was set by the model.
- Every hazard names its source in the design; every mitigation and threshold is the person's, or open.
- Special controls are context; applicability is `dh-regulatory-and-quality` regulatory-pathway-and-classification's; adverse-event wording is quoted from the exact regulation.
- DHAC rows are labeled committee advice, non-binding; MDCG rows not legally binding; SE34 labeled as MHRA's citation of a study not read.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". Where no owner is named, the answer writes "owner not named" and asks, before the record line: "Who owns the hazard list, the mitigations and the thresholds, and who owns regulatory status, and who clears this draft? A name or role in your words." No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The risk file, risk ratings and design history: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Whether a classification or the DiGAV applies: `dh-regulatory-and-quality` regulatory-pathway-and-classification; human-factors validation and wording for FDA, a notified body or BfArM: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Complaints, events and use errors after launch, and whether one is reportable: `dh-clinical-development` mechanism-validation-monitoring (A4 there) and `dh-regulatory-and-quality` audit-capa-and-complaints.
- Security and privacy hazards: `dh-cybersecurity` (heading DH-04.02.2 Security Architecture).
