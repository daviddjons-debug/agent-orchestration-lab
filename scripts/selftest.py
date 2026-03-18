from pathlib import Path
import json
import subprocess
import sys

def sh(cmd: list[str], allow_fail: bool = False) -> subprocess.CompletedProcess:
    print(f"$ {' '.join(cmd)}")
    cp = subprocess.run(cmd, capture_output=True, text=True)
    if cp.stdout:
        print(cp.stdout, end="" if cp.stdout.endswith("\n") else "\n")
    if cp.stderr:
        print(cp.stderr, end="" if cp.stderr.endswith("\n") else "\n", file=sys.stderr)
    if not allow_fail and cp.returncode != 0:
        raise SystemExit(cp.returncode)
    return cp

def latest_run(base: Path) -> Path:
    runs = sorted(base.glob("orchestrated-*"))
    if not runs:
        raise SystemExit("ERROR: no orchestrated run found")
    return runs[-1]

def main() -> int:
    base = Path("docs/runs")

    sh(["python3", "scripts/run_pipeline.py", str(base)])
    run_dir = latest_run(base)
    print(f"SELFTEST_RUN={run_dir}")

    manifest_file = run_dir / "run_manifest.json"
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))

    manifest["artifact_path"] = "output/custom/result.json"
    manifest["expected_message"] = "manifest override works"
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    override_pass = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in override_pass.stdout:
        print("SELFTEST ERROR: expected PASS after manifest override")
        return 1

    plan = run_dir / "02_planner.md"
    plan.write_text(
        "# Planner Output\n\n"
        "Source: 01_orchestrator.md and run_manifest.json only\n\n"
        "Plan:\n"
        "1. Create directory output if missing.\n"
        "2. Create file output/custom/result.json.\n"
        "3. Write JSON field status: WRONG\n"
        "4. Write JSON field message: WRONG VALUE\n"
        "5. Record completion in 03_builder.md.\n",
        encoding="utf-8",
    )

    sh(["python3", "scripts/builder.py", str(run_dir)])
    bad = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if "Final verdict: FAIL" not in bad.stdout:
        print("SELFTEST ERROR: expected FAIL on corrupted plan")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    good = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in good.stdout:
        print("SELFTEST ERROR: expected PASS after planner restore")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["review_policy"]["require_valid_json"] = False
    manifest["review_policy"]["require_exact_status"] = False
    manifest["review_policy"]["require_exact_message"] = False
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    artifact = run_dir / manifest["artifact_path"]
    artifact.parent.mkdir(parents=True, exist_ok=True)
    artifact.write_text("NOT JSON AT ALL\n", encoding="utf-8")

    relaxed = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in relaxed.stdout:
        print("SELFTEST ERROR: expected PASS on fully relaxed non-JSON policy")
        return 1

    print("SELFTEST RESULT: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
