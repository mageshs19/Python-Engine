"""Strict, independent byte-size verifier for COBOL fixed-record groups.

Supports elementary DISPLAY and packed-decimal (COMP-3) PICTURE clauses,
REDEFINES, nested groups and FILLER. Unknown storage features are rejected;
we never guess a wire length for a production output record.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

_DECL = re.compile(r'^\s*(\d{2})\s+([A-Z][A-Z0-9-]*|FILLER)\b(.*)', re.I)
_PIC = re.compile(r'\bPIC(?:TURE)?\s+(?:IS\s+)?([A-Z0-9()VS]+)', re.I)
_REDEF = re.compile(r'\bREDEFINES\s+([A-Z][A-Z0-9-]*)\b', re.I)
_PIC_ELEMENT = re.compile(r'([9XANZ])(?:\((\d+)\))?', re.I)
_OCCURS = re.compile(r'\bOCCURS\s+(\d+)\b(?:\s+TIMES)?', re.I)


@dataclass
class Field:
    level: int
    name: str
    source: str
    children: list['Field'] = field(default_factory=list)
    parent: 'Field | None' = None


def _body(raw: str) -> str:
    if len(raw) >= 7 and raw[:6].isdigit():
        if raw[6] in {'*', '/', 'D', 'd'}:
            return ''
        return raw[7:72].strip()
    return raw.strip() if not raw.lstrip().startswith('*') else ''


def extract_group(text: str, group_name: str) -> Field:
    """Extract the named level-01 group, preserving hierarchy and PIC continuations."""
    target = group_name.upper()
    root: Field | None = None
    stack: list[Field] = []
    for line in text.splitlines():
        code = _body(line)
        if not code:
            continue
        match = _DECL.match(code)
        if match:
            level, name = int(match.group(1)), match.group(2).upper()
            if root is None:
                if level != 1 or name != target:
                    continue
                root = Field(level, name, match.group(3).strip())
                stack = [root]
                continue
            if level == 88:
                # COBOL condition names occupy no additional storage.
                continue
            if level <= root.level:
                break
            while stack and stack[-1].level >= level:
                stack.pop()
            if not stack:
                raise ValueError('invalid COBOL level hierarchy')
            node = Field(level, name, match.group(3).strip(), parent=stack[-1])
            stack[-1].children.append(node)
            stack.append(node)
        elif root is not None and stack:
            # Continued PIC or USAGE clause, not a new field declaration.
            stack[-1].source += ' ' + code
    if root is None:
        raise ValueError(f'level-01 group {target} not found')
    return root


def _picture_bytes(node: Field) -> int:
    src = node.source.upper()
    if re.search(r'\b(?:DEPENDING|SIGN\s+IS\s+|USAGE\s+(?:IS\s+)?(?:COMP|BINARY|COMP-1|COMP-2)|SYNCHRONIZED)\b', src):
        raise ValueError(f'unsupported storage declaration {node.name}: {src}')
    match = _PIC.search(src)
    if not match:
        raise ValueError(f'leaf without PIC {node.name}: {src}')
    pic = match.group(1).upper()
    if re.search(r'[^9XANZVS()0-9]', pic):
        raise ValueError(f'unsupported PIC {node.name}: {pic}')
    parts = _PIC_ELEMENT.findall(pic)
    if not parts:
        raise ValueError(f'unrecognised PIC {node.name}: {pic}')
    digit_count = sum(int(n) if n else 1 for _, n in parts)
    kind = {ch for ch, _ in parts}
    if 'COMP-3' in src or 'PACKED-DECIMAL' in src:
        if kind != {'9'}:
            raise ValueError(f'packed field is not numeric {node.name}')
        return (digit_count + 2) // 2
    if re.search(r'\bCOMP(?:UTATIONAL)?(?:-[0-9]+)?\b', src):
        raise ValueError(f'unsupported binary storage {node.name}: {src}')
    return digit_count


def _field_bytes(node: Field) -> int:
    src = node.source.upper()
    if re.search(r'\bOCCURS\b', src) and (
        not _OCCURS.search(src) or re.search(r'\b(?:DEPENDING|TO\s+\d+|UNTIL)\b', src)
    ):
        raise ValueError(f'unsupported variable or malformed OCCURS {node.name}: {src}')
    repeat = int(_OCCURS.search(src).group(1)) if _OCCURS.search(src) else 1
    if repeat < 1 or repeat > 100000:
        raise ValueError(f'unsafe OCCURS count for {node.name}: {repeat}')
    if not node.children:
        return repeat * _picture_bytes(node)
    if _PIC.search(node.source):
        raise ValueError(f'group has PIC and children: {node.name}')
    offsets: dict[str, tuple[int, int]] = {}
    position = 0
    for child in node.children:
        child_size = _field_bytes(child)
        redefine = _REDEF.search(child.source)
        if redefine:
            target = redefine.group(1).upper()
            if target not in offsets:
                raise ValueError(f'{child.name} REDEFINES unknown preceding sibling {target}')
            offset, _ = offsets[target]
            position = max(position, offset + child_size)
        else:
            offset = position
            position += child_size
        if child.name != 'FILLER':
            if child.name in offsets:
                raise ValueError(f'nonunique data name {child.name} at same level')
            offsets[child.name] = (offset, child_size)
    return repeat * position


def group_byte_length(text: str, group_name: str) -> int:
    return _field_bytes(extract_group(text, group_name))


def child_byte_lengths(text: str, group_name: str) -> dict[str, int]:
    root = extract_group(text, group_name)
    return {ch.name: _field_bytes(ch) for ch in root.children if ch.name != 'FILLER'}
