# `tests/test_input_record_totals_preservation.py`

Source: [tests/test_input_record_totals_preservation.py](../../../tests/test_input_record_totals_preservation.py) | 71 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d77bc551ae00c75efc4e5cdb223ae172706e1f2a993db859565fbbbb484c9d71`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`SOURCE` (L4)

## Import declarations

```python
from converter.composers.counter_declaration_composer import CounterDeclarationComposer
```

## Local dependency notes

- [converter/composers/counter_declaration_composer.py](../converter/composers/counter_declaration_composer.md)

## Symbol contracts and control points

### `test_adds_successful_input_counter_and_preserves_treated_total` - L26-L34

```python
test_adds_successful_input_counter_and_preserves_treated_total()
```

Observed calls (lexical order): `CounterDeclarationComposer`, `composer.compose`.

### `test_input_counter_is_only_incremented_once_and_composer_is_idempotent` - L37-L44

```python
test_input_counter_is_only_incremented_once_and_composer_is_idempotent()
```

Observed calls (lexical order): `CounterDeclarationComposer`, `composer.compose`, `twice.count`.

### `test_eof_is_not_counted_as_an_input_record` - L47-L54

```python
test_eof_is_not_counted_as_an_input_record()
```

Observed calls (lexical order): `CounterDeclarationComposer`, `composer.compose`, `generated.split`, `generated.split('READ INPUT-FILE', 1)[1].split`, `read_block.index`.

### `test_does_not_add_input_totals_to_programs_without_treated_counter_convention` - L58-L71

```python
test_does_not_add_input_totals_to_programs_without_treated_counter_convention()
```

Observed calls (lexical order): `CounterDeclarationComposer`, `CounterDeclarationComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
