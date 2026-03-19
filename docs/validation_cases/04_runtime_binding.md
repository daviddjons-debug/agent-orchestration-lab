# Runtime Binding — Case 04

## Bound runtime claim
Case 04 is bound to the current runnable lab only as a bounded false-locality verification scenario.

It is intended to test whether the current orchestration baseline can reject an apparently successful local outcome when adjacent correctness depends on a verify-only surface.

## What this binding is allowed to prove
- orchestrator-side false-locality framing at the contract level
- planner-side distinction between primary target, adjacent surface, and verify-only surface
- builder staying narrow without modifying the adjacent verify-only surface
- reviewer-side rejection of false-local success when adjacent verification is missing or stale

## What this binding is not allowed to claim
- repository-scale dependency discovery
- real tester-stage execution
- full runtime enforcement of all Surgical Edition extension fields
- full code-level blast-radius control

## Required falsification path
The case must include a runnable failure mode where the primary artifact passes but the adjacent verify-only condition is absent, stale, or unverified, and reviewer must not return a trustworthy pass.
