# Evidence — Case 04

## Scenario status
Not yet executed in runtime.

## Intended PASS condition
- reviewer rejects false-local success when the primary artifact passes but adjacent verify-only validation is missing, stale, or unverified;
- builder stays narrow and does not modify the adjacent verify-only surface;
- the run distinguishes true local success from false-local success.

## Intended falsification path
- primary artifact satisfies its direct contract;
- adjacent verify-only artifact is missing, stale, or not explicitly verified;
- reviewer must not issue a trustworthy pass.

## What must be captured after execution
- manifest/plan shape for Case 04;
- builder behavior on the primary surface;
- reviewer verdict for missing or stale adjacent verification;
- reviewer verdict after adjacent verification condition is satisfied;
- any gap between role-level semantics and current runtime mechanics.

## Current judgment
Pending runnable execution.
