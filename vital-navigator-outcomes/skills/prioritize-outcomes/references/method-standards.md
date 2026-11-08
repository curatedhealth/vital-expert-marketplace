# Method standards: prioritize-outcomes

| Id | Standard / practice | Status | How this skill uses it |
|---|---|---|---|
| MS-01 | Shared 10-part decision record (Launch Navigator design package 02; non-gate path) | [CHECK] | Outputs that feed close / board pack map to record parts; no launch_gate unless handed to Launch Navigator |
| MS-02 | People score; assistant never scores, weights, chooses or signs | [CHECK] | Scripts refuse without team-entered numbers; autonomy marks human-only gates |
| MS-03 | Evidence classes M / V / H; [GAP] never filled from model memory | [CHECK] | Intake and tasks leave unknowns visible |
| MS-04 | Offline first; connectors cited when used | [CHECK] | Connectors section in SKILL.md |


## Method notes

# Method: the rules the Outcomes skills apply

Shared by *Outcome Discovery* and *Outcome Prioritization*. Every rule carries its source, the version read and the date read. A rule not listed here is not part of the method; if a step needs one, mark it `[GAP]`. Drafts are the owner's canon awaiting ratification and are cited as drafts. All read on 19 October 2026.

| Source key | Document | Version and status |
|---|---|---|
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft awaiting ratification |
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L2 | Desired Outcomes (layer) | 3.3, 17 October 2026 |
| DR-0827 | Decision Record: ontology rulings | 1.0, ratified 27 August 2026 |
| FW-JT | Jobs-to-be-Done and Outcomes Framework | 3.0, canonical (conflicts noted below) |
| FW-VD | Value Driver Tree Framework | 3.0, canonical |
| CODE-VR | Navigator `value_range` rule | in code (`mcps/ontology_navigator/jobs.py`) |
| NAV-O | Navigator template `nav.outcomes` and the scoring engine | in code (`mcps/nav_engine/templates.py`, `compute.py`), version 1 |
| LANE | Read-only lane reports and Cowork reviews, 19 October 2026 | measured (M) |
| OWNER | Owner rulings in the Navigator skills workstream | 19 October 2026 |

## O1 Outcomes are the anchor; demand before supply

"Every walk shall reach at least one outcome before the work it leads to is counted" (GOV-06 6.2.3). "A capability, process, knowledge source, system or agent shall be included in the model because an outcome requires it" (GOV-06 6.2.4). EOS-L2 is "the anchor" and hands down "outcome demand to the Intelligence Core, solution-free" (EOS-L2, At a glance).

## O2 The outcome statement

"Each outcome shall be stated in the form of Annex B.1: a direction of change, an object of measurement and a context" (GOV-06 6.1.1). "A statement that cannot be written in this form is not yet an outcome" (GOV-06 B.1 c). Directions: minimize, maximize, increase, reduce, eliminate, maintain (FW-JT, Desired Outcome entity). Empty verbs are rejected (FW-JT rule JT-11: drive, transform, ignite, optimise, enable, establish, accelerate, foster, leverage, enhance). The object must be concrete enough that "two strangers would recognise the finished state in the same way" (FW-JT JT-11, concrete-object test).

## O3 The party

"Each outcome shall name the party for whom it must become true, such as a patient, a prescriber, a payer, a regulator or an internal role" (GOV-06 6.1.2). The party "is the holder of its perspective, not the worker who does it. Who does the work is decided in EOS-L3 and EOS-L4" (EOS-L2 §1; GOV-02 §9 `JobExecutor`, "perspective, not capacity"). The library has no party field (LANE); the party comes from the person.

## O4 Solution-free

"Outcomes shall be defined independently of current processes, capabilities, systems and agents. An outcome that names a solution shall be restated" (GOV-06 6.1.3). "The moment an outcome is defined by reference to an existing process or capability, it has lost its power to challenge what needs to change" (EOS-L2 §1). "JTBD declares WHAT, not HOW" (FW-JT JT-9). The restated solution is kept as an option for the Intelligence Core (skill practice, H).

## O5 Outcomes contribute to value drivers

"Each outcome shall be linked to at least one value driver. The link runs from the outcome to the value driver it contributes to" (GOV-06 6.3.1; GOV-00 R3). Say "contributes to"; the older edge names are retired (GOV-00 RUL-37). FW-JT still names an outcome-to-theme edge "Delivers"; the canon governs [noted for governance].

## O6 Levels and dimension

Five outcome levels: strategic, category, mission, job, atomic (EOS-L2 §2; GOV-00 OD-08). Every value assertion carries one of six dimensions (FW-VD §6). One opportunity score per outcome, its dimension taken from the linked value driver (OWNER, ruling 1, 19 October 
