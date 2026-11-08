# Ontology DCs by cluster (owner ruling, 20 October 2026)

Closes open item E2. Do not invent free "Augment / Automate" tags. Use the live Notion / substrate dictionaries below.

| Cluster | Spoken name | Skills | Ontology DC in play |
|---|---|---|---|
| 1 | Direction: Decision & Value Framing | frame-the-decision, size-value-at-stake | **DC06** Value Dimensions |
| 2 | Outcomes: Outcome Discovery & Prioritization | discover-outcomes, prioritize-outcomes | **DC06** Value Dimensions and **DC05** AI Intervention Levels |
| 3 | Intelligence Core: Investment Choice | assess-strategic-readiness, compare-options, place-the-portfolio | **DC05** AI Intervention Levels |
| 4 | Execution: Delivery Planning | plan-the-delivery, design-the-trial, plan-capability-building | **DC09** AI Execution Modes |
| 5 | Organizational Learning (when measuring) | track-value-realized, review-the-portfolio | **DC06** Value Dimensions |
| 6 | Close | close-the-decision | No new DC; the record inherits what earlier clusters stored |

## Dictionaries (spoken names)

**DC06 — Value Dimensions.** The value axes on drivers and outcomes (Financial, Operational, Clinical, Risk, Capability, Strategic, and siblings in the catalogue). Cluster 1 and 2 use them to frame and score. Cluster 5 places realized value on the same axes used when the range was declared.

**DC05 — AI Intervention Levels** (ASSIST → AUGMENT → AUTOMATE → ORCHESTRATE → REDESIGN; codes AIL-01…AIL-05). How much AI is involved for an outcome or option. Cluster 2 reads linked JT/PH levels when the library has them. Cluster 3 places options on this ladder. Substrate FKs use `dc05_ai_intervention_levels` (AI01…AI05) and `*_dc05_links`; speak the Notion names, not the substrate codes, unless a person asks for the code.

**DC09 — AI Execution Modes** (Full Automation, Agent-Driven, Agent-Primary, Human-Led, Human-Only; codes AEM-01…AEM-05). Who initiates and who executes. Cluster 4 only. Do not collapse this into DC05: a job can be AUGMENT (DC05) and still Human-Led (DC09).

## Hard don'ts

- Do not invent session-only Augment/Automate tags.
- Do not use CF01–05 `ai_augmentation_*` / `ai_automatable` fields as the investment taxonomy; those stay capability-side.
- Do not speak DC09 tiers in clusters 1–3, or DC05 as the delivery oversight vocabulary in cluster 4.
- A missing library link is `[GAP]`, never a guessed level or mode.
