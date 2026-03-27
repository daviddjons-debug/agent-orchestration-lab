# Validation Case 09 — Source-of-Truth / Stale-Defect / Adjacent-Consistency Triad

## Purpose
Prove that the orchestration system can distinguish:
1. the canonical source of truth,
2. the stale defect node derived from it,
3. the adjacent consistency node that must remain aligned but is not identical to the stale defect.

## Expected profile
Heavy

## Runnable lab interpretation
A bounded declared cluster where:
- one node is canonical,
- one node is stale against the canonical node,
- one adjacent node must be verified for consistency,
- reviewer must fail if these roles are collapsed, swapped, or left semantically unproven.

## Required checks
- `source_of_truth_node` is explicitly declared and non-empty.
- `stale_defect_node` is explicitly declared and non-empty.
- `adjacent_consistency_node` is explicitly declared and non-empty.
- `source_of_truth_node` != `stale_defect_node`.
- reviewer must fail if manifest/plan swap source and stale roles.
- reviewer must fail if adjacent consistency is left stale while primary stale defect is fixed.
- reviewer must fail if triad fields exist only as schema with no consistency consequence.
- reviewer may pass only when:
  - canonical source remains authoritative,
  - stale node is brought back into alignment,
  - adjacent consistency node is verified or repaired as declared.

## Minimal runnable substrate candidate
Suggested bounded substrate:
- `src/source.json`
- `src/stale_view.json`
- `src/adjacent_index.txt`

Canonical relation:
- `src/source.json.message` is the authority.
- `src/stale_view.json.message` must match the source.
- `src/adjacent_index.txt` must also match the same canonical message.

## Expected falsification paths
1. Source/stale swap -> FAIL
2. Stale repaired but adjacent left stale -> FAIL
3. Adjacent repaired but stale still stale -> FAIL
4. All three aligned -> PASS

## Success condition
Case 09 becomes real only when:
- a runnable lab substrate exists,
- selftest drives both FAIL and PASS states,
- reviewer verdict changes because of triad semantics rather than field presence alone.
