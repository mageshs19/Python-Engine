# `converter/composers/record_materialisation/record_sites.py`

Source: [converter/composers/record_materialisation/record_sites.py](../../../../../converter/composers/record_materialisation/record_sites.py) | 70 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `256986ade0bf4ab24871363d0a3445bf44632859eafd3b596b036257f26e5ebb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Where a whole-record MOVE and its target field live.

## Module-level bindings

`NOT_FOUND` (L14), `__all__` (L70)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_move_scanner.py](record_move_scanner.md)

## Symbol contracts and control points

### `MoveSite` - L18-L40

```python
class MoveSite()
```

One whole-record MOVE found in the PROCEDURE DIVISION.

Declared class/data-model fields:

```python
index: int = NOT_FOUND
record: str = ''
target: str = ''
```

### `MoveSite.is_found` - L30-L31

```python
is_found(self) -> bool
```

### `MoveSite.key` - L34-L40

```python
key(self) -> tuple[str, str]
```

Identity used to remember which moves have been visited.

### `TargetSite` - L44-L67

```python
class TargetSite()
```

The DATA DIVISION entry a whole-record MOVE writes into.

Declared class/data-model fields:

```python
index: int = NOT_FOUND
declared_bytes: int = 0
level: int = 0
```

### `TargetSite.is_found` - L56-L57

```python
is_found(self) -> bool
```

### `TargetSite.has_length` - L60-L67

```python
has_length(self) -> bool
```

False means the PICTURE could not be sized.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
