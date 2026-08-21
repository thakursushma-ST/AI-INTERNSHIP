def safe_text(value: str) -> str:
    return value.strip() if value else ""

def read_txt(file) -> str:
    return file.getvalue().decode("utf-8", errors="ignore")
