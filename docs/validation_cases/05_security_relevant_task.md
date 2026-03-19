# Validation Case 05 — Security-relevant task with evidence-gated invocation

## Intent
This case tests whether the system invokes Security only when a real security trigger exists and whether Security produces concrete, surface-linked findings instead of ritual security theater.

## Why this case exists
Cases 01-04 proved bounded execution, adjacent verification, coordinated change, and false-locality rejection.
They do not yet prove that the system can:
- distinguish tasks that require security review from those that do not;
- keep security inspection constrained to the relevant surface;
- separate confirmed findings from unproven concerns and optional hardening.

## Target behavior
The system should:
1. invoke Security only when a concrete security trigger exists;
2. state that trigger explicitly;
3. constrain inspection to the declared change surface and immediate trust-boundary neighbors;
4. distinguish confirmed findings, unproven concerns, and optional hardening;
5. avoid reporting speculative noise as blocking security risk.

## Minimal runnable lab interpretation
A bounded artifact scenario where a task declares a specific security trigger and the validation checks whether the security path is justified, constrained, and evidence-linked.

## Pass condition
This case passes only if the runnable scenario can distinguish justified security invocation from ritual invocation and can separate concrete findings from optional hardening or unsupported suspicion.

## Not yet proven by this case
- repository-scale security review
- real exploitability analysis
- full operational Security runtime stage across arbitrary code tasks
