from parser import parse_setting

def render_setting(raw: str) -> str:
    value = parse_setting(raw)
    return f"SETTING={value}"
