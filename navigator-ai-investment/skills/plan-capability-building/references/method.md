# Method: the rules the Execution skills apply

Shared by *Delivery Planning*, *Trial Design* and *Capability Build Planning*. Every rule carries its source and class. The canon says little about Execution method; where it is silent, the rule is an owner ruling of 19 October 2026 (OWNER, class O) adopted from Cowork's recommendation, and says so. Read 19 October 2026.

| Source key | Document | Version and status |
|---|---|---|
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L3 | Intelligence Core (layer) | 3.6, canonical |
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft |
| VM | VITAL method | draft v0.1, 17 October 2026 |
| ENGINE | Navigator engine `weighted_gap` delegability rule | in code (`mcps/nav_engine/v2/weighted.py`) |
| TOOLS | Connector tools at commit e23025f6e: `sequence_check`, `delegation_place`, `trial_note`, `methods_capability_gap` | in code (`mcps/ontology_navigator/jobs.py`, `tools.py`), read by Cowork from the owner checkout, and the tools session's build record (M) |
| OWNER | Owner rulings, Execution cluster | 19 October 2026 |

## X1 A step is a job

Five sizes of work: portfolio, program, mission (serves one outcome), job (ends at one review gate), unit of work (GOV-06 3.12). A delivery plan's step is a job, so every step ends at a review gate (OWNER ruling 1).

## X2 Capability, then constraints, then performer

"Before a person or agent is assigned to work, the required capability shall be resolved, then the constraints on who may act shall be checked, then the person or agent shall be assigned, in that order" (GOV-06 6.5.3; GOV-02 §11.3). The skills name roles and agent types, never named individuals (OWNER ruling 2).

## X3 Context of use before AI at a decision point

"A context-of-use declaration shall be made before AI is assigned to a decision point" (GOV-06 6.6.1). Its fields: question of interest, context of use, model influence, decision consequence, patient risk, regulatory impact (GOV-02 §9 `COUDeclaration`). At a critical decision point "a qualified human decides, with documented responsibility"; no intervention level overrides this (GOV-02 R-LINE). No tool stores the declaration; the skill drafts it for the person to complete and refuses to place AI at a critical point without it (OWNER ruling 6).

## X4 Delegation tiers and the five intervention levels

The connector stores three tiers: people only, agent with review, agent; regulated work stays people only unless the person records an exception; every item needs an oversight owner (TOOLS). The canon's five levels: assist, augment, automate, orchestrate, redesign; the process owner sets them (GOV-00 RUL-47, RUL-49). Mapping (OWNER ruling 3): people only ↔ assist; agent with review ↔ augment, or automate with a human approving; agent ↔ automate. Orchestrate and redesign are set at outcome level by the process owner, not in delivery planning.

## X5 The tier proposal

The engine's delegability rule scores four factors 1 to 10 by people: consequence (high = costly if wrong), reversibility (low = irreversible), checkability (low = cannot be checked), regulatory (high = regulated basis); reversibility and checkability count as 11 minus the score; any factor at 8 or more → people only; all at 3 or less → agent; otherwise agent with review (ENGINE). The skill shows this as a computed proposal; the person chooses (OWNER ruling 4).

## X6 Review points

Every delegated item needs a review date and a question; a missing one is stored as a gap (TOOLS). No method sets a schedule. Default: a review at each job's gate; the owner may add more (OWNER ruling 5, adopted from a Cowork proposal, not canon). A well-formed gate shows the evidence trail, names the reviewer, offers dissent, records the decision with responsibility (GOV-02 R-GATE).

## X7 Dependencies and capacity

The sequence check refuses a step whose dependency is not placed before it and a step with no capacity; it does not rank (TOOLS). Capacity is stated by people (role and share of time, or a number of agent runs); never assumed.

## X8 The trial template

The canon's safe-to-fail experiment: hypothesis, success signal, failure signal, time limit, exit condition (EOS-L3 §2C `ProbeSenseExperiment`), plus what the trial tool stores: the outcome served, a value range, a cost-to-test range (each low, mid, high, unit, basis; a point refused), and one measure with name, baseline and owner; the tool never declares success (TOOLS). Adopted as the trial template (OWNER ruling 7). The VITAL method names "Trials as Experiments" without a procedure (VM).

## X9 Success is defined before the trial

By the owner, before start: the measure, the target and the stop rule. Afterwards the result is only placed against the target; the owner declares success in Organizational Learning (OWNER ruling 8). The skill adds one standing stop rule: any failure that reaches a patient, clinician or regulator stops the trial (H, skill practice drawn from the circuit-breaker duty in GOV-02 R-BREAKER; CHECK with owner).

## X10 Which options get a trial

Options with the owner's result "Investigate first", and "Proceed" options whose risk or reversibility the owner asks to test (OWNER ruling 9).

## X11 Capability building without the maturity assessment

The operational maturity assessment (levels 1 to 5) waits for three owner rulings (level rule, priority formula, question set). Until then, capability building plans from the strategic gap register (Strategic Readiness): top gaps, the options that need them closed, an action, an owner, the required level and a date (OWNER ruling 11). No maturity level is stated.

## X12 Value and measures

Value is a range, declared, never realized until measured (GOV-06 6.3.2). A measure needs a baseline and an owner (TOOLS, `value_range` rule).

## X13 Facilitated, then one report

One question per turn, then one full report (OWNER; references/facilitation.md).

## Gaps in the canon (for the governance workstream)

No canonical procedure for delivery sequencing, review cadence, trial design or capability development planning; the rules above marked OWNER fill them by ruling, not by source.
