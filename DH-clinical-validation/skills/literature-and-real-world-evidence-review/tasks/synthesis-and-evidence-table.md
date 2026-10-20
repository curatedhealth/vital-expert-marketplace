# B1 Synthesis and evidence table

Framework task: DH-01.02.4.1, Part B, task B1. Replaces the old *Build an evidence table*, *Build a citation*, *Generate a literature report*, the old "pass rule" and "miss owner" lines, and the reporting half of *Signal Detection Analysis*.

## What this task delivers

From appraised studies: a pooling decision laid out with its rules (or a reasoned narrative synthesis), certainty per outcome set up for GRADE with each domain's evidence, a Summary of Findings table, the PRISMA 2020 flow from the person's log, an evidence table checked for missing fields and duplicate studies, citations, and the person's pass rule and owner for each gap. It answers "what does the evidence say, how sure can anyone be, and is the table clean enough to hand over?"

Why it matters: a pooled number over diverse studies can mislead (ES-83, ES-88); certainty is judged per outcome, never per paper (ES-96); and HTA bodies expect a flow diagram, an exclusion list and a certainty statement they can audit (ES-14, ES-149, ES-162). The synthesis is never more than its sources.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.4.1 Part B, Synthesis and evidence table |
| Workflow | The steps below |
| Knowledge | `references/appraisal-and-certainty.md` sections 5 to 8; `references/review-rules-by-body.md` sections 6 and 7; ES-11 to ES-21, ES-83 to ES-100, ES-132, ES-149, ES-162, ES-165, ES-166 |
| Tool | `scripts/prisma_flow.py`, `scripts/check_evidence_table.py`; `literature.build_evidence_table` (scaffold only); `literature.build_citation`; `verify.qualify_source` then `verify.check_claim` for any stated finding; `verify.build_record` on release |
| Prompt | This guide |
| Template | `assets/synthesis-output.md` |
| Input | The appraised studies and extraction sheet, the screening log, the reviewers' risk-of-bias judgments, the target body, the person's pass rule (what counts as enough evidence for their decision) and owners |
| Governance | `references/governance.md`; pooling, certainty and conclusions are the reviewers'; wording for a body stops for the owner |
| Catalogue job | `evidence-table` (available on 19 October 2026; the person may start it; its output still goes through Steps 4 and 5) |

## Read the request

- **What decision.** JCA (relative effects and certainty without value judgments, ES-149), NICE (pooling only with enough comparable valid data, ES-132), a publication, or an internal go or no-go. The decision sets the depth.
- **What exists.** Risk-of-bias judgments must exist before certainty can be set up; if they do not, say so and send the person back to A2.
- **Pass rule and owner.** If the person states what evidence would be "enough" (for example, two RCTs at low risk on the primary outcome), record it in their words as their rule. If they did not, do not invent one: "pass rule not given `[GAP]`".

## Workflow

### Step 1. Flow diagram

Run `python3 scripts/prisma_flow.py LOG.csv --rule <body>` (with `--jca` for a JCA). Report the counts in the order of ES-20 [PAPER] doi 10.1136/bmj.n160; if any reconciliation line fails, stop and return it to the reviewers rather than adjusting a number. For updates, ask for the number of studies in the previous version (ES-21). List excluded full texts with reasons (ES-13; Appendix D.2.2 for a JCA, ES-162).

### Step 2. Pool or not

Lay out, per outcome: studies and participants; comparators as reported; outcome measures and time points; direction of effects; risk-of-bias spread. Then the rules: pooling is optional and misleading with inconsistent direction (ES-83); diverse controls can mislead (ES-88); NICE needs enough comparable valid data and a heterogeneity assessment (ES-132); a JCA needs exchangeability and usually random effects (ES-165); only pre-specified subgroups (ES-87). Offer the options; the reviewers choose. If pooled numbers are given, report the model and heterogeneity with the I-squared bands as overlapping guides (ES-85) and check extraction first if heterogeneity is severe (ES-86). Do not compute a meta-analysis yourself unless the person gives the extracted data and asks; label any result "computed from the person's extraction, not reviewed".

### Step 3. Certainty per outcome (GRADE set-up)

For each critical or important outcome:

1. Starting level from study design: randomized high, non-randomized low; state the convention for ROBINS-I-assessed studies (ES-90, ES-100, research "Changes and conflicts").
2. Five downgrading domains with the evidence for each from A2 and Step 2: risk of bias (the reviewers' judgments), inconsistency (direction, heterogeneity), indirectness (PICO match), imprecision (interval, participants), publication bias (ES-91). Upgrading only per ES-92 and ES-93.
3. Leave the rating column for the reviewers; limits per ES-95. Every rating other than high needs an explanation (ES-99).
4. `literature.grade_evidence(standard="grade")` gives only a per-record starting level with empty factors (`tools.md`). Do not present it as an outcome's certainty. For a JCA, the QES "uncertainty" is not GRADE certainty (ES-166); report both terms as their sources use them.

### Step 4. Evidence table

1. Optionally scaffold with `literature.build_evidence_table(records=[...], passages={record_id: "<exact results passage>"}, question={population, intervention, comparison, outcome}, question_type="treatment")`. On 19 October 2026 it put a results sentence in the population field and kept a duplicate study as two rows; treat it as a scaffold only.
2. Build the table from the reviewers' extraction (one row per study result) and run `python3 scripts/check_evidence_table.py TABLE.csv` (add `--jca` for a JCA). Report missing fields, duplicate reports and same-result double counting, design-basis flags, tool and design mismatches, critical ROBINS-I studies marked for synthesis, and retracted papers, exactly as printed.
3. Fix nothing silently: each flag goes to its owner.

### Step 5. Summary of Findings

Columns per ES-97 and ES-98: population and setting, comparison, up to seven outcomes desirable and undesirable, comparator burden, relative and absolute effects, participants and studies, certainty (reviewers'), comments, explanations. Empty cells are `[GAP]` with what fills them.

### Step 6. Check any stated finding

For each finding the summary will state:

1. Get the results passage from the paper (Europe PMC or publisher), with its locator.
2. `verify.qualify_source(doi=..., question=...)`, then `verify.check_claim(claim={"text": ...}, passage={"text": <exact sentence>, "locator": ...}, source=<full qualify_source object>)`.
3. Your reading decides: accept only if the passage states the finding in the same direction (register N3). On 19 October 2026 a correct same-direction restatement came back "unsupported" and a reversed claim also "unsupported" (`tools.md`); record the tool status beside your reading.
4. Cite with `literature.build_citation(record=<record with authors>, passage=...)`; the citation inside `check_claim` is unreliable (C18).

### Step 7. Pass rule and owners

Write the person's pass rule in their words and set each outcome's evidence against it as "meets the person's rule", "does not", or "cannot tell: GAP". Use the owner or role the person names for each open item, in their words; if none, "owner not named". Never invent the rule or the owner.

### Step 8. AI-use table and record

Complete the AI-use table for the whole review (steps, what AI did, responsible human, how checked). For a JCA this is mandatory (ES-169, ES-170). If the output leaves the conversation, call `verify.build_record(clearances=[{"cleared_by": {"name": "<person named>"}}], claims=[...], sources=[...])`; otherwise label it an uncleared draft.

## Build the output

Follow `assets/synthesis-output.md`. Answer first: what the evidence shows per critical outcome in plain words with its limits, whether pooling was appropriate, the open certainty ratings, and the one decision the reviewers must make next. Never write "proves", "demonstrates efficacy" or "cost-effective".

## Before you hand it over

- Counts and table flags are from the scripts' output.
- Every certainty rating is the reviewers' or marked "not yet rated".
- Every stated finding has a passage, a locator and your same-direction reading.
- JCA outputs carry the AI-use table and use RoB 1 for RCT outcomes.
- Wording for a body or for promotion is labeled "draft for the owner".
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- The conclusion and its certainty are the reviewers' or the HTA body's.
- Economic models and value messages built on this synthesis belong to dh-health-economics; payer routes, HTA submission mechanics and prices to dh-market-access; marketing claims and payer communications to dh-commercial, with the owner the person names, or "owner not named".
- Whether a published review is current or trustworthy: `evidence-quality-and-signal-monitoring`.
