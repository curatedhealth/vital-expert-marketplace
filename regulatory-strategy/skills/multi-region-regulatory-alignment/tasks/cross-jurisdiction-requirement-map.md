# A1 Cross-jurisdiction requirement map

Framework task: DH-03.03.2.1, Part A, task A1. Replaces the earlier "Cross-Jurisdiction Requirement Mapping" and "List jurisdictions" sections.

## What this task delivers

One table that shows, region by region, how the same software is classified, which route applies, which reliance or recognition routes exist and whether each is law or still a draft, how MDSAP is used there, and what registration is due once authorized; plus what the library holds for the product (or its comparables) in each region. It answers "what does each region require for this software, and where do we already stand?"

Why it matters: a multi-region plan fails most often on a wrong assumption carried from one region to another: that the EU class applies in Great Britain, that an FDA clearance opens Switzerland, that a consulted reliance route already exists.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.1 Part A, Cross-jurisdiction requirement map |
| Workflow | The steps below |
| Knowledge | `references/jurisdiction-requirements.md`; `references/multi-region-sources.md`; `references/pathways-submissions-sources.md` |
| Tools | `regulatory-dh.list_jurisdictions`, `search_devices`, `compare_authorizations`, `get_market_status`; `scripts/market_matrix.py` (optional) |
| Prompt | This guide |
| Template | `assets/requirement-map-output.md` |
| Input | The request and its context: product, intended purpose, target regions, authorizations already held, classes already argued |
| Governance | `references/governance.md`; the class and pathway are the regulatory owner's decision |

## Read the request

- **Product and intended purpose.** The intended purpose drives every class. If it is missing, ask for it; without it, the class column stays "depends on intended purpose `[GAP]`".
- **Regions.** Take the person's list. If none is given, ask; do not choose markets.
- **What is held.** Existing clearances, CE certificates, MDSAP certificate, licenses. These decide which reliance routes are even open.
- **Mode.** A direct question gets short mode. A planning document gets full mode.

## Workflow

### Step 1. Know what the library can see

Call `list_jurisdictions` (free). For each target region note whether the library holds records, when it last loaded them, or why it cannot (Australia, Brazil and Japan are closed; Great Britain holds safety alerts only; Switzerland holds nothing; Canada is loaded but not searchable by product). Say this once and move on.

### Step 2. What the library holds for the product

Call `search_devices` with the product or manufacturer name, `software_only` "false", `limit` 25. If the product is new, search the closest comparables the person names and treat them as comparables, never as the product. Then call `compare_authorizations` with the identifiers of the same software in each region (for example a K number and a Basic UDI-DI) to put class, pathway and decision date side by side. Call `get_market_status` only for the summary, and merge its rows: one row comes back per stored record, and "false" means "no record in the library's copy" (`references/tools.md`). With code execution, run `scripts/market_matrix.py` on the saved outputs.

Describe each record only by what it states: regime, class as recorded, pathway, identifier, decision date, source and retrieval date. Where a region shows more than one class (MDD-era and MDR records), report both by identifier and do not explain the difference.

### Step 3. Classification per region

For each region, lay out the rule that applies to software from `jurisdiction-requirements.md` section 1 and where the person's intended purpose falls under it, as an argument for the regulatory owner: "Under MDR Rule 11 decision software is IIa, IIb or III by the impact of the decision (EU-02, EU-03); a triage output for stroke imaging points to IIb or III; the owner decides." Flag known divergences in one line each, especially Great Britain (class I is possible where the EU gives IIa, UK-14). Where no rule was read (Canada software rule, Brazil, Japan), write `[GAP]`.

### Step 4. Route, reliance and legal status

For each region, state the route for the class argued (section 2) and every reliance or recognition route into it from what the person already holds (section 3), with its legal status word: in force, draft, proposal, exploratory. Examples of the wording: "Australia: an FDA 510(k) decision is accepted evidence for the same device; an audit may be required (MR-09, MR-10, MR-11): in force." "Great Britain: reliance on FDA authorization is in a draft statutory instrument (MR-26, MR-27): not available today." Never present a draft or proposal as a route the person can use.

### Step 5. MDSAP

If the person holds or plans an MDSAP certificate, state per region how it is used (section 4), including limits (FDA routine inspections only; TGA only if Australian requirements were audited; Health Canada's requirement rests on the MDSAP site, not the regulation's text).

### Step 6. Registration duties

For each region, list the duty that follows authorization and its window (section 5): FDA annual registration 1 October to 31 December, Health Canada annual statement before 1 November, EUDAMED UDI/device registration (28 November 2026 for devices already placed before 28 May 2026), Swiss registration from July 2026, MHRA registration. Where a duty was not read, `[GAP]`. For a dated table, point to the monitoring skill.

### Step 7. What it means for the person

Close with consequences stated as conditions, from sourced mechanics only: "If the EU class is IIb, a notified body is needed (EU-09); that certificate is also accepted evidence in Australia and the basis for Switzerland." Never a forecast of approval.

## Build the output

Follow `assets/requirement-map-output.md`. Answer first: the two or three differences that change the plan. Then the region table, stored records, and gaps. Short mode for direct questions.

## Before you hand it over

- Every rule cites its row; every stored record has its identifier and retrieval date.
- No class or pathway is declared final; each is an argument for the owner.
- Every reliance route has its legal status word.
- No gap is worded as "not authorized".
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Mapping only. Evidence reuse is A2; order and adaptation are B1.
- No regulator correspondence, no submission text.
- Drugs, biologics and wellness apps are out of scope.
