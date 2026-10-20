# A1 Mechanism statement

Framework task: DH-01.01.2.1, Part A, task A1. Replaces the earlier "Mechanism statement" section (DH-01.01.2.1.1, register CF-12.01.01.2.1.1). Also covers the earlier "Mechanism-of-Action Specification" task (DH-01.06.2.1.1, register CF-12.01.06.2.1.1, old worker `behavior-change-designer`), folded in on 20 October 2026; the method below is unchanged.

## What this task delivers

A mechanism written as a chain of links (component, user action, change, outcome), with the population it is expected to hold in and one it is not expected to hold in, each link labeled as a hypothesis, each tied to its source or marked `[GAP]`. Where the person names a therapy model or a precedent, what that model's evidence or that precedent's record states, read from the source.

Why it matters: a feature list cannot be tested; a chain of links can. The US classifications for computerized behavioral therapy ask for a validated model of therapy and its validation "as implemented by the device" (TM120), and the DiGAV asks that the claimed effect be consistent with the product's functions and content (TM148). Both start from a written mechanism.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.1 Part A, Mechanism statement |
| Workflow | The steps below |
| Knowledge | `references/mechanism-rules.md`; `references/precedents.md`; rows TM4 to TM10, TM23, TM40 to TM44, TM80 to TM84, TM87, TM119 to TM130, TM145 to TM150 |
| Tools | `regulatory-dh.get_authorization` for a named precedent; `literature.search_literature` and `literature.get_record` for the therapy model's evidence; `verify.qualify_source` then `verify.check_claim` for any sentence about that evidence |
| Prompt | This guide |
| Template | `assets/mechanism-statement-output.md` |
| Input | The request and its context: product, intended use as the person states it, condition, population, therapy model drawn on, feature list, any precedent the person names |
| Governance | `references/governance.md`; the person chooses the mechanism, population and exclusions |
| Catalogue job | none (`find_job` returned no match); `evidence-table` (available) only if the person wants the therapy model's studies graded |

## Read the request

- **Outcome.** What clinical outcome is the product for? That is the distal outcome (TM83). If the person gives only features, ask for the outcome first: the chain is built backward from it.
- **Therapy model.** Which model does the product draw on (for example a CBT variant), in the person's words? Where does its content come from (DiGAV § 2 asks for these sources, TM149)?
- **Population.** For whom, and is there a group the person already expects it not to help?
- **Precedent.** Did the person name a product to compare with? Use its record only.
- **Disclosure.** Ask before sending unpublished product names or design text to the library (`references/governance.md`).

## Workflow

### Step 1. Write the outcome and work backward

Write the distal outcome in the person's words. For each feature the person lists, ask which change it is meant to produce and which user action carries it. Build one chain per mechanism; a product may have more than one (TM10). A feature with no place in any chain is noted for A2 ("not tied to a link").

### Step 2. Name each link with the sources' terms

Fill the chain table in `references/mechanism-rules.md` section 2: component, user action (engagement proximal outcome, TM87), change (mediator, TM84; COM-B subcomponent where a behavior is targeted, TM44), outcome (TM83). Write each link as "expected to". Where the mechanism is not behavioral, say COM-B does not apply and use the person's model (mechanism-rules section 3).

### Step 3. For whom and not for whom

State the population (context, TM9; tailoring variables if the product adapts, TM80). Name one population where a link is not expected to hold and why, from the person's facts or a precedent's labeled limitation. If neither exists, write `[GAP]` and carry it into B1 as an assumption.

### Step 4. Check the therapy model's evidence (when the person names one)

Call `literature.search_literature` with the model, the delivery mode and the condition, for example `{query: "internet-delivered <model> <condition> randomized trial", limit: 6, filters: {designs: ["rct"]}}`. Screen by the person's question; drop off-topic records. For each paper you will mention, take the sentence from its abstract or full text (Europe PMC), call `verify.qualify_source {doi, question}`, then `verify.check_claim` with the claim, the passage `{text, locator}` and the full qualify_source object. Accept only when you have read the passage and it says the same thing (N3). Describe what the paper states about its own population; never transfer it to the person's product. A graded review is `dh-clinical-development` literature-and-real-world-evidence-review's work; point there.

### Step 5. Set beside a precedent (when the person names one)

Call `regulatory-dh.get_authorization {reference: "<DEN or K number>"}` to confirm identity, date and regulation. Take the mechanism facts from `references/precedents.md` (TM rows). Show only what the record states: for reSET, the CRA model, the lesson structure and the labeled opioid-user limitation (TM133, TM134, TM138); for EndeavorRx, the adaptive closed loop and the isolating control (TM142, TM143). If the precedent is not in `precedents.md`, say its decision summary was not read `[GAP]`.

### Step 6. Mechanism-level texts as context

If the person asks what US classifications or the DiGAV say about mechanisms, give the rows in mechanism-rules section 4, with the "model of therapy" versus "validated measure" difference (TM119 to TM130). Whether any applies to their product: `dh-regulatory-and-quality` regulatory-pathway-and-classification, owner the person names for regulatory status, or owner not named.

### Step 7. Check the structure (optional, with code execution)

Write the chain as JSON in the shape of `evals/files/mechanism_map_illustrative.json` and run `python3 scripts/mechanism_map_check.py MAP.json`. It lists links without a measure, features not tied to a link and missing exclusions. Its marks are structure checks, not findings about the mechanism.

## Build the output

Follow `assets/mechanism-statement-output.md`. Answer first: the chain in one line, the population and exclusion, the biggest gap. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every link says "expected to"; nothing is called validated, proven or evidence-based beyond a passage read in the same direction.
- No feature list stands in for the mechanism.
- Precedents are described only by their records, with the row or call.
- Abstract-only and [WF] rows are labeled where applied.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Whether the mechanism happened in data: mechanism validation monitoring (DH-01.01.2.2).
- Turning a guideline or trial result into product rules: `dh-clinical-development` evidence-to-intervention-translation.
- Device status and whether a classification applies: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Recording the mechanism as a design input: `dh-regulatory-and-quality` design-controls-and-risk-management.
