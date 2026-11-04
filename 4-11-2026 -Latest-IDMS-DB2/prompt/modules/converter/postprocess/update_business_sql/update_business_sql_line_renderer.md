# `converter/postprocess/update_business_sql/update_business_sql_line_renderer.py`

Source: [converter/postprocess/update_business_sql/update_business_sql_line_renderer.py](../../../../../converter/postprocess/update_business_sql/update_business_sql_line_renderer.py) | 94 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `55aa07fb53a01017ccf0ecdda5140bc6e3acb7e57b5686d0afdf06489424b343`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from rules.update_business_sql_rules import ACTIVE_INDICATOR, UPDATE_SQL_AREA_B_INDENT, UPDATE_SQL_BODY_END_COLUMN, UPDATE_SQL_BODY_START_COLUMN, COMMENT_INDICATORS, FIXED_BODY_WIDTH, UPDATE_SQL_FULL_LINE_WIDTH, UPDATE_SQL_INDICATOR_COLUMN, UPDATE_SQL_RIGHT_SEQUENCE_WIDTH, UPDATE_SQL_SEQUENCE_AREA_WIDTH, UPDATE_SQL_TOTAL_LINE_WIDTH
```

## Local dependency notes

- [rules/update_business_sql_rules.py](../../../rules/update_business_sql_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_business_sql_standardizer.py](../update_business_sql_standardizer.md)

## Symbol contracts and control points

### `UpdateBusinessSqlLineRenderer` - L18-L94

```python
class UpdateBusinessSqlLineRenderer()
```

Fixed-format line rendering + logical-line extraction.

### `UpdateBusinessSqlLineRenderer._active_line_like` - L25-L30

```python
_active_line_like(self, *, reference_line: str, body: str) -> str
```

Observed calls (lexical order): `self._line_like`.

### `UpdateBusinessSqlLineRenderer._line_like` - L32-L63

```python
_line_like(self, *, reference_line: str, body: str, force_indicator: str | None=None) -> str
```

Observed calls (lexical order): `str`, `str(reference_line or '').rstrip`, `str(body or '').strip`, `len`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit`, `self._indicator_for`, `body_area[:FIXED_BODY_WIDTH].ljust`, `body_area[:FIXED_BODY_WIDTH].rstrip`.

Control points:

- L42: `if len(text) >= UPDATE_SQL_FULL_LINE_WIDTH and text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit()`
- L57: `if len(text) > UPDATE_SQL_SEQUENCE_AREA_WIDTH and text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit()`

### `UpdateBusinessSqlLineRenderer._indicator_for` - L65-L68

```python
_indicator_for(self, text: str, force_indicator: str | None) -> str
```

Observed calls (lexical order): `len`.

Control points:

- L66: `if force_indicator is not None`

### `UpdateBusinessSqlLineRenderer._is_comment_line` - L70-L77

```python
_is_comment_line(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit`, `text.strip`, `any`, `stripped.startswith`.

Control points:

- L73: `if len(text) >= UPDATE_SQL_INDICATOR_COLUMN and text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit()`

### `UpdateBusinessSqlLineRenderer._logical` - L79-L94

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip`, `text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit`, `text[UPDATE_SQL_BODY_START_COLUMN:UPDATE_SQL_BODY_END_COLUMN].strip`, `body[-UPDATE_SQL_RIGHT_SEQUENCE_WIDTH:].strip`, `body[-UPDATE_SQL_RIGHT_SEQUENCE_WIDTH:].strip().isdigit`, `body.strip`, `text.strip`.

Control points:

- L82: `if len(text) >= UPDATE_SQL_FULL_LINE_WIDTH and text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit()`
- L85: `if len(text) > UPDATE_SQL_SEQUENCE_AREA_WIDTH and text[:UPDATE_SQL_SEQUENCE_AREA_WIDTH].strip().isdigit()`
- L87: `if len(body) >= UPDATE_SQL_RIGHT_SEQUENCE_WIDTH and body[-UPDATE_SQL_RIGHT_SEQUENCE_WIDTH:].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
