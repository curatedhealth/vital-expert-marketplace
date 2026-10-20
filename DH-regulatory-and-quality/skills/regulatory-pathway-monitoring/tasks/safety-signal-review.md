# A2 Safety signal review

Framework task: DH-03.03.3.2, Part A, task A2. Replaces the earlier "Search safety events" section.

## What this task delivers

A dated summary of the public safety records for the person's product and its comparables: recalls, MAUDE report counts and MHRA alerts, each described only as the record states it, with what the library cannot see named. It answers "what do the public safety records show for us and for products like ours, and does anything bear on our pathway?"

Why it matters: a recall in a comparable can change what a regulator asks of the next submission in that code, and what the person's own risk file has to address. Public records are thin and easy to overread; a count of reports is not a count of failures.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.2 Part A, Safety signal review |
| Workflow | The steps below |
| Knowledge | `references/safety-records.md`; `references/quality-systems-sources.md` (vigilance rows) |
| Tools | `regulatory-dh.list_jurisdictions` (free), `regulatory-dh.search_safety_events`, `regulatory-dh.compare_authorizations` (optional) |
| Prompt | This guide |
| Template | `assets/safety-review-output.md` |
| Input | The request and its context: product, manufacturer, product codes, comparables (from the strategy or A1), period (`since`) |
| Governance | `references/governance.md`; reportability is the person's vigilance owner's decision |

## Read the request

- **Scope.** The person's product and manufacturer; comparables by manufacturer or product; the FDA product code(s). At least one of manufacturer, product or product code is required by the tool.
- **Period.** A `since` date, or all stored records.
- **Purpose.** Pathway context (what regulators may ask) or the person's own post-market view. The person's complaint and vigilance data stay with them; never put them into a library call.
- **Mode.** A direct question gets short mode.

## Workflow

### Step 1. Know what the library can see

Call `regulatory-dh.list_jurisdictions` (free): US recalls and MAUDE counts are loaded; UK has MHRA alerts only; EU has no safety events (the EUDAMED vigilance module is not live, RP EU-38); Switzerland is not loaded. Say so once.

### Step 2. Search by manufacturer, product and code

Call `regulatory-dh.search_safety_events` for each scope, for example:
- `{"product_code": "QVO", "jurisdiction": "all"}`
- `{"manufacturer": "Big Health", "jurisdiction": "all"}`
- `{"product": "Somryst", "jurisdiction": "all"}`

Add `since` when the person gave a period. Keep to about six calls.

### Step 3. Check every row's product

A product-code search can return records for other products of the same manufacturer (a QVO search returned two reSET recalls; reSET's authorization is in code PWE). For each row, state the product the record names and whether it is the person's product, a comparable, or another product. Drop nothing silently: list off-scope rows in one line.

### Step 4. Describe each record as stated

For each recall: date, firm, product as titled, the classification label as the source gives it ("Class II", a recall classification, not the device class), and the firm's stated reason in quotation marks. For MAUDE: reports per year for the product code, with the tool's own basis ("counts are reports, not confirmed events") and the note that a code count cannot be attributed to one product. For MHRA alerts: title, date, link. No cause, no rate, no comparison of safety between products (`references/safety-records.md`).

### Step 5. What it may mean for the pathway

Stated as questions for the owner, never as findings. For example: "A comparable's recall cites a software issue in reward logic; does our hazard analysis address the equivalent function?" Point the person's own reporting obligations to their vigilance owner with the clocks as context (EU 15, 10 and 2 days, VG4 to VG6; US 30 calendar days or 5 work days, VG17, VG18; GB as EU, VG28), never deciding whether anything is reportable.

### Step 6. Name what cannot be seen

Swiss field safety actions, EU vigilance, GB registrations, and any recall whose product text lacks a software term (the library loads only those). Absence is a gap, not a clean record.

## Build the output

Follow `assets/safety-review-output.md`. Answer first: what the records show, in one or two sentences, with the main limit. Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every record has date, source and retrieval date; reasons are quoted, not paraphrased.
- No causal claim, no rate, no safety ranking; MAUDE counts are labeled as reports.
- Each row's product is checked against the scope.
- Reportability and any regulator wording stop for the person's vigilance owner (named, or "owner not named").
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Public records only. The person's complaint handling, CAPA and vigilance decisions belong to the Quality pack (DH-03.02) and their vigilance owner.
- No statement about a competitor's safety for external use without the owner.
- Drugs, biologics and wellness apps are out of scope.
