# Worked run: A2 fidelity sample and B1 repair, on live library data and illustrative files

Run on 20 October 2026. The request: "Release 2.3 of FocusPlay is ready for review. Here is the store copy and a week-by-week usage export. Check it against the STARS-ADHD evidence and our regimen of 5 sessions a week for 4 weeks, minimum 25 minutes. Our medical lead, Dr. Amira Haddad, owns claims; product owner Jonas Weber owns release." FocusPlay, its copy, the usage export and the named people are illustrative, written for this example. STARS-ADHD, EndeavorRx and reSET are real and were read live. Calls and outputs: `examples/live/connector_calls_2026-10-20.json`.

Calls and runs in order: `verify.extract_claims` (store copy), `verify.qualify_source` (STARS-ADHD DOI; the De Novo PDF URL), `verify.check_claim` (four claims), `regulatory-dh.search_safety_events {product_code: "PWE"}` (named precedent for rule checks), `python3 scripts/fidelity_sample.py claims focusplay-claim-sample.csv --shipped 9`, `python3 scripts/fidelity_sample.py adherence usage-log-illustrative.csv --sessions-per-week 5 --weeks 4 --min-minutes 25 --enrolled 10`.

---

## Short mode output (as handed to the person)

**Answer.** Version 2.3, read 20 October 2026. Sample: 5 of 9 shipped claims (56 percent); the other 4 were not checked. Three claims differ from their source, one has no source, one matches in substance. Delivered dose: mean 62 percent of expected sessions, coverage 7 of 10 enrolled. Framework: Carroll adherence (TM102, DOI 10.1186/1748-5908-2-40). No pass rules set yet: differences are quoted for Dr. Amira Haddad to mark.

| Claim | Product text | Source passage | Words that differ | Type (for the person to mark) |
|---|---|---|---|---|
| c1 | "game-based therapy for children with ADHD" | "aged 8-12 years, without disorder-related medications" (PMID 33334505, Methods) | source only: aged, 8, 12, without, medications | wider population |
| c2 | "Clinically proven to improve attention in 4 weeks" | "might be used to improve objectively measured inattention" (Interpretation) | source only: might, objectively, measured; product only: clinically, proven | stronger verb |
| c3 | "25 minutes a day, 5 days a week" | "25 min per day, 5 days per week for 4 weeks" (Background) | source only: 4 weeks | matches in substance; duration omitted |
| c4 | "Not a replacement for medication." | none on file | | no source |
| c5 | "Helps kids with hyperactivity and impulsivity" | "may not display benefits in typical behavioral symptoms, such as hyperactivity" (TM144) | source only: may, not | missing caveat; reversed |

**Verify.** It returned "supported" for c2's unhedged verb (89 percent overlap) and for the negation of the source sentence (90 percent): overlap scoring, not a pass (N3). The De Novo summary was rated inadmissible (C1); c5 was compared by hand.

**Decision rules.** No rule evidence supplied [GAP]. Precedent for what to check: FDA Class II recalls of reSET and reSET-O, 7 June 2021, describe reward access "regardless of the UDS results" where the specified rule rewarded negative screens (TM135).

**Dose (illustrative log).** Per user: 0 to 100 percent of 20 expected sessions; median 70. Three of 8 users averaged 25 minutes or more per session. Thresholds: Jonas Weber's to set.

**Repair (B1, proposed until confirmed).** c1, c2, c5: product text changes to the source wording; owner Dr. Amira Haddad. c4: add a source to the claim map (evidence-to-intervention translation) or remove the line. Which version must not ship the failed text: Jonas Weber decides. Release records: `dh-regulatory-and-quality` document-and-change-control.

**Record.** Fidelity sample draft. AI-assisted. Clears it: Dr. Amira Haddad. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

**Calls made.** Listed above.

---

Word count of the short mode output above, without the calls list: 422 (counted by script on 20 October 2026). The table has no source column; the source passages are counted.
