# A2 Post-market change and performance tracking

Framework task: DH-03.03.1.2, Part A, task A2. New task in the rebuilt competency; it covers the monitoring half that the earlier "approval readiness monitoring" left out.

## What this task delivers

Three tables for an authorized AI device: the person's logged model changes sorted against the authorized PCCP (or against the general software-change questions where there is no PCCP); the performance monitoring expectations with whether a plan, data and owner exist for each; and the safety events the library holds for the product and for comparable devices, filtered by hand to the ones that are actually about them. It answers "what have we changed, are we watching what we should, and what has happened to us and to devices like ours?"

Why it matters: a change that drifts outside the authorized plan would generally make the device adulterated and misbranded [AI US-13]; a model that degrades in use is the risk the change plan exists to manage [AI US-31, US-36]. And comparable devices' recalls are early warning. The library's safety search returns off-target recalls for a product code, so the filtering step is where this task earns its keep.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.2 Part A, Post-market change and performance tracking |
| Workflow | The steps below |
| Knowledge | `references/post-market-expectations.md`; the authorized PCCP (the person's); `references/AI_ML_REGULATION.md`; `references/QUALITY_SYSTEMS.md` |
| Tools | `regulatory-dh.list_jurisdictions`, `search_devices`, `search_safety_events`; `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/post-market-tracking-output.md` |
| Input | The request and its context: product and identifiers, authorized PCCP (or none), change log, monitoring plan and data, comparable devices or product code, period |
| Governance | `references/governance.md`; coverage and reportability decisions are the owner's |

## Read the request

- **Which of the three tables.** "Was this retrain covered" is table 1 only. "Any recalls for similar devices" is table 3 only. "Post-market review" is all three.
- **Authorization facts.** K, DEN or P number, or Basic UDI-DI; the PCCP's listed changes and protocol steps. If the person has no PCCP, table 1 uses the 2017 software-change questions.
- **Period.** "Since" date for changes and events. Default: since the authorization date.

## Workflow

### Step 1. Sort the change log (table 1)

For each change the person logged, read the PCCP's Description of Modifications and Modification Protocol and write one of the sort values in `references/post-market-expectations.md` section 1. Check presence of each protocol step's evidence (data, testing against the person's acceptance criteria, labeling update, documentation in the quality system [AI US-12]). Do not judge whether criteria were met beyond comparing the person's recorded result to the person's recorded criterion; state both numbers. For changes outside the PCCP, list which of the 2017 questions the change touches [Q CH11 to CH16]; the owner decides. For EU devices, add the pre-determined change status [AI EU-05, EU-30].

### Step 2. Check monitoring expectations (table 2)

Take section 3 of `references/post-market-expectations.md`. For each expectation that applies to the person's jurisdictions, mark: plan named, data flowing, owner named, each yes, no or not assessable. Mark draft or final status beside each. Thresholds and drift limits are the person's.

### Step 3. Search safety events (table 3)

1. Call `regulatory-dh.list_jurisdictions` (free) to see which jurisdictions hold events (US and UK on 19 October 2026; EU and CH none).
2. For the product: `regulatory-dh.search_safety_events` with `manufacturer` (short form, for example "Aidoc") and with `product` (for example "BriefCase"), `since` set to the period start, `limit` 25.
3. For comparables: identify comparable devices with `regulatory-dh.search_devices` (by competitor name) or take the person's list; then `search_safety_events` with each comparable's `manufacturer`. A `product_code` search returns MAUDE counts for that code, but its recalls are not filtered to the code (`references/tools.md`).
4. Filter by hand: keep a recall only if its title or summary names the product or a comparable device. Report the excluded count as "returned, not about these devices".
5. MAUDE counts: report per product code with "reports, not confirmed events", and never attribute them to one manufacturer.

### Step 4. Put clocks beside any event the person is handling

If the person mentions an incident, state the clocks that apply in their jurisdictions [Q VG4 to VG6, VG12, VG17, VG18, VG22, VG28] and that reportability is the owner's decision. Do not decide it.

## Build the output

Follow `assets/post-market-tracking-output.md`. Short mode: the answer, the one table the question needs, at most three open items, the record line. Full mode: all three tables, the calls list, excluded results, sources.

## Before you hand it over

- No change is called "covered" or "compliant"; sorting is "as described, owner to confirm".
- Every safety row kept names the device it is about; off-target rows are excluded and counted.
- No empty result is read as safety; no MAUDE count is read as confirmed events or attributed to a company.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- Reportability, field actions and corrections are the owner's decisions (and the quality pack's process).
- Model performance analysis on the person's data (drift statistics) belongs to the data science pack; this task checks that monitoring exists and reads the person's recorded results against the person's recorded criteria.
- No forecast of future events.
