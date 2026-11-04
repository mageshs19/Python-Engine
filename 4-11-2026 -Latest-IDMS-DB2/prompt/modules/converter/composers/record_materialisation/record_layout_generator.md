# `converter/composers/record_materialisation/record_layout_generator.py`

Source: [converter/composers/record_materialisation/record_layout_generator.py](../../../../../converter/composers/record_materialisation/record_layout_generator.py) | 190 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `87bec8089a5f23decbab00716590d9b6bd8202fed1cb8eeeca62e00ec482bcee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Renders the materialised record as COBOL data description entries.

## Module-level bindings

`COMMENT_INDICATOR` (L47), `RECORD_GROUP_DEPTH` (L48), `FIELD_DEPTH_OFFSET` (L49), `__all__` (L190)

## Import declarations

```python
from __future__ import annotations
from converter.composers.record_materialisation.record_entry_renderer import RecordEntryRenderer
from converter.composers.record_materialisation.record_layout_geometry import RecordLayoutGeometry
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
from converter.composers.record_materialisation.record_redefines_renderer import RecordRedefinesRenderer
from rules.record_materialisation_rules import EMIT_REMAINDER_FILLER, LAYOUT_MARKER_TEMPLATE, RECORD_GROUP_LEVEL_STEP, REMAINDER_FILLER_NAME, REMAINDER_FILLER_PICTURE_TEMPLATE
```

## Local dependency notes

- [converter/composers/record_materialisation/record_entry_renderer.py](record_entry_renderer.md)
- [converter/composers/record_materialisation/record_layout_geometry.py](record_layout_geometry.md)
- [converter/composers/record_materialisation/record_plan.py](record_plan.md)
- [converter/composers/record_materialisation/record_redefines_renderer.py](record_redefines_renderer.md)
- [rules/record_materialisation_rules.py](../../../rules/record_materialisation_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/generated_fields/test_db2_code_fixes.py](../../../tests/generated_fields/test_db2_code_fixes.md)
- [tests/generated_fields/test_record_comp3_preservation.py](../../../tests/generated_fields/test_record_comp3_preservation.md)
- [tests/test_db2_code_fixes.py](../../../tests/test_db2_code_fixes.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordLayoutGenerator` - L52-L187

```python
class RecordLayoutGenerator()
```

Builds the COBOL body lines for a materialised record.

### `RecordLayoutGenerator.__init__` - L55-L64

```python
__init__(self, *, geometry: RecordLayoutGeometry | None=None, entries: RecordEntryRenderer | None=None, redefines: RecordRedefinesRenderer | None=None) -> None
```

Observed calls (lexical order): `RecordLayoutGeometry`, `RecordEntryRenderer`, `RecordRedefinesRenderer`.

### `RecordLayoutGenerator.generate` - L69-L109

```python
generate(self, plan: RecordMaterialisationPlan, *, base_level: int=0, base_indent: str='') -> list[str]
```

Body lines only. The caller applies the fixed-format frame.

Observed calls (lexical order): `self.geometry.root`, `int`, `LAYOUT_MARKER_TEMPLATE.format`, `self.group_line`, `self.geometry.shift`, `self.geometry.depth`, `lines.extend`, `self._entry`.

Control points:

- L83: `if not fields`
- L103: `for item in fields`

### `RecordLayoutGenerator.remainder_line` - L111-L138

```python
remainder_line(self, *, level: int, byte_count: int, base_indent: str='') -> list[str]
```

CORRECTION 3. FILLER for the unused tail of the target field.

Observed calls (lexical order): `int`, `self.geometry.root`, `REMAINDER_FILLER_PICTURE_TEMPLATE.format`, `self.entries.elementary`, `self.geometry.clamp`, `self.geometry.indent_text`.

Control points:

- L122: `if not EMIT_REMAINDER_FILLER`
- L124: `if not byte_count or int(byte_count) <= 0`

### `RecordLayoutGenerator.group_line` - L140-L153

```python
group_line(self, *, level: int, name: str, base_indent: str='', depth: int=0) -> str
```

Observed calls (lexical order): `self.geometry.root`, `self.entries.group`, `self.geometry.clamp`, `self.geometry.indent_text`.

### `RecordLayoutGenerator._entry` - L158-L187

```python
_entry(self, item, level: str, root: str, depth: int) -> list[str]
```

Observed calls (lexical order): `self.geometry.indent_text`, `self.entries.record_picture_of`, `self.redefines.render`, `self.entries.group`, `self.entries.elementary`.

Control points:

- L162: `if item.is_redefinition`
- L171: `if item.is_group`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
