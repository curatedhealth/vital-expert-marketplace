# A1 Channel map and partner roles

Framework task: DH-02.01.4.1, Part A, task A1. Replaces the register tasks "Partner role" (CF-12.02.01.4.1.1) and "Channel handoff" (CF-12.02.01.4.1.3).

## What this task delivers

A channel map per market: which routes reach the buyer, who the user, buyer and payer are on each route, the rules each route sets with their rows, a role card for each partner (sell, implement or refer; segment; what it must not do), and the handoff from partner to the person's team. It answers "how does our product reach the buyer, and who does what?"

Why it matters: a route decides who the buyer is, and the buyer decides the rules. G0552 is not payable unless the billing practitioner bears the device cost (CP-US-59), so a manufacturer-pays channel cannot use it; German contract physicians may make no deals about routing DiGA prescriptions (CP-DE-06); a partner that touches PHI is a business associate (CP-US-44). A channel drawn without these facts has to be redrawn after legal review.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.1 Part A, Channel map and partner roles |
| Workflow | The steps below |
| Knowledge | `references/channel-rules.md`; `references/fraud-and-abuse-stops.md` (triggers); GTM segments and pricing from other Commercial tasks if the conversation holds them |
| Tools | `commercial-dh.list_commercial_dh_sources` (free); `diligence-dh.build_company_profile` and `diligence-dh.get_funding_signals` for a named partner; `commercial-dh.screen_commercial_peers` for the segment (optional) |
| Prompt | This guide |
| Template | `assets/channel-map-output.md` |
| Input | The request and its context: product and its regulatory status as the person states it, markets, buyer segments, named partners, how the person sells today |
| Governance | `references/governance.md`; people choose channels, partners, segments and owners |
| Catalogue job | `company-dossier` (build_company_profile, get_funding_signals) for a named partner; `screen-commercial-peers` for the segment. The direct calls in the steps remain the method. `examples/live/list_jobs_commercial.json` |

## Read the request

- **Product and status.** Device or not, classification if US (for example 21 CFR 882.5803), DiGA listed or not. From the person or the Regulatory pack; if unknown, `[GAP]`, because several channel rules depend on it (CP-US-58, CP-US-70, CP-DE-01).
- **Markets and segments.** Which countries and which buyer segments (health systems, practices, payers, employers, consumers).
- **Partners.** Named partners and the role the person has in mind.
- **Mode.** Short for a direct question ("can we sell through X"); full for a channel plan.

## Workflow

### Step 1. Name the three roles per segment

For each segment, write who uses the product, who buys it from the seller, and who pays a claim (if anyone). Do not merge them. If the person has a GTM segmentation from the Commercial GTM task, start from it.

### Step 2. List the routes and their rules

For each market and segment, list the candidate routes the person named (direct, reseller, implementation partner, referral partner, practitioner-billed, DiGA prescription or fund approval, NHS framework, direct to consumer). For each, pull the rules from `references/channel-rules.md` with row ids, and state the consequence in one line ("if the device is not in 882.5801 or 882.5803, the DMHT route does not apply: CP-US-58, CP-US-62"). Where a route has no sourced rule (employer, app store), write `[GAP]`.

### Step 3. Flag fraud-and-abuse triggers early

Scan the person's design against triggers T1 to T8 in `references/fraud-and-abuse-stops.md`: pay per referral or volume, outcomes-based partner pay, paid lead or referral platforms, free items to patients, donated technology to providers, discounts, value-based arrangements, German prescription or pharma links. List each trigger hit in one line with its row and "stops for your compliance or legal owner". The elements are laid out in A2.

### Step 4. Public view of named partners (optional)

Call `commercial-dh.list_commercial_dh_sources` (free) once to see which sources are loaded. For each named partner that is a regulated digital health company, call `diligence-dh.build_company_profile {company: "<exact legal or brand name>"}`; for a partner that may be an SEC reporting company, call `diligence-dh.get_funding_signals {company: ...}`. Report only what the record states: authorizations with numbers and dates, studies and their link basis, filings by type with dates. Never infer revenue, outcomes, financial health or intent; the latest filing date is not a status. A partner that is a health system, GPO or reseller is usually not in the store: say "not in the store (coverage limit)". Avoid putting a confidential prospective partner's name into a call unless the person agrees.

For "who else sells this way", call `commercial-dh.screen_commercial_peers {segment: "dtx", limit: 10}` and use the `screen_market` block only (`references/tools.md`).

### Step 5. Write a role card per partner

For each partner: role (sell, implement or refer), segment and market covered, whether it is exclusive (the person's choice), what it must not do (from the rules: no prescription routing in Germany, CP-DE-06; no claims beyond the approved list; no implied FDA approval, CP-US-74; no PHI outside the BAA, CP-US-46), and the data it touches. If two partners hold the same exclusive segment, say so plainly.

### Step 6. Write the handoff

For each partner: the event that moves a buyer from the partner to the person's team (for example a signed order form or a qualified opportunity, in the person's words), the internal owner who receives it (as the person names them; "owner not named" otherwise), and what the partner still does after (implementation, first-line support, nothing). If data moves at handoff, name the term it needs (BAA, processor terms) and send it to A2. A shared inbox is not a handoff owner.

### Step 7. What it means

Close with the consequence of the facts for the person's plan: which routes are open on the facts given, which depend on a `[GAP]` (classification, framework membership), and which carry a fraud-and-abuse stop. No ranking here; that is B1 on the person's scores.

## Build the output

Follow `assets/channel-map-output.md`. Answer first: which routes fit the product on the facts given and which stop. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- User, buyer and payer are separate on every route.
- Every rule has a row; every unknown is `[GAP]`.
- Partners are described only by what their records state.
- Every fraud-and-abuse trigger is listed as a stop, never judged.
- Channels, partners, exclusivity and owners are the person's, and the output says so.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Channel structure only. Payer coverage, codes and payment amounts are Market Access; device status is the Regulatory pack.
- No legal opinion on any arrangement.
- Drugs, biologics and wellness apps are out of scope.
