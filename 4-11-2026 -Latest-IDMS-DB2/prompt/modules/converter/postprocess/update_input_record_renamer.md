# `converter/postprocess/update_input_record_renamer.py`

Source: [converter/postprocess/update_input_record_renamer.py](../../../../converter/postprocess/update_input_record_renamer.py) | 132 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `6a92c2ac4fc2bee3cc955a1a23532b06b4de0981dbb8741bebe3cdede78237e7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
import re
from patterns.update_record_rename_patterns import COPY_RECORD_PATTERN_TEMPLATE, WORD_RECORD_PATTERN_TEMPLATE
```

## Local dependency notes

- [patterns/update_record_rename_patterns.py](../../patterns/update_record_rename_patterns.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../../runners/update/update_postprocess_pipeline.md)
- [tests/test_update_input_record_renamer.py](../../tests/test_update_input_record_renamer.md)

## Symbol contracts and control points

### `UpdateInputRecordRenamer` - L11-L132

```python
class UpdateInputRecordRenamer()
```

Renames original source references to the input record.

### `UpdateInputRecordRenamer.apply` - L28-L95

```python
apply(self, text: str, old_name: str, new_name: str, diagnostics: list[str] | None=None) -> str
```

Observed calls (lexical order): `str`, `str(old_name or '').strip`, `str(old_name or '').strip().upper`, `str(new_name or '').strip`, `str(new_name or '').strip().upper`, `re.compile`, `WORD_RECORD_PATTERN_TEMPLATE.format`, `re.escape`, `COPY_RECORD_PATTERN_TEMPLATE.format`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._is_comment_or_debug`, `output.append`, `self._body`, `word_pattern.sub`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L35: `if not text`
- L41: `if not old or not new or old == new`
- L64: `for line in lines`
- L66: `if self._is_comment_or_debug(line)`
- L75: `if new_body != body`
- L81: `if copy_new_pattern.search(body)`
- L82: `if seen_copy_new`
- L89: `if changed and diagnostics is not None`

### `UpdateInputRecordRenamer._is_comment_or_debug` - L100-L109

```python
_is_comment_or_debug(self, line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.strip`, `stripped.startswith`, `stripped.upper`, `stripped.upper().startswith`.

Control points:

- L102: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `UpdateInputRecordRenamer._body` - L111-L120

```python
_body(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[7:72].rstrip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.rstrip`, `text.rstrip`.

Control points:

- L113: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L115: `if len(text) > 6 and text[:6].strip().isdigit()`
- L117: `if len(body) >= 8 and body[-8:].strip().isdigit()`

### `UpdateInputRecordRenamer._replace_body` - L122-L132

```python
_replace_body(self, line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '')[:65].ljust`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `clean.rstrip`.

Control points:

- L125: `if len(text) >= 72 and text[:6].strip().isdigit()`
- L129: `if len(text) > 6 and text[:6].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
