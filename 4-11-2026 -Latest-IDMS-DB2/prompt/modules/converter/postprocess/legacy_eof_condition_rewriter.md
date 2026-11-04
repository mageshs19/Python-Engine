# `converter/postprocess/legacy_eof_condition_rewriter.py`

Source: [converter/postprocess/legacy_eof_condition_rewriter.py](../../../../converter/postprocess/legacy_eof_condition_rewriter.py) | 296 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `27c78c6f0ed29222757d0007fbf66a2d404a8fd12276c93d6839bfe1ca62ebff`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Point surviving legacy EOF tests at the condition the generator writes.

## Module-level bindings

`BODY_START` (L85), `BODY_END` (L86), `BODY_WIDTH` (L87), `__all__` (L296)

## Import declarations

```python
from __future__ import annotations
import re
from patterns.dynamic_metadata_patterns import AT_END_SET_TRUE_RE, CONDITION_WORD_TEMPLATE, PROCEDURE_DIVISION_RE, WRITE_TO_NAME_TEMPLATE
```

## Local dependency notes

- [patterns/dynamic_metadata_patterns.py](../../patterns/dynamic_metadata_patterns.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)

## Symbol contracts and control points

### `LegacyEofConditionRewriter` - L90-L293

```python
class LegacyEofConditionRewriter()
```

Rewrites surviving legacy EOF condition tests to the live one.

### `LegacyEofConditionRewriter.apply` - L93-L145

```python
apply(self, text: str, *, legacy_condition: str, diagnostics: list[str] | None=None) -> str
```

Observed calls (lexical order): `str`, `str(legacy_condition or '').strip`, `str(legacy_condition or '').strip().upper`, `self._say`, `self._live_condition`, `self._is_written`, `self._rewrite`.

Control points:

- L100: `if not text`
- L105: `if not legacy`
- L115: `if not live`
- L124: `if live == legacy`
- L132: `if self._is_written(text, legacy)`

### `LegacyEofConditionRewriter._rewrite` - L150-L222

```python
_rewrite(self, *, text: str, legacy: str, live: str, diagnostics: list[str] | None) -> str
```

Observed calls (lexical order): `re.compile`, `CONDITION_WORD_TEMPLATE.format`, `re.escape`, `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._is_comment_or_debug`, `output.append`, `self._body`, `PROCEDURE_DIVISION_RE.match`, `pattern.subn`, `len`, `new_body.rstrip`, `self._replace_body`, `self._say`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L172: `for line in lines`
- L173: `if self._is_comment_or_debug(line)`
- L179: `if not in_procedure`
- L180: `if PROCEDURE_DIVISION_RE.match(body)`
- L187: `if not count`
- L191: `if len(new_body.rstrip()) > BODY_WIDTH`
- L199: `if changed`
- L214: `if refused`

### `LegacyEofConditionRewriter._live_condition` - L228-L230

```python
_live_condition(text: str) -> str
```

Observed calls (lexical order): `AT_END_SET_TRUE_RE.search`, `str`, `match.group`, `match.group('name').strip`, `match.group('name').strip().upper`.

### `LegacyEofConditionRewriter._is_written` - L233-L238

```python
_is_written(text: str, name: str) -> bool
```

Observed calls (lexical order): `re.compile`, `WRITE_TO_NAME_TEMPLATE.format`, `re.escape`, `bool`, `pattern.search`, `str`.

### `LegacyEofConditionRewriter._is_comment_or_debug` - L244-L256

```python
_is_comment_or_debug(line: str) -> bool
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text.strip`, `stripped.startswith`, `stripped.upper`, `stripped.upper().startswith`.

Control points:

- L247: `if len(text) >= 7 and text[:6].strip().isdigit()`

### `LegacyEofConditionRewriter._body` - L259-L273

```python
_body(line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `text[BODY_START:BODY_END].rstrip`, `body[-8:].strip`, `body[-8:].strip().isdigit`, `body.rstrip`, `text.rstrip`.

Control points:

- L262: `if len(text) >= BODY_END and text[:6].strip().isdigit()`
- L265: `if len(text) > BODY_START and text[:6].strip().isdigit()`
- L268: `if len(body) >= 8 and body[-8:].strip().isdigit()`

### `LegacyEofConditionRewriter._replace_body` - L276-L288

```python
_replace_body(line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(body or '')[:BODY_WIDTH].ljust`, `len`, `text[:6].strip`, `text[:6].strip().isdigit`, `clean.rstrip`.

Control points:

- L280: `if len(text) >= BODY_END and text[:6].strip().isdigit()`
- L285: `if len(text) > 6 and text[:6].strip().isdigit()`

### `LegacyEofConditionRewriter._say` - L291-L293

```python
_say(diagnostics: list[str] | None, message: str) -> None
```

Observed calls (lexical order): `diagnostics.append`.

Control points:

- L292: `if diagnostics is not None`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
