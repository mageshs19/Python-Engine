# `converter/services/cursor_select_column_parser.py`

Source: [converter/services/cursor_select_column_parser.py](../../../../converter/services/cursor_select_column_parser.py) | 135 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `2cd54c8bed08ba0b8ba20e752b9a9982a3c5cc53e9fbb8c28ccd3e36b557da35`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.final_feedback_fix_patterns import ASC_DESC_PATTERN, END_EXEC_PATTERN, FOR_READ_ONLY_PATTERN, FROM_PATTERN, ORDER_BY_PATTERN, SELECT_ITEM_PATTERN, SELECT_KEYWORD_PATTERN, SQL_NAME_TOKEN_PATTERN
from rules.cursor_select_minimizer_rules import SQL_NON_COLUMN_KEYWORDS
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](fixed_format_line_service.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cursor_select_minimizer_rules.py](../../rules/cursor_select_minimizer_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/services/cursor_select_fetch_rewriter.py](cursor_select_fetch_rewriter.md)
- [converter/services/cursor_select_minimizer_service.py](cursor_select_minimizer_service.md)

## Symbol contracts and control points

### `CursorSelectColumnParser` - L19-L135

```python
class CursorSelectColumnParser()
```

Parses SELECT columns and ORDER BY columns from a DECLARE CURSOR block.

### `CursorSelectColumnParser.__init__` - L26-L30

```python
__init__(self, fixed_format: FixedFormatLineService) -> None
```

### `CursorSelectColumnParser.select_columns` - L32-L55

```python
select_columns(self, block: list[str]) -> list[str]
```

Observed calls (lexical order): `self.fixed_format.logical`, `SELECT_KEYWORD_PATTERN.match`, `FROM_PATTERN.search`, `self.select_column_from_logical`, `columns.append`.

Control points:

- L39: `for line in block`
- L42: `if SELECT_KEYWORD_PATTERN.match(logical)`
- L46: `if in_select and FROM_PATTERN.search(logical)`
- L49: `if in_select`
- L52: `if column`

### `CursorSelectColumnParser.select_column_from_logical` - L57-L79

```python
select_column_from_logical(self, logical: str) -> str
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `self.is_sql_non_column_keyword`, `SELECT_ITEM_PATTERN.match`, `match.group`, `match.group('column').upper`.

Control points:

- L63: `if not text`
- L66: `if self.is_sql_non_column_keyword(text)`
- L71: `if not match`
- L76: `if self.is_sql_non_column_keyword(column)`

### `CursorSelectColumnParser.order_by_columns` - L81-L106

```python
order_by_columns(self, block: list[str]) -> list[str]
```

Observed calls (lexical order): `self.fixed_format.logical`, `ORDER_BY_PATTERN.search`, `ORDER_BY_PATTERN.sub`, `ORDER_BY_PATTERN.sub('', logical).strip`, `columns.extend`, `self.parse_order_by_columns`, `END_EXEC_PATTERN.search`, `FOR_READ_ONLY_PATTERN.search`.

Control points:

- L88: `for line in block`
- L91: `if ORDER_BY_PATTERN.search(logical)`
- L95: `if remainder`
- L100: `if in_order_by`
- L101: `if FOR_READ_ONLY_PATTERN.search(logical) or END_EXEC_PATTERN.search(logical)`

### `CursorSelectColumnParser.parse_order_by_columns` - L108-L122

```python
parse_order_by_columns(self, text: str) -> list[str]
```

Observed calls (lexical order): `str`, `str(text or '').split`, `item.strip`, `ASC_DESC_PATTERN.sub`, `ASC_DESC_PATTERN.sub('', token).strip`, `token.strip`, `SQL_NAME_TOKEN_PATTERN.match`, `columns.append`, `token.upper`.

Control points:

- L114: `for item in str(text or '').split(',')`
- L119: `if SQL_NAME_TOKEN_PATTERN.match(token)`

### `CursorSelectColumnParser.is_sql_non_column_keyword` - L124-L129

```python
is_sql_non_column_keyword(self, value: str) -> bool
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().lstrip`, `str(value or '').strip().upper().lstrip(',').strip`.

### `CursorSelectColumnParser.normalize_name` - L131-L135

```python
normalize_name(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `str(value or '').strip().upper().replace`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
