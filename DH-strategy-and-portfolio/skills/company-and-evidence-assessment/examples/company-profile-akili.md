# Worked example: A1 company profile and A2 evidence read on saved live data (Akili)

**Request (illustrative investor, real company):** "We're screening Akili Interactive Labs. Pull what the public record shows and tell me how mature their evidence is. Their lead product is a game-based treatment for children with ADHD. We look at US and UK. Owner: Jonas Weber, partner."

Data: saved live outputs of 19 October 2026 (`examples/live/build_company_profile_akili_2026-10-19.json`), read 20 October 2026; tables from `python3 scripts/profile_table.py` (`examples/live/profile_table_akili_2026-10-19.md`). The connector was disconnected during this build, so no new call was made.

---

**Answer.** "Akili Interactive Labs, Inc." resolves by normalized legal name to one FDA applicant with three authorizations under product code QFT (regulation 882.5803), 10 registered studies (3 naming the brand) and two Form D filings. The library's evidence score is 100 (90 of 90 assessable points) with reimbursement and jurisdiction breadth excluded; it is a convention, not a level. Status: Akili became a wholly owned subsidiary of Virtual Therapeutics in July 2024 (Akili 8-K, 2 July 2024, SP-151 [WF]). The largest gap: no UK company register in the library.

**Authorizations (retrieved 19 October 2026)**

| Product | Record | Pathway | Decision |
|---|---|---|---|
| EndeavorRx | DEN200026 | De Novo, granted (raw code DENG) | 15 June 2020 |
| EndeavorRx | K231337 | 510(k), substantially equivalent | 13 December 2023 |
| EndeavorOTC | K233496 | 510(k), substantially equivalent | 14 June 2024 |

A 510(k) is a clearance, not an approval (DL-128). Sources: FDA URLs in the saved file.

**Filings.** Form D, 23 May 2018, USD 55,000,010 sold as stated; Form D, 9 June 2021, USD 110,000,007. A Form D date tracks the first sale (DL-002), the amount may be stale (DL-006), and the form shows no valuation or investor names (DL-018 (inference)). Private rounds stay `[GAP]`.

**Studies.** 10 registered (3 by brand, 6 by indication only); registry rows, not publications.

**Evidence maturity.** Library score at full points on every assessable component; round(100 x 90 / 90) = 100. "A stated convention for comparing documented evidence, not a predictive model or a valuation."

| Framework | Proposed | Limits | Rows |
|---|---|---|---|
| NICE ESF | Tier C (treats a condition, as you describe it), proposed | Classifies purpose, not evidence; voluntary | UK12, HE-084, HE-079 |
| Evidence DEFINED | Not assessable until the studies are graded `[GAP]` | Not built for investors | DL-107, DL-108, DOI 10.1038/s41746-023-00836-5 |
| V3 | Does not apply (no sensor-derived measure described) | BioMeTs only | CV156, DOI 10.1038/s41746-020-0260-4 |

**Safety and status.** Saved `compare_portfolio` (19 October 2026): Akili `safety_events` none_found, that is, none found in the loaded enforcement source; not proof of none. Status, as read on 20 October 2026 (`named-company-status.md`; SEC rows [WF]): stored Form Ds sit under CIK 0001741200; the listed registrant is Akili, Inc. (CIK 1850266; SP-148). Merger agreement with Virtual Therapeutics (Akili 8-K, 29 May 2024, SP-150); offer completed and change in control (Akili 8-K, 2 July 2024, SP-151); Form 15, 12 July 2024, not dissolution (SP-154; DL-149 (inference)). EndeavorRx is now listed c/o Virtual Therapeutics (SP-168).

**Not in the library.** Companies House ("API key not yet provisioned"); private funding rounds; reimbursement.

**Gaps and stops.** Grading the studies: `dh-clinical-development` literature-and-real-world-evidence-review. No view on whether to invest.

Full version on request.

**Calls made (saved, 19 October 2026):** `diligence-dh.build_company_profile {company: "Akili Interactive Labs, Inc."}`; `diligence-dh.compare_portfolio {companies: ["Somryst", "Big Health", "Akili Interactive Labs, Inc."]}` (safety events); perimeter from `commercial-dh.list_commercial_dh_sources {}` (`diligence-dh.list_sources` needs a live check). No unpublished name was sent to the library. Research rows read 20 October 2026, no call.

**Record.** Company profile and evidence read draft for Jonas Weber. AI-assisted. Clears it: Jonas Weber, partner. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

---

Word count of the answer above (between the rules, without the calls list and the tables' source column), counted with `python3 scripts/profile_table.py --count` on 20 October 2026 after the status revision: 445 (including tables and the record line), under 450.
