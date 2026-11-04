# `tests/test_qualifier_connector_wrap.py`

Source: [tests/test_qualifier_connector_wrap.py](../../../tests/test_qualifier_connector_wrap.py) | 80 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `8533a6db531e78fd70da47d27c62e9b3c7f91cd606b1f257f0afdb6e550434c4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Regression tests for qualifier-connector aware line wrapping.

## Module-level bindings

`INDENT` (L19)

## Import declarations

```python
from __future__ import annotations
from converter.composers.fixed_format_wrapper import FixedFormatWrapper
from converter.services.fixed_format_line_service import FixedFormatLineService, glue_qualifier_connectors
from patterns.procedure_indent_patterns import PARAGRAPH_HEADER_PATTERN
```

## Local dependency notes

- [converter/composers/fixed_format_wrapper.py](../converter/composers/fixed_format_wrapper.md)
- [converter/services/fixed_format_line_service.py](../converter/services/fixed_format_line_service.md)
- [patterns/procedure_indent_patterns.py](../patterns/procedure_indent_patterns.md)

## Symbol contracts and control points

### `_wrap` - L22-L23

```python
_wrap(stmt: str) -> list[str]
```

Observed calls (lexical order): `FixedFormatWrapper`, `FixedFormatWrapper().wrap_by_words`.

### `test_connector_glue_keeps_of_with_following_name` - L26-L32

```python
test_connector_glue_keeps_of_with_following_name() -> None
```

Observed calls (lexical order): `glue_qualifier_connectors`.

### `test_trailing_connector_without_following_name_is_untouched` - L35-L36

```python
test_trailing_connector_without_following_name_is_untouched() -> None
```

Observed calls (lexical order): `glue_qualifier_connectors`.

### `test_no_fragment_ends_with_a_dangling_connector` - L39-L46

```python
test_no_fragment_ends_with_a_dangling_connector() -> None
```

Observed calls (lexical order): `_wrap`, `line.strip`, `line.strip().upper`, `line.strip().upper().endswith`.

Control points:

- L44: `for line in _wrap(stmt)`

### `test_continuation_fragment_is_not_mistaken_for_a_paragraph` - L49-L55

```python
test_continuation_fragment_is_not_mistaken_for_a_paragraph() -> None
```

Observed calls (lexical order): `_wrap`, `PARAGRAPH_HEADER_PATTERN.match`, `line.strip`, `line.strip().upper`.

Control points:

- L54: `for line in _wrap(stmt)`

### `test_multi_receiver_move_wraps_cleanly` - L58-L66

```python
test_multi_receiver_move_wraps_cleanly() -> None
```

Observed calls (lexical order): `_wrap`, `line.strip`, `line.strip().upper`, `line.strip().upper().endswith`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L64: `for line in lines`

### `test_service_wrap_body_lines_also_glues_connectors` - L69-L80

```python
test_service_wrap_body_lines_also_glues_connectors() -> None
```

Observed calls (lexical order): `FixedFormatLineService`, `FixedFormatLineService().wrap_body_lines`, `line.strip`, `line.strip().upper`, `line.strip().upper().endswith`, `PARAGRAPH_HEADER_PATTERN.match`.

Control points:

- L78: `for line in lines`

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
