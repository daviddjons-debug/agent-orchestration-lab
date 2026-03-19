# Runnable Scenario — Case 05

## Scenario shape
A bounded run simulates a task with a declared security trigger and a constrained security inspection surface.

## Primary surface
`output/security_input.json`

Expected task shape:
- file exists;
- file describes a surface with a concrete security trigger;
- file content allows distinguishing real security linkage from speculative concerns.

## Security review artifact
`output/security_review.json`

Expected review shape:
- file exists;
- file contains:
  - `security_invocation_decision`
  - `security_trigger`
  - `inspected_surfaces`
  - `confirmed_findings`
  - `unproven_concerns`
  - `optional_hardening`
  - `residual_risk`
  - `blocking_security_reason`

## Intended constraint model
- Security is justified only when the declared trigger is concrete;
- findings must stay linked to the declared surface and immediate trust-boundary neighbors;
- optional hardening must not be treated as a blocker;
- unproven concerns must not be reported as confirmed findings.

## Failure mode to falsify
The system must fail the case if:
- Security is invoked without a concrete trigger;
- reported findings are speculative and not linked to the declared surface;
- optional hardening is escalated as a blocking security reason.

## Success criterion
The runtime can distinguish:
- justified security invocation with concrete findings;
- unjustified or ritual security invocation;
- confirmed findings vs unproven concerns vs optional hardening.
