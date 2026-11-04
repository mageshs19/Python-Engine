# `converter/generators/restart/restart_config.py`

Source: [converter/generators/restart/restart_config.py](../../../../../converter/generators/restart/restart_config.py) | 419 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `8232f921fc37befd726b89c7b9997f2fb0523113458ff6039266002f48cf5150`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Immutable configuration consumed by every restart builder.

## Module-level bindings

`__all__` (L415)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, replace
from typing import ClassVar, Mapping
from catalogs.restart_paragraph_catalog import PARAGRAPH_NAME_TEMPLATE, PARAGRAPH_SUFFIXES, QUERYNO_INSERT, QUERYNO_SELECT, QUERYNO_UPDATE, TABLE_PARAGRAPH_NAME_TEMPLATE, TABLE_SUFFIXED_ROLES, RestartDclgenRole
from rules.restart_standard_rules import COMMIT_TEST_THRESHOLD, DEFAULT_PARAGRAPH_SCHEME, DEFAULT_PHASE_NUMBER, ENFORCE_FULL_PAYLOAD_LENGTH_ON_COMMIT, PARAGRAPH_NUMBER_SCHEMES, REQUIRE_RETENTION_FROM_METADATA, RESTART_PARAGRAPH_ROLES, ROLE_ABEND, ROLE_COMMIT, ROLE_CONTROL, ROLE_INSERT, ROLE_RESTART_FOUND, ROLE_SELECT, ROLE_UPDATE, ROLE_WRITE_RESTART, SQLCODE_NOT_FOUND, SQLCODE_OK, STATUS_COMPLETE, STATUS_INCOMPLETE
from rules.restart_statement_templates import COMMIT_ERROR_MESSAGE, COMPLETE_RUN_MESSAGE
```

## Local dependency notes

- [catalogs/restart_paragraph_catalog.py](../../../catalogs/restart_paragraph_catalog.md)
- [rules/restart_standard_rules.py](../../../rules/restart_standard_rules.md)
- [rules/restart_statement_templates.py](../../../rules/restart_statement_templates.md)

## Importers (23)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/restart/legacy_restart_cleanup.py](../../composers/restart/legacy_restart_cleanup.md)
- [converter/composers/restart/process_paragraph_injector.py](../../composers/restart/process_paragraph_injector.md)
- [converter/composers/restart/restart_injection_composer.py](../../composers/restart/restart_injection_composer.md)
- [converter/composers/restart/restart_storage_injector.py](../../composers/restart/restart_storage_injector.md)
- [converter/generators/restart/read_paragraph_builder.py](read_paragraph_builder.md)
- [converter/generators/restart/restart_flow_builder.py](restart_flow_builder.md)
- [converter/generators/restart/restart_main_flow_builder.py](restart_main_flow_builder.md)
- [converter/generators/restart/restart_name_resolver.py](restart_name_resolver.md)
- [converter/generators/restart/restart_sql_builder.py](restart_sql_builder.md)
- [converter/generators/restart/restart_storage_builder.py](restart_storage_builder.md)
- [tests/restart/conftest.py](../../../tests/restart/conftest.md)
- [tests/restart/test_m10c_golden_output.py](../../../tests/restart/test_m10c_golden_output.md)
- [tests/restart/test_m11_storage_builder.py](../../../tests/restart/test_m11_storage_builder.md)
- [tests/restart/test_m11b_storage_injector.py](../../../tests/restart/test_m11b_storage_injector.md)
- [tests/restart/test_m2_restart_config.py](../../../tests/restart/test_m2_restart_config.md)
- [tests/restart/test_m3_name_resolver.py](../../../tests/restart/test_m3_name_resolver.md)
- [tests/restart/test_m4_sql_builder.py](../../../tests/restart/test_m4_sql_builder.md)
- [tests/restart/test_m5_flow_builder.py](../../../tests/restart/test_m5_flow_builder.md)
- [tests/restart/test_m5_storage_builder_derives_record.py](../../../tests/restart/test_m5_storage_builder_derives_record.md)
- [tests/restart/test_m6_main_flow_builder.py](../../../tests/restart/test_m6_main_flow_builder.md)
- [tests/restart/test_m7_process_injector.py](../../../tests/restart/test_m7_process_injector.md)
- [tests/restart/test_m8_read_paragraph.py](../../../tests/restart/test_m8_read_paragraph.md)
- 1 further importers are recorded in [the source manifest](../../../../source_manifest.json).

## Symbol contracts and control points

### `RestartProgramNames` - L140-L201

```python
class RestartProgramNames()
```

Names and measurements that belong to the program being converted.

Declared class/data-model fields:

```python
program_constant: str = ''
run_date_field: str = ''
file_name: str = ''
record_name: str = ''
read_paragraph: str = ''
process_paragraph: str = ''
eof_condition: str = ''
not_eof_condition: str = ''
input_counter: str = ''
commit_counter: str = ''
input_save_area: str = ''
restart_record: str = ''
restart_key_field: str = ''
read_count_field: str = ''
read_count_size: int = 0
restart_key_size: int = 0
error_paragraph: str = ''
abend_module: str = ''
REQUIRED: ClassVar[tuple[str, ...]] = ('program_constant', 'run_date_field', 'file_name', 'record_name', 'read_paragraph', 'process_paragraph', 'eof_condition', 'not_eof_condition', 'input_counter', 'commit_counter', 'input_save_area', 'restart_record', 'restart_key_field', 'read_count_field', 'r...
```

### `RestartProgramNames.missing` - L187-L198

```python
missing(self) -> tuple[str, ...]
```

Names and sizes the resolver could not establish.

Observed calls (lexical order): `getattr`, `isinstance`, `out.append`, `str`, `str(value).strip`, `tuple`.

Control points:

- L190: `for name in self.REQUIRED`
- L192: `if isinstance(value, int)`
- L193: `if value <= 0`
- L196: `if not str(value).strip()`

### `RestartProgramNames.is_complete` - L200-L201

```python
is_complete(self) -> bool
```

Observed calls (lexical order): `self.missing`.

### `build_paragraph_names` - L204-L229

```python
build_paragraph_names(role: RestartDclgenRole, scheme: str=DEFAULT_PARAGRAPH_SCHEME) -> dict[str, str]
```

Role -> paragraph name, for one numbering scheme.

Observed calls (lexical order): `TABLE_PARAGRAPH_NAME_TEMPLATE.format`, `PARAGRAPH_NAME_TEMPLATE.format`.

Control points:

- L212: `for role_key in RESTART_PARAGRAPH_ROLES`
- L216: `if role_key in TABLE_SUFFIXED_ROLES`

### `RestartConfig` - L233-L412

```python
class RestartConfig()
```

Everything the restart builders need, resolved and immutable.

Declared class/data-model fields:

```python
role: RestartDclgenRole
names: RestartProgramNames
paragraphs: Mapping[str, str]
scheme: str = DEFAULT_PARAGRAPH_SCHEME
phase_number: int = DEFAULT_PHASE_NUMBER
queryno_select: int = QUERYNO_SELECT
queryno_update: int = QUERYNO_UPDATE
queryno_insert: int = QUERYNO_INSERT
```

### `RestartConfig.build` - L252-L265

```python
build(cls, role: RestartDclgenRole, names: RestartProgramNames, scheme: str=DEFAULT_PARAGRAPH_SCHEME) -> 'RestartConfig'
```

Observed calls (lexical order): `ValueError`, `cls`, `build_paragraph_names`.

Control points:

- L258: `if scheme not in PARAGRAPH_NUMBER_SCHEMES`

Explicit raises: `ValueError(f'unknown paragraph scheme: {scheme!r}')`.

### `RestartConfig.with_names` - L267-L269

```python
with_names(self, names: RestartProgramNames) -> 'RestartConfig'
```

A copy carrying freshly resolved program names.

Observed calls (lexical order): `replace`.

### `RestartConfig.payload_full_length` - L276-L283

```python
payload_full_length(self) -> int
```

Sum of the two restart-record subfield pictures.

### `RestartConfig.payload_length` - L286-L305

```python
payload_length(self) -> int
```

The FLAG's choice. The decision is named once, here.

Control points:

- L303: `if ENFORCE_FULL_PAYLOAD_LENGTH_ON_COMMIT`

### `RestartConfig.payload_length_on_insert` - L308-L317

```python
payload_length_on_insert(self) -> int
```

The length written when the checkpoint ROW IS CREATED.

### `RestartConfig.payload_length_on_commit` - L320-L322

```python
payload_length_on_commit(self) -> int
```

The length every COMMIT writes. Reads the one decision.

### `RestartConfig.payload_length_is_full` - L325-L332

```python
payload_length_is_full(self) -> bool
```

True when a COMMIT persists the restart key as well.

### `RestartConfig.retention_days` - L335-L336

```python
retention_days(self) -> int
```

### `RestartConfig.paragraph` - L338-L339

```python
paragraph(self, role: str) -> str
```

### `RestartConfig.missing` - L341-L342

```python
missing(self) -> tuple[str, ...]
```

Observed calls (lexical order): `self.names.missing`.

### `RestartConfig.is_usable` - L344-L347

```python
is_usable(self) -> bool
```

Observed calls (lexical order): `self.names.is_complete`.

Control points:

- L345: `if REQUIRE_RETENTION_FROM_METADATA and self.retention_days <= 0`

### `RestartConfig.placeholders` - L353-L412

```python
placeholders(self) -> dict[str, object]
```

The single dictionary every template is rendered against.

Observed calls (lexical order): `self.paragraph`.

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
