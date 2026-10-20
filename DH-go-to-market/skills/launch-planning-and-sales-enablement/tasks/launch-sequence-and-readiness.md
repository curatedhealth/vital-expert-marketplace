# A1 Launch sequence and readiness

Framework task: DH-02.01.1.1, Part A, task A1. Folds in the earlier tool skills "Read the launch sequence", "Read launch readiness" and "Commercial brief". Catalogue jobs on the library: `launch-sequence`, `launch-readiness`, `commercial-brief` (see the formula table).

## What this task delivers

A dated answer to two questions: when did this product and its peers reach each market (authorization, listing), and which launch prerequisites the sourced rules set for the markets in scope, with the person's status against each. It is the evidence base the claim list (A2), the enablement plan (B1) and the sibling monitoring skill build on.

Why it matters: a launch plan that assumes a listing, a billing code or an NHS route without the prerequisites behind it fails at the first customer. A DiGA listing does not open the US; an FDA clearance does not make a product billable under G0552 unless its classification and the billing model fit (CP-US-58, CP-US-59); an NHS buyer reviews DTAC in procurement (CP-UK-01). The value is laying the prerequisites beside the dates, not the lookup.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.1 Part A, Launch sequence and readiness |
| Workflow | The steps below |
| Knowledge | `references/launch-prerequisites.md`; library records; `references/gap-rules.md` |
| Tools | `commercial-dh.list_commercial_dh_sources` (free), `market-access-dh.find_scheme_precedents`, `commercial-dh.get_launch_sequence`, `commercial-dh.get_launch_readiness` (optional, large), `commercial-dh.generate_commercial_brief` (optional attachment); `verify.build_record` when a named person clears the output |
| Prompt | This guide |
| Template | Library events for the data; `assets/launch-sequence-output.md` for the answer |
| Input | The request and its context: product and identifiers (FDA number, DiGA-ID), markets in scope, peers if the person has them, the person's status on each prerequisite, audience and depth |
| Governance | `references/governance.md` |
| Catalogue job | `launch-sequence`, `launch-readiness` and `commercial-brief` (one job per call: get_launch_sequence, get_launch_readiness, generate_commercial_brief); `scheme-precedents` for peer names. The direct calls in the steps remain the method; a job is the one-call option for the buyer. `examples/live/list_jobs_commercial.json` |

Arguments, return fields and observed pitfalls are in `references/tools.md`.

## Read the request

- **Product identity.** Name plus an identifier if there is one. For US products ask for or find the FDA submission number: the brand name does not reach the regulatory record (`references/tools.md`). For a US comparable, also read its classification regulation from the authorization record (regulatory-dh.get_authorization with the K number; K191716 returns 882.5801). Cite CP-US-63 against the person's product only when its regulation is known to fall outside 882.5801 and 882.5803; otherwise ask for the regulation and keep it as the first dependency.
- **Markets.** Keep to those named. If none, ask once; otherwise use the markets where the product already has a record and say so.
- **Peers.** Take the person's. If none, offer comparables from the same scheme and indication (step 2), labeled comparables.
- **Prerequisite status.** What the person can show or state for each prerequisite. Without it, list the prerequisites with status "not stated".
- **Short or full.** A direct question ("are we ready for Germany", "when did X launch") gets short mode. "Launch plan", "board", "full picture" gets full mode.

## Workflow

### Step 1. Know what the library can see (free)

Call `commercial-dh.list_commercial_dh_sources`. Note for each market in scope whether the library holds authorizations or listings and how fresh they are. UK device registrations and Swiss records are not loaded; EU decision dates are empty. Every later gap is judged against this.

### Step 2. Get exact names for the product and peers

Call `market-access-dh.find_scheme_precedents` with the scheme and an indication code or source-language term (`{scheme: "DE_DIGA", indication: "F32"}`), limit 10. Use the stored product names and identifiers for step 3. Pick peers the person named, or up to five comparables in the same indication, labeled comparables. Describe each only by what its record states.

### Step 3. Read the sequence

Call `commercial-dh.get_launch_sequence` with `reference` (FDA number for US products, otherwise the stored name), `peers` (exact stored names, up to 10), and `route_hypothesis` only if the person gave a Swiss route. Then:
- Separate merged products by the identifier in `source_url`.
- Write any peer that returned nothing as "not found under this name `[GAP]`".
- For a `changed_on` that differs from `listed_on`, report the date and source and "status after the change not stated `[GAP]`".
- Order events by date per market. A peer's earlier listing shows a route exists for this kind of product, not that this product would follow it.

### Step 4. Lay out the prerequisites

From `references/launch-prerequisites.md`, list the prerequisites for each market in scope with their rows. Mark each with the person's status: shown, stated, not stated. Never mark one met on your own reading. Where a billing channel is part of the plan (DMHT, RPM, DiGA), list its conditions as prerequisites and say that payment amounts belong to Market Access.

### Step 5. The connector's readiness count, only if useful

Call `commercial-dh.get_launch_readiness` only if the person asks for the connector's checklist or wants the money-flow roles recorded, and only after telling them the response is large. Pass `user`, `buyer` and `payer` as three roles the person named, and `segment` as one of cdss, digital-health, dtx, rpm, samd-diagnostic. Report `met_count` and the seven criteria as the connector's count, with the pitfalls from `references/tools.md`. Do not send unreleased claims in this call without the person's say (it audits them).

### Step 6. Sequence by dependency

Write which prerequisite blocks which ("EUDAMED actor registration before placing on the market, CP-EU-10"; "BAA before PHI flows, CP-US-46"). No dates of your own and no urgency. Clocks in the rows are facts, stated with their instrument.

### Step 7. Gaps

Classify every gap with `references/gap-rules.md`: library coverage, a name not found, a field not stored, a market not in the research, a status the person did not state.

## Build the output

Follow `assets/launch-sequence-output.md`, short or full. If the person wants the connector's dossier attached, call `commercial-dh.generate_commercial_brief` with the same arguments and attach it, labeled "connector dossier, raw"; it is never the answer (`references/tools.md`).

## Before you hand it over

- Every date carries its `source_url` and retrieval date, and the line "library copy of the register; confirm on the authority's page before external use".
- Every prerequisite carries a row; every status is the person's.
- No "ready to launch" statement; the connector's count is labeled as a count.
- Short mode counted and under 450 words.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Payer prices, coverage decisions and contracts: Market Access.
- Whether the product is a device and its class: the person's regulatory owner and the Regulatory pack.
- A competitor's launch dates say nothing about its uptake, revenue or success.
- Drugs and biologics are out of scope; a wellness app is in scope only to check that its launch claims keep it a wellness product (PC-US-63).
