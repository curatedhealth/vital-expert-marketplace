# A2 Option test design

Framework task: DH-01.08.2.1 folded into this competency, Part A, task A2. Carries the old tasks "DH-01.08.2.1.1 Prototype Construction", "DH-01.08.2.1.2 Experiment Design" and "DH-01.08.2.1.3 Concept Validation Testing".

## What this task delivers

For one option the person wants to test before committing: a test plan with the person's question, the prototype or concept being tested, the prespecified endpoint, the success criterion, the decision rule (continue, change, stop) and the date it was written, the sample, and the regulated route the sources describe for the market (FDA early feasibility study and EFS Program, TAP, MHRA IDAP, AI Airlock, NHS evidence planning, NICE ESF early-deployment subset). For a finished test, a readout against the rule written before it started. It answers "how do we learn whether this option works before we commit, and what did the test teach?"

Why it matters: a test whose success criterion is written after the result, or an early study read as proof, lets a team keep an option alive on hope. FDA's own words say early feasibility studies "are not designed or intended to generate statistically valid results" but still need a specified purpose and meaningful endpoints (SP-115).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `chief-digital-health-officer` (old DH-01.08.2.1.1); `behavior-change-designer` (old DH-01.08.2.1.2); `ai-ml-governance-director` (old DH-01.08.2.1.3). Work as a strategy analyst who checks test plans against sourced rules |
| Skill | DH-01.08.2.1 in DH-01.05.1.1 Part A, Option test design |
| Workflow | The steps below |
| Knowledge | `references/option-test-rules.md`; rows SP-020, SP-025, SP-026, SP-109 to SP-129, PL110 to PL112, PL121, CS56, CS57, CS67, UK-06 to UK-08 |
| Tools | None. With code execution, the experiment log check in `strategy-execution-monitoring` (this pack) can read a finished test log |
| Prompt | This guide |
| Template | `assets/option-test-design-output.md` |
| Input | The request and its context: the option, the question, the concept or prototype, the market, the person's success criterion, decision rule and its date, sample, endpoint, and any result |
| Governance | `references/governance.md`; device status and pathway route to `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Catalogue job | none |

## Read the request

- **The option and the question.** In the person's words. If no question is given, ask; a test with no question cannot be designed.
- **The person's rule.** Success criterion, decision rule and the date it was written. Missing: "not given"; ask. Propose one only if asked, labeled "proposed".
- **The market.** US, EU, Great Britain, England or another. It decides which routes are cited.
- **Is it a device?** If the person does not say, do not decide. Device status is the developer's call (SP-129) and `dh-regulatory-and-quality` regulatory-pathway-and-classification's question.
- **Finished test.** If results are given, run step 5 only after the plan elements are written back.

## Workflow

### Step 1. Write the test back

Option, question, prototype or concept, population and setting, in the person's words. Missing: "not given".

### Step 2. Check the plan elements

Against `option-test-rules.md` section 1: specified purpose, appropriate subjects, meaningful prespecified endpoint (SP-115, FDA wording for device early feasibility studies, used here as a checklist), success criterion, decision rule, date the rule was written, sample. IDEAL-D ordering where the option is a device: stage 0 preclinical before first use in people (PL111, PL112, DOI 10.1097/SLA.0000000000004907). Each element: present, "not given", or written after the start.

### Step 3. Routes the sources describe

For the market in the request only (`option-test-rules.md` sections 2 and 3): FDA EFS and the EFS Program steps (SP-109 to SP-120) and TAP (SP-121, SP-122; quote the enrollment count with its date) for the US; MHRA IDAP (SP-124 to SP-126, pilot closed to new applicants) and the AI Airlock (UK-06 to UK-08) for Great Britain; NHS evidence planning (SP-127, SP-128) and the NICE ESF early-deployment subset (CS56, CS57, CS67) for England; EMA and MHRA innovation offices (SP-020, SP-025, SP-026). Say that FDA has no program called a sandbox (research file, "Not sourced"). The model lists routes; whether one applies is the regulatory owner's question, routed to `dh-regulatory-and-quality` regulatory-pathway-and-classification.

### Step 4. What the test will and will not show

One line each: what a positive result would let the person say, in the words of their question; what it would not show (an early, unpowered study does not establish effectiveness, SP-115); what would come next (a traditional feasibility or pivotal study, SP-112, routed to `dh-clinical-development` study-protocol-and-endpoint-design).

### Step 5. Readout of a finished test (if results are given)

Report the result against the rule written before the start, in the person's words: rule met, not met, or not readable (no rule, rule written after the start, result not reported, sample below plan). Never add a rule after the fact. Whether the option continues, changes or stops is the person's. Tracking several tests over time is `strategy-execution-monitoring` (this pack).

## Build the output

Follow `assets/option-test-design-output.md`. Answer first: what the test asks, whether the plan has a rule written before the start, the route the sources describe for the market, and the element that most limits what the test can show. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Question, criterion, rule and sample are the person's, or "not given"; any proposal is labeled "proposed".
- FDA EFS wording applied to a non-device test is labeled as borrowed.
- Only routes for the market in the request are cited; TAP counts carry their date.
- No statement that the product is or is not a device, or that a route applies.
- A finished test is read only against the rule written before it started.
- `python3 scripts/options_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it (for example "MHRA IDAP page, read 20 October 2026 (SP-124)").
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Clinical study protocols, endpoints and statistics: `dh-clinical-development` study-protocol-and-endpoint-design.
- Device status, IDE, pathway: `dh-regulatory-and-quality` regulatory-pathway-and-classification; AI-enabled devices: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Usability tests: `dh-patient-and-user-experience` usability-monitoring.
- Monitoring tests across options: `strategy-execution-monitoring` (this pack).
