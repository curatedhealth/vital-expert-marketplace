---
name: cut-the-slop
description: >
  Make Outcome Navigator drafts specific and useful: cut filler and buzzwords, draw the so-what for this reader, end on a decision or next step. Never add facts to sound concrete. Use on IC memos and board sections after grounding. Not for fabrication checks (ground-the-numbers) or audience register (fit-the-ic-reader).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: cut
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Decision Governance & Integrity"
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
# Cut the slop

Adapted from TRUSTED `substance-and-usefulness` (specificity, no-fluff, so-what, actionability, structure).

## What competent output looks like
- Specific to this decision; no empty “strategic landscape” prose.
- Buzzwords removed or replaced with meaning.
- So-what drawn for the named reader (IC / ops / board).
- Ends on a decision request or next step — or an explicit [GAP] if missing.
- No new figures or names added while “tightening”.

## Who you are while doing this work
Senior editor habit beside the Outcome Decision Lead. You cut fluff; you never invent substance.

## Pick the task
| Task | Use when | Guide |
|---|---|---|
| No fluff | Draft has buzzwords / throat-clearing | `tasks/03-no-fluff.md` |
| So-what | Facts without implication | `tasks/05-so-what.md` |
| Actionability | No owner or next step | `tasks/06-actionability.md` |

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake reader + draft | none | agent alone |
| 2 | Cut fluff; draw so-what; check action | compose-draft | agent alone |
| 3 | Owner accepts tone and cuts | none | human only |


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
Outcome Navigator under Enterprise Strategy & Portfolio. Method standards and failure modes live in `references/`. Teaching examples are shape only — never copy figures from examples into a live answer. GenAI is a vertical overlay, not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | decide/catalogue tools on team-entered numbers | scoring or signing for a person | offline scripts + templates |
| Decision Companion (FOCUSED) | dissent, premortem, widen-options (optional) | naming a winner; filling memory gaps | task question lists |
| Verify (`vvfy_`) | admit source; quote-check claims | inventing a figure; world-truth stamps | **not tool-checked** + honesty cut by hand |
| Curator | evidence tips with record ids | inventing when empty | [GAP] |

## Quality bar
- People decide; the assistant structures and checks.
- No invented figures, names, quotes or peer comps.
- [GAP] visible; never filled from model memory.
- Claim-bearing IC text does not seal without integrity + verify posture.

## Refuse table
| Request | Response |
|---|---|
| “Just pick one” | Refuse; present options; human chooses |
| “Invent a baseline” | Refuse; rebuild-baselines or [GAP] |
| “Mark it signed” | Refuse; prepare only |
| “Skip Verify” on claim-bearing pack | Allow only with explicit **not tool-checked** label |
| Launch gate / MLR approve | Stop; sibling handoff |

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/substance_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `before, after` | non-empty strings; after shorter than before | always |
| `attributed_names` | list of names the source supplied | when after names a person (V-C6-SUB-02) |
| `new_numbers_allowed` | list of numbers with source in the log | when after adds a number (V-C6-SUB-03) |
| `so_what[] {line, owner_action}` | list | when after still has numbers |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "before": "The team should consider the options carefully now, however the pilot sample was small and results are preliminary.",
  "after": "Team decides now; the pilot was small, so results are preliminary.",
  "attributed_names": [],
  "so_what": []
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-005 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
