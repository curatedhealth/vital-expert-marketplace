---
name: mlr-compile
description: "This skill should be used when aligning medical, legal, and regulatory chair packets, calling compile/validate tools, and surfacing conflicts for the board. Trigger when three chairs exist or the person asks to compile the MLR pack. Do not use to invent chair findings or to approve copy."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-4.1"
  register_code: "MLR-4.1"
  framework_path: "MLR Review > Compile"
  family: "mlr-prep"
  worker: "MLR compile lead"
  pack: "vital-mlr-review"
  version: "0.4.2"
  release_state: Released
  route:
    - "Compile the three MLR chair packets"
    - "Validate the MLR packet for the board"
    - "mlr_validate_packet after chair alignment"
    - "Cross-chair conflict matrix for MLR"
    - "Same artefact_version across MLR chairs"
    - "Fail-close finding forces human_gate_required"
    - "Forbidden approval phrases fail MLR validation"
    - "Stub market gap stays visible at compile"
    - "Chair approve means not blocking human handoff"
    - "Send the compiled MLR pack to committee prep"
---

# Compile

Align three separate advisory chairs and the markets in scope. Refuse a blended single-reviewer packet. Never approve the copy.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| align chairs | Build conflict matrix across chairs and markets | `tasks/align-chairs.md` |
| validate for board | Validate packet and set prep status | `tasks/validate-for-board.md` |

## Scripts

`scripts/validate_packet_shape.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Inputs must be supplied (TEH-RDY-017)

Never create stand-in packets, placeholder versions, or chair decisions to make a tool run (MLR-H1). Compile only the chair packets the person or a chair skill in this conversation produced. When a chair packet is missing, list that chair as `[GAP] chair packet not supplied`, do not call `mlr_validate_packet` with an invented decision (for example a placeholder `approve` with no findings), and close with `Status: findings_only` — unless a request to approve or clear, or to bypass any hard rule MLR-H1–H8 (including an AI owner request), in the same request makes it `human_gate_required` (precedence rule 1, `../../references/finding-status-map.md`).

## Skip requests are bypass requests (TEH-RDY-059)

The required order is fixed: `mlr-intake` → the three separate chairs (`mlr-medical-chair`, `mlr-legal-chair`, `mlr-regulatory-chair`) → `mlr-compile` → `mlr-board-prep`. A request to skip or drop a required step or chair for this piece — intake before the chairs, the chairs before compile, compile before board prep, or any one of the three chairs — is a bypass request (precedence rule 1(b), `../../references/finding-status-map.md`), also when it is phrased as a question ("skip the chairs — can compile alone get us to the board?", "can we drop Legal this time?"). Refuse the skip in plain words; say why the step is required (compile only aligns and validates what the three chairs produced; board prep needs the validated compile); route to the next required step; ask for missing inputs (markets when none were supplied, without suggesting any); and close `Status: human_gate_required`. Name what the human must decide: commission the missing step or chair — this pack never offers a path around it, and never leaves the skip to be settled later. A general question about how the order works, with no request to skip a step for this piece, is answered, not refused (rule 4).

## Tool path

1. Run `scripts/validate_packet_shape.py` locally.
2. Call `vital-mlr-review:mlr_compile_checklist` then `vital-mlr-review:mlr_validate_packet`.
   Pass the packet header `artefact_version` to `mlr_compile_checklist` when the person supplied it. **Same artefact version (TEH-RDY-046):** every chair packet's `artefact_version` must equal the packet header version. Report each version exactly as supplied; on a mismatch (an `artefact_version_mismatch` conflict slot or an `artefact_version mismatch` validate error) the packet is not valid for board — never state or carry forward `prep_complete`, name each version as supplied, and ask which version is under review.
   **Tool-derived status is an input (TEH-RDY-050).** `mlr_validate_packet` / `mlr_compile_checklist` statuses feed the precedence order in `../../references/finding-status-map.md`; they do not replace it. After a validation error, read the open findings yourself: a correctable validation problem (such as a version mismatch) and/or open correctable findings → `revise`; any open finding needing a human judgment call → `human_gate_required`; `findings_only` only when no finding is open.
   **Residuals as recorded (TEH-RDY-053).** Carry each residual and its acceptance exactly as the packet records it: "accepted by <name as recorded>", or "[GAP] no named human acceptance recorded" — never say an accepted residual still needs acceptance.
3. Run `scripts/check_forbidden_phrases.py` on any summary text.
4. Optional next: `mlr-verify-handoff`, then `mlr-board-prep`.

## Boundaries

| Question | Where it goes |
|---|---|
| What can this pack do / which skill | `mlr-capability-map` |
| Markets and ruleset load | `mlr-intake` |
| Clinical / label accuracy | `mlr-medical-chair` |
| Misleadingness / comparative-ad / privacy | `mlr-legal-chair` |
| ISI / format / pre-approval process | `mlr-regulatory-chair` |
| Align + validate | `mlr-compile` |
| Passage / source proof | `mlr-verify-handoff` |
| Named-human prep record | `mlr-board-prep` |



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

End every user-facing turn with `python tools/stamp_ready_line.py --skill mlr-compile --status <status>` (see `templates/check-line-stamp.md`). `<status>` is exactly one of `findings_only` · `revise` · `human_gate_required` · `prep_complete` — no other value. Optional `--letter-lines` prints the liability line.

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

Sections in `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

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
| `scripts/validate_packet_shape.py` | Deterministic check — run, do not re-implement |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/status-vocab.md` | Preserved domain reference |
