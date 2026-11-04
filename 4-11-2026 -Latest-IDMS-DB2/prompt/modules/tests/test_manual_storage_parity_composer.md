# `tests/test_manual_storage_parity_composer.py`

Source: [tests/test_manual_storage_parity_composer.py](../../../tests/test_manual_storage_parity_composer.py) | 208 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b6d3dd35e7bf2958f20911c173331cf1f37dd549265ec12d1e1a8598f1952430`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.manual_storage_parity_composer import ManualStorageParityComposer
from tests.workspace_fixtures import generated_program
from pathlib import Path
from converter.services.final_generated_output_service import FinalGeneratedOutputService
from converter.services.program_constant_normalizer import ProgramConstantNormalizer
```

## Local dependency notes

- [converter/composers/manual_storage_parity_composer.py](../converter/composers/manual_storage_parity_composer.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)
- [converter/services/program_constant_normalizer.py](../converter/services/program_constant_normalizer.md)
- [tests/workspace_fixtures.py](workspace_fixtures.md)

## Symbol contracts and control points

### `test_manual_storage_pass_does_not_coerce_field_usage_or_reparent_groups` - L5-L22

```python
test_manual_storage_pass_does_not_coerce_field_usage_or_reparent_groups()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_cursor_with_hold_removed_when_no_transaction_boundary_spans_cursor` - L25-L36

```python
test_cursor_with_hold_removed_when_no_transaction_boundary_spans_cursor()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_unrelated_storage_is_unchanged` - L39-L41

```python
test_unrelated_storage_is_unchanged()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_cursor_hold_is_retained_only_when_transaction_occurs_between_open_and_close` - L44-L56

```python
test_cursor_hold_is_retained_only_when_transaction_occurs_between_open_and_close()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `composer.compose`.

### `test_existing_ws_var_and_counter_declarations_are_never_silently_reordered` - L59-L73

```python
test_existing_ws_var_and_counter_declarations_are_never_silently_reordered()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_program_constant_is_normalized_to_generic_cs_program_for_any_program` - L76-L86

```python
test_program_constant_is_normalized_to_generic_cs_program_for_any_program()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_program_constant_uses_existing_shared_cs_program_and_removes_duplicate` - L89-L99

```python
test_program_constant_uses_existing_shared_cs_program_and_removes_duplicate()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`, `result.count`.

### `test_program_constant_does_not_rename_unrelated_cs_field` - L102-L109

```python
test_program_constant_does_not_rename_unrelated_cs_field()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_real_vmdz7200_manual_cursor_policy_matches_reference` - L112-L123

```python
test_real_vmdz7200_manual_cursor_policy_matches_reference()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `generated_program`, `generated_program('VMDZ7200').read_text`, `(root / 'mainframe/workspace/Manual Output/VMDZ7200.cbl').read_text`, `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_real_vmdz4310_storage_normalizer_is_idempotent` - L126-L134

```python
test_real_vmdz4310_storage_normalizer_is_idempotent()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `generated_program`, `generated_program('VMDZ4310').read_text`, `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_vmdz4310_helper_keeps_untrusted_key_alphanumeric_until_validation` - L137-L159

```python
test_vmdz4310_helper_keeps_untrusted_key_alphanumeric_until_validation()
```

Observed calls (lexical order): `ManualStorageParityComposer`, `ManualStorageParityComposer().compose`.

### `test_final_output_service_removes_redundant_program_constant_generically` - L162-L175

```python
test_final_output_service_removes_redundant_program_constant_generically()
```

Observed calls (lexical order): `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `result.count`.

### `test_generic_program_constant_normalizer_preserves_unrelated_constants` - L178-L192

```python
test_generic_program_constant_normalizer_preserves_unrelated_constants()
```

Observed calls (lexical order): `ProgramConstantNormalizer.normalize`, `result.count`.

### `test_generic_program_constant_normalizer_collapses_multiple_aliases` - L195-L208

```python
test_generic_program_constant_normalizer_collapses_multiple_aliases()
```

Observed calls (lexical order): `ProgramConstantNormalizer.normalize`, `result.count`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
