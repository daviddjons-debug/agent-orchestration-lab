from pathlib import Path
import importlib.util
import sys

BASE = Path("lab_cases/case_07_live_bounded_code/src")
PARSER = BASE / "parser.py"
ADJACENT = BASE / "adjacent_contract.py"
VERIFY = BASE / "verify_only_status.txt"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, str(path))
    if spec is None or spec.loader is None:
        raise RuntimeError(f"unable to load module: {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> int:
    for req in (PARSER, ADJACENT, VERIFY):
        if not req.exists():
            print(f"ERROR: missing required file: {req}")
            return 1

    sys.path.insert(0, str(BASE))
    try:
        parser_mod = load_module("case07_parser", PARSER)
        adjacent_mod = load_module("case07_adjacent", ADJACENT)

        parse_setting = getattr(parser_mod, "parse_setting", None)
        render_setting = getattr(adjacent_mod, "render_setting", None)

        if not callable(parse_setting):
            print("ERROR: parse_setting missing or not callable")
            return 1
        if not callable(render_setting):
            print("ERROR: render_setting missing or not callable")
            return 1

        alpha = parse_setting("  alpha  ")
        if alpha != "alpha":
            print(f"ERROR: expected parse_setting('  alpha  ') == 'alpha', got {alpha!r}")
            return 1

        try:
            parse_setting("   ")
            print("ERROR: expected parse_setting('   ') to raise ValueError")
            return 1
        except ValueError:
            pass

        try:
            render_setting("   ")
            print("ERROR: expected render_setting('   ') to raise ValueError")
            return 1
        except ValueError:
            pass

        verify_text = VERIFY.read_text(encoding="utf-8")
        if verify_text != "adjacent verified\n":
            print(f"ERROR: expected verify-only status to be 'adjacent verified\\n', got {verify_text!r}")
            return 1

        print("CASE07 RESULT: PASS")
        print(" - primary fix verified")
        print(" - adjacent dependency behavior verified")
        print(" - verify-only completion evidence verified")
        return 0
    finally:
        try:
            sys.path.remove(str(BASE))
        except ValueError:
            pass


if __name__ == "__main__":
    raise SystemExit(main())
