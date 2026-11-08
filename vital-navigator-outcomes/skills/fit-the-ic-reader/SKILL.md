---
name: fit-the-ic-reader
description: >
  Fit Outcome Navigator outputs to IC memo, ops delivery note, or board one-pager: register, length, exhibit density. Adapted from TRUSTED fit-for-reader. Not for inventing content or cutting fluff substance (cut-the-slop).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "[CHECK] pending capability register lane"
  verb: fit
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Communication & Exhibits"
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
# Fit the IC reader

## Registers (locked)
| Register | Length guide | Exhibit density |
|---|---|---|
| IC memo | ~2–4 pages equivalent | 1–2 exhibits |
| Ops delivery | checklist + dependency | 1 dependency view |
| Board one-pager | one screen | 1 exhibit max + Endorse/Mandate/Supply/Hold |

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Confirm register with owner | none | human only |
| 2 | Reshape draft to register | compose-draft | agent alone |
| 3 | Owner accepts fit | none | human only |

## Pick the task
| Task | Guide |
|---|---|
| Choose register | `tasks/01-choose-register.md` |
| Reshape | `tasks/04-reshape.md` |


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

## What competent output looks like
- One-pager: decision, options, VAS with classes, risks, Endorse/Mandate/Supply/Hold asks.
- Working file not dumped as the cover.
- No invented “board-friendly” numbers.
- Integrity posture line present (Verify / not tool-checked).

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Identify reader (IC / board / ELT) | classify-text-labels | agent with review |
| 2 | Cut to one-pager structure | compose-draft | agent |
| 3 | Preserve gaps; refuse new facts | ground-the-numbers sibling | agent |
| 4 | Human accepts fit | — | human only |

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/reader_fit_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `reader` | IC, board, ELT, other | always |
| `one_pager.decision` | string | always |
| `one_pager.must_do (alias reader_must_do)` | non-empty string | always (V-C6-READER-01) |
| `one_pager.options` | list, at least 2 | always |
| `one_pager.value_at_stake {text, evidence_class}` | string, M/V/H/O/GAP | always |
| `one_pager.turns_on` | non-empty list | always |
| `one_pager.integrity_posture` | verified or not tool-checked | always |
| `one_pager.asks[] {type, request, who}` | Endorse/Mandate/Supply/Hold | always |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "reader": "IC",
  "one_pager": {
    "decision": "CMO decides the AI content path",
    "must_do": "Mandate a four-week time study before the vendor decision",
    "options": ["vendor", "internal", "do nothing"],
    "value_at_stake": {"text": "not quantified", "evidence_class": "GAP"},
    "turns_on": ["baseline"],
    "integrity_posture": "not tool-checked",
    "asks": [{"type": "Mandate", "request": "time study", "who": "Medical Excellence"}]
  }
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-004, LA-C6-005 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
