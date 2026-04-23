# Execution Profiles Layer

## Purpose
This layer materializes the operator-facing execution profiles used by the routing layer.

It does not replace the canonical definitions in:
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`

It exists to provide a portable execution-profile surface inside `orchestration/`.

## Current profiles
The initial materialized profiles are:

- `direct`
- `lite`
- `heavy`

## Profile meaning
- `direct` = cheapest justified execution path for narrow, low-risk, localized work
- `lite` = bounded execution path when adjacent verification or modest drift control is needed
- `heavy` = explicit higher-discipline path when locality, consistency, regression, or security risk is materially higher

## Current role
This layer is the bridge between:
- routing output
- future module activation
- future skills attachment

## Not yet materialized here
- per-profile module matrix
- per-profile trigger matrix
- per-profile skill attachment rules
- automatic runtime enforcement
