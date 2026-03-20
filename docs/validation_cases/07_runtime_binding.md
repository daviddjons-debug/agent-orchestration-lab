# Case 07 Runtime Binding

## Current binding style
Case 07 is now wired into `scripts/selftest.py` as a dedicated automated scenario using the persistent substrate under `lab_cases/`.

## What is currently proven
The repository now contains a persistent live code substrate under `lab_cases/` and an automated bounded validation pass on that substrate:
- primary code behavior is validated in `parser.py`
- adjacent no-change discipline is preserved for `adjacent_contract.py`
- verify-only completion gating is enforced through `verify_only_status.txt`

## Honest boundary
This is now a first-class automated selftest scenario.
It is still not a generic `docs/runs/*` manifest-driven runtime case and still does not prove repository-scale code orchestration.

## Why this still matters
This closes a major gap between:
- artifact-only run scenarios; and
- persistent bounded code-level validation.
