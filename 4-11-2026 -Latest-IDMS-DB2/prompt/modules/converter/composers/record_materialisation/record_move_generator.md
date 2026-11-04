# `converter/composers/record_materialisation/record_move_generator.py`

Source: [converter/composers/record_materialisation/record_move_generator.py](../../../../../converter/composers/record_materialisation/record_move_generator.py) | 97 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `c33c9ad22195e783626a0fd2b2a19dfb90293a65776258949392376de44c96ca`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders the field-by-field population of a materialised record.

## Module-level bindings

`__all__` (L97)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_field_plan import RecordMaterialisationPlan
from rules.record_materialisation_rules import DATE_CONVERSION_LINE_TEMPLATES, DATE_HIGH_NUMERIC_LITERAL, DATE_HIGH_VALUE_LITERAL, DATE_LOW_VALUE_LITERAL, EMIT_DATE_CONVERSION, MOVE_CONTINUATION_INDENT, MOVE_INLINE_LIMIT, MOVE_MARKER_TEMPLATE, MOVE_TARGET_TEMPLATE, MOVE_TEMPLATE
```

## Local dependency notes

- [converter/composers/record_materialisation/record_field_plan.py](record_field_plan.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordMoveGenerator` - L41-L94

```python
class RecordMoveGenerator()
```

Builds the MOVE block that populates the materialised record.

### `RecordMoveGenerator.generate` - L44-L64

```python
generate(self, plan: RecordMaterialisationPlan) -> list[str]
```

Body lines only. The caller applies indent and the frame.

Observed calls (lexical order): `MOVE_MARKER_TEMPLATE.format`, `len`, `lines.extend`, `self._date_block`, `self._simple_move`.

Control points:

- L47: `if not fields`
- L58: `for item in fields`
- L59: `if EMIT_DATE_CONVERSION and item.is_date`

### `RecordMoveGenerator._simple_move` - L68-L80

```python
_simple_move(record: str, item) -> list[str]
```

One line when it fits; head + indented continuation otherwise.

Observed calls (lexical order): `MOVE_TEMPLATE.format`, `MOVE_TARGET_TEMPLATE.format`, `MOVE_TARGET_TEMPLATE.format(field=item.name, record=record).strip`, `len`.

Control points:

- L77: `if len(single) <= MOVE_INLINE_LIMIT`

### `RecordMoveGenerator._date_block` - L83-L94

```python
_date_block(record: str, item) -> list[str]
```

Observed calls (lexical order): `template.format`.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
