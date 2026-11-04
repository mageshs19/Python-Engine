# `converter/services/cursor_select_usage_guard.py`

Source: [converter/services/cursor_select_usage_guard.py](../../../../converter/services/cursor_select_usage_guard.py) | 68 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `199077234a84ccc3fde40e14d5c5ffedbec5dcd395a209fec7f0d9964f223369`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cursor_select_minimizer_service.py](cursor_select_minimizer_service.md)

## Symbol contracts and control points

### `CursorSelectUsageGuard` - L8-L68

```python
class CursorSelectUsageGuard()
```

Checks whether a candidate removable SELECT column is used outside its DECLARE CURSOR block and matching FETCH block.

### `CursorSelectUsageGuard.__init__` - L14-L18

```python
__init__(self, fixed_format: FixedFormatLineService) -> None
```

### `CursorSelectUsageGuard.has_non_order_usage` - L20-L49

```python
has_non_order_usage(self, *, lines: list[str], declare_range: tuple[int, int], fetch_blocks: list[tuple[str, int, int]], cursor: str, column: str) -> bool
```

Observed calls (lexical order): `column.replace`, `column.replace('_', '-').upper`, `column.upper`, `self.matching_fetch_range`, `enumerate`, `self.index_in_range`, `self.fixed_format.logical`, `self.fixed_format.logical(line).upper`.

Control points:

- L34: `for (index, line) in enumerate(lines)`
- L35: `if self.index_in_range(index, declare_range)`
- L38: `if fetch_range and self.index_in_range(index, fetch_range)`
- L43: `if column_upper in logical`
- L46: `if host_like in logical`

### `CursorSelectUsageGuard.matching_fetch_range` - L51-L60

```python
matching_fetch_range(self, fetch_blocks: list[tuple[str, int, int]], cursor: str) -> tuple[int, int] | None
```

Control points:

- L56: `for (fetch_cursor, start, end) in fetch_blocks`
- L57: `if fetch_cursor == cursor`

### `CursorSelectUsageGuard.index_in_range` - L62-L68

```python
index_in_range(self, index: int, value_range: tuple[int, int]) -> bool
```

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
