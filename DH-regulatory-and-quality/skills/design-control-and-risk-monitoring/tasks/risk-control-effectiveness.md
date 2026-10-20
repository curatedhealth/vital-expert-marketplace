# A2 Risk control effectiveness from post-market data

Framework task: DH-03.02.1.2, Part A, task A2.

## What this task delivers

A table that puts what happened after launch beside what the risk file expected: the person's own complaints and incident files, plus software recalls and alerts for the product and comparable products from the library. For each hazard: own events, comparable events, the highest observed severity against the file's estimate on the person's scale, and the events that match no hazard at all. It answers "were the harms we are seeing foreseen in our risk file", "are our controls working", and "what does the recall history of similar products say about our file".

Why it matters: the MDR requires post-market information to feed back into hazards, estimates and acceptability (EU15), and FDA expects the risk file updated when unforeseen risks appear (QS22). A file that never meets the field drifts away from the product.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.2 Part A, Risk control effectiveness from post-market data |
| Workflow | The steps below |
| Knowledge | `references/post-market-feedback.md`; `references/quality-systems-sources.md` (EU14, EU15, QS18, QS22, VG rows); library safety events |
| Tools | `regulatory-dh.list_jurisdictions` (free); `regulatory-dh.search_safety_events` (counted, two to five calls); `scripts/risk_feedback.py` |
| Prompt | This guide |
| Template | `assets/effectiveness-output.md` |
| Input | The request and its context: the product, its manufacturer name as registered, comparables, the period, the person's risk file (hazards, severity, probability, controls), their complaint or incident extract (de-identified), their severity scale |
| Governance | `references/governance.md`; mapping, severity and effectiveness are the person's |

## Read the request

- **Product and comparables.** The person's firm and product, and the comparables they name. If they name none but ask what similar products were recalled for, that request is consent: run the device-type search (step 2.3) first, then search by `manufacturer` each firm that appears in it, without `since` unless the person gave a period, and say which firms were searched and which were not. If they neither name comparables nor ask about them, propose comparables and ask before calling.
- **Period.** Use `since` for the monitoring period the person gives; otherwise search without it and state the date range returned.
- **Own data.** Complaints and incident files come from the person, de-identified. If none are given, the task runs on comparables only and says the product's own field experience was not reviewed.
- **Short or full.** A direct question gets short mode; a periodic review or a risk management report update gets full mode.

## Workflow

### Step 1. Say what the library can cover

Call `regulatory-dh.list_jurisdictions` once. State the coverage line: US software-related recalls and MAUDE counts, UK MHRA alerts; EU vigilance and Swiss field safety actions not loaded. For an EU-only product, say that the library cannot show its field events.

### Step 2. Search the product, then comparables

1. The person's own firm: `{"manufacturer": "<firm as registered>", "since": "<period start>", "limit": 25}`.
2. Each named comparable firm: `{"manufacturer": "<firm>", "limit": 15}`, adding `since` only for a monitoring period the person gave. Older comparable recalls show foreseeability and are often the closest match (the 30 November 2023 Omnipod 5 Android recall names the confirmation screen as the safeguard that failed).
3. The device type: `{"product": "<generic word, for example insulin>", "jurisdiction": "US", "limit": 10}`.
4. Only if the person gives their FDA product code from the authorization record: `{"product_code": "<code>"}` for the MAUDE count by year.

Save each response. Fold duplicate rows into events: `python3 scripts/risk_feedback.py --from-connector out1.json out2.json > events.csv`. It writes `origin = comparable` for every library row; change it to `own` for rows about the person's own product.

### Step 3. Add the person's own events

Append the person's complaints and incident files to the same table with `origin = own`. Keep their ids. Never put their data into a library call.

### Step 4. Map events to hazards: proposed, then confirmed

For each event, propose the hazard it matches in the person's file, with the words in the event that support the mapping, marked "proposed". Leave events that match nothing unmapped. Ask the person to confirm or change the mapping and to give the observed severity on their own scale. Software harms are often indirect: a decision made on a wrong or late value (VG14, VG15).

### Step 5. Compare

Run `python3 scripts/risk_feedback.py --risk risk_file.csv --events events.csv --scale scale.json`. Without code execution, build the same table by hand. For each hazard read the four outcomes in `references/post-market-feedback.md`: foreseen and within estimate; foreseen but worse than estimated; foreseen but the control did not prevent it; not foreseen. The table shows the facts; the person decides which outcome applies and whether the control is effective.

Treat the two kinds of evidence differently. Own events bear on the product's estimates. A comparable's event shows that a hazard is foreseeable and how severe it became elsewhere; when it is worse than the file's estimate, it is a reason for the owner to re-examine the estimate, not proof it is wrong.

### Step 6. Flag reporting questions, without deciding them

For own events that may meet a reporting definition (`references/post-market-feedback.md`, reporting facts) and have no recorded reporting decision, list them as open items for the person's vigilance owner, with the clock that would apply and from which awareness date. Do not compute a deadline from a date the person has not confirmed.

## Build the output

Follow `assets/effectiveness-output.md`. Short mode: the answer (how many observed harms map to foreseen hazards, how many do not, where observed severity exceeds the file), the hazard table, unmapped events, open items. Full mode adds every event with its source, the mapping basis, and the coverage statement.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Short mode: count the words, excluding tables' source column and any 'Calls made' log; if over 450, cut in the stated order before sending.
- Every library event carries date, firm, product line, recall class or alert type, and retrieval date; duplicates folded.
- Own and comparable events are counted apart.
- Each reporting fact carries the row that states it: 10 working days is VG22, the recorded justification is VG24, and "a pushed software fix is a correction" is VG25, not VG22 or VG24.
- Mappings are confirmed by the person or marked "proposed".
- No sentence says a control is effective or a risk acceptable.
- Store gaps are stated; absence of library events is never "no events".
- Risk file updates, CAPA and reporting decisions stop for the owner. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- No incidence rate from MAUDE counts (reports, no denominator).
- No reportability decision; no field action recommendation as decided.
- No clinical judgment about an individual patient.
