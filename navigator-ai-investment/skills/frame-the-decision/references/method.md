# Method: the rules this skill applies

Every rule below carries its source, the version read and the date it was read. A rule not listed here is not part of the method; if a step needs one, mark it `[GAP]`. Governance documents marked "draft" are the owner's canon awaiting ratification; they are cited as drafts.

All read on 19 October 2026 from the VITAL canon (repository `docs/corpus/`) and the Ontology Navigator project.

| Source key | Document | Version and status |
|---|---|---|
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft awaiting ratification |
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L1 | Strategic Direction (Enterprise OS layer 1) | 3.2, canonical |
| FW-VD | Value Driver Tree Framework | 3.0, canonical |
| VITAL-M | VITAL Method | 0.1, draft |
| DL-CAT | Discovery Lab Service Catalogue | 0.1, project document |
| NAV-T | Navigator scoring templates, `nav.sizing` | version 1, in code (`mcps/nav_engine/templates.py`) |
| OWNER | Owner rulings in the Navigator skills workstream | 19 October 2026 |

## M1 The four clarifying questions

"What is the decision? · Who is accountable? · What does a wrong decision cost? · What do you already know?" (GOV-04 §9, class O). The first moment of a session asks them before anything is scored; the decision owner then signs the Decision Contract, Gate 1 (DL-CAT §3.1; GOV-04 §9 "Gate 1 Decision Contract").

## M2 A decision is intent, not a solution

"Typical failure: Direction written as solutions ('deploy a new CRM') rather than intent" (EOS-L1, At a glance). Outcomes "shall be defined independently of current processes, capabilities, systems and agents. An outcome that names a solution shall be restated" (GOV-06 6.1.3). Options always include "doing nothing or doing it internally" (GOV-04 §7, section 5). The facilitator proposes a reframed decision statement; "the client owns it" (DL-CAT §3.1).

## M3 One named, accountable person decides

"At every critical gate-classified decision point, AI drafts, assembles, analyzes and recommends, and a qualified, named human decides and accepts responsibility" (GOV-00 R5). Decision Record section 1: "The decision — one sentence, who signs, by when, how reversible" (GOV-04 §7).

## M4 Direction orients; outcomes anchor

"Direction is the input that sets the course; outcomes are what every path must reach" (GOV-00 R2). "Every walk ... MUST connect to at least one outcome before it counts" (GOV-00 R1). EOS-L1 answers "Why does this matter?" and holds "the value drivers that say why an outcome matters" (EOS-L1, At a glance). "Value is declared at the top and proven at the bottom" (GOV-00 R3).

## M5 Goals in Direction; objectives in Outcomes

Owner ruling, 19 October 2026 (OWNER, class O): Direction works on strategic goals, not strategic objectives. Measurable objectives are expressed in Outcomes as jobs to be done with their performance measures. If no goal is stated, ask for one sentence and record it as owner-stated; do not refuse and do not invent.

Note: EOS-L1 v3.2 still lists "StrategicObjective" as a Direction entity. The owner ruling governs this skill; the canon owner has been notified. [CHECK when EOS-L1 is next revised]

## M6 The format matches the decision

"The format matches the decision, not the budget" (DL-CAT §3.0; VITAL-M §2). The stage "is set in the first moment by the decision sizing score: stakes, reversibility, how long the decision commits the organization, and how many functions it involves" (DL-CAT §3.0, class H built on V). Signals, as written there:

| Signal | Points to |
|---|---|
| One decision, one function, reversible, the team mostly knows the ground | Ignite (a short working session) |
| One decision that matters, several functions have a view, costly to reverse | Catalyst (one day) |
| Several connected decisions, many functions, hard to reverse, several years of commitment | Accelerate (several days) |
| The organization itself has to change | Transform (a program) |

"The facilitator may recommend a different stage than the client asked for, including a smaller one. That recommendation is recorded" (DL-CAT §3.0). The catalogue sets no numeric thresholds; the skill gives the matching signal and the owner decides. [GAP: no numeric mapping from sizing composite to stage exists in the canon.]

Sizing criteria and anchors (NAV-T, `nav.sizing`, version 1): stakes (1 "A wrong call is cheap", 10 "A wrong call is costly for the organization"); reversibility (1 "Very hard to reverse", 10 "Easy to reverse", counted as cost: 11 minus the score); commitment horizon (1 "A few weeks", 10 "Several years"); functions involved (1 "One function", 10 "Many functions"). Engine: weighted mean, equal weights.

## M7 When outcome scores need a field test

"A field test of the top outcomes MUST precede the decision when all three hold: (a) the decision is hard to reverse; (b) it commits money or people beyond one planning cycle, or across more than one function; (c) it rests on top-ranked outcomes scored only in the room ... The decision owner MAY proceed without the test by recording the reason" (GOV-00 R14A; GOV-06 6.1.7). This skill establishes (a) and (b) with the owner; (c) is checked in outcome prioritization.

## M8 How people score

"People give every score; AI may compute, chart and check, never score. Every scorer carries equal weight by default; any change to a weight carries a logged reason" (GOV-00 R11). "Scores shall be given by named people, privately and before they are discussed" (GOV-06 6.1.4). "The decision owner's own view should be shown beside the group's scores, and only after the group's scores have been revealed" (GOV-06 6.1.5). "In scoring, dissent is flagged and recorded, never averaged away" (GOV-00 R6). Navigator templates use "whole numbers 1 to 10, given privately before discussion" (GOV-04 §9). "Scores from a small group are marked indicative" (DL-CAT §3.1); the skill treats fewer than three scorers as a small group. [CHECK: the catalogue gives no number]

## M9 Evidence classes

"Every claim ... MUST carry its evidence class: M measured, O owner-stated, H hypothesis, V asserted by a document" (GOV-00 R4). A room view is O, never M (GOV-00 R14).

## M10 Audience calibration of value drivers

Owner ruling, 19 October 2026 (OWNER, class O): the facilitator sets the starting level of value drivers from the audience. CEO and C-suite start at value themes (VD01); head of department at value levers and drivers (VD02 to VD03). Within Direction the range is VD01 to VD03. The head-of-function row (VD02) is inferred from the platform's seniority ladder (class H) [CHECK with owner]. The value driver tree runs from themes to metrics across five levels (FW-VD §3).
