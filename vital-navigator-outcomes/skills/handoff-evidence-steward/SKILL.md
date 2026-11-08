---
name: handoff-evidence-steward
description: >
  Hand external V figures to Curator / evidence steward with record-id expectations. Do not invent tips when the store is empty. Not for Verify quote-check (handoff-verify).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Connectors optional; without them label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.5.8.1"
  verb: handoff
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Decision Governance"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: []
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Handoff evidence steward

## What competent output looks like
- Packet: figure, claimed class V, requested Curator fields {record_id, version, grade}.
- Empty store → [GAP], never a fabricated tip.
- Clear return path into size/track or board evidence appendix.

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | List external V figures needing stewardship | none | agent alone |
| 2 | Build Curator handoff packet | compose-draft | agent alone |
| 3 | Call Curator if available else [GAP] | Curator via Navigator | agent alone |
| 4 | Owner accepts gaps | none | human only |


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
Outcome Navigator. Teaching examples are shape only. GenAI is one vertical.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | context | deciding for the person | offline worksheets |
| Sibling plugins | handoff targets | absorbing their work | name plugin and stop |
| Verify / Curator | later integrity / evidence | at entry routing | n/a |

## Quality bar
Route honestly. Do not absorb Launch, DD, Valuation or READY work. People own scores and baselines.

## Refuse table
| Request | Response |
|---|---|
| “Just pick one” | Refuse; present options; human chooses |
| “Invent a baseline” | Refuse; rebuild-baselines or [GAP] |
| “Mark it signed” | Refuse; prepare only |
| “Skip Verify” on claim-bearing pack | Allow only with explicit **not tool-checked** label |
| Launch gate / MLR approve | Stop; sibling handoff |

## Competent output (assessable)
- Every number is team-entered or `[GAP]`; never invented.
- Human gates name the deciding role; assistant does not score, weight, choose or sign.
- Offline scripts run only on supplied inputs; soft issues become flags.
- Deliverable uses the skill templates; open items listed; next skill or sibling handoff named.
- Not covered work (Launch / DD / READY chairs) is refused with a named route.

## Method anchoring
Each judgement cites a method-standards id (MS-*) or is marked `[CHECK]`. Failure modes are screened before release of claim-bearing text.

## Connector use
Offline first. Live connectors, when used, are cited with access date. Claim-bearing packs without Verify are labeled **not tool-checked**.

## Quality bar (release of this skill's draft)
1. Intake gaps visible
2. Tasks complete in order
3. Script exit 0 or explained flags
4. Examples' teaching figures not copied live
5. Governance human gates respected

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/steward_handoff_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `store_available, store_gap_acknowledged` | bool | always; acknowledgment required when store is false |
| `items[].title, evidence_class` | string, M/V/H/O | always |
| `items[].source, source_date or gap` | strings | source or gap text required |
| `items[].derived_from or lineage; responsible_party` | non-empty strings | item has a source (V-C6-STEWARD-01) |
| `items[].version` | exact string, not a floating label | when versioned (V-C6-STEWARD-02) |
| `items[].reuse_cleared, rights_basis` | value, string | reuse_cleared true needs rights_basis (V-C6-STEWARD-05) |
| `items[].steward_id, minted_ids` | null; empty | always null / empty |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "store_available": false,
  "store_gap_acknowledged": true,
  "items": [{
    "title": "HR roster headcount", "evidence_class": "V",
    "source": "HR extract 2025-10-01", "source_date": "2025-10-01",
    "derived_from": "HR system export, writers cost center",
    "responsible_party": "People Analytics (named lead)",
    "version": "2025-10-01", "steward_id": null
  }]
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-008, LA-C6-009 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
