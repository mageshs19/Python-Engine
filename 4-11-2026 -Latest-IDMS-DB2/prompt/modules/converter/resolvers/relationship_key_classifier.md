# `converter/resolvers/relationship_key_classifier.py`

Source: [converter/resolvers/relationship_key_classifier.py](../../../../converter/resolvers/relationship_key_classifier.py) | 37 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `196dfc84cff4b4fe21ea75ca683940c894ab0642ea3b340f8ec89e7457242c75`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from typing import Any
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_key_column_resolver.py](relationship_key_column_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)

## Symbol contracts and control points

### `RelationshipKeyClassifier` - L8-L37

```python
class RelationshipKeyClassifier()
```

Classifies Sheet Mapping rows as primary-key or foreign-key rows.

### `RelationshipKeyClassifier.is_primary_key_row` - L13-L24

```python
is_primary_key_row(self, row: Any) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`.

### `RelationshipKeyClassifier.is_foreign_key_row` - L26-L37

```python
is_foreign_key_row(self, row: Any) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `getattr`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
