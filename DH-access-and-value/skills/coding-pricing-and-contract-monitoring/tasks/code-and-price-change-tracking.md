# A1 Code and price change tracking

Framework task: DH-03.01.2.2, Part A, task A1.

## What this task delivers

A dated list of what changed and what is proposed for the codes, price rules and registered prices the person's strategy depends on: new, revalued or redefined codes; conversion factors; DiGA threshold and group maximums; the month-13 price switch; French fee orders; and pending rules with their publication dates. It answers "what has moved under our coding and price assumptions, and what is about to?"

Why it matters: the CY 2026 fee schedule added short-duration monitoring codes and the CY 2027 proposals would change who may furnish the service; the German maximums reset every six months. A coding strategy or contract written against last year's rules can be wrong without anyone noticing.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.2 Part A, Code and price change tracking |
| Workflow | The steps below |
| Knowledge | `references/publication-cycles.md`; `references/coding-pricing-sources.md`; the person's coding map or contract (baseline) |
| Tool | `list_schemes`, `find_scheme_precedents`, `get_status_history`, `search_listings`; `commercial-dh.get_deltas` only to confirm it has nothing |
| Prompt | This guide |
| Template | `assets/change-tracking-output.md` |
| Input | The request and its context; the codes, routes and products the person depends on; the baseline (an earlier run, the coding map from the sibling skill, or contract values) |
| Governance | `references/governance.md` |

## Read the request

- **What to track.** The codes (for example 99454, G0553), routes (DiGA, PECAN, LATM, ACCESS) and comparator products. If the conversation holds a coding map from the sibling skill (DH-03.01.2.1), take them from it.
- **Baseline.** An earlier run, a contract value, or "as of" a date. Without one, the output is a current snapshot plus the publication calendar, and says so.
- **Mode.** Short for a direct question; full for a review pack.

## Workflow

### Step 1. Know what the library can see

Call `list_schemes` (free). Note last-load dates for the schemes in scope. Say once that the library stores no price or code history (`references/tools.md`).

### Step 2. Today's values

For US codes: `find_scheme_precedents` on US_CMS_RPM and US_CMS_DMHT; read the amount from the passage where `price` is empty. For DiGA comparators or the person's own product: `find_scheme_precedents` with the indication, or `search_listings` with the name. Record value, setting, source and retrieval date.

### Step 3. Compare with the baseline

Where the person gave a baseline, compare value by value and state each difference with both dates. Where the library has only one snapshot, say the change date is `[GAP]`. A call to `get_status_history` confirms a day-zero snapshot; do not quote `durability_days` as a change date.

### Step 4. Published changes in force

From `references/publication-cycles.md`, list what changed in the current cycle for the routes in scope: for the US the CY 2026 final rule (US2 to US8, US18, US19, US21); for Germany the current threshold and maximums window (DE14, DE16), the 20 percent rule (DE2); for France and England what the sources state. Each with effective date and row.

### Step 5. Proposed changes

List each proposal that touches a tracked code or route, with "proposed 16 July 2026; comments closed 14 September 2026; final rule not published as of the read date" (US22 to US28). For Germany list the 2027 volume discount (DE3) as enacted, effective 1 January 2027.

### Step 6. Clocks that move a price

For each listed DiGA in scope, count from the listing date: end of year one and start of the agreed amount (DE1, DE9), the nine-month arbitration point (DE5). For thresholds and maximums, the end of the current window (31 March 2027, DE14). State dates, not urgency.

### Step 7. What it means for the person

Conditional consequences only, tied to rules: "if US25 is finalized, time furnished by contracted monitoring staff stops being payable from 1 January 2027"; "your DiGA reaches month 13 on DATE; from then the agreed amount applies". Route anything that needs a strategy or contract change to the sibling skill DH-03.01.2.1.

## Build the output

Follow `assets/change-tracking-output.md`. Answer first: the one or two changes that matter most to what the person tracks.

## Before you hand it over

- Every change has a publication or effective date and a row or library source.
- Proposals are labeled proposed; nothing proposed is written as current.
- No change date is inferred from a snapshot.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- Tracking only; whether the contract performs is A2 and B1.
- No forecast of what a final rule will say.
- Drugs, biologics and wellness apps are out of scope.
