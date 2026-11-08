# FOCUSED

FOCUSED coaching helps a person decide: Frame, Options, Criteria, Unknowns, Score, Examine, Decide. Skills never name a winner. The person decides at every step.

**Plugin id.** `vital-focused` (Claude / marketplace buyer id). Call the product **FOCUSED**, not Decision Companion.

**Human oversight.** Required for healthcare-adjacent, legal, regulatory, or other high-stakes decisions. This pack does not give clinical, legal, or regulatory advice.

**Version.** 0.5.4 · **Released** · Crossroads Catalyst GmbH (Vital Expert). Buyer channel: `curatedhealth/vital-expert-marketplace` → **`vital-focused`**.

**Support.** Crossroads Catalyst GmbH - Vital Expert - https://vital.expert (use your existing VITAL support channel; no separate public support inbox is claimed here).

## What works without a key

Offline by default:

- All 21 coaching skills
- Local session file `./focused-sessions/<session_id>.focused.json`
- Pack tools for worksheets, weighted score with ±10 robustness, and brief
- Empty `.mcp.json` (no MCP servers required)

Nothing is saved to Vital cloud without an optional key or a future OAuth connection.

## FOCUSED steps

| Step | Plain question | Skills |
|---|---|---|
| Frame | What exactly are we deciding, who decides, by when? | frame-decision, classify-type, rigor-checklist, assign-daii |
| Options | What else could we do, including nothing? | widen-options |
| Criteria / Score | How do your options compare on your own weights, and does the top-ranked option still come first if one priority moves by up to 10 points? | tradeoff-score |
| Unknowns | What do we know / still unknown? | gather-intelligence, handoff-verify |
| Examine | Gut, what could go wrong, who disagrees? | gut-check, premortem, bias-card, record-dissent, decision-check |
| Decide | Choice, owner, when to look again? | make-decision, implement-plan, learning-loop, decision-brief |

Orchestrators: `where-to-start`, `decision-facilitator`. Library: `usecase-library`.

## Optional servers (not loaded by default)

Default install does not connect. Recipes live in `connectors.md`. When the person opts in:

| Server | Sends | Receives |
|---|---|---|
| Decision Companion MCP | Session stage writes, score requests, export, usage | Stage status, scores, export payloads |
| Ontology Navigator MCP | Sealed score / methods handoffs | Navigator results |
| Verify MCP | Source qualify / claim check requests | Admission and claim statuses |

Authentication today: optional Bearer keys in host `userConfig` (`vdec_`, `vont_`, `vvfy_`). OAuth is platform work; see `mcps/decision_companion/docs/SPEC_OAUTH_CONNECTORS.md`.

## Data retention and privacy

- **Local session files** stay on the machine that runs the tools. Retention is the operator's responsibility.
- **Optional cloud MCP** retention follows Vital Expert / Crossroads Catalyst GmbH product terms for those APIs. This README does not invent separate privacy or terms URLs; use https://vital.expert and your contract package until dedicated policy pages are published and measured here.
- Skills must not fill fields from model memory. Missing fields stay "not given yet".

## Skill rename map (0.5.1+)

| Old (≤0.5.0) | New |
|---|---|
| bias | bias-card |
| brief | decision-brief |
| classify | classify-type |
| rigor | rigor-checklist |
| tradeoff | tradeoff-score |
| facilitator | decision-facilitator |
| daii | assign-daii |

Uninstall 0.3.x and stale 0.5.0 before syncing so skill ids do not mix.

## Packaging notes

- Stage schemas: `contract/stage_schemas.json` (not under `skills/`).
- Shared rules SSOT: monorepo `src/shared/rules-core.md` + `rules-full.md`, injected/copied by `packaging/build_shared.py`.
- Eval harness JSON: monorepo `mcps/decision_companion/evals/` only. Not shipped in the buyer install tree.
- License: proprietary (`LICENSE`). Product of Crossroads Catalyst GmbH.
