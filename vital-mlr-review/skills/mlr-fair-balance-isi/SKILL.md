---
name: mlr-fair-balance-isi
description: "This skill should be used when operating the mlr-fair-balance-isi step of READY MLR board prep. Do not use to approve copy or invent clearance."
compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.4"
  register_code: "MLR-0.4"
  framework_path: "MLR Review > mlr-fair-balance-isi"
  worker: "MLR fair balance isi"
  pack: "vital-mlr-review"
  product: "READY"
  version: "0.4.2"
  release_state: Released
  route:
    - "Check fair balance and ISI prominence for MLR"
    - "ISI present but tiny type versus benefit headlines"
    - "mlr-fair-balance-isi US and DE panels"
    - "Score ISI proximity and typography contrast"
    - "Fair balance checklist before regulatory chair"
    - "Do not draft final approved ISI"
    - "DE panel incomplete versus Fachinformation safety"
    - "Important Safety Information placement review"
    - "Fair balance revise when prominence weak"
    - "standards-by-market fair balance scoring"
---
    # MLR fair balance and ISI

    This skill should be used when checking fair balance, Important Safety Information placement, indication prominence, and net impression risks for promotional materials. It prepares Regulatory-facing findings and never approves.

    ## When to use
    After `mlr-capability-map` (and after `mlr-channel-intent` when channel is disputed). Before or beside chairs as the funnel dictates. Never as approval.

    ## Instructions

Follow steps below.

## Steps
    1. Read `intake.md` and gather missing fields only.
    2. Follow `references/method.md`.
    3. Prefer offline tools in `references/tools.md`.
    4. Fill Output cards.
    5. Stamp: `python ../../tools/stamp_ready_line.py --skill mlr-fair-balance-isi --letter-lines`

    ## Output cards (required)
    - `../../templates/isi-fair-balance-checklist.md`
    - `../../templates/liability-line.md`
    - `../../templates/check-line-stamp.md`
    - `../../templates/gap-list.md` when gaps exist

    ## Tasks
    - `scan-isi-presence.md` — Scan for ISI / brief summary / PI pointers
- `score-prominence.md` — Compare benefit vs risk prominence factors
- `write-fair-balance-findings.md` — Write findings_only / revise cards

## Tools run only on supplied artefact text (MLR-H1, TEH-RDY-021)

Run a tool on artefact text (body, claims, ISI, label) only when the person supplied that text in this conversation. When only a description of the piece exists, reason from the description, say "no artefact text was supplied", and present no tool output, decision or rationale — never reconstruct or paraphrase a body from the description to feed a tool. Detail: `../../references/hard-rules.md` (MLR-H1).

**The person's description is person-supplied material (TEH-RDY-035).** When the person describes a mismatch without supplying the file (for example "the body says X; the label says Y"), a finding may be opened on that description. Quote it as theirs — `Person's description: "…"` — and label the finding `based on the person's description — verify against the artefact`. The claim span stays `[GAP]` unless the person quoted the artefact wording; the label text stays `[GAP]` until pasted. The status follows the precedence order like any finding (a correctable described mismatch → `revise`). Still never invent artefact text, locators or label text, never present the description as artefact or label text, never run an artefact-text tool on a description, and never build a stand-in packet from it.

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

## References
| Path | Role |
|---|---|
| `references/method.md` | How to run |
| `references/method-standards.md` | WC-* citations |
| `references/knowledge.md` | Domain knowledge |
| `references/failure-modes.md` | Failure library |
| `references/tools.md` | Offline + optional MCP |
| `references/without-connector.md` | No-keys path |
| `governance.md` | Never-approve law |

## Examples
- `examples/good-sourced-draft.md`
- `examples/poor-indication-only-in-isi.md`

## Hard rules
- Never approve. Never invent locators or markets.
- Numbered hard rules MLR-H1–H8 (canonical ids): `../../references/hard-rules.md`.
- Jurisdiction required when markets are in scope — no US default. When the person named no markets, ask for them; never list or suggest specific jurisdictions (rule packs are listed once markets are named — MLR-H6 detail).
- Compose VERIFY; do not fork.
