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
        "objective": manifest.get("objective", ""),
        "problem_locus": manifest.get("problem_locus", ""),
        "dependency_ring": manifest.get("dependency_ring", []),
        "allowed_read_set": manifest.get("allowed_read_set", []),
        "allowed_change_set": manifest.get("allowed_change_set", []),
        "verify_only_surfaces": manifest.get("verify_only_surfaces", []),
        "excluded_neighbors": manifest.get("excluded_neighbors", []),
        "forbidden_zone": manifest.get("forbidden_zone", []),
        "review_strictness": manifest.get("review_strictness", "standard"),
        "verification_targets": manifest.get("verification_targets", []),
        "blockers_or_uncertainties": manifest.get("blockers_or_uncertainties", []),
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
        "Planner input scope: 01_orchestrator.md and run_manifest.json only",
        "",
        f"Objective: {plan['objective']}",
        f"Problem locus: {plan['problem_locus']}",
        f"Dependency ring: {', '.join(plan['dependency_ring'])}",
        f"Execution-stage allowed read set: {', '.join(plan['allowed_read_set'])}",
        f"Allowed change set: {', '.join(plan['allowed_change_set'])}",
        f"Forbidden zone: {', '.join(plan['forbidden_zone'])}",
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
        "Verification targets:",
    ])
    for item in plan["verification_targets"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "Blockers or uncertainties:",
    ])
    for item in plan["blockers_or_uncertainties"]:
        lines.append(f"- {item}")
    lines.append("")
    plan_text = "\n".join(lines)

    (base / "02_plan.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    (base / "02_planner.md").write_text(plan_text, encoding="utf-8")
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
