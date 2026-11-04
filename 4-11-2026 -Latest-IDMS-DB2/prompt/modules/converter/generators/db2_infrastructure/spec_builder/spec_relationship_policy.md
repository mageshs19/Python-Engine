# `converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py) | 201 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `0a94e6785b5ce7a7e1c8f2ecd3375735a16750b069d17c341aedd44f678d1c35`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Creates safe relationship predicates for child cursor specifications.

## Module-level bindings

`UNMAPPED_DIAGNOSTIC_TEMPLATE` (L80), `UNRENDERABLE_DIAGNOSTIC_TEMPLATE` (L83), `__all__` (L201)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_spec import SPEC_MESSAGES
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [tests/spec_builder/conftest.py](../../../../tests/spec_builder/conftest.md)

## Symbol contracts and control points

### `SpecRelationshipPolicy` - L88-L198

```python
class SpecRelationshipPolicy()
```

Build predicates once and refuse joins with unpopulated parent hosts.

### `SpecRelationshipPolicy.__init__` - L91-L94

```python
__init__(self, relationship_resolver, where_builder) -> None
```

### `SpecRelationshipPolicy.where_conditions` - L96-L178

```python
where_conditions(self, record: str, navigated_records: set[str], lrf_cursors: dict) -> list[str]
```

Return one de-duplicated predicate list for a child record.

Observed calls (lexical order): `NameNormalizer.normalize`, `(lrf_cursors or {}).get`, `str`, `str(getattr(lrf_entry, 'sweep_condition', '') or '').strip`, `str(getattr(lrf_entry, 'sweep_condition', '') or '').strip().upper`, `getattr`, `sweep_condition.startswith`, `self._log`, `self.relationship_resolver.resolve_for_child_record`, `list`, `self.where_builder.predicates`, `len`.

Control points:

- L121: `if lrf_entry is not None and sweep_condition.startswith('SWEEP-')`
- L134: `if not conditions`
- L149: `if parent and parent not in navigated_records`
- L150: `if lrf_entry is None`
- L171: `if lrf_entry is not None and predicates`

### `SpecRelationshipPolicy._log` - L180-L198

```python
_log(self, key: str, **fields) -> None
```

Record one diagnostic. An unmapped key is REPORTED, not dropped.

Observed calls (lexical order): `SPEC_MESSAGES.get`, `' '.join`, `fields.items`, `sorted`, `self.messages.append`, `UNMAPPED_DIAGNOSTIC_TEMPLATE.format`, `template.format`, `UNRENDERABLE_DIAGNOSTIC_TEMPLATE.format`.

Control points:

- L184: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
