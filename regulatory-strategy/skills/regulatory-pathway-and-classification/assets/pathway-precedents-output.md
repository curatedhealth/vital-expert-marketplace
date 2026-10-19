# Output format: pathway precedents

Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line. A refusal or stop answer follows the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** one or two sentences: whether the records show a US predicate candidate, which route comparables took, where they are authorized.
2. **Comparables:** Device · Applicant · Jurisdiction · Route · Decision date · Code · Source (retrieved DATE).
3. **Predicate candidates (US):** Candidate · Code and regulation per record · Predicate it named · What the owner still has to compare (intended use, technology) · Summary URL.
4. **Timing context:** calendar days between stored dates with n; published FDA average total days for the route; one line that FDA days are a different measure.
5. **Gaps:** one line (UK and CH not loaded; EU decision dates not stored).
6. **Record:** "Precedent read, as of DATE. Uncleared." or the clearer's name.

## Full mode

### What the library can see

Per jurisdiction: loaded or not, count, last load date.

### Comparables

| Device | Applicant | Jurisdiction | Route | Class per record | Code | Submission date | Decision date | Calendar days | Source, retrieved |
|---|---|---|---|---|---|---|---|---|---|

### Predicate chains

Each chain as the FDA summaries state it, node by node, with codes and dates. Crossing of product codes noted.

### Code-level precedents

| Code | Decisions | By route | By year | Calendar days (n, min, max) | De Novo grants |
|---|---|---|---|---|---|

### Where comparables are authorized

| Device | US | EU | UK | CH | Source |
|---|---|---|---|---|---|

### Timing context

Stored calendar days beside the published averages and MDUFA goals, each labeled for what it measures.

### Gaps

Classified per `references/gap-rules.md`.

### Record

Precedents are described by their records only. Substantial equivalence is FDA's determination; the predicate choice stops for the regulatory owner. AI-assisted. Cleared by NAME, or uncleared.
