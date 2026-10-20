# A1 Readiness check

Framework task: DH-03.03.1.2, Part A, task A1. Replaces the earlier "AI/ML Approval Readiness Monitoring" section.

## What this task delivers

A completeness table for the person's AI device package against the sourced requirements for their target jurisdictions and dates: each item present, missing, not yet applicable (with its start date and the act that set it), not assessable, or not in the references. It answers "what is missing before we file, and what will apply later?" It does not judge whether present items are good enough; that is the person's.

Why it matters: AI device files fail on absences that are easy to miss: a PCCP without its third component, a post-market plan the protocol never describes, a technical file planned against an AI Act date that has since moved. A presence check against dated sources finds those early and cheaply. A quality judgment by a model would be false comfort.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.1.2 Part A, Readiness check |
| Workflow | The steps below |
| Knowledge | `references/readiness-requirements.md`; the three research files in `references/` |
| Tools | None required; `scripts/ai_act_dates.py` (optional); `verify.build_record` on sign-off |
| Prompt | This guide |
| Template | `assets/readiness-check-output.md` |
| Input | The request and its context: target jurisdictions, route and class (the owner's), planned filing or placing-on-market date, whether a PCCP is sought, the file index or table of contents, the pathway map if one exists |
| Governance | `references/governance.md`; readiness to file is the owner's call |

## Read the request

- **Jurisdictions and dates.** Which markets, and when the person plans to file or place on the market. Dates decide what is "not yet applicable". If no date is given, check against today (19 October 2026 at build) and say so.
- **Route and class.** Use the owner's decision. If undecided, check both branches, or route to the pathway skill (A1) first.
- **What the person has shown.** A file index, a table of contents, a list. Items not shown are "not assessable", never "missing".
- **Short or full.** "Are we AI Act ready?" is short mode on the EU rows. "Full readiness check before the Pre-Sub" is full mode.

## Workflow

### Step 1. Write back the scope

List: jurisdictions, route, class, PCCP yes or no, reference date, and whether the device is already on the market (for the AI Act legacy rule [AI EU-22]). Ask the person to confirm before checking.

### Step 2. Select the applicable requirement rows

From `references/readiness-requirements.md`, take the rows for each jurisdiction whose "Applies when" condition holds on the person's facts. For the EU, settle AI Act scope first: is the software an AI system (person's determination) and does its MDR class need a notified body [AI EU-27]? With code execution, `scripts/ai_act_dates.py --class IIa --ai-system yes --reference-date YYYY-MM-DD` prints the AI Act rows with dates and acts.

### Step 3. Mark each item

For each row: present (where the person shows it), missing, not yet applicable (date and act), not assessable, or `[GAP]`. For PCCP rows, check the three components separately [AI US-03 to US-06] and check that acceptance criteria exist as headings with the person's values, without judging the values [AI US-05]. For the software documentation level [US-R3], mark it present if stated. If the person states Basic, add one line, without deciding: "Enhanced applies where a failure could present a hazardous situation with a probable risk of death or serious injury, assessed before risk controls [RP US-26]; the level is your call."

### Step 4. Flag superseded sources

Scan the person's documents for dates and guidance versions. Flag: 2 August 2027 or 2 August 2026 used as the device high-risk date (in force: 2 August 2028, Regulation (EU) 2026/1744 [AI EU-19, EU-32]); the December 2024 PCCP guidance cited instead of the 18 August 2025 version [AI US-01] (the December 2024 version was final, now reissued; not a draft); the AI lifecycle guidance treated as final [AI US-21]; the 2022 CDS guidance [RP US-19]; quality-system citations to the retired QS regulation after 2 February 2026 [Q QS1]; FY 2026 fees [RP US-55].

### Step 5. Name the unsettled items

List what the sources leave open for this product: Article 72 timing for Annex I devices `[GAP]`; what counts as a significant AI Act design change `[GAP]`; GB PCCP (not in force [AI UK-04]); EU PCCP guidance (not published [AI EU-31]).

## Build the output

Follow `assets/readiness-check-output.md`. Short mode: the answer (counts by status and the most important missing item), one table of missing and not-assessable items, at most three unsettled items, the record line. Full mode: every row per jurisdiction, superseded-source flags, unsettled items, sources.

## Before you hand it over

- Every item cites its row and, for future obligations, its date and the act that set it.
- No item is graded; "present" means present.
- The output never says "ready to file" or "compliant"; it says what is present and missing, and that readiness is the owner's decision.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- If asked "are we ready?", answer with the counts and the missing items, and say the readiness decision is the owner's.
- Standards clause checks (ISO 13485, ISO 14971, IEC 62304) belong to the quality pack; their clause text is not in the references.
- Health Canada, Japan, Australia and other markets: no AI requirements in the references `[GAP]`.
