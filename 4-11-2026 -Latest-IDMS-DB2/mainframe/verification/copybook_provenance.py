"""Derive and verify COPY members from explicit source/target relationships.

A missing renamed DB2 copybook is not interchangeable with an arbitrary source
copybook. The source must actually COPY the original member, the converted
program must COPY its deterministic name, and the unchanged record layout must
be independently measurable before a derived asset can be staged. The generated
COBOL program itself is never edited.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

from converter.services.name_derivation_resolver import NameDerivationResolver
from .cobol_storage_layout import group_byte_length
from .record_write_contract import _code

_COPY = re.compile(r'^COPY\s+([A-Z][A-Z0-9-]*)\s*\.', re.I)
_ROOT = re.compile(r'^01\s+([A-Z][A-Z0-9-]*)\b', re.I)


@dataclass(frozen=True)
class CopybookResolution:
    expanded_text: str
    staged_members: tuple[Path, ...]
    notes: tuple[str, ...]
    errors: tuple[str, ...]


def _copies(text: str) -> set[str]:
    return {match.group(1).upper() for line in text.splitlines()
            if (match := _COPY.match(_code(line)))}


def _member_path(folder: Path, name: str) -> Path | None:
    for suffix in ('.cpy', '.cbl', '.txt'):
        candidate = folder / (name + suffix)
        if candidate.is_file():
            return candidate
    return None


def _sub_outside_literals(code: str, pattern: re.Pattern[str], replacement: str) -> str:
    """Never change VALUE literals while renaming COPY data names."""
    parts: list[str] = []
    start = 0
    pos = 0
    while pos < len(code):
        if code[pos] not in ("'", '"'):
            pos += 1
            continue
        quote = code[pos]
        parts.append(pattern.sub(replacement, code[start:pos]))
        end = pos + 1
        while end < len(code):
            if code[end] == quote:
                if end + 1 < len(code) and code[end + 1] == quote:
                    end += 2
                    continue
                end += 1
                break
            end += 1
        parts.append(code[pos:end])
        pos = end
        start = end
    parts.append(pattern.sub(replacement, code[start:]))
    return ''.join(parts)


def _rename_root(source_text: str, before: str, after: str) -> str:
    # A derived name has exactly the same length, preserving sequence columns.
    pattern = re.compile(r'(?<![A-Z0-9-])' + re.escape(before) + r'(?![A-Z0-9])', re.I)
    result = []
    for line in source_text.splitlines(keepends=True):
        body = _code(line)
        if not body or body.upper().startswith('COPY '):
            result.append(line)
            continue
        if len(line) >= 7 and line[:6].isdigit():
            result.append(line[:7] + _sub_outside_literals(line[7:72], pattern, after) + line[72:])
        else:
            result.append(_sub_outside_literals(line, pattern, after))
    return ''.join(result)


def resolve_copybooks(source: str, target: str, authoritative: Path,
                      staged: Path) -> CopybookResolution:
    original_copies = _copies(source)
    target_copies = _copies(target)
    resolver = NameDerivationResolver()
    expanded = target
    new_members: list[Path] = []
    notes: list[str] = []
    errors: list[str] = []
    for target_name in sorted(target_copies):
        path = _member_path(authoritative, target_name)
        if path is not None:
            content = path.read_text(encoding='latin1')
            notes.append(f'authoritative target COPY {target_name}: {path.name}')
        else:
            candidates = [name for name in original_copies
                          if resolver.is_derivable(name) and resolver.derive(name) == target_name]
            if len(candidates) != 1:
                errors.append(f'COPY {target_name}: no unique source COPY proving renamed member origin')
                continue
            before = candidates[0]
            original_path = _member_path(authoritative, before)
            if original_path is None:
                errors.append(f'COPY {target_name}: source COPY {before} is absent from input library')
                continue
            original = original_path.read_text(encoding='latin1')
            if any(re.search(r'\bCOPY\b', _code(line), re.I) for line in original.splitlines()):
                errors.append(f'COPY {target_name}: nested COPY requires dependency expansion')
                continue
            content = _rename_root(original, before, target_name)
            original_roots = [m.group(1).upper() for line in original.splitlines()
                              if (m := _ROOT.match(_code(line)))]
            if len(original_roots) != 1 or not (
                original_roots[0] == before or original_roots[0].startswith(before + '-')
            ):
                errors.append(f'COPY {target_name}: source root is not a unique member-derived data name')
                continue
            old_root = original_roots[0]
            new_root = target_name + old_root[len(before):]
            try:
                old_size = group_byte_length(original, old_root)
                new_size = group_byte_length(content, new_root)
            except ValueError as exc:
                errors.append(f'COPY {target_name}: unproven source layout: {exc}')
                continue
            if old_size != new_size:
                errors.append(f'COPY {target_name}: derived copybook changes storage length')
                continue
            staged.mkdir(parents=True, exist_ok=True)
            artifact = staged / f'{target_name}.cpy'
            artifact.write_text(content, encoding='latin1')
            new_members.append(artifact)
            digest = hashlib.sha256(original.encode('latin1')).hexdigest()
            notes.append(f'derived COPY {before} -> {target_name}: {old_size} bytes; source sha256={digest}')
        # Expand only for independent static verification, never into the
        # generated COBOL member. COBOL COPY statements are whole source lines.
        replaced: list[str] = []
        for line in expanded.splitlines(keepends=True):
            match = _COPY.match(_code(line))
            if match and match.group(1).upper() == target_name:
                replaced.append(content.rstrip('\r\n') + '\n')
            else:
                replaced.append(line)
        expanded = ''.join(replaced)
    return CopybookResolution(expanded, tuple(new_members), tuple(notes), tuple(errors))
