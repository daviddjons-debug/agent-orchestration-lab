from pathlib import Path
import json
import subprocess
import sys


def run(cmd: list[str]) -> int:
    completed = subprocess.run(cmd)
    return completed.returncode


def should_run_reviewer(run_dir: Path, profile: str) -> bool:
    if profile in {"lite", "heavy"}:
        return True

    manifest_file = run_dir / "run_manifest.json"
    if not manifest_file.exists():
        print("ERROR: missing run_manifest.json for reviewer activation decision")
        return False

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    if manifest.get("verify_only_surfaces"):
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


def main() -> int:
    if len(sys.argv) not in {2, 3}:
        print("Usage: python3 scripts/run_pipeline.py [run_root] [baseline|lite|heavy]")
        return 2

    base_dir = Path(sys.argv[1])
    profile = sys.argv[2] if len(sys.argv) == 3 else "baseline"

    rc = run(["python3", "scripts/orchestrator.py", str(base_dir), profile])
    if rc != 0:
        return rc

    runs = sorted(base_dir.glob("orchestrated-*"))
    if not runs:
        print("ERROR: orchestrator did not create run directory")
        return 1

    run_dir = runs[-1]


    rc = run(["python3", "scripts/planner.py", str(run_dir)])
    if rc != 0:
        return rc

    rc = run(["python3", "scripts/builder.py", str(run_dir)])
    if rc != 0:
        return rc

    if should_run_reviewer(run_dir, profile):
        rc = run(["python3", "scripts/reviewer.py", str(run_dir)])
        if rc != 0:
            return rc
    else:
        print("REVIEWER_SKIPPED=baseline compressed path (no declared review trigger)")

    print(run_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
