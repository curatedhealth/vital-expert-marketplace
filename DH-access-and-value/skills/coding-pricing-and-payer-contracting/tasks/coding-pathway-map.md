# A1 Coding pathway map

Framework task: DH-03.01.2.1, Part A, task A1 (old name: Coding Pathway Strategy).

## What this task delivers

Per target market, the codes or payment routes that could pay for the product, what each one pays (a service, the product, or a contract), who bills, the entry conditions, which conditions the product meets or not, and which changes are proposed but not law. It answers "which code or route would pay for this, and what would it take to use it?"

Why it matters: a team that assumes "there is a code for remote monitoring" can discover late that the code pays the clinician, needs an FDA device, allows one biller per month, or is about to be rewritten. A map with the entry conditions and the pending changes puts that in front of the pricing and contracting work.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.1 Part A, Coding pathway map |
| Workflow | The steps below |
| Knowledge | `references/payment-routes.md`; `references/coding-pricing-sources.md`; `references/france-pecan-lppr-latm.md`; `references/gap-rules.md` |
| Tool | `list_schemes`, `find_scheme_precedents`, `search_listings`; `scripts/price_facts.py` (optional) |
| Prompt | This guide |
| Template | `assets/coding-pathway-map-output.md` |
| Input | The request and its context; the inputs below; a coverage pathway map from the coverage pathway skill, if present, is reused |
| Governance | `references/governance.md` |

## Read the request

| Input | Needed for | If missing |
|---|---|---|
| What the product does: remote physiologic or therapeutic monitoring, digital mental health treatment, therapeutic app, telemonitoring, other | Which routes fit | Ask once; it decides the map |
| Regulatory status: FDA pathway and classification (for DMHT: 21 CFR 882.5801 or 882.5803), CE class | Entry conditions | `[GAP]`; route to the Regulatory pack's classification work. Never guess a classification |
| Who delivers care: the product alone, a practice, or the person's own clinical staff or vendor staff | RPM/RTM biller rules and the 2027 staffing proposal | Ask in the same question |
| Markets | Scope | Map US, Germany, France and England and say so |
| Indication | Comparables and ACCESS track fit | Use the request's words |

Mode: a direct question gets the short map; a document gets the full one.

## Workflow

### Step 1. Know what the library holds

Call `market-access-dh.list_schemes` (free). Note listing counts and last load for US_CMS_RPM, US_CMS_DMHT, DE_DIGA, FR_PECAN, FR_LATM, FR_LPPR. Routes with no library scheme (RTM, ACCESS, EBM, England) come from `references/payment-routes.md` only; say so once.

### Step 2. Pull the stored code rows

For the US, call `market-access-dh.find_scheme_precedents` with `{scheme: "US_CMS_RPM", limit: 25}` and `{scheme: "US_CMS_DMHT", limit: 25}`. Keep for each code: identifier, status, price field, the evidence passage (it holds the amounts and RVUs), source and retrieval date. Where `price` is empty, read the amount from the passage; with code execution, run `scripts/price_facts.py` on the saved output. A code in the research file but not in the store (99445, 99470, RTM codes) is "not stored, sourced" (`gap-rules.md`).

### Step 3. Decide which routes fit

Go through `references/payment-routes.md` market by market. For each route write: fits, does not fit, or unclear, with a one-line reason tied to a row id. Examples of decisive conditions: DMHT needs FDA clearance at 882.5801 or 882.5803 and the practitioner must incur the device cost (US17, US18); RPM and RTM pay a practitioner with E/M billing rights, one per patient per 30 days (US15); CMS did not finalize codes for tools without FDA authorization (US21); in England no code exists and the route is procurement plus DTAC (EN4, EN5). Keep routes that do not fit as one line each, so the reader sees they were considered.

### Step 4. Name the conflicts between routes

State where two routes cannot be used together for the same patient: RPM with RTM (US12); ACCESS participants cannot bill other FFS claims for aligned beneficiaries, and DMHT or RTM set-up billed elsewhere counts as substitute spend against an ACCESS behavioral health participant (US34, US36).

### Step 5. Add the pending changes as dated risk

From the CY 2027 proposed rule (US22 to US28), list each proposal that touches a fitting route, written as "proposed 16 July 2026; final rule not published as of the read date". For a model built on vendor-employed monitoring staff, US25 is the first line. Never write a proposal as current rule.

### Step 6. Check where the product already is

If no coverage status is in the conversation, one `search_listings` call with the product name shows whether a route is already taken (a DiGA PZN, a PECAN or LATM code).

### Step 7. Comparables, if asked

For Germany or France, `find_scheme_precedents` with the indication (ICD code or German term for DE_DIGA) shows which products use the route. Report how many and name up to three. Their prices go to A2, not here.

## Build the output

Follow `assets/coding-pathway-map-output.md`. Answer first: the one or two routes that fit and the condition that decides each. Then the map per market, the conflicts, the pending changes, and the gaps.

## Before you hand it over

- Every code, amount and condition carries its row id or library source with retrieval date.
- Every proposal is dated and labeled proposed.
- No regulatory classification is asserted for the product.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No price for the product (task A2 lays out price facts; the position is the owner's).
- No billing instruction for a specific claim and no advice to bill a service not furnished.
- Coverage status and benefit design belong to the coverage pathway skill; outcome contracts to the value-based care skill.
- Drugs, biologics and wellness apps are out of scope.
