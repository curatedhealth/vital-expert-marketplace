---
name: mlr-regulatory-chair
description: "This skill should be used for the regulatory chair only — ISI/brief-summary format, pre-approval promotion controls, code-process and audience/channel gates grounded in regulatory ruleset rows. Do not use for clinical label science (medical), misleadingness theory (legal), or approving copy."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-R.1"
  register_code: "MLR-R.1"
  framework_path: "MLR Review > Regulatory chair"
  family: "mlr-chair"
  worker: "Regulatory reviewer (host-reasoner)"
  pack: "vital-mlr-review"
  version: "0.4.2"
  release_state: Released
  chair: "regulatory"
  route:
    - "Run the regulatory chair on the ISI block"
    - "Brief summary format gate for MLR"
    - "Load only chairs regulatory from the ruleset"
    - "Pre-approval promotion control for the regulatory chair"
    - "Audience and channel gates for regulatory MLR"
    - "Regulatory findings cite source_ref and claim_span"
    - "Code certification process stays with regulatory chair"
    - "REMS or CDx process box for the regulatory chair"
    - "Hand clinical SmPC truth away from regulatory chair"
    - "Regulatory chair decision revise is not agency clearance"
---

# Regulatory chair

Own promotional format, ISI/brief-summary presence, pre-approval controls, and code-process gates. Never claim agency clearance.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| load regulatory rules | Load chairs.regulatory checklist rows | `tasks/load-regulatory-rules.md` |
| review format and gates | Review ISI/format and process gates | `tasks/review-format-and-gates.md` |
| write regulatory findings | Emit regulatory chair packet JSON | `tasks/write-regulatory-findings.md` |

## Scripts

`scripts/check_finding_shape.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Chair boundary (MECE)

| Own (Regulatory) | Hand off |
|---|---|
| ISI / brief summary presence and format | Medical clinical content → `mlr-medical-chair` |
| Pre-approval promotion controls | Medical scientific framing → `mlr-medical-chair` |
| Code process / certification boxes | Legal character of claims → `mlr-legal-chair` |
| Audience × channel gates | — |

See `references/chair-boundaries.md`.

## Status on close

Pick the card's one status from the shared map `../../references/finding-status-map.md`. Precedence rule 1 comes first: any request to approve or clear, or to bypass any hard rule MLR-H1–H8 (for example fill locators or names from memory, default a market, file a submission, skip ISI, use an AI owner, reuse an expired key) → refuse it, `human_gate_required`, even with inputs missing. Then the highest open finding wins. Every pack rule row is fail-close: it is never waved through, but fail-close is a property of the rule row, not a status — it does not by itself make a finding `human_gate_required` (TEH-RDY-027). A chair never states `prep_complete`. Write it as `Status: <value>`.

| Open regulatory finding | Status |
|---|---|
| Correctable wording or format the chair can state from supplied material: absolute or exaggerated language, a missing mandatory element or ISI / brief-summary block that can be added, a format fix | `revise` |
| A human judgment call: pre-approval promotion or unknown authorization status, an audience or channel gate on supplied facts (supplied audience or channel conflicts with the content, or supplied facts support more than one reading), disagreement with another chair on the same claim span, a request to approve or clear, or to bypass any hard rule MLR-H1–H8 (precedence rule 1, for example a request to file a submission) | `human_gate_required` |
| No open finding: observations only, `Watch for:` notes, `[DEFERRED]` lines only, or could not assess because an input is missing (name each missing input as `[GAP]`; a missing input is not a finding) — including audience or channel not supplied, or a ruleset that cannot load without them: ask for them (TEH-RDY-047) | `findings_only` |

**Missing audience, channel or ruleset (TEH-RDY-047).** When audience or channel was not supplied, or the ruleset cannot load without them, do not escalate: ask for audience and channel, write `[GAP]` for each, cite no rule id, and close `findings_only` (precedence rule 4). An impression from the wording about who the piece targets is an observation, not a supplied audience. `human_gate_required` applies only to a genuine judgment call on supplied facts per `../../references/finding-status-map.md`.

## Tools run only on supplied artefact text (MLR-H1, TEH-RDY-021)

Run a tool on artefact text (body, claims, ISI, label) only when the person supplied that text in this conversation. When only a description of the piece exists, reason from the description, say "no artefact text was supplied", and present no tool output, decision or rationale — never reconstruct or paraphrase a body from the description to feed a tool. Detail: `../../references/hard-rules.md` (MLR-H1).

**The person's description is person-supplied material (TEH-RDY-035).** When the person describes a mismatch without supplying the file (for example "the body says X; the label says Y"), a finding may be opened on that description. Quote it as theirs — `Person's description: "…"` — and label the finding `based on the person's description — verify against the artefact`. The claim span stays `[GAP]` unless the person quoted the artefact wording; the label text stays `[GAP]` until pasted. The status follows the precedence order like any finding (a correctable described mismatch → `revise`). Still never invent artefact text, locators or label text, never present the description as artefact or label text, never run an artefact-text tool on a description, and never build a stand-in packet from it.

## Tool path

1. Call `vital-mlr-review:mlr_get_ruleset`; apply only `chairs.regulatory`.
2. Run `scripts/check_finding_shape.py` then `scripts/check_forbidden_phrases.py`.

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

End every user-facing turn with `python tools/stamp_ready_line.py --skill mlr-regulatory-chair --status <status>` (see `templates/check-line-stamp.md`). `<status>` is exactly one of `findings_only` · `revise` · `human_gate_required` · `prep_complete` — no other value. Optional `--letter-lines` prints the liability line.

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
| `scripts/check_finding_shape.py` | Deterministic check — run, do not re-implement |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/chair-boundaries.md` | Preserved domain reference |
| `../../references/finding-status-map.md` | Shared finding → status map (all three chairs) |
| `references/finding-shape.md` | Preserved domain reference |
| `references/standards-by-market.md` | Preserved domain reference |
