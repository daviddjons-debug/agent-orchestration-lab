from pathlib import Path
import subprocess
import sys

def run(cmd: list[str]) -> int:
    print(f"$ {' '.join(cmd)}")
    completed = subprocess.run(cmd)
    return completed.returncode

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
        ["python3", "scripts/reviewer.py", run_dir],
    ):
        rc = run(cmd)
        if rc != 0:
            return rc

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
