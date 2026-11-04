# `review/checks/chk_32_scope_balance.py`

Source: [review/checks/chk_32_scope_balance.py](../../../../review/checks/chk_32_scope_balance.py) | 160 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `34f1e3a9daf5c9aaaebf3dcbb20e4c54408a5a13c278cbf16ecf9ce0c29bcdbd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> CHK-32 Scope terminator balance.

## Module-level bindings

`SCOPED_VERBS` (L32), `ORPHAN_NOTE` (L34), `UNCLOSED_NOTE` (L35)

## Import declarations

```python
from __future__ import annotations
import re
from review.engine.check_base import CRITICAL, BOTH, Check
from review.standards import cobol_standards as std
```

## Local dependency notes

- [review/engine/check_base.py](../engine/check_base.md)
- [review/standards/__init__.py](../standards/__init__.md)
- [review/standards/cobol_standards.py](../standards/cobol_standards.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)

## Symbol contracts and control points

### `ScopeBalanceCheck` - L38-L160

```python
class ScopeBalanceCheck(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-32'
TITLE = 'Scope terminator balance (IF / EVALUATE)'
SEVERITY = CRITICAL
APPLIES_TO = BOTH
ORDER = 320
```

### `ScopeBalanceCheck.review` - L45-L67

```python
review(self, ctx, view, record) -> None
```

Observed calls (lexical order): `self._walk`, `record.expect_all`, `ORPHAN_NOTE.format`, `UNCLOSED_NOTE.format`.

### `ScopeBalanceCheck._walk` - L70-L117

```python
_walk(self, view)
```

One pass over the PROCEDURE DIVISION, depth per paragraph.

Observed calls (lexical order): `any`, `self._body`, `re.sub`, `re.match`, `self._is_paragraph_header`, `self._drain`, `unclosed.extend`, `body.rstrip`, `re.finditer`, `match.group`, `token.startswith`, `orphans.append`.

Control points:

- L79: `for line in view.lines`
- L80: `if not line.is_code`
- L86: `if re.match('^PROCEDURE\\s+DIVISION\\b', body)`
- L89: `if not in_procedure or not body`
- L91: `if not inside_sql and self._is_paragraph_header(body)`
- L96: `for match in re.finditer('\\bEXEC\\s+SQL\\b|\\bEND-EXEC\\b|(?<![\\w-])(?:END-IF|END-EVALUATE|IF|EVALUATE)(?![\\w-])|\\.(?=\\s|$)', body)`
- L98: `if token.startswith('EXEC')`
- L100: `if token == 'END-EXEC'`
- Another 4 conditions/loops exist in this source span.

### `ScopeBalanceCheck._body` - L121-L124

```python
_body(line) -> str
```

The logical body, uppercased, comments and blanks dropped.

Observed calls (lexical order): `getattr`, `str`, `str(getattr(line, 'logical', '') or '').strip`, `str(getattr(line, 'logical', '') or '').strip().upper`, `' '.join`, `text.split`.

### `ScopeBalanceCheck._opens` - L127-L131

```python
_opens(body: str) -> str
```

Observed calls (lexical order): `body.startswith`.

Control points:

- L128: `for verb in SCOPED_VERBS`
- L129: `if body == verb or body.startswith(verb + ' ')`

### `ScopeBalanceCheck._closes` - L134-L139

```python
_closes(body: str) -> str
```

Observed calls (lexical order): `body.rstrip`, `body.rstrip('.').strip`.

Control points:

- L136: `for verb in SCOPED_VERBS`
- L137: `if bare == f'END-{verb}'`

### `ScopeBalanceCheck._is_paragraph_header` - L142-L150

```python
_is_paragraph_header(body: str) -> bool
```

Observed calls (lexical order): `body.endswith`, `body.rstrip`, `body.rstrip('.').strip`, `word[0].isalnum`.

Control points:

- L143: `if not body.endswith('.')`
- L146: `if not word or ' ' in word`
- L148: `if word in std.NON_PARAGRAPH_WORDS`

### `ScopeBalanceCheck._drain` - L153-L160

```python
_drain(paragraph: str, depth: dict) -> list
```

Observed calls (lexical order): `depth.items`, `sorted`.

Control points:

- L154: `if not paragraph`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
