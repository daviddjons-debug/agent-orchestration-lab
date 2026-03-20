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
    ]
    for field in required_string_fields:
        value = manifest.get(field)
        if not isinstance(value, str) or not value.strip():
            print(f"ERROR: run_manifest.json missing non-empty string field: {field}")
            return 1

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
        value = manifest.get(field)
        if not isinstance(value, list):
            print(f"ERROR: run_manifest.json missing list field: {field}")
            return 1

    plan = {
        "source": ["01_orchestrator.md", "run_manifest.json"],
        "task_class": manifest.get("task_class"),
        "objective": manifest.get("objective"),
        "expected_end_state": manifest.get("expected_end_state"),
        "symptom": manifest.get("symptom"),
        "root_cause_hypothesis": manifest.get("root_cause_hypothesis"),
        "problem_locus": manifest.get("problem_locus"),
        "locus_confidence": manifest.get("locus_confidence"),
        "false_locality_risk": manifest.get("false_locality_risk"),
        "path_decision": manifest.get("path_decision"),
        "dependency_ring": manifest.get("dependency_ring", []),
        "allowed_read_set": manifest.get("allowed_read_set", []),
        "allowed_change_set": manifest.get("allowed_change_set", []),
        "verify_only_surfaces": manifest.get("verify_only_surfaces", []),
        "excluded_neighbors": manifest.get("excluded_neighbors", []),
        "forbidden_zone": manifest.get("forbidden_zone", []),
        "acceptance_criteria": manifest.get("acceptance_criteria", []),
        "verification_targets": manifest.get("verification_targets", []),
        "evidence_required": manifest.get("evidence_required", []),
        "blockers_or_uncertainties": manifest.get("blockers_or_uncertainties", []),
        "escalation_trigger": manifest.get("escalation_trigger", []),
        "patch_strategy": "declared-artifact bounded update",
        "change_rationale": "Current runnable planner preserves the orchestrator contract and keeps execution bounded to declared artifacts and report files.",
        "steps": [
            "Create output directories if missing.",
            "Create all files declared in manifest artifacts.",
            "Write declared content for each artifact.",
            "Record completion in 03_builder.md.",
        ],
        "artifacts": artifacts,
    }

    lines = [
        "# Planner Output",
        "",
        "Planner input scope: 01_orchestrator.md and run_manifest.json only",
        "",
        f"Task class: {plan['task_class']}",
        f"Objective: {plan['objective']}",
        f"Expected end state: {plan['expected_end_state']}",
        f"Symptom: {plan['symptom']}",
        f"Root-cause hypothesis: {plan['root_cause_hypothesis']}",
        f"Problem locus: {plan['problem_locus']}",
        f"Locus confidence: {plan['locus_confidence']}",
        f"False locality risk: {plan['false_locality_risk']}",
        f"Path decision: {plan['path_decision']}",
        f"Dependency ring: {', '.join(plan['dependency_ring'])}",
        f"Execution-stage allowed read set: {', '.join(plan['allowed_read_set'])}",
        f"Allowed change set: {', '.join(plan['allowed_change_set'])}",
        f"Verify-only surfaces: {', '.join(plan['verify_only_surfaces']) if plan['verify_only_surfaces'] else '(none)'}",
        f"Excluded neighbors: {', '.join(plan['excluded_neighbors']) if plan['excluded_neighbors'] else '(none)'}",
        f"Forbidden zone: {', '.join(plan['forbidden_zone'])}",
        f"Patch strategy: {plan['patch_strategy']}",
        f"Change rationale: {plan['change_rationale']}",
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
    ])
    for item in plan["acceptance_criteria"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "Verification targets:",
    ])
    for item in plan["verification_targets"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "Evidence required:",
    ])
    for item in plan["evidence_required"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "Blockers or uncertainties:",
    ])
    for item in plan["blockers_or_uncertainties"]:
        lines.append(f"- {item}")
    lines.extend([
        "",
        "Escalation triggers:",
    ])
    for item in plan["escalation_trigger"]:
        lines.append(f"- {item}")
    lines.append("")
    plan_text = "\n".join(lines)

    (base / "02_plan.json").write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8")
    (base / "02_planner.md").write_text(plan_text, encoding="utf-8")
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
