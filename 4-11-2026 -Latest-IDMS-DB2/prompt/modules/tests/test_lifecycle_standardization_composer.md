# `tests/test_lifecycle_standardization_composer.py`

Source: [tests/test_lifecycle_standardization_composer.py](../../../tests/test_lifecycle_standardization_composer.py) | 231 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `01a8fb2dfdb282bc80c125cdfedfd6518b61775504aa811080ca71f8d1997e4c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer
from converter.services.final_generated_output_service import FinalGeneratedOutputService
```

## Local dependency notes

- [converter/composers/lifecycle_standardization_composer.py](../converter/composers/lifecycle_standardization_composer.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)

## Symbol contracts and control points

### `_fixed` - L9-L10

```python
_fixed(seq: int, body: str, indicator: str=' ') -> str
```

### `_flat_cursor_program` - L13-L114

```python
_flat_cursor_program() -> str
```

Observed calls (lexical order): `_fixed`, `'\n'.join`.

### `test_lifecycle_standardization_moves_flat_cursor_loop_to_standard_wrappers` - L117-L144

```python
test_lifecycle_standardization_moves_flat_cursor_loop_to_standard_wrappers()
```

Observed calls (lexical order): `_flat_cursor_program`, `LifecycleStandardizationComposer`, `composer.compose`, `output.index`, `any`.

### `test_lifecycle_standardization_is_idempotent_for_standardized_output` - L147-L150

```python
test_lifecycle_standardization_is_idempotent_for_standardized_output()
```

Observed calls (lexical order): `FinalGeneratedOutputService`, `FinalGeneratedOutputService().apply`, `_flat_cursor_program`, `LifecycleStandardizationComposer`, `composer.compose`.

### `test_lifecycle_standardization_preserves_nested_cursor_work_verbatim` - L153-L167

```python
test_lifecycle_standardization_preserves_nested_cursor_work_verbatim()
```

Observed calls (lexical order): `_flat_cursor_program`, `_fixed`, `source.replace`, `LifecycleStandardizationComposer`, `composer.compose`, `output.index`.

### `test_lifecycle_standardization_fails_closed_on_unresolved_numbered_target` - L170-L177

```python
test_lifecycle_standardization_fails_closed_on_unresolved_numbered_target()
```

Observed calls (lexical order): `_flat_cursor_program`, `_flat_cursor_program().replace`, `_fixed`, `LifecycleStandardizationComposer`, `composer.compose`, `any`.

### `test_real_vmdz7200_output_standardizes_without_breaking_fixed_format` - L180-L193

```python
test_real_vmdz7200_output_standardizes_without_breaking_fixed_format()
```

Observed calls (lexical order): `Path`, `path.exists`, `FinalGeneratedOutputService`, `path.read_text`, `service.apply`, `all`, `len`, `output.splitlines`.

Control points:

- L182: `if not path.exists()`

### `test_generic_cursor_bounded_flow_standardizes_vmdz4420_without_rewriting_business_logic` - L196-L221

```python
test_generic_cursor_bounded_flow_standardizes_vmdz4420_without_rewriting_business_logic()
```

Observed calls (lexical order): `Path`, `path.exists`, `path.read_text`, `FinalGeneratedOutputService`, `service.apply`, `output.index`, `all`, `len`, `output.splitlines`.

Control points:

- L198: `if not path.exists()`

### `test_generic_cursor_bounded_flow_is_idempotent` - L224-L231

```python
test_generic_cursor_bounded_flow_is_idempotent()
```

Observed calls (lexical order): `Path`, `path.exists`, `FinalGeneratedOutputService`, `path.read_text`, `service.apply`.

Control points:

- L226: `if not path.exists()`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
