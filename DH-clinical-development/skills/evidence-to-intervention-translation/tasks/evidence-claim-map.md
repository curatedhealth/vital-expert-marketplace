# A1 Evidence claim map

Framework task: DH-01.01.4.1, Part A, task A1. Replaces the earlier "Evidence claim map" section (DH-01.01.4.1.1). Also covers the earlier "Efficacy Evidence Linkage" task (DH-01.06.2.1.3, register CF-12.01.06.2.1.3, old worker `behavior-change-designer`), folded in on 20 October 2026; the method below is unchanged.

## What this task delivers

A map of every claim the product will make (in labeling, app text, onboarding, clinician material) against the passage that supports it: the source, the passage quoted with its locator, the population and dose that passage covers, the certainty as the person or a review rated it, and a status. Claims without a read passage stay `[GAP]`. At least one claim the product will not make is named, with the passage that rules it out.

Why it matters: the claim is where the product's intended use is set (PC-US-17) and where a German DiGA must stay consistent with its functions and published statements (TM148, PL92). A feature built from a claim nobody can source becomes a fidelity failure later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.4.1 Part A, Evidence claim map |
| Workflow | The steps below |
| Knowledge | `references/claim-map-rules.md`; rows TM119 to TM144, TM145 to TM149, PL63 to PL73, PL92, PC-US-17, PC-US-23 to PC-US-31, PC-DE-03 to PC-DE-05, ES-89 to ES-96, ES-201 |
| Tools | `verify.extract_claims`; `literature.search_literature`, `literature.get_record`, `literature.find_trial`, `literature.classify_study`, `literature.grade_evidence`; `verify.qualify_source` then `verify.check_claim`; `regulatory-dh.get_authorization` for a named authorized product |
| Prompt | This guide |
| Template | `assets/claim-map-output.md` |
| Input | The request and its context: product, intended use as the person states it, population, the claim text or product copy, the evidence held (papers, trial reports, a treatment manual) |
| Governance | `references/governance.md`; the person decides which claims the product makes |
| Catalogue job | none for a claim map; `evidence-table` (available) if the person wants the studies tabulated and graded. The steps below remain the method. |

## Read the request

- **Claims.** The exact wording, verbatim, from wherever it will appear. If only a feature list exists, ask what the product will say about each feature.
- **Intended use and population.** In the person's words. The claim map cannot test "wider population" without it.
- **Evidence held.** Papers, trial reports, a manual, a guideline. Unpublished data is the person's to describe; it is never sent to the library without their say.
- **Named products.** If the person cites an authorized product as precedent, get its reference (DEN, K or P number).
- **Disclosure.** Ask before sending unpublished product names or claims to the library (`references/governance.md`).

## Workflow

### Step 1. Split the text into claims

Call `verify.extract_claims {text}` on the product copy (up to 20,000 characters). It splits by sentence and marks every sentence checkable, including instructions and caveats (`references/tools.md`). Sort the result into: effect claims, population and indication statements, dose or regimen statements, safety or caveat statements, and mechanism statements ("works by"). Keep the person's wording.

### Step 2. Find the source for each effect claim

If the person holds the source, use it. Otherwise call `literature.search_literature {query: "<intervention> <condition> randomized", limit: 10}` and screen by title and record type against the claim's population and outcome; drop reviews, news and off-question items, and say so. For each kept paper, call `literature.find_trial {record: {doi, pmid, title}}` because `trial_ids` is empty on records (register N8). For a named authorized product, call `regulatory-dh.get_authorization {reference: "DEN..."}`; the record gives dates, product code and regulation number only, so indication and limitation wording comes from the decision summary rows (TM132, TM138, TM144) or the person's copy of the label. A record that was found but not read is listed by DOI with 'not read [GAP]'. Do not describe its design, population or results from its title or the library's design label (N8).

### Step 3. Quote the passage and check it

For each claim and source: take the passage that states the result (results or interpretation, never the background), with its locator. Call `verify.qualify_source {doi, question}`, then `verify.check_claim` with the claim, the passage `{text, locator}` and the full object `qualify_source` returned (register C18). Then read the passage yourself. Accept support only when it says the same thing, in the same direction, for the same population and outcome (register N3: a negation and a dropped hedge both returned "supported" in the build). FDA decision summaries are rated "inadmissible" by Verify (register C1): quote them from the TM rows and say Verify could not check them.

### Step 4. Record population, dose and certainty

For each supported claim, copy from the source: the population studied, the dose or regimen, the comparator and the outcome measure. Certainty: if the person or a review rated it, quote the rating (GRADE levels, ES-89; per outcome, ES-96). `literature.grade_evidence` returns a study-level label from the design tag only (register N8); report it as "library label", never as certainty. If no one has rated certainty, write `[GAP]` and point to `dh-clinical-development` literature-and-real-world-evidence-review.

### Step 5. Mark the status of each claim

Use four statuses: **sourced** (passage read, same direction, population and outcome match), **narrower than claimed** (passage supports a narrower population, outcome or verb; quote the difference), **[GAP]** (no passage read), **refused** (a read passage says the effect was not shown or may not occur, as in TM138 and TM144). A mechanism claim ("works by") is sourced only where a passage states the mechanism; otherwise it is a hypothesis (TM6 to TM8) and labeled so.

### Step 6. Check claim consistency rules where they apply

Lay out, without deciding: for an authorized US product, the CFL factors (indication, population, use limitations, regimen; harm; directions) where the claim reaches beyond the label (PC-US-23, PC-US-24; nonbinding guidance); disclosure does not cure a weak study (PC-US-30). For a DiGA, the claimed care effect must match intended purpose, functions, content and published statements (TM148, PL92), and German advertising rules on efficacy and cited studies (PC-DE-03 to PC-DE-05). For SaMD, valid clinical association, analytical and clinical validation (PL63 to PL65). Whether a claim may be used stops for the owner the person names for regulatory status, or owner not named.

### Step 7. Name at least one claim the product will not make

From the refused and narrower rows, propose the claim the product will not make, labeled "proposed", with the passage behind it. The person confirms.

## Build the output

Follow `assets/claim-map-output.md`. Answer first: how many claims, how many sourced, narrower, [GAP] and refused, and the claim the product will not make. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every "sourced" claim has a quoted passage with a locator, and you read it in the same direction (N3).
- No library grade is presented as certainty; certainty is the person's or a review's.
- No claim is called cleared, approved, compliant or "evidence-based".
- Each [PAPER] paper cited has its DOI once in prose, and every table cell that cites a [PAPER] row carries that row's own DOI; abstract-only and [WF] rows carry their label each time.
- No date, data cut, version, threshold or status appears that the person did not give ("not given" and ask); no fact comes from an earlier, separate request.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Building a review (search strategy, screening, risk of bias, GRADE ratings): `dh-clinical-development` literature-and-real-world-evidence-review.
- Whether the product is a device, or a claim changes its intended use: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- Promotional claims review and value messages: `dh-go-to-market` pricing-and-value-message-monitoring; catalogue job `claim-labels` labels claims against a stored intended purpose and is preparation for that review, not this map.
- Evidence statements for payers or HTA bodies: `dh-clinical-development` evidence-translation-and-communication and `dh-access-and-value` coverage-pathway-and-access-strategy.
