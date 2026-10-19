# A1 Training task card and plan

Framework task: DH-02.02.4.1, Part A, task A1. Replaces register task CF-12.02.02.4.1.1 "Training task".

## What this task delivers

One task card per role (role, the task from the day-one workflow, the steps the user performs, what is out of scope for the session) and a training plan checked against what the sourced frameworks expect: the training need in the pathway, the end-user training approach, the cost line, and, for a device, the limits of training as a control. It answers "what must each role be able to do on day one, and does our plan cover what NICE and FDA expect of training?"

Why it matters: training that teaches screens instead of the task produces attendance, not use. Where the product is a device, FDA treats training as the least preferred control because it depends on memory and decays (CS77, CS78), and a training change can trigger a human factors submission decision (UX-US-49). A plan that ignores this either over-promises safety or breaks the validated use.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.02.4.1 Part A, Training task card and plan |
| Workflow | The steps below |
| Knowledge | `references/training-rules.md`; rows CS18, CS19, CS56 to CS65, CS77 to CS83; UX-US-28, UX-US-31, UX-US-33, UX-US-41, UX-US-42, UX-US-49, UX-EU-14 |
| Tools | `regulatory-dh.search_safety_events` (counted, optional); `verify.qualify_source` and `verify.check_claim` (counted, only if a method claim leaves the conversation) |
| Prompt | This guide |
| Template | `assets/training-task-and-plan-output.md` |
| Input | The request and its context: product, customer site, roles, the day-one workflow, the old step, whether the product is a device and which tasks are critical (from the person's regulatory owner), validated training content if any, the buyer's market |
| Governance | `references/governance.md`; clinician-facing training and go-live plans stop for the owner; training as a risk control stops for the regulatory and design owners |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. post-market-watch also reads safety events but sets a watch; it is not called. |

## Read the request

- **Roles and workflow.** Which roles touch the product on day one, and what they do. If the workflow is not described, ask; without it there is no task card.
- **Device status and critical tasks.** Ask whether the product is a medical device and which tasks are critical (UX-US-28) as the regulatory owner defined them. Never decide either. If unknown, `[GAP]` and keep section 3 of `training-rules.md` conditional.
- **Market.** NHS buyers bring ESF, DTAC and DCB0160 (CS56 to CS71); for other markets the research holds no training-plan duty (`[GAP]`). If the person describes the product by a US clearance and the buyer is NHS, note in one line that DTAC asks for proof of UKCA marking or a recognized equivalent (CP-UK-03) and that UK device status belongs to the regulatory owner (dh-regulatory-strategy); do not assess it.
- **Proposed fix.** If the person asks whether training can fix an error users make, run Step 4 first.
- **Mode.** Short for a direct question; full for a training plan document.

## Workflow

### Step 1. Write the task cards

For each role: the role name in the person's words, mapped to a CFIR 2022 role (CS18); the task from the day-one workflow; the steps the user performs; what the user does not need to learn in this session (register CF-12.02.02.4.1.1). Note per role what training cannot supply: opportunity (time, scope) and motivation are separate from capability (CS19). Do not train features outside the site's scope.

### Step 2. Check the plan against the sourced expectations

Build a table, one line per element, each with its row and "covered", "not covered" or "not stated":

- training need in the pathway description (ESF Standard 12, CS58);
- planned end-user training approach and communication of outputs, benefits and limitations (ESF Standard 20, CS65);
- training and staffing cost in the budget impact (ESF Standard 17, CS63);
- the expected usage profile the training aims at (ESF Standard 16, CS61), which adoption-monitoring will measure;
- for NHS buyers, DTAC and DCB0160 as the customer's assurance and clinical safety duties [WF] (CS69 to CS71);
- the customer's own HIPAA workforce privacy and security training (CS82, CS83) as theirs, not this plan's.

For non-NHS buyers, list the ESF items as "used as a checklist, not a duty in your market".

### Step 3. Device check (only if the person says the product is a device)

State, conditionally: customer training should match the training used in validation, because validation after different training is not valid and retention decays (CS80, UX-US-41); training materials are part of the user interface (UX-US-31); a change to training or labeling is a Decision Point B trigger (UX-US-49). Ask whether the validated training content is available. Any difference between it and the planned customer training goes to the regulatory owner before training ships.

### Step 4. If training is proposed to fix a use error

Lay out, without a verdict: the order of preference puts design first and training last (UX-US-33); training depends on memory and decays (CS77, CS78); "additional training" is not acceptable in a submission without data that it works (CS79, UX-US-42). Name the design option beside the training option for B1. Stop: whether training is an acceptable control is for the regulatory and design owners. Draft the question to them, labeled "draft for the owner".

### Step 5. Field events (optional)

If the person names their product or manufacturer, call `regulatory-dh.search_safety_events` with `manufacturer` or `product`, a `since` date they choose and `limit` 10. Read `references/tools.md` first. For each event, quote what its summary states. If a summary describes something a user does or sees (for example a setting on the user's phone), add "touches the task card for ROLE, per the summary". Never infer a use error or a training need from a recall; no event is not evidence of no events.

### Step 6. What it means for the person

Two or three consequences from the rows, stated conditionally. For example: "If the training plan is shorter than the training used in validation, the validated use no longer describes your customers' use (CS80)." "The NHS buyer will see training and staffing in the budget impact (CS63); a plan without that line leaves the buyer's case incomplete."

## Build the output

Follow `assets/training-task-and-plan-output.md`. Answer first: the task cards (or the one the person asked about), then the elements not covered. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every task card uses the person's roles and workflow; nothing is invented.
- Every task card row keeps the "What training cannot supply (CS19)" cell, even when the steps are [GAP]; it is never cut in short mode.
- Every requirement has a row; NICE items are labeled a checklist outside NHS buyers; [WF] rows say so.
- No statement that training controls a risk or makes use safe.
- Device rows appear only if the person said the product is a device.
- Clinician-facing material is a draft for its editorial owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Training content for the customer's roles. Usability testing and human factors evidence belong to the UX pack (dh-user-experience, healthcare UX design); device status and submissions to dh-regulatory-strategy.
- Implementation planning and deployment coordination belong to DH-02.02.1.x; outcomes the customer agreed to see to DH-02.02.3.x; payment tied to outcomes to Market Access (outcomes-contract-monitoring).
- The customer's HIPAA workforce training programs belong to their privacy and security owners.
