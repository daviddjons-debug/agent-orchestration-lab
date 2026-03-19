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
    previous_artifacts = [a.get("path") for a in manifest.get("artifacts", []) if isinstance(a, dict) and isinstance(a.get("path"), str)]

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

    for rel in previous_artifacts:
        target = run_dir / rel
        if target.exists():
            target.unlink()

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

    boundary_plan = json.loads((run_dir / "02_plan.json").read_text(encoding="utf-8"))
    boundary_plan["allowed_change_set"] = ["02_plan.json", "02_planner.md", "03_builder.md"]
    (run_dir / "02_plan.json").write_text(json.dumps(boundary_plan, indent=2) + "\n", encoding="utf-8")

    builder_boundary = sh(["python3", "scripts/builder.py", str(run_dir)], allow_fail=True)
    if builder_boundary.returncode == 0:
        print("SELFTEST ERROR: expected builder FAIL when artifact path is outside allowed_change_set")
        return 1
    boundary_text = (builder_boundary.stdout or "") + (builder_boundary.stderr or "")
    if "artifact path outside allowed_change_set" not in boundary_text or "output/custom/result.json" not in boundary_text:
        print("SELFTEST ERROR: expected explicit builder evidence for allowed_change_set enforcement")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    boundary_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in boundary_restored.stdout:
        print("SELFTEST ERROR: expected PASS after restoring builder boundary contract")
        return 1

    read_boundary_plan = json.loads((run_dir / "02_plan.json").read_text(encoding="utf-8"))
    read_boundary_plan["allowed_read_set"] = ["02_plan.json", "run_manifest.json"]
    (run_dir / "02_plan.json").write_text(json.dumps(read_boundary_plan, indent=2) + "\n", encoding="utf-8")

    builder_read_boundary = sh(["python3", "scripts/builder.py", str(run_dir)], allow_fail=True)
    if builder_read_boundary.returncode == 0:
        print("SELFTEST ERROR: expected builder FAIL when allowed_read_set exceeds baseline builder contract")
        return 1
    read_boundary_text = (builder_read_boundary.stdout or "") + (builder_read_boundary.stderr or "")
    if "allowed_read_set exceeds baseline builder read contract" not in read_boundary_text:
        print("SELFTEST ERROR: expected explicit builder evidence for allowed_read_set enforcement")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    read_boundary_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in read_boundary_restored.stdout:
        print("SELFTEST ERROR: expected PASS after restoring builder read boundary contract")
        return 1

    rogue = run_dir / "output/rogue.txt"
    rogue.parent.mkdir(parents=True, exist_ok=True)
    rogue.write_text("drift\n", encoding="utf-8")

    undeclared_drift = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if undeclared_drift.returncode == 0:
        print("SELFTEST ERROR: expected FAIL on undeclared output drift")
        return 1
    drift_text = (undeclared_drift.stdout or "") + (undeclared_drift.stderr or "")
    if "No undeclared output drift detected" not in drift_text or "output/rogue.txt" not in drift_text:
        print("SELFTEST ERROR: expected reviewer evidence for undeclared output drift")
        return 1

    rogue.unlink()
    drift_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in drift_restored.stdout:
        print("SELFTEST ERROR: expected PASS after removing undeclared output drift")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    json_artifact = next(a for a in manifest["artifacts"] if a["type"] == "json")
    text_artifact = next(a for a in manifest["artifacts"] if a["type"] == "text")

    artifact_json = run_dir / json_artifact["path"]
    artifact_text = run_dir / text_artifact["path"]

    stale_json = {"status": "ok", "message": "manifest override works"}
    artifact_json.write_text(json.dumps(stale_json, indent=2) + "\n", encoding="utf-8")
    artifact_text.write_text("STALE SUMMARY\n", encoding="utf-8")

    stale_summary = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if stale_summary.returncode == 0:
        print("SELFTEST ERROR: expected FAIL on stale adjacent summary")
        return 1
    stale_text = (stale_summary.stdout or "") + (stale_summary.stderr or "")
    if "message consistency" not in stale_text or "Final verdict: FAIL" not in stale_text:
        print("SELFTEST ERROR: expected reviewer evidence for adjacent summary inconsistency")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    stale_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in stale_restored.stdout:
        print("SELFTEST ERROR: expected PASS after restoring adjacent summary consistency")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    previous_artifacts = [
        a.get("path")
        for a in manifest.get("artifacts", [])
        if isinstance(a, dict) and isinstance(a.get("path"), str)
    ]
    for rel in previous_artifacts:
        target = run_dir / rel
        if target.exists():
            target.unlink()

    manifest["artifacts"] = [
        {
            "path": "src/spec.json",
            "type": "json",
            "required_fields": {
                "message": "cluster update works"
            },
        },
        {
            "path": "src/generated_summary.txt",
            "type": "text",
            "exact_content": "cluster update works\n",
        },
        {
            "path": "src/generated_manifest.json",
            "type": "json",
            "required_fields": {
                "message": "cluster update works"
            },
        },
    ]
    manifest["allowed_change_set"] = [
        "02_plan.json",
        "02_planner.md",
        "03_builder.md",
        "src/",
    ]
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    cluster_pass = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in cluster_pass.stdout:
        print("SELFTEST ERROR: expected PASS on Case 03 coordinated cluster scenario")
        return 1
    cluster_text = (cluster_pass.stdout or "") + (cluster_pass.stderr or "")
    if "src/spec.json <-> src/generated_summary.txt message consistency" not in cluster_text:
        print("SELFTEST ERROR: expected reviewer evidence for spec-summary cluster consistency")
        return 1
    if "src/spec.json <-> src/generated_manifest.json message consistency" not in cluster_text:
        print("SELFTEST ERROR: expected reviewer evidence for spec-manifest cluster consistency")
        return 1

    (run_dir / "src/generated_summary.txt").write_text("STALE CLUSTER SUMMARY\n", encoding="utf-8")
    cluster_stale = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if cluster_stale.returncode == 0:
        print("SELFTEST ERROR: expected FAIL on stale Case 03 dependent summary")
        return 1
    cluster_stale_text = (cluster_stale.stdout or "") + (cluster_stale.stderr or "")
    if "src/spec.json <-> src/generated_summary.txt message consistency" not in cluster_stale_text:
        print("SELFTEST ERROR: expected reviewer evidence for stale Case 03 summary inconsistency")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    cluster_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in cluster_restored.stdout:
        print("SELFTEST ERROR: expected PASS after restoring Case 03 coordinated cluster scenario")
        return 1

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
    manifest["allowed_change_set"] = [
        "02_plan.json",
        "02_planner.md",
        "output/",
        "03_builder.md",
    ]
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    src_dir = run_dir / "src"
    if src_dir.exists():
        for child in sorted(src_dir.rglob("*"), reverse=True):
            if child.is_file():
                child.unlink()
            elif child.is_dir():
                try:
                    child.rmdir()
                except OSError:
                    pass
        try:
            src_dir.rmdir()
        except OSError:
            pass

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])
    post_cluster_restore = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in post_cluster_restore.stdout:
        print("SELFTEST ERROR: expected PASS after restoring post-Case-03 baseline artifact scenario")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["review_policy"]["require_valid_json"] = False
    manifest["review_policy"]["require_exact_text"] = False
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    artifact_json = run_dir / json_artifact["path"]
    artifact_json.parent.mkdir(parents=True, exist_ok=True)
    artifact_json.write_text(
        json.dumps({"status": "ok", "message": "manifest override works"}, indent=2) + "\n",
        encoding="utf-8",
    )

    artifact_text = run_dir / text_artifact["path"]
    artifact_text.parent.mkdir(parents=True, exist_ok=True)
    artifact_text.write_text("manifest override works", encoding="utf-8")

    relaxed = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in relaxed.stdout:
        print("SELFTEST ERROR: expected PASS on relaxed artifact policy")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["objective"] = "Validate false-local success rejection with verify-only adjacent surface"
    manifest["problem_locus"] = "primary artifact may pass while adjacent verify-only surface remains unverified"
    manifest["dependency_ring"] = [
        "01_orchestrator.md",
        "run_manifest.json",
        "02_plan.json",
        "output/result.json",
        "output/adjacent_status.txt",
    ]
    manifest["allowed_read_set"] = ["02_plan.json"]
    manifest["allowed_change_set"] = [
        "02_plan.json",
        "02_planner.md",
        "output/",
        "03_builder.md",
    ]
    manifest["verify_only_surfaces"] = ["output/adjacent_status.txt"]
    manifest["excluded_neighbors"] = []
    manifest["review_strictness"] = "strict"
    manifest["verification_targets"] = [
        "manifest-plan alignment",
        "primary artifact contract",
        "verify-only adjacent surface satisfaction",
    ]
    manifest["artifacts"] = [
        {
            "path": "output/result.json",
            "type": "json",
            "required_fields": {
                "status": "ok",
                "message": "primary success",
            },
        },
    ]
    manifest["review_policy"]["require_valid_json"] = True
    manifest["review_policy"]["require_exact_text"] = True
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    for rel in ["output/result.json", "output/custom/result.json", "output/custom/summary.txt", "output/summary.txt", "output/adjacent_status.txt"]:
        target = run_dir / rel
        if target.exists():
            target.unlink()

    sh(["python3", "scripts/planner.py", str(run_dir)])
    sh(["python3", "scripts/builder.py", str(run_dir)])

    case04_fail = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if case04_fail.returncode == 0:
        print("SELFTEST ERROR: expected FAIL on Case 04 false-local missing verify-only surface")
        return 1
    case04_fail_text = (case04_fail.stdout or "") + (case04_fail.stderr or "")
    if "verify-only surface satisfied: output/adjacent_status.txt" not in case04_fail_text:
        print("SELFTEST ERROR: expected reviewer evidence for missing Case 04 verify-only surface")
        return 1

    adjacent = run_dir / "output/adjacent_status.txt"
    adjacent.parent.mkdir(parents=True, exist_ok=True)
    adjacent.write_text("adjacent verified\n", encoding="utf-8")

    case04_pass = sh(["python3", "scripts/reviewer.py", str(run_dir)])
    if "Final verdict: PASS" not in case04_pass.stdout:
        print("SELFTEST ERROR: expected PASS after satisfying Case 04 verify-only surface")
        return 1

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["objective"] = "Produce declared artifacts for the current run contract"
    manifest["problem_locus"] = "run contract files and declared outputs"
    manifest["dependency_ring"] = ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"]
    manifest["allowed_read_set"] = ["02_plan.json"]
    manifest["allowed_change_set"] = ["02_plan.json", "02_planner.md", "output/", "03_builder.md"]
    manifest["verify_only_surfaces"] = []
    manifest["excluded_neighbors"] = []
    manifest["review_strictness"] = "standard"
    manifest["verification_targets"] = ["manifest-plan alignment", "declared artifact existence", "declared artifact content checks"]
    manifest["artifacts"] = [
        {
            "path": json_artifact["path"],
            "type": "json",
            "required_fields": {
                "status": "ok",
                "message": "manifest override works",
            },
        },
        {
            "path": text_artifact["path"],
            "type": "text",
            "exact_content": "manifest override works\n",
        },
    ]
    manifest["review_policy"]["require_valid_json"] = False
    manifest["review_policy"]["require_exact_text"] = False
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    for rel in ["output/result.json", "output/adjacent_status.txt"]:
        target = run_dir / rel
        if target.exists():
            target.unlink()

    artifact_json = run_dir / json_artifact["path"]
    artifact_json.parent.mkdir(parents=True, exist_ok=True)
    artifact_json.write_text(
        json.dumps({"status": "ok", "message": "manifest override works"}, indent=2) + "\n",
        encoding="utf-8",
    )

    artifact_text = run_dir / text_artifact["path"]
    artifact_text.parent.mkdir(parents=True, exist_ok=True)
    artifact_text.write_text("manifest override works", encoding="utf-8")

    broken_plan = run_dir / "02_plan.json"
    broken_plan.write_text(
        json.dumps(
            {
                "source": ["01_orchestrator.md", "run_manifest.json"],
                "objective": "Produce declared artifacts for the current run contract",
                "problem_locus": "run contract files and declared outputs",
                "dependency_ring": ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"],
                "allowed_read_set": ["02_plan.json"],
                "allowed_change_set": ["02_plan.json", "02_planner.md", "output/", "03_builder.md"],
                "forbidden_zone": ["scripts/", "docs/baseline_v1/"],
                "verification_targets": ["manifest-plan alignment", "declared artifact existence", "declared artifact content checks"],
                "blockers_or_uncertainties": ["current runtime does not enforce read boundaries mechanically"],
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
