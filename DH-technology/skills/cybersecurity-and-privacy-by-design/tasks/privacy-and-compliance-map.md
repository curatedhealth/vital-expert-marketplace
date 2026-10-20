# A1 Privacy and compliance map

Framework task: DH-04.02.1.1 with DH-04.02.4.1, Part A, task A1. Carries the old tasks "DH-04.02.1.1.1 Data class and legal basis", "DH-04.02.1.1.2 Control per data class", "DH-04.02.1.1.3 Reviewer document set", "DH-04.02.4.1.1 Consent purpose list", "DH-04.02.4.1.2 Consent capture check" and "DH-04.02.4.1.3 Privacy engineering change".

## What this task delivers

For the person's product, markets and data: which security and privacy regimes the facts point to (with the fact that decides each, kept apart from the conclusion), a data-class table with region, legal basis and the control that implements it, the consent purposes and how a yes and a later no are stored, and the index of documents a reviewer can open with every missing one marked `[GAP]`. It answers "what applies to our data, what must be in place, and what is missing?"

Why it matters: the old tasks were explicit that one basis is not applied to every class, that a law is not a control, and that a missing policy is not filled with a summary. A map that says "HIPAA and GDPR compliant" without the mechanism and the artifact for each class tells a reviewer nothing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `privacy-engineering-director` (old DH-04.02.1.1.1 to .3 and DH-04.02.4.1.1 to .3). Work as a privacy and security analyst who maps facts to sourced rules |
| Skill | DH-04.02.1.1 with DH-04.02.4.1, Part A, Privacy and compliance map |
| Workflow | The steps below |
| Knowledge | `references/security-and-privacy-requirements.md` sections 1 to 5 and 8; rows EN-032 to EN-035, EN-041 to EN-061, EN-069 to EN-074, EN-086 to EN-128; CP-US-44, CP-US-54 to CP-US-56, CP-EU-01 to CP-EU-08, CP-UK-01 to CP-UK-11; CS68 to CS71, CS96 to CS110; DL-024, DL-086 to DL-106; PL87 |
| Tools | `regulatory-dh.get_authorization` only when the person names an authorized product; `scripts/secdesign_check.py datamap`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/privacy-and-compliance-map-output.md` |
| Input | The request and its context: product and intended use, markets, customers (covered entities or consumers), data classes, cloud and processors, the person's legal-basis view, existing controls and artifacts, consent text, owners |
| Governance | `references/governance.md`; regime conclusions and legal bases are the person's and their legal owner's |
| Catalogue job | none (`list_jobs_2026-10-19.json` lists no security or privacy job) |

## Read the request

- **Product, markets and customers.** Who the product serves (hospitals, payers, consumers), where (US states, EU countries, England, Germany), and whether it is or may be a device. Ask only for what decides a regime.
- **Data.** The classes held, where they are stored, which processors and cloud providers touch them, whether any leave the region.
- **What the person already has.** Legal-basis views, control matrix, policies, consent text, DPIA, BAAs. Keep their words.
- **Short or full.** "Does HIPAA apply to us?" is short mode. "Map our compliance and document set" is full mode.

## Workflow

### Step 1. The facts that decide each regime

From `security-and-privacy-requirements.md` section 1, list each regime the person's facts point to, with the fact that points there, and each regime whose deciding fact is not given ("not given; ask"). Keep the fact apart from the conclusion: "you host PHI for hospitals on a cloud provider (your facts); a vendor doing that is a business associate (45 CFR 160.103, CP-US-44); the cloud provider is a business associate even without the key (HHS cloud guidance, EN-032 [WF])". Whether the regime applies is the person's legal owner's call, or owner not named.

### Step 2. Device facts, if any

If the product is or may be a device, state the 524B three-part test (EN-041) and the FDA reading of "connect to the internet" (EN-049) beside the person's facts, without concluding. If the person names an authorized product, call `regulatory-dh.get_authorization {reference: "<K, DEN or P number>"}` and state the decision date and pathway as the record shows them, beside the 524B effective date (EN-046). Device and cyber device status route to `dh-regulatory-and-quality` regulatory-pathway-and-classification. For the EU, MDR devices are outside the Cyber Resilience Act (EN-086); a health wearable outside the MDR is a CRA important product (EN-090).

### Step 3. Data classes and legal basis (old DH-04.02.1.1.1)

One row per class: class, region, basis (the person's, or "basis not given `[GAP]`"), with the rows that list the options for that region (section 2). Never apply one basis to every class. With code execution, save the table as CSV and run `python3 scripts/secdesign_check.py datamap --file CLASSES.csv`; report flags D1 to D6 as facts.

### Step 4. Control per class (old DH-04.02.1.1.2)

For each class: access control, retention, whether it leaves the region, the mechanism (never the law), and the artifact that shows it in force; a control only intended is "not in force". Cite the Security Rule required and addressable split where HIPAA applies (EN-097 to EN-105), and say that the 6 January 2025 NPRM is a proposal, not a requirement (EN-106, EN-107).

### Step 5. Consent purposes and capture (old DH-04.02.4.1.1 and .2)

List each purpose in the product's words, tied to a data class, with the screen or form that captures it or "no screen yet". For each: what is stored (who, when, which purpose, which text version), how a withdrawal is stored and which processing it stops, and any purpose that cannot be withdrawn with the person's reason. Apply only the consent rows for the market in the request (DL-102 for the EU; EN-122, EN-123, EN-125 for Washington; EN-116, EN-117 for Part 2). A default-on checkbox is not a captured consent.

### Step 6. Fields collected but not used (old DH-04.02.4.1.3)

Where the person lists fields, mark any field the stated purpose does not read: remove it, or name the purpose that needs it, with the product version that carries the change (GDPR by default, EN-109). The decision is the person's; label the model's suggestion "proposed".

### Step 7. Reviewer document set (old DH-04.02.1.1.3)

Index the documents the person has against section 5 of the reference, for the regimes kept in step 1 only. Check that each names the product version it describes. Every missing document is `[GAP]` with the row that asks for it; never draft it as a summary.

## Build the output

Follow `assets/privacy-and-compliance-map-output.md`. Answer first: which regimes the person's facts point to (and which deciding facts are missing), how many data classes have a basis, a control and an artifact, and the documents most missing. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/secdesign_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No regime is declared to apply or not apply; the deciding fact and the row are stated, and the conclusion is the owner's.
- No class shares a basis by default; every basis is the person's or `[GAP]`.
- Every control names a mechanism and an artifact, or says "not in force".
- The NPRM appears only as a proposal.
- Only rows for the markets in the request are cited.
- `python3 scripts/secdesign_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; [WF] and "(inference)" labels travel with their rows.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- "Are we compliant?": decline the verdict; draft what the facts support instead (each regime's deciding fact, the control and artifact per class, the gaps), labeled "draft for the owner".
- Device status and submissions: `dh-regulatory-and-quality` regulatory-pathway-and-classification and regulatory-submission-and-dossier.
- BAA and data terms in a customer rollout: `dh-go-to-market` customer-implementation-planning; the contract wording is the legal owner's.
- Consent screen usability and accessibility: `dh-patient-and-user-experience` usability-monitoring and accessibility-standards-implementation.
- Whether the controls work in operation and whether consent text matches practice: `dh-technology` security-and-privacy-operations-monitoring.
