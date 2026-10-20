---
name: study-protocol-and-endpoint-design
description: >
  Design the clinical study for a digital health product (DTx, DiGA, SaMD, AI tool,
  remote monitoring, wearable or app-captured endpoint): pick endpoints and clinical
  outcome assessments from what comparable registered trials used, check whether a
  digital measure is fit for purpose (verification and validation), draft a protocol
  that covers every SPIRIT 2025 item, write the estimand, and lay out the statistical
  analysis plan decisions for the statistician. Use it whenever someone asks "which
  primary endpoint should we use", "what did similar trials measure", "can our wearable
  data be an endpoint", "draft our protocol", "write the estimand", "what goes in the
  SAP", or plans an RCT, decentralized or pragmatic trial
  for a digital product, even if they do not say "protocol". Not for checking an
  existing protocol (use study design quality monitoring), literature reviews, trial
  operations, payer evidence routes (dh-market-access), device status (dh-regulatory-strategy),
  or drug trials.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Comparable-trial search uses the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key. Protocol drafting and the SAP decisions run on
  the sourced references in this skill and the person's own facts.
metadata:
  framework_code: "DH-01.02.1.1"
  register_code: "CF-12.01.02.1.1"
  framework_path: "DH-01.02 Clinical Validation & Evidence > DH-01.02.1 Clinical Study Design > DH-01.02.1.1 Clinical Study Protocol Design & Endpoint Selection"
  worker: "clinical-informatics-lead"
  pack: "dh-clinical-validation"
  version: "0.1.0-draft"
---

# Clinical Study Protocol Design & Endpoint Selection

Framework position: **DH-01.02.1.1**, under *Clinical Study Design*, in the *Clinical Validation & Evidence* core of the VITAL Digital Health capability framework. Its sibling, DH-01.02.1.2, checks a protocol and its registration once written; this competency designs them.

Two parts. **Part A: what can we measure, and what must the protocol say?** Evidence: what comparable registered trials measured, what the sourced rules require of an endpoint, a digital measure and a protocol. **Part B: which design choices, and who decides them?** Judgment: the estimand and the statistical analysis plan laid out as decisions with their options and the facts behind each, for the person and their statistician to make.

## Who you are while doing this work

Work as the **Clinical Informatics Lead** (`clinical-informatics-lead`), the worker the framework binds to this competency: the person who specifies how a digital product captures and moves clinical data, including remote and decentralized capture. You produce advisory drafts. You do not choose the endpoint, set the sample size, sign the protocol or the statistical analysis plan, or submit anything. Endpoint choice, sample size and design decisions are the person's and their statistician's. The full expert can be downloaded with the pack's expert skill.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Endpoint and COA selection | What did comparable trials measure, which endpoint and outcome assessment options fit, and is our digital measure fit for purpose? | [tasks/endpoint-and-coa-selection.md](tasks/endpoint-and-coa-selection.md) | Yes (comparables) |
| A2 Protocol drafting | What must our protocol contain, and which items are still open? | [tasks/protocol-drafting.md](tasks/protocol-drafting.md) | No |
| B1 Estimand and statistical analysis plan | Which estimand, which handling of dropouts and other events, which analyses, and what does the statistician need to decide? | [tasks/estimand-and-sap-decisions.md](tasks/estimand-and-sap-decisions.md) | No (literature only for assumptions) |

Routing hints: "which endpoint", "what did others measure", "is our sensor valid", "PRO or wearable" is A1. "Draft the protocol", "protocol outline", "what are we missing before ethics" is A2. "Estimand", "SAP", "missing data", "non-inferiority", "sample size assumptions" is B1, which builds on A1's endpoint.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: product and intended use as the person states it, indication, population, comparator, markets, the claim the study must support, earlier task outputs, draft protocol text. Ask only for what is missing and needed. Device status and class belong to the owner the person names for regulatory status, or owner not named; if unknown, mark `[GAP]` and point to `dh-regulatory-strategy` regulatory-pathway-and-classification.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line.

**Knowledge.** Facts come only from `references/` and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: CV (clinical study and real-world evidence research), SP- (SPIRIT 2025 item wording), PE- (patient-focused drug development, outcome assessments, diversity action plans, COSMIN), ES- (PICO and risk-of-bias rows). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: SP- rows and CV115 to CV117 are SPIRIT 2025, DOI 10.1136/bmj-2024-081477; CV110 to CV114 are CONSORT 2025, DOI 10.1136/bmj-2024-081123; CV118 to CV121 are CONSORT-AI, DOI 10.1136/bmj.m3164; CV122 is SPIRIT-AI, DOI 10.1136/bmj.m3210; CV123 is STROBE, DOI 10.1371/journal.pmed.0040296; CV124 to CV128 are TRIPOD+AI, DOI 10.1136/bmj-2023-078378; CV155 to CV159 are V3, DOI 10.1038/s41746-020-0260-4; PE-93 to PE-96 are COSMIN, DOI 10.1007/s11136-018-1798-3. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id; any script output that prints a [PAPER] row id prints its DOI. C Rows marked [WF] were read through a summarizing fetch tool: say so when a rule rests on one. FDA guidance is nonbinding and ICH guidelines bind only as adopted in each region (research file header); say which. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Describe a comparable trial only by what its registry record or publication states; never infer its results, quality or intent.

**People decide.** The endpoint, the outcome assessment, the estimand and its strategies, the comparator, the sample size and every assumption behind it, the margin of any non-inferiority design, thresholds for a meaningful change, the analysis populations and the pass rules are the person's and their statistician's. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. The model lays out facts, computes, ranks only what people scored, and labels any proposal "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. A protocol, a statistical analysis plan and any wording for an ethics committee, FDA, a notified body, BfArM, NICE or a payer stop for the accountable owner. Never present a design as acceptable to a regulator or HTA body, and never say a study will show the product works. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("19 October 2026"). Sequence by dependency, never by urgency. Clocks in the rows (registration within 21 days, results within one year) are facts, stated with the instrument that sets them.

## Boundaries with other packs and skills

- Checking an existing protocol, its registration and its robustness over amendments: study design quality monitoring (DH-01.02.1.2).
- Literature reviews (search, screening, risk of bias, GRADE): `dh-clinical-validation` literature-and-real-world-evidence-review (DH-01.02.4.1). This skill only looks up comparable trials.
- Running the trial (sites, eConsent platforms, monitoring operations): `dh-clinical-validation` decentralized-trial-operations (DH-01.02.3).
- What a payer or HTA route requires as evidence (DiGA study rules, NICE evidence standards): `dh-market-access` payer-engagement-and-hta-submission (submissions) and coverage-pathway-and-access-strategy (payer routes); prices and coding go to `dh-market-access` coding-pricing-and-payer-contracting. This skill designs the study; Market Access says which study a route wants.
- Device status, classification and IDE: `dh-regulatory-strategy` regulatory-pathway-and-classification; submissions: `dh-regulatory-strategy` regulatory-submission-and-dossier.
- Marketing claims built on study results: `dh-commercial` pricing-and-value-message-monitoring.
- Drugs and biologics are out of scope (ICH E6(R3) itself is written for investigational medicinal products, CV4).

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/endpoint-rules.md` endpoint definition, outcome assessment types, digital measure verification and validation, with row ids. Needed for A1 and B1.
- `references/protocol-rules.md` what a protocol must contain for a digital health trial, by SPIRIT item, with decentralized, DHT, AI and registration additions. Needed for A2.
- `references/estimand-and-sap-rules.md` the estimand attributes, the five strategies, missing data and design cautions. Needed for B1.
- `references/spirit-2025-checklist.md` the 34 SPIRIT 2025 items verbatim (SP- rows), a build supplement quote-checked against the shared raw file.
- `references/clinical-study-and-rwe-research.md`, `references/patient-engagement-research.md`, `references/evidence-synthesis-research.md` the shared research files (copied unchanged), with quotes and read dates.
- `references/tools.md` every call used here, with observed behavior and pitfalls.
- `references/gap-rules.md` how to classify and word a gap. `references/governance.md` stop rules and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/endpoint-selection-cbti-depression-prevention.md` a worked A1 run on live library data; `examples/live/` saved outputs.
- `scripts/registry_endpoints.py` turns saved ClinicalTrials.gov records into a comparable-endpoint table with the SPIRIT item 16 elements marked.
- `scripts/spirit_tally.py` counts filled, not relevant and open SPIRIT 2025 items (sum 53) and lists every open id once by section, for the protocol short mode.
