# Shared 10-part decision record — Outcome Navigator path (CF-01.06.01)

Source of shape: Launch Navigator design `docs/claude-project/launch-navigator/02_decision_record_standard.md` (full field table lives there). This file is the **non-gate** adaptation for investment / measurement decisions.

Evidence classes: M measured · V document · O owner ruling · H design. `[CHECK]` = not traced to a dated primary. `[GAP]` = missing fact, never filled.

## Path rules (Outcome vs Launch)

| | Outcome Navigator | Launch Navigator |
|---|---|---|
| Result vocabulary | **Proceed** / **Investigate first** / **Handle it internally** | Pass / Conditional / Hold / Escalate |
| Gate wrapper | **Omit** `launch_gate` / gate_code / gate_verdict | Required for G1–G5 |
| Signature | Prepared for signature or blocked — **never** signed by the assistant | Same |
| MLR language | Forbidden (READY) | Not this path |

If the session is a launch gate, **stop** and hand off to Launch Navigator. Do not dual-write both vocabularies.

## Client eight sections vs these 10 parts

Live close and the playbook speak in **eight sections + annex** (`close-the-decision/templates/decision-record.md`). This file is the shared substrate (10 parts). The board pack maps them: see `compile-board-pack/templates/board-report.md` § “How to read this pack”. Never show part numbers to the client reader.

## The 10 parts (required)

1. **Identity** — decision id, type (investment / measurement / portfolio), version; supersedes prior version by link, never overwrite.
2. **Frame** — question, scope, out of scope, why now. Restate solutions as decisions of intent.
3. **Decision rights** — one named Decide; Advise / Inform / Implement (DAII). Reversibility wording.
4. **Options** — chosen + ≥1 alternative + do nothing + defer/handle internally as appropriate.
5. **Criteria and evidence** — human weights (sum ~1); scores by named people (1–10); evidence lines with source_id / class.
6. **Choice, rationale, prediction** — named chooser; rationale; predicted outcome as low/mid/high + metric + date; confidence %. Result enum = Proceed | Investigate first | Handle it internally only.
7. **Active assumptions** — each with signal, threshold, owner; reopen rules.
8. **Challenge** — premortem; red-team view when listed; bias check (never "clean"); dissent by name or named "no dissent".
9. **Journal** — most confident / most worried / chose to ignore / would change mind.
10. **Follow-up** — review date; success signal; later: actual outcome, prediction error, lessons, pattern link.

Plus: two distinct prepared signers (one = decider); `signature_status` prepared|blocked; `signed` always false from the assistant.

## Skill mapping

| Skill | Parts primarily filled |
|---|---|
| `route-the-entry` / `frame-the-decision` | 1–2 (identity draft, frame) |
| `size-value-at-stake` / `compare-options` / `run-weight-sensitivity` | 4–5 |
| `place-the-portfolio` / `plan-the-delivery` / `design-the-trial` | 5–7 inputs |
| `ground-the-numbers` → `cut-the-slop` → `handoff-verify` | evidence integrity for 5–6 |
| `design-decision-exhibits` / `frame-exhibits-honestly` / `fit-the-ic-reader` | exhibit lock for board |
| `compile-board-pack` | maps pack sections → parts 1–10 |
| `close-the-decision` | seals 6–10; prepare signoff only |

## Hard don'ts

- Assistant never fills scores, never chooses, never `signed=true`.
- Teaching-example figures never enter a live record.
- Relative claims without absolute stay gap/remove.
- Integrity order before seal: ground → cut → verify posture → exhibits locked → seal check.
