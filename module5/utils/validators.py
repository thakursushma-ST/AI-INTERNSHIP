def require_text(value: str, label: str):
    if not value or not value.strip():
        return False, f"Please enter {label}."
    return True, ""

def valid_file_type(filename: str):
    return filename.lower().endswith((".txt", ".pdf"))
