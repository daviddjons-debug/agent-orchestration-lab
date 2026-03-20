from pathlib import Path
import json
import subprocess
import sys

def run(cmd: list[str]) -> int:
    print(f"$ {' '.join(cmd)}")
    completed = subprocess.run(cmd)
    return completed.returncode

def should_run_reviewer(run_dir: Path, profile: str) -> bool:
    if profile in {"lite", "heavy"}:
        return True

    manifest_file = run_dir / "run_manifest.json"
    if not manifest_file.exists():
        print("ERROR: missing run_manifest.json for reviewer activation decision")
        raise SystemExit(1)

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
    if len(sys.argv) > 3:
        print("Usage: python3 scripts/run_pipeline.py [run_root] [baseline|lite|heavy]")
        return 2

    base_dir = sys.argv[1] if len(sys.argv) >= 2 else "docs/runs"
    profile = sys.argv[2] if len(sys.argv) == 3 else "baseline"

    rc = run(["python3", "scripts/orchestrator.py", base_dir, profile])
    if rc != 0:
        return rc

    runs = sorted(Path(base_dir).glob("orchestrated-*"))
    if not runs:
        print("ERROR: no orchestrated run created")
        return 1

    run_dir = str(runs[-1])
    print(f"RUN_DIR={run_dir}")

    for cmd in (
        ["python3", "scripts/planner.py", run_dir],
        ["python3", "scripts/builder.py", run_dir],
    ):
        rc = run(cmd)
        if rc != 0:
            return rc

    if should_run_reviewer(Path(run_dir), profile):
        rc = run(["python3", "scripts/reviewer.py", run_dir])
        if rc != 0:
            return rc
    else:
        print("REVIEWER_SKIPPED=baseline compressed path (no declared review trigger)")

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
