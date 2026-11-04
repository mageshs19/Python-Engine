# `tests/test_cobol_area_alignment_reflow.py`

Source: [tests/test_cobol_area_alignment_reflow.py](../../../tests/test_cobol_area_alignment_reflow.py) | 112 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `7084a55ea98cc0812640958e78f88f181b9018e3a240bcbaa24e95b7026b22f0`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from converter.services.cobol_area_alignment_classifier import CobolAreaAlignmentClassifier
from converter.services.cobol_area_alignment_reflow import CobolAreaAlignmentReflow
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/cobol_area_alignment_classifier.py](../converter/services/cobol_area_alignment_classifier.md)
- [converter/services/cobol_area_alignment_reflow.py](../converter/services/cobol_area_alignment_reflow.md)
- [converter/services/fixed_format_line_service.py](../converter/services/fixed_format_line_service.md)

## Symbol contracts and control points

### `_fixed` - L15-L16

```python
_fixed(body: str, seq: str='002770', right: str='02770000') -> str
```

Observed calls (lexical order): `body[:65].ljust`.

### `_reflow` - L19-L23

```python
_reflow() -> CobolAreaAlignmentReflow
```

Observed calls (lexical order): `CobolAreaAlignmentReflow`, `FixedFormatLineService`, `CobolAreaAlignmentClassifier`.

### `_body` - L26-L27

```python
_body(line: str) -> str
```

Observed calls (lexical order): `line[7:72].rstrip`.

### `test_two_line_move_keeps_both_lines_and_full_name` - L30-L42

```python
test_two_line_move_keeps_both_lines_and_full_name()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`, `len`, `_body`.

### `test_continuation_is_indented_one_level_further` - L45-L56

```python
test_continuation_is_indented_one_level_further()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`, `_body`, `_body(out[0]).startswith`, `_body(out[1]).startswith`.

### `test_never_truncates_a_data_name` - L59-L71

```python
test_never_truncates_a_data_name()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`, `' '.join`, `_body`.

### `test_next_paragraph_header_is_never_joined` - L74-L84

```python
test_next_paragraph_header_is_never_joined()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`.

### `test_next_statement_is_never_joined` - L87-L98

```python
test_next_statement_is_never_joined()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`.

### `test_statement_is_not_collapsed_onto_one_line` - L101-L112

```python
test_statement_is_not_collapsed_onto_one_line()
```

Observed calls (lexical order): `_fixed`, `_reflow`, `_reflow().try_reflow_with_next_line`, `len`, `_body`, `_body(out[1]).strip`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
