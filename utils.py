import re

def extract_first_url(text: str):
    m = re.search(r"https?://\S+", text)
    return m.group(0) if m else None

def safe_preview(text: str, length: int = 200):
    if not text:
        return "(empty)"
    return text if len(text) <= length else text[:length] + "..."
