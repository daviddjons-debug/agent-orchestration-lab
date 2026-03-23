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
        print("SELFTEST ERROR: expected builder FAIL when allowed_read_set mismatches baseline builder read contract")
        return 1
    read_boundary_text = (builder_read_boundary.stdout or "") + (builder_read_boundary.stderr or "")
    if "allowed_read_set does not match builder read contract for path_decision=baseline" not in read_boundary_text:
        print("SELFTEST ERROR: expected explicit builder evidence for baseline allowed_read_set enforcement")
        return 1

    read_boundary_plan = json.loads((run_dir / "02_plan.json").read_text(encoding="utf-8"))
    read_boundary_plan["path_decision"] = "heavy"
    read_boundary_plan["allowed_read_set"] = ["02_plan.json"]
    (run_dir / "02_plan.json").write_text(json.dumps(read_boundary_plan, indent=2) + "\n", encoding="utf-8")

    builder_heavy_read_boundary = sh(["python3", "scripts/builder.py", str(run_dir)], allow_fail=True)
    if builder_heavy_read_boundary.returncode == 0:
        print("SELFTEST ERROR: expected builder FAIL when heavy builder read contract is under-declared")
        return 1
    heavy_read_boundary_text = (builder_heavy_read_boundary.stdout or "") + (builder_heavy_read_boundary.stderr or "")
    if "allowed_read_set does not match builder read contract for path_decision=heavy" not in heavy_read_boundary_text:
        print("SELFTEST ERROR: expected explicit builder evidence for heavy allowed_read_set enforcement")
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
    manifest["dependency_ring_structured"] = {
        "primary_target": "output/result.json",
        "adjacent_read_nodes": [
            "01_orchestrator.md",
            "run_manifest.json",
            "02_plan.json",
        ],
        "adjacent_verify_only_nodes": ["output/adjacent_status.txt"],
        "excluded_neighbors": [],
    }
    manifest["allowed_read_set"] = ["02_plan.json"]
    manifest["allowed_change_set"] = [
        "02_plan.json",
        "02_planner.md",
        "output/",
        "03_builder.md",
    ]
    manifest["verify_only_surfaces"] = ["output/adjacent_status.txt"]
    manifest["excluded_neighbors"] = []
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
    manifest["retriage_required_when_actual_blocker_differs"] = True
    manifest_file.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    sh(["python3", "scripts/planner.py", str(run_dir)])

    retriage_plan = run_dir / "02_plan.json"
    retriage_data = json.loads(retriage_plan.read_text(encoding="utf-8"))
    retriage_data["allowed_change_set"] = ["BROKEN_SCOPE/"]
    retriage_plan.write_text(json.dumps(retriage_data, indent=2) + "\n", encoding="utf-8")

    retriage_fail = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if retriage_fail.returncode == 0:
        print("SELFTEST ERROR: expected FAIL when actual blocker differs under explicit re-triage requirement")
        return 1
    retriage_fail_text = (retriage_fail.stdout or "") + (retriage_fail.stderr or "")
    if "allowed_change_set matches between manifest and plan" not in retriage_fail_text:
        print("SELFTEST ERROR: expected reviewer evidence for actual blocker drift under re-triage branch")
        return 1

    retriage_data.pop("retriage_required_when_actual_blocker_differs", None)
    retriage_plan.write_text(json.dumps(retriage_data, indent=2) + "\n", encoding="utf-8")

    retriage_policy_missing = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if retriage_policy_missing.returncode == 0:
        print("SELFTEST ERROR: expected FAIL when re-triage policy is omitted from drifted plan")
        return 1
    retriage_policy_missing_text = (retriage_policy_missing.stdout or "") + (retriage_policy_missing.stderr or "")
    if "retriage_required_when_actual_blocker_differs matches between manifest and plan" not in retriage_policy_missing_text:
        print("SELFTEST ERROR: expected reviewer evidence for missing re-triage field alignment")
        return 1

    retriage_data["retriage_required_when_actual_blocker_differs"] = True
    retriage_plan.write_text(json.dumps(retriage_data, indent=2) + "\n", encoding="utf-8")

    retriage_policy_restored = sh(["python3", "scripts/reviewer.py", str(run_dir)], allow_fail=True)
    if retriage_policy_restored.returncode == 0:
        print("SELFTEST ERROR: expected FAIL to remain because actual blocker drift is still present after restoring re-triage policy")
        return 1

    sh(["python3", "scripts/planner.py", str(run_dir)])

    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    manifest["objective"] = "Produce declared artifacts for the current run contract"
    manifest["problem_locus"] = "run contract files and declared outputs"
    manifest["dependency_ring"] = ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"]
    manifest["dependency_ring_structured"] = {
        "primary_target": "output/",
        "adjacent_read_nodes": [
            "01_orchestrator.md",
            "run_manifest.json",
            "02_plan.json",
        ],
        "adjacent_verify_only_nodes": [],
        "excluded_neighbors": [],
    }
    manifest["allowed_read_set"] = ["02_plan.json"]
    manifest["allowed_change_set"] = ["02_plan.json", "02_planner.md", "output/", "03_builder.md"]
    manifest["verify_only_surfaces"] = []
    manifest["excluded_neighbors"] = []
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
                "task_class": "narrow_bugfix",
                "objective": "Produce declared artifacts for the current run contract",
                "expected_end_state": "Declared artifacts exist and satisfy the runnable contract checks.",
                "symptom": "Need a visible bounded multi-role run with falsifiable artifact validation.",
                "root_cause_hypothesis": "A small declared artifact contract can prove bounded orchestration behavior in the current runtime.",
                "problem_locus": "run contract files and declared outputs",
                "locus_confidence": "high",
                "false_locality_risk": "low",
                "path_decision": "baseline",
                "dependency_ring": ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"],
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
                "allowed_read_set": ["02_plan.json"],
                "allowed_change_set": ["02_plan.json", "02_planner.md", "output/", "03_builder.md"],
                "verify_only_surfaces": [],
                "excluded_neighbors": [],
                "forbidden_zone": ["scripts/", "docs/baseline_v1/"],
                "acceptance_criteria": ["broken"],
                "verification_targets": ["manifest-plan alignment", "declared artifact existence", "declared artifact content checks"],
                "evidence_required": ["reviewer verdict"],
                "blockers_or_uncertainties": ["current runtime does not enforce full stage-wide read sandboxing beyond the current Builder-only read-boundary contract"],
                "escalation_trigger": ["required edit exceeds allowed_change_set"],
                "patch_strategy": "declared-artifact bounded update",
                "change_rationale": "Broken schema fixture for selftest.",
                "steps": ["broken"],
                "artifacts": [
                    {
                        "path": json_artifact["path"],
                        "type": "json"
                    }
                ],
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


    print("== CASE 07: live bounded code with verify-only gate ==")
    case07_src = Path("lab_cases/case_07_live_bounded_code/src")
    parser_file = case07_src / "parser.py"
    adjacent_file = case07_src / "adjacent_contract.py"
    verify_file = case07_src / "verify_only_status.txt"

    parser_original = parser_file.read_text(encoding="utf-8")
    adjacent_original = adjacent_file.read_text(encoding="utf-8")
    verify_original = verify_file.read_text(encoding="utf-8")

    case07_code = """import sys
from pathlib import Path
sys.path.insert(0, "lab_cases/case_07_live_bounded_code/src")
from parser import parse_setting
from adjacent_contract import render_setting

assert parse_setting("  alpha  ") == "alpha"

parse_ok = False
render_ok = False

try:
    parse_setting("   ")
except ValueError:
    parse_ok = True

try:
    render_setting("   ")
except ValueError:
    render_ok = True

assert parse_ok, "expected ValueError for whitespace-only parse_setting input"
assert render_ok, "expected ValueError for whitespace-only render_setting input"

status = Path("lab_cases/case_07_live_bounded_code/src/verify_only_status.txt").read_text(encoding="utf-8").strip()
sys.exit(0 if status == "adjacent verified" else 1)
"""
    case07_cmd = ["python3", "-c", case07_code]

    try:
        verify_file.write_text("adjacent verification pending\n", encoding="utf-8")

        case07_fail = sh(case07_cmd, allow_fail=True)
        if case07_fail.returncode == 0:
            print("SELFTEST ERROR: expected FAIL on Case 07 when verify-only gate is pending")
            return 1

        if parser_file.read_text(encoding="utf-8") != parser_original:
            print("SELFTEST ERROR: parser.py changed during Case 07 fail path")
            return 1
        if adjacent_file.read_text(encoding="utf-8") != adjacent_original:
            print("SELFTEST ERROR: adjacent_contract.py changed during Case 07 fail path")
            return 1

        verify_file.write_text("adjacent verified\n", encoding="utf-8")

        case07_pass = sh(case07_cmd)
        if case07_pass.returncode != 0:
            print("SELFTEST ERROR: expected PASS on Case 07 after verify-only gate is satisfied")
            return 1

        if parser_file.read_text(encoding="utf-8") != parser_original:
            print("SELFTEST ERROR: parser.py changed during Case 07 pass path")
            return 1
        if adjacent_file.read_text(encoding="utf-8") != adjacent_original:
            print("SELFTEST ERROR: adjacent_contract.py changed during Case 07 pass path")
            return 1
    finally:
        parser_file.write_text(parser_original, encoding="utf-8")
        adjacent_file.write_text(adjacent_original, encoding="utf-8")
        verify_file.write_text(verify_original, encoding="utf-8")

    print("== PIPELINE ACTIVATION CHECK: baseline vs lite reviewer behavior ==")
    baseline_pipeline = sh(["python3", "scripts/run_pipeline.py", str(base), "baseline"])
    baseline_runs = sorted(base.glob("orchestrated-*"))
    if not baseline_runs:
        print("SELFTEST ERROR: expected baseline pipeline run directory")
        return 1
    baseline_run = baseline_runs[-1]
    baseline_output = (baseline_pipeline.stdout or "") + (baseline_pipeline.stderr or "")
    if "REVIEWER_SKIPPED=Direct policy / baseline runtime path (no declared review trigger)" not in baseline_output:
        print("SELFTEST ERROR: expected Direct/baseline pipeline to skip reviewer on no-trigger path")
        return 1
    if (baseline_run / "04_reviewer.md").exists():
        print("SELFTEST ERROR: baseline compressed pipeline must not emit 04_reviewer.md")
        return 1

    lite_pipeline = sh(["python3", "scripts/run_pipeline.py", str(base), "lite"])
    lite_runs = sorted(base.glob("orchestrated-*"))
    if len(lite_runs) < 2:
        print("SELFTEST ERROR: expected lite pipeline run directory")
        return 1
    lite_run = lite_runs[-1]
    lite_output = (lite_pipeline.stdout or "") + (lite_pipeline.stderr or "")
    if "Final verdict: PASS" not in lite_output:
        print("SELFTEST ERROR: expected lite pipeline reviewer PASS")
        return 1
    if not (lite_run / "04_reviewer.md").exists():
        print("SELFTEST ERROR: lite pipeline must emit 04_reviewer.md")
        return 1

    print("SELFTEST RESULT: PASS")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
