"""Reject unconverted DB2 character-to-packed group transfers.

An ordinary group MOVE is a byte copy, NOT a field-wise numeric conversion.
This independent audit never infers a serialization merely from a matching
length. A changed source/target representation requires a separate, explicit
migration contract. It does not rewrite COBOL or the mapping data.
"""
from __future__ import annotations

from bisect import bisect_right
from dataclasses import dataclass, field
import re
from typing import Iterable

from .cobol_storage_layout import group_byte_length

_DECL = re.compile(r'^(0[1-9]|[1-4]\d|66|77|88)\s+([A-Z][A-Z0-9-]*)\b(.*)$', re.I)
_NONDISPLAY = re.compile(r'\b(?:COMP(?:UTATIONAL)?(?:-[1-5])?|PACKED-DECIMAL|BINARY)\b', re.I)
_QUALIFIER = r'(?:\s+(?:OF|IN)\s+[A-Z][A-Z0-9-]*)*'
_MOVE = re.compile(
    r'\bMOVE\s+(?P<host>[A-Z][A-Z0-9-]*)\s+(?:OF|IN)\s+'
    r'(?P<group>DCL[A-Z0-9-]+)\s+TO\s+(?P<target>[A-Z][A-Z0-9-]*)'
    r'(?P<qualifiers>'+_QUALIFIER+r')(?=\s|\.|$)', re.I)
_CHAR_TYPE = re.compile(r'^(?:CHAR|CHARACTER)\s*\(\s*(\d+)\s*\)', re.I)


def _body(raw: str) -> str:
    if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace()):
        if raw[6] in '*/Dd':
            return ''
        raw = raw[7:72]
    if raw.lstrip().startswith(('*', '/')):
        return ''
    # Preserve literals for storage declarations; executable searches use a
    # separately masked version so messages never become MOVE statements.
    return raw.strip()


def _masked(text: str) -> str:
    pattern = r"'(?:''|[^'])*'|\"(?:\"\"|[^\"])*\"|\*>[^\n]*"
    return re.sub(pattern, lambda m: ''.join('\n' if c == '\n' else ' ' for c in m.group()), text)


@dataclass
class _Node:
    level: int
    name: str
    clause: str
    line: int
    parent: '_Node | None' = None
    children: list['_Node'] = field(default_factory=list)

    def descendants(self) -> Iterable['_Node']:
        for child in self.children:
            yield child
            yield from child.descendants()

    def ancestors(self) -> tuple[str, ...]:
        values = []
        parent = self.parent
        while parent is not None:
            values.append(parent.name)
            parent = parent.parent
        return tuple(values)


def _nodes(text: str) -> list[_Node]:
    nodes: list[_Node] = []
    stack: list[_Node] = []
    in_data = False
    in_sql = False
    for number, raw in enumerate(text.splitlines(), 1):
        body = _body(raw)
        if re.match(r'^DATA\s+DIVISION\b', body, re.I):
            in_data = True
        if re.match(r'^PROCEDURE\s+DIVISION\b', body, re.I):
            break
        if not in_data:
            continue
        if re.match(r'^EXEC\s+SQL\b', body, re.I):
            in_sql = True
        if in_sql:
            if re.search(r'\bEND-EXEC\b', body, re.I):
                in_sql = False
            continue
        if re.match(r'^[A-Z-]+\s+SECTION\b|^FD\s|^SD\s', body, re.I):
            stack = []
        match = _DECL.match(body)
        if not match:
            if stack and re.match(r'^(?:PIC(?:TURE)?|USAGE|COMP(?:UTATIONAL)?(?:-[1-5])?|'
                                  r'VALUE|SIGN|OCCURS|REDEFINES|SYNCHRONIZED)\b', body, re.I):
                stack[-1].clause += ' '+body
            continue
        level = int(match.group(1))
        if level in {66, 88}:
            continue
        while stack and (stack[-1].level >= level or level in {1, 77}):
            stack.pop()
        node = _Node(level, match.group(2).upper(), match.group(3).strip(), number,
                     stack[-1] if stack else None)
        if node.parent:
            node.parent.children.append(node)
        nodes.append(node)
        stack.append(node)
    return nodes


def _node_size(node: _Node) -> int:
    # Reuse the independent storage calculator with a neutral level-01 root.
    body = [f'01 {node.name} {node.clause}']
    body += [f'{n.level:02d} {n.name} {n.clause}' for n in node.descendants()]
    return group_byte_length('\n'.join(body), node.name)


def _column_key(column) -> tuple[str, str]:
    return ('DCL'+str(column.table_name).strip().upper().replace('_','-'),
            str(column.cobol_host_name).strip().upper().replace('_','-'))


@dataclass(frozen=True)
class GroupRepresentationFinding:
    code: str
    line: int
    source: str
    target: str
    message: str


def audit_character_group_moves(text: str, columns: Iterable) -> tuple[GroupRepresentationFinding, ...]:
    """Detect scalar CHAR hosts copied without conversion to packed groups.

    Unknown or ambiguous storage is reported, not treated as a successful proof.
    Elementary numeric receivers are deliberately excluded: those MOVEs perform
    a numeric conversion, unlike the group case.
    """
    by_host: dict[tuple[str, str], list] = {}
    for column in columns:
        by_host.setdefault(_column_key(column), []).append(column)
    nodes = _nodes(text)
    lines = [_body(line) for line in text.splitlines()]
    start = next((i for i,b in enumerate(lines) if re.match(r'^PROCEDURE\s+DIVISION\b',b,re.I)), len(lines))
    lines[:start] = ['']*start
    code = _masked('\n'.join(lines))
    offsets = [0]
    for match in re.finditer('\n', code):
        offsets.append(match.end())
    findings: list[GroupRepresentationFinding] = []
    for match in _MOVE.finditer(code):
        candidates = by_host.get((match.group('group').upper(),match.group('host').upper()), [])
        if not candidates:
            continue
        column = candidates[0]
        host_type = _CHAR_TYPE.match(str(column.db2_type).strip())
        if not host_type:
            continue
        target = match.group('target').upper()
        qualifiers = re.findall(r'\b(?:OF|IN)\s+([A-Z][A-Z0-9-]*)', match.group('qualifiers'), re.I)
        qualified = [n for n in nodes if n.name == target and
                     all(q.upper() in n.ancestors() for q in qualifiers)]
        line = bisect_right(offsets,match.start())
        source = match.group('host').upper()+' OF '+match.group('group').upper()
        if len(qualified) != 1:
            # Missing COPY content is a separate copybook readiness check.
            if len(qualified) > 1:
                findings.append(GroupRepresentationFinding('AMBIGUOUS-GROUP-TARGET',line,source,target,
                    'multiple data declarations match the receiving group'))
            continue
        node = qualified[0]
        if not node.children or not any(_NONDISPLAY.search(n.clause) for n in [node,*node.descendants()]):
            continue
        width = int(host_type.group(1))
        try:
            size = _node_size(node)
        except ValueError as exc:
            findings.append(GroupRepresentationFinding('UNVERIFIED-GROUP-REPRESENTATION',line,source,target,str(exc)))
            continue
        findings.append(GroupRepresentationFinding('UNCONVERTED-CHARACTER-GROUP',line,source,target,
            f'CHAR({width}) copied to a {size}-byte group containing packed/binary fields; '
            'group MOVE copies bytes without numeric conversion; an explicit encoding contract is required'))
    return tuple(findings)


def audit_target_character_widths(text: str, rows: Iterable, columns: Iterable) -> tuple[GroupRepresentationFinding, ...]:
    """Compare declared target CHAR widths, scoped to hosts used by this member.

    Base-table/view aliases must already have been resolved by the input adapter;
    IDMS storage width is not assumed equal to its DB2 target representation.
    """
    code = _masked('\n'.join(_body(ln) for ln in text.splitlines()))
    findings = []
    seen = set()
    for column in columns:
        target_type = _CHAR_TYPE.match(str(column.db2_type).strip())
        if not target_type:
            continue
        group, host = _column_key(column)
        # SQL INTO and COBOL moves both establish actual use of this host.
        if not (re.search(r'\b'+re.escape(host)+r'\b',code,re.I) or
                re.search(r'\b'+re.escape(str(column.column_name).upper())+r'\b',code,re.I)):
            continue
        for row in rows:
            if str(row.new_db2_record).strip().upper() != str(column.table_name).strip().upper():
                continue
            if str(row.new_db2_field_name).strip().upper() != str(column.column_name).strip().upper():
                continue
            sheet_type = _CHAR_TYPE.match(str(row.new_db2_data_type).strip())
            if not sheet_type or int(sheet_type.group(1)) == int(target_type.group(1)):
                continue
            identity=(group,host,int(sheet_type.group(1)),int(target_type.group(1)))
            if identity in seen:
                continue
            seen.add(identity)
            findings.append(GroupRepresentationFinding('MAPPING-DCLGEN-CHAR-CONFLICT',0,group+'.'+host,'',
                f'mapping target CHAR({sheet_type.group(1)}) conflicts with DCLGEN CHAR({target_type.group(1)}); '
                'do not infer serialization or truncate to resolve this conflict'))
    return tuple(findings)
