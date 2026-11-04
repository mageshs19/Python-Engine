# `converter/services/cursor_sql_block_scanner.py`

Source: [converter/services/cursor_sql_block_scanner.py](../../../../converter/services/cursor_sql_block_scanner.py) | 92 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1cd1dc5a255def1c32c320305a00768470253b3a96d7c39fa44243f759295fde`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.final_feedback_fix_patterns import DECLARE_CURSOR_PATTERN, END_EXEC_PATTERN, FETCH_CURSOR_PATTERN
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cursor_select_minimizer_service.py](cursor_select_minimizer_service.md)

## Symbol contracts and control points

### `CursorSqlBlockScanner` - L13-L92

```python
class CursorSqlBlockScanner()
```

Finds DECLARE CURSOR and FETCH cursor EXEC SQL blocks.

### `CursorSqlBlockScanner.__init__` - L20-L24

```python
__init__(self, fixed_format: FixedFormatLineService) -> None
```

### `CursorSqlBlockScanner.find_declare_blocks` - L26-L58

```python
find_declare_blocks(self, lines: list[str]) -> list[tuple[str, int, int]]
```

Observed calls (lexical order): `enumerate`, `self.fixed_format.logical`, `logical.upper`, `logical.upper().startswith`, `DECLARE_CURSOR_PATTERN.search`, `match.group`, `match.group('cursor').upper`, `END_EXEC_PATTERN.search`, `blocks.append`.

Control points:

- L35: `for (index, line) in enumerate(lines)`
- L38: `if logical.upper().startswith('EXEC SQL')`
- L44: `if in_exec_sql and (not cursor)`
- L47: `if match`
- L50: `if in_exec_sql and END_EXEC_PATTERN.search(logical)`
- L51: `if cursor`

### `CursorSqlBlockScanner.find_fetch_blocks` - L60-L92

```python
find_fetch_blocks(self, lines: list[str]) -> list[tuple[str, int, int]]
```

Observed calls (lexical order): `enumerate`, `self.fixed_format.logical`, `logical.upper`, `logical.upper().startswith`, `FETCH_CURSOR_PATTERN.search`, `match.group`, `match.group('cursor').upper`, `END_EXEC_PATTERN.search`, `blocks.append`.

Control points:

- L69: `for (index, line) in enumerate(lines)`
- L72: `if logical.upper().startswith('EXEC SQL')`
- L78: `if in_exec_sql and (not cursor)`
- L81: `if match`
- L84: `if in_exec_sql and END_EXEC_PATTERN.search(logical)`
- L85: `if cursor`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
