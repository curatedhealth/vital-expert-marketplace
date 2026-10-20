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
| Template | `assets/route-answer.md` |
| Input | The person's question or request, and any draft they attached |
| Governance | TR-H3, TR-H9, `references/governance.md` |

## Steps

1. **Read what the person wants to happen**, not only the words. "Is this OK to send?"
   is a request for a check, not a definition.
2. **Classify the request.**
   - A question about the standard ("what does Unbiased cover"): explain from
     `references/standard.md` in plain words, with the "fails alone" example.
   - A piece of work to draft: route to `trusted-intake` first if the audience, market,
     product status or sources are unknown; otherwise to the Build skill that fits.
   - A finished draft to look over, including "is this OK to send": route to
     `trusted-check`. If the draft will leave the company, also name the internal process
     it goes through next (TR-H11), and say plainly that TRUSTED cannot say it is OK to
     send.
   - A claim or source to test: route to the Prove skill that fits.
   - A question about using the assistant itself ("can I paste this in", "should I say
     AI helped"): route to the Ethical skills and point to the company's AI use policy.
3. **Set the depth** from who will read the work (TR-H12). Say it in one line only if it
   is not obvious.
4. **Match on the reader's question, not on keywords.** "Is this balanced" with a draft
   that only lists benefits is Unbiased; "is this balanced" about a slide layout is not
   a TRUSTED question (TR-H9).
5. **Choose one skill and the reason**, internally. In the answer, describe the step in
   plain words; name the skill only if the person asks. Add a second step only when the
   request clearly spans two letters, and say which comes first.
6. **Check the active letters.** If the skill belongs to a letter the person turned off,
   say so and ask whether to turn it back on.
7. **Answer with `assets/route-answer.md`.**

## Checks before answering

- No verdict words (TR-H3).
- No style advice presented as TRUSTED (TR-H9).
- The skill named exists in the index.

## Boundaries

- Do not start the work of the routed skill here.
- Do not explain rules beyond what `references/standard.md` and
  `references/hard-rules.md` say.
