# A1 Lifecycle stage map

Framework task: DH-01.01.1.1, Part A, task A1. Replaces the earlier "Lifecycle stage" section (DH-01.01.1.1.1).

## What this task delivers

The stage the product is in, in the person's stage model and mapped to a sourced vocabulary; the work products that stage owes, each with the row that names it; what is present and what is missing from what the person shared; the stage it blocks. Where the person names a comparable product, a dated timeline of that product's authorizations and safety events from the register, described only by what the records state.

Why it matters: a product that runs a regulated release while its intended use is still a concept (the old rule) builds evidence for a claim nobody fixed. The sources make the same point from both sides: repeat a phase rather than progress automatically while uncertainties remain (TM3), and recategorize when the definition statement changes (PL59).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.1 Part A, Lifecycle stage map |
| Workflow | The steps below |
| Knowledge | `references/lifecycle-stages.md`; rows TM2 to TM7, TM13 to TM15, PL5, PL7, PL9, PL10, PL58 to PL65, PL110 to PL117, PL122 to PL124, QS9, QS23, QS24 (TM rows DOI 10.1136/bmj.n2061; PL110 to PL120 DOI 10.1097/SLA.0000000000004907) |
| Tools | For a named comparable product only: `regulatory-dh.search_devices`, `regulatory-dh.get_authorization`, `regulatory-dh.find_predicates`, `regulatory-dh.search_safety_events`; `scripts/lifecycle_timeline.py` |
| Prompt | This guide |
| Template | `assets/lifecycle-stage-output.md` |
| Input | The request and its context: product, intended use as stated, the person's stage model and current stage, work products held (ids, versions), markets, any comparable product named |
| Governance | `references/governance.md`; the person names the stage model and decides the stage |
| Catalogue job | none (`find_job {query: "product lifecycle stage gate"}` returned no match, 20 October 2026) |

## Read the request

- **Stage model.** Which stages does the person's organization use? Take their names verbatim. If none, say "Stage model not stated `[GAP]`" and offer the vocabularies in `references/lifecycle-stages.md` section 1 as "proposed".
- **Intended use.** Stated, drafted or unknown? The stage map ties every owed item to it (PL58).
- **Work products held.** Ids, versions, dates. A status word without a work product does not count.
- **Comparable product.** A named product (for example EndeavorRx, reSET) the person wants to learn from. Ask before sending the person's own unpublished product name to the library.
- **Device status.** If unknown, `[GAP]` and route; this task does not decide it.

## Workflow

### Step 1. Place the product in the person's stage

Write the person's stage name and map it to the closest sourced vocabulary (MRC/NIHR phase, QMSR decision point, IDEAL-D stage 0, post-market). Say which vocabulary. If the person's facts fit two stages, say so and name the fact that decides it; the person chooses.

### Step 2. List what the stage owes

From `references/lifecycle-stages.md` section 3, list the work products a source names for this stage and this product type, each with its row. Add the MRC/NIHR core element questions where the product is a complex intervention (TM4, TM5), labeled "proposed" for device gates. Mark each: present (with the person's reference), missing, or not known `[GAP]`.

### Step 3. Name what the stage blocks

Name the next stage and the owed item that blocks it, by dependency (for example: no definition statement blocks a clinical evaluation plan, PL58, PL62; no predefined progression criteria blocks a feasibility exit, TM14). Never advance by date.

### Step 4. Comparable product timeline (only if one is named)

1. `regulatory-dh.search_devices {query: "<product or maker>", jurisdiction: "US"}` (or `all`).
2. `regulatory-dh.get_authorization {reference: "<DEN, K or P number>"}` for the first authorization.
3. `regulatory-dh.find_predicates {reference}` or `{product_code}` where later clearances matter.
4. `regulatory-dh.search_safety_events {product}` or `{product_code}`.
5. Save the outputs and run `python3 scripts/lifecycle_timeline.py FILE.json --product <name>`.

Report the dated sequence, days from submission to decision where both dates are stored, days between decisions, predicates as stored, and MAUDE counts labeled "reports, not confirmed events". Never state why a later submission was made, whether the product is still marketed, or what it means for the person's timeline. Regulation numbers (for example 882.5801, 882.5803) are context for design; whether the person's product falls under one is a question for `dh-regulatory-and-quality` regulatory-pathway-and-classification (pack rule 4).

### Step 5. What the person must decide

List the decisions this map surfaces (which stage model, whether to repeat a phase, which owed items they require) with the fact behind each. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/lifecycle-stage-output.md`. Answer first: the stage, the item it owes that blocks the next stage, and what that blocks. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The stage is the person's; the vocabulary it maps to is named.
- Every owed item carries its row; [WF], abstract-only and draft rows are labeled.
- A comparable product is described only by its records, with reference numbers and retrieval dates.
- No stage is called complete and no product ready.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Whether the product is a device and its pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification; catalogue jobs `pathway-assessment` and `predicate-chain` sit there.
- The content of design control and risk records: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Stage health over time: `lifecycle-quality-monitoring` (this pack).
