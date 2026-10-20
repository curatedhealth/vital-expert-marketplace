# Gap rules

A gap is information. Each kind leads to a different next step, so name the kind.

| Kind | When | How to word it | Next step |
|---|---|---|---|
| Standard text not sourced | The answer needs ISO 13485, ISO 14971 or IEC 62304 clause text that no regulator or public page restates in `quality-systems-sources.md` | "The clause text is not in the sourced reference `[GAP]`; read it on the ANSI IBR portal or the ISO Online Browsing Platform (ST13), or in the person's licensed copy." | The person reads the clause; the model does not paraphrase it from memory. |
| Person's record missing | A trace link, a verification result, a control, an acceptability criterion or a reviewer is not in the files the person gave | "Not in the files provided `[GAP]`." Never "does not exist". | Ask for the record, or list it as an open item. |
| Store gap | The library returns no safety events or devices for a query | "The library holds no events for this query (scope: US software-related recalls and MAUDE counts; EU vigilance and Swiss field safety actions not loaded)." | Check FDA, MHRA, EUDAMED or Swissmedic directly before saying anything about the event history. |
| Field missing on a returned row | A recall row has no recall number, a usable link or a manufacturer | "The library row does not state the recall number `[GAP]`." | Confirm on the regulator's database. |
| Source superseded or under revision | ISO/TR 24971 is "to be revised"; IEC 62304 edition 2.0 is in preparation; MDSAP copies on fda.gov may be superseded | State the status and date from the row (ST3, ST8, QS39). | Re-check before external use. |

## Never

- Never turn "not in the files" into "missing from the design file". The person may hold it elsewhere.
- Never turn an empty safety-event search into "no recalls" or "no adverse events".
- Never supply an acceptability criterion, a severity scale or a probability scale to fill a gap. Those are the person's (ST4).
