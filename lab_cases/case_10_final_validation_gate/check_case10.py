import json
from pathlib import Path
import sys


BASE = Path("lab_cases/case_10_final_validation_gate/src")

REQUIRED_ROW_FIELDS = [
    "output_row_id",
    "source_file",
    "source_page",
    "source_item_id",
    "description",
    "quantity",
    "duty",
    "confidence",
    "limitation_note",
]

LOOP_APPROVAL_RULE = "explicit_user_approval_or_PARTIAL_BLOCKED_or_FAIL_NEEDS_REWORK"


def load_json(name: str) -> object:
    return json.loads((BASE / name).read_text(encoding="utf-8"))


def present(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    return True


def evaluate(source: dict, output: dict) -> tuple[str, bool, dict, list[str]]:
    errors: list[str] = []

    source_rows = source.get("source_rows")
    if not isinstance(source_rows, list) or not source_rows:
        errors.append("source_table.json must contain non-empty source_rows")
        source_rows = []

    rows = output.get("rows")
    if not isinstance(rows, list) or not rows:
        errors.append("output must contain non-empty rows")
        rows = []

    source_ids = {
        row.get("source_item_id")
        for row in source_rows
        if isinstance(row, dict) and present(row.get("source_item_id"))
    }
    output_ids = {
        row.get("source_item_id")
        for row in rows
        if isinstance(row, dict) and present(row.get("source_item_id"))
    }

    coverage_checked = bool(source_ids) and source_ids == output_ids

    source_mapping_checked = True
    required_fields_checked = True
    uncertainties_declared = True

    for idx, row in enumerate(rows, start=1):
        if not isinstance(row, dict):
            errors.append(f"row {idx} must be an object")
            source_mapping_checked = False
            required_fields_checked = False
            uncertainties_declared = False
            continue

        for field in REQUIRED_ROW_FIELDS:
            if field not in row:
                errors.append(f"row {idx} missing required field: {field}")
                required_fields_checked = False

        for field in ["output_row_id", "source_file", "source_page", "source_item_id", "description", "quantity", "duty", "confidence"]:
            if not present(row.get(field)):
                errors.append(f"row {idx} has blank required field: {field}")
                required_fields_checked = False
                if field in ["source_file", "source_page", "source_item_id"]:
                    source_mapping_checked = False

        confidence = row.get("confidence")
        limitation = row.get("limitation_note")
        if confidence != "confirmed" and not present(limitation):
            errors.append(f"row {idx} has uncertainty without limitation_note")
            uncertainties_declared = False

    summary = output.get("summary")
    consistency_checked = isinstance(summary, dict)
    if not consistency_checked:
        errors.append("summary must be an object")
        summary = {}
    else:
        limited_count = sum(1 for row in rows if isinstance(row, dict) and row.get("confidence") != "confirmed")
        confirmed_count = sum(1 for row in rows if isinstance(row, dict) and row.get("confidence") == "confirmed")
        expected = {
            "row_count": len(rows),
            "confirmed_count": confirmed_count,
            "limited_count": limited_count,
        }
        for key, expected_value in expected.items():
            if summary.get(key) != expected_value:
                errors.append(f"summary {key} expected {expected_value}, got {summary.get(key)!r}")
                consistency_checked = False

    computed_checks = {
        "coverage_checked": coverage_checked,
        "source_mapping_checked": source_mapping_checked,
        "required_fields_checked": required_fields_checked,
        "consistency_checked": consistency_checked,
        "uncertainties_declared": uncertainties_declared,
    }

    if output.get("validation_required") is not True:
        errors.append("validation_required must be true for this high-risk artifact case")
    if output.get("validation_level") not in {"artifact", "technical"}:
        errors.append("validation_level must be artifact or technical")

    for field, computed_value in computed_checks.items():
        if output.get(field) != computed_value:
            errors.append(f"{field} declared as {output.get(field)!r}, computed as {computed_value!r}")

    loop = output.get("validation_loop")
    if not isinstance(loop, dict):
        errors.append("validation_loop must be declared")
    else:
        if loop.get("validation_passes_before_final") != 1:
            errors.append("validation loop must allow one validation pass before final delivery")
        if loop.get("correction_passes_by_default", 0) > 1:
            errors.append("validation loop allows too many correction passes by default")
        if loop.get("revalidation_passes_by_default", 0) > 1:
            errors.append("validation loop allows too many re-validation passes by default")
        if loop.get("further_loops_require") != LOOP_APPROVAL_RULE:
            errors.append("validation loop must require approval or explicit blocked/partial status after default passes")

    if errors:
        return "FAIL_NEEDS_REWORK", False, computed_checks, errors

    if any(row.get("confidence") != "confirmed" for row in rows if isinstance(row, dict)):
        return "PASS_WITH_LIMITATIONS", True, computed_checks, []

    return "PASS", True, computed_checks, []


def check_fixture(source: dict, filename: str, expected_status: str) -> bool:
    output = load_json(filename)
    status, final_allowed, checks, errors = evaluate(source, output)
    declared_status = output.get("validation_status")
    declared_allowed = output.get("final_delivery_allowed")

    print(f"{filename}: computed_status={status}; computed_final_delivery_allowed={final_allowed}")
    print(f"{filename}: declared_status={declared_status}; declared_final_delivery_allowed={declared_allowed}")
    print(f"{filename}: checks={json.dumps(checks, sort_keys=True)}")

    if status != expected_status:
        print(f"CASE10 ERROR: expected computed {expected_status}, got {status}")
        return False

    if expected_status == "FAIL_NEEDS_REWORK":
        if final_allowed:
            print("CASE10 ERROR: failed validation must block final delivery")
            return False
        if not errors:
            print("CASE10 ERROR: failed validation must expose failure reasons")
            return False
        print(f"{filename}: failure_reasons={json.dumps(errors, sort_keys=True)}")
        return True

    if declared_status != expected_status:
        print(f"CASE10 ERROR: corrected output must declare {expected_status}, got {declared_status}")
        return False
    if declared_allowed is not True or final_allowed is not True:
        print("CASE10 ERROR: corrected output should allow final delivery")
        return False

    return True


def main() -> int:
    source = load_json("source_table.json")

    checks = [
        check_fixture(source, "draft_missing_traceability.json", "FAIL_NEEDS_REWORK"),
        check_fixture(source, "corrected_with_limitations.json", "PASS_WITH_LIMITATIONS"),
    ]

    if not all(checks):
        return 1

    print("CASE10 RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
