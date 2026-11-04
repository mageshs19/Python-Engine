"""Conservative per-WRITE fixed-record field-population audit.

The compiler accepts a correctly sized fixed record even when conversion has
lost a mapping MOVE. The output length audit cannot detect that data loss.

This audit validates that every *non-FILLER numeric elementary field* in a
resolvable WRITE FROM group is populated before the WRITE in the same
paragraph. A MOVE to a containing group counts; REDEFINES do not add
independent bytes. In ambiguous/unparsed cases the result is UNVERIFIED,
never inferred success. No program, field or member names are embedded.

This is a necessary static data-flow check, not control-flow proof: SQL row
semantics and branch-sensitive definite assignment require runtime parity.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass

from .cobol_storage_layout import Field, extract_group
from .record_write_contract import _code, _mask_quoted_literals

_PARA = re.compile(r'^([A-Z][A-Z0-9-]*)\.$', re.I)
_WRITE = re.compile(r'\bWRITE\s+([A-Z][A-Z0-9-]*)(?:\s+FROM\s+([A-Z][A-Z0-9-]*))?\b', re.I)
_DEST = re.compile(r'\bTO\s+([A-Z][A-Z0-9-]*)(?:\s+(?:OF|IN)\s+([A-Z][A-Z0-9-]*))?', re.I)
_INIT = re.compile(r'\bINITIALIZE\s+([A-Z][A-Z0-9-]*)\b', re.I)
_MOVE = re.compile(r'\bMOVE\b', re.I)
_VERB = re.compile(r'\b(?:MOVE|ADD|SUBTRACT|MULTIPLY|DIVIDE|COMPUTE|IF|ELSE|END-IF|EVALUATE|WHEN|END-EVALUATE|PERFORM|WRITE|READ|OPEN|CLOSE|DISPLAY|SET|INITIALIZE|EXEC|END-EXEC|CONTINUE|EXIT|GOBACK|STOP|CALL)\b', re.I)


@dataclass(frozen=True)
class PopulationFinding:
    level: str  # FAIL, UNVERIFIED
    buffer: str
    field: str
    reason: str


def _leaves(root: Field) -> list[tuple[Field, tuple[str, ...]]]:
    found = []
    def walk(node: Field, ancestors: tuple[str, ...]):
        if node.name == 'FILLER' or re.search(r'\bREDEFINES\b', node.source, re.I):
            return
        names = (node.name, *ancestors)
        if node.children:
            for c in node.children:
                walk(c, names)
        elif re.search(r'\bPIC(?:TURE)?\s+(?:IS\s+)?S?9', node.source, re.I):
            found.append((node, names))
    walk(root, ())
    return found


def _paragraphs(lines: list[str]) -> list[tuple[str, str]]:
    """Return paragraph body with its label; fixed-format sequence excluded."""
    procedure = False
    name = ''
    body = []
    result = []
    for line in lines:
        code = _code(line)
        if re.match(r'^PROCEDURE\s+DIVISION\b', code, re.I):
            procedure = True
            continue
        if not procedure or not code:
            continue
        new = _PARA.fullmatch(code)
        if new:
            if name:
                result.append((name, ' '.join(body)))
            name, body = new.group(1).upper(), []
        else:
            body.append(code)
    if name:
        result.append((name, ' '.join(body)))
    return result


def _written_targets_before(body: str, write_pos: int) -> tuple[set[tuple[str, str | None]], set[str]]:
    """Capture simple MOVE targets and INITIALIZE groups without guessing receivers.

    A MOVE whose receiver is not safely parseable cannot prove coverage.
    Source/data names are never inferred from output paragraph naming.
    """
    earlier = _mask_quoted_literals(body[:write_pos]).upper()
    # Separate each MOVE from the following COBOL verb. Destination clauses
    # can cross physical lines, which were already joined by _paragraphs.
    targets: set[tuple[str, str | None]] = set()
    for occurrence in _MOVE.finditer(earlier):
        next_verb = _VERB.search(earlier, occurrence.end())
        segment = earlier[occurrence.end():(next_verb.start() if next_verb else len(earlier))]
        if ' TO ' not in f' {segment} ':
            continue
        # Ignore MOVE CORRESPONDING since it requires a separate name-resolver.
        if re.match(r'\s+CORR(?:ESPONDING)?\b', segment):
            continue
        dest = _DEST.search(segment)
        if dest:
            receiver = dest.group(1)
            sender = segment[:dest.start()].strip()
            # A group MOVE of SPACES is a byte reset, not a valid numeric
            # initialization. Without this distinction, a record can pass
            # coverage with every packed decimal still holding X'40'.
            if re.fullmatch(r'SPACE[S]?', sender):
                continue
            targets.add((receiver, dest.group(2)))
    initialized = {m.group(1) for m in _INIT.finditer(earlier)}
    return targets, initialized


def _proven_caller_initializers(paragraphs: list[tuple[str, str]],
                                write_paragraph: str, buffer: str) -> bool:
    """Prove that every direct call initializes the buffer immediately before WRITE.

    This is intentionally narrow: any THRU/inline/conditional/indirect call,
    missing caller, or prior operation in the initializer prevents the proof.
    The proof never relies on program or paragraph naming conventions.
    """
    bodies = dict(paragraphs)
    call = re.compile(r'\bPERFORM\s+' + re.escape(write_paragraph) + r'\b', re.I)
    found = 0
    for caller, body in paragraphs:
        masked = _mask_quoted_literals(body).upper()
        for match in call.finditer(masked):
            found += 1
            # Only a plain PERFORM target. THRU/UNTIL call sites need full CFG.
            if not re.match(r'\s*\.', masked[match.end():]):
                return False
            preceding = masked[:match.start()].rstrip()
            previous = re.search(r'\bPERFORM\s+([A-Z][A-Z0-9-]*)\s*\.\s*$', preceding)
            if not previous or previous.group(1) not in bodies:
                return False
            init_name = previous.group(1)
            if init_name in {caller, write_paragraph}:
                return False
            initializer = _mask_quoted_literals(bodies[init_name]).upper()
            init = re.search(r'\bINITIALIZE\s+' + re.escape(buffer) + r'\b', initializer)
            if not init:
                return False
            before = initializer[:init.start()]
            # DISPLAY diagnostics may precede initialization; no branch, I/O,
            # or delegated subroutine may do so.
            if re.search(r'\b(?:IF|EVALUATE|WHEN|PERFORM|CALL|READ|WRITE|EXEC|EXIT|GO|GOBACK|STOP)\b', before):
                return False
    return found > 0


def audit_record_population(text: str) -> tuple[PopulationFinding, ...]:
    """Raise a release blocker for provably unpopulated numeric record fields.

    Only fully self-contained fixed-record buffer groups can be checked. The
    result is UNVERIFIED for unsupported layouts, not a guessed PASS.
    """
    findings: list[PopulationFinding] = []
    paragraphs = _paragraphs(text.splitlines())
    for paragraph_name, body in paragraphs:
        masked = _mask_quoted_literals(body)
        for write in _WRITE.finditer(masked):
            buffer = (write.group(2) or write.group(1)).upper()
            try:
                root = extract_group(text, buffer)
                leaves = _leaves(root)
            except ValueError as exc:
                findings.append(PopulationFinding('UNVERIFIED', buffer, '', f'cannot resolve output group: {exc}'))
                continue
            if not leaves:
                continue
            targets, initialized = _written_targets_before(body, write.start())
            if _proven_caller_initializers(paragraphs, paragraph_name, buffer):
                initialized.add(buffer)
            counts = Counter(f.name for f, _ in leaves)
            def assigned(chain: tuple[str, ...]) -> tuple[bool, bool]:
                ambiguous = False
                for at, name in enumerate(chain):
                    for receiver, qualifier in targets:
                        if receiver != name:
                            continue
                        if qualifier is not None:
                            # An OF/IN qualifier must refer to the target's
                            # ancestor, not some other equally named item.
                            if qualifier in chain[at + 1:]:
                                return True, False
                            continue
                        if counts[name] > 1:
                            ambiguous = True
                        else:
                            return True, False
                return False, ambiguous
            # Group INITIALIZE establishes valid numeric representations;
            # MOVE SPACES deliberately does not.
            for field, chain in leaves:
                if any(ancestor in initialized for ancestor in chain):
                    continue
                proven, ambiguous = assigned(chain)
                if not proven:
                    findings.append(PopulationFinding(
                        'UNVERIFIED' if ambiguous else 'FAIL', buffer, field.name,
                        ('ambiguous unqualified MOVE target' if ambiguous else
                         'numeric field is not assigned in its WRITE paragraph')))
    return tuple(findings)
