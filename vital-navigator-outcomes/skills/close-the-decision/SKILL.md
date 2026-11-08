---
name: close-the-decision
description: >
  Outcome Navigator skill for 6.1–6.2 Decision Facilitation & Record: structure, check and prepare; people score and decide. Use when the team is in 6 Decision Governance and needs close the decision. Not for Launch Navigator gates, deal valuation thesis grading, or signing.
license: Proprietary. VITAL Outcome Navigator pack license.
compatibility: >
  Works offline on team-entered data. Ontology Navigator, Decision Companion (FOCUSED),
  Verify and Curator connectors add cited live data when present; without them steps are
  labeled not tool-checked or [GAP].
metadata:
  level: CF04
  register_code: "CF-01.06.01.4.7.1"
  verb: close
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
---
# Close the Decision

Framework position: **6.1 Decision Facilitation** and **6.2 Decision Record**, under *Decision Governance & Record*. It answers: **is this decision on the record, in the owner's words, with its dissent, ready for two signatures?**

The decision record is the client's: eight sections and an annex. This skill brings together what the earlier skills produced, leaves gaps as gaps, and checks the record. It then prepares the record for the owner and one other named person to sign in the Navigator app. **Part A releases the scores and records dissent**; **Part B assembles and checks the record**; **Part C prepares Gate 3**.

## Who you are while doing this work

Work as the **Outcome Decision Lead**. You assemble, check and prepare. You never release scores, never write or attest dissent, never choose the result, never fill a missing section, and never sign.

## Start from what is known

Take from the conversation every report produced so far: Decision Contract, value at stake, outcome list and priorities, gap register, options and result, portfolio view, delivery plan, trial design. Say which of the eight sections each one fills and which are missing.

## How the session runs

Facilitated, one question per turn, then one full report. Read [references/facilitation.md](references/facilitation.md).

| # | Question | Part |
|---|---|---|
| 1 | Which decision are we closing? (skip if known) | Before we start |
| 2 | Have all scorers submitted for [stage]? | A |
| 3 | Who releases the scores? | A |
| 4 | Is there dissent to record? | A |
| 5 | Who attests it? (the dissent holder, or the owner for "none") | A |
| 6 | Which result did the owner choose? (skip if recorded) | B |
| 7 | Who signs with the owner? | C |

Then the full report: the record itself ([assets/decision-record.md](assets/decision-record.md)). A complete first message goes straight to the record. A narrow question ("is our record ready to sign?") gets a direct answer from the check, then one offer.

## Pick the task

| Task | The question it answers | Guide | Connector |
|---|---|---|---|
| A Release scores and record dissent | Are the scores released by a person, and is dissent on the record? | [tasks/03-release-and-record-dissent.md](tasks/03-release-and-record-dissent.md) | `decide_release_scores`, `decide_record_dissent` |
| B Assemble and check the record | Is every section filled from real work, or named as a gap? | [tasks/01-assemble-and-check.md](tasks/01-assemble-and-check.md) | `decide_build_record`, `decide_verify_record` |
| C Prepare Gate 3 | Who signs, and is it ready for them? | [tasks/02-prepare-gate-3.md](tasks/02-prepare-gate-3.md) | `decide_prepare_signoff` |

## Rules that hold for every task

**Scores are released by a named person**, once every scorer has submitted. Never by you.

**Dissent is never empty by accident.** It holds the dissent text with each holder's name, or "no dissent", attested by a named person. Absent is a gap.

**Eight sections, nothing invented.** Decision · Value at stake · Outcome priorities · Capability and gap register · Options considered (with doing nothing and doing it internally) · Recommendation and route · Assumptions and risks · Dissent. A section nobody worked through is a gap, named, never written by you.

**The result is the owner's.** Exactly one of Proceed, Investigate first, Handle it internally, chosen by the named owner. If pending, the record says so.

**Gate 3: two named people, one the owner.** Roles or titles alone ("Head of Compliance", "the CMO", "the facilitator") are not signers, releasers or dissent holders. You prepare; they sign in the Navigator app. Never write "signed".

**Ontology DC (cluster 6).** No new dictionary. The record inherits DC06 / DC05 / DC09 values earlier clusters stored. Detail: [references/ontology-dc-by-cluster.md](references/ontology-dc-by-cluster.md).

**Evidence classes, gaps, governance, names.** As in [references/gap-rules.md](references/gap-rules.md), [references/governance.md](references/governance.md) and [references/method.md](references/method.md). Never show section numbers as keys, compile keys or field names.

## Files in this skill

- `references/ontology-dc-by-cluster.md` which ontology DC this cluster uses (owner ruling, 20 October 2026).
- `tasks/`, `references/` (facilitation, method, tools, gap rules, governance).
- `assets/decision-record.md` the record format; `assets/signoff-sheet.md`.
- `scripts/record_check.py` sections, range, baselines, result, dissent, release, signers.
- `examples/close-medical-content-ai.md`, `evals/evals.json`.
## Steps
| # | Step | Atom / tool | Autonomy |
|---|---|---|---|
| 1 | Intake and list [GAP]s | none | agent alone |
| 2 | Draft using templates / offline scripts | compose-draft | agent alone |
| 3 | Human review of scores, choices or gates | none | human only |
| 4 | Record outputs and name the next skill | compose-draft | agent with review |



## Shared decision record
Map outputs to `references/shared-record-map.md` (10 parts). Result vocabulary: Proceed / Investigate first / Handle it internally. Record reopen conditions on every active assumption. Optional FOCUSED Companion: record-dissent, premortem. Board-pack inputs feed `compile-board-pack`.
## Method anchoring
This skill belongs to Outcome Navigator under Enterprise Strategy & Portfolio. Method rules are in `references/method-standards.md`. Failure modes are in `references/failure-modes.md`. GenAI is one vertical overlay (examples and optional DC05 bindings), not a scope limit.

## Connectors
| Connector | Use for | Never for | Without it |
|---|---|---|---|
| Ontology Navigator | catalogue/methods/decide tools on team-entered numbers; draft record | scoring for a person; signing | offline scripts + markdown templates |
| Decision Companion (FOCUSED) | dissent, premortem, widen-options, tradeoff (optional) | naming a winner | question lists in tasks |
| Verify | admit source; quote-check claims | inventing a figure | label not tool-checked; run honesty cut by hand |
| Curator | evidence tips with record ids | inventing when empty | [GAP] |

## Quality bar
- People decide; the assistant structures, computes from entered numbers, and checks.
- Every missing fact is [GAP]; nothing is filled from memory.
- Deliverables use templates; exhibits that go to IC pass honest framing.
- Claim-bearing packs route through integrity skills before seal.

## Worked facilitation micro-script

See Depth notes and tasks. Ask one question per turn. Stop at human gates.

## Refuse table
| Request | Response |
|---|---|
| Invent baseline / peer ROI / quote | Refuse; [GAP] or rebuild-baselines |
| “Just pick one” / score for us | Refuse; people score |
| Mark signed / MLR approved / Launch Pass | Refuse; prepare only; name sibling if needed |
| Fill gaps from memory | Refuse |
| Copy teaching example numbers | Refuse |

## C6 check-script input: required JSON fields (C6 Phase 1, 8 November 2026)

`scripts/record_check.py` reads the fields below. Content checks are primary and fail with no confess flag set; flags such as those listed in `references/gap-rules.md` are secondary. Exit 0 = ok, 1 = gaps, 2 = usage.

| Field | Shape | Required when |
|---|---|---|
| `owner` | named person | always |
| `sections.1-7` | objects (range, provenance, options incl. do nothing and do it internally, result, assumptions) | always; missing section is a gap |
| `sections.8.dissent / none_attested_by` | list of {id, text, by} or named attestation | always; never both |
| `prior_dissent_present, prior_dissent_ids` | bool, list of ids | CLOSE-01 when earlier dissent exists |
| `requires_reopen_conditions, reopen_conditions` | bool, list or string | CLOSE-02 when conditions are required |
| `assumptions[].expires_on, review_by` | ISO dates | CLOSE-03 when an assumption can expire |
| `integrity_revisions` | {ground, cut, verify or verify_fallback, frame} non-empty strings | close packet (signers, chosen result, or require_integrity_link) |
| `signers, score_stages` | named people; release records | Gate 3 |

Illustrative shape only. Values are placeholders for the structure and are never live input:

```json
{
  "owner": "Dr. Lena Brandt",
  "prior_dissent_present": true,
  "prior_dissent_ids": ["D1"],
  "requires_reopen_conditions": true,
  "reopen_conditions": ["Baseline time study moves more than 10 percent"],
  "sections": {
    "7": {"assumptions": [{"text": "Vendor price holds", "owner": "Dr. Omar Haddad",
                           "expires_on": "2027-03-01", "review_by": "2027-02-15"}]},
    "8": {"dissent": [{"id": "D1", "text": "Too early", "by": "Dr. Omar Haddad"}]}
  },
  "integrity_revisions": {"ground": "r1", "cut": "r2", "verify_fallback": "r3", "frame": "r4"},
  "signers": ["Dr. Lena Brandt", "Dr. Omar Haddad"]
}
```

Abbreviated: sections 1 to 6, score_stages and the DQ declarations are also required (see `scripts/test_record_check.py` `_rec()` for a full passing record).

Method sections: `references/method.md` (C6 validator-aligned method). Worksheet: `templates/worksheet.md`. Turn questions: `intake.md`, `references/facilitation.md`. Lane A cites: LA-C6-004, LA-C6-006 in `references/lane-a-sources-c6-2026-11-08.md` (rights unknown; no new ids).
