# `tests/restart/test_m10d_line_utils.py`

Source: [tests/restart/test_m10d_line_utils.py](../../../../tests/restart/test_m10d_line_utils.py) | 133 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `acbd9acb8a560a3687753916a0154f0ba553969d708e47015d79e1a91285f389`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M10d - RestartLineUtils.

## Module-level bindings

`BODY_WIDTH` (L36), `RIGHT_WIDTH` (L37), `CODE` (L46), `COMMENT` (L47), `BLANK` (L48), `FREE_FORM` (L49), `SEQUENCE_ONLY` (L50), `SEQUENCE_ARTIFACT` (L51)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.restart.restart_line_utils import RestartLineUtils
```

## Local dependency notes

- [converter/composers/restart/restart_line_utils.py](../../converter/composers/restart/restart_line_utils.md)

## Symbol contracts and control points

### `_fixed` - L40-L43

```python
_fixed(sequence: str, body: str, indicator: str=' ') -> str
```

One realistic 80-column record.

Observed calls (lexical order): `f'{sequence}00'[:RIGHT_WIDTH].ljust`, `body.ljust`.

### `utils` - L55-L56

```python
utils()
```

Observed calls (lexical order): `RestartLineUtils`.

### `_is_skipped` - L59-L62

```python
_is_skipped(line_tool, raw: str) -> bool
```

The contract every restart module applies, in one place.

Observed calls (lexical order): `line_tool.logical`, `str`, `str(line_tool.logical(raw) or '').strip`, `bool`, `line_tool.is_comment`.

### `test_a_code_line_yields_its_body` - L68-L69

```python
test_a_code_line_yields_its_body(utils)
```

Observed calls (lexical order): `utils.logical`.

### `test_free_form_text_is_still_read` - L72-L73

```python
test_free_form_text_is_still_read(utils)
```

Observed calls (lexical order): `utils.logical`.

### `test_a_comment_line_yields_nothing` - L76-L78

```python
test_a_comment_line_yields_nothing(utils)
```

The asterisk lives in column 7 and never reaches the body.

Observed calls (lexical order): `utils.logical`.

### `test_a_blank_line_yields_nothing` - L81-L82

```python
test_a_blank_line_yields_nothing(utils)
```

Observed calls (lexical order): `utils.logical`.

### `test_a_stray_sequence_area_yields_nothing` - L86-L88

```python
test_a_stray_sequence_area_yields_nothing(utils, raw)
```

001690. matches the paragraph-header shape; digits are legal.

Observed calls (lexical order): `utils.logical`.

### `test_a_numeric_paragraph_name_survives` - L91-L94

```python
test_a_numeric_paragraph_name_survives(utils)
```

Only a SIX digit run is a sequence area.

Observed calls (lexical order): `_fixed`, `utils.logical`.

### `test_marked_text_is_a_comment` - L98-L99

```python
test_marked_text_is_a_comment(utils, marker)
```

Observed calls (lexical order): `utils.is_comment`.

### `test_ordinary_text_is_not_a_comment` - L102-L103

```python
test_ordinary_text_is_not_a_comment(utils)
```

Observed calls (lexical order): `utils.is_comment`.

### `test_split_and_join_round_trip` - L106-L108

```python
test_split_and_join_round_trip(utils)
```

Observed calls (lexical order): `utils.join`, `utils.lines`.

### `test_an_unusable_service_is_refused_at_construction` - L114-L118

```python
test_an_unusable_service_is_refused_at_construction()
```

A wiring error must name the wiring, not a line three passes on.

Observed calls (lexical order): `pytest.raises`, `RestartLineUtils`, `object`, `str`.

### `test_both_implementations_skip_non_code` - L125-L127

```python
test_both_implementations_skip_non_code(utils, line_utils, raw)
```

Observed calls (lexical order): `_is_skipped`.

### `test_both_implementations_keep_code` - L131-L133

```python
test_both_implementations_keep_code(utils, line_utils, raw)
```

Observed calls (lexical order): `_is_skipped`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
