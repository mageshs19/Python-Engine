# `converter/composers/record_materialisation/record_field.py`

Source: [converter/composers/record_materialisation/record_field.py](../../../../../converter/composers/record_materialisation/record_field.py) | 162 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `88e9122836d2a1491e608263f7e6b8e795ef09f8c415729cf17303ad3a95fd36`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> One COBOL data description entry of a materialised record.

## Module-level bindings

`DEFAULT_LEVEL` (L51), `COMP_3_SYMBOL` (L52), `__all__` (L162)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.record_materialisation_rules import DATE_DB2_TYPE_PREFIX, FILLER_FIELD_NAMES, NON_COLUMN_SENTINELS, NON_DATE_DB2_TYPE_PREFIXES
```

## Local dependency notes

- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (7)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation/record_plan.py](record_plan.md)
- [converter/composers/record_materialisation/record_row_reader.py](record_row_reader.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/generated_fields/test_record_comp3_preservation.py](../../../tests/generated_fields/test_record_comp3_preservation.md)
- [tests/test_db2_code_fixes.py](../../../tests/test_db2_code_fixes.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordFieldPlan` - L56-L159

```python
class RecordFieldPlan()
```

One COBOL data description entry of the materialised record.

Declared class/data-model fields:

```python
level: str = DEFAULT_LEVEL
name: str = ''
picture: str = ''
usage: str = ''
redefines: str = ''
db2_column: str = ''
db2_type: str = ''
host_reference: str = ''
declared_bytes: int = 0
```

### `RecordFieldPlan.is_group` - L73-L74

```python
is_group(self) -> bool
```

### `RecordFieldPlan.is_filler` - L77-L79

```python
is_filler(self) -> bool
```

Shape 5. Occupies bytes, carries no data.

Observed calls (lexical order): `str`, `str(self.name or '').strip`, `str(self.name or '').strip().upper`.

### `RecordFieldPlan.is_redefinition` - L82-L83

```python
is_redefinition(self) -> bool
```

Observed calls (lexical order): `bool`.

### `RecordFieldPlan.has_db2_column` - L87-L95

```python
has_db2_column(self) -> bool
```

CORRECTION C.

Observed calls (lexical order): `str`, `str(self.db2_column or '').strip`, `str(self.db2_column or '').strip().upper`.

### `RecordFieldPlan.is_date` - L98-L102

```python
is_date(self) -> bool
```

Observed calls (lexical order): `str`, `str(self.db2_type or '').upper`, `str(self.db2_type or '').upper().replace`, `compact.startswith`.

Control points:

- L100: `if compact.startswith(NON_DATE_DB2_TYPE_PREFIXES)`

### `RecordFieldPlan.requires_host` - L106-L116

```python
requires_host(self) -> bool
```

CORRECTION B.

Control points:

- L114: `if self.is_filler or self.is_redefinition`

### `RecordFieldPlan.is_missing_host` - L119-L120

```python
is_missing_host(self) -> bool
```

### `RecordFieldPlan.is_declarable` - L123-L125

```python
is_declarable(self) -> bool
```

Every shape except 7 occupies storage and must be declared.

Observed calls (lexical order): `bool`.

### `RecordFieldPlan.is_movable` - L128-L146

```python
is_movable(self) -> bool
```

CORRECTION D.

Observed calls (lexical order): `bool`.

Control points:

- L140: `if self.is_redefinition`
- L142: `if self.is_filler`
- L144: `if not self.has_db2_column`

### `RecordFieldPlan.occupies_storage` - L149-L159

```python
occupies_storage(self) -> bool
```

Bytes are counted once, on elementary items only.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
