# `converter/generators/cursor_paragraph_generator.py`

Source: [converter/generators/cursor_paragraph_generator.py](../../../../converter/generators/cursor_paragraph_generator.py) | 406 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `81a286c12894510b0b5fa8ef0714e6b1c8cf9e2d0354ee8ee3ac12e4f375c20b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generates DB2 cursor OPEN / FETCH / CLOSE paragraphs.

## Module-level bindings

`__all__` (L406)

## Import declarations

```python
from __future__ import annotations
from typing import Optional
from catalogs.output_sections import DB2_CURSOR_PARAGRAPH_MARKER
from converter.domain.models import IdmsOperation
from converter.generators.cursor_paragraph.cursor_paragraph_body_builder import CursorParagraphBodyBuilder
from converter.generators.cursor_paragraph.cursor_perform_rewriter import CursorPerformRewriter
from converter.generators.db2_infrastructure_generator import Db2InfrastructureGenerator
from converter.generators.sql_error_generator import SqlErrorGenerator
from converter.resolvers.host_variable_resolver import HostVariableResolver
from patterns.db2_patterns import END_PROGRAM_PATTERN
from rules.cursor_paragraph_rules import COMMENT_BLOCK_TEMPLATE, DIAG_BLOCK_EXISTS, DIAG_GENERATED_TEMPLATE, DIAG_NO_CURSOR_OPERATIONS, DIAG_NO_HOST_VARIABLES_TEMPLATE, SQL_ERROR_PARAGRAPH_NAME
```

## Local dependency notes

- [catalogs/output_sections.py](../../catalogs/output_sections.md)
- [converter/domain/models.py](../domain/models.md)
- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](cursor_paragraph/cursor_paragraph_body_builder.md)
- [converter/generators/cursor_paragraph/cursor_perform_rewriter.py](cursor_paragraph/cursor_perform_rewriter.md)
- [converter/generators/db2_infrastructure_generator.py](db2_infrastructure_generator.md)
- [converter/generators/sql_error_generator.py](sql_error_generator.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [patterns/db2_patterns.py](../../patterns/db2_patterns.md)
- [rules/cursor_paragraph_rules.py](../../rules/cursor_paragraph_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../../tests/test_generic_cursor_numbering_and_perform_integrity.md)

## Symbol contracts and control points

### `CursorParagraphGenerator` - L72-L403

```python
class CursorParagraphGenerator()
```

Builds and inserts the generated cursor paragraph block.

Declared class/data-model fields:

```python
SQLERROR_PARAGRAPH_NAME = SQL_ERROR_PARAGRAPH_NAME
```

### `CursorParagraphGenerator.__init__` - L77-L96

```python
__init__(self, db2_infrastructure_generator: Db2InfrastructureGenerator, host_variable_resolver: HostVariableResolver, sql_error_generator: SqlErrorGenerator, body_builder: CursorParagraphBodyBuilder | None=None, perform_rewriter: CursorPerformRewriter | None=None) -> None
```

Observed calls (lexical order): `CursorParagraphBodyBuilder`, `self._mapping_repository`, `CursorPerformRewriter`.

### `CursorParagraphGenerator.apply` - L101-L148

```python
apply(self, cobol_text: str, operations: list[IdmsOperation]) -> tuple[str, list[str]]
```

Observed calls (lexical order): `self._reset_body_builder`, `str`, `self._cursor_specs`, `self.messages.append`, `self._sql_error_paragraph_name`, `self.perform_rewriter.normalize_sql_error_references`, `self.perform_rewriter.rewrite`, `self.paragraph_block`, `self._insert_paragraph_block`, `DIAG_GENERATED_TEMPLATE.format`, `len`, `self._host_variable_warnings`, `self.messages.extend`, `self._body_builder_messages`.

Control points:

- L111: `if not text`
- L116: `if not cursor_specs`
- L130: `if DB2_CURSOR_PARAGRAPH_MARKER in updated_text`

### `CursorParagraphGenerator.augment_lrf_procedure_division` - L153-L192

```python
augment_lrf_procedure_division(self, cobol_text: str) -> tuple[str, list[str]]
```

Apply LRF host variable population after main generation.

Observed calls (lexical order): `getattr`, `populator.augment_procedure_division`, `list`, `type`.

Control points:

- L170: `if not populator`

### `CursorParagraphGenerator.paragraph_block` - L197-L250

```python
paragraph_block(self, cursor_specs: list[dict[str, object]], sql_error_paragraph: str) -> str
```

Observed calls (lexical order): `lines.extend`, `self._comment_block`, `lines.append`, `spec.get`, `str`, `list`, `bool`, `builder`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L206: `for spec in cursor_specs`
- L208: `if not cursor_name`
- L222: `for (key, builder, needs_hosts) in builders`
- L224: `if not paragraph_name`
- L227: `if needs_hosts`

### `CursorParagraphGenerator.open_paragraph` - L255-L265

```python
open_paragraph(self, cursor_name: str, paragraph_name: str, sql_error_paragraph: str) -> list[str]
```

Observed calls (lexical order): `self.body_builder.open_paragraph`.

### `CursorParagraphGenerator.fetch_paragraph` - L267-L285

```python
fetch_paragraph(self, cursor_name: str, paragraph_name: str, host_variables: list[str], sql_error_paragraph: str, where_conditions: list[str] | None=None, table_name: str='', is_parent_cursor: bool=False) -> list[str]
```

Observed calls (lexical order): `self.body_builder.fetch_paragraph`, `self._clean_host_variables`.

### `CursorParagraphGenerator.close_paragraph` - L287-L297

```python
close_paragraph(self, cursor_name: str, paragraph_name: str, sql_error_paragraph: str) -> list[str]
```

Observed calls (lexical order): `self.body_builder.close_paragraph`.

### `CursorParagraphGenerator._sql_error_paragraph_name` - L302-L307

```python
_sql_error_paragraph_name(self) -> str
```

Single source of truth for the SQL error paragraph name.

Observed calls (lexical order): `str`, `str(getattr(self.sql_error_generator, 'PARAGRAPH_NAME', '') or '').strip`, `getattr`.

### `CursorParagraphGenerator._mapping_repository` - L309-L321

```python
_mapping_repository(self)
```

Sheet Mapping, reached through the infrastructure generator.

Observed calls (lexical order): `getattr`.

### `CursorParagraphGenerator._reset_body_builder` - L323-L332

```python
_reset_body_builder(self) -> None
```

Drop the previous program's label diagnostics.

Observed calls (lexical order): `getattr`, `callable`, `reset`.

Control points:

- L331: `if callable(reset)`

### `CursorParagraphGenerator._body_builder_messages` - L334-L340

```python
_body_builder_messages(self) -> list[str]
```

Label-resolution diagnostics from the body builder.

Observed calls (lexical order): `getattr`, `list`.

### `CursorParagraphGenerator._cursor_specs` - L342-L355

```python
_cursor_specs(self, operations: list[IdmsOperation]) -> list[dict[str, object]]
```

Reuse the specs the infrastructure generator already built.

Observed calls (lexical order): `getattr`, `self.db2_infrastructure_generator.cursor_specs`.

Control points:

- L352: `if cached_specs`

### `CursorParagraphGenerator._clean_host_variables` - L358-L369

```python
_clean_host_variables(host_variables: list[str]) -> list[str]
```

Observed calls (lexical order): `set`, `str`, `str(host or '').strip`, `seen.add`, `out.append`.

Control points:

- L362: `for host in host_variables or []`
- L364: `if not value or value in seen`

### `CursorParagraphGenerator._comment_block` - L372-L373

```python
_comment_block(title: str) -> list[str]
```

Observed calls (lexical order): `COMMENT_BLOCK_TEMPLATE.format`.

### `CursorParagraphGenerator._host_variable_warnings` - L375-L392

```python
_host_variable_warnings(self, cursor_specs: list[dict[str, object]]) -> list[str]
```

Observed calls (lexical order): `list`, `spec.get`, `warnings.append`, `DIAG_NO_HOST_VARIABLES_TEMPLATE.format`, `str`.

Control points:

- L381: `for spec in cursor_specs`
- L382: `if list(spec.get('host_variables', []) or [])`

### `CursorParagraphGenerator._insert_paragraph_block` - L395-L403

```python
_insert_paragraph_block(text: str, block: str) -> str
```

Place the block before END PROGRAM, else append at the end.

Observed calls (lexical order): `END_PROGRAM_PATTERN.search`, `match.start`, `text.rstrip`.

Control points:

- L399: `if match`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
