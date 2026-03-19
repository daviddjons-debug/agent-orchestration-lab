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

    manifest["artifacts"] = [
        {
            "path": "output/custom/result.json",
            "type": "json",
            "required_fields": {
                "status": "ok",
                "message": "manifest override works",
            },
        },
        {
            "path": "output/custom/summary.txt",
            "type": "text",
            "exact_content": "manifest override works\n",
        },
    ]
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    override_pass = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in override_pass.stdout:
        print("SELFTEST ERROR: expected PASS after manifest override")
        return 1

    plan_file = run_dir / "02_plan.json"
    plan_data = json.loads(plan_file.read_text(encoding="utf-8"))
    corrupted = json.loads(json.dumps(plan_data))
    corrupted["artifacts"][0]["required_fields"]["status"] = "WRONG"
    corrupted["artifacts"][0]["required_fields"]["message"] = "WRONG VALUE"
    corrupted["artifacts"][1]["exact_content"] = "WRONG VALUE\n"
    plan_file.write_text(json.dumps(corrupted, indent=2) + "\n", encoding="utf-8")

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

    drifted_plan = json.loads((run_dir / "02_plan.json").read_text(encoding="utf-8"))
    drifted_plan["allowed_change_set"] = ["HACKED_SCOPE/"]
    (run_dir / "02_plan.json").write_text(json.dumps(drifted_plan, indent=2) + "\n", encoding="utf-8")

    surgical_drift = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if surgical_drift.returncode == 0:
        print("SELFTEST ERROR: expected FAIL on surgical contract drift")
        return 1
    if "allowed_change_set matches between manifest and plan" not in ((surgical_drift.stdout or "") + (surgical_drift.stderr or "")):
        print("SELFTEST ERROR: expected reviewer evidence for allowed_change_set drift")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    re_good = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in re_good.stdout:
        print("SELFTEST ERROR: expected PASS after restoring surgical contract")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["review_policy"]["require_valid_json"] = False
    manifest["review_policy"]["require_exact_text"] = False
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    json_artifact = next(a for a in manifest["artifacts"] if a["type"] == "json")
    text_artifact = next(a for a in manifest["artifacts"] if a["type"] == "text")

    artifact_json = run_dir / json_artifact["path"]
    artifact_json.parent.mkdir(parents=True, exist_ok=True)
    artifact_json.write_text("NOT JSON AT ALL\n", encoding="utf-8")

    artifact_text = run_dir / text_artifact["path"]
    artifact_text.parent.mkdir(parents=True, exist_ok=True)
    artifact_text.write_text("TOTALLY DIFFERENT TEXT\n", encoding="utf-8")

    relaxed = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in relaxed.stdout:
        print("SELFTEST ERROR: expected PASS on relaxed artifact policy")
        return 1

    broken_plan = run_dir / "02_plan.json"
    broken_plan.write_text(
        json.dumps(
            {
                "source": ["01_orchestrator.md", "run_manifest.json"],
                "objective": "Produce declared artifacts for the current run contract",
                "problem_locus": "run contract files and declared outputs",
                "dependency_ring": ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"],
                "allowed_read_set": ["01_orchestrator.md", "run_manifest.json"],
                "allowed_change_set": ["02_plan.json", "02_planner.md", "output/", "03_builder.md"],
                "forbidden_zone": ["scripts/", "docs/baseline_v1/"],
                "verification_targets": ["manifest-plan alignment", "declared artifact existence", "declared artifact content checks"],
                "blockers_or_uncertainties": ["current runtime does not enforce read/change boundaries mechanically"],
                "steps": ["broken"],
                "artifacts": [
                    {
                        "path": json_artifact["path"],
                        "type": "json"
                    }
                ],
                "acceptance_criteria": ["broken"],
            },
            indent=2,
        ) + "\n",
        encoding="utf-8",
    )

    print("== EXPECTED FAILURE: invalid 02_plan.json schema ==")
    invalid_plan = sh(["python3", "scripts/builder.py", str(run_dir)], allow_fail=True)
    if invalid_plan.returncode == 0:
        print("SELFTEST ERROR: expected builder failure on invalid 02_plan.json")
        return 1
    if "json artifact missing object field: required_fields" not in ((invalid_plan.stdout or "") + (invalid_plan.stderr or "")):
        print("SELFTEST ERROR: expected explicit schema error for invalid 02_plan.json")
        return 1
    print("Expected builder failure observed.")

    print("SELFTEST RESULT: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
