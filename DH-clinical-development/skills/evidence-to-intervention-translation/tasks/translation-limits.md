# B1 Translation limits

Framework task: DH-01.01.4.1, Part B, task B1. Replaces the earlier "Translation limit" section (DH-01.01.4.1.3).

## What this task delivers

A limits draft: for each place where the product would reach beyond its evidence (a population, age range, dose, duration, outcome, setting or use as standalone therapy the source does not cover), the fact that sets the edge, the product behavior that stays off because of it, and who may reopen the limit and on what evidence. The person sets every limit and names every owner; the model lays out the edges the sources draw and the criteria a decision would weigh.

Why it matters: regulators write these edges into indications. reSET was "not demonstrated to be effective" in primary opioid users after a subgroup showed no benefit (TM138); EndeavorRx's indication says patients "may not display benefits in typical behavioral symptoms, such as hyperactivity" (TM144). A product team that writes its own limits before launch keeps features, text and claims inside them.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.1 Part B, Translation limits |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/translation-limit-rules.md`; rows TM107 to TM113, TM122, TM128, TM132, TM137, TM138, TM144, TM19, TM20, PC-US-23, PC-US-27, PL59, PL75, PL95, ES-91, ES-96 |
| Tools | A1's tools if the claim map is missing; `regulatory-dh.get_authorization` and `regulatory-dh.search_safety_events` for a named precedent |
| Prompt | This guide |
| Template | `assets/translation-limits-output.md` |
| Input | The request and its context; the A1 map and the A2 specification; the expansion the person is considering; the owners they name |
| Governance | `references/governance.md`; people set limits and name who may reopen them |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person sets each limit, the behavior that stays off and the owner who may reopen it, in their own words. The model finds where the product reaches beyond the source and lays out the criteria a decision would weigh. It never decides that a limit may be lifted, never lifts one because a stakeholder asked (old DH-01.01.4.1.3 rule), and never names an owner the person has not named. Any proposed limit is labeled "proposed".

## Workflow

### Step 1. Find the edges

Compare, row by row, the A2 specification and the A1 claims with each source's population, dose, duration, comparator, outcome and setting. List every place the product goes further. Typical edges: an age band outside the trial's; patients the trial excluded (for example medicated patients when the trial enrolled unmedicated ones); a longer or shorter dose than tested; an outcome the trial did not measure or a subgroup that did not benefit (TM138, TM144); standalone use where the source tested an adjunct (TM119, TM122, TM132).

### Step 2. State the fact behind each edge

For each edge, quote the passage that sets it, with locator and row. Distinguish three kinds: **shown not to help** (a subgroup or outcome with no benefit, TM138), **not studied** (outside the inclusion criteria), and **stated as a limitation** in an indication or label (TM144). Not studied is not the same as shown not to help; say which.

### Step 3. Lay out the decision criteria

If the person is considering going past an edge, lay out the evidence-to-decision criteria the GRADE Working Group frameworks share (TM110, DOI 10.1186/s12961-018-0320-2): priority of the problem, desirable and undesirable effects, certainty of the evidence, values, balance, cost-effectiveness, acceptability and feasibility, with the questions in TM111 and the equity question. Certainty is per outcome (ES-96) and indirectness is a reason to rate down (ES-91): applying evidence to a different population is that question. Each criterion gets the facts held or `[GAP]`; the judgment column stays empty for the person. Alonso-Coello 2016 (TM107, TM108) was read through WebFetch only: say so if used.

### Step 4. Name the behavior that stays off

For each limit, write the product behavior that stays off because of it (a feature, a rule branch, an onboarding path, a claim or a message), labeled "proposed" until the person confirms. Link it to the A2 rule or the A1 claim it constrains.

### Step 5. Name who may reopen, and on what

Ask the person who may reopen each limit and what evidence would be needed. Facts that bear on reopening: a new population or indication may change the definition statement and its category (PL59); a module-level change may need re-confirmation of clinical performance only for that module, while a change that alters indications needs whole-product evaluation (PL75); for a DiGA, a change in the patient group is a significant change (PL95); for a US authorized product, communications that change indication, population or regimen are inconsistent with labeling (PC-US-23, PC-US-27). Which of these applies is a question for the owner the person names for regulatory status, or owner not named.

### Step 6. Check precedents where useful

For a named authorized product the person cites, call `regulatory-dh.get_authorization {reference}` for dates and regulation, and `regulatory-dh.search_safety_events {product_code}` for recalls and report counts. When the events or the person name a sibling product under the same product code (for example reSET-O under PWE), read it with `regulatory-dh.search_devices {query}` or `get_authorization` before marking it [GAP], and state its pathway, number and date as precedent facts only; whether it applies is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question. Describe the precedent, and any recall or event, only by what its record states; do not judge its relevance to the person's product.

## Build the output

Follow `assets/translation-limits-output.md`. Short mode for a direct question: the limits found, each with its fact, the behavior that stays off and the owner the person named, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every limit cites the passage that sets it; "not studied" and "shown not to help" are kept apart.
- No limit is lifted, and no expansion is called supported, by the model.
- Every owner is the person's; "owner not named" where they named none.
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Whether an expansion needs a new submission or a DiGA change notice: `dh-regulatory-and-quality` regulatory-submission-and-dossier; a PCCP: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control; device status: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Designing the study that would reopen a limit: `dh-clinical-development` study-protocol-and-endpoint-design.
- Recording a limit as a design input and controlling its change: `dh-regulatory-and-quality` design-controls-and-risk-management and document-and-change-control.
- Portfolio decisions about which expansion to fund: `dh-cross-functional-leadership` (old pack), heading DH-01.03.3 Governance & Portfolio.
