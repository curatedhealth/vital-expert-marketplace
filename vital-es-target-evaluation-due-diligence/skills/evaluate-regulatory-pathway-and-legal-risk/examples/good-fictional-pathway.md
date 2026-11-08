# Good example (fictional asset FX-401; not a real product, company or filing)

Inputs: evals/fixtures/good-pathway.json; investor buyer; asset unit; US and EU. Upstream outputs: signed clinical register (reviewer and date recorded), ranges (final number UNSIGNED), exclusivity register (UNSIGNED).

**Answer first**
- US: keep standard and priority review open (priority: PR1 met on register row R1; PR2 is a gap, no head-to-head data). Accelerated approval is a candidate only if a confirmatory trial is agreed: the plan has none, and the January 2025 draft guidance says FDA generally intends to require it underway before approval (DRAFT, R3). [rules us_priority_review, us_accelerated_approval]
- EU: conditional authorisation is a candidate (CM1 and CM3 met on the register; CM2 and CM4 gaps); accelerated assessment cannot be judged (both criteria gaps). EU pharma reform is not yet law: current rules used. [rules eu_conditional_ma, eu_accelerated_assessment]
- Three risks that matter most: (K1) the seller's press release says the filing is on track and no regulator correspondence was supplied, so the statement cannot be compared with the record (RL-01); (K2) drug substance comes from a contract site with no inspection history supplied (RL-02); (K3) a paragraph IV notice letter carried from the exclusivity register. Counsel decides what each means.
- Route choice and legal opinion: HUMAN ONLY. Status UNSIGNED.

**Investor view (options only).** The route that sets the next value inflection is the filing date; ask for regulator minutes and the site's inspection reports before any timeline is relied on; the timeline in skill B assumed standard review.

**Why this is good:** every criterion of every route is assessed and "met" cites the register; the draft guidance is marked; missing records are gaps that say what they hide; no outcome is stated as certain.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| priority review needs a significant improvement; PR2 is a gap | FDA expedited programs guidance | VP-D-004, VP-D-005 |
| accelerated approval only if a confirmatory trial is agreed; the January 2025 draft is marked DRAFT | FDA draft: confirmatory trial underway prior to approval | VP-D-011, VP-D-012 |
| conditional authorisation criteria CM1 and CM3 met, CM2 and CM4 gaps | EMA conditional marketing authorisation criteria | VP-D-023, VP-D-029 |
| accelerated assessment cannot be judged | EMA accelerated assessment | VP-D-021, VP-D-022, VP-D-033 |
| the press release says the filing is on track; no regulator correspondence supplied (RL-01) | press release statements versus complete response letters; the letters are at openFDA | VP-D-050 to VP-D-053, VP-D-080 to VP-D-082 |
| drug substance from a site without inspection history (RL-02) | inspection classifications and the limits of the public database; data integrity | VP-D-060 to VP-D-063, VP-D-070, VP-D-071 |
| route choice and legal opinion are human only | legal conclusions are counsel's; a seller's regulatory representations can be breached | VP-D-090 |
