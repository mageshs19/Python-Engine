# `tests/test_generated_cobol_release_validator.py`

Source: [tests/test_generated_cobol_release_validator.py](../../../tests/test_generated_cobol_release_validator.py) | 170 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `5159580b6a0f26dd8ac5e3eb8c98d33be5412958dd65dbd0172178b82bc65e72`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L5)

## Import declarations

```python
from pathlib import Path
from converter.validators.generated_cobol_release_validator import validate_generated_cobol
```

## Local dependency notes

- [converter/validators/generated_cobol_release_validator.py](../converter/validators/generated_cobol_release_validator.md)

## Symbol contracts and control points

### `test_generated_vmdz4310_passes_structural_release_checks` - L8-L14

```python
test_generated_vmdz4310_passes_structural_release_checks()
```

Observed calls (lexical order): `(ROOT / 'mainframe/workspace/Output').glob`, `sorted`, `len`, `path.read_text`, `str`, `validate_generated_cobol`.

### `test_validator_catches_projection_mismatch` - L17-L24

```python
test_validator_catches_projection_mismatch()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_catches_residual_idms_but_ignores_comments` - L27-L32

```python
test_validator_catches_residual_idms_but_ignores_comments()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_validator_catches_unbalanced_inline_perform` - L35-L39

```python
test_validator_catches_unbalanced_inline_perform()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_catches_fixed_format_overflow` - L42-L45

```python
test_validator_catches_fixed_format_overflow()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_counts_inline_times_scope_and_ignores_paragraph_perform_until` - L48-L55

```python
test_validator_counts_inline_times_scope_and_ignores_paragraph_perform_until()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_counts_varying_inline_scope` - L58-L64

```python
test_validator_counts_varying_inline_scope()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_ignores_syntax_like_tokens_inside_literals_and_inline_comments` - L67-L74

```python
test_validator_ignores_syntax_like_tokens_inside_literals_and_inline_comments()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_sql_terminator_inside_quoted_sql_literal_does_not_close_block` - L77-L83

```python
test_sql_terminator_inside_quoted_sql_literal_does_not_close_block()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_sql_terminator_inside_doubled_quote_literal_does_not_close_block` - L86-L92

```python
test_sql_terminator_inside_doubled_quote_literal_does_not_close_block()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_validator_blocks_residual_executable_error_status_but_ignores_comment` - L95-L102

```python
test_validator_blocks_residual_executable_error_status_but_ignores_comment()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_blocks_period_that_makes_idms_stop_unconditional` - L105-L113

```python
test_validator_blocks_period_that_makes_idms_stop_unconditional()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_accepts_scoped_idms_stop_and_local_target` - L116-L124

```python
test_validator_accepts_scoped_idms_stop_and_local_target()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_blocks_unresolved_idms_stop_call` - L127-L132

```python
test_validator_blocks_unresolved_idms_stop_call()
```

Observed calls (lexical order): `validate_generated_cobol`, `any`.

### `test_validator_blocks_residual_idms_dml_and_access_commands` - L135-L147

```python
test_validator_blocks_residual_idms_dml_and_access_commands()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_validator_ignores_idms_dml_words_in_comments_and_literals` - L150-L155

```python
test_validator_ignores_idms_dml_words_in_comments_and_literals()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_validator_refuses_move_to_reserved_statement_verbs` - L158-L163

```python
test_validator_refuses_move_to_reserved_statement_verbs()
```

Observed calls (lexical order): `validate_generated_cobol`.

### `test_validator_accepts_normal_move_followed_by_write` - L166-L170

```python
test_validator_accepts_normal_move_followed_by_write()
```

Observed calls (lexical order): `any`, `validate_generated_cobol`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
