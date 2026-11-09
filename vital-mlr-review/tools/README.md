# Offline READY tools

Non-generative CLIs mirroring MCP `mlr_*` tools, plus pre-chair helpers. Run from this directory:

```bash
python3 mlr_intake_offline.py --help
python3 channel_intent_gate.py --args-json '{"channel":"scientific_exchange","proactive_or_reactive":"proactive","offlabel_or_unlicensed":"yes"}'
python3 mlr_claims_matrix_offline.py --help
python3 check_isi_presence.py --text 'Efficacy headline. Important Safety Information...'
python3 stamp_ready_line.py --skill mlr-intake --letter-lines
```

| CLI | Role |
|---|---|
| `mlr_*_offline.py` (9) | MCP parity (except `my_usage`) |
| `channel_intent_gate.py` | Promo / scientific exchange / med_info structural gate |
| `mlr_claims_matrix_offline.py` | Claims matrix + align merge |
| `check_isi_presence.py` | ISI / fair-balance heuristic scan |
| `check_submission_pack.py` | Submission-pack completeness; refuses 2253 filing fields |\n| `stamp_ready_line.py` / `render_board_pack.py` / `structural_mlr_checks.py` | Shared stamps |

Tests: `python3 -m unittest test_offline_tools -v`  
Forbidden scan: `python3 ../scripts/scan_forbidden_in_examples.py`

See plugin `references/mcp-opt-in.md` for optional live connectors.

`channel_intent_gate.py` optional inputs `branded` and `product_claims_present` (TEH-RDY-040): set only from person-supplied evidence. With no declared channel, a reactive posture with a documented request, non-branded, no product claims and no promo markers returns a provisional `treat_as_med_info` (`channel` stays in `gaps`). Output fields and decision values unchanged.

`render_board_pack.py` (TEH-RDY-041) reads the compile-packet schema fields and prints the packet's own `mlr_status`.

Intent versus medium (TEH-RDY-057/058). `channel` is the communication intent, the rule-pack catalogue key (`promo`, `scientific_exchange`; `med_info`, `other` carry no pack). The delivery medium (email, print, digital display, congress, social …) is recorded and never binds a pack. `mlr_intake`, `mlr_list_rulesets`, `mlr_get_ruleset` and `channel_intent_gate.py` accept optional `intent` and `medium` inputs, split the supplied words with `contract.split_channel`, map common intent words transparently ("promotional" → `promo`) and return optional `medium` and `channel_mapping` fields (intake also `context.medium`). A medium alone leaves the intent missing (`missing_fields: channel`, bind-later line) — never an unrecognized channel. The gate adds optional `status`, `status_basis` (`judgment` · `missing_inputs` · `provisional` · `final`) and `pending`: `human_gate_required` only on a judgment call on supplied facts; missing inputs → `findings_only`. Existing fields, decision values and statuses are unchanged.

Mixed content and unknown users (TEH-RDY-061/062, owner rulings). `channel_intent_gate.py` accepts optional `mixed_content` + `mixed_elements` (a mix the person described, quoted from their words) and `users` (alias `intended_users`: who will use or present the piece). Supplied text with both promotional markers and medical-information letter markers, or a described mix, returns `human_gate_required` with `status_basis: judgment` and an optional `mixed_content` field quoting the conflicting elements. With no declared intent, content that carries one reading returns a provisional `treat_as_*` (`status_basis: provisional`, `findings_only`) with an optional `provisional_label` (for example `provisional: treat as promotional — pending: who will use it`); users not decided add the pending item `users`. Optional `questions` lists each pending item as a question. Content with no signal for any reading stays `missing_inputs`. Existing fields and decision values unchanged.

Provisional reading (TEH-RDY-064). Optional input `described_as` (the person's own words for the piece, a signal only — never the declared intent) and optional output `provisional_reading`: the provisional reading whenever supplied content, derived fields or the description carry one, including `provisional: non-promotional (disease awareness / corporate) — pending: …` (unbranded, no product claims, disease-awareness or corporate markers; `status_basis: provisional`, `decision` unchanged). None when no reading exists.
