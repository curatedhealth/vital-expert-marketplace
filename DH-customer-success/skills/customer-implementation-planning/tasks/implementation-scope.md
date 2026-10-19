# A1 Implementation scope and blueprint

Framework task: DH-02.02.1.1, Part A, task A1. Replaces the old register task "Implementation scope" (CF-12.02.02.1.1.1).

## What this task delivers

A scope note and implementation blueprint for one customer deployment: the sites, modules and users in the first release; integrations now and later; the clinical workflow that must work on day one; core components and what may be adapted; the context the site described, laid out against named framework constructs; what the site needs from the company to deploy; and the measures, each with one named definition. It answers "what exactly are we deploying here, and how will we know it took?"

Why it matters: implementation outcomes come before clinical or service outcomes (CS32), so a deployment without agreed scope and measures cannot later separate a failed rollout from a product that did not work. ERIC's blueprint asks for aim, scope, milestones and measures up front (CS42).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.1.1 Part A, Implementation scope and blueprint |
| Workflow | The steps below |
| Knowledge | `references/implementation-blueprint.md`; `references/customer-success-research.md` (CS rows) |
| Tools | `literature.search_literature`, `verify.qualify_source`, `verify.check_claim` (counted, optional, Step 6) |
| Prompt | This guide |
| Template | `assets/implementation-scope-output.md` |
| Input | The request and its context: product, customer, sites, market, modules sold and agreed, users, integrations, the site's aim, what the site said about its context, any dates agreed |
| Governance | `references/governance.md`; scope and measures are the person's and the site's |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. evidence-table grades a set of studies for a product's claims; this task only identifies or checks a source the person names. |

## Read the request

- **Product and customer.** Product, the customer organization, the sites in the first release. Market (US, EU country, England, other) decides later contract steps (A2).
- **Modules and users.** What the contract covers and what the site agreed to. A module not agreed by the site stays out (register rule).
- **Day-one workflow.** The one clinical workflow that must work at go-live. If the person cannot name it, ask; without it there is no bar for B1.
- **Context.** What the person knows about the site: workflows, competing priorities, resources, who leads, funding route.
- **Mode.** Short for a direct question; full for a blueprint document.

## Workflow

### Step 1. Write the scope

Site(s), modules, user groups and integrations in the first release; integrations and modules for later; the day-one workflow. List anything sold but not agreed by the site separately, as "not agreed by the site". Unknowns are `[GAP]`.

### Step 2. Fill the blueprint skeleton

Aim, scope, timeframe and milestones, measures (CS42). Milestones and dates come only from the person; write "unset" where none is agreed.

### Step 3. Core and adaptable

Ask which components must stay fixed and which the site may adapt (CS4, CS48). If the person does not know, write "core components not defined `[GAP]`" and say why it matters: fidelity is later measured against the plan (CS9, CS37).

### Step 4. Lay out the context

Operationalize CFIR 2022 for this deployment first: name the inner setting (where the product is used) and the outer setting (the system around it) (CS11, CS12). Then, for each construct in `references/implementation-blueprint.md` section 3, write what the person said, with the row. Where they said nothing, "not described". Optionally add the NASSS domain questions (CS50 to CS54) with the person's own rating, or "not rated". Say once that CFIR and NASSS are not predictive and set no thresholds (CS3, CS51).

### Step 5. What the site needs from the company

Run the NICE ESF deployment list (`implementation-blueprint.md` section 5): training needs (CS58), deployment data items (CS64), communication and training approach (CS65), load testing (CS66), expected usage profile and reporting (CS61, CS62), implementation costs in the budget impact (CS63). For a product affected by local factors (for example AI), add silent-mode evaluation on local data before use in care as an option, not a requirement (CS60). Mark each "in hand", "to produce" or `[GAP]` from the person's facts. Outside NICE settings, label the list "NICE ESF, used as a checklist".

### Step 6. Published programs (optional)

If the person asks how comparable deployments went, call `literature.search_literature {query: "<product type> implementation <setting>", limit: 5}`. For any statement you want to use, call `verify.qualify_source {doi: ...}` and then `verify.check_claim` with the passage you read. Accept it only if the passage states the finding in the same direction (register N3). Report it as context for this site, never as a target. Read `references/tools.md` for pitfalls (design labels, empty excerpts).

### Step 7. Measures

Offer measures from `implementation-blueprint.md` section 4 with one definition each, named by source. Write back the ones the person picks. Targets are theirs; without a target, the measure has none. Keep usage and clinical outcomes apart (CS32).

## Build the output

Follow `assets/implementation-scope-output.md`. Answer first: the scope in three lines (sites, modules and users, day-one workflow), then what is missing to finish the blueprint. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every module in scope was agreed by the site, per the person.
- Every date and target is the person's or "unset".
- Every framework construct is described, not scored, unless the person scored it.
- Each measure has one named definition with its row.
- If it leaves the conversation (for example to the customer), it is a go-live-adjacent plan: ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Planning only. Checking a live deployment is the sibling skill (DH-02.02.1.2).
- Training content and change programs are Adoption & Change Enablement (DH-02.02.4.x). EHR interface build is the Interoperability pack.
- Prices, discounts and payer terms are Commercial or Market Access; outcome-linked payments are Market Access (outcomes-contract-monitoring).
- Whether the product is a device, its class and marking belong to the regulatory owner (dh-regulatory-strategy).
