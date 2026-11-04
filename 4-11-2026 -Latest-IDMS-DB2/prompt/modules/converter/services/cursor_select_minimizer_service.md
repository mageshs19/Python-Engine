# `converter/services/cursor_select_minimizer_service.py`

Source: [converter/services/cursor_select_minimizer_service.py](../../../../converter/services/cursor_select_minimizer_service.py) | 199 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `dda29bbb7d6a6dec79ca5df70df2aced5672e3aa2b08359e9dc07e2c55f2ede5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor SELECT minimizer service.

## Import declarations

```python
from __future__ import annotations
from converter.services.cursor_select_column_parser import CursorSelectColumnParser
from converter.services.cursor_select_fetch_rewriter import CursorSelectFetchRewriter
from converter.services.cursor_select_usage_guard import CursorSelectUsageGuard
from converter.services.cursor_sql_block_scanner import CursorSqlBlockScanner
from converter.services.fixed_format_line_service import FixedFormatLineService
from rules.final_feedback_fix_rules import ORDER_BY_COLUMNS_IN_SELECT_DEFAULT
```

## Local dependency notes

- [converter/services/cursor_select_column_parser.py](cursor_select_column_parser.md)
- [converter/services/cursor_select_fetch_rewriter.py](cursor_select_fetch_rewriter.md)
- [converter/services/cursor_select_usage_guard.py](cursor_select_usage_guard.md)
- [converter/services/cursor_sql_block_scanner.py](cursor_sql_block_scanner.md)
- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [rules/final_feedback_fix_rules.py](../../rules/final_feedback_fix_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/final_cobol_fix_composer.py](../composers/final_cobol_fix_composer.md)

## Symbol contracts and control points

### `CursorSelectMinimizerService` - L34-L199

```python
class CursorSelectMinimizerService()
```

Removes order-by-only columns from cursor SELECT/FETCH when safe.

### `CursorSelectMinimizerService.__init__` - L47-L61

```python
__init__(self, fixed_format: FixedFormatLineService | None=None, require_order_by_columns_in_select: bool=ORDER_BY_COLUMNS_IN_SELECT_DEFAULT) -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `CursorSqlBlockScanner`, `CursorSelectColumnParser`, `CursorSelectUsageGuard`, `CursorSelectFetchRewriter`.

### `CursorSelectMinimizerService.minimize` - L63-L102

```python
minimize(self, text: str) -> str
```

Observed calls (lexical order): `str`, `source.splitlines`, `self.block_scanner.find_declare_blocks`, `self.block_scanner.find_fetch_blocks`, `self._removal_positions_by_cursor`, `self._apply_select_removals`, `self._apply_fetch_removals`, `'\n'.join`.

Control points:

- L69: `if not source`
- L72: `if self.require_order_by_columns_in_select`
- L85: `if not removals_by_cursor`

### `CursorSelectMinimizerService._removal_positions_by_cursor` - L104-L145

```python
_removal_positions_by_cursor(self, *, lines: list[str], declare_blocks: list[tuple[str, int, int]], fetch_blocks: list[tuple[str, int, int]]) -> dict[str, set[int]]
```

Observed calls (lexical order): `self.column_parser.select_columns`, `self.column_parser.order_by_columns`, `self.column_parser.normalize_name`, `set`, `enumerate`, `self.usage_guard.has_non_order_usage`, `removable.add`.

Control points:

- L113: `for (cursor, start, end) in declare_blocks`
- L118: `if not select_columns or not order_columns`
- L127: `for (index, column) in enumerate(select_columns)`
- L128: `if self.column_parser.normalize_name(column) not in order_set`
- L131: `if self.usage_guard.has_non_order_usage(lines=lines, declare_range=(start, end), fetch_blocks=fetch_blocks, cursor=cursor, column=column)`
- L142: `if removable`

### `CursorSelectMinimizerService._apply_select_removals` - L147-L172

```python
_apply_select_removals(self, *, lines: list[str], declare_blocks: list[tuple[str, int, int]], removals_by_cursor: dict[str, set[int]]) -> list[str]
```

Observed calls (lexical order): `list`, `sorted`, `removals_by_cursor.get`, `self.rewriter.remove_select_positions`.

Control points:

- L156: `for (cursor, start, end) in sorted(declare_blocks, key=lambda item: item[1], reverse=True)`
- L163: `if not removable`

### `CursorSelectMinimizerService._apply_fetch_removals` - L174-L199

```python
_apply_fetch_removals(self, *, lines: list[str], fetch_blocks: list[tuple[str, int, int]], removals_by_cursor: dict[str, set[int]]) -> list[str]
```

Observed calls (lexical order): `list`, `sorted`, `removals_by_cursor.get`, `self.rewriter.remove_fetch_positions`.

Control points:

- L183: `for (cursor, start, end) in sorted(fetch_blocks, key=lambda item: item[1], reverse=True)`
- L190: `if not removable`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
