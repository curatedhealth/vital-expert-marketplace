# A1 Integration point map

Framework task: DH-01.01.3.1, Part A, task A1. Replaces the earlier "Integration point" section (DH-01.01.3.1.1).

## What this task delivers

A map of the places where one function must hand a named work product to another before a named decision can be made: work product, sender, receiver, the decision that waits, and, for each review the person names, the functions the person says attend. Each point is tied to the sourced anchor it rests on (design review, design transfer, multiple function impact assessment, software implementing a clinical model, critical-to-quality factor, deployment hand-over), or labeled "the person's integration point" where no source names it.

Why it matters: a decision that waits on work nobody has named as owed stalls quietly. The sources name a few places where work must cross functions (PL1, PL10, PL25, TM120, TM121, CV29, CS64); the rest the team must name itself.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.1 Part A, Integration point map |
| Workflow | The steps below |
| Knowledge | `references/handoff-rules.md` sections 1 and 3; rows PL1 to PL10, PL24 to PL29, PL41, PL80, PL91, PL98, TM120 to TM122, CV28, CV29, CV96, CS18, CS20, CS42, CS61, CS62, CS64, CS65 |
| Tools | Optional: `regulatory-dh.search_devices`, `regulatory-dh.get_authorization` for a named product's classification; `regulatory-dh.search_safety_events` only if the person asks about public events; `scripts/handoff_log.py check` on the person's log |
| Prompt | This guide |
| Template | `assets/integration-point-map-output.md` |
| Input | The request and its context: product and intended use as stated, stage, the functions and people the person names, the next review or gate, any existing log |
| Governance | `references/governance.md`; the person names the points, the receivers and the attendees |
| Catalogue job | none (`find_job` and `list_jobs`, 20 October 2026) |

## Read the request

- **Product and stage.** What is being built, for what intended use as the person states it, and where it stands (concept, build, verification, validation, release, deployment).
- **Next decision.** Which review, gate, release, submission or go-live is the person working toward? The map is built backward from it.
- **Functions and people.** The functions involved and the people the person names for each, in their words.
- **Shape of the product.** Does it have device and non-device functions (PL24)? Does software implement a clinical model the person names? Is a study running with critical-to-quality factors? Is a site deployment planned?
- **Markets.** US, EU, Germany or England change which anchors apply (QMSR, MDR, DiGAV, DTAC).
- **Disclosure.** Ask before sending unpublished product names to the library.

## Workflow

### Step 1. Fix the decision the map serves

Write the decision in the person's words ("Design review 3 go or no-go", "pilot site go-live plan"). If it is a design review, say what the source says a review checks (PL4) and when reviews are held (PL5). Do not say whether the gate will pass.

### Step 2. Walk the sourced anchors

For each anchor in `references/handoff-rules.md` section 1 that applies to the person's product, ask what work product crosses functions there:

- **Design review (PL1, PL4, PL6).** Which functions are "concerned with the stage under review"? List the functions the person names and the people they name. Note that the manufacturer chooses the individuals (PL1) and that independent review is a choice the person justifies (PL2, PL66, PL67).
- **Clinical evaluation inside design validation (PL7).** What clinical or performance evaluation output reaches the design validation record, from whom?
- **Design transfer (PL9, PL10).** Which final design outputs move into the medical device file, and who receives them? ISO 13485 7.3.8 text is not sourced `[GAP]`.
- **Other functions (PL24 to PL29).** For each non-device or other function, the team that owns it hands an impact assessment to the team that owns the device function; all three kinds (negative, positive, no impact) are documented as design validation (PL25). Separation is decided early in architecture (PL26).
- **Software that implements a clinical model (TM120 to TM122)** for products the person places under 21 CFR 882.5801 or a similar special control: clinical science hands the validated model to software; software hands SRS, SDS and V&V showing the model is implemented back to clinical science; clinical science hands the summary of clinical testing to labeling. Whether the product falls under that regulation is `dh-regulatory-and-quality` regulatory-pathway-and-classification's question. Where the person's regulation has special controls this skill holds only in part (for example 21 CFR 882.5803: TM123 and TM124 hold clinical testing and software, not labeling), write "labeling special controls for [regulation] not in this skill's sources `[GAP]`; `dh-regulatory-and-quality` regulatory-pathway-and-classification".
- **Study running (CV28, CV29, CV96).** Ask the person which handoffs carry a critical-to-quality factor; they mark them. Note dependencies among CTQ factors (CV29).
- **Deployment (CS64, CS65, CS61, CS62).** Data dictionary, data flow map, format and infrastructure requirements, training approach, usage and performance-change reporting plan: from product to the customer's implementation team.
- **Jurisdiction (PL80, PL91, PL98).** DiGA: §§ 3 to 6 evidence must all be in hand at application (PL80), certificates no older than 12 months (PL91). DTAC: form and evidence per version [WF] (PL98).

### Step 3. Add the person's own integration points

Ask what else moves between functions before the decision. For each, apply the old framework's test: a work product, a sender, a receiver and a decision that cannot be made until it arrives. A shared channel, a standing meeting or a status update is not an integration point. Label these "the person's integration point".

### Step 4. Fill each point, leave gaps visible

One row per point: work product, sender function and named person, receiver function and named person, blocked decision, anchor and rows (or "the person's"), what the source says the work product must contain where it says anything. Blank cells stay `[GAP]`. If the person has a log, run `python3 scripts/handoff_log.py check LOG.csv --as-of YYYY-MM-DD` and use its missing-field list.

### Step 5. Attendees, where the person named a review

List the functions the person says attend each review, beside the functions the person's map shows as sending or receiving for that stage. Where a sending or receiving function is not on the attendee list, show it as a difference for the person to resolve; do not add anyone. Never suggest a job title.

### Step 6. Named product (only if asked)

If the person names a marketed product as a reference ("map it like reSET"), read its record: `regulatory-dh.search_devices {query: "<maker or product>", jurisdiction: "US"}` then `regulatory-dh.get_authorization {reference: "<DEN or K number>"}`. Report class, product code, regulation number and dates as stored, with the retrieval date; do not judge how the record bears on the person's product. The record does not hold special controls or intended use (register P5): take the special controls from the TM rows for that regulation. If the person asks about public events, call `regulatory-dh.search_safety_events {product_code}` and quote the record; never attribute a cause.

## Build the output

Follow `assets/integration-point-map-output.md`. Answer first: the decision served, the number of integration points, the ones with gaps, and the anchor each rests on. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every point has a work product, a sender, a receiver and a blocked decision, or a visible `[GAP]`.
- Sourced anchors carry their rows; the person's points are labeled as theirs.
- No attendee, owner, job title, date or status was added by the model.
- No gate is called passed, and no map is called compliant.
- Each [PAPER] paper cited has its DOI once in prose, and beside its own row id in every table cell (rows from several papers each keep their own DOI); [WF] rows are labeled.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The design and development file, design review minutes as quality records, and design transfer procedures: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Whether a function is a device function: `dh-regulatory-and-quality` regulatory-pathway-and-classification; what a submission must contain about other functions (PL28): `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Separating device and other functions in the architecture: `dh-digital-therapeutic-design` (old pack, heading DH-01.06.4 DTx Architecture); this task only names the handoff of the impact assessment.
- Gate criteria across the lifecycle: clinical-product-lifecycle-and-stage-gates (DH-01.01.1.1).
