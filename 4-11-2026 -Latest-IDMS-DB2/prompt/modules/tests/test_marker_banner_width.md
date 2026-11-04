# `tests/test_marker_banner_width.py`

Source: [tests/test_marker_banner_width.py](../../../tests/test_marker_banner_width.py) | 157 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `a8b6f01690fa7097cadc42b1a6964dc2114e664e67ce49800879dac0baf66de6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generated marker banners must fit the fixed-format body window.

## Module-level bindings

`BANNER_TEMPLATE` (L41), `MARKERS_UNDER_TEST` (L43)

## Import declarations

```python
import pytest
from catalogs.output_sections import COMMENT_BODY_WIDTH, COMMENT_TITLE_WIDTH, DB2_CURSOR_DECLARATIONS_MARKER, DB2_CURSOR_FLAGS_MARKER, DB2_INFRASTRUCTURE_MARKER, DB2_INFRASTRUCTURE_MARKER_SHORT
from converter.generators.db2_infrastructure.infrastructure_block_builder import InfrastructureBlockBuilder
```

## Local dependency notes

- [catalogs/output_sections.py](../catalogs/output_sections.md)
- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](../converter/generators/db2_infrastructure/infrastructure_block_builder.md)

## Symbol contracts and control points

### `_LineUtils` - L50-L71

```python
class _LineUtils()
```

Minimal stand-in for the injected infrastructure line utils.

### `_LineUtils.comment_block` - L54-L55

```python
comment_block(title: str) -> list[str]
```

Observed calls (lexical order): `BANNER_TEMPLATE.format`.

### `_LineUtils.and_lines` - L58-L59

```python
and_lines(items: list[str], indent: str) -> list[str]
```

### `_LineUtils.comma_lines` - L62-L63

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

### `_LineUtils.normalize_include_name` - L66-L67

```python
normalize_include_name(value: str) -> str
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`.

### `_LineUtils.logical` - L70-L71

```python
logical(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').strip`.

### `builder` - L75-L76

```python
builder()
```

Observed calls (lexical order): `InfrastructureBlockBuilder`, `_LineUtils`.

### `test_every_chosen_title_fits_the_banner_window` - L83-L85

```python
test_every_chosen_title_fits_the_banner_window(builder, marker)
```

Template independent: the TITLE itself must fit.

Observed calls (lexical order): `builder._fit_marker`, `len`.

### `test_the_long_infrastructure_marker_uses_its_short_form` - L88-L94

```python
test_the_long_infrastructure_marker_uses_its_short_form(builder)
```

The 69-character marker is the one that overflowed.

Observed calls (lexical order): `len`, `builder._fit_marker`.

### `test_a_marker_that_already_fits_is_left_alone` - L97-L101

```python
test_a_marker_that_already_fits_is_left_alone(builder)
```

Observed calls (lexical order): `builder._fit_marker`.

### `test_an_unregistered_over_long_marker_is_truncated` - L104-L108

```python
test_an_unregistered_over_long_marker_is_truncated(builder)
```

Observed calls (lexical order): `builder._fit_marker`, `len`, `fitted.endswith`.

### `test_an_empty_marker_yields_no_title` - L111-L113

```python
test_an_empty_marker_yields_no_title(builder)
```

Observed calls (lexical order): `builder._fit_marker`.

### `test_every_marker_renders_as_one_line` - L120-L122

```python
test_every_marker_renders_as_one_line(builder, marker)
```

A wrapped banner is what produced the orphan '*FLAGS*' line.

Observed calls (lexical order): `builder._marker_lines`, `len`.

### `test_every_marker_fits_the_body_window` - L126-L128

```python
test_every_marker_fits_the_body_window(builder, marker)
```

Observed calls (lexical order): `builder._marker_lines`, `len`.

Control points:

- L127: `for line in builder._marker_lines(marker)`

### `test_every_marker_opens_and_closes_with_an_asterisk` - L132-L136

```python
test_every_marker_opens_and_closes_with_an_asterisk(builder, marker)
```

Observed calls (lexical order): `builder._marker_lines`, `line.startswith`, `line.rstrip`, `line.rstrip().endswith`.

### `test_an_empty_marker_emits_no_line` - L139-L141

```python
test_an_empty_marker_emits_no_line(builder)
```

Observed calls (lexical order): `builder._marker_lines`.

### `test_the_short_form_fallback_is_reported` - L147-L151

```python
test_the_short_form_fallback_is_reported(builder)
```

A silently shortened banner is a review problem.

Observed calls (lexical order): `builder._marker_lines`, `any`.

### `test_truncation_is_reported` - L154-L157

```python
test_truncation_is_reported(builder)
```

Observed calls (lexical order): `builder._marker_lines`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
