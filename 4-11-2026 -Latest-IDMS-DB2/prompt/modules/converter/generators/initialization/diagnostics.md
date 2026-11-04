# `converter/generators/initialization/diagnostics.py`

Source: [converter/generators/initialization/diagnostics.py](../../../../../converter/generators/initialization/diagnostics.py) | 36 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `1545bd9aa12ba84cae0424c604b07525af11254d51dec84be111ec3ff0e0bafe`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L36)

## Import declarations

```python
from __future__ import annotations
from typing import List
from rules.initialization_placement_rules import INITIALIZATION_PLACEMENT_MESSAGES
```

## Local dependency notes

- [rules/initialization_placement_rules.py](../../../rules/initialization_placement_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/enhancement/output_validator.py](../enhancement/output_validator.md)
- [converter/generators/initialization/__init__.py](__init__.md)
- [converter/generators/initialization/initialize_placer.py](initialize_placer.md)
- [converter/generators/initialization/legacy_paragraph_remover.py](legacy_paragraph_remover.md)
- [converter/generators/initialization/scope_initializer.py](scope_initializer.md)
- [converter/generators/timestamp/cs_program_declarator.py](../timestamp/cs_program_declarator.md)

## Symbol contracts and control points

### `InitializationDiagnostics` - L10-L33

```python
class InitializationDiagnostics()
```

### `InitializationDiagnostics.__init__` - L12-L13

```python
__init__(self) -> None
```

### `InitializationDiagnostics.reset` - L15-L16

```python
reset(self) -> None
```

### `InitializationDiagnostics.log` - L18-L25

```python
log(self, key: str, **values: object) -> None
```

Observed calls (lexical order): `INITIALIZATION_PLACEMENT_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L20: `if not template`

### `InitializationDiagnostics.extend` - L27-L30

```python
extend(self, other: 'InitializationDiagnostics') -> None
```

Observed calls (lexical order): `self.messages.extend`.

Control points:

- L28: `if other is None`

### `InitializationDiagnostics.all` - L32-L33

```python
all(self) -> List[str]
```

Observed calls (lexical order): `list`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
