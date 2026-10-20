# Tool calls

## Companion slot

These tools are available only when VERIFY is connected with a key. Without them, run the task by hand and label results not tool-checked (VR-H4).

## check_claim

Arguments: claim text, source id, quoted passage.

Returns: one status and the deciding passage. It does not search. It does not return the faithfulness percent. The writer computes that from the counts.

Pitfall: an empty passage returns unverifiable. Do not paste a summary you wrote into the passage field.

## verify_text

Arguments: the submitted text and the sources the person already gave.

Returns: at most 60 findings. A longer text must be split. It does not fetch sources the person did not give.

Schema source: Verify connector, 19 October 2026.
