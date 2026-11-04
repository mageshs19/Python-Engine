# `tests/generated_fields/test_record_comp3_preservation.py`

Source: [tests/generated_fields/test_record_comp3_preservation.py](../../../../tests/generated_fields/test_record_comp3_preservation.py) | 60 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `78a2c81ac55b829f0fadf0e363a518fd6607ef34f221119381228142540bf4d3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from types import SimpleNamespace
from converter.composers.record_materialisation.record_entry_renderer import RecordEntryRenderer
from converter.composers.record_materialisation.record_field import RecordFieldPlan
from converter.composers.record_materialisation.record_layout_generator import RecordLayoutGenerator
from converter.composers.record_materialisation.record_plan import RecordMaterialisationPlan
```

## Local dependency notes

- [converter/composers/record_materialisation/record_entry_renderer.py](../../converter/composers/record_materialisation/record_entry_renderer.md)
- [converter/composers/record_materialisation/record_field.py](../../converter/composers/record_materialisation/record_field.md)
- [converter/composers/record_materialisation/record_layout_generator.py](../../converter/composers/record_materialisation/record_layout_generator.md)
- [converter/composers/record_materialisation/record_plan.py](../../converter/composers/record_materialisation/record_plan.md)

## Symbol contracts and control points

### `test_record_layout_preserves_comp3_and_does_not_add_value_zeroes` - L8-L16

```python
test_record_layout_preserves_comp3_and_does_not_add_value_zeroes()
```

Observed calls (lexical order): `SimpleNamespace`, `RecordEntryRenderer.record_picture_of`.

### `test_record_layout_preserves_numeric_display_without_value_clause` - L19-L27

```python
test_record_layout_preserves_numeric_display_without_value_clause()
```

Observed calls (lexical order): `SimpleNamespace`, `RecordEntryRenderer.record_picture_of`.

### `test_existing_work_field_normalization_is_unchanged` - L30-L38

```python
test_existing_work_field_normalization_is_unchanged()
```

Observed calls (lexical order): `SimpleNamespace`, `RecordEntryRenderer.picture_of`.

### `test_record_layout_generator_uses_storage_preserving_picture_renderer` - L41-L60

```python
test_record_layout_generator_uses_storage_preserving_picture_renderer()
```

Observed calls (lexical order): `RecordMaterialisationPlan`, `RecordFieldPlan`, `'\n'.join`, `RecordLayoutGenerator`, `RecordLayoutGenerator().generate`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
