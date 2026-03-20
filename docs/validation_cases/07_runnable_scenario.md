# Case 07 Runnable Scenario

## Scenario
A narrow fix is applied in `parser.py` so that whitespace-only input is rejected.

## Expected local result
- `parse_setting("  alpha  ") -> "alpha"`
- `parse_setting("   ")` raises `ValueError`

## Adjacent expectation
- `adjacent_contract.py` remains unchanged
- adjacent behavior follows the parser change through dependency, not through direct adjacent editing

## Verify-only gate
Trustworthy completion is withheld until:
- `verify_only_status.txt` is updated from `adjacent verification pending` to `adjacent verified`

## Failure mode
A local parser fix must not be treated as trustworthy completion while verify-only status remains stale.
