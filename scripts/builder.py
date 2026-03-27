from pathlib import Path
import json
import sys

from runtime_contract import PLAN_REQUIRED_LIST_FIELDS, PLAN_REQUIRED_STRING_FIELDS, expected_builder_read_set

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

def validate_structured_ring(plan: dict) -> str | None:
    structured = plan.get("dependency_ring_structured")
    if not isinstance(structured, dict):
        return "02_plan.json missing object field: dependency_ring_structured"

    primary_target = structured.get("primary_target")
    adjacent_read_nodes = structured.get("adjacent_read_nodes")
    adjacent_verify_only_nodes = structured.get("adjacent_verify_only_nodes")
    excluded_neighbors = structured.get("excluded_neighbors")

    if not isinstance(primary_target, str) or not primary_target.strip():
        return "dependency_ring_structured missing non-empty string field: primary_target"
    if not isinstance(adjacent_read_nodes, list):
        return "dependency_ring_structured missing list field: adjacent_read_nodes"
    if not isinstance(adjacent_verify_only_nodes, list):
        return "dependency_ring_structured missing list field: adjacent_verify_only_nodes"
    if not isinstance(excluded_neighbors, list):
        return "dependency_ring_structured missing list field: excluded_neighbors"

    dependency_ring = plan.get("dependency_ring", [])
    if primary_target not in dependency_ring:
        return "dependency_ring_structured.primary_target must be present in dependency_ring"

    for node in adjacent_read_nodes + adjacent_verify_only_nodes:
        if not isinstance(node, str) or not node.strip():
            return "dependency_ring_structured contains non-string adjacent node"
        if node not in dependency_ring:
            return f"dependency_ring_structured node missing from dependency_ring: {node}"

    if plan.get("verify_only_surfaces", []) != adjacent_verify_only_nodes:
        return "verify_only_surfaces must match dependency_ring_structured.adjacent_verify_only_nodes"
    if plan.get("excluded_neighbors", []) != excluded_neighbors:
        return "excluded_neighbors must match dependency_ring_structured.excluded_neighbors"

    return None

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

    for field in PLAN_REQUIRED_STRING_FIELDS:
        value = plan.get(field)
        if not isinstance(value, str) or not value.strip():
            return fail(f"02_plan.json missing non-empty string field: {field}")

    for field in PLAN_REQUIRED_LIST_FIELDS:
        value = plan.get(field)
        if not isinstance(value, list):
            return fail(f"02_plan.json missing list field: {field}")

    structured_ring_error = validate_structured_ring(plan)
    if structured_ring_error:
        return fail(structured_ring_error)

    allowed_read_set = plan["allowed_read_set"]
    allowed_change_set = plan["allowed_change_set"]
    verify_only_surfaces = plan["verify_only_surfaces"]
    structured_ring = plan["dependency_ring_structured"]
    adjacent_read_nodes = structured_ring["adjacent_read_nodes"]

    path_decision = plan["path_decision"].strip()
    expected_read_set = expected_builder_read_set(path_decision)
    if expected_read_set is None:
        return fail(f"unsupported path_decision for builder read contract: {path_decision}")

    normalized_read_set = [item.strip() for item in allowed_read_set]

    if normalized_read_set != expected_read_set:
        return fail(
            "allowed_read_set does not match builder read contract for "
            f"path_decision={path_decision}: expected {expected_read_set}, got {normalized_read_set}"
        )

    actual_read_sources = ["02_plan.json"]
    if path_decision in {"lite", "heavy"}:
        manifest_file = base / "run_manifest.json"
        if not manifest_file.exists():
            return fail(f"missing run_manifest.json for {path_decision} builder read contract")
        try:
            manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
        except Exception:
            return fail(f"run_manifest.json is not valid JSON for {path_decision} builder read contract")
        if not isinstance(manifest, dict):
            return fail(f"run_manifest.json root must be an object for {path_decision} builder read contract")
        actual_read_sources.append("run_manifest.json")

    for source in actual_read_sources:
        if source not in adjacent_read_nodes:
            return fail(
                "builder actual read source is outside dependency_ring_structured.adjacent_read_nodes: "
                f"{source}"
            )

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
        f"Actual read sources: {', '.join(actual_read_sources)}\n"
        f"Path decision: {path_decision}\n"
        f"Declared allowed read set: {', '.join(expected_read_set)}\n\n"
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
