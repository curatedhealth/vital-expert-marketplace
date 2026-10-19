# A1 Evidence requirement map

Framework task: DH-03.01.3.1, Part A, task A1. Replaces the earlier "Value Dossier Assembly" section.

## What this task delivers

A table, per target body, of what that body requires of the evidence, set against the studies the person actually holds: shown, not shown, or `[GAP]`, each with its source row and, for the person's studies, the library record, design, CEBM level from design, and the Verify status of each key claim with the passage that decided it. It answers "what does BfArM (or HAS, or NICE) need, and which of our studies cover which part?"

Why it matters: most files fail on gaps the company could have seen. A DiGA trial without a German setting or a transferability case, a PECAN claim of organizational progress with no organizational endpoint, a NICE response with no UK-relevant study: each is visible before filing if the requirement and the evidence sit side by side.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.1 Part A, Evidence requirement map |
| Workflow | The steps below |
| Knowledge | `references/evidence-requirements.md`; `references/hta-submissions-sources.md`; `references/requirements/` |
| Tools | `literature.search_literature`, `literature.get_record`, `literature.classify_study`, `literature.grade_evidence`, `verify.qualify_source`, `verify.check_claim`; `market-access-dh.list_schemes` (free); `scripts/diga_study_rules.py` (optional); `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/evidence-map-output.md` |
| Input | The request and its context: product, intended purpose and device class, target bodies, the person's studies (DOI, PMID or the document), the claims they want to make |
| Governance | `references/governance.md` |

Tool names use the library's names; arguments and pitfalls are in `references/tools.md`.

## Read the request

- **Bodies.** Take them from the request or from a pathway map in the conversation. If none are named, ask which, offering Germany (DiGA), France (PECAN, LPPR, LATM), England (NICE) and the United States (Medicare). Keep to the ones named.
- **Device facts.** Device class and intended purpose decide whether the DiGA trial route is open (`DE19`) and whether medical benefit is mandatory (class IIb), and the ESF tier (`UK12`). If unknown, mark `[GAP]` and carry on with both branches shown.
- **Studies.** Ask for an identifier (DOI or PMID) for each study the person relies on. A product name is not enough: a search by name returns related trials that do not name the product (`references/tools.md`).
- **Claims.** Ask which claims the person wants to make (for example "reduces insomnia severity", "improves adherence"). Without claims, map the studies to the requirements and skip step 5.
- **Mode.** "Is our RCT enough for…" is short mode. "Full evidence map for the steering committee" is full mode.

## Workflow

### Step 1. Fix the rule set per body

Open `references/evidence-requirements.md` and copy, for each named body, the rules that apply to this product, with row ids. For Germany, state which effect type each claim targets: medical benefit (`DE6`) or one of the nine pSVV areas (`DE7`), and flag any claim resting on staff workload or economic indicators as inadmissible (`DE8`). For France, name the route (LPPR, PECAN, LATM, or two dossiers, `FR8`). For England, say there is no company submission and the map prepares answers to NICE's requests (`UK2`). For the United States, keep to the rows that exist.

### Step 2. Resolve each study

For each study, call `literature.get_record` with `doi` (or `pmid`). Record identifiers, title, venue, year, retraction status, open-access URL and `trial_ids`. If the person gave only a name, call `literature.search_literature` with the name and the indication, show the candidates, and ask which is theirs. Never pick one silently.

### Step 3. Classify and grade

Call `literature.classify_study` with the record, then `literature.grade_evidence` with the record and `question_type` "treatment" (or "diagnosis" for a diagnostic component). Report design with the fields that decided it, and the CEBM level labeled "from design only". Neither is a body's view.

### Step 4. Check each study against each rule

For each rule, decide shown, not shown, `[GAP]`, or not applicable, using `references/gap-rules.md`. The record answers design and publication; the person's paper answers the rest. For DiGA, `scripts/diga_study_rules.py --record <saved get_record JSON> --facts <facts JSON>` applies G1 to G7 and prints each rule with its status; fill the facts file from the paper sections the person shows (country, comparator, registry id, completion and publication dates, use data, endpoints). With no facts file, every rule the record cannot answer comes back `[GAP]`, which is correct.

Specific checks that catch common misses:
- A waitlist or care-as-usual comparator fits the DiGA "non-use" comparator (`DE11`); an active-control-only design does not show use beats non-use (`DE10`).
- A study outside Germany needs a transferability case on guidelines, access and reimbursement, and validated questionnaire language versions (`DE12`, `DE13`).
- An empty `trial_ids` field means the library cannot confirm registration (`DE14`); ask for the registry entry.
- Studies started under the 2026 amendment collect duration and frequency of use (`DE15`).
- For LPPR, no usable comparative study generally means no ASA (`FR4`); for PECAN, the ongoing studies must be expected to support the later opinion (`FR13`).
- For any organizational claim (pSVV, PECAN organizational progress, LATM organizational gain), look for a measured organizational endpoint (`FR25`).

### Step 5. Check the key claims

For each claim the person wants to make: call `verify.qualify_source` with the study's DOI; then `verify.check_claim` with the claim, the **results or conclusion sentence** quoted verbatim from the paper with its locator, and the returned source. Then read the passage yourself. `check_claim` decides on word overlap and has marked a claim and its negation both "supported" from a passage that stated no result (`references/tools.md`). Record the claim as "checked" only when the passage states the finding in the same direction; otherwise "not checked". If the person has not supplied the results text, the claim is "not checked: results passage not supplied".

### Step 6. Say what it means

Close with the consequence, in facts: which requirements are open per body, which body the current evidence fits best on the rules alone, and what evidence would close each open requirement. Phrase it as "on the sourced rules, X is not yet shown", never as "BfArM will refuse". Which route to take is the person's decision (the coverage pathway skill, B1, holds the strategy).

## Build the output

Follow `assets/evidence-map-output.md`. Answer first: per body, one line on what is shown and what is open. Then the requirement table, the study table, the claim table with passages, and the open items. Short mode keeps one table (requirements by body, with the study that shows each) and the claim lines.

## Before you hand it over

- Every requirement carries its row id and read date; every study its identifiers; every checked claim its passage.
- No "met" for a rule the record cannot answer.
- CEBM level is labeled "from design only".
- Effect type, comparator and ASA claims are flagged as the accountable owner's decision (owner as named, or "owner not named").
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No judgment that the evidence is "strong enough": the person and the owner they name decide. You list facts against rules.
- No new study design; point to the clinical validation pack for protocol work.
- Drugs, biologics and wellness apps are out of scope.
