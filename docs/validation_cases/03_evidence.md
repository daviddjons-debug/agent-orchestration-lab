# Validation Case 03 — Evidence

## Evidence status
NOT YET PASSED.

## Required positive evidence
- a bounded run uses one primary source-like artifact plus two justified dependent artifacts:
  - `src/spec.json`
  - `src/generated_summary.txt`
  - `src/generated_manifest.json`
- planner carries forward the declared local cluster without widening beyond it
- builder creates or updates only declared artifacts inside the allowed change boundary
- reviewer returns PASS when:
  - each declared artifact satisfies its direct contract
  - both dependent artifacts remain semantically aligned with the primary spec
  - no undeclared cluster widening is detected

## Required negative evidence
- reviewer returns FAIL when one dependent artifact is stale relative to the primary spec
- reviewer returns FAIL when the two dependent artifacts disagree with each other
- reviewer returns FAIL when undeclared files appear outside the declared local cluster
- builder returns FAIL if declared writes exceed the allowed change boundary
- builder returns FAIL if declared read boundary exceeds the current baseline Builder contract

## What a future PASS would prove
- the current runtime can validate a bounded coordinated multi-file local cluster
- widening can be justified and still remain explicit and falsifiable
- reviewer can distinguish direct primary correctness from incomplete coordinated local updates
- Case 03 would extend the validation ladder beyond adjacent-pair consistency into bounded coordinated-cluster consistency

## What a future PASS would still not prove
- real repository-scale code dependency analysis
- automatic discovery of the correct cluster without scenario structure
- planner-side read-boundary enforcement
- general runtime read sandboxing
- tester-backed regression execution for real code changes

## Final judgment
Do not mark this case PASS until both positive and negative evidence are recorded from runnable runtime behavior.
