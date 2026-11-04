# `converter/composers/cursor_close_guarantee/line_utils.py`

Source: [converter/composers/cursor_close_guarantee/line_utils.py](../../../../../converter/composers/cursor_close_guarantee/line_utils.py) | 118 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `708d57661898af3c1cc0857cf35b05892eb2fc81e5a00e3d94828e090e3ca932`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Line inspection and formatting helpers.

## Module-level bindings

`COMMENT_INDICATORS` (L24), `UNTIL_KEYWORD` (L25), `__all__` (L118)

## Import declarations

```python
from __future__ import annotations
from converter.composers.cursor_flow_line_formatter import CursorFlowLineFormatter
from patterns.cursor_close_guarantee_patterns import UNTIL_ONLY_PATTERN
from rules.cursor_close_guarantee_rules import LEGACY_EOC_CONDITIONS, STATEMENT_TERMINATOR
```

## Local dependency notes

- [converter/composers/cursor_flow_line_formatter.py](../cursor_flow_line_formatter.md)
- [patterns/cursor_close_guarantee_patterns.py](../../../patterns/cursor_close_guarantee_patterns.md)
- [rules/cursor_close_guarantee_rules.py](../../../rules/cursor_close_guarantee_rules.md)

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_close_guarantee/__init__.py](__init__.md)
- [converter/composers/cursor_close_guarantee/business_paragraph_resolver.py](business_paragraph_resolver.md)
- [converter/composers/cursor_close_guarantee/close_guarantor.py](close_guarantor.md)
- [converter/composers/cursor_close_guarantee/condition_normaliser.py](condition_normaliser.md)
- [converter/composers/cursor_close_guarantee/cursor_scanner.py](cursor_scanner.md)
- [converter/composers/cursor_close_guarantee/loop_finder.py](loop_finder.md)
- [converter/composers/cursor_close_guarantee/loop_synthesiser.py](loop_synthesiser.md)
- [converter/composers/cursor_close_guarantee/paragraph_index.py](paragraph_index.md)

## Symbol contracts and control points

### `CursorGuaranteeLineUtils` - L28-L115

```python
class CursorGuaranteeLineUtils()
```

Physical line helpers shared by every close-guarantee helper.

### `CursorGuaranteeLineUtils.__init__` - L31-L35

```python
__init__(self, line_formatter: CursorFlowLineFormatter | None=None) -> None
```

Observed calls (lexical order): `CursorFlowLineFormatter`.

### `CursorGuaranteeLineUtils.logical` - L40-L42

```python
logical(self, line: str) -> str
```

The COBOL body of a line, sequence areas stripped.

Observed calls (lexical order): `self.line_formatter.logical`.

### `CursorGuaranteeLineUtils.is_blank_or_comment` - L44-L46

```python
is_blank_or_comment(self, line: str) -> bool
```

Observed calls (lexical order): `self.logical`, `self.is_comment`.

### `CursorGuaranteeLineUtils.is_comment` - L49-L51

```python
is_comment(logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').strip`, `bool`.

### `CursorGuaranteeLineUtils.is_terminated` - L54-L55

```python
is_terminated(logical: str) -> bool
```

Observed calls (lexical order): `str`, `str(logical or '').rstrip`, `str(logical or '').rstrip().endswith`.

### `CursorGuaranteeLineUtils.format_like` - L60-L65

```python
format_like(self, reference_line: str, body: str) -> str
```

Render `body` with the layout of `reference_line`.

Observed calls (lexical order): `self.line_formatter.format_like_line`.

### `CursorGuaranteeLineUtils.partition_until` - L71-L86

```python
partition_until(logical: str) -> tuple[str, str, str]
```

Split a logical line on UNTIL, preserving the original case.

Observed calls (lexical order): `str`, `text.upper`, `text.upper().find`, `len`, `text[position + len(UNTIL_KEYWORD):].strip`.

Control points:

- L80: `if position < 0`

### `CursorGuaranteeLineUtils.is_until_only` - L89-L91

```python
is_until_only(logical: str) -> bool
```

True when the line carries nothing but the UNTIL clause.

Observed calls (lexical order): `UNTIL_ONLY_PATTERN.match`, `bool`, `str`.

### `CursorGuaranteeLineUtils.is_legacy_condition` - L93-L103

```python
is_legacy_condition(self, condition: str) -> bool
```

True when the exit test is still the raw IDMS / SQLCODE form.

Observed calls (lexical order): `self.compress`, `any`.

Control points:

- L97: `if not current`

### `CursorGuaranteeLineUtils.compress` - L109-L111

```python
compress(text: str) -> str
```

Whitespace-insensitive, case-insensitive comparison key.

Observed calls (lexical order): `' '.join`, `' '.join(str(text or '').split()).upper`, `str`, `str(text or '').split`.

### `CursorGuaranteeLineUtils.normalize_line_endings` - L114-L115

```python
normalize_line_endings(text: str) -> str
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
