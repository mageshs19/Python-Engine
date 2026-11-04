# `tests/test_compiler_safety_validator.py`

Source: [tests/test_compiler_safety_validator.py](../../../tests/test_compiler_safety_validator.py) | 128 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `738909cc52ae25f94a1d783c961d469f50554defc02f31602f34af19c61fe327`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.validators.compiler_safety_validator import CompilerSafetyValidator
from converter.repositories.dclgen_repository import DclgenRepository
from converter.validators.production_validator import ProductionValidator
```

## Local dependency notes

- [converter/repositories/dclgen_repository.py](../converter/repositories/dclgen_repository.md)
- [converter/validators/compiler_safety_validator.py](../converter/validators/compiler_safety_validator.md)
- [converter/validators/production_validator.py](../converter/validators/production_validator.md)

## Symbol contracts and control points

### `test_flags_value_clause_on_redefines_declaration` - L4-L9

```python
test_flags_value_clause_on_redefines_declaration()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_accepts_redefines_without_value_clause` - L12-L17

```python
test_accepts_redefines_without_value_clause()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_flags_cursor_select_fetch_count_mismatch` - L20-L27

```python
test_flags_cursor_select_fetch_count_mismatch()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_accepts_matching_cursor_select_fetch_counts` - L30-L37

```python
test_accepts_matching_cursor_select_fetch_counts()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_flags_unbalanced_exec_sql_block` - L40-L45

```python
test_flags_unbalanced_exec_sql_block()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_production_validator_includes_compiler_preflight_findings` - L48-L59

```python
test_production_validator_includes_compiler_preflight_findings()
```

Observed calls (lexical order): `DclgenRepository`, `ProductionValidator`, `validator.validate`, `any`.

### `test_flags_sentence_terminator_inside_sqlcode_evaluate` - L62-L71

```python
test_flags_sentence_terminator_inside_sqlcode_evaluate()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_accepts_sqlcode_evaluate_with_period_after_scope_terminator` - L74-L83

```python
test_accepts_sqlcode_evaluate_with_period_after_scope_terminator()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_sql_terminator_inside_literal_does_not_close_block` - L86-L93

```python
test_sql_terminator_inside_literal_does_not_close_block()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_sql_terminator_inside_sql_line_comment_does_not_close_block` - L96-L104

```python
test_sql_terminator_inside_sql_line_comment_does_not_close_block()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_sql_terminator_inside_multiline_block_comment_does_not_close_block` - L107-L117

```python
test_sql_terminator_inside_multiline_block_comment_does_not_close_block()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

### `test_fixed_format_comment_line_does_not_close_sql_block` - L120-L128

```python
test_fixed_format_comment_line_does_not_close_sql_block()
```

Observed calls (lexical order): `CompilerSafetyValidator`, `CompilerSafetyValidator().validate`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
