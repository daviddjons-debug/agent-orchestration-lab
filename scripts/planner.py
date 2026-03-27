from pathlib import Path
import json
import sys

from runtime_contract import MANIFEST_REQUIRED_LIST_FIELDS, MANIFEST_REQUIRED_STRING_FIELDS, build_plan_from_manifest, planner_trace_expected

# Current runnable pipeline note:
# dependency_ring remains the flat compatibility shape for runtime stability.
# dependency_ring_structured is the primary bounded-check shape used by the current
# runtime, while dependency_ring is still preserved for compatibility and fallback flow.

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

    for field in MANIFEST_REQUIRED_STRING_FIELDS:
        value = manifest.get(field)
        if not isinstance(value, str) or not value.strip():
            print(f"ERROR: run_manifest.json missing non-empty string field: {field}")
            return 1

    for field in MANIFEST_REQUIRED_LIST_FIELDS:
        value = manifest.get(field)
        if not isinstance(value, list):
            print(f"ERROR: run_manifest.json missing list field: {field}")
            return 1

    plan = build_plan_from_manifest(manifest)

    structured_ring = plan.get("dependency_ring_structured") or {}
    primary_target = structured_ring.get("primary_target") or plan["problem_locus"]
    adjacent_read_nodes = structured_ring.get("adjacent_read_nodes") or ["(none)"]
    adjacent_verify_only = structured_ring.get("adjacent_verify_only_nodes") or (
        plan["verify_only_surfaces"] if plan["verify_only_surfaces"] else ["(none)"]
    )
    excluded_neighbors = structured_ring.get("excluded_neighbors") or (
        plan["excluded_neighbors"] if plan["excluded_neighbors"] else ["(none)"]
    )
    bounded_scope_note = (
        "Current runnable planner preserves the flat compatibility dependency_ring for runtime stability "
        "while also carrying dependency_ring_structured as the target semantic shape."
    )

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
        f"Dependency ring (flat compatibility shape in the runnable lab): {', '.join(plan['dependency_ring'])}",
        f"Dependency ring structured primary target: {primary_target}",
        f"Dependency ring structured adjacent read nodes: {', '.join(adjacent_read_nodes)}",
        f"Dependency ring structured adjacent verify-only nodes: {', '.join(adjacent_verify_only)}",
        f"Dependency ring structured excluded neighbors: {', '.join(excluded_neighbors)}",
        f"Primary target (trace-level narrowing signal): {primary_target}",
        f"Adjacent verify-only nodes (trace-level): {', '.join(adjacent_verify_only)}",
        f"Excluded neighbors (trace-level): {', '.join(excluded_neighbors)}",
        f"Builder-compatible read boundary payload: {', '.join(plan['builder_read_boundary'])}",
        f"Allowed change set: {', '.join(plan['allowed_change_set'])}",
        f"Verify-only surfaces: {', '.join(plan['verify_only_surfaces']) if plan['verify_only_surfaces'] else '(none)'}",
        f"Source-of-truth node: {plan['source_of_truth_node'] if plan['source_of_truth_node'] else '(none)'}",
        f"Stale defect node: {plan['stale_defect_node'] if plan['stale_defect_node'] else '(none)'}",
        f"Adjacent consistency node: {plan['adjacent_consistency_node'] if plan['adjacent_consistency_node'] else '(none)'}",
        f"Expansion trigger: {plan['expansion_trigger'] if plan['expansion_trigger'] else '(none)'}",
        f"Re-triage required when actual blocker differs: {plan['retriage_required_when_actual_blocker_differs'] if plan['retriage_required_when_actual_blocker_differs'] is not None else '(none)'}",
        f"Excluded neighbors: {', '.join(plan['excluded_neighbors']) if plan['excluded_neighbors'] else '(none)'}",
        f"Forbidden zone: {', '.join(plan['forbidden_zone'])}",
        f"Patch strategy: {plan['patch_strategy']}",
        f"Change rationale: {plan['change_rationale']}",
        f"Bounded scope note: {bounded_scope_note}",
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
    planner_trace = base / "02_planner.md"
    if planner_trace_expected(plan["path_decision"]):
        planner_trace.write_text(plan_text, encoding="utf-8")
    elif planner_trace.exists():
        planner_trace.unlink()
    print(json.dumps(plan, indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
