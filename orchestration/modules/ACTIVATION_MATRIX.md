# Module Activation Matrix

## Purpose
This matrix defines which modules are:
- default-on
- trigger-based
- default-off

for each materialized execution profile inside `orchestration/`.

It is an operator-facing portable layer.
It does not replace the canonical logic in:
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`

## Profiles

### direct
Default-on:
- `triage`
- `planning`
- `execution`

Trigger-based:
- `review`

Default-off:
- `testing`
- `security`
- `browser_verification`
- `external_second_opinion`
- `release_packaging`

Interpretation:
- use the cheapest justified path;
- keep review conditional;
- keep non-essential modules off unless evidence forces activation.

### lite
Default-on:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based:
- `testing`
- `browser_verification`
- `external_second_opinion`

Default-off:
- `security`
- `release_packaging`

Interpretation:
- review becomes part of the normal bounded path;
- extra validation modules activate only when the task surface requires them.

### heavy
Default-on:
- `triage`
- `planning`
- `execution`
- `review`

Trigger-based:
- `testing`
- `security`
- `browser_verification`
- `external_second_opinion`
- `release_packaging`

Default-off:
- none by default beyond the trigger requirement itself

Interpretation:
- heavy does not mean “everything always on”;
- it means higher-discipline routing with broader activation eligibility;
- testing, security, browser, second-opinion, and packaging still require evidence, not ritual.

## Notes
- No module should activate merely because it exists.
- Escalation is evidence-driven, not narrative-driven.
- This matrix is the first portable/operator-facing bridge between profiles and modules.
