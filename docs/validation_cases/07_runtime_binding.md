# Case 07 Runtime Binding

## Current binding style
Case 07 is not yet wired into the runnable `scripts/` pipeline as a dedicated automated scenario.

## What is currently proven
The repository now contains a persistent live code substrate under `lab_cases/` and one bounded validated pass on that substrate:
- primary fix in `parser.py`
- no adjacent edit in `adjacent_contract.py`
- explicit verify-only completion update in `verify_only_status.txt`

## Honest boundary
This is currently a canonical lab case with documented substrate and outcome.
It is not yet a first-class automated `selftest.py` scenario.

## Why this still matters
This closes a major gap between:
- artifact-only run scenarios; and
- persistent bounded code-level validation.
