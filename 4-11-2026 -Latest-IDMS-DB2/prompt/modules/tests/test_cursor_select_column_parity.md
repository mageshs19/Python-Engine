# `tests/test_cursor_select_column_parity.py`

Source: [tests/test_cursor_select_column_parity.py](../../../tests/test_cursor_select_column_parity.py) | 429 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `3b30653984d4dce06d7eaf46eb7e1b5778a0bfbadbdb8551a878c822b0600259`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> SELECT / INTO parity and full-record coverage.

## Module-level bindings

`CURSOR` (L39), `TABLE` (L40), `GROUP` (L41)

## Import declarations

```python
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from converter.resolvers.cursor_column_resolver import CursorColumnResolver
from converter.generators.db2_infrastructure.cursor_spec_builder import CursorSpecBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_declare_builder.py](../converter/generators/db2_infrastructure/cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](../converter/generators/db2_infrastructure/cursor_spec.md)
- [converter/generators/db2_infrastructure/cursor_spec_builder.py](../converter/generators/db2_infrastructure/cursor_spec_builder.md)
- [converter/resolvers/cursor_column_resolver.py](../converter/resolvers/cursor_column_resolver.md)

## Symbol contracts and control points

### `_LineUtils` - L44-L63

```python
class _LineUtils()
```

Minimal stand-in for the infrastructure line utils.

### `_LineUtils.and_lines` - L52-L56

```python
and_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `_LineUtils.comma_lines` - L59-L63

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `_host_for` - L66-L68

```python
_host_for(column: str) -> str
```

The host reference the resolver builds for one column.

Observed calls (lexical order): `column.replace`.

### `_source` - L71-L86

```python
_source(columns: list[str]) -> dict
```

A spec dict exactly as CursorSpecBuilder.build() emits it.

Observed calls (lexical order): `list`, `_host_for`.

### `_declared_columns` - L89-L108

```python
_declared_columns(lines: list[str]) -> list[str]
```

Column tokens between SELECT and FROM in a rendered DECLARE.

Observed calls (lexical order): `line.strip`, `next`, `enumerate`, `body.upper`, `body.upper().startswith`, `token.startswith`, `len`, `token.strip`, `token.strip().lstrip`, `token.strip().lstrip(',').strip`, `out.append`.

Control points:

- L101: `for body in bodies[start:stop]`
- L103: `if token.startswith('SELECT')`
- L106: `if token`

### `_host_column` - L111-L113

```python
_host_column(reference: str) -> str
```

':DCLDZBFASTV.DA-CPTAFS-479BFAS' -> 'DA_CPTAFS_479BFAS'.

Observed calls (lexical order): `reference.split`, `reference.split('.')[-1].strip`, `reference.split('.')[-1].strip().replace`, `reference.split('.')[-1].strip().replace('-', '_').upper`.

### `test_cursor_spec_preserves_the_select_column_sequence` - L119-L130

```python
test_cursor_spec_preserves_the_select_column_sequence()
```

CursorSpec must not silently reorder or drop a column.

Observed calls (lexical order): `range`, `_source`, `CursorSpec.read`.

### `test_declared_select_matches_the_host_list_count` - L133-L143

```python
test_declared_select_matches_the_host_list_count()
```

SELECT and INTO are positional. A count mismatch corrupts the row.

Observed calls (lexical order): `range`, `_source`, `_declared_columns`, `CursorDeclareBuilder`, `CursorDeclareBuilder(_LineUtils()).build`, `CursorSpec.read`, `_LineUtils`, `len`.

### `test_declared_select_matches_the_host_list_position_by_position` - L146-L155

```python
test_declared_select_matches_the_host_list_position_by_position()
```

Observed calls (lexical order): `_source`, `_declared_columns`, `CursorDeclareBuilder`, `CursorDeclareBuilder(_LineUtils()).build`, `CursorSpec.read`, `_LineUtils`, `enumerate`, `_host_column`.

Control points:

- L154: `for (index, column) in enumerate(declared)`

### `test_duplicate_columns_are_collapsed_in_both_carriers` - L158-L172

```python
test_duplicate_columns_are_collapsed_in_both_carriers()
```

A dedupe on one side only is the desynchronisation this guards.

Observed calls (lexical order): `_source`, `CursorSpec.read`, `_declared_columns`, `CursorDeclareBuilder`, `CursorDeclareBuilder(_LineUtils()).build`, `_LineUtils`, `len`.

### `_StubColumnNameResolver` - L178-L183

```python
class _StubColumnNameResolver()
```

### `_StubColumnNameResolver.__init__` - L179-L180

```python
__init__(self, columns: list[str]) -> None
```

### `_StubColumnNameResolver.columns_for_record` - L182-L183

```python
columns_for_record(self, record_name: str) -> list[str]
```

Observed calls (lexical order): `list`.

### `_StubTableNameResolver` - L186-L193

```python
class _StubTableNameResolver()
```

### `_StubTableNameResolver.table_for_record` - L188-L189

```python
table_for_record(record_name: str) -> str
```

### `_StubTableNameResolver.resolve_table` - L192-L193

```python
resolve_table(table_name: str) -> str
```

### `_StubUsageSelector` - L196-L201

```python
class _StubUsageSelector()
```

### `_StubUsageSelector.__init__` - L197-L198

```python
__init__(self, columns: list[str]) -> None
```

### `_StubUsageSelector.columns_from_field_usage` - L200-L201

```python
columns_from_field_usage(self, record_name, field_usage_analysis)
```

Observed calls (lexical order): `list`.

### `_StubMappingRepository` - L204-L211

```python
class _StubMappingRepository()
```

### `_StubMappingRepository.db2_columns_for_table` - L206-L207

```python
db2_columns_for_table(table_name: str) -> list[str]
```

### `_StubMappingRepository.rows_for_record` - L210-L211

```python
rows_for_record(record_name: str) -> list
```

### `_StubRelationshipResolver` - L214-L217

```python
class _StubRelationshipResolver()
```

### `_StubRelationshipResolver.resolve_for_child_record` - L216-L217

```python
resolve_for_child_record(record_name: str)
```

### `_resolver` - L220-L250

```python
_resolver(usage: list[str], full: list[str])
```

Build a REAL CursorColumnResolver through its real __init__.

Observed calls (lexical order): `CursorColumnResolver`, `_StubMappingRepository`, `_StubTableNameResolver`, `_StubColumnNameResolver`, `_StubRelationshipResolver`, `hasattr`, `_StubUsageSelector`.

### `test_usage_columns_drive_the_select_when_present` - L252-L264

```python
test_usage_columns_drive_the_select_when_present()
```

Observed calls (lexical order): `range`, `_resolver`, `_resolver(usage, full).select_columns_for_record`, `object`.

### `test_audit_columns_never_enter_the_cursor` - L267-L276

```python
test_audit_columns_never_enter_the_cursor()
```

Observed calls (lexical order): `_resolver`, `_resolver(usage, full).select_columns_for_record`, `object`.

### `test_missing_full_column_set_falls_back_to_usage` - L279-L288

```python
test_missing_full_column_set_falls_back_to_usage()
```

No fabrication: an unresolvable record keeps the proven columns.

Observed calls (lexical order): `_resolver`, `_resolver(usage, []).select_columns_for_record`, `object`.

### `test_empty_usage_on_a_non_materialised_record_selects_nothing` - L291-L322

```python
test_empty_usage_on_a_non_materialised_record_selects_nothing()
```

No proven usage and not materialised -> no columns from THIS layer.

Observed calls (lexical order): `_resolver`, `_resolver([], full).select_columns_for_record`, `object`.

### `test_materialised_record_selects_the_full_mapped_record` - L325-L341

```python
test_materialised_record_selects_the_full_mapped_record()
```

force_full_record=True projects every mapped column.

Observed calls (lexical order): `_resolver`, `_resolver([], full).select_columns_for_record`, `object`.

### `_StubHostVariableResolver` - L346-L350

```python
class _StubHostVariableResolver()
```

### `_StubHostVariableResolver.host_references_for_columns` - L348-L350

```python
host_references_for_columns(table_name: str, columns: list[str])
```

Observed calls (lexical order): `str`, `str(table_name).upper`, `c.replace`.

### `_AugmentOwner` - L353-L354

```python
class _AugmentOwner()
```

Declared class/data-model fields:

```python
host_variable_resolver = _StubHostVariableResolver()
```

### `_augment` - L357-L364

```python
_augment(specs: list[dict])
```

Observed calls (lexical order): `CursorSpecBuilder`, `_AugmentOwner`, `builder._augment_select_columns`.

### `test_child_order_by_key_is_added_to_its_own_select` - L367-L381

```python
test_child_order_by_key_is_added_to_its_own_select()
```

A minimal usage SELECT must still project its ORDER BY key.

Observed calls (lexical order): `_augment`, `any`.

### `test_parent_join_columns_are_added_from_child_where` - L384-L414

```python
test_parent_join_columns_are_added_from_child_where()
```

The parent must SELECT the keys the child WHERE reads from it.

Observed calls (lexical order): `_augment`, `any`.

### `test_materialised_record_selects_the_full_mapped_record` - L416-L429

```python
test_materialised_record_selects_the_full_mapped_record()
```

Observed calls (lexical order): `_resolver`, `_resolver([], full).select_columns_for_record`, `object`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
