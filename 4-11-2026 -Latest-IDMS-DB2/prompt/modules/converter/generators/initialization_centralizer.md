# `converter/generators/initialization_centralizer.py`

Source: [converter/generators/initialization_centralizer.py](../../../../converter/generators/initialization_centralizer.py) | 35 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `4f2a29ca54b759d209da9e8f865bb88f2b0cf64547033deb37245bd9d5085909`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L35)

## Import declarations

```python
from __future__ import annotations
from typing import List, Set
from converter.generators.initialization.scope_initializer import CursorScopedInitializer
```

## Local dependency notes

- [converter/generators/initialization/scope_initializer.py](initialization/scope_initializer.md)

## Symbol contracts and control points

### `InitializationCentralizer` - L10-L28

```python
class InitializationCentralizer()
```

### `InitializationCentralizer.__init__` - L12-L13

```python
__init__(self, program_text: str) -> None
```

Observed calls (lexical order): `CursorScopedInitializer`.

### `InitializationCentralizer.program_text` - L16-L17

```python
program_text(self) -> str
```

### `InitializationCentralizer.dclgen_groups` - L20-L21

```python
dclgen_groups(self) -> Set[str]
```

### `InitializationCentralizer.messages` - L24-L25

```python
messages(self) -> List[str]
```

### `InitializationCentralizer.process` - L27-L28

```python
process(self) -> str
```

Observed calls (lexical order): `self._delegate.process`.

### `centralize_initialization` - L31-L32

```python
centralize_initialization(program_text: str) -> str
```

Observed calls (lexical order): `InitializationCentralizer`, `InitializationCentralizer(program_text).process`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
