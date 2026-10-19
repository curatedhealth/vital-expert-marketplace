# Worked example: A2 pathway precedents for a CBT-I app

Run on live library data, 19 October 2026. Trimmed outputs in `live/insomnia_cbt_calls_2026-10-19.json`. Evidence class M (measured in live calls).

## The request

"We are building a prescription app that delivers CBT for chronic insomnia in adults. Is there a US predicate, and what did similar products do in the US and the EU? Competitors we know: Big Health (Sleepio), Somryst, somnio."

## Calls made

| # | Call | Arguments |
|---|---|---|
| 0 | `regulatory-dh.list_jurisdictions` (free) | none |
| 1 | `regulatory-dh.search_devices` | `{"query": "Big Health", "jurisdiction": "all"}` |
| 2 | `regulatory-dh.search_devices` | `{"query": "Somryst", "jurisdiction": "all"}` |
| 3 | `regulatory-dh.search_devices` | `{"query": "somnio", "jurisdiction": "EU"}` |
| 4 | `regulatory-dh.find_predicates` | `{"product_code": "QVO"}` |
| 5 | `regulatory-dh.find_predicates` | `{"reference": "K191716"}` |
| 6 | `regulatory-dh.get_pathway_precedents` | `{"product_code": "QVO", "jurisdiction": "US"}` |
| 7 | `regulatory-dh.get_pathway_precedents` | `{"product_code": "PWE", "jurisdiction": "US"}` |
| 8 | `regulatory-dh.get_pathway_precedents` | `{"emdn_code": "V92", "jurisdiction": "EU"}` |
| 9 | `regulatory-dh.get_authorization` | `{"reference": "DEN160018"}` |
| 10 | `regulatory-dh.compare_authorizations` | `{"references": ["K191716", "K233577", "DEN160018"], "jurisdiction": "US"}` |
| 11 | `regulatory-dh.get_market_status` | `{"reference": "K233577"}` (the name "Sleepio" returned nothing) |
| 12 | `regulatory-dh.get_market_status` | `{"name": "somnio"}` |

Twelve counted calls, plus one failed name lookup.

## The answer (short mode)

**Answer.** Yes, the records show US predicate candidates. Two devices in FDA product code QVO ("Computerized Behavioral Therapy Device For Insomnia", regulation 882.5801) were cleared through 510(k), and the chain starts at a De Novo granted in another code. In the EU, the one comparable checked (somnio) is CE marked as class IIa; the library stores no EU decision dates.

**Comparables (US)**

| Device | Applicant | Route | Code | Submitted | Decided | Calendar days | Named predicate |
|---|---|---|---|---|---|---|---|
| Sleepio® (K233577) | Big Health, Inc. | 510(k) | QVO | 7 November 2023 | 5 August 2024 | 272 | K191716 |
| Somryst (K191716) | Pear Therapeutics, Inc. | 510(k) | QVO | 26 June 2019 | 23 March 2020 | 271 | DEN160018 |
| reSet (DEN160018) | Pear Therapeutics, Inc. | De Novo (status "DENG") | PWE | 16 May 2016 | 14 September 2017 | 486 | none (De Novo) |
| Daylight (K233872) | Big Health, Inc. | 510(k) | SCP | 7 December 2023 | 30 August 2024 | 267 | K191716 |

Source: FDA records via the library, retrieved 13 October 2026; URLs in the live file. Daylight sits in code SCP; whether it is comparable is the owner's call.

**Predicate candidates.** K233577 and K191716: same product code and regulation number per their records. The records do not show intended use wording or technology; the owner compares those from the summaries (https://www.accessdata.fda.gov/cdrh_docs/pdf23/K233577.pdf, https://www.accessdata.fda.gov/cdrh_docs/pdf19/K191716.pdf) against the test in 21 CFR 807 (same intended use; same technology or different technology raising no different questions, RP US-06). Substantial equivalence is FDA's determination.

**Timing context.** Stored calendar days in QVO: 271 and 272 (n = 2). FDA's published average total time to a 510(k) decision was 141 to 144 days in FY 2023 to FY 2025 (RP US-58). The MDUFA goal of 90 days is counted in FDA days, which exclude time with the sponsor, so it cannot be set against these calendar days. Two precedents are not a forecast.

**EU.** somnio and somnio teens (mementor DE GmbH): CE marked, class IIa, EMDN V92 (Basic UDI-DI PP12257SOMNIO57, retrieved 14 October 2026). V92 holds 1,256 devices in the library, all without a decision date, so no EU timing. The market-status call returned two somnio rows, one with EU authorized and one without; check EUDAMED.

**Gaps.** UK registrations and Swiss devices are not loaded. Sleepio® absent from the EU copy is not proof it lacks a CE mark. "Not assessable" safety counts are not zero.

**Record.** Precedent read as of 19 October 2026. Predicate choice stops for the regulatory owner (owner not named: who is it?). Uncleared.

(Under 450 words. Full version on request.)

## What the run taught

- The name search missed "Sleepio®"; the reference worked. Prefer references.
- Product-code precedents hide the founding De Novo when it sits under another code; follow the chain.
- `analytics.mcda` was also measured in this session for B1, with test scores entered by the build agent (not anyone's judgment). `scripts/mcda_swap_points.py` reproduced the tool's values (80, 57.5, 57.5) and flagged the tie the tool does not report: `mcda_swap_points_2026-10-19.txt`.
