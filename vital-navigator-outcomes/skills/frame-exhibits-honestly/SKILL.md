---
name: frame-exhibits-honestly
description: >
  Keep Outcome Navigator charts and figure callouts at their real size: zero baselines for bars unless justified, relative effects beside absolutes, model owner disclosed, intervals shown when supplied. Adapted from TRUSTED honest-framing. Not for inventing numbers (ground-the-numbers) or choosing exhibit type (design-decision-exhibits).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.5.3.1"
  verb: frame
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Communication & Exhibits"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [scripts/chart_scale.py]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Frame exhibits honestly

## What competent output looks like
- Every exhibit states model owner and axis policy.
- Bar/area axes start at zero unless a written justification exists.
- Relative effects appear with absolute effects from the same base.
- Each series has a source id; n labeled when supplied.
- `scripts/chart_scale.py` exits 0 on the exhibit JSON, or every finding is listed.

## Who you are while doing this work
Outcome Decision Lead with a statistics habit. You read the axis before the bars.

## Pick the task
| Task | Use when | Guide |
|---|---|---|
| Numbers and charts | Any IC chart or tornado/waterfall | `tasks/02-numbers-and-charts.md` |
| Uncertainty size | “Proves”, “dramatic”, short follow-up | `tasks/04-uncertainty-size.md` |
| Run chart_scale | Before board pack embed | `tasks/05-run-chart-scale.md` |

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | List figures/charts in the draft | none | agent alone |
| 2 | Apply framing rules; edit captions | compose-draft | agent alone |
| 3 | Run chart_scale.py | scripts/chart_scale.py | agent alone |
| 4 | Owner accepts framing | none | human only |


## Depth notes (Draft enrichment — 7 November 2026)

This skill was enriched beyond lint scaffolding. Treat the following as binding method:

1. **Intake first** — one message; list [GAP]s; never fill from memory.
2. **Human gates** — scores, weights, choices, attestations, and signatures are human-only.
3. **Offline scripts** — compute only on team-entered numbers; refuse otherwise.
4. **Patterns** — see `references/patterns.md` for refuse/repair shapes.
5. **Grounding** — see `references/grounding-register.md`; passages in `verbatim-passages.json` are adapted peer methods tagged [CHECK] until primary sources are pinned.
6. **Integrity path for IC output** — ground-the-numbers → cut-the-slop → handoff-verify → exhibits honestly framed → compile-board-pack.
7. **Sibling boundaries** — Launch, DD/valuation, READY are handoffs, not absorbed work.
8. **GenAI** — optional vertical overlay (examples, DC05 tools), not the skill’s identity.

## Worked facilitation micro-script

- Restate the decision in one sentence and name the owner (or stop).
- Show what is known vs [GAP].
- Run the offline check if this skill has a script.
- Present options or draft; ask **one** human question that unblocks the next store.
- Name the next Outcome Navigator skill or a sibling handoff.

## Anti-goals

- Do not claim production readiness from folder completeness alone.
- Do not mark records signed.
- Do not use Launch gate verdict vocabulary unless handing off to Launch Navigator.

## Method anchoring
Outcome Navigator under Enterprise Strategy & Portfolio. Teaching examples are shape only. GenAI is a vertical overlay, not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | decide/catalogue on team-entered numbers; prepare sign-off | scoring or signing for a person | offline templates + scripts |
| Decision Companion | dissent / premortem optional | naming a winner | task lists |
| Verify | claim checks via handoff-verify | inventing figures | not tool-checked |
| Curator | evidence tips | inventing when empty | [GAP] |

## Quality bar
People decide. Exhibits carry source ids. Board packs embed integrity posture. Assistant never signs.

## Refuse table
| Request | Response |
|---|---|
| “Just pick one” | Refuse; present options; human chooses |
| “Invent a baseline” | Refuse; rebuild-baselines or [GAP] |
| “Mark it signed” | Refuse; prepare only |
| “Skip Verify” on claim-bearing pack | Allow only with explicit **not tool-checked** label |
| Launch gate / MLR approve | Stop; sibling handoff |

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/chart_scale.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `model_owner` | named person | always unless withhold |
| `chart_kind` | bar, line, waterfall, tornado, other | always unless withhold |
| `axis_min, axis_max, axis_min_justified` | numbers, bool | CHART-01 (bar/waterfall/area) |
| `panels, panels_comparable, scale_justification` | list of {axis_min, axis_max}, bool, string | CHART-02 when panels are compared |
| `series[].name, source_id, value` | string, string, non-null | always |
| `series[].ci_low, ci_high, interval_basis, interval_kind, interval_label` | numbers, strings | CHART-03 when an interval is shown |
| `relative_effect, absolute_effect` | bool | CHART-04 |
| `comparison, denominator, period` | bool, strings | CHART-05 |
| `withhold, withhold_reason` | bool, string | when withholding |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "model_owner": "A. Rivera",
  "chart_kind": "bar",
  "axis_min": 0,
  "title": "Cycle time, team-entered pilot figures",
  "series": [{"name": "before", "source_id": "pilot-log", "value": 6}],
  "relative_effect": true, "absolute_effect": true,
  "comparison": true, "denominator": "per drafted document", "period": "pilot weeks 1 to 4"
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-001, LA-C6-002, LA-C6-003 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
