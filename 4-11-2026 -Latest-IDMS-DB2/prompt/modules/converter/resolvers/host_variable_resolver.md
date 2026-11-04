# `converter/resolvers/host_variable_resolver.py`

Source: [converter/resolvers/host_variable_resolver.py](../../../../converter/resolvers/host_variable_resolver.py) | 242 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `98e7930d9863f27569573ba061d1df62047034e3a8aeed587500e305de2b4a39`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
import re
from catalogs.db2_naming_catalog import DB2_HOST_REFERENCE_PREFIX
from converter.repositories.dclgen_repository import DclgenRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [catalogs/db2_naming_catalog.py](../../catalogs/db2_naming_catalog.md)
- [converter/repositories/dclgen_repository.py](../repositories/dclgen_repository.md)
- [converter/resolvers/table_name_resolver.py](table_name_resolver.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (18)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_program_feedback_composer.py](../composers/update_program_feedback_composer.md)
- [converter/composers/update_sql_cleanup_base.py](../composers/update_sql_cleanup_base.md)
- [converter/generators/cursor_paragraph_generator.py](../generators/cursor_paragraph_generator.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/generators/sql_generator.py](../generators/sql_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [converter/resolvers/relationship_child_resolver.py](relationship_child_resolver.md)
- [converter/resolvers/relationship_resolver.py](relationship_resolver.md)
- [converter/resolvers/update_sql_plan_resolver.py](update_sql_plan_resolver.md)
- [converter/transformers/field_reference/field_reference_host_resolver.py](../transformers/field_reference/field_reference_host_resolver.md)
- [converter/transformers/field_reference_context_builder.py](../transformers/field_reference_context_builder.md)
- [converter/transformers/field_reference_rewriter.py](../transformers/field_reference_rewriter.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../tests/test_handwritten_obtain_calc_planner.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_sql_insert_sequence_metadata.py](../../tests/test_sql_insert_sequence_metadata.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `HostVariableResolver` - L9-L242

```python
class HostVariableResolver()
```

Resolves DCLGEN host variables.

Declared class/data-model fields:

```python
HOST_OF_GROUP_PATTERN = re.compile('^:?\\s*(?P<host>[A-Z][A-Z0-9-]*)\\s+OF\\s+(?P<group>DCL[A-Z0-9-]+)\\s*$', flags=re.IGNORECASE)
GROUP_DOT_HOST_PATTERN = re.compile('^:?\\s*(?P<group>DCL[A-Z0-9-]+)\\s*\\.\\s*(?P<host>[A-Z][A-Z0-9-]*)\\s*$', flags=re.IGNORECASE)
DOUBLE_COLON_PATTERN = re.compile('^:+', flags=re.IGNORECASE)
```

### `HostVariableResolver.__init__` - L59-L65

```python
__init__(self, dclgen_repository: DclgenRepository, table_name_resolver: TableNameResolver) -> None
```

### `HostVariableResolver.host_for_column` - L67-L80

```python
host_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `self.dclgen_repository.host_for_column`.

Control points:

- L74: `if not resolved_table`

### `HostVariableResolver.group_for_table` - L82-L96

```python
group_for_table(self, table_name: str) -> str
```

Observed calls (lexical order): `self.table_name_resolver.resolve_table`, `self.dclgen_repository.group_for_table`, `NameNormalizer.to_cobol`.

Control points:

- L88: `if not resolved_table`
- L93: `if group`

### `HostVariableResolver.host_reference_for_column` - L98-L114

```python
host_reference_for_column(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.group_for_table`, `self.host_for_column`, `self.normalize_host_reference`.

Control points:

- L109: `if not group or not host`

### `HostVariableResolver.host_references_for_columns` - L116-L141

```python
host_references_for_columns(self, table_name: str, columns: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `self.host_reference_for_column`, `reference.upper`, `seen.add`, `output.append`.

Control points:

- L124: `for column in columns`
- L130: `if not reference`
- L135: `if key in seen`

### `HostVariableResolver.normalize_host_reference` - L143-L201

```python
normalize_host_reference(self, value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `text.replace`, `self.DOUBLE_COLON_PATTERN.sub`, `self.HOST_OF_GROUP_PATTERN.match`, `NameNormalizer.to_cobol`, `of_match.group`, `self.GROUP_DOT_HOST_PATTERN.match`, `dot_match.group`, `text.startswith`, `text[1:].strip`, `text.split`, `group.upper`, `group.upper().startswith`, `text.upper`, `text.upper().startswith`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L149: `if not text`
- L157: `if of_match`
- L161: `if not group or not host`
- L168: `if dot_match`
- L172: `if not group or not host`
- L177: `if text.startswith(DB2_HOST_REFERENCE_PREFIX)`
- L180: `if '.' in text`
- L185: `if group and host and group.upper().startswith('DCL')`
- Another 4 conditions/loops exist in this source span.

### `HostVariableResolver.valid_host_references` - L203-L215

```python
valid_host_references(self) -> set[str]
```

Observed calls (lexical order): `set`, `self.dclgen_repository.valid_host_references`, `self.normalize_host_reference`, `output.add`.

Control points:

- L208: `for reference in self.dclgen_repository.valid_host_references()`
- L211: `if normalized`

### `HostVariableResolver.has_host_for_column` - L217-L227

```python
has_host_for_column(self, table_name: str, column_name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.host_for_column`.

### `HostVariableResolver.host_reference_key` - L229-L242

```python
host_reference_key(self, table_name: str, column_name: str) -> str
```

Observed calls (lexical order): `self.host_reference_for_column`.

Control points:

- L239: `if not reference`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
