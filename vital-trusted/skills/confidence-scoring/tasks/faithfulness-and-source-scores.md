# Task TR-8.3.1 Faithfulness calculation and source scores

New in TRUSTED. Restates the confidence line from the VERIFY connector instruction.

## Formula

| Slot | For this task |
|---|---|
| Worker | Evidence lead |
| Workflow | Collect the statuses VERIFY returned, confirm where they came from, count, compute, print the score lines and the confidence line, say what they mean |
| Skill | TR-8.3.1 |
| Knowledge | `references/rules.md` (C1–C7), `references/patterns.md` (P1–P10) |
| Tool | `scripts/faithfulness.py` where code can run. Companion slot: reads results of VERIFY `check_claim` / `verify_text` (via `claim-assessment`) and `qualify_source` / `check_currency` (via `source-assessment`); calls none |
| Prompt | This guide |
| Template | `assets/confidence-line.md`, `assets/check-line.md` |
| Input | The findings from `claim-assessment` (one status per statement), the qualified sources from `source-assessment`, the reference list from `citation-and-record`, who will read the work |
| Governance | TR-H1, TR-H3, TR-H4, TR-H5, TR-H13 |

## Steps

1. **Confirm the statuses came from VERIFY.** Each status must have been returned in
   this conversation by `check_claim` or `verify_text`. If any were decided by reading
   (a "manual" decision, a Build skill's "not found in the material", the person's own
   tally), keep them apart. Do not mix them into the count (`references/patterns.md` P2).
2. **If no status came from VERIFY**, give no confidence figure. Say so in one line,
   offer the counts from reading labeled "not tool-checked", and say what VERIFY would
   add (`references/tools.md`). Stop here for the percent.
3. **Count each status once per statement:** supported, partial, unsupported,
   contradicted, unverifiable, out_of_scope. One statement, one status. If a statement
   was checked against two passages, use the status `claim-assessment` settled on; if it
   settled on none, ask.
4. **Compute.** Run
   `python scripts/faithfulness.py --source verify --supported <n> --partial <n> --unsupported <n> --contradicted <n> --unverifiable <n> --out-of-scope <n>`,
   or pass the findings as JSON with `--json-file`. Where code cannot run, do the
   arithmetic by hand and show it:
   (supported + 0.5 × partial) ÷ (supported + partial + unsupported + contradicted +
   unverifiable) × 100, rounded to a whole percent, half up.
5. **Zero denominator.** If every statement was out of scope, or none was checked, there
   is no figure. Write "No confidence figure: nothing factual was checked." Never write
   0% or 100% for an empty count.
6. **Print the source score lines.** Under each reference line (built by
   `citation-and-record`), print the `source_score` total and each axis whose value is a
   number. Leave out any axis that came back empty; do not write it as zero. Say in one
   plain line what the score is about: the page (who published it, how recent, how close
   to the question, how complete its details, whether it was checked for retraction),
   not the statement.
7. **Print the confidence line** immediately under the reference list, in the format of
   `assets/confidence-line.md`, with the arithmetic.
8. **Say what it means, in plain words**, once per answer:
   - It means: of the factual statements checked, this share is backed by the passages
     supplied, with partly backed statements counting half.
   - It does not mean: that the statements are true in the world, that the sources are
     good, that the evidence is balanced, or that the work is allowed or ready to send.
   - The check compares words in the statement with words in the passage. A weaker or
     reworded sentence can still come back backed, so the open items and a human read
     still matter (`references/rules.md` C5).
9. **Hand on** to the card (`tasks/verify-card.md`).

## Questions people ask

- **"Is 85% good enough to send?"** There is no threshold. Answer with what 85% counts,
  name the open items behind the missing 15%, and point to the review the material goes
  through next (for a payer: your market access or promotional review process). The
  decision belongs to the named reviewer (TR-H5).
- **"Can you round it up / leave out the unverifiable ones?"** No. Unverifiable stays in
  the denominator; only out of scope is left out. Offer instead to fix or remove the
  statements and check again.
- **"Why did it go down after we added sources?"** More statements were checked, or a
  new passage contradicted one. Show the two counts side by side.
- **"Average it with the source scores."** Decline. They measure different things.

## Check line

See `assets/check-line.md`.

## Boundaries

- Do not decide or change a status here; that is `claim-assessment`.
- Do not compute or re-weight a source score; print what VERIFY returned
  (`source-assessment` owns the grade).
- Do not compare a percent across two drafts as "better" or "worse" without saying the
  statements checked differ.
