from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
index_path = root / "index.html"
text = index_path.read_text(encoding="utf-8")
version = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")

patterns = [
    (
        r'(?P<prefix>href=["\'])stylesheet\.css(?P<suffix>["\'])',
        rf'\g<prefix>stylesheet.css?v={version}\g<suffix>',
    ),
    (
        r'(?P<prefix>src=["\'])(?P<path>(?:Images|GIFS|Music)/[^"\']+)(?P<suffix>["\'])',
        rf'\g<prefix>\g<path>?v={version}\g<suffix>',
    ),
]

for pattern, replacement in patterns:
    text, _ = re.subn(pattern, replacement, text)

index_path.write_text(text, encoding="utf-8")
