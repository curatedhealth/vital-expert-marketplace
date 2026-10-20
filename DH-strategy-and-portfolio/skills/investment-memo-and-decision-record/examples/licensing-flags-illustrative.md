# Worked example: A2 licensing flags on ILLUSTRATIVE license facts

Run on 20 October 2026 (rerun 20 October 2026 after the technology pool echo, the side-by-side share wording and the GDPR data row were added): `python3 scripts/memo_facts.py flags --deal evals/files/license_deal_illustrative.json`. The license facts are a tester's, not a real transaction; no library call was made (the licensing rows come from `references/licensing-deal-rules.md`). The script prints figures and rows only; the answer around it must still say that whether the parties compete, the market definition, the shares and any exemption are for the owner the person names for legal or competition questions, and must never write "exempt" or "inside the safety zone".

# Transaction and data flags

Your deal facts set beside the sourced figures (`evals/files/license_deal_illustrative.json`). Figures and rows only. Whether the deal is reportable, covered, notifiable or compliant is for the owner you name for legal or compliance, or owner not named. Nothing here says a deal is clear.

| Regime | Your fact | Sourced figure or rule | Rows | How your fact sits |
|---|---|---|---|---|
| HSR | value not given | size-of-transaction USD 133.9 million | DL-045 | not given; ask |
| CFIUS | US individuals with health data: not given | sensitive personal data above one million individuals | DL-056, DL-057 | not given; ask |
| CFIUS | genetic test results held: not given | identifiable genetic test results are sensitive at any count | DL-058 | not given; ask |
| DOJ bulk data | personal health data: not given | bulk threshold more than 10,000 US persons | DL-066 | not given; ask |
| DOJ bulk data | human 'omic data: not given | bulk threshold more than 1,000 US persons | DL-066 | not given; ask |
| DOJ bulk data | human genomic data: not given | bulk threshold more than 100 US persons | DL-066 | not given; ask |
| DOJ bulk data | access by a country of concern or covered person: not given | the rule bites on transactions giving such access | DL-070, DL-071 | for your owner |
| Health data | target HIPAA role: not given | covered entity or business associate: HIPAA breach rules and BAA terms; outside HIPAA, a health app falls under the FTC rule | DL-086 to DL-094, CP-US-44 to CP-US-49, CP-US-54 to CP-US-56 | ask for breach risk assessments and the portal search (DL-087, DL-095) |
| Licensing (EU TTBER) | territory EU | Regulation 316/2014 expired 30 April 2026; Regulation (EU) 2026/877 in force 1 May 2026, expires 30 April 2038 | SP-134, SP-135 | which regulation applies on your dates, and any exemption, is for your owner |
| Licensing (EU TTBER) | competitors: not given | competitors: combined share at most 20%; non-competitors: each party at most 30%, on any relevant market | SP-136 | not given; ask your owner whether the parties compete |
| Licensing (EU TTBER) | in force on 30 April 2026: yes | agreements in force on 30 April 2026 that met the old rules but not the new: prohibition does not apply until 30 April 2027 | SP-137 | transition may be relevant; for your owner |
| Licensing (EU TTBER) | research and development restriction stated | between competitors, hardcore unless indispensable to protect licensed know-how | SP-139 | for your owner |
| Licensing (EU TTBER) | technology pool: no | agreements setting up technology pools are outside the regulation | SP-140 | no pool stated |
| Licensing (EU TTBER) | data licensed | TTBER can apply to data licensing where the data qualifies as an existing technology right such as production know-how | SP-142 | whether your data qualifies is for your owner |
| Licensing (DOJ/FTC 2017) | collective share not given | safety zone: restraint not facially anticompetitive and licensor and licensees at most 20% of each relevant market significantly affected; outside the zone not presumed unlawful | SP-143, SP-144, SP-146, SP-147 | not given; ask |
| Health data (GDPR) | training data licensed (as you state it) | data concerning health is a special category; processing is prohibited unless an Article 9(2) ground applies; member states may add conditions | DL-099, DL-101 (inference), DL-105 | whether the data is health data, and the Article 9(2) ground, are for your owner |
| Licensing (SEC disclosure) | SEC registrant party: yes | material contracts and licenses the business depends on are filed as exhibits (redaction allowed); 8-K Item 1.01 within four business days | SP-130 to SP-133, DL-019 to DL-021 | where the counterparty's terms may appear; disclosure decisions are for your owner |
