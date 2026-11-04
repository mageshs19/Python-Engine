# `converter/generators/db2_infrastructure_generator.py`

Source: [converter/generators/db2_infrastructure_generator.py](../../../../converter/generators/db2_infrastructure_generator.py) | 194 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `ad4dc2238618812489f465a387c7cc68a3107ce54d0155ef545634eb8973624c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates DB2 infrastructure in DATA DIVISION.

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.field_usage_analyzer import FieldUsageAnalyzer
from converter.domain.models import IdmsOperation
from converter.generators.db2_infrastructure.block_inserter import BlockInserter
from converter.generators.db2_infrastructure.cobol_line_utils import CobolLineUtils
from converter.generators.db2_infrastructure.cursor_spec_builder import CursorSpecBuilder
from converter.generators.db2_infrastructure.infrastructure_block_builder import InfrastructureBlockBuilder
from catalogs.output_sections import DB2_INFRASTRUCTURE_MARKER
from converter.resolvers.column_name_resolver import ColumnNameResolver
from converter.resolvers.cursor_column_resolver import CursorColumnResolver
from converter.resolvers.cursor_name_resolver import CursorNameResolver
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.relationship_resolver import RelationshipResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from rules.cursor_rules import cursor_paragraph_number
```

## Local dependency notes

- [catalogs/output_sections.py](../../catalogs/output_sections.md)
- [converter/analyzers/field_usage_analyzer.py](../analyzers/field_usage_analyzer.md)
- [converter/domain/models.py](../domain/models.md)
- [converter/generators/db2_infrastructure/block_inserter.py](db2_infrastructure/block_inserter.md)
- [converter/generators/db2_infrastructure/cobol_line_utils.py](db2_infrastructure/cobol_line_utils.md)
- [converter/generators/db2_infrastructure/cursor_spec_builder.py](db2_infrastructure/cursor_spec_builder.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](db2_infrastructure/infrastructure_block_builder.md)
- [converter/resolvers/column_name_resolver.py](../resolvers/column_name_resolver.md)
- [converter/resolvers/cursor_column_resolver.py](../resolvers/cursor_column_resolver.md)
- [converter/resolvers/cursor_name_resolver.py](../resolvers/cursor_name_resolver.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/relationship_resolver.py](../resolvers/relationship_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [rules/cursor_rules.py](../../rules/cursor_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_paragraph_generator.py](cursor_paragraph_generator.md)
- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `Db2InfrastructureGenerator` - L44-L194

```python
class Db2InfrastructureGenerator()
```

### `Db2InfrastructureGenerator.__init__` - L45-L76

```python
__init__(self, table_name_resolver: TableNameResolver, column_name_resolver: ColumnNameResolver, host_variable_resolver: HostVariableResolver, cursor_name_resolver: CursorNameResolver) -> None
```

Observed calls (lexical order): `RelationshipResolver`, `CursorColumnResolver`, `CobolLineUtils`, `CursorSpecBuilder`, `InfrastructureBlockBuilder`, `BlockInserter`.

### `Db2InfrastructureGenerator.apply` - L78-L142

```python
apply(self, cobol_text: str, operations: list[IdmsOperation], lrf_source_text: str | None=None) -> tuple[str, list[str]]
```

Observed calls (lexical order): `str`, `FieldUsageAnalyzer`, `FieldUsageAnalyzer(mapping_repository=self.mapping_repository, table_name_resolver=self.table_name_resolver...`, `messages.extend`, `self.cursor_specs`, `self.include_names`, `messages.append`, `', '.join`, `self._spec_builder.spec_messages`, `self.infrastructure_block`, `self._inserter.insert_in_data_division`, `self._inserter.ensure_dclgen_initialization`.

Control points:

- L87: `if not text`
- L106: `if include_names`
- L119: `if DB2_INFRASTRUCTURE_MARKER in text`

### `Db2InfrastructureGenerator.cursor_specs` - L144-L156

```python
cursor_specs(self, operations: list[IdmsOperation], cobol_text: str='', field_usage_analysis=None, lrf_source_text: str | None=None) -> list[dict[str, object]]
```

Observed calls (lexical order): `self._spec_builder.build`.

### `Db2InfrastructureGenerator.include_names` - L158-L162

```python
include_names(self, cursor_specs: list[dict[str, object]]) -> list[str]
```

Observed calls (lexical order): `self._spec_builder.include_names`.

### `Db2InfrastructureGenerator.infrastructure_block` - L164-L172

```python
infrastructure_block(self, include_names: list[str], cursor_specs: list[dict[str, object]]) -> str
```

Observed calls (lexical order): `self._block_builder.build`.

### `Db2InfrastructureGenerator._cursor_paragraph_spec` - L174-L194

```python
_cursor_paragraph_spec(self, cursor_order: int, table_name: str) -> dict[str, str]
```

Observed calls (lexical order): `hasattr`, `self.cursor_name_resolver.cursor_spec`, `self.cursor_name_resolver.cursor_name_from_table`, `cursor_paragraph_number`.

Control points:

- L179: `if hasattr(self.cursor_name_resolver, 'cursor_spec')`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
