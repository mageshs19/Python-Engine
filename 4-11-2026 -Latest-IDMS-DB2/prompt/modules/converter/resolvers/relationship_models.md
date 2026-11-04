# `converter/resolvers/relationship_models.py`

Source: [converter/resolvers/relationship_models.py](../../../../converter/resolvers/relationship_models.py) | 24 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `a915a9cf3e7d98082ae617a497d4a6a14fcabbe10d92095b20dde420a1bee307`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)

## Symbol contracts and control points

### `RelationshipCondition` - L7-L14

```python
class RelationshipCondition()
```

Declared class/data-model fields:

```python
child_record: str
child_table: str
child_column: str
parent_record: str
parent_table: str
parent_column: str
parent_host_reference: str
```

### `RelationshipResolution` - L18-L24

```python
class RelationshipResolution()
```

Declared class/data-model fields:

```python
child_record: str
parent_record: str = ''
child_table: str = ''
parent_table: str = ''
conditions: list[RelationshipCondition] = field(default_factory=list)
diagnostics: list[str] = field(default_factory=list)
```

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
