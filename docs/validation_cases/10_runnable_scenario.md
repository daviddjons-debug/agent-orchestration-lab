# Validation Case 10 — Runnable Scenario

## Scenario
A compact source table defines two required source rows. Two candidate outputs are checked against that source table.

## Source artifact
- `source_table.json`

## Flawed output
- `draft_missing_traceability.json`

Expected computed validation result:
- `validation_status`: `FAIL_NEEDS_REWORK`
- `final_delivery_allowed`: `false`

Failure reasons include:
- required source mapping is blank for one row;
- declared validation checks are inconsistent with the actual row evidence;
- final delivery is claimed despite missing traceability.

## Corrected output
- `corrected_with_limitations.json`

Expected computed validation result:
- `validation_status`: `PASS_WITH_LIMITATIONS`
- `final_delivery_allowed`: `true`

Pass reasons include:
- source coverage is complete;
- source/file/row mapping is present for every output row;
- required fields exist;
- summary counts match detail rows;
- uncertainty is visible through confidence and limitation notes.

## Anti-cycle rule
The case is bounded to:
- one validation pass before final delivery;
- one correction pass plus one re-validation pass by default;
- further loops only with explicit user approval or explicit `PARTIAL_BLOCKED` / `FAIL_NEEDS_REWORK` declaration.

## Non-goal
This case must not be read as a requirement for full QA on every task.

Low-risk prose, simple rewrites, short explanations, basic translation, and non-material drafting remain light or skipped under Leo policy.
