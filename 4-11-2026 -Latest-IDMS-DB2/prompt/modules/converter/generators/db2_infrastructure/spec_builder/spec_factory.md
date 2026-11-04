# `converter/generators/db2_infrastructure/spec_builder/spec_factory.py`

Source: [converter/generators/db2_infrastructure/spec_builder/spec_factory.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/spec_factory.py) | 144 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `dc7bae03309c9edd0469a7e9dde804da28339fdface331882c5976a1798b6703`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Creates raw cursor specification dictionaries from IDMS operations.

## Module-level bindings

`__all__` (L144)

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.spec_builder.spec_build_context import SpecBuildContext
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_spec import IDMS_RETRIEVAL_VERBS, SPEC_CLOSE_PARAGRAPH, SPEC_CURSOR_NAME, SPEC_CURSOR_ORDER, SPEC_FETCH_PARAGRAPH, SPEC_HOST_VARIABLES, SPEC_IS_PARENT_CURSOR, SPEC_OPEN_PARAGRAPH, SPEC_ORDER_BY_COLUMNS, SPEC_RECORD_NAME, SPEC_SELECT_COLUMNS, SPEC_SET_NAME, SPEC_TABLE_NAME, SPEC_WHERE_CONDITIONS
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/spec_build_context.py](spec_build_context.md)
- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)
- [rules/cursor_spec/__init__.py](../../../../rules/cursor_spec/__init__.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)

## Symbol contracts and control points

### `SpecFactory` - L27-L141

```python
class SpecFactory()
```

Creates raw specifications before cross-spec augmentation.

### `SpecFactory.__init__` - L30-L38

```python
__init__(self, owner, relationship_policy, parent_classifier) -> None
```

### `SpecFactory.build` - L40-L61

```python
build(self, context: SpecBuildContext) -> list[dict[str, object]]
```

Observed calls (lexical order): `set`, `self._create_spec`, `specs.append`.

Control points:

- L48: `for operation in context.operations`
- L55: `if spec is None`

### `SpecFactory._create_spec` - L63-L141

```python
_create_spec(self, operation, cursor_order: int, seen: set[tuple[str, str, str]], context: SpecBuildContext) -> dict[str, object] | None
```

Observed calls (lexical order): `str`, `str(getattr(operation, 'operation', '') or '').upper`, `getattr`, `NameNormalizer.normalize`, `self.owner.table_name_resolver.table_for_record`, `seen.add`, `self.owner._cursor_paragraph_spec`, `self.owner.cursor_column_resolver.select_columns_for_record`, `self.relationship_policy.where_conditions`, `self.owner.cursor_name_resolver.cursor_name_from_table`, `self.owner.host_variable_resolver.host_references_for_columns`, `self.owner.cursor_column_resolver.order_by_columns_for_record`, `self.parent_classifier.is_parent`.

Control points:

- L73: `if operation_name not in IDMS_RETRIEVAL_VERBS`
- L79: `if not record`
- L86: `if not table`
- L90: `if duplicate_key in seen`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
