# A1 QMS scope and process map

Framework task: DH-03.02.3.1, Part A, task A1. Replaces the earlier "QMS scope" section.

## What this task delivers

A scope statement and a process map for the quality management system of a regulated digital health product: which products, sites and markets it covers, which requirement set applies in each market, and, for each process, the sourced requirement it answers (QMSR and ISO 13485 as FDA restates them, MDR Article 10(9) elements, Article 15 for the PRRC, MDSAP chapters where multi-region). It answers "what does our QMS have to cover, and why each process is there?"

Why it matters: since 2 February 2026 FDA inspects against the QMSR through six QMS areas and four other requirements (QS28, QS30, BX3, BX4), and the MDR asks for at least thirteen elements (EU3, BX1, BX2). A map that ties each process to its source shows gaps before an investigator or notified body does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.1 Part A, QMS scope and process map |
| Workflow | The steps below |
| Knowledge | `references/process-map-requirements.md` (built on `quality-systems-research.md`, `qms-requirements-additions.md`, `multi-region-research.md`) |
| Tools | `regulatory-dh.list_jurisdictions` (free), `regulatory-dh.search_safety_events` (optional, comparables) |
| Prompt | This guide |
| Template | `assets/scope-and-process-map-output.md` |
| Input | The request and its context: products and versions, sites and outsourced parties, target markets, device class per market as the person states it, existing procedures if any |
| Governance | `references/governance.md` |

## Read the request

- **Products and versions.** Named products only. A QMS is never claimed for a product the scope does not name.
- **Markets and class per market.** Ask for both. Class is the person's regulatory owner's call; if unknown, mark `[GAP]` and do not choose the requirement set for that market.
- **Sites and outsourcing.** Development, hosting, complaint intake, distribution: who does each.
- **Existing system.** If the person has procedures, map theirs to the sources; do not replace their names.
- **Mode.** A direct question ("what does our QMS need for US and EU?") gets short mode. A document for a QMS kickoff or a gap review gets full mode.

## Workflow

### Step 1. Fix the scope facts

Write back, in one table, the products, sites, outsourced parties, markets and the class per market the person gave. Mark each missing item `[GAP]` and ask once for all of them together.

### Step 2. Pick the requirement set per market

From section 1 of `references/process-map-requirements.md`, list the requirement set for each market with its row ids. Say plainly where the research does not hold a market's QMS requirement (for example GB) and route it to the regulatory owner.

Points that change the scope and must be stated when they apply:

- US design controls apply to class II, III and class I devices automated with software (QS9). For software products this usually means design controls apply; state it as the row says, against the class the person gave.
- A CGMP exemption by classification still requires complaint files (QS14).
- The QMSR has applied since 2 February 2026 with no phase-in (QS1, QS2). FDA may still review records made before then (QS26).
- An ISO 13485 certificate does not replace an FDA inspection (QS25).
- EU: the QMS is proportionate to risk class and type of device and covers all quality-relevant parts of the organization (EU1, BX1).
- EU: at least one PRRC, or one permanently at the disposal of a micro or small enterprise (EU8, EU9).

### Step 3. Build the process map

Start from the process skeleton P1 to P16 in section 2 of `references/process-map-requirements.md`. For each process write: the person's process name (or the skeleton name if they have none), the US basis, the EU basis, the MDSAP chapter where QS43 names one, and the row ids. Rules:

- Clause numbers come only from FDA's CP 7382.850 tables (BX6 to BX12). Never write clause text.
- Keep a cell `[GAP]` where the reference has one. Do not fill MDSAP chapter cells by inference.
- Mark processes the person outsources (P8 applies to them; VG11 says outsourced complaint handlers count for the EU awareness date).
- A process the person runs that no row supports stays on the map as "the person's process, no regulatory row".
- Non-applicable cells (for example sterile product validation for software) are marked "not applicable, per the person", not deleted.

### Step 4. Name what is missing

Compare the person's existing procedures (if given) with the map. List each map process with no procedure. This is a coverage gap in the design, not a compliance finding; say so.

### Step 5. Comparables (optional, when the person asks what goes wrong)

Call `regulatory-dh.list_jurisdictions` (free) to see which markets have safety events loaded. Then call `regulatory-dh.search_safety_events` with a manufacturer or product the person names as comparable, `since` a date they choose, `limit` 5 to 10. Read `references/tools.md` first: the `product_code` filter did not restrict recalls in live tests, and recall source URLs point to the API endpoint, not the record.

Report each event only by what its record states (title, date, class, summary). Then say which process on the map the stated problem touches (for example "summary says a software issue after an update: change control P10 and release P9"). That link is a reading of the summary, labeled "process touched, per the summary"; never a root cause.

### Step 6. Say what it means for the person

Two or three consequences, from the rows only. Examples: "Because management review and audit reports are inspectable since 2 February 2026 (QS15), P2 and P14 records need to be written for an investigator." "Because Canada ties MDSAP certification to Class II to IV licenses (MR-05), adding Canada changes the audit model; that is a B1 decision."

## Build the output

Follow `assets/scope-and-process-map-output.md`. Answer first: the requirement set per market and the processes with no procedure yet. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections, then table rows that the person's facts do not touch (list them by P number in one line); count every table cell except the Rows column; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every requirement cell has a row id or `[GAP]`.
- No clause text from ISO 13485, ISO 14971 or IEC 62304.
- No device class chosen by the model.
- No statement that the QMS is compliant, effective or ready for inspection; the map is a design draft.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Scope and map only. Owners and cadence are A2; the operating model choice is B1.
- No classification, no conformity route, no notified body choice: those are the regulatory owner's.
- Drugs, biologics and wellness apps are out of scope.
