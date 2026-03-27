from __future__ import annotations

PROFILES = {"baseline", "lite", "heavy"}

ALLOWED_READ_SET_BY_PROFILE = {
    "baseline": ["02_plan.json"],
    "lite": ["02_plan.json", "run_manifest.json"],
    "heavy": ["02_plan.json", "run_manifest.json"],
}

PROFILE_SELECTION_BASIS_BY_PROFILE = {
    "baseline": [
        "locus is clear",
        "false locality risk is low",
        "no declared review trigger",
    ],
    "lite": [
        "bounded adjacent discipline is required",
        "reviewer is active by profile",
        "manifest read is required for builder evidence",
    ],
    "heavy": [
        "full review lane is active by profile",
        "manifest read is required for builder evidence",
        "task is routed to the widest active profile contract",
    ],
}

MANIFEST_REQUIRED_STRING_FIELDS = [
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

MANIFEST_REQUIRED_LIST_FIELDS = [
    "profile_selection_basis",
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

PLAN_REQUIRED_STRING_FIELDS = [
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

PLAN_REQUIRED_LIST_FIELDS = [
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

CONTRACT_FIELDS = [
    "task_class",
    "objective",
    "expected_end_state",
    "symptom",
    "root_cause_hypothesis",
    "problem_locus",
    "locus_confidence",
    "false_locality_risk",
    "profile_selection_basis",
    "path_decision",
    "dependency_ring",
    "dependency_ring_structured",
    "allowed_change_set",
    "verify_only_surfaces",
    "source_of_truth_node",
    "stale_defect_node",
    "adjacent_consistency_node",
    "expansion_trigger",
    "retriage_required_when_actual_blocker_differs",
    "excluded_neighbors",
    "forbidden_zone",
    "acceptance_criteria",
    "verification_targets",
    "evidence_required",
    "blockers_or_uncertainties",
    "escalation_trigger",
]

def expected_builder_read_set(path_decision: str) -> list[str] | None:
    return ALLOWED_READ_SET_BY_PROFILE.get(path_decision)

def planner_trace_expected(path_decision: str | None) -> bool:
    return path_decision in {"lite", "heavy"}
