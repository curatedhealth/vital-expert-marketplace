# Task TR-0.1.1 Explain the standard and route a request

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced cross-functional colleague |
| Workflow | Identify the need, match it to a letter, name one skill, say why |
| Skill | TR-0.1.1 |
| Knowledge | `references/standard.md` (letters, boundaries, skill index) |
| Tool | None. Companion slot: none needed |
| Prompt | This guide |
| Template | `templates/route-answer.md` |
| Input | The person's question or request, and any draft they attached |
| Governance | TR-H3, TR-H9, `governance.md` |

## Steps

1. **Safety first (TR-H14).** If any input mentions a possible side effect, pregnancy or breastfeeding exposure, overdose, misuse or off-label use reported for a person, medication error, lack of effect or product quality problem, route to
   `patient-safety` first, so its flag goes out before any question or draft.
2. **Read what the person wants to happen**, not only the words. "Is this OK to send?"
   is a request for a check, not a definition.
3. **Classify the request.**
   - A question about the standard ("what does Unbiased cover"): explain from
     `references/standard.md` in plain words, with the "fails alone" example, in two to
     four sentences, or one line when the person asks for one.
   - A question about what TRUSTED does for someone's work ("what does it do for me"):
     give all seven letters, one plain line each, then name the letters that usually
     matter most for the work they mention, from the table "Which letters matter most,
     by work type" in `references/standard.md`; say it is guidance, that all active
     letters still run and that depth follows the stakes (TR-H12), and say what each
     needs from the person (a label, the sources, the reader). Always end with one
     line that TRUSTED supports the company's review processes and never replaces
     them (TR-H11), also for internal work.
   - A piece of work to draft: route to `trusted-intake` first if the audience, market,
     product status or sources are unknown; otherwise to the Build skill that fits.
   - A finished draft to look over, including "is this OK to send": route to
     `trusted-check`. If the person pasted the work, run the check in the same reply,
     with no extra round trip. If the draft will leave the company, also name the
     internal process it goes through next (TR-H11), and say plainly that TRUSTED cannot
     say it is OK to send. That one sentence and the check meet the verdict stop rule in
     `governance.md`; do not add a routing answer as well.
   - A claim or source to test: route to the Prove skill that fits.
   - A question about using the assistant itself ("can I paste this in", "should I say
     AI helped"): route to the Ethical skills and point to the company's AI use policy.
4. **Set the depth** from who will read the work (TR-H12). Say it in one line only if it
   is not obvious.
5. **Match on the reader's question, not on keywords.** "Is this balanced" with a draft
   that only lists benefits is Unbiased; "is this balanced" about a slide layout is not
   a TRUSTED question (TR-H9).
6. **Choose one skill and the reason**, internally. In the answer, describe the step in
   plain words; name the skill only if the person asks. Add a second step only when the
   request clearly spans two letters, and say which comes first.
7. **Check the active letters.** If the skill belongs to a letter the person turned off,
   say so and ask whether to turn it back on.
8. **Answer with `templates/route-answer.md`.**

## Checks before answering

- No verdict words (TR-H3).
- No `[GAP:` marker: in a routing or explaining answer, gaps are plain sentences (TR-H13).
- When declining a verdict, name the person's own words for it ("safe for patients",
  "ready to print") and say who decides.
- No style advice presented as TRUSTED (TR-H9).
- The skill named exists in the index.

## Boundaries

- Do not start the work of the routed skill here, with one exception: when the person
  pasted the work and asks "is this OK to send" or similar, route and run `trusted-check`
  in the same reply.
- Do not explain rules beyond what `references/standard.md` and
  `references/hard-rules.md` say.
