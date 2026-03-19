# Runnable Scenario — Case 05

## Scenario shape
A bounded run simulates a task with a declared security trigger and a constrained security inspection surface.

## Primary surface
`output/security_input.json`

Expected task shape:
```json
{
  "surface": "file_upload_handler",
  "security_trigger": "unsafe file handling",
  "declared_risk": "uploaded filename reaches filesystem path construction"
}
```

## Security review artifact
`output/security_review.json`

Expected review shape:
```json
{
  "security_invocation_decision": "invoke",
  "security_trigger": "unsafe file handling",
  "inspected_surfaces": ["output/security_input.json"],
  "confirmed_findings": ["uploaded filename reaches filesystem path construction"],
  "unproven_concerns": [],
  "optional_hardening": [],
  "residual_risk": "path validation still required in real implementation",
  "blocking_security_reason": "filesystem path construction uses untrusted filename input"
}
```

## Intended constraint model
- Security is justified only when the declared trigger is concrete;
- findings must stay linked to the declared surface and immediate trust-boundary neighbors;
- optional hardening must not be treated as a blocker;
- unproven concerns must not be reported as confirmed findings.

## Failure mode to falsify
The system must fail the case if:
- Security is invoked without a concrete trigger; or
- `blocking_security_reason` is filled with optional hardening or unsupported speculation; or
- `confirmed_findings` are not linked to the declared input surface.

## Success criterion
The runtime can distinguish:
- justified security invocation with concrete findings;
- unjustified or ritual security invocation;
- confirmed findings vs unproven concerns vs optional hardening.
