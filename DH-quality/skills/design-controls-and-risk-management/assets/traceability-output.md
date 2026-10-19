# Output format: design inputs and traceability

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line.

## Short mode (default for a direct question)

1. **Answer:** two or three sentences. For a rules question: what applies in each named market and the one caveat that matters most (often: IEC 62304 gives no presumption under the MDR). For a trace check: how many items were read and how many findings of which kind.
2. **Table:** either the rules (Market · Rule · What it means for the team · Row) or the findings (Item · Code · What is missing or broken).
3. **Open items:** at most three lines, including any `[GAP]` for clause text or a missing record.
4. **Record:** one line ("Findings, not a compliance verdict. Uncleared AI-assisted draft." or the clearer's name).

End with one offer: the full version, or the next task (risk management file).

## Full mode (design review input, document to share)

### Answer
Finding first, as in the short mode.

### Rule base by market
| Market | Rule | What it means for the design file | Row |
|---|---|---|---|

### IEC 62304 and IEC 82304-1 status
| Standard | US | EU | What it does not cover | Rows |
|---|---|---|---|---|

### Proposed design inputs from regulatory requirements
| Id (proposed) | Design input, testable | Origin (regulation or standard) | Row | Status: proposed |
|---|---|---|---|---|

### Column mapping used
Person's column → `id`, `type`, `links`, `text`, `result`.

### Trace findings
| Item | Type | Code | Detail | Plain meaning |
|---|---|---|---|---|

Counts by code. Every item was checked; none was sampled out.

### Gaps
Clause text not sourced (with the free read-only route), records not in the files provided.

### Record
Findings, not a compliance verdict. Anything that enters the design and development file as a decision stops for the owner. Cleared by NAME, or uncleared. AI-assisted draft.
