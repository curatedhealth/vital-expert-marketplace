# Workflow — scientific exchange vs promotion gate

Sources: Medicines Australia Scientific Exchange FAQs; PMCPA unsolicited-enquiry guidance; CPS unsolicited-request safe harbor framing (access date 8 November 2026).

1. Run `mlr-channel-intent` before loading promo rulesets.
2. Require explicit **reactive / unsolicited** posture for scientific exchange with off-label or unlicensed content.
3. Proactive off-label / unlicensed → `human_gate_required` (do not auto-route as scientific exchange).
4. If gated as promo → continue READY promo funnel with ISI/fair-balance skill.
5. If gated as scientific exchange / med_info → load the packs matching that intent; still never approve; still no invented safe-harbor clearance.
6. Intent versus medium (TEH-RDY-057): the gate classifies the communication intent; the delivery medium (email, print, congress, social) is recorded and never classifies or binds a pack. Intent, posture or request record not supplied and the supplied content carries no reading → `not classified — pending: <items>`, ask, `Status: findings_only` (TEH-RDY-058). Content that carries one reading, or users not decided (reps vs MSLs) → `provisional: <decision> — pending: <items>`, ask (including who will use it), `Status: findings_only` (TEH-RDY-062). Promotional and medical-information content mixed in one piece → `human_gate_required`, conflicting elements quoted (TEH-RDY-061).

**Inputs (MLR-H1, TEH-RDY-017):** never create stand-in packets, placeholder versions, or chair decisions to make a tool run. When a step's input (artefact version, a chair packet, the validated compile output) is not supplied, stop at that step, say what is missing, close with `Status: findings_only` (or `human_gate_required` when the request asks to approve or clear, or to bypass any hard rule MLR-H1–H8, including an AI owner request — precedence rule 1, `../references/finding-status-map.md`), and do not call later tools — never `mlr_build_prep_record`.

**Close stamp (TEH-RDY-030):** the stamp names the last skill actually run in this answer. When the workflow stops early (a gate, a missing input), stamp the skill where it stopped — never a later skill that did not run.
