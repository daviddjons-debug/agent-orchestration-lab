from __future__ import annotations

import copy

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


DEFAULT_REVIEW_POLICY = {
    "require_valid_json": True,
    "require_exact_text": True,
}

DEFAULT_BASELINE_ARTIFACTS = [
    {
        "path": "output/result.json",
        "type": "json",
        "required_fields": {
            "status": "ok",
            "message": "multi-agent orchestration check passed",
        },
    },
    {
        "path": "output/summary.txt",
        "type": "text",
        "exact_content": "multi-agent orchestration check passed\n",
    },
]

def default_manifest(run_id: str, profile: str) -> dict:
    return {
        "run_id": run_id,
        "task_class": "narrow_bugfix",
        "objective": "Produce declared artifacts for the current run contract",
        "expected_end_state": "Declared artifacts exist and satisfy the runnable contract checks.",
        "symptom": "Need a visible bounded multi-role run with falsifiable artifact validation.",
        "root_cause_hypothesis": "A small declared artifact contract can prove bounded orchestration behavior in the runnable lab.",
        "problem_locus": "run contract files and declared outputs",
        "locus_confidence": "high",
        "false_locality_risk": "low",
        "profile_selection_basis": PROFILE_SELECTION_BASIS_BY_PROFILE[profile],
        "path_decision": profile,
        "dependency_ring": [
            "01_orchestrator.md",
            "run_manifest.json",
            "02_plan.json",
            "output/",
        ],
        "dependency_ring_structured": {
            "primary_target": "output/",
            "adjacent_read_nodes": [
                "01_orchestrator.md",
                "run_manifest.json",
                "02_plan.json",
            ],
            "adjacent_verify_only_nodes": [],
            "excluded_neighbors": [],
        },
        "allowed_read_set": ALLOWED_READ_SET_BY_PROFILE[profile],
        "allowed_change_set": [
            "02_plan.json",
            "02_planner.md",
            "output/",
            "03_builder.md",
        ],
        "verify_only_surfaces": [],
        "excluded_neighbors": [],
        "forbidden_zone": [
            "scripts/",
            "docs/baseline_v1/",
        ],
        "acceptance_criteria": [
            "every declared artifact exists",
            "every JSON artifact satisfies required_fields",
            "every text artifact satisfies exact_content when required",
            "any missing file or content mismatch must cause reviewer FAIL",
        ],
        "verification_targets": [
            "manifest-plan alignment",
            "declared artifact existence",
            "declared artifact content checks",
        ],
        "evidence_required": [
            "reviewer verdict",
            "artifact existence checks",
            "artifact content checks",
        ],
        "blockers_or_uncertainties": [
            "the runnable lab does not enforce any stage-wide mechanically enforced read control beyond the current Builder-enforced read-boundary payload",
        ],
        "escalation_trigger": [
            "required Builder read exceeds allowed_read_set",
            "required edit exceeds allowed_change_set",
            "declared artifact contract becomes internally inconsistent",
        ],
        "artifacts": copy.deepcopy(DEFAULT_BASELINE_ARTIFACTS),
        "review_policy": copy.deepcopy(DEFAULT_REVIEW_POLICY),
    }
