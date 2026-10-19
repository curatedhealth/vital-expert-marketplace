# Honesty examples

## Drop the figure, keep the comparison

Draft: "Response was 62 percent higher at week 12, and leading analysts expect broad uptake."
Passage: "Response was higher at week 12 than at week 4."
Finding: `partial`.

Answer: "Response was higher at week 12 than at week 4." The 62 percent and the analysts are gone.

## Drop the whole sentence

Draft: "The program was likely founded in the 1990s and is SOC 2 certified."
Passage: the source describes the current submission workflow and says nothing about founding or certification.
Finding: `unverifiable`.

Answer: the sentence is omitted. The card counts one unverifiable item. No replacement sentence is written.

## Citation stays the tool's line

After the prose, call `build_citation` once per source that survived. Paste `formatted` with no caption. A sentence that was dropped does not get a citation invented to match it.
