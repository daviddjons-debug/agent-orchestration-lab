# Validation Case 09 — Runnable Scenario

## Scenario
A bounded local triad is defined under `lab_cases/case_09_source_truth_stale_consistency/src`.

## Source of truth
- `source.json`

## Stale defect node
- `stale_view.json`

## Adjacent consistency node
- `adjacent_index.txt`

## Expected local rule
The canonical message in `source.json` must remain authoritative.

That same message must also appear in:
- `stale_view.json`
- `adjacent_index.txt`

## Pass/Fail invariant
PASS iff:
- `source.json` carries a non-empty canonical message;
- `stale_view.json` matches that message;
- `adjacent_index.txt` matches that same message.

FAIL if:
- the stale defect node diverges from the source of truth;
- the adjacent consistency node diverges from the source of truth;
- the stale defect node is repaired but the adjacent consistency node remains stale.

## Expected orchestration behavior
The system should:
1. localize `source.json` as the canonical authority;
2. distinguish `stale_view.json` from the canonical source rather than collapsing the two roles;
3. require `adjacent_index.txt` to remain aligned as a separate consistency surface;
4. fail when either non-canonical node is stale;
5. restore PASS only when the full triad is aligned.

## Failure mode
The case must not be treated as complete when:
- `source.json` is valid,
- `stale_view.json` is restored,
- but `adjacent_index.txt` still carries stale content.

## Boundary
This case remains bounded to the declared triad and does not yet prove generic repository-scale source-of-truth inference or runtime-derived dependency discovery.

The triad is explicitly declared in advance.
It is not automatically discovered by the runtime.
