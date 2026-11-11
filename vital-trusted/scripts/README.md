# Release checks

`ci_checks.py` checks the plugin folder before it is handed off. It uses only the Python
standard library, reads the plugin and writes nothing.

## Run

From the plugin folder:

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/ci_checks.py            # static checks
PYTHONDONTWRITEBYTECODE=1 python3 scripts/ci_checks.py --tests    # static checks, then every test file
PYTHONDONTWRITEBYTECODE=1 python3 scripts/ci_checks.py --only pointers,em-dash
python3 scripts/ci_checks.py --list                                # check names
```

Exit code 0 means every check passed. Exit code 1 means at least one failed, with the
files and line numbers printed under the check name. Set `PYTHONDONTWRITEBYTECODE=1` so
no `__pycache__` folder is left in the plugin.

## What each check does

| Check | Passes when |
|---|---|
| `file-count` | The plugin holds 512 files or fewer. |
| `descriptions` | Every skill, agent and plugin description is 1024 characters or fewer. |
| `versions` | Every skill's `metadata.version` and `plugin.json` say 0.3.4, `release_state` is Pilot, and each skill's `name` matches its folder. |
| `depends-on` | No `depends_on` names a skill that is not shipped. |
| `pointers` | Every path named in a shipped `.md` file exists, resolved from the file's folder, then its skill folder (or the plugin root for plugin-level files). Names of files the person supplies (`.txt`, `.json`) and URLs are skipped. No file is exempt. |
| `files-tables` | Each `SKILL.md` "Files in this skill" table lists exactly the files that skill ships. |
| `repo-paths` | No shipped file names a repository-internal folder. |
| `verify-words` | No shipped text names a tool, key prefix or result word from the retired companion outside a "do not use" rule. `CHANGELOG.md` is exempt by name because it records what was retired. The two check scripts name the banned words in order to find them and are exempt by name. |
| `em-dash` | No em dash appears in any `templates/` or `examples/` file, gap markers included. The gap marker separator is a semicolon: `[GAP: <class>; <what is missing>; <what would close it>]`. |
| `duplicates` | No two shipped files are byte-identical. |
| `frontmatter` | Every `SKILL.md` frontmatter uses only the allowed keys, its name matches the folder and the naming rule, and its description cues its use in the third person. |
| `body-size` | Every `SKILL.md` body is under 500 lines; a reference file over 100 lines opens with a contents list. |
| `safety-first` | Every skill's method file (in its `references` folder) opens with the TR-H14 safety step, and the hard rule is present. |
| `eval-rules` | Every `evals.json` parses with 3 or more cases and unique ids; no eval or known-answer case requires a gap marker outside a drafted deliverable. |
| `contradictions` | No shipped file uses a phrasing known to contradict a rule. |
| `voice` | No superlatives; no exclamation marks in templates or examples. |
| `tests` (only with `--tests`) | Every `test_*.py` in the plugin exits 0, run from its own folder. |

## Test the checks

```
PYTHONDONTWRITEBYTECODE=1 python3 scripts/test_ci_checks.py
```

The tests build small temporary plugin trees and confirm each check passes a clean tree
and fails the defect it exists to catch. `--tests` runs this file too.
