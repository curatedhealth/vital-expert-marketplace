# Output format: positioning check set and artifact sample

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** how many in-market artifacts carry the line as written, how many altered, how many absent, and the most serious flag.
2. **Per artifact:** Artifact · Line present, altered or absent · Quoted sentence (if altered or contradicting) · Top flag (row).
3. **Not measurable or not scored:** artifacts with no in-market copy, drafts.
4. **Stop:** flagged claims to the claims audit (DH-02.01.3.2), then the regulatory or legal owner as you named them.
5. **Record:** "Sample draft. Flags are signals, not verdicts." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
6. One line offering the full version.

## Full mode

### Check set (yours)
| Artifact | Segment | Line it must carry | Pass rule (your words) | Sampler | How often |
|---|---|---|---|---|---|

### Sample
| Artifact | In market? | Line status | Best matching sentence | Similarity (if computed) |
|---|---|---|---|---|

### Flags
| Artifact | Sentence | Flag | Rule and row | Note ([INDUSTRY], [WF]) |
|---|---|---|---|---|

### Contradicted claims (against your claim list)
| Artifact | Sentence | Claim on list or not | Note |
|---|---|---|---|

### Gaps

### Record
Sample draft. No artifact cleared. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
