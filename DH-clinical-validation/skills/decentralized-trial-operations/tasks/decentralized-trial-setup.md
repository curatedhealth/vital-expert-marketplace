# A1 Decentralized trial setup

Framework task: DH-01.02.3.1, Part A, task A1 (old DH-01.02.3.1.1 Decentralised Trial Setup).

## What this task delivers

A setup brief that lays every decentralized element of the trial against the rules that apply to it: where each activity happens and who performs it, what the protocol must state, what the consent route needs, how monitoring covers remote activity, which submission and registration items follow, and what stays open. It answers "what has to be in place before our hybrid trial can start, and what must the protocol say?"

Why it matters: the same rules apply with or without decentralized elements (CV66, CV98). What changes is where things can go wrong: a visit left to participant choice can bias the result (CV67), a local nurse doing protocol-specific work is trial personnel (CV70), and a remote consent without identity checks fails the basic requirement (CV16).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.3.1 Part A, Decentralized trial setup |
| Workflow | The steps below |
| Knowledge | `references/dct-setup-rules.md`; rows CV1 to CV30, CV61, CV65 to CV72, CV95 to CV103, CV132 to CV142, CVB7 |
| Tool | Optional: `literature.search_literature`, `literature.find_trial` (comparable trials) |
| Catalogue job | None (no trial-operations job in the library) |
| Prompt | This guide |
| Template | `assets/decentralized-trial-setup-output.md` |
| Input | The request and its context: protocol or synopsis, visit schedule, site plan, product type (drug, biologic, device, software), jurisdictions |
| Governance | `references/governance.md` |

## Read the request

- **Product type and jurisdictions.** Drug or biologic trial, device investigation, or a trial of a drug that uses DHTs? US, EU, both? This decides which rows apply (step 1).
- **What exists.** A protocol, a synopsis, a visit schedule, or only an idea. Without a visit schedule, build the element list with the person first.
- **Mode.** A direct question ("can we do eConsent in Germany?") gets short mode. A setup brief for a study team gets full mode.

## Workflow

### Step 1. Fix the framework

From `dct-setup-rules.md` section 1: for a drug or biologic trial, ICH E6(R3) principles and Annex 1 apply as adopted (CV1 to CV3) and Annex 2 takes effect in the EU on 15 January 2027 (CV2); FDA adoption of Annex 2 is `[GAP]`. If the person has not stated the product type, write the framework line conditionally ('If the app is investigated as a device, ...'); device status is the person's and dh-regulatory-strategy's call. For a device investigation, say that E6(R3) does not name devices (CV4) and that ISO 14155 and EU MDR investigation rules are `[GAP]` in this skill; continue with the FDA DCT and DHT guidances, which cover devices (CV65, CV42), and the EU paper as context. State this in one line at the top of the output.

### Step 2. List the decentralized elements

Make one row per trial activity that happens outside the investigator's location (CV19): each visit or assessment, consent, delivery of the product or device, sample collection, DHT data capture, safety follow-up. For each: where (site, home, local facility), who (investigator, trial staff, local provider, participant), how (in person, video, DHT). Take everything from the person's documents; blank stays `[GAP]`.

### Step 3. Fix visit modality

Ask the person to mark each visit site, remote or participant's choice; the protocol must say which (CV67). Where an endpoint assessment is marked "participant's choice", flag the bias the guidance names and ask whether that is intended. Do not change the person's choice. If a non-inferiority design is planned, add that FDA recommends consulting the review division first (CV72); the consultation stops for the owner the person names for regulatory contact, or owner not named.

### Step 4. Consent route

For remote consent: identity confirmation (CV16); for EU sites, real-time audio and video and a protected downloadable copy (CV100, CV101); for DHTs, who may access the data including under terms of service (CV61). List what the consent process must contain; the consent text itself stops for the owner.

### Step 5. Who does what

Split each remote activity into routine-practice tasks a local provider may do and protocol-specific tasks for trained trial personnel (CV70). Where the person's plan gives a local provider a protocol-specific task, flag it.

### Step 6. Monitoring and contingency

Note what the monitoring plan must cover for decentralized settings (CV17) and that FDA recommends centralized monitoring for missing, inconsistent and outlying data and potential deviations (CV71). For each element the person calls critical-to-quality, ask for the contingency if the tool fails or the visit cannot happen (CV99, CV96).

### Step 7. Submission and registration items

- EU: summary of decentralized elements in the cover letter (CV97); the national provisions appendix content is `[GAP]`.
- Registration: ICMJE before first patient consent (CV132); US applicable clinical trials within 21 calendar days after first enrollment (CV141, device trials per CV142). Say both when both apply. Registration tracking during the trial is the sibling monitoring skill.

### Step 8. Comparable trials (optional, when the person wants precedent)

Call `literature.search_literature` with the design and setting, for example `{query: "decentralized randomized trial remote enrollment wearable digital health technology", limit: 5, filters: {date_from: "2022-01-01"}}`. For a comparable trial with a PMID, call `literature.find_trial {record: <the record>}` to reach the registration, or `{nct_id}` when known. Report what each source states (design, setting, what was decentralized), with the design read from the abstract, not the label (N8). It is context, never a template the person must follow.

### Step 9. What it means for the person

Close with the consequence of the open items: which ones block a protocol or submission draft, which block first enrollment, which can close later. Sequence by dependency, not by date.

## Build the output

Follow `assets/decentralized-trial-setup-output.md`. Answer first: the framework line, then the two or three open items that block the next document. When an EU Member State is in scope and the trial runs under the EU CTR, keep the cover-letter item (CV97) in the short answer. Then the element table, consent, roles, monitoring, submission and registration items, comparables if run, gaps.

## Before you hand it over

- Every rule has its row id; guidance is "recommends", law is "requires".
- No visit modality, DHT or acceptance criterion was chosen for the person.
- Device trials say the E6(R3) scope and the ISO 14155 gap.
- Protocol, consent and cover-letter text is labeled "draft for the owner".
- Record line present: cleared by a named person through `verify.build_record`, or "uncleared draft".

## Boundaries

- Protocol design, endpoints and estimands: the study design skill (DH-01.02.1). This task only lists what the protocol must state about decentralized operations.
- Device status, human factors and submissions: dh-regulatory-strategy.
- Monitoring a running trial: the trial operations monitoring skill (DH-01.02.3.2).
