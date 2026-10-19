# A2 Pathway precedents

Framework task: DH-03.03.3.1, Part A, task A2. Replaces the earlier "Read pathway precedents", "Find predicates", "Search devices", "Open an authorization", "Compare authorizations" and "Read market status" sections.

## What this task delivers

The comparable devices the public registers hold, the route each took and how long it took between its stored dates, where each is authorized, and, for the US, the substantial-equivalence predicate candidates with their chains. Every device is described only by what its record states. It answers "what did products like ours do, and is there a predicate?"

Why it matters: in the US the existence of a predicate decides between a 510(k) and a De Novo, which differ in fee, clock and evidence (`pathway-facts.md`). Elsewhere, comparables show which class and route the market has already used. Precedent is the cheapest evidence a strategy can have, and the easiest to overstate.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.1 Part A, Pathway precedents |
| Workflow | The steps below |
| Knowledge | `references/pathway-facts.md` (observed FDA totals for context); `references/gap-rules.md` |
| Tools | `regulatory-dh.list_jurisdictions` (free), `search_devices`, `find_predicates`, `get_pathway_precedents`, `get_authorization`, `compare_authorizations`, `get_market_status` |
| Prompt | This guide |
| Template | `assets/pathway-precedents-output.md` |
| Input | The request and its context: the A1 intended use (or the person's description), known competitors, a product code or EMDN code if known, target jurisdictions |
| Governance | `references/governance.md`; substantial equivalence is FDA's determination |

## Read the request

- **What to compare against.** Named competitors or manufacturers; a product code (FDA) or EMDN code (EU); or only a description. The library searches by name and by code, not by intended use, so a description alone needs a first name or code. Ask for known competitors if none are given.
- **Jurisdictions.** Default US and EU (the two the library holds with authorizations); say UK and CH are not loaded.
- **Mode.** A direct question ("is there a predicate for a CBT-I app?") gets short mode.

## Workflow

Keep to about 10 counted calls for one product. Save each output; the example run used 12.

### Step 1. Know what the library can see

Call `regulatory-dh.list_jurisdictions` (free). Note per target jurisdiction whether authorizations are loaded and the last load date. UK registrations and Swiss devices are not loaded: say so once and move on (`gap-rules.md`).

### Step 2. Find the first comparables

Call `regulatory-dh.search_devices` with each named competitor or manufacturer (`{"query": "Big Health", "jurisdiction": "all"}`). Keep rows whose stored product code, regulation number or name the person confirms as comparable. Do not decide comparability from a name: ask, or show the stored fields and let the person judge.

### Step 3. Widen through the code

With the product code from the comparables (or from A1), call:
- `regulatory-dh.find_predicates` with `{"product_code": "QVO"}`: recent decisions in the code with their stated predicates.
- `regulatory-dh.get_pathway_precedents` with `{"product_code": "QVO", "jurisdiction": "US"}`: counts by pathway and year, De Novo grants, and calendar days between stored submission and decision dates.

If the code shows no De Novo, follow the chain (Step 4): the founding De Novo can sit under another code (QVO's chain starts at DEN160018 in code PWE). For the EU, `get_pathway_precedents` with an EMDN code returns a count without dates; report it as the size of the code, not as a set of comparables.

### Step 4. Predicate candidates (US)

For each candidate, call `regulatory-dh.find_predicates` with `{"reference": "K191716"}` to read the chain as FDA summaries state it. Describe each candidate only by its record: device, applicant, pathway, decision date, product code, regulation number, the predicate it named, and the summary URL. State the substantial-equivalence test the owner will apply (same intended use; same or different technology that raises no different questions, RP US-06), and which of those facts the records can and cannot show: the records show code and chain, not intended use wording or technology. Those come from the summary PDFs, which the owner reads.

Never write "X is a valid predicate" or "substantially equivalent". Write "candidate predicate: same product code and regulation number per the record; intended use and technology to be compared by the owner from the summary at URL".

### Step 5. Authorization details and comparison

- `regulatory-dh.get_authorization` for any reference the person asks about or whose fields are needed.
- `regulatory-dh.compare_authorizations` with 2 to 12 references for a side-by-side table. A "not assessable" safety count is not zero.
- `regulatory-dh.get_market_status` with the `reference` (a name can miss a product with a trademark sign, and can return two rows for one product) to show where each comparable is authorized.

### Step 6. Put timing in context

For each precedent with both dates, report calendar days from submission to decision and n. Beside them, give the published FDA averages for the same route as context (510(k) about 141 total days; De Novo 247 to 278 total days, FY 2023 to FY 2025, RP US-58, RP US-61), and the MDUFA goal in FDA days, with the warning that FDA days exclude sponsor time and are not comparable to calendar days (RP "Changes and conflicts"). Two precedents are not a forecast for the person's product.

## Build the output

Follow `assets/pathway-precedents-output.md`. Answer first: is there a US predicate candidate, which route did comparables take, and where are they authorized. Short mode: 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every device fact has its source URL and retrieval date; nothing about a device goes beyond its record.
- No predicate is called valid or equivalent; the owner reads the summaries.
- Calendar days and FDA days are never mixed; n is stated.
- Gaps are classified (`gap-rules.md`); UK and CH are named as not loaded.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Precedents and predicate candidates only. Classification arguments are A1; choosing the route is B1; monitoring a comparable's later changes or safety events is the pathway monitoring skill.
- Reimbursement status is the Market Access pack's work.
- Drugs, biologics and wellness apps are out of scope.
