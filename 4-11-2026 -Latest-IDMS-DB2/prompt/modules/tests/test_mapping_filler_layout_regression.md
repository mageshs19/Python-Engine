# `tests/test_mapping_filler_layout_regression.py`

Source: [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.py) | 111 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `6c9c3e82eb6e0abd34411aac975737df5acfa11900e33ac19a027ce82e7ccf2e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression: mapping-defined FILLER rows must survive record expansion.

## Module-level bindings

`PROJECT_ROOT` (L17), `MAPPING_PATH` (L19)

## Import declarations

```python
from pathlib import Path
from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
from converter.composers.record_materialisation.record_row_reader import RecordRowReader
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from tests.workspace_fixtures import mapping_export
from rules.record_materialisation_rules import EMIT_REMAINDER_FILLER
from converter.composers.record_materialisation.record_field import RecordFieldPlan
from converter.composers.record_materialisation.record_materialisation_guard import RecordMaterialisationGuard
from converter.composers.record_materialisation.record_block_writer import RecordBlockWriter
from converter.composers.record_materialisation.record_move_generator import RecordMoveGenerator
from converter.composers.record_materialisation.record_line_utils import RecordLineUtils
```

## Local dependency notes

- [converter/composers/record_materialisation/record_block_writer.py](../converter/composers/record_materialisation/record_block_writer.md)
- [converter/composers/record_materialisation/record_field.py](../converter/composers/record_materialisation/record_field.md)
- [converter/composers/record_materialisation/record_layout_generator.py](../converter/composers/record_materialisation/record_layout_generator.md)
- [converter/composers/record_materialisation/record_line_utils.py](../converter/composers/record_materialisation/record_line_utils.md)
- [converter/composers/record_materialisation/record_materialisation_guard.py](../converter/composers/record_materialisation/record_materialisation_guard.md)
- [converter/composers/record_materialisation/record_move_generator.py](../converter/composers/record_materialisation/record_move_generator.md)
- [converter/composers/record_materialisation/record_plan.py](../converter/composers/record_materialisation/record_plan.md)
- [converter/composers/record_materialisation/record_row_reader.py](../converter/composers/record_materialisation/record_row_reader.md)
- [converter/parsers/sheet_mapping_parser.py](../converter/parsers/sheet_mapping_parser.md)
- [rules/record_materialisation_rules.py](../rules/record_materialisation_rules.md)
- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `_mapped_vmbfas_x14_filler` - L22-L33

```python
_mapped_vmbfas_x14_filler()
```

Observed calls (lexical order): `SheetMappingParser`, `SheetMappingParser().parse_csv_text`, `MAPPING_PATH.read_text`, `next`, `row.cobol_record_idms.strip`, `row.cobol_record_idms.strip().upper`, `' '.join`, `' '.join(row.cobol_zone.split()).upper`, `row.cobol_zone.split`, `row.idms_pic_clause.strip`, `row.idms_pic_clause.strip().upper`, `RecordRowReader`, `RecordRowReader().read`.

### `test_mapping_filler_x14_is_emitted_in_vmbfas_expansion` - L36-L55

```python
test_mapping_filler_x14_is_emitted_in_vmbfas_expansion()
```

Observed calls (lexical order): `_mapped_vmbfas_x14_filler`, `RecordMaterialisationPlan`, `RecordLayoutGenerator`, `RecordLayoutGenerator().generate`, `'\n'.join`.

### `test_explicit_mapping_filler_is_not_suppressed_with_remainder_filler_disabled` - L58-L66

```python
test_explicit_mapping_filler_is_not_suppressed_with_remainder_filler_disabled()
```

Observed calls (lexical order): `_mapped_vmbfas_x14_filler`, `RecordMaterialisationPlan`, `len`.

### `test_full_sheet_mapping_preserves_original_record_byte_length` - L69-L91

```python
test_full_sheet_mapping_preserves_original_record_byte_length()
```

The sheet's 432-byte prefix must fit its 478-byte target exactly.

Observed calls (lexical order): `MAPPING_PATH.read_text`, `SheetMappingParser`, `SheetMappingParser().parse_csv_text`, `RecordRowReader`, `reader.read`, `row.cobol_record_idms.strip`, `row.cobol_record_idms.strip().upper`, `RecordMaterialisationPlan`, `plan.remainder_bytes`, `RecordMaterialisationGuard.check_length`, `RecordLayoutGenerator`, `RecordLayoutGenerator().remainder_line`, `len`.

### `test_filler_rendering_respects_fixed_format_columns` - L94-L111

```python
test_filler_rendering_respects_fixed_format_columns()
```

Observed calls (lexical order): `RecordFieldPlan`, `RecordMaterialisationPlan`, `RecordBlockWriter`, `RecordLayoutGenerator`, `RecordMoveGenerator`, `'000100 05 SAMPLE-AREA PIC X(36).'.ljust`, `writer.expand_target`, `len`, `all`, `filler[0].index`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
