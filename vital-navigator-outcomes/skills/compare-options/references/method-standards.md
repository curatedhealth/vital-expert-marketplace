# Method standards: compare-options

| Id | Standard / practice | Status | How this skill uses it |
|---|---|---|---|
| MS-01 | Shared 10-part decision record (Launch Navigator design package 02; non-gate path) | [CHECK] | Outputs that feed close / board pack map to record parts; no launch_gate unless handed to Launch Navigator |
| MS-02 | People score; assistant never scores, weights, chooses or signs | [CHECK] | Scripts refuse without team-entered numbers; autonomy marks human-only gates |
| MS-03 | Evidence classes M / V / H; [GAP] never filled from model memory | [CHECK] | Intake and tasks leave unknowns visible |
| MS-04 | Offline first; connectors cited when used | [CHECK] | Connectors section in SKILL.md |


## Method notes

# Method: the rules the Intelligence Core skills apply

Shared by *Strategic Readiness*, *Option Comparison* and *Portfolio Placement*. Every rule carries its source, the version read and the date read. A rule not listed here is not part of the method; if a step needs one, mark it `[GAP]`. Drafts are cited as drafts. All read on 19 October 2026; code read by the cluster 3 inputs lane (HEAD e23025f6), reviewed PASS.

| Source key | Document | Version and status |
|---|---|---|
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft awaiting ratification |
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L3 | Intelligence Core (layer) | 3.6, canonical |
| DR-0827 | Decision Record: ontology rulings | 1.0, ratified 27 August 2026 |
| ESSAY-03 | One Code, Many Questions | draft v4.2, 17 October 2026 |
| NAV-OPT | Navigator template `nav.options` and the scoring engine | in code (`mcps/nav_engine/templates.py`, `compute.py`, `service.py`), version 1 |
| NAV-CAP | Navigator `nav.capabilities` template and `weighted_gap` | in code (`mcps/nav_engine/v2/templates.py`, `v2/weighted.py`) |
| NAV-GRID | `opportunity_governance_grid` | in code (`mcps/nav_engine/v2/grids.py`) |
| LANE | Cluster 3 inputs lane, 19 October 2026 | measured (M) |
| OWNER | Owner rulings in the Navigator skills workstream | 19 October 2026 |

## I1 What this stage answers

Intelligence Core answers "How should we act here?": it reads conditions, knowledge and rules and produces a design; it holds abstract capability requirements, never named actors (EOS-L3 At a glance; design rule 5: "EOS-L3 says 'this situation requires HEOR modeling competency.' EOS-L4 says 'assign this to Dr. Chen and the CEA Agent.'").

## I2 The record sections this stage drafts

"Section 4 Capability and gap register; section 5 Options considered, always including doing nothing or doing it internally; section 6 Recommendation and route" (GOV-06 Annex A.4; GOV-04 §7). Results: "Proceed · Investigate first · Handle it internally" (GOV-04 §9). "The calculator does not choose the result" (Navigator record annex, LANE). Gate 3: "record signed by two people, one of them the decision-owner" (GOV-04 §9); taken in cluster 6, not here.

## I3 How capabilities, options and outcomes are scored

"Outcomes, options and capabilities are scored with a documented multi-criteria method"; whole numbers on the template scale (Navigator 1 to 10), given privately by named people before discussion; equal weight; disagreement above a stated threshold flagged and recorded, never averaged away; "AI may compute, chart and check scores. It does not give them" (GOV-06 Annex B.2). Owner's view shown after the group's (GOV-06 6.1.5). The engine flags a spread of 3 or more and marks fewer than three scorers indicative (NAV-OPT).

## I4 Capability before performer; context before assignment

"Before a person or agent is assigned to work, the required capability shall be resolved, then the constraints on who may act shall be checked, then the person or agent shall be assigned, in that order" (GOV-06 6.5.3; GOV-02 §11.3). "Context must constrain applicability before capability is selected" (GOV-02 §11.3). A context-of-use declaration is made before AI is assigned to a decision point (GOV-06 6.6.1). At a critical point a qualified human decides; no intervention level overrides this (GOV-02 R-LINE).

## I5 The strategic capability gap (outcome-weighted)

Template `nav.capabilities`: Current (1 "Does not exist today", 10 "Fully in place today"); Required (1 "Not needed", 10 "Essential") (NAV-CAP). "gap = max(0, mean required − mean current), weighted by criticality." Criticality: a direct value if given; otherwise "the link-weighted mean of the outcome scores it serves (outcome scores are the Outcomes composites, so importance flows down)"; otherwise 1, marked default (NAV-CAP). Ranked by w
