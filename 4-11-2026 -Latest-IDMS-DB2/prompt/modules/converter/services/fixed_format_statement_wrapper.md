# `converter/services/fixed_format_statement_wrapper.py`

Source: [converter/services/fixed_format_statement_wrapper.py](../../../../converter/services/fixed_format_statement_wrapper.py) | 132 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `3d92a4fdbda2c24591e66521c55e7fae5b6a3edcc76ebe1e3468e48baf2ef741`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Wrap-aware fixed-format body replacement.

## Import declarations

```python
from __future__ import annotations
from patterns.fixed_format_wrap_patterns import MOVE_TO_PATTERN
from rules.fixed_format_wrap_rules import BODY_WIDTH, CONTINUATION_INDENT, DIAG_WRAPPED_TEMPLATE, BODY_END_COLUMN, TOKEN_MOVE, TOKEN_OF_DCL, TOKEN_TO
```

## Local dependency notes

- [patterns/fixed_format_wrap_patterns.py](../../patterns/fixed_format_wrap_patterns.md)
- [rules/fixed_format_wrap_rules.py](../../rules/fixed_format_wrap_rules.md)

## Symbol contracts and control points

### `FixedFormatStatementWrapper` - L28-L132

```python
class FixedFormatStatementWrapper()
```

### `FixedFormatStatementWrapper.__init__` - L30-L32

```python
__init__(self, fixed_format) -> None
```

### `FixedFormatStatementWrapper.replace_body` - L34-L59

```python
replace_body(self, line: str, new_body: str) -> list[str]
```

Replace a fixed-format body, wrapping when it no longer fits.

Observed calls (lexical order): `str`, `str(new_body or '').rstrip`, `self.fixed_format.is_fixed_line`, `self._leading_spaces`, `self._wrap`, `len`, `self.messages.append`, `DIAG_WRAPPED_TEMPLATE.format`, `self.fixed_format.replace_body`.

Control points:

- L45: `if not self.fixed_format.is_fixed_line(line)`
- L51: `if len(fragments) > 1`

### `FixedFormatStatementWrapper._wrap` - L61-L72

```python
_wrap(self, body: str, indent: str) -> list[str]
```

Observed calls (lexical order): `len`, `self._wrap_move`, `self._wrap_by_words`.

Control points:

- L62: `if len(body) <= BODY_WIDTH`
- L66: `if move_lines`

### `FixedFormatStatementWrapper._wrap_move` - L74-L100

```python
_wrap_move(self, body: str, indent: str) -> list[str]
```

Split MOVE <source> TO <target> on the TO boundary.

Observed calls (lexical order): `MOVE_TO_PATTERN.match`, `body.strip`, `match.group`, `str`, `str(match.group('source') or '').strip`, `str(match.group('target') or '').strip`, `str(match.group('dot') or '').strip`, `source.upper`, `len`.

Control points:

- L81: `if not match`
- L88: `if not source or not target`
- L94: `if len(one_line) <= BODY_WIDTH and (not force_split)`

### `FixedFormatStatementWrapper._wrap_by_words` - L102-L127

```python
_wrap_by_words(self, body: str, continuation_indent: str) -> list[str]
```

Observed calls (lexical order): `body.split`, `self._leading_spaces`, `current.strip`, `len`, `current.rstrip`, `output.append`.

Control points:

- L108: `if not words`
- L115: `for word in words`
- L117: `if len(candidate) <= BODY_WIDTH`
- L124: `if current.strip()`

### `FixedFormatStatementWrapper._leading_spaces` - L130-L132

```python
_leading_spaces(text: str) -> str
```

Observed calls (lexical order): `str`, `len`, `raw.lstrip`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
