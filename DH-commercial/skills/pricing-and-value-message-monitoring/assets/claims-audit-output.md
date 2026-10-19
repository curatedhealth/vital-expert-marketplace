# Output format: claims audit (flags for the owner, not a clearance)

## Short mode (default for direct questions; 250 to 450 words)

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

1. **Answer:** N claims; Stop, Review, Note counts; the claim that matters most and why, in one sentence. "This audit flags; it does not clear."
2. **Flag table:** Claim · Level · Rows (kind) · Safer draft for the owner.
3. **Evidence:** one line per number or efficacy claim: passage read and direction, or `[GAP]`.
4. **Authorization on file:** the record found (route, class, identifier, source) or `[GAP]`; the intended use used, and whose words.
5. **Record:** "Claims not cleared. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer

### Basis
Material audited, audience, market, intended use (source), authorization record (source, retrieved).

### Claims
| # | Claim (as written) | Audience, market | Type | Rows it may cross (kind) | Inside intended use? | Evidence passage and check | Level |
|---|---|---|---|---|---|---|---|

### Safer drafts for the owner
| # | Claim | Safer draft | What it keeps | What it drops |
|---|---|---|---|---|

### Decisions for the owner
Numbered list: each Stop and Review, each [INDUSTRY] or [WF] row relied on, each gap.

### Calls and record
Calls made with arguments. Library labels from `audit_claims` not used as findings, with the reason. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft. The record covers the audit, not the claims.
