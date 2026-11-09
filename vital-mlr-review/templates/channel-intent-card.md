# Channel-intent card

"Channel" on this card is the communication **intent** — the rule-pack key in `rulesets/REGISTRY.json`. The **medium** is how the piece is delivered; it is recorded and never binds a pack (TEH-RDY-057).

| Field | Value |
|---|---|
| Intent (rule-pack channel) | promo / scientific_exchange / med_info / other / [GAP] — as declared; report any mapping from the person's words (for example `promotional → promo`) |
| Medium (recorded; never binds a pack) | as the person named it (email, print, digital display, congress, social …) or [GAP] — never read as an unrecognized channel |
| Audience | hcp / patient / payer / internal / mixed |
| Proactive or reactive? | proactive / reactive (unsolicited request) |
| Off-label or unlicensed content present? | yes / no / [GAP] |
| Who will use it? | as the person named it (for example reps, MSLs) · not decided → pending item, asked below (TEH-RDY-062); never an intent |
| Mixed content? | no · yes → quote each conflicting element (promotional / medical information) from the supplied text, or from the person's description as theirs (TEH-RDY-061) |
| Gate decision | Take the row from the gate's `status_basis` (TEH-RDY-058). `judgment` → `human_gate_required` (→ `Status: human_gate_required`), including mixed promotional / medical-information content (TEH-RDY-061) · `missing_inputs` → `not classified — pending: <items>` (→ `Status: findings_only`; only when the content is incomplete and carries no reading; never print the bare gate token beside it) · `provisional` → `<decision> — provisional — pending: <items>`, worded as the gate's `provisional_reading` / `provisional_label` — including `provisional: non-promotional (disease awareness / corporate) — pending: <items>` for unbranded content with no product claims, and a reading from the person's own description of the piece (TEH-RDY-064); never "not classified" when content or description carries a reading, for example `provisional: treat as promotional — pending: who will use it` (→ `Status: findings_only`; TEH-RDY-062) · `final` → `<decision>` (→ `Status: findings_only`) |
| Ruleset implication | packs bind on market + audience + intent; none until all three are supplied |
| Questions for the person | each pending item as a question (intent, who will use it, posture, request record, off-label status) — the gate returns them in `questions` |
| Gaps | |

Never approve. Stamp READY-local when offline.
