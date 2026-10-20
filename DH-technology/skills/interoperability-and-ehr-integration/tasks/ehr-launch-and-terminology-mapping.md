# A2 EHR launch and terminology mapping

Framework tasks: DH-04.01.2.1, DH-04.01.3.1 and DH-04.01.4.1, Part A, task A2. Carries the old tasks "DH-04.01.2.1.1 SMART app registration", "DH-04.01.2.1.2 Screen to FHIR interaction map", "DH-04.01.2.1.3 Sandbox launch proof", "DH-04.01.3.1.1 Code system selection", "DH-04.01.3.1.2 Equivalence mapping", "DH-04.01.4.1.1 Current step observation" and "DH-04.01.4.1.2 New exchange placement".

## What this task delivers

For one named EHR: a registration note (launch type, scopes, endpoints), a screen-to-FHIR map with write-back stated per screen, a sandbox launch log from the token the person saved, a code system and equivalence map table with versions on every row, and the clinical step the exchange replaces (before and after). It answers "what does our app ask the EHR for, what does each screen read or write, what did the sandbox actually return, and how do our codes map?"

Why it matters: the old tasks were clear that a login page is not a SMART launch, a display of a read is not write-back, and a narrower map is not "equal". Each mistake shows up first at a customer's go-live.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `fhir-integration-specialist` (old DH-04.01.2.1.x); `data-engineering-manager-health` (old DH-04.01.3.1.x); `clinical-informatics-lead` (old DH-04.01.4.1.x). Work as an integration engineer who records what the sandbox and the maps show |
| Skill | DH-04.01.2.1 with DH-04.01.3.1 and DH-04.01.4.1, Part A, EHR launch and terminology mapping |
| Workflow | The steps below |
| Knowledge | `references/interop-rules.md` sections 2, 3, 11 and 13 |
| Tools | `scripts/fhir_check.py scopes`, `token` and `map` on the person's files; `verify.build_record` when the output leaves |
| Prompt | This guide |
| Template | `assets/ehr-launch-and-terminology-mapping-output.md` |
| Input | The request and its context: the EHR and sandbox named, launch type the EHR supports, the scopes requested, the screen list, the saved token response, the source and target code lists, the observed clinical step, owners |
| Governance | `references/governance.md`; scopes, labels and placement are the person's |
| Catalogue job | none |

## Read the request

- **One EHR at a time** (old task output: "A registration note for one named EHR"). If several are named, run one and offer the next.
- **Sandbox, not production.** Payloads and tokens are synthetic or de-identified sandbox data. If the person pastes what looks like real patient data, stop and ask for sandbox data (`governance.md`).
- **Which parts.** Registration and launch, mapping, or the workflow step: run only those asked. "Is our scope list right?" is short mode.

## Workflow

### Step 1. Registration note (old "SMART app registration")

Launch type (EHR launch or standalone), as the person states the target EHR supports it; EHR app-registration terms are not in the sources `[GAP]`. Scopes: run `python3 scripts/fhir_check.py scopes --scopes "..." --screens SCREENS.csv` and quote its table: v1 syntax with its v2 equivalent (EN-138), suffixes outside the ordered c r u d s subset (EN-138), `system/` scopes in a user-facing app (EN-139), scopes no screen uses (drop them, old task method step 2). Record client id, redirect URI and launch endpoint as the person gives them ("not given" otherwise).

### Step 2. Screen to FHIR map (old "Screen to FHIR interaction map")

| Screen | Resource | Interaction | Write-back to the chart |
|---|---|---|---|

From the person's screen list. A screen with no FHIR call is "local-only" and is not described as integrated; a screen with only a read or search interaction is not write-back (the script flags both).

### Step 3. Sandbox launch proof (old "Sandbox launch proof")

From the token response the person saved after launching as a test user into a test patient and encounter: run `python3 scripts/fhir_check.py token TOKEN.json --need patient,encounter,fhirUser`. Report each context field present or missing, the scopes granted against those requested, and for a missing field: the EHR, the scope requested and the field that was empty. A login page or a mocked token is not a launch. Where launch context was requested, note that a granted patient scope obliges the EHR to set patient context (EN-140).

### Step 4. Code systems and equivalence map (old "Code system selection" and "Equivalence mapping")

Element list: source system as it arrives, target system the product stores (SNOMED CT, LOINC, ICD-10-CM, ICD-11, or another the person names), or "uncoded". Never invent a default code; never map free text without a stated method (old task "Do not"). Map table from the person's file: run `python3 scripts/fhir_check.py map MAP.csv --labels "LABELS"` with the person's own label list and quote its flags (K1 to K5). Versions on every row (old task method step 3). The labels are the person's; the HL7 ConceptMap equivalence value set is not in the sources `[GAP]`. Add terminology licensing lines for the target systems and the person's countries (EN-171 to EN-177); RxNorm licensing is `[GAP]`.

### Step 5. The clinical step the exchange replaces (old "Current step observation" and "New exchange placement")

From the person's observation of today's step: step, actor, system, data retyped, frequency. Then the screen or message that replaces the retyped data and the click or reading that goes away; if the exchange adds a step, say so. No time saved is claimed without naming the step removed (old task "Do not"). Never describe the future workflow as the current one.

## Build the output

Follow `assets/ehr-launch-and-terminology-mapping-output.md`. Answer first: launch type and scope findings, context fields present or missing, map flags, the step that changes. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every scope finding cites EN-138 or EN-139; no scope was added by the model.
- Context fields come from the person's token, not from assumption; missing ones say MISSING.
- No equivalence label was changed by the model; flags are facts.
- No code was invented; uncoded elements stay "uncoded".
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Live EHR configuration changes stop for the owner the person names.
- Screen and workflow UX design: `dh-patient-and-user-experience` clinical-workflow-ux-design.
- Token handling security, secrets and threat model: `dh-technology` cybersecurity-and-privacy-by-design. The token check reads fields only; it never tests, replays or alters a token.
