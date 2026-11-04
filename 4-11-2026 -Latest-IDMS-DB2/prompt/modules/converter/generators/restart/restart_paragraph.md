# `converter/generators/restart/restart_paragraph.py`

Source: [converter/generators/restart/restart_paragraph.py](../../../../../converter/generators/restart/restart_paragraph.py) | 50 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `4fcf1cf78d4a50299399eb9a591dde7ee0a89fbded74ad96d94fff9394033e9d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The value object every restart builder returns.

## Module-level bindings

`__all__` (L50)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.restart_sql_templates import PARAGRAPH_HEADER
```

## Local dependency notes

- [rules/restart_sql_templates.py](../../../rules/restart_sql_templates.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/restart/read_paragraph_builder.py](read_paragraph_builder.md)
- [converter/generators/restart/restart_flow_builder.py](restart_flow_builder.md)
- [tests/restart/test_m5_flow_builder.py](../../../tests/restart/test_m5_flow_builder.md)

## Symbol contracts and control points

### `RestartParagraph` - L33-L47

```python
class RestartParagraph()
```

One generated paragraph, ready for the geometry renderer.

Declared class/data-model fields:

```python
role: str
name: str
debug_trace: str
body: tuple[str, ...]
```

### `RestartParagraph.lines` - L41-L43

```python
lines(self) -> tuple[str, ...]
```

Header plus body. The trace carries its own indicator.

Observed calls (lexical order): `PARAGRAPH_HEADER.format`.

### `RestartParagraph.executable` - L45-L47

```python
executable(self) -> tuple[str, ...]
```

Body lines with blanks removed and indent stripped.

Observed calls (lexical order): `line.strip`, `tuple`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
