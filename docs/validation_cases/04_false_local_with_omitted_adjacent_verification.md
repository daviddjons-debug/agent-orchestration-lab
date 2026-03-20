# Validation Case 04 — False-local change with omitted adjacent verification

## Intent
This case tests whether the system can reject an apparently local success when correctness depends on an adjacent surface that is verify-only or explicitly excluded from modification.

## Why this case exists
Cases 01-03 proved bounded contract execution, adjacent consistency checks, and bounded coordinated change.
They do not yet prove that the system can distinguish:
- a truly local success;
- a false-local success where the primary artifact passes but adjacent correctness remains unverified.

This case is the first direct validation target for the new Surgical Edition semantics:
- `false_locality_risk`
- `verify_only_surfaces`
- sufficiency-focused reviewer behavior

## Target behavior
The system should:
1. classify the task as having false-locality risk;
2. keep the implementation surface narrow;
3. avoid modifying verify-only adjacent surfaces;
4. require explicit adjacent verification before a trustworthy pass;
5. fail or withhold a trustworthy pass when adjacent verification is omitted.

## Minimal runnable lab interpretation
A bounded artifact scenario where:
- one primary artifact satisfies its direct contract;
- one adjacent artifact is not supposed to be modified in the chosen run;
- overall correctness depends on verifying that adjacent artifact;
- reviewer must detect when the primary result looks correct but adjacent verification is missing or stale.

## Pass condition
This case passes only if the runnable scenario can falsify false-local success rather than accepting the primary artifact at face value.

## Not yet proven by this case
- repository-scale code dependency discovery
- real tester-stage execution
- full runtime enforcement of all Surgical Edition fields
