# `converter/generators/cursor_paragraph/cursor_error_branch.py`

Source: [converter/generators/cursor_paragraph/cursor_error_branch.py](../../../../../converter/generators/cursor_paragraph/cursor_error_branch.py) | 88 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `4d5b3d80e48cc41ba7fc62551b886922244867a0f3730a2fa9cf9076b4c7a89b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The WHEN OTHER branch of an EVALUATE SQLCODE block.

## Module-level bindings

`__all__` (L88)

## Import declarations

```python
from __future__ import annotations
from converter.generators.cursor_paragraph.cursor_key_diagnostics import KeyDiagnosticsBuilder
from converter.generators.cursor_paragraph.cursor_sql_location import SqlLocationBuilder
from rules.cursor_paragraph_rules import DISPLAY_ERROR_TEMPLATE, ENFORCE_SQL_LOCATION_IN_ERROR_BRANCH, IND_STATEMENT, IND_WHEN, IND_WHEN_BODY, LONE_PERIOD, PERFORM_TEMPLATE, TOKEN_END_EVALUATE, TOKEN_WHEN_OTHER
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](cursor_key_diagnostics.md)
- [converter/generators/cursor_paragraph/cursor_sql_location.py](cursor_sql_location.md)
- [rules/cursor_paragraph_rules.py](../../../rules/cursor_paragraph_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph_body_builder.md)

## Symbol contracts and control points

### `ErrorBranchBuilder` - L40-L85

```python
class ErrorBranchBuilder()
```

Renders WHEN OTHER through the closing period.

### `ErrorBranchBuilder.__init__` - L43-L49

```python
__init__(self, sql_location: SqlLocationBuilder | None=None, diagnostics: KeyDiagnosticsBuilder | None=None) -> None
```

Observed calls (lexical order): `SqlLocationBuilder`, `KeyDiagnosticsBuilder`.

### `ErrorBranchBuilder.build` - L51-L85

```python
build(self, error_text: str, sql_error_paragraph: str, paragraph_name: str='', where_conditions: list[str] | None=None, fetched_hosts: list[str] | None=None) -> list[str]
```

One WHEN OTHER branch.

Observed calls (lexical order): `lines.append`, `self.sql_location.body`, `DISPLAY_ERROR_TEMPLATE.format`, `lines.extend`, `self.diagnostics.lines_for_where`, `self.diagnostics.lines_for_hosts`, `PERFORM_TEMPLATE.format`.

Control points:

- L66: `if ENFORCE_SQL_LOCATION_IN_ERROR_BRANCH and paragraph_name`
- L73: `if where_conditions`
- L75: `if fetched_hosts`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
