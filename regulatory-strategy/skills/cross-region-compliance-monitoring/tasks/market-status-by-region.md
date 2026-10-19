# A1 Market status by region

Framework task: DH-03.03.2.2, Part A, task A1. Replaces the earlier "Cross-Region Compliance Monitoring" section (status part).

## What this task delivers

A dated view of where the product is authorized according to the registers the library holds, and which registration, renewal and acceptance dates are running in each of the person's markets. It answers "where do we stand in each region, and which dates are coming up?"

Why it matters: authorizations do not stay valid on their own. Annual registrations, license statements, certificate expiries, EUDAMED registration and the end of CE acceptance in Great Britain all run on different clocks in different regions.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.2 Part A, Market status by region |
| Workflow | The steps below |
| Knowledge | `references/obligations.md`; the multi-region plan if the conversation holds one |
| Tools | `regulatory-dh.list_jurisdictions`, `get_market_status`, `search_devices`, `get_register_deltas`; `scripts/obligations_table.py` |
| Prompt | This guide |
| Template | `assets/market-status-output.md` |
| Input | The request and its context: product, markets entered, basis per market (for example CE under the MDR for Great Britain), certificate dates, first placing date in the EU, a baseline (an earlier run or date) |
| Governance | `references/governance.md` |

## Read the request

- **Product and markets.** Take the markets from the plan (DH-03.03.2.1) if the conversation holds one; otherwise ask.
- **Dates the clocks need.** EU first placing date; QMS certificate issue or expiry for Canada; the GB basis (CE under MDR, MDD, up-classified MDD, or UKCA); Brazil GMP certificate date. Missing ones stay `[GAP]` in the table, and you ask.
- **Baseline.** An earlier run or a date to compare against. Without it, the output is a snapshot and says so.

## Workflow

### Step 1. Know what the library can see

Call `list_jurisdictions` (free). For each market: records held and last load, or "register not loaded" (Great Britain registration, Switzerland, Australia, Brazil, Japan) or "not searchable" (Canada).

### Step 2. Status per region

Call `get_market_status` with the product name and merge its rows (any true wins; "false" is "no record in the library's copy"). Then call `search_devices` with `limit` 25 for identifiers, classes as recorded, pathway, decision dates and retrieval dates. Report each record by regime and identifier; if a region shows records under two regimes (for example EU_MDD and EU_MDR), list both and do not explain the difference. Classify every absence with `references/gap-rules.md`.

### Step 3. What changed since the baseline

Call `get_register_deltas` for the manufacturer (or FDA product code, or EMDN code) since the baseline date. If it says the log has not started, write "no change recorded; the log has not started for this scope" and compare instead: US records with a decision date after the baseline, or the person's earlier run. EU records carry no decision date, so EU change can only be seen by comparing runs.

### Step 4. Dated obligations

Build the obligations table from `references/obligations.md`. With code execution, write the person's markets and dates to a JSON file and run `scripts/obligations_table.py FILE --as-of DATE`. Each line has its date or window, days from the as-of date, legal status and row. A passed date reads "confirm what was filed". A duty no row sources reads `[GAP]`.

### Step 5. What it means for the person

Close with conditional consequences from sourced mechanics: "If the device was first placed in the EU before 28 May 2026 and units are still placed, EUDAMED UDI/device registration is due by 28 November 2026 (JX-39)." "Great Britain accepts the CE mark under the MDR until 30 June 2030; indefinite recognition is only a proposal (UK-03, UK-05)." No prediction, no urgency language.

## Build the output

Follow `assets/market-status-output.md`. Answer first: the next two or three dates and any status change. Then the status table, the obligations table and the gaps. Short mode for direct questions.

## Before you hand it over

- Every status has its identifier and retrieval date; every obligation its row.
- No "false" is worded as "not authorized"; no empty log as "no change".
- No passed date is worded as missed.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Status and dates only. Guidance and law changes are A2; whether the alignment is holding is B1.
- No filing on the person's behalf; the owner files.
- Drugs, biologics and wellness apps are out of scope.
