# A2 Coverage pathway mapping

Framework task: DH-03.01.4.1, Part A, task A2.

## What this task delivers

For a product that is not yet paid (or not paid everywhere it should be), a map of where it could be paid and what each route would take: per target country, the schemes that fit this kind of product, what the record says each requires, how long it runs, and which comparable products already made it. It describes the options. Choosing between them and putting them in order is Part B (task B1, access strategy design).

Why it matters: teams pick a market by habit ("Germany first, DiGA") and discover the evidence bar, the clock, or the fact that a scheme pays a service rather than a product only after committing. A map built from the registers puts those facts in front of the decision.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.4.1 Part A, Coverage pathway mapping |
| Workflow | The steps below |
| Knowledge | Library scheme records; `references/requirements/` (sourced requirements per country); `references/scheme-kinds.md`; `references/gap-rules.md` |
| Tools | `list_schemes`, `find_scheme_precedents`, `search_listings`, `retrieve_guidance` |
| Prompt | This guide |
| Template | `assets/pathway-map-output.md` |
| Input | The request and its context, plus the four inputs below; an A1 status check already in the conversation is reused, not repeated |
| Governance | `references/governance.md` |

## Inputs

| Input | Needed for | If missing |
|---|---|---|
| Kind of product: therapeutic app (DTx), remote or telemonitoring, digital mental health treatment, diagnostic or monitoring device software, other | Which schemes fit | Ask once; it decides the whole map |
| Indication | Precedents | Use the request's words; mark the precedent search as broad |
| Regulatory status: class and where it is cleared or CE-marked | Whether a scheme's prerequisite is met | Mark `[GAP]`. Say the class comes from a regulatory classification (the Regulatory pack's classification job), not from this task. Do not guess a class |
| Target countries | Scope | Map every country the library covers and say so |

Ask at most one question, for the kind of product if it is unclear. Otherwise state assumptions and proceed.

## Workflow

### Step 1. Know what the library holds

Call `market-access-dh.list_schemes` (free). Keep each scheme's `pathway_kind`, `clock_rule`, `notes`, `listing_count`, `last_load` and `posture`. Filter to the target countries.

### Step 2. Decide which schemes fit this kind of product

Use only what the scheme records and `references/scheme-kinds.md` state about what each scheme covers. Examples the records state: FR_LPPR is for therapeutic digital medical devices; FR_LATM is for telemonitoring activities; IE_HSE_CGM lists CGM sensors for type 1 diabetes only; US_CMS_DMHT covers digital mental health treatment codes; US_CMS_RPM pays remote monitoring services by code, not products. For each scheme write fits, does not fit, or unclear, with the one-line reason. A scheme that does not fit stays in the map as a line, so the reader sees it was considered.

### Step 3. Read what each fitting scheme requires

Read the requirements file for the country in `references/requirements/` (Germany, France, United Kingdom). Each row is a primary-source requirement with its URL, quote and date read: take eligibility, regulatory prerequisite, evidence bar, clock, price mechanics and certifications from there, and cite the row's source. Add the scheme record's `clock_rule` and `notes`. Only for a country or point not covered there, call `retrieve_guidance` once with a short query and use a passage only if it carries a `source_url`. Anything still unsourced is `[GAP]` with the authority to check. Where the requirements file lists a conflict between sources, show both and say which is newer. Do not fill requirements from memory: they change, and a wrong requirement is worse than a named gap.

### Step 4. Count precedents

For each fitting scheme, call `find_scheme_precedents` with `scheme` and the `indication`, in the register's language or as an ICD code (see `references/tools.md`); an English term can miss German rows. Report how many comparable products are listed and name up to three, with status and date. Zero precedents in a well-loaded scheme is a finding; zero in a scheme the library barely covers is a gap. Say which.

### Step 5. Note where the product already is

If the conversation already holds an A1 status check for this product, use it. Otherwise one `search_listings` call for the product name tells you whether any route is already taken.

## Build the output

Follow `assets/pathway-map-output.md`, short or full by the same rule as A1: "quick" or "overview" gets the short map; a document to share gets the full one.

## Before you hand it over

- Every requirement, clock and precedent carries its source and retrieval date, or is `[GAP]`.
- Do not send register facts to the Verify claim tools (they rate register pages inadmissible; see `references/tools.md`).
- If the map will leave the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by`; otherwise label it an uncleared draft.

## Boundaries

- No ranking, sequencing or recommendation of which route to take: that is task B1. You may name the facts that will drive the choice (a running clock, a missing prerequisite, no precedent).
- Precedent prices may appear as the competitors' recorded prices, labeled as such with their retrieval date. Never turn them into a price for this product: a pricing position stops for its accountable owner.
- No promise that a product would qualify. Precedents show a route exists, not that this product meets it.
- No regulatory classification. Missing class is a gap routed to regulatory work.
- Drugs, biologics and wellness apps are out of scope.
