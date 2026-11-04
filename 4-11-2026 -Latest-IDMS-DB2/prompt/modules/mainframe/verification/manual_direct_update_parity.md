# `mainframe/verification/manual_direct_update_parity.py`

Source: [mainframe/verification/manual_direct_update_parity.py](../../../../mainframe/verification/manual_direct_update_parity.py) | 169 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `fa227efe9d242c70fc2d6bb4941af10b28e38b4ae1bc231e9f53f0753316a993`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Narrow, source-proven manual-parity evidence for paired IDMS CALC/MODIFY.

## Module-level bindings

`_PAIR` (L23)

## Import declarations

```python
from __future__ import annotations
import re
from pathlib import Path
from converter.analyzers.program_flow.business_operation_parity_audit import OperationParityReview, _body, _read_source, _target_sql_blocks_with_following_context
from converter.parsers.cobol_parser import CobolParser
```

## Local dependency notes

- [converter/analyzers/program_flow/business_operation_parity_audit.py](../../converter/analyzers/program_flow/business_operation_parity_audit.md)
- [converter/parsers/cobol_parser.py](../../converter/parsers/cobol_parser.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_semantic_release_gate.py](../zowe_semantic_release_gate.md)
- [tests/test_manual_direct_update_parity.py](../../tests/test_manual_direct_update_parity.md)

## Symbol contracts and control points

### `_update_assignments` - L26-L52

```python
_update_assignments(sql: str) -> tuple[str, tuple, tuple] | None
```

Observed calls (lexical order): `re.sub`, `re.sub('\\s+', ' ', sql.upper()).strip`, `re.sub('\\s+', ' ', sql.upper()).strip().rstrip`, `sql.upper`, `re.fullmatch`, `match.groups`, `parse`, `table.split`.

Control points:

- L32: `if not match`
- L50: `if not set_items or not where_items`

### `_update_assignments.parse` - L36-L46

```python
parse(section: str, separator: str) -> tuple | None
```

Observed calls (lexical order): `re.split`, `_PAIR.fullmatch`, `part.strip`, `paired.group`, `result.append`, `len`, `set`, `sorted`, `tuple`.

Control points:

- L39: `for part in parts`
- L41: `if not paired`
- L44: `if len(set((item[0] for item in result))) != len(result)`

### `_sqlcode_actions` - L55-L97

```python
_sqlcode_actions(context: str) -> tuple[str, str] | None
```

Require an operation-local success/error branch with no hidden actions.

Observed calls (lexical order): `re.search`, `list`, `matched.group`, `re.finditer`, `len`, `m.group`, `m.group(1).upper`, `enumerate`, `branch.end`, `branches[index + 1].start`, `matched.group(1)[start:end].upper`, `code.splitlines`, `line.strip`, `line.strip().rstrip`, `line.startswith`, `re.fullmatch`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L58: `if not matched`
- L61: `if len(branches) != 2`
- L64: `if kinds not in ({'0', 'OTHER'}, {'ZERO', 'OTHER'})`
- L67: `for (index, branch) in enumerate(branches)`
- L74: `for line in code.splitlines()`
- L76: `if not line or line.startswith('DISPLAY')`
- L79: `if action`
- L83: `if action`
- Another 3 conditions/loops exist in this source span.

### `_source_has_unconditional_pair` - L100-L119

```python
_source_has_unconditional_pair(source_text: str, record: str) -> bool
```

Observed calls (lexical order): `_read_source`, `enumerate`, `' '.join`, `' '.join((code for line, code in executable if op.line <= line < following.line)).upper`, `re.search`, `re.escape`.

Control points:

- L102: `for (pos, op) in enumerate(operations[:-1])`
- L104: `if not (op.family == 'SELECT' and op.statement == f'OBTAIN CALC {record}' and (following.family == 'UPDATE') and (following.operand == record) and (op.paragraph == following.paragr...`
- L113: `if re.search('\\b(?:ON\\s+DB-REC-NOT-FOUND|ERROR-STATUS|DB-REC-NOT-FOUND|IF|EVALUATE|WHEN|EXEC|PERFORM|CALL|READ|WRITE|STORE|ERASE|EXIT)\\b', between)`
- L116: `if re.search(f'\\bMOVE\\b[^.]*?\\bOF\\s+{re.escape(record)}\\s+TO\\b', between)`

### `manually_confirmed_direct_updates` - L122-L169

```python
manually_confirmed_direct_updates(source_text: str, generated_text: str, manual_text: str, reviews: tuple[OperationParityReview, ...], mapped_tables: dict[str, set[str]]) -> tuple[set[str], tuple[OperationParityReview, ...]]
```

Return eligible record operands and reviews still requiring resolution.

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `set`, `getattr`, `_target_sql_blocks_with_following_context`, `sorted`, `_source_has_unconditional_pair`, `mapped_tables.get`, `len`, `_update_assignments`, `_sqlcode_actions`, `any`, `confirmed.add`, `tuple`.

Control points:

- L136: `if not generated_id or CobolParser().program_id(manual_text) != generated_id`
- L142: `for record in sorted(candidates)`
- L143: `if not _source_has_unconditional_pair(source_text, record)`
- L146: `if not tables`
- L152: `if len(gen) != 1 or len(ref) != 1`
- L154: `if _update_assignments(gen[0][0]) is None or _update_assignments(gen[0][0]) != _update_assignments(ref[0][0])`
- L157: `if gen_handler is None or gen_handler != ref_handler`
- L161: `if any((family in {'SELECT', 'DELETE', 'INSERT'} and table in tables for family, table, _sql, _context in manual_sql))`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
