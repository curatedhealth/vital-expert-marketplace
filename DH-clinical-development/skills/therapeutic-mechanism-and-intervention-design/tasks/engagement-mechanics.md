# A3 Engagement mechanics design

Framework task: DH-01.01.2.1, Part A, task A3. Folds in the earlier DH-01.06.3.1 heading "Sustained Engagement Pattern Design & Behavioural Mechanics Implementation" (register CF-12.01.06.3.1), with its tasks "Behavioural Mechanics Design" (DH-01.06.3.1.1, CF-12.01.06.3.1.1), "Engagement Loop Construction" (DH-01.06.3.1.2, CF-12.01.06.3.1.2) and "Adherence Optimisation" (DH-01.06.3.1.3, CF-12.01.06.3.1.3). Old worker: `behavior-change-designer`; the binding of this skill is unchanged.

## What this task delivers

A mechanics table in which each behavioral mechanic (cue, reminder, streak, points, levels, rewards, narrative, social feature, unlock sequence, lock-out) and each engagement loop is tied to one link of the A1 mechanism and to the A2 component it supports, with the usage measure, the intended use as the person defines it, and their justification for it. Engagement is written as a proximal outcome, never as the outcome. Each mechanic carries the flags the dark-pattern and subscription rules raise, for the person and their named owner to settle. Adherence features are written the same way: what "adherent" means is the person's definition, and without a justified intended use the measure is called usage.

Why it matters: usage that does not serve a link can grow while the therapy does not reach the user (SE84, Perski 2017, DOI 10.1007/s13142-016-0453-1), and usage-outcome correlations are often weak or confounded (SE82, Perski 2017; SE88, Michie 2017, DOI 10.2196/jmir.7126). A mechanic that pushes use can also carry a risk to health (SE16) or a consumer-protection problem (SE113 [WF], SE130).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Validation Director (`clinical-validation-director`) |
| Skill | DH-01.01.2.1 Part A, Engagement mechanics design |
| Workflow | The steps below |
| Knowledge | `references/engagement-rules.md`; `references/precedents.md`; rows TM8, TM11, TM87, TM135, TM142, TM143, SE16, SE26, SE70 to SE73, SE78 to SE108, SE109 to SE132 |
| Tools | `regulatory-dh.get_authorization` and `regulatory-dh.search_safety_events` for a named precedent; `literature.search_literature`, `verify.qualify_source` then `verify.check_claim` only if the person says a mechanic is supported by a study; `scripts/mechanism_map_check.py` |
| Prompt | This guide |
| Template | `assets/engagement-mechanics-output.md` |
| Input | The request and its context; the A1 chain and A2 components (run A1 in short mode first if none exists); the mechanics or loops the person plans, verbatim; any intended-use definition, payment or subscription model, and the users (age, condition) as the person states them |
| Governance | `references/governance.md`; the person decides which mechanics ship, what effective engagement is, any threshold, and the owner for consumer-protection law |
| Catalogue job | none (`find_job` returned no match for mechanism design on 20 October 2026; no saved `list_jobs` output shows an engagement job) |

## Read the request

- **Mechanism.** Is there an A1 chain and an A2 component table? If not, ask for the outcome and the intended change, and write A1 in short mode first.
- **Mechanics.** The person's list, verbatim, including copy text for prompts, notifications and exit or cancel screens if they have it.
- **Intended use.** Does the person define what use is needed (sessions, lessons, minutes, a dose), and why? If not, it is "not given".
- **Users.** Age group and condition, in the person's words: children and people in crisis change which rules matter (SE113 [WF], SE129, SE132).
- **Money.** Is there a subscription, a trial that converts, or a reward of value outside the app? If unknown, ask.
- **Market.** US, EU or Germany (DiGA), as the person states it, or "not given".

## Workflow

### Step 1. Tie each mechanic to a link

For each mechanic or loop, write the link it serves (usually the user action link, TM87) and the A2 component it supports. A mechanic that supports no component and no link goes to the "not tied" list (TM8, TM11). Where the person says a mechanic exists for usage alone, label it "usage mechanic, not a therapy component". Note popular versus effective features where the person has data on both (SE84).

### Step 2. Write the loop

For each loop, write trigger, action, feedback and the next trigger in the person's words. Where the loop adapts to user data, specify it as an A2 decision rule (decision point, tailoring variable, rule, missing-data rule; TM82, TM89, JITAI, DOI 10.1007/s12160-016-9830-8); building the engine belongs to `dh-digital-therapeutic-design` (heading DH-01.06.1 Personalization Engine).

### Step 3. Effective engagement versus usage

For each mechanic, fill three columns (engagement-rules section 3): usage measure (SE80), intended use as the person operationalizes it, and their justification (SE90). If either of the last two is missing, write "usage, not adherence (SE92, Sieverink 2017, DOI 10.2196/jmir.8578)" and list "define effective engagement" as an open item for the person (SE86, SE87, Michie 2017, DOI 10.2196/jmir.7126). Note receipt versus enactment where the link is a skill (SE85). Never supply a threshold, a benchmark or a retention target; none is sourced (engagement-rules, opening note). Where the product is a DiGA, name the DiGAV usage definitions it will have to report (weekly minutes, weekly sessions, discontinuation after three weeks without use for prescriptions of 90 days or more, or 25 percent of the period for shorter ones; SE70 to SE72) as definitions, not targets.

### Step 4. Adherence features

For reminders, lock-outs, schedules and unlock sequences, write what they enforce or prompt and which A2 dose (TIDieR item 8) they serve, as the person states it. Show a precedent's pattern only if asked, as context: EndeavorRx's regimen enforced by lock-out and reminders (TM142), and its control that matched reward and engagement (TM143).

### Step 5. Flag the limits

Run each mechanic against `references/engagement-rules.md` section 6: repeated prompts after a choice, shame wording, unequal prominence of choices, cancellation harder than sign-up, attention capture designed to extend use, A/B-tested or personalized persuasion, targeting of children or people in crisis, AI-driven persuasion. Each match is a flag with its row and status ([WF], staff report, statute, guidance, regulation). For a subscription, list the ROSCA elements (SE114) and the current Negative Option Rule status (SE115, SE116). Which law applies, and whether the mechanic is lawful, is the call of the owner the person names for consumer-protection law, or owner not named. A reward of value outside the app routes to `dh-go-to-market` channel-and-partner-design. Compare each mechanic's usage measure with the dose its link states (for example, a daily streak on a link of 3 sessions a week) and list any mismatch as a fact from the person's map, not a flag.

### Step 6. Risks to health the mechanics carry

Name any mechanic that could carry a risk to health with the record that shows the pattern (screen addiction, decreased sleep quality, frustration, SE16, SE17; reward logic recall, PWE). Carry each into A4 as a hazard source. Do not rate it.

### Step 7. Precedent records (when the person names one)

Call `regulatory-dh.get_authorization {reference: "<DEN or K number>"}` and `regulatory-dh.search_safety_events {product_code: "<code>"}`. Quote what the record states, with its date. For reSET and EndeavorRx the saved outputs in `examples/live/connector_calls_2026-10-20.json` hold these calls (see `references/tools.md` on rechecking them live). Do not judge whether a recall bears on the person's product.

### Step 8. Check the structure (optional, with code execution)

Add the mechanics to the map JSON in the shape of `evals/files/mechanics_safety_illustrative.json` and run `python3 scripts/mechanism_map_check.py MAP.json`. It lists mechanics with no link, no intended use or justification ("usage, not adherence"), and the flags the person marked open. Its marks are structure checks, not findings.

## Build the output

Follow `assets/engagement-mechanics-output.md`. Answer first: how many mechanics tie to a link, which do not, whether effective engagement is defined, and the flags that need the person's owner. Where no owner is named, write "owner not named" in the answer and ask, before the record line: "Who owns which mechanics ship and the flags for consumer-protection law, and who clears this draft? A name or role in your words." Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every mechanic names its link, or sits on the "not tied" list.
- Engagement is a proximal outcome on a link, never the outcome; no usage figure is presented as benefit.
- No benchmark, retention target or intended-use threshold was supplied by the model; proposals are labeled "proposed".
- No mechanic is called "safe", "effective" or "compliant"; flags are flags, not findings.
- [WF] rows (SE109 to SE113, SE117, SE118) carry their label every time they are applied, in every table cell; SE109 to SE113 also carry "staff report, not a rule" in every cell. A subscription mechanic's Flags cell carries ROSCA (SE114) and the Negative Option Rule status (SE115, SE116).
- Every [PAPER] row id carries its own paper's DOI: once in prose at first use, and in every table cell that holds it, even if given earlier; rows from different papers each keep their own DOI. Abstract-only and [WF] rows carry their label every time they are applied.
- No job title appears that the person did not use; owners are the person's words or "owner not named". Where no owner is named, the answer writes "owner not named" and asks, before the record line: "Who owns which mechanics ship and the flags for consumer-protection law, and who clears this draft? A name or role in your words." No date, data cut, threshold or status appears that the person did not give or a record does not state.
- The record line is the last line of the answer body (the calls list, if any, follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Reading engagement and retention after launch: `dh-clinical-development` mechanism-validation-monitoring (A3 there).
- Personalization engines that drive adaptive loops: `dh-digital-therapeutic-design` (heading DH-01.06.1 Personalization Engine).
- Usability of the mechanics: `dh-patient-and-user-experience` clinical-workflow-ux-design.
- Patient rewards of value and beneficiary-inducement rules: `dh-go-to-market` channel-and-partner-design.
- Recording mechanics as design inputs: `dh-regulatory-and-quality` design-controls-and-risk-management.
