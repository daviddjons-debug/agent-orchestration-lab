# Runtime Binding — Case 05

## Bound runtime claim
Case 05 is bound to the current runnable lab only as a bounded security-invocation and evidence-linkage scenario.

It is intended to test whether the orchestration baseline can distinguish justified security review from ritual security theater and whether the security output stays constrained to the declared task surface.

## What this binding is allowed to prove
- security invocation can be modeled as evidence-gated rather than automatic;
- a concrete security trigger can be propagated as part of the case contract;
- the scenario can distinguish confirmed findings, unproven concerns, and optional hardening;
- the case can reject unsupported blocking security claims.

## What this binding is not allowed to claim
- repository-scale security review
- real exploitability analysis
- full operational Security runtime stage across arbitrary code tasks
- end-to-end security validation on live code changes
- comprehensive trust-boundary analysis beyond the bounded scenario.

## Required falsification path
The case must include a runnable failure mode where Security is invoked without a concrete trigger, or where the review artifact escalates speculative or optional items as confirmed blocking findings, and the validation must not accept that as success.
