# `tests/output_write/test_perform_thru_helper_safety.py`

Source: [tests/output_write/test_perform_thru_helper_safety.py](../../../../tests/output_write/test_perform_thru_helper_safety.py) | 62 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `435b93108473a5c09ea20f71e0552dbb510dbd4375a07fcc7471c7026cf7d42d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
from converter.services.perform_thru_scope import perform_spans, paragraph_indices
```

## Local dependency notes

- [converter/composers/output_write_paragraph_composer.py](../../converter/composers/output_write_paragraph_composer.md)
- [converter/services/perform_thru_scope.py](../../converter/services/perform_thru_scope.md)
- [converter/validators/generated_cobol_release_validator.py](../../converter/validators/generated_cobol_release_validator.md)

## Symbol contracts and control points

### `fmt` - L6-L9

```python
fmt(text)
```

Observed calls (lexical order): `text.endswith`.

Control points:

- L7: `if text.endswith('DIVISION.') or (text.endswith('.') and ' ' not in text)`

### `source` - L12-L35

```python
source()
```

Observed calls (lexical order): `'\n'.join`, `map`.

### `test_extracted_paragraph_is_after_thru_exit_and_reset_per_record` - L38-L47

```python
test_extracted_paragraph_is_after_thru_exit_and_reset_per_record()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`, `source`, `code.splitlines`, `paragraph_indices`, `code.upper`, `code.upper().split`, `code.upper().split('WRITE-FORM-REC.')[1].split`, `helper.index`, `any`, `validate_generated_cobol`, `len`, `perform_spans`.

### `test_release_gate_rejects_unguarded_helper_inside_thru` - L50-L56

```python
test_release_gate_rejects_unguarded_helper_inside_thru()
```

Observed calls (lexical order): `source`, `source_text.replace`, `source_text.replace(fmt('BUSINESS-EXIT.'), '\n'.join([fmt('WRITE-FORM-REC.'), fmt('WRITE FORM-REC FROM REC-...`, `fmt`, `'\n'.join`, `any`, `validate_generated_cobol`.

### `test_no_duplicate_reset_without_proven_source_clear` - L59-L62

```python
test_no_duplicate_reset_without_proven_source_clear()
```

Observed calls (lexical order): `fmt`, `source`, `source().replace`, `OutputWriteParagraphComposer`, `OutputWriteParagraphComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
