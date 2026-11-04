# `converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py`

Source: [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](../../../../../converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py) | 259 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `c63d443811247b1d0f0c09aeb4063a28649b3e04ccc1935047cb50ccd7319ee9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the COBOL body of a cursor OPEN / FETCH / CLOSE paragraph.

## Module-level bindings

`__all__` (L259)

## Import declarations

```python
from __future__ import annotations
from converter.generators.cursor_paragraph.cursor_error_branch import ErrorBranchBuilder
from converter.generators.cursor_paragraph.cursor_fetch_paragraph import FetchParagraphBuilder
from converter.generators.cursor_paragraph.cursor_key_diagnostics import KeyDiagnosticsBuilder
from converter.generators.cursor_paragraph.cursor_sql_location import SqlLocationBuilder
from converter.generators.cursor_paragraph.cursor_statement_blocks import StatementBlockBuilder
from converter.generators.cursor_paragraph.join_key_label_resolver import JoinKeyLabelResolver
from rules.cursor_paragraph_rules import CLOSE_STATEMENT_TEMPLATE, CURSOR_NOT_EOC_SUFFIX, ERROR_CLOSE_TEMPLATE, ERROR_OPEN_TEMPLATE, IND_STATEMENT, IND_WHEN, IND_WHEN_BODY, OPEN_STATEMENT_TEMPLATE, SET_NOT_EOC_TEMPLATE, TOKEN_CONTINUE, TOKEN_EVALUATE_SQLCODE, TOKEN_WHEN_ZERO
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_error_branch.py](cursor_error_branch.md)
- [converter/generators/cursor_paragraph/cursor_fetch_paragraph.py](cursor_fetch_paragraph.md)
- [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](cursor_key_diagnostics.md)
- [converter/generators/cursor_paragraph/cursor_sql_location.py](cursor_sql_location.md)
- [converter/generators/cursor_paragraph/cursor_statement_blocks.py](cursor_statement_blocks.md)
- [converter/generators/cursor_paragraph/join_key_label_resolver.py](join_key_label_resolver.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/__init__.py](__init__.md)
- [converter/generators/cursor_paragraph_generator.py](../cursor_paragraph_generator.md)
- [tests/cursor_contract/conftest.py](../../../tests/cursor_contract/conftest.md)
- [tests/test_fetch_error_diagnostics.py](../../../tests/test_fetch_error_diagnostics.md)

## Symbol contracts and control points

### `CursorParagraphBodyBuilder` - L104-L256

```python
class CursorParagraphBodyBuilder()
```

Assembles one cursor paragraph from its collaborators.

### `CursorParagraphBodyBuilder.__init__` - L107-L130

```python
__init__(self, mapping_repository=None) -> None
```

Observed calls (lexical order): `SqlLocationBuilder`, `StatementBlockBuilder`, `JoinKeyLabelResolver`, `KeyDiagnosticsBuilder`, `ErrorBranchBuilder`, `FetchParagraphBuilder`.

### `CursorParagraphBodyBuilder.messages` - L133-L135

```python
messages(self) -> list[str]
```

Label-resolution diagnostics. The generator must drain this.

### `CursorParagraphBodyBuilder.reset` - L137-L139

```python
reset(self) -> None
```

Clear per-program diagnostics.

Observed calls (lexical order): `self.label_resolver.reset`.

### `CursorParagraphBodyBuilder.open_paragraph` - L144-L173

```python
open_paragraph(self, cursor_name: str, paragraph_name: str, sql_error_paragraph: str) -> list[str]
```

Observed calls (lexical order): `self.blocks.prologue`, `OPEN_STATEMENT_TEMPLATE.format`, `lines.extend`, `SET_NOT_EOC_TEMPLATE.format`, `self.error_branch.build`, `ERROR_OPEN_TEMPLATE.format`.

### `CursorParagraphBodyBuilder.fetch_paragraph` - L178-L197

```python
fetch_paragraph(self, cursor_name: str, paragraph_name: str, host_variables: list[str], sql_error_paragraph: str, where_conditions: list[str] | None=None, table_name: str='', is_parent_cursor: bool=False) -> list[str]
```

FETCH paragraph body. Signature retained for every caller.

Observed calls (lexical order): `self.fetch_builder.build`.

### `CursorParagraphBodyBuilder.close_paragraph` - L202-L227

```python
close_paragraph(self, cursor_name: str, paragraph_name: str, sql_error_paragraph: str) -> list[str]
```

Observed calls (lexical order): `self.blocks.prologue`, `CLOSE_STATEMENT_TEMPLATE.format`, `lines.extend`, `self.error_branch.build`, `ERROR_CLOSE_TEMPLATE.format`.

### `CursorParagraphBodyBuilder.sql_location_move` - L232-L233

```python
sql_location_move(self, paragraph_name: str) -> str
```

Observed calls (lexical order): `self.sql_location.statement`.

### `CursorParagraphBodyBuilder.sql_location_body` - L235-L236

```python
sql_location_body(self, paragraph_name: str) -> str
```

Observed calls (lexical order): `self.sql_location.body`.

### `CursorParagraphBodyBuilder.fetch_into_lines` - L238-L239

```python
fetch_into_lines(self, host_variables: list[str]) -> list[str]
```

Observed calls (lexical order): `self.blocks.into_lines`.

### `CursorParagraphBodyBuilder.sqlcode_error_tail` - L241-L256

```python
sqlcode_error_tail(self, error_text: str, sql_error_paragraph: str, paragraph_name: str='', diagnostic_hosts: list[str] | None=None, display_where_clause: bool=False) -> list[str]
```

Retained signature for existing callers and tests.

Observed calls (lexical order): `self.error_branch.build`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
