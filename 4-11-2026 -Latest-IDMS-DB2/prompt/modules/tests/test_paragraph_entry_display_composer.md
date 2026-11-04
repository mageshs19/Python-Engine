# `tests/test_paragraph_entry_display_composer.py`

Source: [tests/test_paragraph_entry_display_composer.py](../../../tests/test_paragraph_entry_display_composer.py) | 91 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `51a8974b3e64bf28f83f4260e98ea067ddcfb2317cb57963e644c84e4af421da`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer
from pathlib import Path
```

## Local dependency notes

- [converter/composers/paragraph_entry_display_composer.py](../converter/composers/paragraph_entry_display_composer.md)

## Symbol contracts and control points

### `_logical` - L8-L11

```python
_logical(line: str) -> str
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.strip`.

Control points:

- L9: `if len(line) >= 7 and line[:6].isdigit()`

### `_paragraphs` - L14-L24

```python
_paragraphs(text: str) -> list[tuple[str, int]]
```

Observed calls (lexical order): `text.splitlines`, `_logical`, `enumerate`, `next`, `re.match`, `len`, `range`, `re.fullmatch`, `lines[i][7:72].lstrip`, `lines[i][:6].isdigit`, `result.append`.

Control points:

- L18: `for i in range(procedure + 1, len(lines))`
- L20: `if re.fullmatch('[A-Z0-9][A-Z0-9-]*\\.', body, re.I) and (len(lines[i]) < 7 or not lines[i][:6].isdigit() or len(lines[i][7:72]) - len(lines[i][7:72].lstrip()) <= 3) and (not (len(...`

### `test_every_paragraph_gets_active_exact_name_display_and_is_idempotent` - L27-L51

```python
test_every_paragraph_gets_active_exact_name_display_and_is_idempotent()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `ParagraphEntryDisplayComposer`, `composer.compose`, `output.splitlines`, `_paragraphs`, `_logical`, `len`, `f"DISPLAY '{name}.' .".replace`, `lines[next_idx][:6].isdigit`.

Control points:

- L44: `for (name, index) in paragraphs`
- L46: `while next_idx < len(lines) and (not _logical(lines[next_idx]))`

### `test_every_paragraph_gets_active_exact_name_display_and_is_idempotent.fixed` - L28-L29

```python
fixed(seq: int, body: str, indicator: str=' ') -> str
```

### `test_inserts_entry_display_when_paragraph_has_no_existing_display` - L54-L59

```python
test_inserts_entry_display_when_paragraph_has_no_existing_display()
```

Observed calls (lexical order): `'000010 PROCEDURE DIVISION.'.ljust`, `'000020 DO-WORK.'.ljust`, `'000030 MOVE 1 TO WS-X.'.ljust`, `ParagraphEntryDisplayComposer`, `ParagraphEntryDisplayComposer().compose`.

### `test_all_vmdz7200_lifecycle_v99_paragraphs_have_exact_active_entry_display` - L62-L79

```python
test_all_vmdz7200_lifecycle_v99_paragraphs_have_exact_active_entry_display()
```

Observed calls (lexical order): `Path`, `path.exists`, `path.read_text`, `output.splitlines`, `_paragraphs`, `len`, `_logical`, `_logical(lines[next_idx]).upper`, `f"DISPLAY '{name}.' .".replace`, `f"DISPLAY '{name}.' .".replace("' .", "'.").upper`, `lines[next_idx][:6].isdigit`, `all`.

Control points:

- L66: `if not path.exists()`
- L72: `for (name, index) in paragraphs`
- L74: `while next_idx < len(lines) and (not _logical(lines[next_idx]))`

### `test_nonmatching_debug_display_is_not_overwritten` - L82-L91

```python
test_nonmatching_debug_display_is_not_overwritten()
```

Observed calls (lexical order): `'\n'.join`, `'000010 PROCEDURE DIVISION.'.ljust`, `'000020 DO-WORK.'.ljust`, `"000030D DISPLAY 'BUSINESS DIAGNOSTIC'.".ljust`, `'000040 GOBACK.'.ljust`, `ParagraphEntryDisplayComposer`, `ParagraphEntryDisplayComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
