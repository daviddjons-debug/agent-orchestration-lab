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
    consistency_checks = []
    undeclared_files = []
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

        if isinstance(manifest, dict) and isinstance(plan, dict):
            for field in CONTRACT_FIELDS:
                same = manifest.get(field) == plan.get(field)
                contract_checks.append((field, same))

        artifacts_match = (
            isinstance(manifest_artifacts, list)
            and isinstance(plan_artifacts, list)
            and plan_artifacts == manifest_artifacts
        )

        plan_ok = artifacts_match and bool(contract_checks) and all(same for _, same in contract_checks)

        declared_artifact_paths = []
        if isinstance(manifest_artifacts, list):
            for spec in manifest_artifacts:
                path = spec.get("path", "<missing>")
                declared_artifact_paths.append(path)

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

            allowed_files = set(REQUIRED + ["04_reviewer.md"] + declared_artifact_paths)
            for p in sorted(base.rglob("*")):
                if p.is_file():
                    rel = p.relative_to(base).as_posix()
                    if rel not in allowed_files:
                        undeclared_files.append(rel)

            declared_paths_set = set(declared_artifact_paths)
            summary_candidates = sorted(
                path for path in declared_artifact_paths
                if path == "summary.txt" or path.endswith("/summary.txt")
            )

            for summary_path in summary_candidates:
                summary_posix = Path(summary_path).as_posix()
                parent = Path(summary_posix).parent
                result_posix = (parent / "result.json").as_posix()
                if result_posix == ".":
                    result_posix = "result.json"
                if result_posix not in declared_paths_set:
                    continue

                result_json = base / result_posix
                summary_txt = base / summary_posix
                same_message = False

                if result_json.exists() and summary_txt.exists():
                    try:
                        result_data = json.loads(result_json.read_text(encoding="utf-8"))
                        json_message = result_data.get("message")
                        summary_message = summary_txt.read_text(encoding="utf-8").rstrip("\n")
                        same_message = isinstance(json_message, str) and summary_message == json_message
                    except Exception:
                        same_message = False

                consistency_checks.append((f"{result_posix} <-> {summary_posix} message consistency", same_message))

        ok = (
            (not missing)
            and plan_ok
            and bool(artifact_results)
            and all(artifact_results)
            and all(same for _, same in consistency_checks)
            and not undeclared_files
        )

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
    for label, same in consistency_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    lines.append(f"- [{'x' if not undeclared_files else ' '}] No undeclared output drift detected")
    if undeclared_files:
        lines.append("Undeclared files:")
        for path in undeclared_files:
            lines.append(f"- {path}")
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
