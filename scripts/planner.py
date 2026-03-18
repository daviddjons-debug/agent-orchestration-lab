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
    artifacts = manifest.get("artifacts")
    if not isinstance(artifacts, list) or not artifacts:
        print("ERROR: run_manifest.json missing non-empty artifacts list")
        return 1

    plan = {
        "source": ["01_orchestrator.md", "run_manifest.json"],
        "steps": [
            "Create output directories if missing.",
            "Create all files declared in manifest artifacts.",
            "Write declared content for each artifact.",
            "Record completion in 03_builder.md.",
        ],
        "artifacts": artifacts,
        "acceptance_criteria": [
            "every declared artifact exists",
            "every JSON artifact satisfies required_fields",
            "every text artifact satisfies exact_content when required",
            "any missing file or content mismatch must cause reviewer FAIL",
        ],
    }

    lines = [
        "# Planner Output",
        "",
        "Source: 01_orchestrator.md and run_manifest.json only",
        "",
        "Plan:",
        "1. Create output directories if missing.",
    ]
    for idx, artifact in enumerate(artifacts, start=2):
        path = artifact.get("path", "<missing>")
        atype = artifact.get("type", "<missing>")
        lines.append(f"{idx}. Create file {path} ({atype}).")
    lines.append(f"{len(artifacts) + 2}. Record completion in 03_builder.md.")
    lines.extend([
        "",
        "Acceptance criteria:",
        "- every declared artifact exists",
        "- every JSON artifact satisfies required_fields",
        "- every text artifact satisfies exact_content when required",
        "- any missing file or content mismatch must cause reviewer FAIL",
        "",
    ])
    plan_text = "\n".join(lines)

    (base / "02_plan.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    (base / "02_planner.md").write_text(plan_text, encoding="utf-8")
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
