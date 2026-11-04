# `tests/cursor_contract/test_join_key_labels.py`

Source: [tests/cursor_contract/test_join_key_labels.py](../../../../tests/cursor_contract/test_join_key_labels.py) | 112 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `525afd721c9aa02c19210494f833ff5419420701dd6cf181d8891ef3abedf37c`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`GROUP` (L9), `COLUMN` (L10), `HOST` (L11), `MAPPED_NAME` (L12)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.cursor_paragraph.join_key_label_resolver import JoinKeyLabelResolver
from converter.generators.cursor_paragraph.cursor_key_diagnostics import KeyDiagnosticsBuilder
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_key_diagnostics.py](../../converter/generators/cursor_paragraph/cursor_key_diagnostics.md)
- [converter/generators/cursor_paragraph/join_key_label_resolver.py](../../converter/generators/cursor_paragraph/join_key_label_resolver.md)

## Symbol contracts and control points

### `FakeRepository` - L15-L25

```python
class FakeRepository()
```

### `FakeRepository.__init__` - L16-L20

```python
__init__(self, rows: dict) -> None
```

Observed calls (lexical order): `column.upper`, `table.upper`, `rows.items`.

### `FakeRepository.cobol_field_for_column` - L22-L25

```python
cobol_field_for_column(self, table_name: str, column_name: str)
```

Observed calls (lexical order): `self.rows.get`, `str`, `str(column_name).upper`, `str(table_name).upper`.

### `mapped` - L29-L32

```python
mapped() -> JoinKeyLabelResolver
```

Observed calls (lexical order): `JoinKeyLabelResolver`, `FakeRepository`.

### `test_the_dclgen_group_resolves_to_the_mapping_table` - L35-L36

```python
test_the_dclgen_group_resolves_to_the_mapping_table(mapped)
```

Observed calls (lexical order): `mapped.candidate_tables`.

### `test_the_label_comes_from_sheet_mapping` - L39-L43

```python
test_the_label_comes_from_sheet_mapping(mapped)
```

Observed calls (lexical order): `mapped.label_for`, `mapped.table_of`.

### `test_the_level_prefix_is_stripped` - L46-L50

```python
test_the_level_prefix_is_stripped(mapped)
```

Observed calls (lexical order): `mapped.label_for`, `mapped.table_of`, `label.startswith`.

### `test_a_successful_lookup_reports_nothing` - L53-L55

```python
test_a_successful_lookup_reports_nothing(mapped)
```

Observed calls (lexical order): `mapped.label_for`, `mapped.table_of`.

### `test_a_missing_row_falls_back_and_reports` - L58-L65

```python
test_a_missing_row_falls_back_and_reports()
```

Observed calls (lexical order): `FakeRepository`, `JoinKeyLabelResolver`, `resolver.label_for`, `resolver.table_of`.

### `test_no_repository_falls_back_and_reports` - L68-L75

```python
test_no_repository_falls_back_and_reports()
```

Observed calls (lexical order): `JoinKeyLabelResolver`, `resolver.label_for`, `resolver.table_of`.

### `test_an_empty_cobol_zone_is_not_a_label` - L78-L87

```python
test_an_empty_cobol_zone_is_not_a_label()
```

Observed calls (lexical order): `JoinKeyLabelResolver`, `FakeRepository`, `resolver.label_for`, `resolver.table_of`.

### `test_the_repository_lookup_does_not_raise` - L89-L99

```python
test_the_repository_lookup_does_not_raise(mapped)
```

Regression: cobol_field_for_column delegated to a non-existent attribute, so every lookup raised AttributeError, was caught, and fell back to the DCLGEN host name. A converter defect that looked exactly like a missing workbook cell.

Observed calls (lexical order): `mapped.label_for`, `mapped.table_of`.

### `test_a_builder_without_a_resolver_is_refused` - L102-L112

```python
test_a_builder_without_a_resolver_is_refused()
```

Regression: KeyDiagnosticsBuilder() was legal and substituted an empty resolver, degrading every label silently.

Observed calls (lexical order): `pytest.raises`, `KeyDiagnosticsBuilder`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
