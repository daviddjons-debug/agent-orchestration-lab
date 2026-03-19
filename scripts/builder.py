from pathlib import Path
import json
import sys

def fail(msg: str) -> int:
    print(f"ERROR: {msg}")
    return 1

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
        "objective",
        "problem_locus",
    ]
    for field in required_string_fields:
        value = plan.get(field)
        if not isinstance(value, str) or not value.strip():
            return fail(f"02_plan.json missing non-empty string field: {field}")

    required_list_fields = [
        "dependency_ring",
        "allowed_read_set",
        "allowed_change_set",
        "forbidden_zone",
        "verification_targets",
        "blockers_or_uncertainties",
    ]
    for field in required_list_fields:
        value = plan.get(field)
        if not isinstance(value, list) or not value or not all(isinstance(x, str) and x.strip() for x in value):
            return fail(f"02_plan.json missing non-empty string-list field: {field}")

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

    builder_report = (
        "# Builder Output\n\n"
        "Source: 02_plan.json only\n\n"
        "Actions completed:\n"
        + "\n".join(created)
        + "\n\nArtifact paths:\n"
        + "\n".join(f"- {a['path']}" for a in artifacts)
        + "\n"
    )
    (base / "03_builder.md").write_text(builder_report, encoding="utf-8")
    print(builder_report)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
