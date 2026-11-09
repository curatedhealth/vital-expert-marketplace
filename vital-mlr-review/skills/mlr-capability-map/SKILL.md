---
name: mlr-capability-map
description: "This skill should be used when the person asks what MLR Review can do, which skill to run, how TRUSTED differs from VERIFY and MLR, whether Medical versus Legal versus Regulatory applies, how to set up vmlr_/vvfy_, or whether a piece is ready for the MLR board. Routes to intake, chairs, compile, verify-handoff, or board-prep. Do not use to approve copy or replace the company MLR committee."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Runs offline with skills + local tools. Optional vmlr_/vvfy_ when `.mcp.json` opted in. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.0"
  register_code: "MLR-0.0"
  framework_path: "MLR Review > Capability map"
  family: "mlr-core"
  worker: "Cross-functional MLR coordinator"
  pack: "vital-mlr-review"
  version: "0.4.2"
  release_state: Released
  route:
    - "What can MLR Review do on this host"
    - "Route me to the right MLR skill"
    - "TRUSTED versus VERIFY versus MLR Review"
    - "When do I use Medical versus Legal versus Regulatory chairs"
    - "Is this piece ready for the MLR board"
    - "How do I set up the vmlr key for MLR"
    - "Capability map for MLR board prep"
    - "Do not blend the three MLR chairs"
    - "MLR Review never approves promotional copy"
    - "Start with the MLR capability map"
---

# Capability map

Routeboard for VITAL MLR Review. Explain prep-only scope. Point to the next skill. Never stamp compliance.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| explain and route | Explain scope and route to the next skill | `tasks/explain-and-route.md` |
| companions | Explain vmlr_/vvfy_ and TRUSTED/VERIFY/MLR | `tasks/companions.md` |
| choose depth | Choose light / short / full review depth | `tasks/choose-depth.md` |

## Scripts

`scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Output card (required, TEH-RDY-039)

Every capability-map answer renders `../../templates/capability-map-card.md` in full: the fixed table of all 11 skill ids — including `mlr-capability-map` itself — and the fixed "Will never" block (approve or clear; decide for humans; claim tool-checked without keys; file submissions; default markets; accept AI owners). Never shorten the table to the skills on the route, never drop this skill's own row, and never trim the block. Then the liability line and the closing stamp (`../../templates/liability-line.md`, `../../templates/check-line-stamp.md`).

## Standard table

| Skill | Own question |
|---|---|
| `mlr-capability-map` | What the pack can do, which skill when, hard boundaries |
| `mlr-channel-intent` | Promo vs scientific exchange vs med_info gate |
| `mlr-intake` | Markets, audience, channel, artefact version, authorized use per market (no markets named → ask; never list or suggest jurisdictions) |
| `mlr-claims-matrix` | Pre-chair verbatim claims + locators + authorised-use bind |
| `mlr-medical-chair` | **M** — clinical/label accuracy, clinical evidence |
| `mlr-legal-chair` | **L** — misleading impression, comparative-ad, privacy/IP |
| `mlr-fair-balance-isi` | Fair balance / ISI / net impression (prep) |
| `mlr-regulatory-chair` | **R** — format, pre-approval gates, code process, audience/channel overlays |
| `mlr-compile` | Align chairs; validate; conflict slots; reconciliation |
| `mlr-verify-handoff` | Admit sources / check claims on VERIFY (or offline packet) |
| `mlr-board-prep` | Named-human prep record for the committee |

Hard rules detail: `../../references/hard-rules.md` (canonical numbering; `references/hard-rules.md` points there). Chair MECE: `references/chair-index.md`. Funnel: `../../workflows/offline-prep-e2e.md`.

## Boundaries

| Question | Where it goes |
|---|---|
| What can this pack do / which skill | `mlr-capability-map` |
| Promo vs scientific exchange | `mlr-channel-intent` |
| Markets and ruleset load | `mlr-intake` |
| Claims matrix / locators | `mlr-claims-matrix` |
| Clinical / label accuracy | `mlr-medical-chair` |
| Misleadingness / comparative-ad / privacy | `mlr-legal-chair` |
| Fair balance / ISI prominence | `mlr-fair-balance-isi` |
| Format / pre-approval process | `mlr-regulatory-chair` |
| Align + validate | `mlr-compile` |
| Passage / source proof | `mlr-verify-handoff` |
| Named-human prep record | `mlr-board-prep` |
| Post-clearance regulator submission filing | **DEFERRED** — not in READY. Record `[DEFERRED]`; do not fake a filing path. Name Form 2253 only when US is a supplied market or the person asks (`[DEFERRED] Form 2253 — out of READY scope`); otherwise write "regulator submission filings are deferred". After human MLR clearance, a named human owns any filing the company SOP requires (`../../references/post-clearance-deferred.md`). |

## Skip requests are bypass requests (TEH-RDY-059)

The required order is fixed: `mlr-intake` → the three separate chairs (`mlr-medical-chair`, `mlr-legal-chair`, `mlr-regulatory-chair`) → `mlr-compile` → `mlr-board-prep`. A request to skip or drop a required step or chair for this piece — intake before the chairs, the chairs before compile, compile before board prep, or any one of the three chairs — is a bypass request (precedence rule 1(b), `../../references/finding-status-map.md`), also when it is phrased as a question ("skip the chairs — can compile alone get us to the board?", "can we drop Legal this time?"). Refuse the skip in plain words; say why the step is required (compile only aligns and validates what the three chairs produced; board prep needs the validated compile); route to the next required step; ask for missing inputs (markets when none were supplied, without suggesting any); and close `Status: human_gate_required`. Name what the human must decide: commission the missing step or chair — this pack never offers a path around it, and never leaves the skip to be settled later. A general question about how the order works, with no request to skip a step for this piece, is answered, not refused (rule 4).

## Write requests without a key (TEH-RDY-044)

A request to write, save, record or run every stage "to the MLR MCP" (or to VERIFY) when no valid `vmlr_` / `vvfy_` key is connected is a bypass of MLR-H4: refuse the write, say no connector write happened and nothing is tool-checked, offer the READY-local path, and close `human_gate_required` (precedence rule 1). Name what the human must do: connect a valid key, or accept a local, not tool-checked record.

## Routing to intake asks for markets (TEH-RDY-045)

When the answer routes to `mlr-intake` (or names any market-dependent next step) and the person supplied no markets, ask for the markets in the same answer — also on a refusal path — without listing or suggesting any jurisdiction.

## Requests to paste all hard rules

When asked to dump, paste or list all MLR-H rules, do not reproduce the full text. Give the file pointers (the Hard rules section of this `SKILL.md` and the canonical `../../references/hard-rules.md`) and one line per rule id from the Hard rules section below: the id and a short summary of a few words.



## Supplied markets, rule ids and values only (TEH-RDY-024–031)

Detail: `../../references/hard-rules.md` (MLR-H1, MLR-H6).

- **Per supplied market.** Every market-scoped line — label basis, ruleset coverage, standards touched, `applies_to`, residuals — has one entry per market the person supplied, and none for any other market. Never copy a market list from a reference, template or example. A label-basis line names the supplied market's own label document from `../../references/label-basis-by-market.md` (a market not listed there: "authorized labeling for <market>") — never another market's document name and never an "X or Y" list of document names (TEH-RDY-038).
- **Echo markets exactly.** Whenever the answer restates which markets the person named, repeat the supplied list exactly — every supplied market, in the person's order, and no other. Never narrow it (not "only <one market>" when more were supplied) and never widen it. To set aside a market, authority or rule set the person did not name, say it is not in the supplied list and repeat the full list (TEH-RDY-042).
- **Rule pack binds only on supplied context.** "Channel" in a rule pack is the communication **intent** — the key in `rulesets/REGISTRY.json` (`promo` or `scientific_exchange`; `med_info` and `other` carry no pack). The **medium** — how the piece is delivered (email, print, digital display, congress, social) — is recorded on the card and never binds a pack; a medium is never an "unrecognized channel" and never blocks binding (TEH-RDY-057). Rule packs bind on market + audience + intent. Map common intent words transparently and say so ("promotional" / "promo" → `promo`; "scientific exchange" → `scientific_exchange`); never map a medium to an intent. Do not name, bind or report coverage for any rule pack (a `ruleset_id`) as applying to this piece until the markets AND the audience AND the channel (intent) are all person-supplied — or explicitly derived from supplied evidence, and the answer says so (for example "channel derived from the supplied request record", or a `ruleset_id` the person's own packet carries, quoted as supplied). Until then write, per supplied market, "rule pack binds once audience and channel are supplied" and ask for the missing values (for a medium-only answer, ask which intent applies). Tools receive only supplied values: never pass a guessed or default audience or channel to `mlr_intake`, `mlr_list_rulesets` or `mlr_get_ruleset` (pass a named medium as `medium`), and never present coverage or rows a tool returned for a guessed value (TEH-RDY-043). When markets, audience and intent were all supplied, never write that line: show the binding the tool returned per supplied market (its `ruleset_id` and status) or the specific gap it returned — for example `[GAP] no rule pack for intent <intent> in <market>` for an intent no rule pack carries. Never map a supplied intent to another intent yourself (TEH-RDY-052). **What this rule does not stop (TEH-RDY-060):** it limits only asserting that a pack applies while audience or intent is missing. It never stops acknowledging, reporting or recording a pack, coverage label (`full` / `stub`) or residual that the person or the packet names (for example "the <market> stub residual you named": report it as the person stated it, as theirs), and never stops reporting catalog coverage read from `rulesets/REGISTRY.json` for a supplied market ("the catalog lists <market> as a stub") — labeled as catalog coverage, not as the binding for this piece.
- **Ask for markets before any market-dependent step.** Any answer that routes to `mlr-intake` or to any market-dependent step (ruleset load, label basis, chair review, compile, board prep) asks the person for the markets when none were supplied — including on a refusal path. Ask without listing or suggesting any jurisdiction (TEH-RDY-045).
- **Rule ids exist.** Cite only rule ids that exist in a ruleset loaded for this packet, from the row whose check covers the concern. Never mint a rule id; with no matching row write `[GAP] no matching rule row` or route the concern.
- **Claim spans are verbatim.** A claim span quotes text the person supplied (artefact text, or a phrase the person quoted). If no artefact text was supplied, the claim span is `[GAP]`.
- **Tool arguments are supplied values.** Call a tool only with field values the person supplied or an earlier tool returned. Leave a missing field empty so the tool reports it; never pass a placeholder, example or guessed value.
- **Form 2253.** Name it only when US is a supplied market or the person asks, and only as the line `[DEFERRED] Form 2253 — out of READY scope` — never as a finding, rule row or rule id. Otherwise write "regulator submission filings are deferred".
- **Close stamp in a multi-skill answer.** The stamp names the last skill actually run in this answer: the last skill whose step actually executed (a tool call, a card, a check or a refusal it made) — never a later skill that was only named, routed to or walked through, and never a skill that ran no step. A journey that only refuses stamps the skill that refused (TEH-RDY-054).

## Status precedence, stated once (TEH-RDY-033, TEH-RDY-034)

Detail: `../../references/finding-status-map.md` § Precedence order and § One status, stated once.

- **Status precedence.** The first rule that applies sets the status: (1) any request to approve or clear, or to bypass any hard rule MLR-H1–H8 — for example fill or invent data, locators or names from memory; assume or default a market, audience or channel; make an AI / system the record owner; file a submission; skip ISI; skip a required step or chair (intake before the chairs, the chairs before compile, compile before board prep, or any one chair) — even when asked as a question about this piece (TEH-RDY-059); reuse an expired key; write to a connector (the MLR MCP, VERIFY) without a valid key — → `human_gate_required`, always, even when inputs are missing (refuse it and name what the human must decide; a field simply not yet supplied — markets, audience, channel, or a ruleset that cannot load without them — is rule 4: ask for it, `findings_only`, not a bypass and not a human gate; asking a chair for another chair's work, or asking about a deferred feature, is routing, not a bypass; naming a delivery medium where the channel (intent) was asked is a missing intent, not a bypass (TEH-RDY-057); a gate that could not classify only because inputs are missing is rule 4, not a human gate (TEH-RDY-058) — route it, rule 4 unless the packet sets another rule, TEH-RDY-051); (2) an open finding that needs a human judgment call → `human_gate_required`; (3) every open finding correctable by a copy change → `revise`; (4) missing inputs or observations only → `findings_only`; (5) `prep_complete` only per the board-prep rule. Any status sentence or table elsewhere in this skill applies only within this order.
- **Findings only on supplied issues (TEH-RDY-048).** Open a finding only on an issue present in the supplied text or described by the person (what is wrong, not just a category such as "an omission" or "a flag"). A risk the person did not describe and the supplied text does not show goes under a `Watch for:` note — it is not a finding, carries no severity and does not change the status. A request that names only a category with no content is a missing input: write `[GAP]` for what the issue is, ask for it, and apply rule 4 (`findings_only`).
- **One status, stated once.** Write the status once, on the `Status:` line (the close stamp repeats it). Never name a conditional, alternative or future status anywhere else in the answer; say in words what a human must supply or decide.

## Closing stamp

End every user-facing turn with `python tools/stamp_ready_line.py --skill mlr-capability-map --status <status>` (see `templates/check-line-stamp.md`). `<status>` is exactly one of `findings_only` · `revise` · `human_gate_required` · `prep_complete` — no other value. Optional `--letter-lines` prints the liability line.

## Hard rules (every MLR skill)

- **MLR-H1.** Only stored material counts — fields from the person or a tool result.
- **MLR-H2.** Teaching material is never input — examples/ and patterns.md are invented for shape.
- **MLR-H3.** Never approve — no approved-for-use, mlr_reviewed, or regulator-compliant stamp.
- **MLR-H4.** Never simulate the connector — without vmlr_/vvfy_ label not tool-checked.
- **MLR-H5.** A named human owns prep records — refuse ai/model/assistant/system as cleared_by.
- **MLR-H6.** Markets explicit — never default jurisdictions to the US.
- **MLR-H7.** Keep M / L / R MECE — do not blend chairs or substitute another market's rules.
- **MLR-H8.** Plain liability — every user-facing result ends with the closing line.

## What to return

The full `../../templates/capability-map-card.md` (all 11 rows and the "Will never" block), then the route for this request. End with the closing line in `references/governance.md`.

## Files

| File | Role |
|---|---|
| `tasks/` | Formula tasks for this skill |
| `references/tools.md` | Fully qualified MCP tool names |
| `references/knowledge.md` | Skill rules |
| `references/knowledge.md` | Shapes, not facts |
| `references/failure-modes.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `../../templates/` Output cards (see SKILL.md) | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Route and refuse cases |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/hard-rules.md` | Preserved domain reference |
| `references/chair-index.md` | Preserved domain reference |
| `references/companions.md` | Preserved domain reference |
