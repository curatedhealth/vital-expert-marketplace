# A1 Endpoint and COA selection

Framework task: DH-01.02.1.1, Part A, task A1. Replaces the earlier "Endpoint & COA Selection" section.

## What this task delivers

A sourced view of the endpoint options for the person's study: what comparable registered trials measured (verbatim, with design and time frames), the outcome assessment types that fit the claim, how each option would be defined to the four SPIRIT elements, and, for any digital measure, what verification and validation evidence exists and what is missing. The person and the owner they name for statistics choose; this task makes the choice informed and traceable.

Why it matters: in digital health the endpoint is where studies most often fail review. A sensor metric nobody validated in the target population, or a PRO with no meaningful-change anchor, can sink a well-run trial (CV48, PE-20).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.1.1 Part A, Endpoint and COA selection |
| Workflow | The steps below |
| Knowledge | `references/endpoint-rules.md`; rows CV42 to CV64, CV155 to CV159, PE-10 to PE-21, PE-93 to PE-96, SP-16, ES-36 |
| Tools | `literature.search_literature`; `literature.find_trial`; ClinicalTrials.gov record read and `scripts/registry_endpoints.py`; `verify.qualify_source` then `verify.check_claim` for a publication's stated endpoint |
| Prompt | This guide |
| Template | `assets/endpoint-selection-output.md` |
| Input | The request and its context: product, intended use or claim, population, comparator if chosen, markets, the endpoints or instruments already in mind, any V&V data held |
| Governance | `references/governance.md`; the person and the owner they name for statistics choose the endpoint |
| Catalogue job | none for endpoint selection; `evidence-table` (available) if the person wants the comparables graded. The steps below remain the method. |

## Read the request

- **Claim and PICO.** What must the study show, in whom, against what? Write it as PICO (ES-36). If the claim is unclear, ask: the endpoint follows the claim.
- **Candidates.** Instruments or measures the person already has in mind, verbatim.
- **Digital measure.** Is any endpoint captured by the product or another DHT? Which device and version? What V&V exists?
- **Markets and readers.** US, EU, Germany or England matter for which rows apply; payer evidence rules are Market Access's.
- **Disclosure.** Ask before sending unpublished product or endpoint names to the library (`references/governance.md`).

## Workflow

### Step 1. Find comparable trials

Call `literature.search_literature` with the condition, the intervention type and the design, for example `{query: "<intervention> <condition> randomized controlled trial app", limit: 10, filters: {designs: ["rct"]}}`. Screen the results against the person's PICO by title and record type; drop conference abstracts unless nothing else exists, and say so. Keep three to five. If none fit, widen one PICO element at a time and say which.

### Step 2. Get each trial's registration

Call `literature.find_trial` with `{record: {doi, pmid, pmcid, title}}` for each kept paper. The library leaves `trial_ids` empty on records, so this call is the only route to the NCT id. "No linked registration found" is a gap, not evidence the trial is unregistered (`references/tools.md`).

### Step 3. Read the registered endpoints

For each NCT id, read the ClinicalTrials.gov record (`https://clinicaltrials.gov/api/v2/studies/<NCT id>` or the record page). With code execution, save each as JSON and run `python3 scripts/registry_endpoints.py FILE.json ...`. Report per trial: design, masking, enrollment, primary outcome with time frame, secondary outcomes, verbatim. The script marks which SPIRIT item 16 elements the registered wording shows; a mark is a reading aid, not a finding (SP-16).

### Step 4. Check the published endpoint where it matters

For each comparable whose full text is open, take the publication's sentence stating the primary outcome (from the full text or the person). Call `verify.qualify_source {doi, question}`, then `verify.check_claim` with the claim, the passage `{text, locator}` and the full object from `qualify_source`. Accept only when you have read the passage and it says the same thing (N3). If registry and publication differ in wording, quote both and point to the monitoring skill.

### Step 5. Lay out the endpoint options

Build one row per candidate endpoint, from the person's list and from the comparables. For each: COA type (PE-11), the meaningful aspect of health and concept of interest it would address (PE-14, PE-15), the four elements as they would be defined (SP-16, CV55), who used it among the comparables, and what is still open (meaningful change anchor, PE-20; measurement properties, PE-93 to PE-96). Fill only from sources and the person's input; leave the rest `[GAP]`.

### Step 6. Digital measure fitness

For each endpoint captured by a DHT, walk the questions in `references/endpoint-rules.md` section 4: verification, validation in the study population, evidence types, reuse of existing data, usability, specifications, own-device policy, replicated or novel endpoint (CV46 to CV57). Mark each as shown (with the source the person holds), stated not shown, or `[GAP]`. If the person uses V3 terms, map them and say V3 is a [PAPER] framework, not FDA policy (CV155, research file conflicts).

### Step 7. What the choice depends on

Name, without choosing: the decisions the person and the owners they name must make (primary versus secondary, PRO versus digital measure, time point), and the facts that bear on each. If asked to propose a primary endpoint, label it "proposed", give the fact behind it, and leave the choice open.

## Build the output

Follow `assets/endpoint-selection-output.md`. Answer first: the comparables found, the endpoint options in one table, the biggest open item. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every comparable is described only by its registry record or publication, with NCT id or DOI.
- Every rule carries its row; [PAPER] rows carry the DOI; drafts are labeled.
- No endpoint is called validated, accepted or best. The choice is the person's, with the owners they name.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Graded literature reviews (review method): `dh-clinical-development` literature-and-real-world-evidence-review (DH-01.02.4.1).
- Whether a payer or HTA route accepts an endpoint: `dh-access-and-value` coverage-pathway-and-access-strategy (payer routes) and payer-engagement-and-hta-submission (submissions).
- Device status of the DHT: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Developing a new COA instrument (qualitative work, psychometrics) beyond the rows here: `[GAP]`, the owner the person names for outcome assessments, or owner not named.
