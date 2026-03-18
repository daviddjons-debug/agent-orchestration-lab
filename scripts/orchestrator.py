from pathlib import Path
from datetime import datetime
import json
import sys

USER_GOAL = (
    "# User Goal\n\n"
    "Create a tiny, verifiable multi-agent run with visible handoffs, "
    "executed as separate role scripts.\n"
)

ORCHESTRATOR_HANDOFF = (
    "# Orchestrator Handoff\n\n"
    "Assigned workflow:\n"
    "1. Planner must read only this handoff and run_manifest.json, then create 02_plan.json and 02_planner.md.\n"
    "2. Builder must read only 02_plan.json and create output/result.json plus 03_builder.md.\n"
    "3. Reviewer must evaluate files on disk and write 04_reviewer.md.\n\n"
    "Constraints:\n"
    "- Expected artifact path: output/result.json\n"
    "- Expected JSON field status: ok\n"
    "- Expected JSON field message: multi-agent orchestration check passed\n"
    "- Any missing file or content mismatch = FAIL\n"
)

def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) == 2 else Path("docs/runs")
    run = "orchestrated-" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    base = root / run
    base.mkdir(parents=True, exist_ok=True)

    manifest = {
        "run_id": run,
        "artifact_path": "output/result.json",
        "expected_status": "ok",
        "expected_message": "multi-agent orchestration check passed",
        "review_policy": {
            "require_valid_json": True,
            "require_exact_status": True,
            "require_exact_message": True,
        },
    }

    (base / "00_user_goal.md").write_text(USER_GOAL, encoding="utf-8")
    (base / "01_orchestrator.md").write_text(ORCHESTRATOR_HANDOFF, encoding="utf-8")
    (base / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(base)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
