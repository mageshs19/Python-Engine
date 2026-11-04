# `converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py) | 129 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `18c7b5729ac8e8d2bd8dd04caa57e55ed3135a2f45933377b62601ad3ab0ed80`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Turns a resolved relationship into WHERE predicates, once.

## Module-level bindings

`__all__` (L129)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_spec import DCLGEN_GROUP_PREFIX, HOST_GROUP_SEPARATOR, HOST_REFERENCE_PREFIX, RELATIONSHIP_PREDICATE_TEMPLATE
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py](spec_select_augmenter.md)

## Symbol contracts and control points

### `SpecWhereBuilder` - L46-L126

```python
class SpecWhereBuilder()
```

Builds and reads child-cursor predicates.

### `SpecWhereBuilder.__init__` - L49-L51

```python
__init__(self, dclgen_repository=None) -> None
```

### `SpecWhereBuilder.predicates` - L53-L83

```python
predicates(self, conditions) -> list[str]
```

One predicate per resolved relationship condition.

Observed calls (lexical order): `set`, `NameNormalizer.normalize`, `getattr`, `str`, `str(getattr(condition, 'parent_host_reference', '') or '').strip`, `RELATIONSHIP_PREDICATE_TEMPLATE.format`, `seen.add`, `output.append`.

Control points:

- L62: `for condition in conditions or []`
- L70: `if not child_column or not parent_host`
- L77: `if predicate in seen`

### `SpecWhereBuilder.parent_reference` - L85-L104

```python
parent_reference(self, condition: str) -> tuple[str, str]
```

'CHILD_COL = :DCLDZBEFFTV.CT-RKTPROD-479BEFF' -> (table, column).

Observed calls (lexical order): `str`, `text.split`, `text.split(HOST_REFERENCE_PREFIX, 1)[1].strip`, `host.partition`, `group.strip`, `group.strip().upper`, `self._table_for_group`, `NameNormalizer.normalize`, `field.strip`.

Control points:

- L93: `if HOST_REFERENCE_PREFIX not in text`
- L97: `if HOST_GROUP_SEPARATOR not in host`

### `SpecWhereBuilder._table_for_group` - L107-L126

```python
_table_for_group(self, group: str) -> str
```

Ask the DCLGEN repository; fall back to the prefix rule.

Observed calls (lexical order): `getattr`, `callable`, `resolver`, `str`, `group.startswith`, `len`.

Control points:

- L109: `if not group`
- L115: `if callable(resolver)`
- L120: `if table`
- L123: `if group.startswith(DCLGEN_GROUP_PREFIX)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
