# `tests/test_retrieval_handwritten_obtain_calc_safety.py`

Source: [tests/test_retrieval_handwritten_obtain_calc_safety.py](../../../tests/test_retrieval_handwritten_obtain_calc_safety.py) | 109 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `85dd03449ff863add9ad315245d9d512c69d24907c6839452dc50ba15a556c4e`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
```

## Local dependency notes

- [converter/validators/generated_cobol_release_validator.py](../converter/validators/generated_cobol_release_validator.md)

## Symbol contracts and control points

### `test_retrieval_handwritten_obtain_calc_is_not_silently_removed` - L4-L19

```python
test_retrieval_handwritten_obtain_calc_is_not_silently_removed(transformer_context)
```

Observed calls (lexical order): `set`, `transformer.transform_line`, `'\n'.join`, `any`.

### `test_release_gate_blocks_unconverted_handwritten_retrieval_obtain_calc` - L22-L28

```python
test_release_gate_blocks_unconverted_handwritten_retrieval_obtain_calc()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_update_obtain_calc_legacy_removal_is_unchanged` - L31-L43

```python
test_update_obtain_calc_legacy_removal_is_unchanged(transformer_context)
```

Observed calls (lexical order): `set`, `transformer.transform_line`, `'\n'.join`.

### `test_proven_handwritten_retrieval_calc_emits_keyed_select` - L46-L70

```python
test_proven_handwritten_retrieval_calc_emits_keyed_select(transformer_context)
```

Observed calls (lexical order): `set`, `transformer.transform_line`, `'\n'.join`.

### `test_handwritten_calc_status_guards_map_only_in_active_scope` - L73-L97

```python
test_handwritten_calc_status_guards_map_only_in_active_scope(transformer_context)
```

Observed calls (lexical order): `transformer.transform_line`.

### `test_handwritten_calc_status_scope_ends_before_next_idms_access` - L100-L109

```python
test_handwritten_calc_status_scope_ends_before_next_idms_access(transformer_context)
```

Observed calls (lexical order): `transformer.transform_line`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
