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

    artifact_rel = plan.get("artifact_path")
    payload = plan.get("payload")

    if not isinstance(artifact_rel, str) or not artifact_rel.strip():
        return fail("02_plan.json missing non-empty string field: artifact_path")
    if not isinstance(payload, dict):
        return fail("02_plan.json missing object field: payload")

    status_value = payload.get("status")
    message_value = payload.get("message")

    if not isinstance(status_value, str):
        return fail("02_plan.json payload missing string field: status")
    if not isinstance(message_value, str):
        return fail("02_plan.json payload missing string field: message")

    artifact = base / artifact_rel
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text(json.dumps({"status": status_value, "message": message_value}, indent=2) + "\n", encoding="utf-8")

    builder_report = (
        "# Builder Output\n\n"
        "Source: 02_plan.json only\n\n"
        "Actions completed:\n"
        f"- created {artifact_rel}\n"
        f"- wrote JSON from planner: status={status_value}, message={message_value}\n\n"
        "Artifact path:\n"
        f"- {artifact_rel}\n"
    )
    (base / "03_builder.md").write_text(builder_report, encoding="utf-8")
    print(builder_report)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
