def parse_setting(raw: str) -> str:
    value = raw.strip()
    if value == "":
        raise ValueError("empty setting")
    return value
