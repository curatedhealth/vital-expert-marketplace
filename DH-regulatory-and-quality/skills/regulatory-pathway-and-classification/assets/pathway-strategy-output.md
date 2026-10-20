# Output format: pathway strategy (decision draft)

Short mode is 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line. A refusal or stop answer follows the same 450-word cap.

## Short mode (default for a direct question)

1. **Ranking by your scores:** one or two sentences naming the order and the close call.
2. **Ranking:** Option · Value estimate · Biggest contributing criterion.
3. **How robust:** the weight at which adjacent options swap; ties named.
4. **Sequence and gates:** numbered; each step names what it unlocks and its gate.
5. **Facts that could change a score:** at most three, each with its row.
6. **Decision for the owner:** one line, with the owner's name or "owner not named".
7. **Record:** "Decision draft. Scores and weights are yours. Uncleared." or the clearer's name.

## Full mode

### What this ranks

Options considered, options left out and why, and that weights and scores are the person's.

### Options and sourced facts

| Option | Route | Evidence bar | Review clock (labeled) | Fee | Capacity | Rows |
|---|---|---|---|---|---|---|

### Criteria, anchors and weights

| Criterion | 0 means | 2 means | 4 means | Weight |
|---|---|---|---|---|

### Scores

| Option | Criterion 1 | Criterion 2 | ... |
|---|---|---|---|

Each cell: the person's score; a `[GAP]` fact behind a cell is shown.

### Ranking

| Option | Value estimate | Contributions |
|---|---|---|

Method as the tool returns it, with its citations.

### How robust

Swap weight for each adjacent pair, other weights kept in proportion. Ties.

### Sequence and gates

| Step | Route or action | What it unlocks or waits for | Gate to proceed |
|---|---|---|---|

### Risks and open inputs

Gaps, proposals not yet law (GB reliance, Swiss FDA recognition, GB indefinite CE recognition), assumptions.

### Record

Decision draft. The pathway choice and any wording for FDA, a notified body, the MHRA or Swissmedic stop for the regulatory owner. AI-assisted. Cleared by NAME, or uncleared.
