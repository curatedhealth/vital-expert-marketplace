# Financial register: FICTIONAL Aurelian Bio Inc. (investor, mode investor, markets US)

Reviewers: accountant UNSIGNED; tax UNSIGNED; counsel UNSIGNED    Status: Draft
Quality of earnings: HUMAN ONLY    Net debt definition: HUMAN ONLY    Accounting opinion: HUMAN ONLY    Tax opinion: HUMAN ONLY
(Every name, figure and filing here is FICTIONAL. Currency units are illustrative.)

## Answer first
- Cash and runway: liquid cash 120 at 30 June 2026 (restricted 4 excluded). Base runway 10.0 months to 30 April 2027 on trailing operating cash flow (10 a month, source: FICTIONAL 10-Q); with a 25% higher burn and the contingent licensor milestone paid, 9.08 months to 1 April 2027; with the planned follow-on (80, expected, not closed) 18.0 months. Both the Item 303(b)(1) 12-month horizon (FIN-HORIZON-12M) and the auditor's one-year horizon (FIN-AUDITOR-1Y) are flagged in the first two scenarios. The filed 10-Q quotes substantial-doubt language (section "Going concern").
- The seller's deck says "runway into 2028"; the 10-Q liquidity section says cash is sufficient "into the second quarter of 2027". Inconsistent: the 2028 figure needs the follow-on to close. Question below.
- The licence for FX-601 (FICTIONAL University X) lets the licensor terminate for a lump sum if the licensee is not the surviving entity in a merger (clause 11): passes to buyer: needs consent. Tax: the supplied ownership shifts total 62 points in the 3-year testing period, more than 50; a tax specialist decides.

## Cash, runway and going-concern language
| Item | Figure | Period / date | Rule id | Source |
|---|---|---|---|---|
| Cash and equivalents plus marketable securities | 120 | 30 Jun 2026 | n/a | F-2 FICTIONAL 10-Q balance sheet |
| Going-concern language | quoted: "these conditions raise substantial doubt about our ability to continue as a going concern within one year after the date the financial statements are issued" | 30 Jun 2026 | FIN-AUDITOR-1Y | F-2 note 1 |
| Management look-ahead from issuance (ASC 205-40) | not applied | n/a | FIN-ASC205-40-ISSUE disabled: [CHECK] | none |

## Runway scenarios
| Scenario | Burn multiplier | Included items | Runway (months) | Cash-out date | Flags |
|---|---|---|---|---|---|
| base | 1.0 | scheduled debt (20, due 31 Mar 2027) | 10.0 | 30 Apr 2027 | FIN-HORIZON-12M, FIN-AUDITOR-1Y |
| burn +25%, milestone paid | 1.25 | plus contingent licensor milestone (5, 15 Dec 2026) | 9.08 | 1 Apr 2027 | same |
| planned raise closes | 1.0 | plus expected follow-on (80, 31 Oct 2026) | 18.0 | 30 Dec 2027 | none |
Convention: calendar months from the period end; events applied at month end; linear inside the cash-out month.

## Upstream licensor obligations
| Licensor | Agreement | Type | Trigger | Amount or rate | Passes to buyer | Source |
|---|---|---|---|---|---|---|
| FICTIONAL University X | 2021 licence for FX-601 | milestone | first patient dosed in Phase 3 | 5 | needs consent | F-4 section 4.2 |
| FICTIONAL University X | same | change_of_control | merger in which the licensee is not the surviving entity | licensor option to terminate for a lump sum | needs consent | F-4 section 11 |

## Failure-mode screen
| Mode | State | Register ref or reason | Gap |
|---|---|---|---|
| FE-01 | triggered | licensor_obligations[1] | |
| FE-02 | cannot tell | | no valuation basis for the asset was supplied |
| FE-03 | not triggered | the data-room index matches the list of exhibits the 10-K references | |
| FE-04 | triggered | going_concern | |

## Questions
1. Counsel: does the licensor's lump-sum termination option apply to this transaction structure, and can consent be sought before signing?
2. Tax specialist: has an ownership change occurred in the 3-year testing period, and what annual limitation would apply?
3. Accountant (and the seller): what financing is assumed in the "into 2028" claim, and is any of it closed?

## Open items
[CHECK]: management look-ahead (ASC 205-40) not applied.  [GAP]: asset valuation basis (blocks FE-02).  Decisions needed (owner): whether to price the licensor termination risk into the bid (buyer deal lead).  Hand-off: licensor obligations to cross-check against the ownership and license chain in assess-ip-portfolio-and-freedom-to-operate.

## Fact patterns and the real precedents they follow
Every fact below is fictional. The pattern behind it is documented in a registered passage of this skill's `references/verbatim-passages.json` (or of the skill named); the real names behind the passages are in the local appendix `docs/due_diligence/EXAMPLES_REAL_PRECEDENTS.md` (not shipped).

| Fact in the example | Pattern documented in | Passage ids |
|---|---|---|
| cash is exhausted inside 12 months of the period end; the filing must discuss the course of action | Item 303 liquidity horizon and known trends | VP-E-001, VP-E-003 |
| filed going-concern language quoted; one year beyond the statements | PCAOB AS 2415 horizon | VP-E-050, VP-E-051 |
| ASC 205-40 look-ahead not applied: rule disabled | the FASB text could not be opened | none (SUMMARY-ONLY row E3) |
| a licensor milestone and a change-of-control clause; a redacted term is a GAP with a request for the unredacted agreement | Item 601(b)(10) redaction and the Commission's power to require disclosure | VP-E-010 to VP-E-013 |
| ownership shifts of 62 points: section 382 flag; the 80 percent cap and the IRS rate source named | section 382 and 172; Rev. Rul. 2019-04 Table 3 | VP-E-020 to VP-E-025 |
| IPR&D treatment is a specialist flag; contingencies are the accountant's | practitioner articles, not standards | VP-E-030 to VP-E-034 |
| seller deck says "into 2028" against the 10-Q language: a seller's statement is a claim to cross-check | a seller's regulatory representations breached; the record controls | VP-D-090 (skill D) |
