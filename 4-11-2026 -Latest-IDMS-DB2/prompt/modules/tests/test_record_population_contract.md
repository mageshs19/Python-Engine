# `tests/test_record_population_contract.py`

Source: [tests/test_record_population_contract.py](../../../tests/test_record_population_contract.py) | 85 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `e8218f9515676a38edad3c0b92e74b464c686ec065ef721654172cabd502ed9d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from pathlib import Path
from mainframe.verification.record_population_contract import audit_record_population
import re
import pytest
```

## Local dependency notes

- [mainframe/verification/record_population_contract.py](../mainframe/verification/record_population_contract.md)

## Symbol contracts and control points

### `_program` - L5-L18

```python
_program(body)
```

Observed calls (lexical order): `''.join`, `enumerate`.

### `test_complete_numeric_coverage_passes` - L21-L25

```python
test_complete_numeric_coverage_passes()
```

Observed calls (lexical order): `_program`, `audit_record_population`.

### `test_missing_numeric_assignment_rejected_even_when_layout_correct` - L28-L33

```python
test_missing_numeric_assignment_rejected_even_when_layout_correct()
```

Observed calls (lexical order): `_program`, `audit_record_population`, `len`.

### `test_move_into_parent_group_covers_child_fields` - L36-L39

```python
test_move_into_parent_group_covers_child_fields()
```

Observed calls (lexical order): `_program`, `audit_record_population`.

### `test_initialize_counts_as_numeric_assignment_not_move_spaces` - L42-L44

```python
test_initialize_counts_as_numeric_assignment_not_move_spaces()
```

Observed calls (lexical order): `_program`, `audit_record_population`.

### `test_renamed_buffer_fields_same_generic_behavior` - L47-L50

```python
test_renamed_buffer_fields_same_generic_behavior()
```

Observed calls (lexical order): `_program`, `original.replace`, `original.replace('OUT-BUFFER', 'OUT-DATA').replace`, `audit_record_population`.

### `test_real_generated_7200_numeric_fields_have_assignments` - L53-L59

```python
test_real_generated_7200_numeric_fields_have_assignments()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `(root / 'mainframe/workspace/Output').glob`, `sorted`, `pytest.skip`, `audit_record_population`, `members[-1].read_text`.

Control points:

- L56: `if not members`

### `test_same_named_target_of_unrelated_group_does_not_cover_output` - L62-L66

```python
test_same_named_target_of_unrelated_group_does_not_cover_output()
```

Observed calls (lexical order): `_program`, `audit_record_population`.

### `test_generated_output_would_fail_if_mapped_numeric_move_were_dropped` - L69-L85

```python
test_generated_output_would_fail_if_mapped_numeric_move_were_dropped()
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `(root / 'mainframe/workspace/Output').glob`, `sorted`, `pytest.skip`, `members[-1].read_text`, `re.search`, `re.sub`, `any`, `audit_record_population`.

Control points:

- L72: `if not members`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
