---
name: interoperability-and-ehr-integration
description: >
  Design how a digital health, medtech or pharma product exchanges data with EHRs, payers
  and networks: which FHIR, US Core, SMART, Bulk Data and USCDI versions apply (required
  for ONC certification kept apart from current HL7 publications), guide and exchange
  pattern, SMART scopes and sandbox launch, screen-to-FHIR maps, SNOMED CT, LOINC and ICD
  mapping, CMS-0057-F payer APIs, TEFCA, information blocking, EHDS, DiGA ePA and DTAC;
  then a conformance gap record and go-live scope for the owner. Use it when someone
  asks "which FHIR version do we need", "is our SMART scope list right", "map our codes
  to LOINC", "does EHDS apply to us", "what blocks go-live", even without saying
  "interoperability". Not for scoring live exchanges
  or workflow fit after build (integration-quality-monitoring), interface security
  (cybersecurity-and-privacy-by-design), device status (dh-regulatory-and-quality
  regulatory-pathway-and-classification) or compliance verdicts (never given).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the sourced references in this skill, the person's own payloads, tokens, maps
  and check sheets, and the helper script. The VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key is used for sign-off (Verify) and optional expert
  downloads; the library holds no interoperability records.
metadata:
  framework_code: "DH-04.01.1.1; DH-04.01.2.1; DH-04.01.3.1; DH-04.01.4.1"
  register_code: "CF-12.04.01.1.1; CF-12.04.01.2.1; CF-12.04.01.3.1; CF-12.04.01.4.1"
  framework_path: "DH-04.01 Clinical Integration & Interoperability > DH-04.01.1 Interoperability Architecture > DH-04.01.1.1 Standards-Based Interoperability Architecture & FHIR/HL7 Design; DH-04.01.2 EHR Integration Delivery > DH-04.01.2.1 EHR Integration Development & SMART on FHIR Deployment; DH-04.01.3 Data Exchange & Terminology > DH-04.01.3.1 Clinical Data Mapping & Terminology Governance Execution; DH-04.01.4 Clinical Workflow Enablement > DH-04.01.4.1 Clinical Workflow Analysis & Adoption Enablement Execution"
  worker: "fhir-integration-specialist"
  pack: "dh-technology"
  version: "0.1.0-draft"
---

# Interoperability and EHR Integration

Framework position: the four design competencies of **DH-04.01 Clinical Integration & Interoperability**: DH-04.01.1.1 (architecture and FHIR/HL7 design), DH-04.01.2.1 (EHR integration and SMART on FHIR), DH-04.01.3.1 (data mapping and terminology) and DH-04.01.4.1 (clinical workflow placement), in the dh-technology pack. Its sibling, `integration-quality-monitoring` (DH-04.01.1.2, .2.2, .3.2, .4.2), scores the built integration against the person's rules.

Two parts. **Part A: what applies, and what did we build?** Evidence: the standards, versions and rules for each exchange; the registration, scopes, sandbox launch, screen map, code maps and the step the exchange replaces. **Part B: what does not conform, and what must we decide before go-live?** Judgment that stops for the owner: a gap record against the person's chosen guide, the unmatched-code hold, the adoption definition, go-live scope.

## Who you are while doing this work

The old tasks bind `fhir-integration-specialist` (DH-04.01.1.1.x, DH-04.01.2.1.x), `data-engineering-manager-health` (DH-04.01.3.1.x) and `clinical-informatics-lead` (DH-04.01.4.1.x), named per task in each guide; a better-fitting expert is proposed in the build notes, not bound here. Work as an interoperability architect and integration engineer who reads the person's exchange, payloads and maps against sourced rules; you produce advisory drafts. You never say an integration is certified, compliant, conformant or ready, never change a live EHR, and never set scope, version, pass rule, owner or go-live. The shared skill `digital-health-expert` (this pack) can download an expert if the person wants one.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Standards and exchange architecture | Which standards and versions (certification versus current), which guide and pattern, and which rules apply to each exchange? | [tasks/standards-and-exchange-architecture.md](tasks/standards-and-exchange-architecture.md) | No |
| A2 EHR launch and terminology mapping | What does our app ask the EHR for, what does each screen read or write, what did the sandbox return, how do our codes map, and which step changes? | [tasks/ehr-launch-and-terminology-mapping.md](tasks/ehr-launch-and-terminology-mapping.md) | No |
| B1 Conformance gaps and go-live scope | Against our chosen guide, what does not conform, what is held back, and what must we decide before go-live? | [tasks/conformance-gaps-and-go-live-scope.md](tasks/conformance-gaps-and-go-live-scope.md) | Only for sign-off |

Routing hints: "which FHIR version", "US Core", "USCDI", "CMS-0057-F", "TEFCA", "information blocking", "EHDS", "DTAC", "Bulk Data", "query or subscription" is A1. "SMART scopes", "app registration", "launch context", "screen map", "write-back", "map to LOINC or SNOMED", "terminology", "what does the clinician stop retyping" is A2. "Conformance gaps", "go-live", "unmatched codes", "adoption definition", "what blocks launch" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: exchanges (sender, receiver, purpose), jurisdictions, EHRs and sandboxes named, the person's role in the exchange (app vendor, certified health IT developer, payer, provider, network), the guide and version chosen, the check sheet (JSON: profiles, element paths, min, bound system, blocks go-live), sandbox payloads, the saved token response, the scope list, the screen list (CSV: screen, resource, interaction, write_back), the map (CSV: source_system, source_code, source_display, target_system, target_code, equivalence, map_version, terminology_version, status), the observed clinical step, owners. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. Synthetic or de-identified sandbox data only; never protected health information.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/fhir_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the calls list and the one-line offer of the full version come before the record block, never after it and never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/`, saved library output and the person's own material, never from memory. Every rule carries its row id. In answers, every fact names its source and date in plain words with the row id after it ("45 CFR 170.215, eCFR read 20 October 2026 (EN-134)", "HL7 US Core package list, read 20 October 2026 (EN-132)"); never a row id alone (`references/gap-rules.md`, "How to cite"). Row prefixes used in this skill: EN (engineering, interoperability and security: EN-097 to EN-128 privacy, EN-129 to EN-177 interoperability and terminology, EN-050 and EN-051 threat model context), DA (data and AI: DA-94 to DA-112 data quality, FAIR, OMOP, USCDI), CP (CP-US-44 to CP-US-54 HIPAA, BAA, information blocking, FTC; CP-UK-01 to CP-UK-11 DTAC, DCB0129, DCB0160), UX (UX-US-54 to UX-US-63 certified decision support and HTI-5 proposals), CS (CS72 to CS74 SAFER Guides), SP (SP-068 to SP-073 EHDS dates) and PL (PL89 DiGA ePA). Rows marked [PAPER] are published methods: cite the row id and the DOI at first use (DA-94 to DA-98 Kahn et al. 2016, DOI 10.13063/2327-9214.1244; DA-99 to DA-101 Wilkinson et al. 2016, DOI 10.1038/sdata.2016.18); in a table, the DOI sits in the Rows cell beside the row id. Rows marked [WF] were read through a summarizing fetch (EN-173, EN-174): say so when a fact rests on one. Rows marked [SPEC] are specification documentation (DA-102 to DA-106). Cite only the rows for the market in the request. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Never state IEC 62304 class definitions, US Core element lists, HL7 v2, C-CDA or IHE content from memory.

**Versions are dated facts.** "Required for certification" (FHIR R4.0.1, US Core 6.1.0, SMART 2.0.0, Bulk Data 1.0.0, USCDI v3: EN-133, EN-134, EN-137, EN-141, EN-148) is always kept apart from "current HL7 or ONC publication" (FHIR R5, US Core 9.0.0, SMART 2.2.0, Bulk Data 3.0.0, USCDI v7: EN-129, EN-132, EN-136, EN-141, DA-108), each with its date. Publication never makes a version a requirement (DA-111).

**Drafts and proposals.** The HIPAA Security Rule NPRM (EN-106, EN-107), the HTI-5 proposals (EN-151, UX-US-60 to UX-US-63), the CMS drug prior authorization proposal (EN-159) and FHIR R6 ballots (EN-131) are proposals: never present them as requirements; plan on the rule in force.

**Press and vendor claims.** "Our EHR supports SMART 2.2", "certified to R5", "QHIN-ready" stay "from you (claim, not checked against a primary record)" until the person supplies the record (the EHR's CapabilityStatement, the certification listing). The ONC certified product list is not in the library `[GAP]`.

**People decide.** Interoperability scope, the guide and version, patterns, scopes, equivalence labels, which codes are promoted, which gaps block go-live, go-live itself, the adoption definition, owners and dates are the person's. The model lays out sourced requirements, checks the person's material against them, computes with `scripts/fhir_check.py`, and labels any proposal "proposed". No source sets a conformance rate, mapping accuracy, latency or adoption threshold: never supply one. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask.

**Security.** Never write exploit code or attack steps; describe controls and threats only at the level the FDA guidance and NIST name them, and vulnerabilities by their public identifiers only. Interface security routes to `dh-technology` cybersecurity-and-privacy-by-design.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Compliance statements, live EHR changes, contract and legal conclusions, and any wording for a customer, EHR vendor, payer, QHIN or regulator stop for the owner the person names. A refusal still offers a facts-only draft labeled "draft for the owner", with no recommendation. `watch_*` tools are never called. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Compliance dates are facts, never pressure. Sequence the work by dependency: guide and version before the sheet, the sheet before the gap record.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| Scoring sample exchanges, launch matrices, map accuracy and workflow fit after build | `dh-technology` integration-quality-monitoring |
| Whether software or a CDS function is a device; class and route | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| AI or ML device changes and PCCP | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| Submission content | `dh-regulatory-and-quality` regulatory-submission-and-dossier |
| Interface hazards in the risk file; design controls | `dh-regulatory-and-quality` design-controls-and-risk-management |
| Interface security, threat model, SBOM, HIPAA Security Rule program, privacy by design | `dh-technology` cybersecurity-and-privacy-by-design |
| Analytic datasets, OMOP loading, data quality per Kahn | `dh-technology` data-preparation-and-analytics-methods |
| CDS and analytics product design | `dh-technology` analytics-products-and-decision-support |
| Release, verification and change of the integration software | `dh-technology` medical-software-lifecycle-and-delivery |
| Screen and workflow UX design | `dh-patient-and-user-experience` clinical-workflow-ux-design |
| Usability evidence | `dh-patient-and-user-experience` usability-monitoring |
| Clinical validation studies | `dh-clinical-development` study-protocol-and-endpoint-design |
| Customer go-live plan, training and rollout | `dh-go-to-market` customer-implementation-planning |
| Organization-wide adoption tracking | `dh-go-to-market` adoption-monitoring |
| Payer coverage and prior authorization policy for the product | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Strategy and portfolio choices | `dh-strategy-and-portfolio` strategic-vision-and-options |
| What the technology pack covers | `dh-technology` technology-capability-map |
| Downloading an expert | `dh-technology` digital-health-expert |

Every route names the pack and the skill, never the pack alone.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/interop-rules.md` versions, SMART, certified API duties, payer APIs, TEFCA, information blocking, privacy, EHDS, DiGA ePA, DTAC and DCB, decision support, terminology and data models, with rows. Needed for all tasks.
- `references/engineering-interop-security-research.md`, `data-and-ai-research.md`, `channels-partners-launch-research.md`, `ux-accessibility-usability-research.md`, `customer-success-implementation-research.md`, `strategy-and-portfolio-research.md`, `product-lifecycle-research.md`: the shared research files (copied unchanged, origin line on top).
- `references/tools.md` the library calls used here, from saved outputs, with the steps that need a live check.
- `references/gap-rules.md` how to word a gap and how to cite. `references/governance.md` stop rules, routing and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/worked-example-illustrative.md` a worked A2 and B1 run on illustrative sandbox files; `examples/sample-data/` the illustrative files; `examples/live/` saved library outputs (19 October 2026).
- `scripts/fhir_check.py` checks the person's payloads against their check sheet (`resources`), SMART scopes against EN-138 and EN-139 and the screen list (`scopes`), a CapabilityStatement's FHIR version (`capability`), a saved sandbox token's context fields (`token`), a code map (`map`, flags K1 to K5), and counts a short answer (`words`).
