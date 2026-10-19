# Output format: growth offer

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words and write 'Words: N' as the first line of the Calls made list. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. State each fact once. Open questions: at most three. One line per item; a rule column holds the row ids and at most fifteen words.

## Short mode (default for a direct question)

Budget: answer 50, elements 150, claims 120, questions 50, record 40. The format itself fits under 450 words; do not add sections.

1. **Answer** (at most 50 words): per account, the offer elements that stop for your compliance or legal owner and the claims that need your regulatory owner.
2. **Offer elements** (one line each, only the elements in the offer): Element (your words): rows; missing fact; stops for [owner as named, or owner not named]. A value case, if run, is one line: inputs yours, result, "hypothesis", or `[GAP]` if the calculator refused.
3. **Claims** (one line each, only the claims in the question): Claim: rows; issue in at most fifteen words; draft for the owner: safer wording.
4. **Open questions** (at most three, one line each): for example Federal program payment, owners not named.
5. **Record:** Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. One line offering the full version.

**Refusal (any task, same cap):** (1) what is declined and why, one line with the rows; (2) the elements or figures behind it, one line each, at most five; (3) "Draft for the owner", at most 120 words, holding only facts the person stated and figures from the run, never a commitment they did not make; (4) the record line.

## Full mode

### Answer

### The offer
| Account | Module, site or population | Result seen it builds on | Your rule checks (SR5 to SR8, if adopted) |
|---|---|---|---|

### Who uses, buys and pays (as you stated)
User · Buyer · Payer · Federal program payment: as your compliance owner determines

### Offer elements and the rules they meet
| Element (your words) | Type (offer-rules.md) | Rows | What the rule requires | Facts you gave | Facts missing | Stops for |
|---|---|---|---|---|---|---|

### Authorization record (library)
Route · Class · Product code · Regulation · Decision date · Source URL, as the record states them; or "no authorization in the library for this reference; absence is not evidence of none".

### Value case (only if asked)
| Input (yours or adopted, with tool) | Value | Calculator | Result | Label |
|---|---|---|---|---|
Hypothesis on your numbers. A refused calculator or an unexposed tool is `[GAP]`.

### Claims in the materials
| Claim as written | Audience | Rows | What the row requires | Missing | Draft for the owner |
|---|---|---|---|---|---|

### Gaps

### Calls
`commercial-dh.audit_claims` (authorization record only); `commercial-dh.map_money_flow` if used.

### Record
Offer draft for the owner. No element is called protected or compliant; no claim is cleared. Industry codes are labeled as codes, not law. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
