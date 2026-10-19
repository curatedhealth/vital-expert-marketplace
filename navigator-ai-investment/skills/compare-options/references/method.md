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

Template `nav.capabilities`: Current (1 "Does not exist today", 10 "Fully in place today"); Required (1 "Not needed", 10 "Essential") (NAV-CAP). "gap = max(0, mean required − mean current), weighted by criticality." Criticality: a direct value if given; otherwise "the link-weighted mean of the outcome scores it serves (outcome scores are the Outcomes composites, so importance flows down)"; otherwise 1, marked default (NAV-CAP). Ranked by weighted gap, then gap, then id. The skill uses the attested opportunity scores from *Outcome Prioritization* as the outcome scores. The connector's capability gap tool does not pass outcome links, so every capability gets criticality 1 (LANE); the skill computes the outcome-weighted gap locally with the same formula.

## I6 Strategic and operational tiers

Strategic tier: the outcome-weighted capability gap (this stage). Operational tier: the capability maturity assessment, levels 1 to 5, in Execution (OWNER, 19 October 2026). Data readiness, change capacity and risk appetite have no instrument anywhere (LANE); they are named gaps until one exists.

## I7 Options and the baseline

Six criteria, whole numbers 1 to 10 (OWNER ruling R1, 19 October 2026: these become method; NAV-OPT): Outcome fit (1 "Does not deliver the outcome", 10 "Delivers the outcome fully"); Cost (1 "Very low cost", 10 "Very high cost", counted as a cost); Time (1 "Fast to deliver", 10 "Slow to deliver", cost); Reversibility (1 "Hard to reverse", 10 "Easy to reverse"); Risk (1 "Low risk", 10 "High risk", cost); Governance burden (1 "Light", 10 "Heavy", cost). A cost criterion counts as 11 minus the score; the composite is the weight-normalized mean, 1 to 10. All weights 1 by default; a weight change needs a reason and the unadjusted result is shown beside the adjusted one. Sensitivity: each scorer left out, each weight moved by −20% and +20%; "stable" when the leader never changes, otherwise "close call". Ties broken by median, then id (NAV-OPT). A baseline option ("nothing yet" or "do it internally") is required (NAV-OPT); the Standard requires the options to include doing nothing or doing it internally (GOV-06 A.4); these skills always carry both (OWNER R5). The engine ranks the baseline like any option and does not subtract it (LANE). OWNER ruling R5 (19 October 2026): the baseline is a reference line, not a contender; equal weights are kept; options are ranked among themselves and each shows its difference from each baseline; the skill explains which criteria carry the baseline. With equal weights, doing nothing scores well on five of the six criteria by construction (cheap, fast, reversible, low risk to start, light burden) and poorly on outcome fit; the room may change a weight only with a recorded reason (NAV-OPT).

## I8 The investment grid

Axes: value = the option's **Outcome fit** (group average from the option comparison), per OWNER ruling R4 (19 October 2026), replacing the engine's option composite (NAV-GRID), which counts cost and burden twice and places doing nothing in "Invest now". Baselines are never placed (OWNER R5). Second axis per OWNER ruling R2 (19 October 2026): **fit to capacity**, after ESSAY-03 Exhibit 15 ("Invest where the opportunity is high and the oversight fits your capacity"). The oversight an option needs is its Governance burden score; the oversight the organization can carry today is scored by named people, 1 ("Very little") to 10 ("A great deal") [anchors: skill wording, H]. An option is heavy when needed exceeds capacity; the engine runs this by passing capacity as its burden split. Value is high when at or above the value split (median of the options by default, or a split the owner states). With fewer than four options a median split puts half of them low by definition; the skill asks the owner for a split (H, skill practice).

| Value | Oversight | Bucket (spoken; OWNER ruling R3) | Code |
|---|---|---|---|
| High | Fits capacity | Invest now | invest_now |
| High | Above capacity | Build the basis first | codify_first |
| Low | Fits capacity | Later, in batches | harvest_later |
| Low | Above capacity | Not now | not_now |
| Any, consequence of error too high to delegate | — | Support, do not automate | augment_dont_automate (override; the underlying bucket is kept) |

"A decision aid, not a measurement. Placement on each axis is a scored judgment by named people, and the quadrant boundaries are a convention. The oversight axis is read from the context-of-use statement" (ESSAY-03). The grid is not a connector tool and the connector's placement call stores the caller's quadrant (LANE); the skill computes placement locally.

## I9 Lenses

Default lens value against oversight; further lenses: cost against benefit, capability against capacity (augmentation or automation play), productivity against differentiation, internal against external. A lens changes the view, never the ranking; lenses use only scores and tags people gave (OWNER, 19 October 2026). The play tags are stated to exist in the owner's database [O]; no lane has read them (LANE item 5).

## I10 AI intervention levels

Five levels: assist, augment, automate, orchestrate, redesign; they govern (DR-0827 Ruling 5; GOV-00 RUL-47); the process owner sets the level; EOS-L3's tree outputs automate, augment or assist; orchestrate and redesign are set at the outcome level (GOV-00 RUL-49). Compliance caps on outcome rows: very high compliance sensitivity allows assist at most; high allows augment at most (FW-JT rule JT-4, in the schema comment, LANE). The skills record a proposed level as the owner's, never set it.

## I11 Facilitated, then one report

One question per turn, then one full report (OWNER; references/facilitation.md).

## Conflicts noted

1. Record numbered keys in code differ from canon sections 4, 5, 6 (LANE). The skills follow the canon.
2. Two intervention vocabularies: RUL-47 names vs a seed file's AI01 to AI05 (LANE). The skills use RUL-47.
3. Three label sets for placement (essay, grid codes, standing option labels). The skills speak the essay names (OWNER R3).
4. The engine's grid takes the option composite as value; OWNER R4 sets Outcome fit. Register finding for the tools session.
