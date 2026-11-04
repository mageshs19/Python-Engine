"""Configured source copybook metadata, with no program-specific paths."""
from __future__ import annotations

from config.path_settings import copybook_paths


def read_source_copybook_members() -> dict[str, str]:
    members: dict[str, str] = {}
    for path in copybook_paths():
        # Never silently substitute a different member on read failure.
        members[path.stem.upper()] = path.read_text(encoding="utf-8-sig")
    return members
