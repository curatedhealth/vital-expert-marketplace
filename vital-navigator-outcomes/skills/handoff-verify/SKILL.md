---
name: handoff-verify
description: >
  Hand claim/source checks to VITAL Verify. Build a claim packet; call qualify_source then check_claim when vvfy_ is present; otherwise label not tool-checked and run the honesty cut by hand. Never mark a claim supported in this skill. Not for grounding arithmetic (ground-the-numbers) or Curator tips (handoff-evidence-steward).
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator add cited live data when present; otherwise label not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.5.7.1"
  verb: handoff
  capability: "[CHECK] Outcome Navigation (Enterprise Strategy & Portfolio)"
  mission: "6 Decision Governance & Integrity"
  agent: outcome-navigator-agent
  atoms: [compose-draft]
  requires: []
  feeds: []
  tools: [Verify qualify_source, Verify check_claim]
  version: "0.2.2"
  release_state: Draft
  pack: "vital-navigator-outcomes"
  depth: method-authored
---
# Handoff to Verify

Pattern from FOCUSED `handoff-verify` + VERIFY `honesty`. This skill does **not** decide support.

## What competent output looks like
- A claim packet: sentence, place in draft, candidate URL/DOI/upload, quoted passage slot.
- With `vvfy_`: qualify_source then check_claim; statuses returned as tool results only.
- Without `vvfy_`: every result labeled **not tool-checked**; unsupported specifics removed (honesty).
- No “verified true” / “cleared” language. No invented Verify status.

## Who you are while doing this work
Outcome Decision Lead preparing evidence for IC. You refuse to bless a guess.

## Pick the task
| Task | Use when | Guide |
|---|---|---|
| Build packet | Claims need checking | `tasks/01-build-packet.md` |
| Call Verify | Packet ready and vvfy_ present | `tasks/04-call-verify.md` |
| Honesty cut offline | No vvfy_ | `tasks/06-honesty-cut-offline.md` |

## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Build claim packet from draft | compose-draft | agent alone |
| 2 | qualify_source → check_claim OR honesty cut | Verify tools | agent alone |
| 3 | Present findings; owner decides what to keep | none | human only |


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

`scripts/verify_handoff_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `verify_status` | verified, not tool-checked, claims_removed | always |
| `circulation` | internal_only, external_blocked, external_ok | always |
| `author_role or preparer; assurance_role or assurer` | distinct non-empty strings | verified or external_ok (V-C6-VERIFY-04) |
| `claims[].id, text, tool_checked` | string, string, bool | always unless claims_removed |
| `claims[].source_revision or passage` | non-empty string; at least one | verified or external_ok; any tool_checked claim (V-C6-VERIFY-06) |
| `assured_revision, current_revision` | strings; must match | when assurance is renewed (V-C6-VERIFY-05) |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "A. Rivera",
  "verify_status": "verified",
  "circulation": "internal_only",
  "author_role": "Analyst, Medical Excellence",
  "assurance_role": "Reviewer, Evidence Office",
  "assured_revision": "r4", "current_revision": "r4",
  "claims": [{"id": "C1", "text": "Drafting takes half of writer time", "tool_checked": true,
              "source_revision": "time-study-q3@v2", "passage": "Writers logged 50 percent of hours on drafting."}]
}
```

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-006, LA-C6-010 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
