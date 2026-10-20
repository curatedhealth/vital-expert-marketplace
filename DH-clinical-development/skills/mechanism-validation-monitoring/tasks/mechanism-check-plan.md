# A1 Mechanism check plan

Framework task: DH-01.01.2.2, Part A, task A1. Replaces the earlier "Mechanism check" section (DH-01.01.2.2.1, register CF-12.01.01.2.2.1).

## What this task delivers

A check plan, written before any data are read: for each link of the mechanism (delivered, used, changed, outcome, and the population it should hold in), the measure that counts as evidence the link happened, its denominator and time point, any proxy the person names in advance, and the threshold the person sets. Links that cannot be measured yet are marked `[GAP]` and are not scored later.

Why it matters: engagement data arrive first and are easy to read as success. Implementation outcomes are preconditions for clinical outcomes (CS32), and use of the app is not proof of the outcome (old task rule). A plan set in advance stops the target from moving after the data are in (TM57).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.2 Part A, Mechanism check plan |
| Workflow | The steps below |
| Knowledge | `references/check-plan-rules.md`; rows TM57, TM83, TM84, TM87 to TM89, TM92 to TM105, TM117, TM118; CS25, CS27, CS29, CS32, CS37, CS39 |
| Tools | `literature.search_literature`, `verify.qualify_source` and `verify.check_claim` only when the person wants a measure a published study used; `scripts/link_check.py` reads the plan |
| Prompt | This guide |
| Template | `assets/mechanism-check-plan-output.md` |
| Input | The request and its context: the mechanism chain and components (design skill A1 and A2, or the person's documents), the version, the data the product and study collect |
| Governance | `references/governance.md`; the person sets measures, proxies and thresholds |
| Catalogue job | none |

## Read the request

- **Chain.** Is there a written mechanism? If not, ask for it or point to therapeutic mechanism and intervention design A1; a plan needs links.
- **Version and cohort.** Which version, which study or live cohort, which data cut? Any not given is written "not given" and asked; the model never supplies one.
- **Data held.** What does the product log, what does the study collect, and what does neither collect?
- **Has anyone looked yet?** If the data were already read, say measures chosen now are labeled "set after the data were read" and are reported as exploratory, never scored.

## Workflow

### Step 1. Lay out the links in reading order

Write the links as delivered, used, changed, outcome, plus population (check-plan-rules section 1). Delivery comes first because a downstream miss is uninterpretable without it (CS32). Pull the essential components and their fixed functions from the design skill (TM105, TM117).

### Step 2. Name the measure per link

For each link, the measure that counts as evidence it happened, from data the person has:
- Delivered: fidelity (adherence: content, frequency, duration, coverage, TM102), dose (TM92), reach on a valid denominator (TM94, CS27). Name the fidelity framework used (research file "Changes and conflicts" 3).
- Used: engagement proximal outcome (TM87; RE-AIM individual implementation, CS25).
- Changed: the mediator and its instrument, at a named time point (TM84).
- Outcome: the distal outcome and its instrument (TM83).
- Population: the subgroups the person wants to see (TM9, TM96).
Write the person's measure, verbatim. Do not supply an instrument.

### Step 3. Denominator, time point, aggregation

For each measure, write the denominator (eligible, enrolled, active; CS27, CS39), the time point and how values combine (mean, proportion reaching a cut, change from baseline). These are the person's; where missing, list them as open.

### Step 4. Proxies, named now or never

If a link has no direct measure, ask whether the person names a proxy now. A named proxy is labeled as one. A link with no measure and no named proxy is `[GAP]`: not measurable yet, and A2 will not score it (old task rule).

### Step 5. Thresholds, set now

Ask the person for the threshold that counts as "met" for each link, on clinical significance, before the data are read (TM57, TM118). If they have none, the plan records the measure without a threshold, and A2 reports values without a verdict.

### Step 6. An existing measure from a study (only if asked)

If the person wants to use a measure a published study used, find the paper (`literature.search_literature`), take the sentence naming the measure from the abstract or full text, call `verify.qualify_source {doi, question}` then `verify.check_claim` with that passage, and accept only a passage read in the same direction (N3). Quote the study's measure as the study wrote it. Example from the build: the CTN-0044 registration lists "Coping Skills" as a secondary outcome (`references/precedents.md`).

### Step 7. Save the plan for A2

With code execution, write the plan as JSON in the shape of `evals/files/check_plan_illustrative.json` (one entry per link: id, type, column, aggregation, direction, threshold, prespecified, proxy). `scripts/link_check.py` reads this file.

## Build the output

Follow `assets/mechanism-check-plan-output.md`. Answer first: links with a measure and threshold, links with a measure and no threshold, links not measurable, and the one decision the person needs to make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every measure, proxy and threshold is the person's or open; proposals are labeled.
- Delivery and use are separate links from the outcome.
- Unmeasurable links are `[GAP]` and marked "not scored".
- The plan states its date and whether data had been read before it was set.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Mediation analysis methods, estimands and sample size: `dh-clinical-development` study-protocol-and-endpoint-design.
- Choosing a validated instrument for a new outcome: `dh-clinical-development` study-protocol-and-endpoint-design (endpoint and COA selection).
- Writing the mechanism itself: therapeutic mechanism and intervention design (DH-01.01.2.1).
