# Without connector — mlr-board-prep

1. Require a real human name in cleared_by.
2. Run `mlr_build_prep_record_offline.py`; reject AI names.
3. Stamp `prep_complete` only as board-prep readiness, never use-approval, and only under the three conditions in `SKILL.md` § When `prep_complete` may be stated. Report `prep_cleared_for_human_mlr` as the record state on its own line, never as the status.
