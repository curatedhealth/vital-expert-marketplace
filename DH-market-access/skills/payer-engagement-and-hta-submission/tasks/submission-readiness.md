# A2 Submission readiness

Framework task: DH-03.01.3.1, Part A, task A2. Replaces the earlier "HTA Submission Preparation" section.

## What this task delivers

Per target body: the completeness checklist with each item marked present, missing or `[GAP]`; the fees that will apply; the review clocks from a complete file; the consultation options with their cost and lead time; the failure patterns the body itself publishes; and how comparable products fared on the same route. It answers "are we ready to file, what will it cost, and how long will it take?"

Why it matters: incompleteness, not evidence, stops most files first. In 2025, 69 percent of LPP and intra-GHS requests to CNEDiMTS had at least one incompleteness suspension (`FR24`). In Germany, an incomplete file gets up to three months to complete and is then refused (`DE22`), and a refused or withdrawn DiGA waits 12 months to re-apply with new evidence (`DE23`).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.1 Part A, Submission readiness |
| Workflow | The steps below |
| Knowledge | `references/readiness-checklists.md`; `references/engagement-options.md`; `references/hta-submissions-sources.md`; `references/requirements/` |
| Tools | `market-access-dh.list_schemes` (free), `market-access-dh.find_scheme_precedents`; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/readiness-output.md` |
| Input | The request and its context: body and route, what the person has ready (their list or the A1 map), device class |
| Governance | `references/governance.md` |

## Read the request

- **Body and route.** One checklist per route: DiGA permanent or trial; LPPR, PECAN or LATM; NICE; Medicare NCD or TCET. If the route is open, show the two most likely and say which facts decide.
- **What the person holds.** Their own list, or the A1 map from the conversation. Items they have not mentioned are `[GAP]`, not missing.
- **Mode.** "Are we ready" or "what does it cost" is short mode. A readiness review for a filing decision is full mode.

## Workflow

### Step 1. Copy the checklist

From `references/readiness-checklists.md`, copy the items for the route, with row ids. Mark each present (the person says so or a document shows it), missing (the person says it is not there), or `[GAP]` (not discussed). Put the formal-completeness conditions first: for DiGA the portal, the gematik confirmation and the BSI certificate (D1 to D3); for PECAN the Sésame and Convergence filings (F3); for LATM the ANS certificate (F4).

### Step 2. Fees and clocks

State the fee ranges and the clocks for the route, each with its row. Count nothing the source does not give: actual BfArM days to decision are not published (`[GAP]`). Where the ordinance and the guide differ (receipt confirmation 21 versus 14 days), give both and say which is law and which is practice (conflict note 4). State clocks as facts, never as pressure.

### Step 3. Consultation options

From `references/engagement-options.md`, give the early-contact route for the body with cost, lead time and limits. For BfArM: EUR 250 to 5,000, usually three to four months from request to meeting, package three weeks before, advice non-binding and no pre-assessment of data (`DE27`, `DE28`). For HAS: early and pre-submission meetings, free and confidential (`FR11`).

### Step 4. Failure patterns from official statistics

Give the body's own figures as context, with their period:
- BfArM, as of 9 September 2026: 254 applications; 62 listed, 29 refused, 131 withdrawn, 14 in review, 18 delisted (`DE33`, `DE34`). Say that withdrawals far exceed refusals and that BfArM does not name refused products (`DE32`).
- CNEDiMTS 2025: 69 percent of requests suspended at least once for incompleteness, 51 percent for administrative reasons only, mean 49 days to administrative completeness (`FR24`); the 2023 analysis of causes (device description, clinical data, missing vigilance data) (`FR7`); organizational impact rarely evaluated (`FR25`).
- NICE: missing information may affect the recommendation (`UK4`).
These are what happened to other files. They are not the person's odds.

### Step 5. Comparable decisions

Call `market-access-dh.list_schemes` (free) once, then `market-access-dh.find_scheme_precedents` on the route's scheme, narrowed by `indication` in the register's language or ICD code (DE_DIGA: `F51`, not "insomnia"). Report up to three comparable products with status, listing date and source. Say what the library cannot show: the evidence behind each listing (read the directory page), refusals (not published, `DE32`), and FR_LPPR (no rows loaded). For NICE, rows are guidance documents, not products; count renumbered guidance once (`references/tools.md`).

### Step 6. What blocks filing

List, in dependency order, the missing items that block formal completeness, then the ones that block a decision on substance, then the rest. Dependency order is a fact (for example, the DiGA trial route needs the independent evaluation concept before filing, `DE19`); when to file is the person's decision.

## Build the output

Follow `assets/readiness-output.md`. Answer first: complete or not against the sourced checklist, the blocking items, total fee range, and the review clock from a complete file. Then the checklist, clocks, consultation, failure patterns and comparables.

## Before you hand it over

- Every item, fee and clock has its row; the read date is stated.
- No "ready to file": say "complete against the sourced checklist of 19 October 2026" at most.
- Statistics carry their period and are labeled context.
- Filing and any wording for the body stop for the owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checklist and facts only; the quality of each section is checked in the monitoring skill (DH-03.01.3.2, A1) and judged by the person.
- No price proposal for the actual-price field or the CEPS file: that is the coding, pricing and contracting skill.
- Drugs, biologics and wellness apps are out of scope.
