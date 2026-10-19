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

Five outcome levels: strategic, category, mission, job, atomic (EOS-L2 §2; GOV-00 OD-08). Every value assertion carries one of six dimensions (FW-VD §6). One opportunity score per outcome, its dimension taken from the linked value driver (OWNER, ruling 1, 19 October 2026). FW-JT's per-dimension scoring with strategic weights is not used here [noted for governance].

## O7 Goals in Direction, objectives in Outcomes

Direction works on strategic goals; measurable objectives are outcomes with their measures (OWNER, 19 October 2026). EOS-L2 owns "measurable objectives and targets" (GOV-02 §6 EOS-L2). Measures (unit, baseline, target) live with performance measures, not on the driver or the outcome name (FW-VD §8).

## O8 Measured, not asserted

Value "shall be counted as realized only when the outcome is measured as achieved" (GOV-06 6.3.2). An outcome is met "when its associated evaluation passes ..., not when an output merely exists" (GOV-02 R-MEASURE). The Navigator refuses a measure without a baseline and an owner when storing a value range (CODE-VR via LANE). The measure library holds 25 headline metrics, 163 category measures and 709 measures, with 5 baselines at the finest level and no owners (LANE, M).

## O9 Audience calibration

C-suite starts at strategic and category outcomes; head of function at category; head of department at category and mission (OWNER, 19 October 2026). Within the Outcomes stage of an investment decision, stop at mission level; job and atomic outcomes belong to execution design (OWNER).

## O10 How outcomes are scored

"Outcomes shall be prioritized by a documented multi-criteria method (Annex B.2). Scores shall be given by named people, privately and before they are discussed. Each scorer's weight shall be equal" (GOV-06 6.1.4). Whole numbers on the template scale, 1 to 10 in the Navigator; "AI may compute, chart and check scores. It does not give them" (GOV-06 B.2 b, f). Template `nav.outcomes`: Importance (1 "Not important", 10 "Critically important"); Satisfaction with today (1 "Not satisfied at all", 10 "Fully satisfied") (NAV-O).

## O11 One opportunity formula

"Opportunity = Importance + max(0, Importance − Satisfaction)" (GOV-06 B.2 e; DR-0827 Ruling 4, ratified; GOV-00 R11). On 1 to 10 inputs the score runs 1 to 19. EOS-L2's older "(I − S) × I" is superseded. The engine computes the group score from the mean importance and mean satisfaction and also reports the median of each scorer's own opportunity (NAV-O). Bands reported by the engine: extreme 15 and above, strong 12 to under 15, moderate 10 to under 12, low under 10 (NAV-O). The single-score tool uses different words (underserved 15 and above, overserved under 10) (LANE); the skill uses the engine's bands.

## O12 Bands describe; people decide

No automatic invest threshold (OWNER, ruling 2, 19 October 2026). FW-JT's "IF Composite > 10 THEN invest" is not applied [noted for governance]. A band says how underserved an outcome looks to the room; it does not choose.

## O13 Owner's view, disagreement, sensitivity

The owner's view is shown beside the group's, "only after the group's scores have been revealed" (GOV-06 6.1.5). Disagreement "above a stated threshold is flagged and recorded in the dissent field; it is never averaged away" (GOV-06 B.2 d; GOV-00 R6). The engine flags a spread of 3 or more on either criterion, marks fewer than three scorers as indicative, and drops each scorer in turn to see whether the leader changes ("stable" or "close call") (NAV-O). Thresholds (OWNER, 18 October 2026, open-items register item 54): dissent flag at a spread of 3 or more; strong disagreement at a spread of 4 or more on a top-five outcome; a flip is a change in the first-ranked outcome; "beyond one planning cycle" means beyond the client's own budget cycle. The skill's script also reports changes in the top set and the order below the leader, as information, not as a trigger.

## O14 Where a score came from, and the field test

"Every outcome score shall state where it came from: scored in the room by named people, or field-verified by measurement with the people the outcome is for. A room score shall not be presented as a measured result" (GOV-06 6.1.6; GOV-02 R-PROVENANCE). "A field test of the top outcomes shall precede the decision when the Decision Record states that the decision is hard to reverse, commits money or people beyond one planning cycle or across more than one function, and rests on top-ranked outcomes scored only in the room. A field test shall also precede it, whatever its size, when scorers strongly disagreed on a top outcome or the ranking changes under the sensitivity check. The test should be proportionate: a short check of the top three to five outcomes. Where field and room disagree, the disagreement shall be recorded as dissent. The decision owner may proceed without the test by recording the reason in the record" (GOV-06 6.1.7; GOV-00 R14A). A field reference records who was asked, how many, and when (GOV-02 §9). The test covers the top five by default (OWNER thresholds, O13). No field-test check exists in the connector's code (LANE).

## O15 Gate 2: priorities attested

Session gates: "Gate 1 Decision Contract · Gate 2 priorities attested · Gate 3 record signed by two people, one of them the decision-owner" (GOV-04, Gates). A gate is well-formed only if it presents the evidence trail, binds a named, qualified reviewer, offers dissent as a structured act, and records the decision with responsibility (GOV-02 R-GATE). Gates 1 to 3 of a decision session are always critical (GOV-02 §11.3). The connector has no Gate 2 function (LANE); the attestation is taken in conversation and recorded in the report.

## O16 Who sets the intervention level

Whether AI should assist, augment, automate, orchestrate or redesign is decided against the outcome, by the process owner, using the five intervention levels (EOS-L2 §11 rule 4; DR-0827 Ruling 5). It is not set in the Outcomes skills; it is carried to the Intelligence Core stage as an open question.

## O17 Facilitated, then one report

One question per turn, then one full report (OWNER, 19 October 2026; references/facilitation.md).

## Conflicts noted for the governance workstream

1. FW-JT stores importance and satisfaction on 0 to 10 decimals; the Navigator and GOV-06 use whole numbers 1 to 10. The skills follow the Navigator.
2. FW-JT's "invest when composite above 10". Not applied (O12).
3. FW-JT's "Delivers" edge from outcome to theme. "Contributes to" governs (O5).
4. FW-JT multi-dimensional weighted ODI. One score per outcome governs (O6).
5. The two connector scoring tools use different band names (O11).
