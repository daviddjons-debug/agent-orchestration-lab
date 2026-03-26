# Validation Case 07 — Evidence

## Baseline observed before fix
- `parse_setting("   ") -> ""`
- `render_setting("   ") -> "SETTING="`
- verify-only status: `adjacent verification pending`

## Bounded intervention
Changed:
- `lab_cases/case_07_live_bounded_code/src/parser.py`

Not changed:
- `lab_cases/case_07_live_bounded_code/src/adjacent_contract.py`

## Observed after fix
- `parse_setting("  alpha  ") -> "alpha"`
- `parse_setting("   ")` raises `ValueError`
- `render_setting("   ")` raises `ValueError`

## Completion evidence
Verify-only surface updated to:
- `adjacent verified`

## Conclusion
Case 07 provides the first persistent bounded live code-level validation pass in the repository.
It remains intentionally narrow and does not yet constitute full automated runtime binding.

## Explicit bridge from Case 04
Case 04 established the verify-only completion logic in a bounded artifact-level runtime scenario.
Case 07 carries that same invariant onto a persistent live code substrate:
- Case 04 = bounded false-locality verification with a verify-only adjacent surface in runtime artifacts
- Case 07 = bounded live code-level validation with a verify-only completion gate on persistent repository files
