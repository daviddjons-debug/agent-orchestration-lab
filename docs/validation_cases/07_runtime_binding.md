# Validation Case 07 — Runtime Binding

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

## Explicit bridge from Case 04
Case 04 proved that a supposedly successful local result must still FAIL when verify-only adjacent evidence is missing.
Case 07 extends that same logic onto a persistent live code substrate:
- Case 04 = artifact-level false-locality rejection with verify-only gating
- Case 07 = live code-level verify-only completion gating on persistent repository files

Case 07 therefore does not replace Case 04.
It upgrades the substrate from runtime artifacts to persistent code while preserving the same trust boundary.

## Why this still matters
This closes a major gap between:
- artifact-only run scenarios; and
- persistent bounded code-level validation.
