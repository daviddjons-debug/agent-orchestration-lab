from pathlib import Path
from datetime import datetime
import json
import sys

from runtime_contract import PROFILES, default_manifest


ORCHESTRATOR_HANDOFF_TEMPLATE = (
    "# Orchestrator Handoff\n\n"
    "Role: triage gate for the current runnable {profile} path.\n\n"
    "Assigned workflow:\n"
    "1. Planner must read only this handoff and run_manifest.json, then create 02_plan.json and emit 02_planner.md only when the active path keeps a separate planner trace.\n"
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
    if profile not in PROFILES:
        print("ERROR: profile must be one of baseline, lite, heavy")
        return 1
    run = "orchestrated-" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S-%f")
    base = root / run
    base.mkdir(parents=True, exist_ok=True)

    manifest = default_manifest(run, profile)

    orchestrator_handoff = ORCHESTRATOR_HANDOFF_TEMPLATE.format(profile=profile)
    (base / "01_orchestrator.md").write_text(orchestrator_handoff, encoding="utf-8")
    (base / "run_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    print(base)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
