# A4 Safety and efficacy signal read

Framework task: DH-01.01.2.2, Part A, task A4. Folds in DH-01.06.2.2 Safety & Efficacy Compliance Assessment & Therapeutic Quality Monitoring (register CF-12.01.06.2.2): the old sections "Therapeutic Safety & Efficacy Monitoring" (DH-01.06.2.2.1, CF-12.01.06.2.2.1) and "therapeutic safety pass rule" (DH-01.06.2.2.2, CF-12.01.06.2.2.2, now steps 1 and 2 here). The old "therapeutic safety miss owner" (DH-01.06.2.2.3) is part of B1.

## What this task delivers

For one version and the periods the person names: complaints, adverse events, use errors and other signal categories counted as the person categorized them, rates on the person's denominator, any efficacy measure the person tracks, and each compared with the threshold the person set before launch: crossed, not crossed, or not compared. Named products' public safety records are quoted as the records state them. The rule text on what counts as a reportable event, a malfunction or a risk to health is laid out; whether anything is reportable is the call of the owner the person names for vigilance reporting, or owner not named.

Why it matters: MDCG 2025-10 asks for indicators and threshold values set in the premarket phase and re-evaluated with PMS data (SE63); FDA's malfunction definition includes failure to meet "all claims made in the labeling" (SE40), so an efficacy drift is a signal to read, not only a marketing question.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`); the old DH-01.06.2.2 files bound `behavior-change-designer` (BUILD_NOTES) |
| Skill | DH-01.01.2.2 Part A, Safety and efficacy signal read |
| Workflow | The steps below |
| Knowledge | `references/signal-read-rules.md`; `references/precedents.md`; rows SE1 to SE20, SE27, SE33 to SE68 |
| Tools | `scripts/signal_read.py` on the person's event and exposure files. Named product: `regulatory-dh.search_safety_events {product_code}` or `{manufacturer}`, `regulatory-dh.get_authorization {reference}` |
| Prompt | This guide |
| Template | `assets/safety-and-efficacy-signal-read-output.md` |
| Input | The request and its context; the event log with the person's categories; active users per period; any efficacy measure per period; the thresholds and the date set; the version |
| Governance | `references/governance.md`; thresholds, categories, seriousness and reportability are the person's or their named owner's |
| Catalogue job | none (`post-market-watch` would call `watch_register`, which this skill never calls; `references/tools.md`) |

## Read the request

- **Thresholds.** Which signals, which threshold, set when? Set before launch, or after? Without thresholds, write them with the person first (step 1).
- **Categories.** Who categorized each event (complaint, adverse event, use error, malfunction)? The skill keeps their categories and never reclassifies.
- **Periods, version, denominator.** As the person gave them; otherwise "not given" and ask. Never supply a period or an awareness date.
- **Named product.** If the person names a product or product code, the library can return its public recalls and report counts.
- **Reportability.** If the person asks "is this reportable", say the call is the owner's they name for vigilance reporting (or owner not named), lay out the rule text (signal-read-rules section 3), and route to `dh-regulatory-and-quality` audit-capa-and-complaints.
- **Privacy.** Event and patient details stay local; never send them to a library call.

## Workflow

### Step 1. Write the signals and thresholds before reading (old "pass rule", step 1)

List the elements that count, as the old pass rule did ("hazard, monitoring signal, and stop rule"): for each hazard the design named (from therapeutic mechanism and intervention design A4, or the person's risk documents), the signal that would show it (a complaint category, an event category, a use error, an efficacy measure), its denominator and period, the threshold, and the stop rule the person attaches. Each element is the person's. The DHAC (advisory, non-binding) said postmarket monitoring should mirror premarket evidence and may include engagement, adherence and symptom reports (SE27).

### Step 2. Which element blocks release (old "pass rule", steps 2 and 3)

Ask the person which signal, if crossed, they treat as blocking release (old pass rule step 3). Record it in their words. The skill never sets a stop rule.

### Step 3. Run the read

With code execution, run `python3 scripts/signal_read.py --thresholds THRESHOLDS.json --events EVENTS.csv --exposure EXPOSURE.csv --version "<version>"`. It counts by the person's category per period, lists events outside every period (never dropped silently), computes rates on the person's active-user denominator, and marks each signal crossed, not crossed, or not compared (threshold set after launch, or no value). Check the output against the files before quoting.

### Step 4. Named product: public records

For a named product, call `regulatory-dh.search_safety_events {product_code}` (or `{manufacturer}`), with `since` set only from a period the person gave. Quote each record as it states, with its date and class (example: the PWE recalls of 7 June 2021, `precedents.md`). MAUDE counts are reports, not confirmed events. Do not judge whether a record bears on the person's product. If the connector is unavailable, say in the answer body, not only in the calls list: "saved records of 20 October 2026, not rechecked live". For a precedent's safety facts from the De Novo summaries (SE11 to SE20), quote the rows; a precedent's adverse event rate is not a threshold.

### Step 5. Lay out the rule text, not the call

For each crossed signal, lay out the rule text that touches its category (signal-read-rules section 2 and 3: 803.3 reportable event, "caused or contributed" including labeling and user error, malfunction including labeling claims, 806.2 risk to health, MDR Art. 87(1)(a) expected side-effects, MDR Art. 83(4) action duty), quoted with its row. Then say: whether this is reportable under 21 CFR 803 or 806 or MDR Articles 87 to 89, and by when, is the call of the owner the person names for vigilance reporting, or owner not named; deadlines from the awareness date are computed in `dh-regulatory-and-quality` audit-capa-and-complaints. Never write "reportable", "not reportable", "serious" or "device-related" as a finding, and never write a sentence that ties a rule to a named signal (for example "this touches S4"); list the rule by category and let the owner apply it.

### Step 6. Efficacy drift

For an efficacy measure, report the value per period against the person's threshold and the version; state the measure is the person's and no source sets a drift threshold (signal-read-rules section 2). A crossed efficacy threshold goes to B1 beside the claims the product makes; claim and labeling wording stop for the owner and `dh-regulatory-and-quality` regulatory-submission-and-dossier.

### Step 7. Hand on

List each crossed signal with its value, threshold, period and source for B1. Categories counted without a threshold are listed as such. Name the routes: complaint handling and reportability to `dh-regulatory-and-quality` audit-capa-and-complaints; risk file updates to `dh-regulatory-and-quality` design-controls-and-risk-management; device status and whether a special control applies to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

## Build the output

Follow `assets/safety-and-efficacy-signal-read-output.md`. Answer first: version, periods, which signals crossed the person's thresholds, which were not compared and why, and who makes the reportability call. Where no owner is named, write "owner not named" in the answer and ask, before the record line: "Who owns reportability, the thresholds and the next step on each crossed signal, and who clears this draft? A name or role in your words." Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Only thresholds set before launch (or before the period, as the person says) are compared; the date set is shown.
- No event is reclassified; no seriousness, causality, device-relatedness or reportability is decided.
- Nothing is called "safe", "effective", "compliant" or "acceptable"; a threshold not crossed is not a finding of safety.
- Public records are quoted as stated, with date; no judgment of their bearing on the person's product.
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". Where no owner is named, the answer writes "owner not named" and asks, before the record line: "Who owns reportability, the thresholds and the next step on each crossed signal, and who clears this draft? A name or role in your words." No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Complaint handling, reportability, reporting clocks and CAPA: `dh-regulatory-and-quality` audit-capa-and-complaints; complaint trends after a CAPA: `dh-regulatory-and-quality` capa-effectiveness-monitoring.
- The risk file and the hazard analysis: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Designing safety into the mechanism and mechanics: therapeutic-mechanism-and-intervention-design (DH-01.01.2.1).
- Labeling, claims and PMS documents for an authority or notified body: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
