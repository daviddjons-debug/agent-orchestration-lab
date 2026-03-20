from pathlib import Path
from datetime import datetime
import json
import sys

USER_GOAL = (
    "# User Goal\n\n"
    "Create a tiny, verifiable multi-agent run with visible handoffs, "
    "executed as separate role scripts.\n"
)

ORCHESTRATOR_HANDOFF_TEMPLATE = (
    "# Orchestrator Handoff\n\n"
    "Role: triage gate for the current runnable {profile} path.\n\n"
    "Assigned workflow:\n"
    "1. Planner must read only this handoff and run_manifest.json, then create 02_plan.json and 02_planner.md.\n"
    "2. Builder must read only 02_plan.json and create all declared output files plus 03_builder.md.\n"
    "3. Reviewer must evaluate files on disk and write 04_reviewer.md.\n\n"
    "Triage decisions declared in run_manifest.json are the contract source of truth for this run.\n"
    "No downstream role may silently widen scope.\n"
)

def main() -> int:
    if len(sys.argv) > 3:
        print("Usage: python3 scripts/orchestrator.py [run_root] [baseline|lite|heavy]")
        return 2

    root = Path(sys.argv[1]) if len(sys.argv) >= 2 else Path("docs/runs")
    profile = sys.argv[2] if len(sys.argv) == 3 else "baseline"
    if profile not in {"baseline", "lite", "heavy"}:
        print("ERROR: profile must be one of baseline, lite, heavy")
        return 1
    run = "orchestrated-" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base = root / run
    base.mkdir(parents=True, exist_ok=True)

    allowed_read_set_by_profile = {
        "baseline": ["02_plan.json"],
        "lite": ["02_plan.json", "run_manifest.json"],
        "heavy": ["02_plan.json", "run_manifest.json"],
    }

    manifest = {
        "run_id": run,
        "task_class": "narrow_bugfix",
        "objective": "Produce declared artifacts for the current run contract",
        "expected_end_state": "Declared artifacts exist and satisfy the runnable contract checks.",
        "symptom": "Need a visible bounded multi-role run with falsifiable artifact validation.",
        "root_cause_hypothesis": "A small declared artifact contract can prove bounded orchestration behavior in the current runtime.",
        "problem_locus": "run contract files and declared outputs",
        "locus_confidence": "high",
        "false_locality_risk": "low",
        "path_decision": profile,
        "dependency_ring": [
            "01_orchestrator.md",
            "run_manifest.json",
            "02_plan.json",
            "output/",
        ],
        "allowed_read_set": allowed_read_set_by_profile[profile],
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
            "current runtime does not enforce full mechanical read sandboxing",
        ],
        "escalation_trigger": [
            "required read exceeds allowed_read_set",
            "required edit exceeds allowed_change_set",
            "declared artifact contract becomes internally inconsistent",
        ],
        "artifacts": [
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
        ],
        "review_policy": {
            "require_valid_json": True,
            "require_exact_text": True,
        },
    }

    (base / "00_user_goal.md").write_text(USER_GOAL, encoding="utf-8")
    orchestrator_handoff = ORCHESTRATOR_HANDOFF_TEMPLATE.format(profile=profile)
    (base / "01_orchestrator.md").write_text(orchestrator_handoff, encoding="utf-8")
    (base / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(base)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
