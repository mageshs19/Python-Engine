# `converter/composers/record_materialisation/record_row_reader.py`

Source: [converter/composers/record_materialisation/record_row_reader.py](../../../../../converter/composers/record_materialisation/record_row_reader.py) | 158 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `5894df1de13382d8414ed35dc04289909a4b8f8028cdcb97d266f7e9617c8ebe`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Turns one Sheet Mapping row into a RecordFieldPlan.

## Module-level bindings

`COUNTED_SYMBOLS` (L35), `__all__` (L158)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_field import COMP_3_SYMBOL, DEFAULT_LEVEL, RecordFieldPlan
from patterns.record_materialisation_patterns import COBOL_ZONE_PATTERN, COBOL_ZONE_REDEFINES_PATTERN, PICTURE_PATTERN, PICTURE_SYMBOL_PATTERN
from rules.record_materialisation_rules import GROUP_PICTURE_TOKENS
```

## Local dependency notes

- [converter/composers/record_materialisation/record_field.py](record_field.md)
- [patterns/record_materialisation_patterns.py](../../../patterns/record_materialisation_patterns.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [converter/composers/record_materialisation/record_plan_builder.py](record_plan_builder.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordRowReader` - L38-L155

```python
class RecordRowReader()
```

Reads Sheet Mapping rows. Resolves nothing, decides nothing.

### `RecordRowReader.read` - L42-L70

```python
read(self, row) -> RecordFieldPlan | None
```

A field, or None when the row declares no COBOL storage.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(row, 'cobol_zone', '') or '').strip`, `self._split_zone`, `self.picture`, `RecordFieldPlan`, `str(level).strip`, `str(level).strip().zfill`, `self.column`, `self.declared_bytes`.

Control points:

- L50: `if not zone`
- L54: `if not name`

### `RecordRowReader._split_zone` - L74-L92

```python
_split_zone(zone: str) -> tuple[str, str, str]
```

'05 CT-RK-TGOOD REDEFINES CT-RK-TGDSV' -> (level, name, base).

Observed calls (lexical order): `COBOL_ZONE_REDEFINES_PATTERN.match`, `redefines.group`, `redefines.group('name').upper`, `redefines.group('base').upper`, `COBOL_ZONE_PATTERN.match`, `plain.group`, `plain.group('name').upper`.

Control points:

- L77: `if redefines`
- L85: `if not plain`

### `RecordRowReader.picture` - L96-L109

```python
picture(clause: str) -> tuple[str, str]
```

'PIC S9(13)V99 COMP-3' -> ('PIC S9(13)V99', 'COMP-3').

Observed calls (lexical order): `str`, `str(clause or '').strip`, `str(clause or '').strip().upper`, `PICTURE_PATTERN.search`, `match.group`, `str(match.group('usage') or '').strip`.

Control points:

- L99: `if not text or text in GROUP_PICTURE_TOKENS`
- L103: `if not match`

### `RecordRowReader.column` - L113-L118

```python
column(row) -> str
```

Observed calls (lexical order): `str`, `str(getattr(row, 'new_db2_field_name', '') or getattr(row, 'cross_application_db2_field_name', '') or '').s...`, `getattr`.

### `RecordRowReader.declared_bytes` - L122-L129

```python
declared_bytes(cls, row, picture: str, usage: str) -> int
```

The sheet's length column, or the PICTURE when it is blank.

Observed calls (lexical order): `str`, `str(getattr(row, 'length_of_field_bytes', '') or '').strip`, `getattr`, `declared.isdigit`, `int`, `cls.picture_bytes`.

Control points:

- L127: `if declared.isdigit()`

### `RecordRowReader.picture_bytes` - L132-L155

```python
picture_bytes(picture: str, usage: str='') -> int
```

Character positions of a PICTURE, honouring repeat counts.

Observed calls (lexical order): `str`, `str(picture or '').upper`, `PICTURE_SYMBOL_PATTERN.finditer`, `found.group`, `str(found.group('symbol') or '').upper`, `int`, `repeat.isdigit`, `str(usage or '').upper`.

Control points:

- L140: `if not text`
- L144: `for found in PICTURE_SYMBOL_PATTERN.finditer(text)`
- L146: `if symbol not in COUNTED_SYMBOLS`
- L151: `if not digits`
- L153: `if COMP_3_SYMBOL in str(usage or '').upper()`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
