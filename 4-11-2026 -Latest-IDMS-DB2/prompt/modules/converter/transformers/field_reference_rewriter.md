# `converter/transformers/field_reference_rewriter.py`

Source: [converter/transformers/field_reference_rewriter.py](../../../../converter/transformers/field_reference_rewriter.py) | 463 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `38d4f1120d24f9dfd507ba8b4c4b8fb6375b931ddf7e3d1fe5dbd960bc0f7f10`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`PROCEDURE_DIVISION_NAME` (L40), `BLANK_INDICATOR` (L41), `LINE_ENDINGS` (L42), `__all__` (L461)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.name_normalizer import NameNormalizer
from converter.composers.db2_date_condition_assembler import Db2DateConditionAssembler
from converter.repositories.mapping_repository import MappingRepository
from converter.resolvers.host_variable_resolver import HostVariableResolver
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.transformers.field_reference_context_builder import FieldReferenceContextBuilder
from converter.transformers.field_reference_line_utils import FieldReferenceLineUtils
from converter.transformers.field_reference_record_context import FieldReferenceRecordContext
from converter.transformers.field_reference_replacement_engine import FieldReferenceReplacementEngine
from patterns.field_reference_rewriter_patterns import DIVISION_PATTERN, END_EXEC_PATTERN, EXEC_SQL_PATTERN
from rules.field_reference_rewriter_rules import ALLOW_REWRITE_WRAPPING, ENFORCE_FIXED_FORMAT_REWRITE, FIELD_REFERENCE_GEOMETRY_MESSAGES
```

## Local dependency notes

- [converter/composers/db2_date_condition_assembler.py](../composers/db2_date_condition_assembler.md)
- [converter/repositories/mapping_repository.py](../repositories/mapping_repository.md)
- [converter/resolvers/host_variable_resolver.py](../resolvers/host_variable_resolver.md)
- [converter/resolvers/table_name_resolver.py](../resolvers/table_name_resolver.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)
- [converter/transformers/field_reference_context_builder.py](field_reference_context_builder.md)
- [converter/transformers/field_reference_line_utils.py](field_reference_line_utils.md)
- [converter/transformers/field_reference_record_context.py](field_reference_record_context.md)
- [converter/transformers/field_reference_replacement_engine.py](field_reference_replacement_engine.md)
- [patterns/field_reference_rewriter_patterns.py](../../patterns/field_reference_rewriter_patterns.md)
- [rules/field_reference_rewriter_rules.py](../../rules/field_reference_rewriter_rules.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)
- [tests/test_field_reference_geometry.py](../../tests/test_field_reference_geometry.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_transformers.py](../../tests/test_transformers.md)

## Symbol contracts and control points

### `FieldReferenceRewriter` - L45-L458

```python
class FieldReferenceRewriter()
```

Generic IDMS field reference to DB2 DCLGEN reference rewriter.

### `FieldReferenceRewriter.__init__` - L128-L155

```python
__init__(self, mapping_repository: MappingRepository, table_name_resolver: TableNameResolver, host_variable_resolver: HostVariableResolver, fixed_format: FixedFormatLineService | None=None, copybook_repository=None) -> None
```

Observed calls (lexical order): `FieldReferenceLineUtils`, `FixedFormatLineService`, `FieldReferenceContextBuilder`.

### `FieldReferenceRewriter._build_reference_maps` - L157-L165

```python
_build_reference_maps(self) -> None
```

Retained for any external caller. rewrite() does not need it.

Observed calls (lexical order): `self.context_builder.build_reference_maps`, `self.rewrite_messages.extend`.

### `FieldReferenceRewriter._unique_bare_maps` - L167-L212

```python
_unique_bare_maps(self, lines)
```

Resolve missing bare scalars only with unique ownership and no local shadow.

Observed calls (lexical order): `set`, `self.line_utils.logical_line`, `re.match`, `declared.add`, `match.group`, `match.group(1).upper`, `NameNormalizer.to_cobol`, `declared.update`, `self.copybook_repository.all`, `self.mapping_repository.all`, `NameNormalizer.normalize`, `owners.setdefault`, `owners.setdefault(field, set()).add`, `row.new_db2_field_name.strip`, `row.new_db2_field_name.strip().upper`, `row.new_db2_record.strip`.
Another 19 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L170: `for line in lines`
- L172: `if re.match('^PROCEDURE\\s+DIVISION', logical, re.I)`
- L175: `if match`
- L177: `if self.copybook_repository is not None`
- L182: `for row in rows`
- L184: `if match`
- L187: `if row.new_db2_field_name`
- L191: `for row in rows`
- Another 6 conditions/loops exist in this source span.

### `FieldReferenceRewriter.rewrite` - L217-L323

```python
rewrite(self, text: str) -> str
```

Observed calls (lexical order): `self.context_builder.build_reference_maps`, `self.rewrite_messages.extend`, `str`, `str(text or '').rstrip`, `str(text or '').splitlines`, `any`, `DIVISION_PATTERN.match`, `self.line_utils.logical_line`, `FieldReferenceRecordContext`, `FieldReferenceReplacementEngine`, `getattr`, `self._unique_bare_maps`, `Db2DateConditionAssembler`, `Db2DateConditionAssembler().spans`, `enumerate`, `raw_line.rstrip`.
Another 10 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L224: `if not text`
- L241: `if not self.record_field_map`
- L277: `for (line_index, raw_line) in enumerate(lines)`
- L287: `if division_match`
- L298: `if detected_context`
- L301: `if EXEC_SQL_PATTERN.match(logical)`
- L306: `if inside_exec_sql`
- L309: `if END_EXEC_PATTERN.match(logical)`

### `FieldReferenceRewriter._rewrite_line` - L328-L385

```python
_rewrite_line(self, *, line: str, current_division: str, active_record: str, replacement_engine: FieldReferenceReplacementEngine) -> list[str]
```

Rewrite one line. Returns one line, or several when wrapped.

Observed calls (lexical order): `self.line_utils.is_comment_or_blank`, `self._is_fixed`, `self._rewrite_text`, `self._split`, `self._build`, `self._wrap`, `self.rewrite_messages.append`, `FIELD_REFERENCE_GEOMETRY_MESSAGES['wrapped'].format`, `len`, `list`, `FIELD_REFERENCE_GEOMETRY_MESSAGES['refused'].format`, `new_body.strip`.

Control points:

- L337: `if self.line_utils.is_comment_or_blank(line)`
- L340: `if current_division != PROCEDURE_DIVISION_NAME`
- L343: `if not ENFORCE_FIXED_FORMAT_REWRITE or not self._is_fixed(line)`
- L360: `if new_body == body`
- L365: `if rebuilt is not None`
- L368: `if ALLOW_REWRITE_WRAPPING`
- L371: `if wrapped`

### `FieldReferenceRewriter._rewrite_text` - L387-L412

```python
_rewrite_text(self, *, text: str, active_record: str, replacement_engine: FieldReferenceReplacementEngine) -> str
```

Apply both rewrites to one span, string literals protected.

Observed calls (lexical order): `self.line_utils.split_string_segments`, `rewritten_segments.append`, `replacement_engine.rewrite_qualified_references`, `replacement_engine.rewrite_bare_references`, `replacement_engine.rewrite_unique_bare_references`, `''.join`.

Control points:

- L398: `for (segment, is_string) in segments`
- L399: `if is_string`

### `FieldReferenceRewriter._is_fixed` - L417-L421

```python
_is_fixed(self, line: str) -> bool
```

Observed calls (lexical order): `bool`, `self.fixed_format.is_fixed_line`.

### `FieldReferenceRewriter._split` - L423-L433

```python
_split(self, line: str) -> tuple[str, str, str, str]
```

Observed calls (lexical order): `self.fixed_format.split`, `str`.

### `FieldReferenceRewriter._build` - L435-L450

```python
_build(self, left: str, indicator: str, body: str, right: str) -> str | None
```

Observed calls (lexical order): `self.fixed_format.build_or_none`.

### `FieldReferenceRewriter._wrap` - L452-L458

```python
_wrap(self, line: str, body: str) -> list[str]
```

Observed calls (lexical order): `list`, `self.fixed_format.replace_body_wrapped`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
