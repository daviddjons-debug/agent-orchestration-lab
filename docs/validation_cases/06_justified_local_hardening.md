# Validation Case 06 — Task with justified local hardening

## Intent
This case tests whether the system can distinguish required local hardening from opportunistic refactoring and can justify why the hardening is necessary for the declared task rather than decorative scope growth.

## Why this case exists
Cases 01-05 proved bounded execution, adjacent verification, coordinated change, false-locality rejection, and security-gated review.
They do not yet prove that the system can distinguish:
- a direct fix with no hardening;
- a direct fix plus one necessary local protective change;
- optional cleanup or refactoring disguised as hardening.

## Target behavior
The system should:
1. identify the direct fix surface;
2. distinguish any claimed hardening from the direct fix itself;
3. justify why a local hardening step is required for the same failure surface;
4. reject wider cleanup or refactoring presented as safety work;
5. keep any justified hardening bounded and evidence-linked.

## Minimal runnable lab interpretation
A bounded artifact scenario where the primary task can be completed directly, but one additional local protective change may be justified if the validation can show that it prevents the same nearby failure mode.

## Pass condition
This case passes only if the runnable scenario can distinguish justified local hardening from decorative scope growth and can reject opportunistic refactoring disguised as safety or cleanup.

## Not yet proven by this case
- repository-scale code hardening policy
- full operational Tester runtime stage
- end-to-end hardening validation on live code changes
