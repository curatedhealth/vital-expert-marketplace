# Output format: product portfolio choice list

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Short mode (default for a direct question)

1. **Answer:** Forum · period · items ready (n) · items not ready (n) · the gap that blocks most.
2. **Ready items:** Item · Ask (continue, stop, delay) · Stage as you stated it · Stage gate record (ref, date) · Key facts with source and date · Gaps.
3. **Not ready:** Item · Reason (for example "no stage gate record") · Route (pack and skill).
4. **Licensing items (if any):** Item · Counterparty · Company status line (the filings read, each by name and date, for example "Pear 8-K, 7 April 2023 (SP-156)", with what the form does not mean; or "Company status [GAP]: not read" with the filings to open, most recent first) · Authorized to (FDA record) and listed today by (FDA registration and listing), as two facts · Overlap with an item on your list and the competitor question · Flags, each by source name and date then row (for example "Regulation (EU) 2026/877 of 16 April 2026 (SP-135)") · Each threshold beside your figure, or "not given" · Deal facts not given · For the owner you name for legal, or owner not named.
5. **Needed before ranking:** your criteria, weights and scores; missing facts per item; capacity (amount, unit, period).
6. One line offering the full version.
7. **Record:** "Choice list draft. Which items come to the forum is yours." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

Calls made (after the record line): each library call with its arguments and retrieval date, or "no library call".

## Full mode

### Forum and scope
Forum, period, as you gave them. Product portfolio only (your company's own products and programs); any investment holding moved to `investment-portfolio-monitoring` (this pack).

### Choice list
| Item | Ask | Stage (yours) | Stage gate record | Evidence (yours, dated) | Regulatory status | Readiness level (proposed, EU wording) | Capacity ask | Source | Rows |
|---|---|---|---|---|---|---|---|---|---|

### Benchmarks as context (only if asked)
| Figure | Counting method and dataset | Rows (with DOI) | Note |
|---|---|---|---|
Note column always reads: "context, not your probability".

### Delay routes (only where the ask is delay pending evidence)
Route · What it is · Rows · Who decides if it applies (`dh-regulatory-and-quality` regulatory-pathway-and-classification).

### Licensing, partnering and acquisition flags
Per item: rule, instrument and date, condition; each threshold beside your figure (or "not given"), without leaning; overlap with your own items and the competitor question; GDPR Article 9 if health data moves (DL-101, DL-105, DL-106); deal facts not given; owner for legal as you named, or owner not named. Company status line per counterparty, from the dated filings; the authorized company and the current FDA listing holder stated separately. No license called exempt.

### Not ready for this forum
| Item | Reason | Route |
|---|---|---|

### Open questions before ranking

### Record
Choice list draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
