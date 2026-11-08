# Workflow — scientific exchange vs promotion gate

Sources: Medicines Australia Scientific Exchange FAQs; PMCPA unsolicited-enquiry guidance; CPS unsolicited-request safe harbor framing (access date 8 November 2026).

1. Run `mlr-channel-intent` before loading promo rulesets.
2. Require explicit **reactive / unsolicited** posture for scientific exchange with off-label or unlicensed content.
3. Proactive off-label / unlicensed → `human_gate_required` (do not auto-route as scientific exchange).
4. If gated as promo → continue READY promo funnel with ISI/fair-balance skill.
5. If gated as scientific exchange / med_info → load matching channel packs; still never approve; still no invented safe-harbor clearance.
