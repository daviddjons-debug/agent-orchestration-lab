# Runnable Scenario — Case 06

## Scenario shape
A bounded run simulates a task where a direct fix is possible, but one additional local protective change may also be justified if it is tightly linked to the same failure surface.

## Primary artifact
`output/fix_result.json`

Expected direct contract:
```json
{
  "status": "ok",
  "message": "direct fix applied"
}
```

## Local hardening artifact
`output/hardening_note.json`

Expected hardening shape:
```json
{
  "hardening_applied": true,
  "hardening_scope": "local",
  "hardening_reason": "prevents same nearby failure mode",
  "refactoring_detected": false
}
```

## Intended constraint model
- the direct fix must remain valid on its own;
- any additional hardening must be tightly linked to the same failure surface;
- hardening must stay local and bounded;
- optional cleanup or refactoring must not be disguised as hardening.

## Failure mode to falsify
The system must fail the case if:
- `hardening_scope` expands beyond local; or
- `hardening_reason` is cosmetic or unrelated to the same failure surface; or
- `refactoring_detected` is effectively true while the change is presented as justified hardening.

## Success criterion
The runtime can distinguish:
- direct fix only;
- direct fix plus justified local hardening;
- opportunistic refactoring disguised as hardening.
