# Runtime Binding — Case 06

## Bound runtime claim
Case 06 is bound to the current runnable lab only as a bounded local-hardening discrimination scenario executed through the existing 4-stage runtime.

It is intended to test whether the orchestration baseline can distinguish a direct fix, a justified local hardening step, and opportunistic refactoring disguised as safety work.

## What this binding is allowed to prove
- a direct fix can be represented separately from a local hardening artifact;
- the scenario can require evidence that hardening is tied to the same nearby failure surface;
- the case can reject decorative or widened cleanup presented as justified hardening;
- the current 4-stage runtime can validate bounded hardening semantics without claiming a dedicated Tester runtime stage.

## What this binding is not allowed to claim
- repository-scale hardening policy
- full operational Tester runtime stage across arbitrary code tasks
- end-to-end hardening validation on live code changes
- comprehensive regression analysis beyond the bounded scenario

## Required falsification path
The case must include a runnable failure mode where hardening is claimed but is either non-local, weakly justified, or effectively opportunistic refactoring, and the validation must not accept that as success.
