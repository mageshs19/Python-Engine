# `review/engine/registry.py`

Source: [review/engine/registry.py](../../../../review/engine/registry.py) | 55 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `6d11afe4e8c7946f4d73aaf38a49f0c6e84958d62966b999c889b2dab9720e21`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Auto-discovers checks. Drop a module in review/checks to add one.

## Module-level bindings

`PACKAGE` (L16)

## Import declarations

```python
from __future__ import annotations
import importlib
import inspect
import pkgutil
from review.engine.check_base import Check
from review.standards.pipeline import CHECK_ORDER, DISABLED_CHECKS, ENABLED_CHECKS
```

## Local dependency notes

- [review/engine/check_base.py](check_base.md)
- [review/standards/pipeline.py](../standards/pipeline.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/engine/reviewer.py](reviewer.md)

## Symbol contracts and control points

### `_classes` - L19-L34

```python
_classes() -> list[type[Check]]
```

Observed calls (lexical order): `importlib.import_module`, `list`, `pkgutil.iter_modules`, `info.name.startswith`, `inspect.getmembers`, `issubclass`, `found.append`.

Control points:

- L22: `for info in pkgutil.iter_modules(list(package.__path__))`
- L23: `if info.name.startswith('_')`
- L26: `for (_, member) in inspect.getmembers(module, inspect.isclass)`
- L27: `if issubclass(member, Check) and member is not Check and (member.__module__ == module.__name__) and member.CHECK_ID`

### `_enabled` - L37-L40

```python
_enabled(check_id: str) -> bool
```

Control points:

- L38: `if check_id in DISABLED_CHECKS`

### `_key` - L43-L46

```python
_key(check: Check)
```

Observed calls (lexical order): `CHECK_ORDER.index`.

Control points:

- L44: `if CHECK_ORDER and check.CHECK_ID in CHECK_ORDER`

### `load_checks` - L49-L51

```python
load_checks() -> list[Check]
```

Observed calls (lexical order): `_classes`, `_enabled`, `c`, `sorted`, `unique.values`.

### `check_ids` - L54-L55

```python
check_ids() -> list[str]
```

Observed calls (lexical order): `load_checks`.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
