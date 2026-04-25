# Case 10 — Final Validation Gate substrate

Purpose: provide a compact runnable fixture for `final_validation_gate` behavior on high-risk artifact/source-mapping output.

Status: persistent substrate established; run with:

```bash
python3 lab_cases/case_10_final_validation_gate/check_case10.py
```

Expected result:
- `draft_missing_traceability.json` evaluates to `FAIL_NEEDS_REWORK`;
- `corrected_with_limitations.json` evaluates to `PASS_WITH_LIMITATIONS`.

Boundary: this is lab evidence only, not active Leo authority and not host-wide enforcement.
