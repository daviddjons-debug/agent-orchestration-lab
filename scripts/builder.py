from pathlib import Path
import json
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/builder.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    plan_file = base / "02_planner.md"
    if not plan_file.exists():
        print("ERROR: missing 02_planner.md")
        return 1

    plan_text = plan_file.read_text(encoding="utf-8")

    artifact_prefix = "2. Create file "
    artifact_line = next((line for line in plan_text.splitlines() if line.startswith(artifact_prefix)), None)
    if artifact_line is None:
        print("ERROR: planner output does not define artifact path")
        return 1
    artifact_rel = artifact_line[len(artifact_prefix):].strip().rstrip(".")

    status_marker = "Write JSON field status:"
    message_marker = "Write JSON field message:"
    status_line = next((line for line in plan_text.splitlines() if status_marker in line), None)
    message_line = next((line for line in plan_text.splitlines() if message_marker in line), None)
    if status_line is None or message_line is None:
        print("ERROR: planner output does not define JSON fields")
        return 1

    status_value = status_line.split(status_marker, 1)[1].strip()
    message_value = message_line.split(message_marker, 1)[1].strip()

    artifact = base / artifact_rel
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text(json.dumps({"status": status_value, "message": message_value}, indent=2) + "\n", encoding="utf-8")

    builder_report = (
        "# Builder Output\n\n"
        "Source: 02_planner.md only\n\n"
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
