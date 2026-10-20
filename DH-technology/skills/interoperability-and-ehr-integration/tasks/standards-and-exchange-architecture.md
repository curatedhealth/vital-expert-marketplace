# A1 Standards and exchange architecture

Framework task: DH-04.01.1.1, Part A, task A1. Carries the old tasks "DH-04.01.1.1.1 Implementation guide selection" and "DH-04.01.1.1.2 Exchange pattern design".

## What this task delivers

For each exchange the person names (who sends, who receives, the clinical purpose): the standards and versions in play with "required for certification" kept apart from "current publication", the implementation guide options and the profiles in use, the elements the guide leaves open, and an exchange pattern table (query, subscription or bulk) with the FHIR interaction and the scope each needs. Plus the rules that attach to the exchange: payer APIs, TEFCA, information blocking, privacy, EHDS, DiGA ePA, DTAC and DCB0129. It answers "which standards, which versions, which pattern, and which rules apply to this exchange?"

Why it matters: US regulation pins FHIR R4.0.1, US Core 6.1.0, SMART 2.0.0, Bulk Data 1.0.0 and USCDI v3 while HL7 publishes newer versions (`interop-rules.md` section 1). Building to the wrong one, or calling a publication a requirement, costs an integration its EHR partners.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `fhir-integration-specialist` (old DH-04.01.1.1.1 and .2). Work as an interoperability architect who reads the person's exchange against sourced rules |
| Skill | DH-04.01.1.1 Part A, Standards and exchange architecture |
| Workflow | The steps below |
| Knowledge | `references/interop-rules.md` sections 1 to 12; the copied research files |
| Tools | None required. `scripts/fhir_check.py capability` if the person supplies a CapabilityStatement; `verify.build_record` when the output leaves |
| Prompt | This guide |
| Template | `assets/standards-and-exchange-architecture-output.md` |
| Input | The request and its context: exchanges (sender, receiver, purpose), jurisdictions, EHRs or networks named, data elements, the person's guide and version choice if made, owners |
| Governance | `references/governance.md`; scope, guide and version are the person's |
| Catalogue job | none |

## Read the request

- **The exchange.** Sender, receiver and clinical purpose for each. If missing, ask once; without them no guide can be chosen (old task method step 1).
- **Jurisdiction.** US rows by default; EU (EHDS), Germany (DiGA ePA) and UK (DTAC, DCB0129) only when named. Cite only the rows for the market in the request.
- **Who the person is in the exchange.** App vendor, EHR or certified health IT developer, payer, provider, network. This changes which rows bind them (a certified-API duty binds the EHR module, not the app; information blocking actor status depends on certified modules, CP-US-51).
- **Short or full.** "Which FHIR version do we need?" is short mode. "Design our interoperability architecture" is full mode.

## Workflow

### Step 1. Version baseline

Print the two-column table from `interop-rules.md` section 1 for the standards the exchange uses. If the person supplied a CapabilityStatement, run `python3 scripts/fhir_check.py capability FILE.json` and quote its lines. Name every proposal as a proposal with its date (HTI-5, EN-151; HIPAA Security Rule NPRM, EN-106 and EN-107; CMS drug prior authorization, EN-159; FHIR R6 ballot, EN-131).

### Step 2. Guide options (old "Implementation guide selection")

For each exchange: the base guide candidates the person can choose from (US Core for US certified APIs, EN-134; a national guide where the person names one; the Da Vinci CRD, DTR and PAS guides for provider prior authorization, EN-146). IPS and national guides other than these are not in the sources: name them only if the person does and mark their content `[GAP]`. List the profiles the exchange will use (from the person's data elements), and the elements the guide leaves open, each marked "local profile" or "out of scope" by the person. Do not invent a profile for an element the guide already constrains (old task "Do not"). Without the guide's StructureDefinitions, element-level must-support is `[GAP]`: ask for them.

### Step 3. Exchange pattern (old "Exchange pattern design")

| Profile | Pattern (query, subscription, bulk) | FHIR interaction | Scope needed | Why the other patterns were set aside |
|---|---|---|---|---|

Use EN-138 to EN-141 for scopes and Bulk Data group-export. One pattern per profile unless the first cannot carry a named element (old task method step 3); never REST, messaging and bulk for the same payload. Subscription mechanics are not in the sources: if chosen, mark its version and topic content `[GAP]`.

### Step 4. Rules that attach to the exchange

One line each, only those that apply: payer APIs and dates (EN-152 to EN-159); TEFCA Exchange Purposes (EN-160 to EN-163); information blocking actor categories and the knowledge standard (CP-US-50 to CP-US-53, for the owner the person names for legal matters); HIPAA business associate and BAA terms (CP-US-44 to CP-US-49); Part 2 consent (EN-114 to EN-117); MHMDA or FTC HBNR for consumer apps (EN-121 to EN-128, CP-US-54); EHDS (EN-164 to EN-170, SP-068 to SP-073); DiGA ePA (PL89); DTAC and DCB0129 or DCB0160 (CP-UK-01 to CP-UK-11); certified DSI duties if decision support shows inside the EHR (UX-US-54 to UX-US-60); terminology licensing (EN-171 to EN-177).

### Step 5. What the person must decide

The guide and version, the patterns, which open elements become local profiles, which rules the legal or regulatory owner must read. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/standards-and-exchange-architecture-output.md`. Answer first: the versions that apply (both columns), the guide options and pattern per exchange, the rule that most changes the design. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md`; without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every version appears with "required for certification" and "current publication" kept apart, each with its source and date.
- No proposal is presented as a rule; HTI-5, the HIPAA NPRM and the CMS drug proposal say "proposed".
- No profile, must-support element or code was invented; element-level gaps say `[GAP]`.
- Information blocking, BAA, Part 2 and EHDS conclusions stop for the owner the person names.
- Every fact names its source and date in plain words with the row id after it.
- The record line is the very last line; the calls list and the offer of the full version come before it.

## Boundaries

- Whether the integration software or a CDS function is a device: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Interface security design and threat model (EN-050, EN-051): `dh-technology` cybersecurity-and-privacy-by-design.
- Payer coverage of the product: `dh-access-and-value` coverage-pathway-and-access-strategy.
