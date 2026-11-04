# `converter/domain/models.py`

Source: [converter/domain/models.py](../../../../converter/domain/models.py) | 234 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `b95afcb43112b4ed5ce04bd860f927c879cebcd098c4521f3540ce171c9d61cd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Domain models shared by parsers, repositories, resolvers and the UI.

## Module-level bindings

`__all__` (L217)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
```

## Importers (55)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/metadata_service.py](../analyzers/metadata_service.md)
- [converter/analyzers/program_flow/flow_cursor_loop_scanner.py](../analyzers/program_flow/flow_cursor_loop_scanner.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](../analyzers/program_flow/program_flow_analyzer.md)
- [converter/generators/cursor_paragraph_generator.py](../generators/cursor_paragraph_generator.md)
- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](../generators/db2_infrastructure/spec_builder/cursor_spec_builder.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_build_context.py](../generators/db2_infrastructure/spec_builder/spec_build_context.md)
- [converter/generators/db2_infrastructure/spec_builder/spec_navigation_scanner.py](../generators/db2_infrastructure/spec_builder/spec_navigation_scanner.md)
- [converter/generators/db2_infrastructure_generator.py](../generators/db2_infrastructure_generator.md)
- [converter/parsers/cobol_parser.py](../parsers/cobol_parser.md)
- [converter/parsers/copybook_parser.py](../parsers/copybook_parser.md)
- [converter/parsers/dclgen/dclgen_column_merger.py](../parsers/dclgen/dclgen_column_merger.md)
- [converter/parsers/dclgen_parser.py](../parsers/dclgen_parser.md)
- [tests/conftest.py](../../tests/conftest.md)
- [tests/test_conversion_result_production_gate.py](../../tests/test_conversion_result_production_gate.md)
- [tests/test_field_reference_group_issue_scope.py](../../tests/test_field_reference_group_issue_scope.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)
- [tests/test_generic_unused_copybook_and_group_move.py](../../tests/test_generic_unused_copybook_and_group_move.md)
- [tests/test_handwritten_obtain_calc_planner.py](../../tests/test_handwritten_obtain_calc_planner.md)
- [tests/test_imports.py](../../tests/test_imports.md)
- [tests/test_lrf_intermediate_artifact.py](../../tests/test_lrf_intermediate_artifact.md)
- [tests/test_lrf_key_binding_planner.py](../../tests/test_lrf_key_binding_planner.md)
- [tests/test_lrf_keyword_scope_safety.py](../../tests/test_lrf_keyword_scope_safety.md)
- [tests/test_lrf_select_projection_analysis.py](../../tests/test_lrf_select_projection_analysis.md)
- 31 further importers are recorded in [the source manifest](../../../source_manifest.json).

## Symbol contracts and control points

### `SheetMappingRow` - L60-L79

```python
class SheetMappingRow()
```

Declared class/data-model fields:

```python
cobol_record_idms: str = ''
cobol_zone: str = ''
idms_key: str = ''
idms_pic_clause: str = ''
length_of_field_bytes: str = ''
field_end_position: str = ''
db2_key: str = ''
new_db2_record: str = ''
new_db2_field_name: str = ''
new_db2_data_type: str = ''
hopex_expression_type_remark: str = ''
remarks: str = ''
relation: str = ''
reference_field_name_copybook: str = ''
reference_field_pic_clause: str = ''
cross_application_db2_table: str = ''
cross_application_db2_field_name: str = ''
cross_application_db2_data_type: str = ''
basetype: str = ''
```

### `DclgenColumn` - L83-L90

```python
class DclgenColumn()
```

Declared class/data-model fields:

```python
table_name: str = ''
column_name: str = ''
db2_type: str = ''
cobol_host_name: str = ''
cobol_picture: str = ''
cobol_usage: str = ''
nullable: bool = True
```

### `CopybookField` - L94-L100

```python
class CopybookField()
```

Declared class/data-model fields:

```python
level: str = ''
name: str = ''
picture: str = ''
usage: str = ''
occurs: str = ''
redefines: str = ''
```

### `IdmsOperation` - L109-L114

```python
class IdmsOperation()
```

Declared class/data-model fields:

```python
operation: str
record_name: str = ''
set_name: str = ''
line_number: int = 0
raw_line: str = ''
```

### `RelationshipSummary` - L123-L128

```python
class RelationshipSummary()
```

Declared class/data-model fields:

```python
relation: str = ''
parent_record: str = ''
child_record: str = ''
parent_key: str = ''
child_key: str = ''
```

### `RecordSummary` - L132-L136

```python
class RecordSummary()
```

Declared class/data-model fields:

```python
record_name: str
db2_table: str
column_count: int
key_columns: list[str] = field(default_factory=list)
```

### `LrfPathCommand` - L148-L158

```python
class LrfPathCommand()
```

One command line inside a SELECT FOR KEYWORD block.

Declared class/data-model fields:

```python
verb: str = ''
scope: str = ''
record_name: str = ''
within_name: str = ''
where_clause: str = ''
status_actions: dict[str, str] = field(default_factory=dict)
line_number: int = 0
raw_line: str = ''
```

### `LrfPath` - L162-L168

```python
class LrfPath()
```

One SELECT FOR KEYWORD block.

Declared class/data-model fields:

```python
keyword: str = ''
path_group_verb: str = ''
logical_record: str = ''
commands: list[LrfPathCommand] = field(default_factory=list)
```

### `LogicalRecord` - L172-L180

```python
class LogicalRecord()
```

One ADD LOGICAL RECORD block plus every path that serves it.

Declared class/data-model fields:

```python
logical_record_name: str = ''
element_records: list[str] = field(default_factory=list)
comments: list[str] = field(default_factory=list)
paths: list[LrfPath] = field(default_factory=list)
subschema_name: str = ''
schema_name: str = ''
```

### `ConversionInput` - L191-L199

```python
class ConversionInput()
```

Declared class/data-model fields:

```python
sheet_mapping_rows: list[SheetMappingRow] = field(default_factory=list)
dclgen_columns: list[DclgenColumn] = field(default_factory=list)
copybook_fields: list[CopybookField] = field(default_factory=list)
source_copybook_members: dict[str, str] = field(default_factory=dict)
logical_records: list[LogicalRecord] = field(default_factory=list)
idms_cobol_text: str = ''
target_program_id: str = ''
auto_fix_pic_length_mismatches: bool = False
```

### `ConversionResult` - L203-L214

```python
class ConversionResult()
```

Declared class/data-model fields:

```python
converted_cobol: str = ''
validation_messages: list[str] = field(default_factory=list)
operations: list[IdmsOperation] = field(default_factory=list)
```

### `ConversionResult.production_blocked` - L209-L214

```python
production_blocked(self) -> bool
```

Whether a safety gate explicitly refused production promotion.

Observed calls (lexical order): `any`, `str`, `str(message or '').startswith`.

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
