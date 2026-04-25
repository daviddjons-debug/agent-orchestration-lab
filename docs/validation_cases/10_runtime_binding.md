# Validation Case 10 — Runtime Binding

## Goal
Bind `final_validation_gate` semantics to a runnable lab fixture without creating a new runtime framework.

## Current runtime reality
The lab already proves bounded artifact and consistency checks in earlier cases.

Case 10 adds a dedicated final-validation fixture for high-risk artifact/source-mapping work:
- required source rows are declared in a compact source table;
- a flawed output attempts to claim final delivery while traceability is incomplete;
- a corrected output reaches `PASS_WITH_LIMITATIONS` only after required validation checks pass.

## Falsifiable checks
The checker must fail the flawed draft as `FAIL_NEEDS_REWORK` when:
- `validation_required` is true;
- required source mapping is missing;
- required fields are incomplete or inconsistent;
- summary/detail counts disagree;
- uncertainty is hidden or final delivery is claimed falsely.

The checker may pass the corrected draft as `PASS_WITH_LIMITATIONS` when:
- coverage is complete;
- source mapping is complete;
- required fields are present;
- summary/detail consistency holds;
- uncertainties are declared.

## Honest boundary
Case 10 is a dedicated runnable lab-case proof.

It does not prove:
- automatic enforcement in every future Codex host;
- repository-scale document extraction quality;
- a new Leo role or execution profile;
- blanket heavy validation for low-risk work.

It proves the final-validation gate concept is now represented as falsifiable lab evidence.
