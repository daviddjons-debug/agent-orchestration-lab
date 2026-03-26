# Case 07 Execution Target

## First bounded task
Apply a narrow fix in `src/parser.py` so that whitespace-only input is not accepted silently.

## Desired behavior
- `parse_setting("  alpha  ") -> "alpha"`
- `parse_setting("   ")` must raise `ValueError`

## Boundary expectations
### Allowed change candidate
- `src/parser.py`

### Adjacent read-only surface
- `src/adjacent_contract.py`

### Verify-only completion surface
- `src/verify_only_status.txt`

## Explicit no-change expectation
The initial bounded pass must not modify:
- `src/adjacent_contract.py`

## Why this task is useful
This creates a real local code fix candidate while preserving adjacent verification pressure.

A local parser fix may be correct, but trustworthy completion still requires explicit verify-only evidence.

## Status
Execution target is now exercised by automated `scripts/selftest.py` coverage on a persistent live substrate.
