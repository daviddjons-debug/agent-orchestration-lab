# Validation Case 10 — Risk-Based Final Validation Gate

## Purpose
Prove that high-risk artifact/source-mapping work cannot be treated as final when required traceability, required fields, or consistency checks are missing.

## What this case tests
This case tests whether the evidence layer can distinguish:
- a flawed generated artifact that claims final delivery despite missing source mapping;
- a corrected generated artifact that declares uncertainty and reaches `PASS_WITH_LIMITATIONS`;
- bounded validation behavior that leaves low-risk tasks light or skipped.

## Substrate
- `lab_cases/case_10_final_validation_gate/src/source_table.json`
- `lab_cases/case_10_final_validation_gate/src/draft_missing_traceability.json`
- `lab_cases/case_10_final_validation_gate/src/corrected_with_limitations.json`

## Classification
- `task_class`: high-risk artifact/source-mapping validation
- `validation_required`: `true`
- `validation_level`: `technical`

## Expected outcomes
- `draft_missing_traceability.json` must evaluate to `FAIL_NEEDS_REWORK`.
- `corrected_with_limitations.json` must evaluate to `PASS_WITH_LIMITATIONS`.

## Boundary
This is a bounded lab validation case.

It does not add a Leo role, profile, runtime wrapper, or host-wide enforcement mechanism.
It proves only that the declared final-validation semantics are falsifiable on a compact artifact/source-mapping fixture.
