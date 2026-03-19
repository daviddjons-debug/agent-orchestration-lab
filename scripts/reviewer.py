from pathlib import Path
import json
import sys

REQUIRED = [
    "00_user_goal.md",
    "01_orchestrator.md",
    "02_plan.json",
    "02_planner.md",
    "03_builder.md",
    "run_manifest.json",
]

CONTRACT_FIELDS = [
    "objective",
    "problem_locus",
    "dependency_ring",
    "allowed_read_set",
    "allowed_change_set",
    "forbidden_zone",
    "verification_targets",
    "blockers_or_uncertainties",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/reviewer.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    missing = [x for x in REQUIRED if not (base / x).exists()]

    plan_ok = False
    contract_checks = []
    artifact_checks = []
    artifact_results = []
    ok = False

    if not missing:
        try:
            manifest = json.loads((base / "run_manifest.json").read_text(encoding="utf-8"))
            plan = json.loads((base / "02_plan.json").read_text(encoding="utf-8"))
        except Exception:
            manifest = None
            plan = None

        manifest_artifacts = manifest.get("artifacts") if isinstance(manifest, dict) else None
        plan_artifacts = plan.get("artifacts") if isinstance(plan, dict) else None
        policy = manifest.get("review_policy", {}) if isinstance(manifest, dict) else {}

        require_valid_json = policy.get("require_valid_json", True)
        require_exact_text = policy.get("require_exact_text", True)

        contract_ok = []
        if isinstance(manifest, dict) and isinstance(plan, dict):
            for field in CONTRACT_FIELDS:
                same = manifest.get(field) == plan.get(field)
                contract_checks.append((field, same))
                contract_ok.append(same)

        artifacts_match = (
            isinstance(manifest_artifacts, list)
            and isinstance(plan_artifacts, list)
            and plan_artifacts == manifest_artifacts
        )

        plan_ok = artifacts_match and bool(contract_checks) and all(x[1] for x in contract_checks)

        if isinstance(manifest_artifacts, list):
            for spec in manifest_artifacts:
                path = spec.get("path", "<missing>")
                atype = spec.get("type")
                artifact = base / path
                exists_ok = artifact.exists()
                content_ok = False

                if exists_ok:
                    if atype == "json":
                        try:
                            data = json.loads(artifact.read_text(encoding="utf-8"))
                            required_fields = spec.get("required_fields")
                            if isinstance(required_fields, dict):
                                content_ok = isinstance(data, dict) and all(data.get(k) == v for k, v in required_fields.items())
                            elif not require_valid_json:
                                content_ok = True
                        except Exception:
                            content_ok = not require_valid_json
                    elif atype == "text":
                        exact_content = spec.get("exact_content")
                        if isinstance(exact_content, str):
                            actual = artifact.read_text(encoding="utf-8")
                            content_ok = (actual == exact_content) if require_exact_text else True

                artifact_checks.append((path, exists_ok, content_ok))
                artifact_results.append(exists_ok and content_ok)

        ok = (not missing) and plan_ok and bool(artifact_results) and all(artifact_results)

    lines = [
        "# Reviewer Verdict",
        "",
        "Source: files on disk, run_manifest.json, 02_plan.json, and review_policy",
        "",
        "Checklist:",
        f"- [{'x' if not missing else ' '}] Required prior artifacts exist",
        f"- [{'x' if plan_ok else ' '}] 02_plan.json matches full run_manifest.json contract",
    ]
    for field, same in contract_checks:
        lines.append(f"- [{'x' if same else ' '}] {field} matches between manifest and plan")
    for path, exists_ok, content_ok in artifact_checks:
        lines.append(f"- [{'x' if exists_ok else ' '}] {path} exists")
        lines.append(f"- [{'x' if content_ok else ' '}] {path} satisfies declared contract")
    lines.extend([
        "",
        f"Final verdict: {'PASS' if ok else 'FAIL'}",
        "",
    ])
    verdict = "\n".join(lines)

    (base / "04_reviewer.md").write_text(verdict, encoding="utf-8")
    print(verdict)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
