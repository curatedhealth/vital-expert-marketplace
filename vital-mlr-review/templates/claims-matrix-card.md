# Claims matrix (pre-chair)

| Claim ID | Verbatim claim | Type | Authorised-use bind (jurisdiction) | Evidence locator | Fair-balance / ISI pairing | Status |
|---|---|---|---|---|---|---|
| C-001 | | efficacy/safety/other | | e.g. Study/pg/col/para | | draft / aligned / gap / exceeds |

Rules: verbatim claim text quoted from what the person supplied — no artefact text supplied → `[GAP]`, never a composed span (TEH-RDY-026); jurisdiction bind only for supplied markets (TEH-RDY-024), each naming that market's label document from `references/label-basis-by-market.md` (not listed: "authorized labeling for <market>") — never another market's document name (TEH-RDY-038); retire never delete; no invented locators.
Row checklist (every row, against the supplied source passage; TEH-RDY-049):
- Comparator: the source names a comparator (for example placebo, an active drug, standard of care) that the claim does not state → flag the row: "comparator in source (<as quoted>) absent from claim".
- Framing: the claim gives a relative effect (for example a percent reduction) where the source also gives, or the claim omits, the absolute values → flag the row: "relative framing — absolute values <as quoted, or [GAP]>"; an absolute claim with no supplied absolute figures → `[GAP]`.
- Population, endpoint, time point and interval stated in the source but absent from the claim → flag each as missing from the claim.
- Flags quote the supplied source; nothing is filled from memory. A flag is an observation for the chairs to judge, not a verdict.
Liability: This prepares material for human MLR review. It is not medical, legal, or regulatory approval.
