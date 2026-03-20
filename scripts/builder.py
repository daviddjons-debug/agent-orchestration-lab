from pathlib import Path
import json
import sys

def fail(msg: str) -> int:
    print(f"ERROR: {msg}")
    return 1

def is_allowed_target(target_rel: str, allowed_change_set: list[str]) -> bool:
    normalized_target = target_rel.strip("/")
    for raw in allowed_change_set:
        zone = raw.strip()
        if not zone:
            continue
        normalized_zone = zone.strip("/")
        if zone.endswith("/"):
            if normalized_target == normalized_zone or normalized_target.startswith(normalized_zone + "/"):
                return True
        else:
            if normalized_target == normalized_zone:
                return True
    return False

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/builder.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    plan_json_file = base / "02_plan.json"
    if not plan_json_file.exists():
        return fail("missing 02_plan.json")

    try:
        plan = json.loads(plan_json_file.read_text(encoding="utf-8"))
    except Exception:
        return fail("02_plan.json is not valid JSON")

    if not isinstance(plan, dict):
        return fail("02_plan.json root must be an object")

    required_string_fields = [
        "task_class",
        "objective",
        "expected_end_state",
        "symptom",
        "root_cause_hypothesis",
        "problem_locus",
        "locus_confidence",
        "false_locality_risk",
        "path_decision",
        "patch_strategy",
        "change_rationale",
    ]
    for field in required_string_fields:
        value = plan.get(field)
        if not isinstance(value, str) or not value.strip():
            return fail(f"02_plan.json missing non-empty string field: {field}")

    required_list_fields = [
        "dependency_ring",
        "allowed_read_set",
        "allowed_change_set",
        "verify_only_surfaces",
        "excluded_neighbors",
        "forbidden_zone",
        "acceptance_criteria",
        "verification_targets",
        "evidence_required",
        "blockers_or_uncertainties",
        "escalation_trigger",
    ]
    for field in required_list_fields:
        value = plan.get(field)
        if not isinstance(value, list):
            return fail(f"02_plan.json missing list field: {field}")

    allowed_read_set = plan["allowed_read_set"]
    allowed_change_set = plan["allowed_change_set"]
    verify_only_surfaces = plan["verify_only_surfaces"]

    normalized_read_set = [item.strip() for item in allowed_read_set]
    if "02_plan.json" not in normalized_read_set:
        return fail("allowed_read_set must include 02_plan.json for baseline builder contract")
    if any(item != "02_plan.json" for item in normalized_read_set):
        return fail("allowed_read_set exceeds baseline builder read contract")

    artifacts = plan.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        return fail("02_plan.json missing non-empty list field: artifacts")

    created = []
    for artifact_spec in artifacts:
        if not isinstance(artifact_spec, dict):
            return fail("02_plan.json artifacts must contain only objects")

        artifact_rel = artifact_spec.get("path")
        artifact_type = artifact_spec.get("type")

        if not isinstance(artifact_rel, str) or not artifact_rel.strip():
            return fail("artifact spec missing non-empty string field: path")
        if artifact_type not in {"json", "text"}:
            return fail(f"artifact spec has unsupported type: {artifact_type}")
        if artifact_rel in verify_only_surfaces:
            return fail(f"artifact path declared as verify-only surface: {artifact_rel}")
        if not is_allowed_target(artifact_rel, allowed_change_set):
            return fail(f"artifact path outside allowed_change_set: {artifact_rel}")

        artifact = base / artifact_rel
        artifact.parent.mkdir(parents=True, exist_ok=True)

        if artifact_type == "json":
            required_fields = artifact_spec.get("required_fields")
            if not isinstance(required_fields, dict):
                return fail(f"json artifact missing object field: required_fields ({artifact_rel})")
            artifact.write_text(json.dumps(required_fields, indent=2) + "\n", encoding="utf-8")
            created.append(f"- created {artifact_rel} [json]")
        else:
            exact_content = artifact_spec.get("exact_content")
            if not isinstance(exact_content, str):
                return fail(f"text artifact missing string field: exact_content ({artifact_rel})")
            artifact.write_text(exact_content, encoding="utf-8")
            created.append(f"- created {artifact_rel} [text]")

    builder_report_rel = "03_builder.md"
    if not is_allowed_target(builder_report_rel, allowed_change_set):
        return fail("artifact path outside allowed_change_set: 03_builder.md")

    builder_report = (
        "# Builder Output\n\n"
        "Source: 02_plan.json only\n\n"
        f"Task class: {plan['task_class']}\n"
        f"Objective: {plan['objective']}\n"
        f"Problem locus: {plan['problem_locus']}\n"
        f"Patch strategy: {plan['patch_strategy']}\n\n"
        "Executed change set:\n"
        + "\n".join(created)
        + "\n\nUntouched but adjacent surfaces:\n"
        + (("\n".join(f"- {x}" for x in verify_only_surfaces)) if verify_only_surfaces else "- none")
        + "\n\nContract deviation detected: no\n"
        "Direct build blocker: none\n"
        "Execution summary: declared artifacts created within allowed_change_set.\n"
    )
    (base / builder_report_rel).write_text(builder_report, encoding="utf-8")
    print(builder_report)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
