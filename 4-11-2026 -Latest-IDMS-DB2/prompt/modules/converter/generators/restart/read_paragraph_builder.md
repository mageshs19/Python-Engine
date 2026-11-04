# `converter/generators/restart/read_paragraph_builder.py`

Source: [converter/generators/restart/read_paragraph_builder.py](../../../../../converter/generators/restart/read_paragraph_builder.py) | 154 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `0551f36884096b2e2957fa9f49acd5ad3f30d3db4fb7f685680fbaac0f2a6c10`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the reader paragraph that feeds the checkpoint.

## Module-level bindings

`ROLE_READ` (L61), `PERIOD` (L62), `__all__` (L154)

## Import declarations

```python
from __future__ import annotations
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_paragraph import RestartParagraph
from rules.restart_sql_templates import DEBUG_TRACE
from rules.restart_statement_templates import READ_PARAGRAPH_TEMPLATE
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](restart_config.md)
- [converter/generators/restart/restart_paragraph.py](restart_paragraph.md)
- [rules/restart_sql_templates.py](../../../rules/restart_sql_templates.md)
- [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [tests/restart/test_m8_read_paragraph.py](../../../tests/restart/test_m8_read_paragraph.md)

## Symbol contracts and control points

### `RestartReadParagraphBuilder` - L65-L151

```python
class RestartReadParagraphBuilder()
```

Renders the reader paragraph, and reports what a source one lacks.

### `RestartReadParagraphBuilder.__init__` - L68-L70

```python
__init__(self, config: RestartConfig) -> None
```

### `RestartReadParagraphBuilder.build` - L76-L96

```python
build(self) -> RestartParagraph | None
```

The reader paragraph, or None when the config is unusable.

Observed calls (lexical order): `self._usable`, `self.config.placeholders`, `line.format`, `rendered[0].strip`, `rendered[0].strip().rstrip`, `self.messages.append`, `RestartParagraph`, `DEBUG_TRACE.format`, `tuple`.

Control points:

- L80: `if not self._usable()`

### `RestartReadParagraphBuilder.required_statements` - L98-L106

```python
required_statements(self) -> tuple[str, ...]
```

The four statements a source reader must carry.

### `RestartReadParagraphBuilder.missing_statements` - L108-L115

```python
missing_statements(self, lines: list[str]) -> tuple[str, ...]
```

Which required statements a source reader does not carry.

Observed calls (lexical order): `' '.join`, `self._logical`, `tuple`, `self.required_statements`.

### `RestartReadParagraphBuilder.needs_rebuild` - L117-L124

```python
needs_rebuild(self, lines: list[str]) -> bool
```

True when the source reader is missing anything required.

Observed calls (lexical order): `self.missing_statements`, `self.messages.append`, `bool`.

Control points:

- L120: `for statement in missing`

### `RestartReadParagraphBuilder._usable` - L130-L143

```python
_usable(self) -> bool
```

Observed calls (lexical order): `self.config.is_usable`, `self.config.missing`, `self.messages.append`.

Control points:

- L131: `if self.config.is_usable()`
- L134: `for name in self.config.missing()`
- L138: `if self.config.retention_days <= 0`

### `RestartReadParagraphBuilder._logical` - L150-L151

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `' '.join`, `str`, `str(line or '').upper`, `str(line or '').upper().split`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
