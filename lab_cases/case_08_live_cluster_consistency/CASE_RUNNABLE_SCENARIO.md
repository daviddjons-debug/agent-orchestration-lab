# Case 08 Runnable Scenario

## Scenario type
Bounded live coordinated-cluster consistency validation.

## Scenario boundary
### Primary target
- `src/spec.json`

### Justified secondary nodes
- `src/generated_summary.txt`
- `src/generated_manifest.json`

## Expected orchestration behavior
The system should:
1. localize `src/spec.json` as the primary locus;
2. justify the two dependent surfaces as a bounded local cluster;
3. require coordinated consistency across all three surfaces;
4. fail if one dependent surface is stale;
5. refuse undeclared widening beyond this cluster.

## Status
Runnable scenario is now exercised as a dedicated automated `scripts/selftest.py` scenario on a persistent live substrate.
