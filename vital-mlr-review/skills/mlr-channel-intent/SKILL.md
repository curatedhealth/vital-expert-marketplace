---
name: mlr-channel-intent
description: "This skill should be used when operating the mlr-channel-intent step of READY MLR board prep. Do not use to approve copy or invent clearance."
compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.4"
  register_code: "MLR-0.4"
  framework_path: "MLR Review > mlr-channel-intent"
  worker: "MLR channel intent"
  pack: "vital-mlr-review"
  product: "READY"
  version: "0.4.2"
  release_state: Released
  route:
    - "Classify promo versus scientific exchange for MLR"
    - "Channel intent gate before MLR chairs"
    - "Is this scientific exchange or promotional leave-behind"
    - "Unsolicited med info versus branded efficacy PDF"
    - "mlr-channel-intent for DE HCP material"
    - "Gate proactive off-label as scientific exchange"
    - "Channel unknown mixed branding and MI letter"
    - "Treat as promo after channel intent conflict"
    - "Scientific exchange without MI request record"
    - "Channel intent human_gate_required for MLR"
---
    # MLR channel intent

    This skill should be used when classifying whether material is promotional, scientific exchange, or medical information before MLR chairs run. It gates ruleset choice and never approves.

    ## When to use
    After `mlr-capability-map` (and after `mlr-channel-intent` when channel is disputed). Before or beside chairs as the funnel dictates. Never as approval.

    ## Instructions

Follow steps below.

## Steps
    1. Read `intake.md` and gather missing fields only.
    2. Follow `references/method.md`.
    3. Prefer offline tools in `references/tools.md`.
    4. Fill Output cards.
    5. Stamp: `python ../../tools/stamp_ready_line.py --skill mlr-channel-intent --letter-lines`

    ## Output cards (required)
    - `../../templates/channel-intent-card.md`
    - `../../templates/liability-line.md`
    - `../../templates/check-line-stamp.md`
    - `../../templates/gap-list.md` when gaps exist

    ## Tasks
    - `classify-channel.md` — Classify promo vs scientific_exchange vs med_info
- `record-reactive-posture.md` — Capture proactive vs unsolicited reactive facts

## Status on close (TEH-RDY-022, TEH-RDY-058, TEH-RDY-061, TEH-RDY-062, TEH-RDY-064)

Precedence rule 1 comes first (`../../references/finding-status-map.md`): any request to approve or clear, or to bypass any hard rule MLR-H1–H8 (for example a request to call a piece scientific exchange to skip ISI, or to assume a channel) → refuse it, `human_gate_required`. Otherwise the status follows the shared map: the gate tool's result is an input, read through its `status` and `status_basis` fields. A missing channel (intent), posture or request record is a missing input (map rule 4) — never a human gate on that ground alone. Exactly one row applies:

| Gate result (`status_basis`) | Gate decision row on the card | Status line |
|---|---|---|
| `judgment` — a genuine call on supplied facts: a piece that mixes promotional and medical-information content, or any content that supports more than one channel/intent reading (`mixed_content` in the gate result; TEH-RDY-061 — quote the conflicting elements from the supplied text, or from the person's description quoted as theirs), a `channel_content_mismatch` rationale (promotional markers in the body, or an unsolicited request answered with promotional material), proactive off-label content declared as scientific exchange, scientific exchange declared with a proactive posture, or a reactive posture the supplied record contradicts | `human_gate_required` | write `Status: human_gate_required` |
| `missing_inputs` — the gate could not classify only because inputs are missing or unmatched (no text or description of the content, no intent, a medium only, no posture, an unrecognized value) and neither the supplied content nor the person's description carries a signal for any reading — incomplete, not mixed | `not classified — pending: <items>`, with each item asked as a question | `Status: findings_only` |
| `provisional` — `treat_as_promo` · `treat_as_scientific_exchange` · `treat_as_med_info` with one or more required fields still open (for example the declared intent, who will use it, audience, off-label answer, the documented unsolicited-request record), including a decision read from the supplied content or the person's description when no intent was declared (TEH-RDY-062, TEH-RDY-064), and a non-promotional reading — unbranded content with no product claims, disease awareness or corporate (the gate's `provisional_reading`; its `decision` stays the not-classified token, never printed) | the gate's `provisional_reading` (same text as `provisional_label`), for example `provisional: treat as promotional — pending: who will use it` | `Status: findings_only` |
| `final` — `treat_as_*` with nothing open | `<decision>` (final) | `Status: findings_only` |

**Mixed content (TEH-RDY-061, owner ruling).** Branded claims plus MI letter fragments in one artefact — or any content that supports more than one channel/intent reading — is a human gate, not a missing input. Quote each conflicting element: from the supplied text, or, when only a description exists, from the person's description (`Person's description: "…"`). Say what the human must decide (which intent the piece serves, or whether to split it). When the content is simply incomplete (one reading only, or no signal for any reading), it is not mixed: rule 4.

**Unknown users (TEH-RDY-062, owner ruling).** When who will use or present the piece is not decided (for example reps vs MSLs), give a provisional decision from the supplied content — `provisional: treat as promotional — pending: who will use it` — `Status: findings_only`, and ask "Who will use or present it?". Who will use it is not an intent and never maps to one; it is a pending item. When content is supplied and carries a reading, never write "not classified".

**Provisional reading whenever a reading exists (TEH-RDY-064).** When the supplied content or the person's description carries a reading, give it provisionally — never "not classified". The readings are: promotional, scientific exchange, medical information, and non-promotional (disease awareness / corporate) — `provisional: non-promotional (disease awareness / corporate) — pending: <items>` for unbranded content with no product claims. A person-stated word for the piece ("a med-info letter", "unbranded disease-awareness slides") counts as a signal: pass it as `described_as`, quote it as theirs, and keep the intent pending — a description is never the declared intent. A non-promotional reading binds no rule pack. "Not classified" is only for content that is missing or carries no signal at all.

Never show a gated decision beside a lower status, and never print the bare `human_gate_required` token as the gate decision when the status is `findings_only`. Never show a provisional decision without the label `provisional — pending: <items>`, naming each open field. Never make a provisional decision final by filling an open field yourself. Shared mapping: `../../references/finding-status-map.md`.

## Intent versus medium (TEH-RDY-057)

The gate's `channel` is the communication intent (the rule-pack key: `promo`, `scientific_exchange`, `med_info`). A delivery medium the person names (email, print, digital display, congress, social) goes in the gate's `medium` field and on the card's Medium row; it never classifies the piece, never counts as an unrecognized channel and never binds a rule pack. Map intent words transparently and say so on the card ("promotional" → `promo`; "scientific exchange" → `scientific_exchange`; the gate returns them in `channel_mapping`). A medium never implies an intent: when only a medium was named, the intent is pending — ask for it.

## Derive gate fields from supplied evidence (TEH-RDY-040)

Before calling the gate, derive its fields from what the person supplied, and pass them:

- **Posture.** An attached or pasted request record from the recipient → `proactive_or_reactive: reactive` and `unsolicited_request_documented: true`. The person stating the piece is pushed or sent unprompted → `proactive`. No request record and no statement → leave both empty.
- **Branding.** Pasted text that names no product or trade name → `branded: false`; a product or trade name in the pasted text → `branded: true`. No text pasted → leave it empty.
- **Claims.** Pasted text with no product claim → `product_claims_present: false`; a product claim → `true`.
- **Off-label.** Only from the person or the pasted text; otherwise leave it empty (the gate reports it as pending).
- **Mixed content (TEH-RDY-061).** When no text was pasted but the person describes a piece that mixes promotional and medical-information content (for example "branded claims and MI letter fragments"), pass `mixed_content: true` and `mixed_elements` quoting the person's own words. Pasted text is read by the gate itself (promotional and MI-letter markers); never pass `mixed_content` from a guess.
- **Description (TEH-RDY-064).** When the person names what the piece is in their own words ("a med-info letter", "unbranded disease-awareness slides"), pass those words as `described_as`. The gate reads them as a signal for a provisional reading only; a description supporting two readings is mixed (TEH-RDY-061).
- **Users (TEH-RDY-062).** When the person says who will use or present the piece is not decided (for example "reps or MSLs, not decided yet"), pass `users` with their words; the gate records it as pending and asks. A known user group is recorded and never classifies.

Refuse to classify only when a required field truly cannot be derived from supplied material. When the gate returns a `treat_as_*` decision with fields still pending, state the classification with its conditions — `<decision> — provisional — pending: <items>` — and say what the human must confirm (the declared channel, the request record against company SOP, off-label status). Never derive a field from a guess, a teaching example or the body of a description (MLR-H1, MLR-H2).

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
- `examples/poor-proactive-offlabel-as-sciex.md`

## Hard rules
- Never approve. Never invent locators or markets.
- Numbered hard rules MLR-H1–H8 (canonical ids): `../../references/hard-rules.md`.
- Jurisdiction required when markets are in scope — no US default. When the person named no markets, ask for them; never list or suggest specific jurisdictions (rule packs are listed once markets are named — MLR-H6 detail).
- Compose VERIFY; do not fork.
