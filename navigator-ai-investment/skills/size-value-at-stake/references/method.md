# Method: the rules this skill applies

Every rule carries its source, the version read and the date read. A rule not listed here is not part of the method; if a step needs one, mark it `[GAP]`. Drafts are the owner's canon awaiting ratification and are cited as drafts. All read on 19 October 2026.

| Source key | Document | Version and status |
|---|---|---|
| GOV-00 | Outcome-Driven Ontology Framework | 0.12, draft awaiting ratification |
| GOV-02 | Outcome-Driven Ontology Blueprint | 4.8, canonical |
| GOV-04 | Canon of Names and Glossary | 1.9-draft |
| GOV-06 | Outcome-Driven Ontology: The Standard | 0.6-draft |
| EOS-L1 | Strategic Direction | 3.2, canonical |
| FW-VD | Value Driver Tree Framework | 3.0, canonical |
| NAV-V2 | Navigator template `nav.value_drivers` | in code (`mcps/nav_engine/v2/templates.py`), no version field |
| CODE-VR | Navigator `value_range` rule | in code (`mcps/ontology_navigator/jobs.py`) |
| LANE | Read-only lane reports and Cowork reviews, 19 October 2026 | measured (M) |
| OWNER | Owner rulings in the Navigator skills workstream | 19 October 2026 |

## V1 Value is declared, then proven

"A value driver states why an outcome matters. Outcomes contribute to value drivers; this is the one direction of that link everywhere in the canon. Value is counted only when the outcome is measured as achieved. A promised value is a hypothesis until it is measured" (GOV-00 R3). "Value is declared at the top and proven at the bottom" (GOV-02 §6, EOS-L1).

## V2 A range, with assumptions, and the cost of a wrong decision

"Expected value shall be stated as a range with its assumptions. Value shall be counted as realized only when the outcome is measured as achieved" (GOV-06 6.3.2). Decision Record section 2: "Value at stake: a range, and the cost of a wrong decision" (GOV-04 §7). The Navigator refuses a point: low, mid and high are required, low and high must differ, unit and basis are required, and each measure passed needs a baseline and an owner (CODE-VR, read by LANE). The skill adds two checks of its own, labeled as such: low is not above likely, and likely is not above high (H, ordinary consistency).

## V3 Sourced numbers only

"A figure taken from outside the organization shall name its primary source. A figure that cannot be traced to a primary source shall not be used" (GOV-06 6.4.3). "A claim made in one document shall not be used as evidence for a claim in another until it has been re-established" (GOV-06 6.4.2). Evidence classes M, O, H, V on every claim (GOV-00 R4); a room view is O, never M (GOV-00 R14).

## V4 Every outcome reaches a driver

"Each outcome shall be linked to at least one value driver. The link runs from the outcome to the value driver it contributes to" (GOV-06 6.3.1). The link is named "contributes to"; the older edge name is retired (GOV-00 RUL-37, per LANE). "Every walk ... MUST connect to at least one outcome before it counts" (GOV-00 R1).

## V5 The value driver tree and its dimensions

The tree runs in five levels from themes (01) to metrics (05) (FW-VD §3). Every value assertion is dimensioned in one of six dimensions: financial, operational, clinical or scientific, risk, capability, strategic (FW-VD §6). "VD holds levers, VP holds instruments": unit, baseline, target and thresholds live with performance measures, not on the driver (FW-VD §8). Value rolls up through the Value Compounding Formula (FW-VD §7; D43); no tool computes it today (LANE), so this skill declares a range and does not compute a roll-up.

## V6 How drivers are compared

Four criteria, scored by people 1 to 10: size of the prize (1 "Small effect on the organization", 10 "Large effect on the organization"); confidence in the estimate (1 "A guess", 10 "Well evidenced"); time to value (1 "Value arrives quickly", 10 "Value arrives slowly", counted as a cost); breadth (1 "Touches one group", 10 "Touches many groups") (NAV-V2). The engine method there is a weighted sum; the connector's scoring tool cannot run this template today (LANE). The skill computes an equal-weight average with time to value inverted, labeled "computed" [CHECK against the engine's weighted-sum normalization when the tool is fixed].

## V7 Audience calibration

C-suite starts at value themes, head of department at levers and drivers; within Direction the range is levels 1 to 3 (OWNER). Head of function at levers is inferred (H) [CHECK with owner].

## V8 How people score

"People give every score; AI may compute, chart and check, never score. Every scorer carries equal weight by default" (GOV-00 R11). Scores "given by named people, privately and before they are discussed" (GOV-06 6.1.4); the owner's view shown after the group's (GOV-06 6.1.5); dissent "flagged and recorded, never averaged away" (GOV-00 R6).

## V9 Direction holds goals; outcomes hold objectives

Direction works on strategic goals; measurable objectives are outcomes with their measures (OWNER, 19 October 2026). Numeric targets go to the outcome work.

## V10 Facilitated, then one report

One question per turn, then one full report (OWNER, 19 October 2026; references/facilitation.md).
