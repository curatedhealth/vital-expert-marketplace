# Market intelligence quality: how to check an ecosystem map

Source: the old DH-01.05.2.2 file "Market Intelligence Quality Assessment & Ecosystem Coverage Monitoring" (old pack dh-digital-health-strategy; task sections DH-01.05.2.2.1 "Ecosystem Coverage Monitoring", DH-01.05.2.2.2 "market intelligence pass rule", DH-01.05.2.2.3 "market intelligence miss owner", register codes CF-12.01.05.2.2.1 to .3), the SP rows in `strategy-and-portfolio-research.md`, and the lane rules of `market-and-target-screening` A3 (this pack). Used by task A3 Market intelligence quality check.

## 1. What the old file asked for

The old prompt: "Test whether the market read covers the ecosystem that matters, and list missing segments." The old pass rule method, quoted: "List the elements that count: source, date, and segment covered." "Set a pass or fail for each element on one brief." "Name the element that blocks release if it fails." "Do not score a unit before this rule exists." The old miss owner method: "Name the intelligence owner for each failed element." "State the date the element will be rechecked, or that the unit is stopped." "Do not close a failed element because the existing assessment skill already described it."

These become steps 2 to 6 of task A3. Two changes: the elements, the blocking element and "the ecosystem that matters" are the person's, never the model's; and the owner and recheck date are the person's, in their words.

## 2. The elements a check can read

The three elements the old file names are offered as "proposed" elements when the person has none. Each reads a field the ecosystem map already carries:

| Element (old file's word) | What the check reads in each map entry | Fails when |
|---|---|---|
| Source | A tool and its arguments, or a row id | The entry has no source, or its source is "from your material" with no origin given |
| Date | The retrieval date of the tool output, or the instrument date of a rule row | No date; or older than the maximum age the person sets (no default: "not given" and ask) |
| Segment covered | The lane (buyers, payers, peers, rules) and the segment or jurisdiction of the entry | A lane or jurisdiction the person said matters has no entry, or only a gap |
| Readable source (proposed) | Whether the source is a document a reader can open: a row id resolves to the URL in its row (for example DE34 to the BfArM DiGA page; SP-068 to the EHDS CELEX link); `mi-check` prints the name and URL for every row id it finds | The source is only a row id or tool name (`mi-check --readable-source`); offer the URL from the row; the person decides whether this element applies |

The person may add elements (for example "every peer has a status line read from a primary record"). The model applies only the elements the person confirms.

## 3. Coverage: what "missing" can mean

A lane with no entries is one of three things, and the check says which (wording per `gap-rules.md`):

- **Not loaded.** The store does not hold that source or scheme. On 19 October 2026 the company store held `dtx` only, and FR_LPPR and UK_NICE_NHAP were "gap" with 0 listings, DE_DIGA "partial" (`examples/market-intelligence/list_schemes_2026-10-19.json`). A rerun of `market-access-dh.list_schemes` or `diligence-dh.list_sources` shows whether that changed.
- **Not asked.** The map never ran the lookup (for example no buyers given). The fix is the person's input, not a tool call.
- **Lookup missed.** The lookup ran and returned nothing; absence from the store "is not evidence of absence from the scheme" or the market (`examples/market-intelligence/screen_commercial_peers_dtx_somryst.json`, saved 19 October 2026).

## 4. Dated facts that move a map's rules lane

A rules entry that was right on its date can go stale. The check rereads these against the map's date (rows from `strategy-and-portfolio-research.md`, read 20 October 2026):

| Instrument | Dated fact | Rows |
|---|---|---|
| EHDS, Regulation (EU) 2025/327 | Applies from 26 March 2027; primary-use and EHR system rules from 26 March 2029 and 26 March 2031 by data category; Chapter IV (secondary use) from 26 March 2029; implementing acts due by 26 March 2027 | SP-068 to SP-073 |
| WHO Global strategy on digital health 2020-2025 | Extended to 2027 by WHA78 (27 May 2025); a 2028-2033 strategy goes to the 80th World Health Assembly in 2027, not yet adopted | SP-066 |
| WHO classification of digital interventions | The 2018 first edition is superseded by the 2023 second edition with a new title | SP-054 to SP-057; SP "Changes and conflicts" |
| EU Technology Transfer Block Exemption | Regulation 316/2014 expired 30 April 2026; Regulation (EU) 2026/877 applies from 1 May 2026 to 30 April 2038, transition to 30 April 2027 | SP-134 to SP-137 |

Other dated rule changes for a pipeline (HSR, AI Act, EU and Swiss screening, UK accounts, DiGA directory) are read in A2 from `monitoring-signals.md`.

## 5. What the check never does

- It never sets the elements, the maximum age, the lanes that matter, the blocking element, the owner or the recheck date.
- It never scores the map or its author; it marks elements pass, fail or not measurable on the person's rule.
- It never fills a missing lane from memory or proposes a buyer, payer or peer; the next step for a missing lane is a named lookup or a question to the person.
- It never supplies a market size, share or growth figure (DL and SP "Not sourced").
- It never takes a peer's holder or status from press. For a peer entry, note that the holder is as stored by the applicant and that a predecessor name can hide a later owner (DL-133 (inference)). Where `named-company-status.md` covers the company or product, add what the filings and FDA records state, with source and date (Somryst: current FDA listing holder Nox Medical, listing created 18 December 2024, SP-167; Pear Therapeutics: chapter 11, Pear 8-K, 7 April 2023, SP-156 [WF]); status stays "[GAP]: not read" only for companies no row covers.
- It never presents a whole-directory figure as indication-specific: an entry resting on DE33 or DE34 covers every DiGA, not the person's indication.
- It never lets a lane pass on count alone without saying what its entries hold: a rules lane with only EHDS and deal rows has no device or DiGA rules (route device rules to `dh-regulatory-and-quality` regulatory-pathway-and-classification). This is a note, not a fail, unless the person's rule says so.
