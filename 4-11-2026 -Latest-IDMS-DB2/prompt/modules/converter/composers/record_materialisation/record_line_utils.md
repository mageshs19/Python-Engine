# `converter/composers/record_materialisation/record_line_utils.py`

Source: [converter/composers/record_materialisation/record_line_utils.py](../../../../../converter/composers/record_materialisation/record_line_utils.py) | 116 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `8af50c0680a2f6212a82697b5f5e287b560f31938e140626038f231322405abb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format line helpers for record materialisation.

## Module-level bindings

`COMMENT_INDICATOR` (L16), `BLANK_INDICATOR` (L17), `__all__` (L116)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../../services/fixed_format_line_service.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/__init__.py](__init__.md)
- [converter/composers/record_materialisation/record_block_writer.py](record_block_writer.md)
- [converter/composers/record_materialisation/record_move_scanner.py](record_move_scanner.md)
- [converter/composers/record_materialisation_composer.py](../record_materialisation_composer.md)
- [tests/test_mapping_filler_layout_regression.py](../../../tests/test_mapping_filler_layout_regression.md)

## Symbol contracts and control points

### `RecordLineUtils` - L20-L113

```python
class RecordLineUtils()
```

Reads and writes fixed-format COBOL lines.

### `RecordLineUtils.__init__` - L23-L27

```python
__init__(self, fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `FixedFormatLineService`.

### `RecordLineUtils.logical` - L30-L35

```python
logical(self, line: str) -> str
```

Columns 8-72, stripped.

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `RecordLineUtils.body_indent` - L37-L42

```python
body_indent(self, line: str) -> str
```

Leading spaces of the body, as a string.

Observed calls (lexical order): `self.fixed_format.body_indent`, `str`.

### `RecordLineUtils.is_skippable` - L44-L49

```python
is_skippable(self, line: str) -> bool
```

Comment / page-eject / debug / continuation, read from col 7.

Observed calls (lexical order): `bool`, `self.fixed_format.is_comment_or_control_line`, `str`, `str(line or '').lstrip`, `str(line or '').lstrip().startswith`.

### `RecordLineUtils.level_of` - L52-L57

```python
level_of(body: str) -> int
```

Level number of a data description entry, or 0.

Observed calls (lexical order): `str`, `str(body or '').strip`, `str(body or '').strip().split`, `parts[0].isdigit`, `int`.

Control points:

- L55: `if parts and parts[0].isdigit()`

### `RecordLineUtils.emit` - L60-L102

```python
emit(self, template: str, body: str, indicator: str=BLANK_INDICATOR) -> list[str]
```

Render one logical body as one or more fixed-format lines.

Observed calls (lexical order): `str`, `str(body or '').rstrip`, `self.fixed_format.split`, `getattr`, `callable`, `emitter`, `list`, `self.fixed_format.build_or_none`.

Control points:

- L72: `if not text`
- L89: `if callable(emitter)`

### `RecordLineUtils.emit_generated` - L104-L113

```python
emit_generated(self, template: str, text: str) -> list[str]
```

Emit a generated body, routing a leading '*' to column 7.

Observed calls (lexical order): `str`, `str(text or '').lstrip`, `stripped.startswith`, `self.emit`, `stripped.lstrip`.

Control points:

- L107: `if stripped.startswith(COMMENT_INDICATOR)`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
