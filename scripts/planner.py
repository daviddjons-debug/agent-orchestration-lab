from pathlib import Path
import json
import sys

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/planner.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    handoff = base / "01_orchestrator.md"
    manifest_file = base / "run_manifest.json"

    if not handoff.exists():
        print("ERROR: missing 01_orchestrator.md")
        return 1
    if not manifest_file.exists():
        print("ERROR: missing run_manifest.json")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    artifact_path = manifest["artifact_path"]
    expected_status = manifest["expected_status"]
    expected_message = manifest["expected_message"]

    plan_text = (
        "# Planner Output\n\n"
        "Source: 01_orchestrator.md and run_manifest.json only\n\n"
        "Plan:\n"
        "1. Create directory output if missing.\n"
        f"2. Create file {artifact_path}.\n"
        f"3. Write JSON field status: {expected_status}\n"
        f"4. Write JSON field message: {expected_message}\n"
        "5. Record completion in 03_builder.md.\n\n"
        "Acceptance criteria:\n"
        f"- {artifact_path} exists\n"
        "- file contains valid JSON\n"
        f"- status exactly equals: {expected_status}\n"
        f"- message exactly equals: {expected_message}\n"
        "- any mismatch must cause reviewer FAIL\n"
    )

    (base / "02_planner.md").write_text(plan_text, encoding="utf-8")
    print(plan_text)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
