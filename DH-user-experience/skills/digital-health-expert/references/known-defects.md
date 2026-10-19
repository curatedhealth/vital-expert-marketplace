# Known defects in downloaded experts

Observed in the downloads of 19 October 2026 (samd-regulatory-affairs-director, quality-systems-director-software, regulatory-submission-manager-samd). Register items refer to `digital-health-connector-improvements.md`. Tell the person about these before they install; what to keep or delete is their decision.

| # | Defect | Where seen | Register | What the person should do |
|---|---|---|---|---|
| 1 | Prompt leaks internal plumbing: "Record disagreements (trust the foreign key, not legacy text): function_name=... vs de21_function_id=...", "Posture: [GAP] (persona_archetype)", "[GAP] (agent_context_packs)", "[GAP] (autonomy_level)", "Workforce archetype: AL03-PLN" (AL04-DEL on the submission manager) | All three prompts | C15 | Delete these lines; they are not instructions |
| 2 | Work-product sections and elements titled "None (WP-...)" | Director prompts (7 in the regulatory director, 3 in the quality director) | C15 | Delete, or replace with the work products the person actually wants |
| 3 | Unrelated tools listed (UniProt, ChEMBL, PubChem, MyVariant, Open Targets, DailyMed and others); every expert carries the same 32 tools | All three | C15 | Remove tools that do not fit the role or are not connected |
| 4 | 20 of 32 tools have no hosted product and no call route | All three | C15 | Treat as unavailable through VITAL |
| 5 | Counts disagree: "Bound competencies (8)" with six listed; "Tools you can operate (24)" with 32 in the file | Regulatory director, submission manager; tool count in all three | C15 | Ignore the counts; rely on the file's lists |
| 6 | Quality director's prompt names six bound competencies, all regulatory or study-design, while its remit is QMS design and its file carries 24 quality skills | quality-systems-director-software | C14 (register bindings) | Check the skills against the job; use the quality skills |
| 7 | Skill entries with empty Prompt or Template sections or "Prompt: not bound"; pass-rule and miss-owner entries hold only a header | 24 entries in each of the two single downloads | C14 | Use the pack's competency skills for method; the entries are outlines |
| 8 | Template code `ST05-PHARMA-DH-OVERLAY` in a Digital Health pack | Skill entries | C16 | Cosmetic; leave or delete |
| 9 | Key wording conflicts: tool entries say "with its own key"; the note says no second key is needed | All files | C15 | Try the library connector already connected first; ask VITAL before buying another key |
| 10 | Escalation peer named from VITAL's graph (the regulatory director names "Behavioral Science Lead", the quality director "Digital Supply Chain Director", the submission manager "Digital Health Consultant") and a paired human role | All three prompts | C15 | Replace with the person's own accountable owner; if none is named, write "owner not named" and ask |
| 11 | "Service category: Evidence & HEOR" on the regulatory director and the submission manager; "Strategy & Value" on the quality director | All three prompts | C15 | Delete; not used by the assistant |

What stays: the mandate, the "YOU NEVER" stop list, the human-in-the-loop line, the evidence rules ("Every material claim carries graded evidence or an explicit [GAP]"), and the AI disclosure line. These carry the governance.
