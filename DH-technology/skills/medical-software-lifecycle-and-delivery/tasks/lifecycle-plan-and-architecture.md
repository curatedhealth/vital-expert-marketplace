# A1 Lifecycle plan and architecture

Framework task: DH-04.03.4.1 with DH-01.06.4.1 and DH-04.03.1.1, Part A, task A1. Carries the old tasks "DH-04.03.4.1.1 Safety class and software items", "DH-04.03.4.1.2 Required process for the class", "DH-01.06.4.1.1 SaMD Architecture Design", "DH-01.06.4.1.2 Platform Component Development", "DH-01.06.4.1.3 Data-Flow & Integration Design", "DH-04.03.1.1.1 Workload and data placement", "DH-04.03.1.1.2 Scale limit" and "DH-04.03.1.1.3 Operate the environment" as steps.

## What this task delivers

For one product and version: the safety class and software items as the person states them, a SOUP and component inventory checked against the FDA identity and support fields, a lifecycle plan checklist (the plans the person says their process requires, each present, draft or missing and tied to the version), the premarket software document register checked against FDA's ten elements, an architecture and data-flow description built only from components the person named, and a cloud placement, scale and operations table with every missing value marked. It answers "what does our software lifecycle need to hold, what do we have, and what is missing?"

Why it matters: validation effort scales with the hazard of each function (EN-005), and the FDA premarket software documentation is built from these same records (PL15). A lifecycle plan that assumes a class, invents a component or claims elastic scale without a first-failure component says more than the team knows.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-04.03.4.1.x); `behavior-change-designer` (old DH-01.06.4.1.x); `digital-health-product-manager` (old DH-04.03.1.1.x). Work as a medical software lifecycle engineer who records the person's decisions against sourced requirements |
| Skill | DH-04.03.4.1 Part A, Lifecycle plan and architecture |
| Workflow | The steps below |
| Knowledge | `references/lifecycle-rules.md`; `references/engineering-interop-security-research.md`; `references/quality-systems-research.md`; `references/product-lifecycle-research.md` |
| Tools | `regulatory-dh.list_jurisdictions` and `regulatory-dh.search_safety_events` (step 3, optional); `scripts/lifecycle_check.py items` and `docs`; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/lifecycle-plan-and-architecture-output.md` |
| Input | The request and its context: product, version, intended use in one sentence, markets, the safety class and hazards the person states, the item inventory (CSV columns in `scripts/lifecycle_check.py`), the plans their procedure requires, the document register, named components and data flows, regions, scale unit and target, paging rules, read date |
| Governance | `references/governance.md`; class, plans, level and targets are the person's |
| Catalogue job | none known (needs a live check) |

## Read the request

- **Product, version, intended use.** Needed: every item and plan ties to a version. If the version is missing, ask once; write "version not given" until then.
- **Class.** If the person gives a class, write it verbatim with the hazard they name. If they ask the model to set it, or to define the classes: decline that part (`references/governance.md`), say the class definitions are not in this skill's sources, and draft what the facts support: the hazards they listed, which items each hazard touches, and the questions for whoever they name for the risk file.
- **Short or full.** "What does IEC 62304 need from us?" or "check our SOUP list" is short mode. "Draft our lifecycle plan and architecture" is full mode.
- **Markets.** US by default. Add the EU rows (EU19, EU20, EN-031, EN-069, EU30) when the EU is named, and the DTAC rows (PL97 to PL100) when the NHS is named.

## Workflow

### Step 1. Class and software items (old 4.1.1)

Write the class the person states and the hazard that drove it (I1 and I2 flags when either is missing). List the software items; separate items the team writes from OTS and open-source items (EN-024). Record nothing about what the class requires beyond what the person's own procedure says: the IEC 62304 class definitions and class-by-class requirements are `[GAP]` (`lifecycle-rules.md` section 2).

### Step 2. SOUP and component inventory

Run `python3 scripts/lifecycle_check.py items --inventory FILE --as-of DATE` on the person's inventory (read date from the person; "not given" if absent, and the script stops). It checks title, manufacturer, version, release date and patch (EN-026), support level and end-of-support date (EN-054). Say that the NTIA minimum elements were not read (`[GAP]`). An end-of-support date before the read date is a fact (I6). Vulnerabilities and patch policy route to `cybersecurity-and-privacy-by-design` (this pack).

### Step 3. Public recall records of comparable software (optional, only if asked or useful for the hazard list)

Call `regulatory-dh.list_jurisdictions {}` once, then `regulatory-dh.search_safety_events {manufacturer: "<stored spelling>", jurisdiction: "US", since: "<person's date>", limit: 10}` or `{product_code: "<code>", jurisdiction: "US", limit: 10}`. Read every title; keep only rows that name software; quote title, date and class as the record states them (`references/tools.md`). Never judge relevance to the person's product; the person decides what enters their hazard list. An empty result is not evidence of safety.

### Step 4. Lifecycle plans (old 4.1.2)

Ask which plans the person's procedure requires for their class (the old task's examples: development, risk, configuration, problem resolution, maintenance). Mark each present, draft or missing and tie it to the product version. Old rule: cite the document, never "IEC 62304" as a plan. For a US submission, run `python3 scripts/lifecycle_check.py docs --register FILE --level LEVEL --product NAME` against the ten elements (PL15) at the level the person states (PL17 to PL20); the level itself is the regulatory owner's.

### Step 5. Architecture, components and data flows (old 06.4.1.1 to 06.4.1.3)

From components and flows the person named only: a component table (component, own or OTS, item id, function it serves, device function or other function as the person classes it) and a data-flow table (from, to, data, interface, as named). Apply the multiple-function rows: separate the device function from other functions in design and implementation, and document the impact assessments (PL24 to PL27). Name the security architecture views FDA asks for (EN-056) and route their content to `cybersecurity-and-privacy-by-design` (this pack). Interfaces to EHRs route to `interoperability-and-ehr-integration` (this pack). Anything unnamed is `[GAP]`; never invent an integration.

### Step 6. Placement, scale and operations (old 1.1.1 to 1.1.3)

Placement table: workload, region, account or subscription, data class, store, backup location, each from the person or "not given" (old rule: "multi-region" names the regions). Note the sourced duties that attach: a cloud provider holding ePHI is a business associate [WF] (EN-032, EN-033); offshore storage needs a BAA and a risk analysis entry [WF] (EN-034); contingency plans (EN-102); CSA for cloud tools used in production or the QMS (EN-017). Scale: the unit, the number the design must hold and the component that fails first, from the person; no source sets a figure. Operations: the health signal per workload, who is paged on what condition, and the runbook or `[GAP]` (old rule: no dashboard nobody is assigned to watch).

## Build the output

Follow `assets/lifecycle-plan-and-architecture-output.md`. Answer first: the class as stated, counts of items and flags, the documentation elements missing or in draft, and the biggest open item. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/lifecycle_check.py words ANSWER.md`; without code execution, count the same way by hand. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- No class assigned, lowered or defined; the class is written as the person stated it.
- No component, flow, region, scale figure or runbook the person did not give.
- Every requirement names its source and date in plain words with the row id after it; [WF] rows say so.
- Recalls are quoted as their records state them, with no relevance judgment.
- `python3 scripts/lifecycle_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Class decisions and the risk file: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Documentation level and submission content: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Threat model, controls and SBOM vulnerabilities: `cybersecurity-and-privacy-by-design` (this pack).
- Reading how the lifecycle performs over time: `software-quality-and-delivery-monitoring` (this pack).
