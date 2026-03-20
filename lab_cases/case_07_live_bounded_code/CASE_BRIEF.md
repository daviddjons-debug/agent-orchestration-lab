# Case 07 Brief

## Purpose
Provide the first persistent bounded live code-level validation surface outside `docs/runs/`.

## Current substrate
- `src/parser.py` — primary candidate locus
- `src/adjacent_contract.py` — adjacent dependency surface
- `src/verify_only_status.txt` — verify-only surface

## Observed baseline behavior
- `parse_setting("  alpha  ") -> "alpha"`
- `render_setting("  alpha  ") -> "SETTING=alpha"`
- verify-only status currently reads: `adjacent verification pending`

## Intended validation value
This case is meant to test whether the orchestration system can:
- localize the likely primary node;
- keep the change surface narrow;
- treat adjacent validation as required evidence rather than decorative narrative;
- avoid claiming trustworthy success if verify-only evidence remains stale.

## Status
Substrate established.
Runnable bounded case contract not yet defined.
