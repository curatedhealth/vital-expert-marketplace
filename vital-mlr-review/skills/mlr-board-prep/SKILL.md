---
name: mlr-board-prep
description: "This skill should be used when producing the reviewer-facing MLR board packet and calling mlr_build_prep_record with a named human owner after compile. Do not use to stamp approved or mlr_reviewed, to write chair findings, or to run VERIFY alone."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-6.1"
  register_code: "MLR-6.1"
  framework_path: "MLR Review > Board prep"
  family: "mlr-prep"
  worker: "MLR coordinator"
  pack: "vital-mlr-review"
  version: "0.4.2"
  release_state: Released
  route:
    - "Assemble the MLR board pack for the committee"
    - "Build the MLR prep record with a named human"
    - "mlr_build_prep_record requires cleared_by name"
    - "prep_cleared_for_human_mlr is not approved for use"
    - "mlr_reviewed stays false on the prep record"
    - "Refuse system as cleared_by for MLR prep"
    - "Surface stub market gaps on the board cover"
    - "Keep chair disagreements visible in the board pack"
    - "Point the board pack at the company MLR SOP"
    - "Send the prep record to tomorrow's MLR committee"
---

# Board prep

Assemble what humans on the MLR committee will read. The prep record carries the record state `prep_cleared_for_human_mlr`: ready for their process — not a packet status and not use-clearance. Require a named human owner.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| assemble board pack | Assemble reviewer-facing board cover | `tasks/assemble-board-pack.md` |
| build prep record | Build prep record with named human | `tasks/build-prep-record.md` |

## Scripts

`scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Inputs must be supplied (TEH-RDY-017)

Never create stand-in packets, placeholder versions, or chair decisions to make a tool run (MLR-H1). If the validated compile output or any chair packet is not supplied, stop: say what is missing, close with `Status: findings_only` — unless a request to approve or clear, or to bypass any hard rule MLR-H1–H8 (including an AI owner request), in the same request makes it `human_gate_required` (precedence rule 1, `../../references/finding-status-map.md`) — and do not call `vital-mlr-review:mlr_build_prep_record` (or the offline CLI). The prep-record tool also refuses packets flagged synthetic / stand-in or carrying a placeholder token in a version or chair summary, but that guard is narrow — the rule is yours to keep.

## Tool path

1. Confirm prior `vital-mlr-review:mlr_validate_packet` (or explicit gate).
2. Call `vital-mlr-review:mlr_build_prep_record` with `cleared_by.name` set to a human.
3. Run `scripts/check_forbidden_phrases.py` on the board cover.

`cleared_by` (MLR-H5) is refused when the name is, or contains as a whole word, any of: assistant, ai, a.i., model, system, auto, automated, automation, bot, chatbot, chatgpt, gpt (and gpt4-style variants), openai, claude, anthropic, copilot, gemini, llm, agent, n/a, tbd, unknown, empty or whitespace. Case does not matter, and a human name attached to such a token is still refused (for example "Claude (acting on behalf of Dr. Weber)"). Names that merely contain the letters (Aileen, Claudette, Gaia) are not refused. Ask for the person's full name; never pick a workaround.

**A real name that collides with a token (TEH-RDY-036).** When the person names a human whose name contains a refused token as a whole word (for example a given name that is itself a token), the tool refuses it. Say so plainly: the refusal comes from the token rule, not from a doubt about the person. Then ask the person to confirm the owner's name in a form that does not contain the token as a standalone word — for example the full given name when the token is a short form, or the form the company's records use, such as family name with given-name initial (family-name-first ordering alone still contains the token, so the tool still refuses it). The person supplies and confirms that form; never choose, shorten or re-spell it yourself. Otherwise the person names a different human owner or takes the question to the plugin owner — there is no in-session override, and the token list is not changed here. Never accept an AI, model, tool or system as owner. Build no record until an accepted name is supplied. This is not an AI owner request: the status comes from precedence rules 2–5 on the packet as supplied.

## Status line and record state

Every user-facing result carries one line `Status: <value>`, where `<value>` is exactly one of `findings_only` · `revise` · `human_gate_required` · `prep_complete`. Nothing else goes on that line or in `--status`.

When a prep record exists, report it on its own separate line, exactly:

`Record state (not a status, not use-clearance): prep_cleared_for_human_mlr`

**Re-derive the packet status from its findings (TEH-RDY-063).** The packet's own status (`mlr_status`, a cover line, a status the person states for the packet) is an input, never the answer's status by itself. Read the packet's open findings, validation result and residuals and apply the precedence order (`../../references/finding-status-map.md`): rule 1 → `human_gate_required`; an open finding needing a human judgment call, `reject` / `abstain`, chair disagreement or an unaccepted residual → `human_gate_required`; every open finding correctable → `revise`; no open finding → `findings_only` (or `prep_complete` only per § When `prep_complete` may be stated). When the derived status differs from the packet's, report both on one line — `Packet says <packet status>; findings support <derived status>.` — name the findings (or their absence) behind the derived one, and write the derived status on the `Status:` line. Never silently carry a status no finding supports, and never lower a status a finding supports.

Never call the record state `prep_cleared_for_human_mlr` a status. The tool field `record.status` keeps that value for app compatibility; present it only as the record state. See `references/status-vocab.md`.

## When `prep_complete` may be stated

State `prep_complete` only when all three hold:

1. A compile packet exists and `vital-mlr-review:mlr_validate_packet` returned ok for the same artefact version.
   **Same artefact version (TEH-RDY-046).** Read the packet header `artefact_version` and every chair packet's `artefact_version` yourself, before quoting any tool. Every chair version must equal the header version. Report each version exactly as supplied ("packet header v<x>; medical v<y>; legal v<z>; regulatory v<w>") — never restate a chair's version as the header's, never say "on all three chairs" unless every chair carries that same value. On any mismatch, `mlr_validate_packet` returns an `artefact_version mismatch` error: condition 1 fails, build no record, and do not state `prep_complete`; name the mismatch and ask the person which version is under review.
   **Tool-derived status is an input (TEH-RDY-050).** The status the validator or render step reports is not the answer's status. After a validation error, read the packet's open findings and apply the precedence order: a correctable validation problem (such as a version mismatch) and/or open correctable findings → `revise`; any open finding needing a human judgment call → `human_gate_required`; `findings_only` only when the packet has no open finding. Never take `findings_only` from a failed validation while a correctable finding is open.
2. No blocking item is open: no chair finding still open under decision `revise`, `reject` or `abstain`; no open fail-close finding; no unresolved compile conflict slot.
3. Every residual that remains (stub or missing ruleset coverage, `[GAP]`, a claim not tool-checked) is listed on the board cover with the named human who accepted it.
   **Report residual acceptance exactly as recorded (TEH-RDY-053).** Read each residual's acceptance from the packet as supplied. When the packet records a named human acceptor, write "accepted by <name as recorded>" — never say the residual still needs acceptance. When it records none, write "[GAP] no named human acceptance recorded" — never supply or assume an acceptor.

Otherwise, after precedence rule 1 (any request to approve or clear, or to bypass any hard rule MLR-H1–H8, including an AI owner request → `human_gate_required`): no packet or no validate result → `findings_only`; an open correctable finding → `revise`; an open fail-close finding, chair disagreement, `reject` / `abstain`, or a residual that no named human has accepted → `human_gate_required` (mapping: `../../references/finding-status-map.md`). A listed and accepted residual never blocks `prep_complete` and never leaves the cover.

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

End every user-facing turn with `python tools/stamp_ready_line.py --skill mlr-board-prep --status <status>` (see `templates/check-line-stamp.md`). `<status>` is exactly one of `findings_only` · `revise` · `human_gate_required` · `prep_complete` — no other value. Optional `--letter-lines` prints the liability line.

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
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/board-pack-shape.md` | Preserved domain reference |
| `references/status-vocab.md` | Preserved domain reference |
