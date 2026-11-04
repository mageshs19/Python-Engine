# `converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py`

Source: [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py) | 281 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `4ad6edab4b0c0b43854bf7ed6c2005a414b96b3856b1e3bb61755c1967249780`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Facade for DB2 cursor specification construction.

## Module-level bindings

`__all__` (L281)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.domain.models import IdmsOperation
from converter.generators.db2_infrastructure.spec_builder.spec_build_context import SpecBuildContext
from converter.generators.db2_infrastructure.spec_builder.spec_factory import SpecFactory
from converter.generators.db2_infrastructure.spec_builder.spec_lrf_scanner import SpecLrfScanner
from converter.generators.db2_infrastructure.spec_builder.spec_navigation_scanner import SpecNavigationScanner
from converter.generators.db2_infrastructure.spec_builder.spec_parent_classifier import SpecParentClassifier
from converter.generators.db2_infrastructure.spec_builder.spec_relationship_policy import SpecRelationshipPolicy
from converter.generators.db2_infrastructure.spec_builder.spec_reporter import SpecReporter
from converter.generators.db2_infrastructure.spec_builder.spec_select_augmenter import SpecSelectAugmenter
from converter.generators.db2_infrastructure.spec_builder.spec_where_builder import SpecWhereBuilder
from converter.services.name_normalizer import NameNormalizer
from converter.resolvers.lrf_cursor_where_resolver import LrfCursorWhereResolver
```

## Local dependency notes

- [converter/analyzers/field_usage_analyzer.py](../../../analyzers/field_usage_analyzer.md)
- [converter/domain/models.py](../../../domain/models.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_build_context.py](spec_build_context.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_factory.py](spec_factory.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_lrf_scanner.py](spec_lrf_scanner.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](spec_navigation_scanner.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_parent_classifier.py](spec_parent_classifier.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_relationship_policy.py](spec_relationship_policy.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_reporter.py](spec_reporter.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_select_augmenter.py](spec_select_augmenter.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_where_builder.py](spec_where_builder.md)
- [converter/resolvers/lrf_cursor_where_resolver.py](../../../resolvers/lrf_cursor_where_resolver.md)
- [converter/services/name_normalizer.py](../../../services/name_normalizer.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/spec_builder/__init__.py](__init__.md)
- [tests/spec_builder/test_cursor_spec_builder.py](../../../../tests/spec_builder/test_cursor_spec_builder.md)
- [tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.py](../../../../tests/spec_builder/test_cursor_spec_builder_lrf_extra_filters.md)

## Symbol contracts and control points

### `CursorSpecBuilder` - L48-L278

```python
class CursorSpecBuilder()
```

Builds and augments DB2 cursor specification dictionaries.

### `CursorSpecBuilder.__init__` - L51-L74

```python
__init__(self, owner) -> None
```

Observed calls (lexical order): `SpecNavigationScanner`, `SpecLrfScanner`, `SpecParentClassifier`, `SpecWhereBuilder`, `getattr`, `SpecSelectAugmenter`.

### `CursorSpecBuilder.relationship_policy` - L77-L96

```python
relationship_policy(self) -> SpecRelationshipPolicy
```

Create relationship policy only for a complete build.

Observed calls (lexical order): `getattr`, `AttributeError`, `SpecRelationshipPolicy`.

Control points:

- L79: `if self._relationship_policy is None`
- L85: `if resolver is None`

Explicit raises: `AttributeError('CursorSpecBuilder.build() requires owner.relationship_resolver')`.

### `CursorSpecBuilder.factory` - L99-L108

```python
factory(self) -> SpecFactory
```

Create the spec factory only when build() is called.

Observed calls (lexical order): `SpecFactory`.

Control points:

- L101: `if self._factory is None`

### `CursorSpecBuilder.reporter` - L111-L122

```python
reporter(self) -> SpecReporter
```

Create reporter only when report output is requested.

Observed calls (lexical order): `getattr`, `AttributeError`, `SpecReporter`.

Control points:

- L113: `if self._reporter is None`
- L115: `if line_utils is None`

Explicit raises: `AttributeError('Cursor reporting requires owner.line_utils')`.

### `CursorSpecBuilder.build` - L124-L157

```python
build(self, operations: list[IdmsOperation], cobol_text: str='', field_usage_analysis=None, lrf_source_text: str | None=None) -> list[dict[str, object]]
```

Build and augment cursor specifications.

Observed calls (lexical order): `self._reset_messages`, `self._field_usage`, `SpecBuildContext.create`, `self.factory.build`, `self._apply_lrf_extra_filters`, `self._augment_select_columns`, `self.messages.extend`.

Control points:

- L135: `if usage is None`

### `CursorSpecBuilder._apply_lrf_extra_filters` - L159-L221

```python
_apply_lrf_extra_filters(self, specs: list[dict[str, object]], cobol_text: str) -> None
```

Push source-proven LRF path filters into the actual cursor specs.

Observed calls (lexical order): `LrfCursorWhereResolver`, `getattr`, `resolver.extract_lrf_cursors_from_cobol`, `NameNormalizer.normalize`, `spec.get`, `lrf_info_by_record.get`, `info.get`, `str`, `str(info.get('extra_filters', '') or '').strip`, `resolver.extra_filter_conditions_for_lrf_cursor`, `list`, `existing.append`, `self.messages.extend`, `str(item).strip`, `str(item).strip().upper`, `str(condition).strip`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L176: `if not specs or not cobol_text`
- L187: `if not lrf_info_by_record`
- L190: `for spec in specs`
- L193: `if not info`
- L197: `if not extra_text`
- L204: `if conditions is None`
- L207: `if '1 = 0' not in existing`
- L214: `for condition in conditions`
- Another 1 conditions/loops exist in this source span.

### `CursorSpecBuilder._augment_select_columns` - L223-L228

```python
_augment_select_columns(self, specs: list[dict[str, object]]) -> None
```

Backward-compatible select-column augmentation entry point.

Observed calls (lexical order): `self.augmenter.augment`.

### `CursorSpecBuilder.include_names` - L230-L235

```python
include_names(self, cursor_specs: list[dict[str, object]]) -> list[str]
```

Return DCLGEN include names.

Observed calls (lexical order): `self.reporter.include_names`.

### `CursorSpecBuilder.spec_messages` - L237-L242

```python
spec_messages(self, cursor_specs: list[dict[str, object]]) -> list[str]
```

Return completed-spec diagnostics.

Observed calls (lexical order): `self.reporter.messages`.

### `CursorSpecBuilder._field_usage` - L244-L271

```python
_field_usage(self, cobol_text: str)
```

Observed calls (lexical order): `getattr`, `AttributeError`, `FieldUsageAnalyzer`, `FieldUsageAnalyzer(mapping_repository=mapping_repository, table_name_resolver=table_name_resolver).analyze`.

Control points:

- L256: `if mapping_repository is None`
- L262: `if table_name_resolver is None`

Explicit raises: `AttributeError('CursorSpecBuilder.build() requires owner.mapping_repository')`; `AttributeError('CursorSpecBuilder.build() requires owner.table_name_resolver')`.

### `CursorSpecBuilder._reset_messages` - L273-L278

```python
_reset_messages(self) -> None
```

Control points:

- L277: `if self._relationship_policy is not None`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
