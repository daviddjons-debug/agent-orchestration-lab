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
    "reviewer_focus",
    "tester_focus",
    "security_focus",
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


def build_plan_from_manifest(manifest: dict) -> dict:
    structured_ring = manifest.get("dependency_ring_structured") or {}
    structured_verify_only = structured_ring.get("adjacent_verify_only_nodes")
    structured_excluded_neighbors = structured_ring.get("excluded_neighbors")
    artifacts = manifest.get("artifacts")

    return {
        "source": ["01_orchestrator.md", "run_manifest.json"],
        "task_class": manifest.get("task_class"),
        "objective": manifest.get("objective"),
        "expected_end_state": manifest.get("expected_end_state"),
        "symptom": manifest.get("symptom"),
        "root_cause_hypothesis": manifest.get("root_cause_hypothesis"),
        "problem_locus": manifest.get("problem_locus"),
        "locus_confidence": manifest.get("locus_confidence"),
        "false_locality_risk": manifest.get("false_locality_risk"),
        "profile_selection_basis": manifest.get("profile_selection_basis", []),
        "path_decision": manifest.get("path_decision"),
        "dependency_ring": manifest.get("dependency_ring", []),
        "dependency_ring_structured": structured_ring,
        "allowed_read_set": manifest.get("allowed_read_set", []),
        "builder_read_boundary": manifest.get("allowed_read_set", []),
        "allowed_change_set": manifest.get("allowed_change_set", []),
        "verify_only_surfaces": (
            structured_verify_only
            if isinstance(structured_verify_only, list)
            else manifest.get("verify_only_surfaces", [])
        ),
        "source_of_truth_node": manifest.get("source_of_truth_node"),
        "stale_defect_node": manifest.get("stale_defect_node"),
        "adjacent_consistency_node": manifest.get("adjacent_consistency_node"),
        "expansion_trigger": manifest.get("expansion_trigger"),
        "retriage_required_when_actual_blocker_differs": manifest.get("retriage_required_when_actual_blocker_differs"),
        "reviewer_focus": manifest.get("reviewer_focus"),
        "tester_focus": manifest.get("tester_focus"),
        "security_focus": manifest.get("security_focus"),
        "excluded_neighbors": (
            structured_excluded_neighbors
            if isinstance(structured_excluded_neighbors, list)
            else manifest.get("excluded_neighbors", [])
        ),
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


def reviewer_required_by_manifest(manifest: dict) -> bool:
    path_decision = manifest.get("path_decision")
    structured_ring = manifest.get("dependency_ring_structured", {}) if isinstance(manifest, dict) else {}

    if path_decision in {"lite", "heavy"}:
        return True
    if manifest.get("verify_only_surfaces"):
        return True
    if isinstance(structured_ring, dict) and structured_ring.get("adjacent_verify_only_nodes"):
        return True
    if manifest.get("retriage_required_when_actual_blocker_differs") is True:
        return True
    if manifest.get("source_of_truth_node"):
        return True
    if manifest.get("stale_defect_node"):
        return True
    if manifest.get("adjacent_consistency_node"):
        return True
    return False


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
        "reviewer_focus": None,
        "tester_focus": None,
        "security_focus": None,
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
