# Gap rules

A gap is information. Name its kind, because each kind has a different next step.

| Kind | When | How to word it | Next step |
|---|---|---|---|
| Record not provided | A trace link, verification result, risk file entry, complaint field or reporting decision is not in the files the person gave | "Not in the files provided `[GAP]`." Never "missing" or "does not exist". | Ask for it, or list it as an open item. |
| Not mapped | An observed event has no hazard id in the person's mapping | "Not mapped to a hazard in the file: candidate for 'not foreseen'; your decision." | The person maps it or adds a hazard. |
| Store gap | The library returns no events for a query, or the jurisdiction is not loaded (EU vigilance, Swiss field safety actions) | "The library holds no events for this query (scope: ...)." | Check FDA, MHRA, EUDAMED or Swissmedic directly. Never "no recalls". |
| Field missing on a row | A recall row has no recall number or record link; an MHRA row has no manufacturer | "The library row does not state ... `[GAP]`." | Confirm on the regulator's database. |
| Standard text not sourced | The check would need ISO 13485 or ISO 14971 clause text that no row restates | "The clause text is not in the sourced reference `[GAP]`." | Free read-only route (ST13) or the person's licensed copy. |
| No rule or scale | The person has set no acceptability criterion, severity scale or grading scheme | "No criterion given: laid out, not compared." | The person sets it; the model does not. |

## Never

- Never turn a store gap into "no adverse events" or "the controls work".
- Never count comparable products' events as occurrences of the person's product.
- Never compute an incidence rate from MAUDE report counts (no denominator; reports are not confirmed events).
