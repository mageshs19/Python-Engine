# `converter/transformers/field_reference_context_builder.py`

Source: [converter/transformers/field_reference_context_builder.py](../../../../converter/transformers/field_reference_context_builder.py) | 417 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `f60ce3ae32f6e46f013e54d34f1e2d9099c43d195b8c6bb5c076f849a3708731`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`FILLER_NAME` (L19), `GROUP_SPLIT_TEMPLATE` (L24), `GROUP_PARTIAL_TEMPLATE` (L29), `GROUP_NARROWED_TEMPLATE` (L34), `__all__` (L415)

## Import declarations

```python
from __future__ import annotations
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
from converter.transformers.field_reference.field_reference_field_extractor import FieldReferenceFieldExtractor
from converter.transformers.field_reference.field_reference_host_resolver import FieldReferenceHostResolver
from rules.field_reference_rewriter_rules import DCLGEN_GROUP_PREFIX
```

## Local dependency notes

- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [converter/transformers/field_reference/field_reference_field_extractor.py](field_reference/field_reference_field_extractor.md)
- [converter/transformers/field_reference/field_reference_host_resolver.py](field_reference/field_reference_host_resolver.md)
- [rules/field_reference_rewriter_rules.py](../../rules/field_reference_rewriter_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference_rewriter.py](field_reference_rewriter.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)

## Symbol contracts and control points

### `FieldReferenceContextBuilder` - L40-L412

```python
class FieldReferenceContextBuilder()
```

Builds record-to-field and record-to-DCLGEN context maps from Sheet Mapping and DCLGEN metadata.

### `FieldReferenceContextBuilder.__init__` - L111-L128

```python
__init__(self, *, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver) -> None
```

Observed calls (lexical order): `FieldReferenceFieldExtractor`, `FieldReferenceHostResolver`.

### `FieldReferenceContextBuilder.build_reference_maps` - L130-L177

```python
build_reference_maps(self) -> tuple[dict[str, dict[str, str]], dict[str, str], dict[str, str], dict[str, str]]
```

Observed calls (lexical order): `self.mapping_repository.records`, `NameNormalizer.normalize`, `self.table_name_resolver.table_for_record`, `NameNormalizer.to_cobol`, `self.field_map_for_record`, `self.add_redefines_aliases`.

Control points:

- L147: `for record in self.mapping_repository.records()`
- L149: `if not normalized_record`
- L156: `if resolved_table`

### `FieldReferenceContextBuilder.field_map_for_record` - L179-L207

```python
field_map_for_record(self, record_name: str) -> dict[str, str]
```

Observed calls (lexical order): `self.mapping_repository.rows_for_record`, `self.source_candidates_from_row`, `self.target_reference_for_row`, `self._extractor.field_key`, `self.add_group_resolutions`.

Control points:

- L184: `for row in rows`
- L186: `if not source_candidates`
- L190: `if not target_reference`
- L193: `for source_candidate in source_candidates`
- L195: `if not source_key`
- L197: `if source_key not in output`

### `FieldReferenceContextBuilder.target_reference_for_row` - L212-L233

```python
target_reference_for_row(self, row) -> str
```

The DCLGEN host reference this row maps to, or ''.

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `self._extractor.first_non_empty`, `getattr`, `NameNormalizer.normalize`, `self._host_resolver.dclgen_reference_for_column`.

Control points:

- L227: `if not target_table or not target_column`

### `FieldReferenceContextBuilder.layout_nodes` - L238-L273

```python
layout_nodes(self, rows) -> list[dict]
```

One node per row that names a COBOL field, in layout order.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(row, 'cobol_zone', '') or '').strip`, `zone.split`, `parts[0].isdigit`, `self._extractor.extract_field_name`, `self._extractor.field_key`, `nodes.append`, `int`, `bool`, `self._extractor.extract_redefines_base`, `key.upper`, `self.target_reference_for_row`.

Control points:

- L247: `for row in rows`
- L249: `if not zone`
- L253: `if not parts or not parts[0].isdigit()`
- L258: `if not key`

### `FieldReferenceContextBuilder.gather_mapped_content` - L275-L316

```python
gather_mapped_content(self, nodes: list[dict], index: int) -> tuple[list[str], list[str]]
```

(mapped references, unmapped leaf names) beneath nodes\[index\].

Observed calls (lexical order): `len`, `self.skip_subtree`, `references.append`, `unmapped.append`.

Control points:

- L293: `while position < total and nodes[position]['level'] > level`
- L296: `if node['redefines'] or node['filler']`
- L300: `if node['reference']`
- L301: `if node['reference'] not in references`
- L311: `if is_leaf and node['key'] not in unmapped`

### `FieldReferenceContextBuilder.skip_subtree` - L319-L327

```python
skip_subtree(nodes: list[dict], index: int) -> int
```

Index of the first node that is NOT beneath nodes\[index\].

Observed calls (lexical order): `len`.

Control points:

- L324: `while position < len(nodes) and nodes[position]['level'] > level`

### `FieldReferenceContextBuilder.add_group_resolutions` - L329-L362

```python
add_group_resolutions(self, *, record_name: str, rows, output: dict[str, str]) -> None
```

Store group decomposition facts; emit warnings only at use sites.

Observed calls (lexical order): `self.layout_nodes`, `NameNormalizer.normalize`, `self.group_issues.setdefault`, `self.group_columns.setdefault`, `enumerate`, `self.gather_mapped_content`, `len`, `list`.

Control points:

- L342: `for (index, node) in enumerate(nodes)`
- L343: `if node['reference'] or node['redefines'] or node['filler']`
- L345: `if node['key'] in output`
- L349: `if not references`
- L352: `if len(references) > 1 or unmapped`

### `FieldReferenceContextBuilder.source_candidates_from_row` - L364-L385

```python
source_candidates_from_row(self, row) -> list[str]
```

Observed calls (lexical order): `getattr`, `self._extractor.extract_field_name`, `NameNormalizer.to_cobol`, `candidates.append`, `self._extractor.extract_redefines_base`.

Control points:

- L367: `for value in [getattr(row, 'cobol_zone', ''), getattr(row, 'reference_field_name_copybook', '')]`
- L372: `if not field_name`
- L376: `if cobol_name and cobol_name not in candidates`
- L380: `if redefines_base`
- L382: `if base_name and base_name not in candidates`

### `FieldReferenceContextBuilder.add_redefines_aliases` - L387-L412

```python
add_redefines_aliases(self, record_field_map: dict[str, dict[str, str]]) -> None
```

Observed calls (lexical order): `self.mapping_repository.records`, `NameNormalizer.normalize`, `self.mapping_repository.rows_for_record`, `record_field_map.get`, `getattr`, `self._extractor.extract_field_name`, `self._extractor.extract_redefines_base`, `self._extractor.field_key`.

Control points:

- L391: `for record in self.mapping_repository.records()`
- L395: `if not field_map`
- L398: `for row in rows`
- L402: `if not alias_name or not base_name`
- L407: `if not alias_key or not base_key`
- L409: `if alias_key in field_map`
- L411: `if base_key in field_map`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
