# `converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py`

Source: [converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py](../../../../../converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py) | 239 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `3aabeabff9bd9be987b2b5d63a8f1d04bf2d9e1f3246a5f474f7b0e29146de79`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Enhanced cursor spec builder with LRF support.

## Import declarations

```python
from converter.services.name_normalizer import NameNormalizer
from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.generators.db2_infrastructure.cursor_spec_builder import CursorSpecBuilder
```

## Local dependency notes

- [converter/analyzers/field_usage_analyzer.py](../../analyzers/field_usage_analyzer.md)
- [converter/generators/db2_infrastructure/cursor_spec_builder.py](cursor_spec_builder.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/lrf_cursor_fix.py](../../pipeline/lrf_cursor_fix.md)

## Symbol contracts and control points

### `build_with_lrf_support` - L11-L201

```python
build_with_lrf_support(self, operations: list, cobol_text: str='', field_usage_analysis=None, lrf_cursor_where_resolver=None) -> list[dict]
```

Enhanced build() that detects LRF cursors and generates WHERE clauses.

Observed calls (lexical order): `set`, `FieldUsageAnalyzer`, `FieldUsageAnalyzer(mapping_repository=self.owner.mapping_repository, table_name_resolver=self.owner.table_n...`, `self._navigated_records`, `lrf_cursor_where_resolver.extract_lrf_cursors_from_cobol`, `str`, `str(operation.operation or '').upper`, `NameNormalizer.normalize`, `self.owner.table_name_resolver.table_for_record`, `seen.add`, `self.owner.cursor_name_resolver.cursor_name_from_table`, `self.owner._cursor_paragraph_spec`, `self.owner.cursor_column_resolver.select_columns_for_record`, `self.owner.relationship_resolver.resolve_for_child_record`, `lrf_cursors.get`, `lrf_cursor_info.get`.
Another 12 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L44: `if field_usage_analysis is None`
- L55: `if lrf_cursor_where_resolver`
- L60: `for operation in operations or []`
- L62: `if operation_name not in {'OBTAIN_FIRST', 'OBTAIN_NEXT', 'FIND_FIRST'}`
- L67: `if not record_name`
- L73: `if not table_name`
- L77: `if key in seen`
- L114: `if parent_record and parent_record in navigated_records`
- Another 7 conditions/loops exist in this source span.

### `integrate_lrf_support_into_cursor_spec_builder` - L205-L239

```python
integrate_lrf_support_into_cursor_spec_builder(lrf_resolver)
```

Integrate LRF support into CursorSpecBuilder.

### `integrate_lrf_support_into_cursor_spec_builder.wrapped_build` - L222-L235

```python
wrapped_build(self, operations: list, cobol_text: str='', field_usage_analysis=None)
```

Wrapper that adds LRF support.

Observed calls (lexical order): `build_with_lrf_support`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
