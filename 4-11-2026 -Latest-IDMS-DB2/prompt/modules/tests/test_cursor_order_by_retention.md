# `tests/test_cursor_order_by_retention.py`

Source: [tests/test_cursor_order_by_retention.py](../../../tests/test_cursor_order_by_retention.py) | 227 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `2f314bca341c84750e21f47ee8556d64050bad20266c223f9cb4d8be0fa2ad9e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> ORDER BY must survive on every cursor.

## Module-level bindings

`CURSOR` (L45), `TABLE` (L46), `RECORD` (L47), `ORDER_COLUMN` (L48), `PREDICATE` (L49)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.cursor_order_cleanup_composer import CursorOrderCleanupComposer
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from rules.cursor_declaration_rules import CHILD_CURSOR_KEEPS_ORDER_BY, ENFORCE_ORDER_BY_RETENTION, PARENT_CURSOR_KEEPS_ORDER_BY
from rules.cursor_order_cleanup_rules import ENFORCE_PARENT_CURSOR_ORDER_BY_CLEANUP
```

## Local dependency notes

- [converter/composers/cursor_order_cleanup_composer.py](../converter/composers/cursor_order_cleanup_composer.md)
- [converter/generators/db2_infrastructure/cursor_declare_builder.py](../converter/generators/db2_infrastructure/cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](../converter/generators/db2_infrastructure/cursor_spec.md)
- [rules/cursor_declaration_rules.py](../rules/cursor_declaration_rules.md)
- [rules/cursor_order_cleanup_rules.py](../rules/cursor_order_cleanup_rules.md)

## Symbol contracts and control points

### `_LineUtils` - L55-L70

```python
class _LineUtils()
```

Minimal stand-in for the infrastructure line utils.

### `_LineUtils.and_lines` - L59-L63

```python
and_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `_LineUtils.comma_lines` - L66-L70

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `_bodies` - L73-L75

```python
_bodies(lines: list[str]) -> list[str]
```

Non-blank lines, trimmed. Indentation is not under test here.

Observed calls (lexical order): `line.strip`.

### `_clause_index` - L78-L82

```python
_clause_index(bodies: list[str], token: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`.

Control points:

- L79: `for (index, body) in enumerate(bodies)`
- L80: `if body.upper().startswith(token)`

### `_has_clause` - L85-L86

```python
_has_clause(bodies: list[str], token: str) -> bool
```

Observed calls (lexical order): `_clause_index`.

### `_spec` - L89-L105

```python
_spec(where=None, order_by=None, order: int=0) -> CursorSpec
```

A spec dict exactly as CursorSpecBuilder emits it, then read.

Observed calls (lexical order): `CursorSpec.read`, `list`.

### `declares` - L109-L110

```python
declares() -> CursorDeclareBuilder
```

Observed calls (lexical order): `CursorDeclareBuilder`, `_LineUtils`.

### `test_retention_is_the_site_standard` - L116-L119

```python
test_retention_is_the_site_standard()
```

### `test_the_cleanup_pass_is_disabled` - L122-L123

```python
test_the_cleanup_pass_is_disabled()
```

### `test_a_root_cursor_keeps_order_by` - L129-L134

```python
test_a_root_cursor_keeps_order_by(declares)
```

The manual reference orders its root cursor.

Observed calls (lexical order): `_bodies`, `_spec`, `declares.build`, `_has_clause`, `any`.

### `test_a_child_cursor_keeps_order_by` - L137-L142

```python
test_a_child_cursor_keeps_order_by(declares)
```

Observed calls (lexical order): `_bodies`, `_spec`, `declares.build`, `_has_clause`.

### `test_clause_order_is_unchanged` - L145-L157

```python
test_clause_order_is_unchanged(declares)
```

SELECT, FROM, WHERE, ORDER BY, FOR READ ONLY, QUERYNO.

Observed calls (lexical order): `_bodies`, `_spec`, `declares.build`, `_clause_index`, `bodies[-2].upper`, `bodies[-2].upper().startswith`, `bodies[-1].upper`, `bodies[-1].upper().startswith`.

### `test_no_order_by_columns_is_reported_not_silent` - L160-L163

```python
test_no_order_by_columns_is_reported_not_silent(declares)
```

Observed calls (lexical order): `_spec`, `declares.build`, `any`.

### `test_a_kept_order_by_is_reported` - L166-L169

```python
test_a_kept_order_by_is_reported(declares)
```

Observed calls (lexical order): `_spec`, `declares.build`, `any`.

### `test_order_by_is_never_removed` - L172-L175

```python
test_order_by_is_never_removed(declares)
```

Observed calls (lexical order): `_spec`, `declares.build`, `any`.

### `test_a_cursor_without_order_by_renders_valid_sql` - L178-L184

```python
test_a_cursor_without_order_by_renders_valid_sql(declares)
```

No ORDER BY columns must not break the clause sequence.

Observed calls (lexical order): `_bodies`, `_spec`, `declares.build`, `_has_clause`, `bodies[-1].upper`, `bodies[-1].upper().startswith`.

### `_declare_text` - L190-L203

```python
_declare_text() -> str
```

Observed calls (lexical order): `'\n'.join`.

### `test_the_composer_is_a_no_op` - L206-L209

```python
test_the_composer_is_a_no_op()
```

Observed calls (lexical order): `_declare_text`, `CursorOrderCleanupComposer`, `CursorOrderCleanupComposer().compose`.

### `test_the_composer_reports_that_it_is_disabled` - L212-L216

```python
test_the_composer_reports_that_it_is_disabled()
```

Observed calls (lexical order): `CursorOrderCleanupComposer`, `_declare_text`, `composer.compose`, `any`.

### `test_the_composer_never_strips_order_by` - L219-L223

```python
test_the_composer_never_strips_order_by()
```

Observed calls (lexical order): `CursorOrderCleanupComposer`, `CursorOrderCleanupComposer().compose`, `_declare_text`.

### `test_empty_text_is_safe` - L226-L227

```python
test_empty_text_is_safe()
```

Observed calls (lexical order): `CursorOrderCleanupComposer`, `CursorOrderCleanupComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
