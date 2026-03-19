# Evidence — Case 06

## Scenario status
Executed in runtime.

## Executed run
- run directory: `docs/runs/orchestrated-2026-03-19_21-56-01`

## Observed success path
The runtime produced:
- `output/fix_result.json`
- `output/hardening_note.json`

Reviewer returned `PASS` when:
- the direct fix artifact satisfied its declared contract;
- `hardening_scope` was `local`;
- `hardening_reason` was `prevents same nearby failure mode`;
- `refactoring_detected` was `false`.

Observed reviewer evidence:
- `output/fix_result.json` exists
- `output/fix_result.json` satisfies declared contract
- `output/hardening_note.json` exists
- `output/hardening_note.json` satisfies declared contract
- `hardening scope is local` -> PASS
- `hardening reason is evidence-linked` -> PASS
- `refactoring is not disguised as hardening` -> PASS
- final verdict -> `PASS`

## Observed failure path
Reviewer returned `FAIL` after:
- `hardening_scope` was changed to `broad`
- `hardening_reason` was changed to `general cleanup improvement`
- `refactoring_detected` was changed to `true`

Observed reviewer evidence:
- `output/hardening_note.json` satisfies declared contract` -> FAIL
- `hardening scope is local` -> FAIL
- `hardening reason is evidence-linked` -> FAIL
- `refactoring is not disguised as hardening` -> FAIL
- final verdict -> `FAIL`

## What this now proves
- Case 06 has bounded runtime evidence through the existing 4-stage runner;
- the current reviewer can distinguish justified local hardening from opportunistic refactoring in this bounded scenario;
- the validation can reject widened or cosmetic hardening presented as necessary task-linked protection.

## What this still does not prove
- repository-scale hardening policy
- a dedicated operational Tester runtime stage
- end-to-end hardening validation on live code changes

## Current judgment
Validation Case 06 is passed as a bounded runtime justified-local-hardening scenario.
