# Poor example (fictional asset FX-301)

"FX-301 has patents until 2035, so the asset is free to operate in the US and EU and exclusivity runs to 2035. The license is standard. No issues found."

**What is wrong**
1. States a freedom-to-operate conclusion ("free to operate"): a legal opinion that only counsel gives. validate_register.py rejects it (E_FTO_CONCLUSION).
2. One date copied from the seller's list; no patent term extension or SPC, no regulatory exclusivity, no later-of rule, no source. The calculator would have shown the date as a range of two views.
3. "The license is standard": no clause read; inherited obligations not listed (IP-02 not screened).
4. "No issues found": failure modes not screened; absence of evidence stated as a finding instead of a GAP with its consequence.
5. No question for counsel, no reviewer, no market-by-market view, no note that the EU reform is not yet law.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| "free to operate" | an FTO report asks for a legal opinion on infringement | VP-C-101 |
| one date copied from the seller's list | periods and extensions computed from statutes | VP-C-001, VP-C-010 to VP-C-017, VP-C-060 to VP-C-063 |
| "the license is standard"; no clause read | chain of title and assignment language decide ownership | VP-C-120 to VP-C-122, VP-C-130 |
| no note that the EU reform is not law | the 2023 reform proposal is not law | VP-C-091 |
