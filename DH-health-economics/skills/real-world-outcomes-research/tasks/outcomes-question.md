# A1 Outcomes question

Framework task: DH-01.07.3.1, Part A, task A1. Replaces the earlier "Outcomes question" section (CF-12.01.07.3.1.1).

## What this task delivers

A question brief for a real-world outcomes study: the question in the person's words, the study type to declare (HETE or exploratory), the PICO and estimand laid out with the choices still open, the data source checked against the framework that applies, the outcome measures and value set each target market expects, and what the published record already holds on the same question. It answers "what exactly are we testing, in whom, with which data?"

Why it matters: most real-world studies fail at the question, not the statistics. A question fixed and declared before any outcome data are seen is what lets the result be read as a test rather than a search (HE-025, HE-026).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Clinical Trials Director |
| Skill | DH-01.07.3.1 Part A, Outcomes question |
| Workflow | The steps below |
| Knowledge | `references/study-question-and-design.md`; HE, CV and ES rows in the `*-sources.md` files |
| Tool | `literature.search_literature`, `literature.get_record`, `literature.find_trial`, `literature.classify_study` (prior record); `verify.qualify_source` for any paper cited |
| Catalogue job | `evidence-table` (available) may tabulate the prior record; it does not frame the question |
| Prompt | This guide |
| Template | `assets/outcomes-question-output.md` |
| Input | The request and its context; the product, its intended use and regulatory status if known; candidate data sources; target markets and decision makers |
| Governance | `references/governance.md`; the person chooses type, comparator, estimand strategy, data source and measures |

## Read the request

- **The decision the study serves.** A payer or HTA submission, a NICE early-use evidence plan, a publication, an internal go or no-go. Ask if not stated; it decides which market rows apply.
- **Product and status.** Intended use, device class and markets, if known. If regulatory status matters and is unknown, mark it `[GAP]` and point to dh-regulatory-strategy `regulatory-pathway-and-classification`.
- **Prospective assignment.** If the person plans to assign people to the product, it is a trial (CV133): say so and point to dh-clinical-validation `study-protocol-and-endpoint-design` (DH-01.02.1.1).
- **Data in hand.** Claims, EHR, registry, app logs, or a planned collection. Ask which.
- **Mode.** Short for a direct question; full for a protocol working session.

## Workflow

### Step 1. Write the question in the person's words

One sentence, theirs. Then restate it as PICO (ES-36) and, for a patient-facing product, note the PICOTS-ComTeC extra domains as optional prompts (HE-032, abstract only). Leave any element the person has not given as "your choice, not made yet".

### Step 2. Declare the study type

Lay out what HETE requires (Berger et al. 2017, DOI 10.1002/pds.4297, rows HE-025 to HE-030: a specific hypothesis in a specific population, HE-025; declared a priori, HE-026; protocol and analysis plan publicly registered before analysis, HE-027; tested on a different data source from the one that generated the hypothesis, HE-029). Ask the person to declare HETE or exploratory. If the hypothesis came from the same data they plan to test it in, say so (HE-029). If outcome data have already been looked at, the study cannot be declared HETE for that outcome; it is exploratory, and the output says why.

### Step 3. Lay out the estimand

Fill the five attributes (CV33, CV34) from what the person gave. Name the expected intercurrent events (CV32), for example stopping the app, switching, starting medication. For each, show the strategies that apply (CV35 to CV39) and what question each answers. The person picks. Note that E9(R1) is written for trials and is used here as a framing (references, section 2). For a causal question, add the target trial emulation option (CV107) and the feasibility assessment before the protocol (CV106).

### Step 4. Check the data against one named framework

Ask which decision maker the evidence is for, then use one framework from the table in `references/study-question-and-design.md` section 3 (ICH E6(R3) Annex 2, FDA drugs, or FDA CDRH devices) and say which. For each key variable list: conceptual definition, operational definition, how it was or will be validated (CV80, CV81). For claims data, continuity of coverage (CV83). For registry reuse, consent scope (CV85). For app data used as an outcome, verification and validation (CV46) and endpoint definition (CV55). Mark what the person has not supplied `[GAP]`.

### Step 5. Outcome measures and value sets by market

For each target market, give the sourced expectation (section 4 table): NICE 5L rule and its start date, always both halves: new topics since 27 August 2026 use the UK 5L set; topics started before then keep mapping 5L to 3L (HE-058 to HE-063), HAS French 5L (HE-106), German 5L set (HE-128), ICER and ICER-PHTI (HE-120, HE-121, HE-122). If no market is named, ask; do not default to one.

### Step 6. Read the prior record

Search two or three phrasings with `literature.search_literature {query: "<intervention> <outcome> real-world <data source>", limit: 8}`. Keep only on-topic records. For each kept record, call `literature.get_record {doi}`, open the full text, and state design from the paper's methods, not the library label (register N8; `classify_study` only as a cross-check). Call `literature.find_trial {record}`; "no linked registration found" means not confirmed, not unregistered (`references/tools.md`). Report what the record shows on the same question, with design and data source, never as an effect size you have not read. If the person needs a full systematic review, that method is in dh-clinical-validation `literature-and-real-world-evidence-review`; point there.

### Step 7. Open choices and next document

List the choices still open (type, comparator, estimand strategy, data source, measures, markets) and the next document the person needs: a feasibility assessment (CV106) or the protocol and analysis plan, with the A2 execution log started now.

## Build the output

Follow `assets/outcomes-question-output.md`. Short mode: the question as PICO, the type to declare and why, the three choices that matter most, the data-fitness gaps, the prior record in at most three lines, the record line. Full mode adds the estimand table, the framework table per variable, the market table and the calls list.

## Before you hand it over

- Every rule carries its row; every [PAPER] row its DOI beside the row id, in prose and tables.
- Full text read for any open-access source before a field is marked `[GAP]` from its abstract.
- Every choice is marked as the person's; suggestions say "proposed".
- Designs of prior studies come from the paper, not the library label.
- No effect size, cost saving or certainty level is stated for the planned study.
- The record line ends the answer: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- No protocol signature, no registration, no regulator or payer contact.
- Randomized trial design is dh-clinical-validation `study-protocol-and-endpoint-design`; systematic review method is dh-clinical-validation `literature-and-real-world-evidence-review`. Economic model design is dh-health-economics 2.x. Device status is dh-regulatory-strategy `regulatory-pathway-and-classification`.
- Drugs, biologics and wellness apps are out of scope.
