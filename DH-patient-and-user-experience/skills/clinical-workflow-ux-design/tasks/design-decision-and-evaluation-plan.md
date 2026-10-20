# B1 Design decision and evaluation plan

Framework task: DH-02.04.4.1, Part B, task B1. Replaces the earlier one-line pass rule and owner sections of this competency.

## What this task delivers

A decision paper for one design choice (for example how a risk recommendation reaches the clinician: interruptive alert, worklist banner or inline in the order panel): the options, the sourced facts per option and criterion, what CDS Criterion 4 and ONC decision support rules ask the interface to show, the person's scores and weights ranked by the connector, where a weight change would flip the order, the formative evaluation plan for the chosen option, the facts the regulatory owner needs, and the stops. It answers "which design, and what do we test first?"

Why it matters: the order of the top options often rests on one weight. In the live example the top two differed by 1.25 points on a 0 to 100 scale (`examples/live/mcda_alert_placement.json`). Knowing that before building saves a rebuild. FDA also notes that if no formative work is done and flaws appear in validation, the validation test becomes formative (UX-M-06).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Service Design Director (`service-design-director`) |
| Skill | DH-02.04.4.1 Part B, Design decision and evaluation plan |
| Workflow | The steps below |
| Knowledge | `references/decision-support-and-evaluation.md`; A1 fit and A2 analysis; `references/ux-usability-research.md` |
| Tools | `analytics.mcda` (counted); `scripts/mcda_swap.py` (optional); `verify.build_record` for sign-off |
| Prompt | This guide |
| Template | `assets/design-decision-output.md` |
| Input | The request and its context: the options, the person's criteria, weights and 0 to 4 scores, A1 and A2 outputs, the decision owner |
| Governance | `references/governance.md`; people score, the connector ranks, the owner decides; device and submission questions go to the regulatory owner |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people score; regulatory questions are handed over, not answered

The person chooses criteria, weights and scores. The model lays out facts so scoring is informed, runs the ranking, shows where it is fragile, and never calls an option "recommended". Criterion 4 and ONC facts are laid out as design requirements to compare options on; whether the function is a device, meets the CDS criteria or falls in an HF Submission Category is the regulatory owner's (dh-regulatory-and-quality).

## Read the request

- **Options.** Take the person's. If none, ask; do not invent a list.
- **Criteria and weights.** Ask. Offer criterion names only as examples phrased so higher is better, because the connector treats every criterion that way (`references/tools.md`): "critical-task protection", "workflow interruption avoided", "basis reviewable by the clinician", "build effort avoided".
- **A1 and A2.** If missing, run them first in short mode or ask for the person's equivalents. Without A2, "critical-task protection" cannot be informed.
- **Certified health IT and market.** Decide which rows apply.
- **Decision owner and regulatory owner.** Names in the person's words, or "owner not named".
- **Mode.** Short or full.

## Workflow

### Step 1. Frame the decision

Write the decision, the options and the criteria back for confirmation.

### Step 2. Facts per option

For each option and criterion, list the sourced facts with row ids, no scores. Typical facts:
- Basis reviewable: Criterion 4 elements the option can carry (inputs explained UX-US-67; plain-language algorithm basis UX-US-68; knowns and unknowns such as missing inputs UX-US-69; decision-relevant information first, detail on request UX-US-70); automation bias risk under time pressure (UX-US-72).
- Workflow placement: certified DSI must appear while the user interacts (UX-US-54) and capture feedback (UX-US-55).
- Certified health IT transparency: source attributes and predictive DSI disclosures (UX-US-56 to UX-US-59), in force on 19 October 2026 but proposed for removal under HTI-5, not final (UX-US-60).
- Critical-task protection: the A2 controls each option carries and their type (UX-US-33).

State the consequence for the person in one line per option. If a fact depends on device status ("if this function is non-device CDS..."), say so and leave the question with the regulatory owner.

### Step 3. Collect the person's scores

Ask for 0 to 4 scores per option and criterion and weights that sum to 1. Write them back. A missing score stops the ranking for that option; say which.

### Step 4. Rank what they scored

Call `analytics.mcda`:

```
{alternatives: [{id: "<option>", scores: {"<criterion>": <0-4>, ...}}, ...],
 criteria_weights: {"<criterion>": <weight>, ...}}
```

Report each option's value and contributions. With code execution, save the call and response as JSON (`{"arguments": ..., "response": ...}`) and run `python3 scripts/mcda_swap.py FILE` to check the values and get the swap points. Report the smallest weight change that flips the top two in plain words.

### Step 5. Evaluation plan for the chosen option

Draft the formative plan the person can hand to their UX research lead: purpose, the UI portion, scenarios and tasks (the A2 critical tasks first), participants per distinct population, data collection, analysis, and how results feed the design (UX-US-44). Sample size is the person's, with the rule that formative sizes vary (UX-M-04) and the MHRA expectation that the rationale is documented (UX-UK-17). Note the validation conditions it prepares for, as facts: representative users, all critical tasks, final UI, realistic conditions (UX-US-34); at least 15 per distinct population (UX-US-35); no employees (UX-US-38); no think-aloud (UX-US-40); training matching real use and not immediately before testing (UX-US-41, CS80). Note consent and whether the Common Rule applies is the person's institution's call (UX-UK-19, UX-M-11, UX-M-12). For certified health IT, note the current safety-enhanced design minimum of 10 participants per capability, proposed for removal (UX-US-62, UX-US-63).

**Option: formative service pilot.** When the choice is a service model rather than a screen (for example nurse-led review versus pharmacist-led review of the same alert, built from an A1 blueprint), offer a small formative pilot of the service as the evaluation. The plan layout is method, not a sourced rule, and carries no number, threshold or legal statement: purpose (what the pilot must learn about the service), the blueprint steps and handoffs it exercises, the roles and population taking part (the person's), what is observed at each handoff, what would change the design, and the stop conditions the person sets. It is formative: it informs the design and is not human factors validation, and its results are never presented as validation or outcome evidence. Sourced facts that can inform it: staged scale-up starts with small pilots or demonstration projects before system-wide rollout (CS47 [PAPER]); for England, NICE ESF Standard 15 lists what a pilot-site statement may confirm (acceptability, intended performance, integration, no unintended harm, outcome improvement, use as expected) (CS59), and silent mode for products affected by local factors (CS60). Sample size, duration and success criteria are the person's.

A deployment pilot at a customer site (go-live, rollout, site readiness, training delivery) is not this task: route it to `customer-implementation-planning` (dh-go-to-market).

### Step 6. Handoff facts for the regulatory owner

Without picking a category, list the facts the FDA HF Submission Category decision points ask about (UX-US-48 to UX-US-51): UI, users, uses, environment, training or labeling changed or not; critical tasks none, new or impacted (from A2); UI history of use, complexity, adequacy of existing controls. Add that FDA recommends keeping human factors records whether or not submitted (UX-US-53) and encourages a Pre-Submission of the validation protocol (UX-US-46). Hand to the owner the person names.

### Step 7. Stops

List what stops: the decision itself (decision owner); device status, CDS criteria, HF category, Pre-Submission and any regulator wording (regulatory owner); acceptance of any open A2 gap (risk owner). If asked for wording to a regulator, draft only what the facts support, labeled "draft for the owner".

## Build the output

Follow `assets/design-decision-output.md`. Answer first: the ranked result of the person's scores and how robust it is, then the first formative test. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every score and weight is the person's, and the output says so; the ranking is never called a recommendation.
- Every fact has a row id; HTI-5 items say "proposed, not final".
- No device, CDS-criteria or submission-category conclusion.
- No dates or urgency in the plan.
- A service pilot, if offered, is labeled "formative" and "method, not a sourced rule", and is not called validation.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- One design choice at a time. Visual design and component standards belong to the Design Systems skills (UX 2.x).
- Running the study and judging its results is usability-monitoring and the person's research lead.
- A formative service pilot is planned here; a deployment pilot at a customer site goes to `customer-implementation-planning` (dh-go-to-market).
- No cost estimate: the rows hold no cost data; a cost criterion is scored by the person from their own figures.
