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

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/reviewer.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    missing = [x for x in REQUIRED if not (base / x).exists()]

    artifact_rel = "output/result.json"
    expected_status = "ok"
    expected_message = "multi-agent orchestration check passed"
    require_valid_json = True
    require_exact_status = True
    require_exact_message = True

    artifact = base / artifact_rel
    plan_ok = False
    json_ok = False
    status_ok = False
    message_ok = False

    if not missing:
        manifest = json.loads((base / "run_manifest.json").read_text(encoding="utf-8"))
        artifact_rel = manifest["artifact_path"]
        expected_status = manifest["expected_status"]
        expected_message = manifest["expected_message"]

        policy = manifest.get("review_policy", {})
        require_valid_json = policy.get("require_valid_json", True)
        require_exact_status = policy.get("require_exact_status", True)
        require_exact_message = policy.get("require_exact_message", True)

        artifact = base / artifact_rel

        try:
            plan = json.loads((base / "02_plan.json").read_text(encoding="utf-8"))
            plan_ok = (
                isinstance(plan, dict)
                and plan.get("artifact_path") == artifact_rel
                and isinstance(plan.get("payload"), dict)
                and plan["payload"].get("status") == expected_status
                and plan["payload"].get("message") == expected_message
            )
        except Exception:
            plan_ok = False

        if artifact.exists():
            try:
                data = json.loads(artifact.read_text(encoding="utf-8"))
                json_ok = isinstance(data, dict)
                status_ok = json_ok and ((data.get("status") == expected_status) if require_exact_status else ("status" in data))
                message_ok = json_ok and ((data.get("message") == expected_message) if require_exact_message else ("message" in data))
            except Exception:
                json_ok = False

        if not require_valid_json:
            json_ok = artifact.exists()
            if not require_exact_status:
                status_ok = artifact.exists()
            if not require_exact_message:
                message_ok = artifact.exists()

    ok = (not missing) and plan_ok and artifact.exists() and json_ok and status_ok and message_ok

    verdict = (
        "# Reviewer Verdict\n\n"
        "Source: files on disk, run_manifest.json, 02_plan.json, and review_policy\n\n"
        "Checklist:\n"
        f"- [{'x' if not missing else ' '}] Required prior artifacts exist\n"
        f"- [{'x' if plan_ok else ' '}] 02_plan.json matches run_manifest.json contract\n"
        f"- [{'x' if artifact.exists() else ' '}] {artifact_rel} exists\n"
        f"- [{'x' if json_ok else ' '}] {artifact_rel} satisfies JSON policy\n"
        f"- [{'x' if status_ok else ' '}] status satisfies policy\n"
        f"- [{'x' if message_ok else ' '}] message satisfies policy\n\n"
        f"Final verdict: {'PASS' if ok else 'FAIL'}\n"
    )

    (base / "04_reviewer.md").write_text(verdict, encoding="utf-8")
    print(verdict)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
