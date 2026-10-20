# A2 Remote data capture operations

Framework task: DH-01.02.3.1, Part A, task A2 (old DH-01.02.3.1.2 Remote Data Capture Operations).

## What this task delivers

A capture plan, one row per data stream (each DHT, app, ePRO or EHR export), that shows on evidence seen whether the stream is fit for purpose, where its source data sit, how data and metadata reach the sponsor, how safety-relevant readings are handled, and what happens when it fails. It answers "is our wearable data trial-grade, and where are the holes?"

Why it matters: a DHT is a data acquisition tool (CV20). If verification, validation or usability evidence is missing for the trial population (CV46, CV48, CV51), or arms are measured differently (CV58), the endpoint can be uninterpretable however clean the database looks.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.1 Part A, Remote data capture operations |
| Workflow | The steps below |
| Knowledge | `references/remote-capture-rules.md`; rows CV14, CV15, CV20, CV26, CV41, CV43 to CV64, CV68, CV69, CV99, CV102, CV103, CV155 to CV159 (V3, DOI 10.1038/s41746-020-0260-4) |
| Tool | Optional: `literature.search_literature`, `verify.qualify_source`, `verify.check_claim` (published validation of a named DHT); `scripts/capture_inventory_check.py` |
| Catalogue job | None |
| Prompt | This guide |
| Template | `assets/remote-data-capture-output.md` |
| Input | The request and its context: DHT list with model and version, what each measures, endpoint it feeds, arms, the person's V&V and usability documents, data flow or vendor description |
| Governance | `references/governance.md` |

## Read the request

- **Which streams.** Ask for the list if not given. A stream without a named model and version is `[GAP]` for specifications (CV52).
- **What evidence exists.** Ask what the person holds per stream: verification, validation in which population, usability, vendor audit-trail and validation documents.
- **Mode.** Short for one DHT question, full for a capture plan.

## Workflow

### Step 1. Build the inventory

One row per stream: data element, DHT and version, endpoint it feeds (primary, key secondary, safety, exploratory), arms that use it, who enters it (device, participant, staff), first durable repository, audit trail, timestamps, validation evidence, usability evidence, contingency. With code execution, write it as a CSV with the columns in `scripts/capture_inventory_check.py` and run it; it lists the missing attributes per stream. Quote the script's counts as printed (streams, open attributes) and state how many streams have at least one open attribute by counting the table, not by estimate.

### Step 2. Fit for purpose, on evidence seen

For each stream, lay the person's evidence against `remote-capture-rules.md` section 2:

- Verification of the measured parameter (CV46), validation in the proposed population (CV46, CV48), the evidence types used (CV49), whether it is reused from a manufacturer or another submission (CV50).
- Usability with the trial population (CV51).
- Minimum technical and performance specifications set by the sponsor (CV52).

Mark each element "evidence seen", "stated, evidence not seen" or `[GAP]`. Say which vocabulary you use (FDA two steps or V3 three steps, CV155 to CV159 (V3, DOI 10.1038/s41746-020-0260-4)) and that V3 is not FDA policy.

### Step 3. Published validation (optional)

If the person names a published validation study, run `verify.qualify_source {doi, question}`, read the passage, then `verify.check_claim {claim, passage: {text, locator}, source: <whole qualify_source object>}`. Accept the claim only if you read the passage in the same direction; "partial" and "supported" are not enough on their own (N3). To find such studies, `literature.search_literature {query: "<device> validation <population> <measure>", limit: 10}`; check whether the study population matches the trial population (CV48). Grading the study is the literature review skill's work.

### Step 4. Same method, same meaning

Check that each endpoint stream uses the same collection method in all arms (CV58), that the endpoint definition names type, timing, tool and aggregation (CV55), and that a replicated measurement still has V&V (CV57). Flag a planned non-inferiority comparison against a comparator not measured with similar DHTs (CV58).

### Step 5. Source and data flow

Name the source for each stream: the first durable electronic repository (CV60). Check the data management plan covers origin, flow and service providers (CV68) and that a data flow overview exists for all parties (CV102). Check audit trail and unambiguous timestamps (CV14) and visit record fields (CV69). Participant-entered data on primary, key secondary or safety endpoints needs safeguards (CV103).

### Step 6. Safety-relevant readings

For each stream that can show an abnormal value, check the protocol's safety monitoring plan says how it is reviewed and managed (CV62) and how it reaches the investigator in a manageable form (CV26). The plan's content is the person's; the model lists what the guidance expects.

### Step 7. Missing data and failure

Ask for the plan to reduce and handle missing data (CV59) and the contingency for tool failure on critical streams (CV99). Bring-your-own-device needs a sponsor-provided option (CV53).

## Build the output

Follow `assets/remote-data-capture-output.md`. Answer first: the streams that are not yet fit for purpose on evidence seen, and why. Then the inventory table, the source and flow line per stream, safety handling, missing-data and contingency items, gaps.

## Before you hand it over

- No stream is called "validated" or "fit for purpose" as a verdict; only "evidence seen" against named elements.
- No threshold was set for the person.
- Published claims were accepted only with the passage read in the same direction.
- Record line present.

## Boundaries

- Whether the DHT is a device, and human-factors validation for a device submission: dh-regulatory-strategy.
- Endpoint selection and COA development: the study design skill (DH-01.02.1). An ePRO or other COA stream's validation gap is cited to CV45 (out of DHT guidance scope) and routed there, not to CV46.
- Grading a validation paper: dh-clinical-validation 4.1 (literature-and-real-world-evidence-review).
- RWE platform and digital endpoint management outside a trial: DH-01.02.4.
