# `converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_diagnostics.py) | 58 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `e935e0e2a6b28a29d2aa3f7ae46456d680d64df50919fdee648b5d90e4b34910`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Collects the declaration decisions of one program.

## Module-level bindings

`__all__` (L58)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_rules import DECLARATION_MESSAGES
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](../../cursor_declaration/cursor_declaration_generator.md)
- [converter/generators/db2_infrastructure/cursor_declare/cursor_declare_builder.py](cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](declare_column_ownership.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](declare_order_by_planner.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_refusal.py](declare_refusal.md)

## Symbol contracts and control points

### `DeclareDiagnostics` - L15-L55

```python
class DeclareDiagnostics()
```

One message list, one render path.

### `DeclareDiagnostics.__init__` - L18-L19

```python
__init__(self) -> None
```

### `DeclareDiagnostics.reset` - L21-L28

```python
reset(self) -> None
```

Drop the previous program's messages.

### `DeclareDiagnostics.log` - L30-L34

```python
log(self, key: str, **fields) -> None
```

Render and record one catalogued diagnostic.

Observed calls (lexical order): `self.render`, `self.messages.append`.

Control points:

- L33: `if text`

### `DeclareDiagnostics.add` - L36-L39

```python
add(self, text: str) -> None
```

Record an already-rendered message.

Observed calls (lexical order): `self.messages.append`.

Control points:

- L38: `if text`

### `DeclareDiagnostics.render` - L42-L55

```python
render(key: str, **fields) -> str
```

One catalogued diagnostic, or "".

Observed calls (lexical order): `DECLARATION_MESSAGES.get`, `template.format`.

Control points:

- L50: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
