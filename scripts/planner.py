from pathlib import Path
import sys

PLAN_TEXT = (
    "# Planner Output\n\n"
    "Source: 01_orchestrator.md only\n\n"
    "Plan:\n"
    "1. Create directory output if missing.\n"
    "2. Create file output/result.json.\n"
    "3. Write JSON field status: ok\n"
    "4. Write JSON field message: multi-agent orchestration check passed\n"
    "5. Record completion in 03_builder.md.\n\n"
    "Acceptance criteria:\n"
    "- output/result.json exists\n"
    "- file contains valid JSON\n"
    "- status exactly equals: ok\n"
    "- message exactly equals: multi-agent orchestration check passed\n"
    "- any mismatch must cause reviewer FAIL\n"
)

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/planner.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    handoff = base / "01_orchestrator.md"
    if not handoff.exists():
        print("ERROR: missing 01_orchestrator.md")
        return 1

    (base / "02_planner.md").write_text(PLAN_TEXT, encoding="utf-8")
    print(PLAN_TEXT)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
