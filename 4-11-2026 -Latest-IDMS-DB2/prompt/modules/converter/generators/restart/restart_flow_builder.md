# `converter/generators/restart/restart_flow_builder.py`

Source: [converter/generators/restart/restart_flow_builder.py](../../../../../converter/generators/restart/restart_flow_builder.py) | 183 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `a6cfacfd3e14cc7f8419638049c2416a29f2639284f7ac11f1b8ab7f49708ace`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the five restart flow paragraphs.

## Module-level bindings

`FLOW_TEMPLATES` (L65), `SENTENCE_TERMINATOR` (L73), `__all__` (L183)

## Import declarations

```python
from __future__ import annotations
from converter.generators.restart.restart_config import RestartConfig
from converter.generators.restart.restart_paragraph import RestartParagraph
from rules.restart_sql_templates import DEBUG_TRACE
from rules.restart_standard_rules import ROLE_ABEND, ROLE_COMMIT, ROLE_CONTROL, ROLE_RESTART_FOUND, ROLE_WRITE_RESTART
from rules.restart_statement_templates import ABEND_TEMPLATE, COMMIT_TEMPLATE, CONTROL_TEMPLATE, RESTART_FOUND_TEMPLATE, WRITE_RESTART_TEMPLATE
```

## Local dependency notes

- [converter/generators/restart/restart_config.py](restart_config.md)
- [converter/generators/restart/restart_paragraph.py](restart_paragraph.md)
- [rules/restart_sql_templates.py](../../../rules/restart_sql_templates.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [tests/restart/test_m5_flow_builder.py](../../../tests/restart/test_m5_flow_builder.md)

## Symbol contracts and control points

### `RestartFlowBuilder` - L76-L180

```python
class RestartFlowBuilder()
```

Renders control / restart_found / write_restart / commit / abend.

### `RestartFlowBuilder.__init__` - L79-L81

```python
__init__(self, config: RestartConfig) -> None
```

### `RestartFlowBuilder.build_all` - L87-L101

```python
build_all(self) -> list[RestartParagraph]
```

Observed calls (lexical order): `self._usable`, `self.config.placeholders`, `self._paragraph`, `self.messages.append`, `len`.

Control points:

- L90: `if not self._usable()`

### `RestartFlowBuilder.build` - L103-L108

```python
build(self, role: str) -> RestartParagraph | None
```

One paragraph by role, or None when the config is unusable.

Observed calls (lexical order): `self.build_all`.

Control points:

- L105: `for candidate in self.build_all()`
- L106: `if candidate.role == role`

### `RestartFlowBuilder._usable` - L114-L127

```python
_usable(self) -> bool
```

Observed calls (lexical order): `self.config.is_usable`, `self.config.missing`, `self.messages.append`.

Control points:

- L115: `if self.config.is_usable()`
- L118: `for name in self.config.missing()`
- L122: `if self.config.retention_days <= 0`

### `RestartFlowBuilder._paragraph` - L133-L148

```python
_paragraph(self, role: str, template: tuple[str, ...], values: dict[str, object]) -> RestartParagraph
```

Observed calls (lexical order): `line.format`, `self._header_name`, `self._terminated`, `RestartParagraph`, `DEBUG_TRACE.format`, `tuple`.

### `RestartFlowBuilder._header_name` - L150-L159

```python
_header_name(self, header: str, role: str) -> str
```

The paragraph name the template rendered, minus its period.

Observed calls (lexical order): `header.strip`, `header.strip().rstrip`, `self.config.paragraph`, `self.messages.append`.

Control points:

- L154: `if name != expected`

### `RestartFlowBuilder._terminated` - L161-L180

```python
_terminated(self, body: list[str]) -> list[str]
```

Guarantee the paragraph closes its sentence.

Observed calls (lexical order): `enumerate`, `line.strip`, `body[last].rstrip`, `body[last].rstrip().endswith`, `list`, `updated.insert`, `self.messages.append`.

Control points:

- L168: `if not executable`
- L172: `if body[last].rstrip().endswith(SENTENCE_TERMINATOR)`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
