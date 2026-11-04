# `converter/composers/procedure_indent/indent_models.py`

Source: [converter/composers/procedure_indent/indent_models.py](../../../../../converter/composers/procedure_indent/indent_models.py) | 191 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9acd0fc95b3b06b76cc30fc16a97652e3628f6c84df07d891bfc79aa127502ee`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Frames, the frame stack and line classification. The passive parts.

## Module-level bindings

`SELF_CLOSING_SUFFIXES` (L45), `SCOPED_CLOSING_SUFFIXES` (L46), `__all__` (L191)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from patterns.procedure_indent_patterns import PARAGRAPH_HEADER_PATTERN, SECTION_HEADER_PATTERN
from rules.procedure_indent_rules import BLOCK_KIND_EVALUATE, BLOCK_KIND_SQL, CONTINUATION_OPENERS, CONTINUATION_TRAILERS, NEST_STEP, NON_PARAGRAPH_SINGLE_WORDS, RESPECT_STATEMENT_CONTINUATIONS, SQL_BODY_OFFSET, STATEMENT_VERBS, WHEN_BODY_OFFSET, WHEN_OFFSET
```

## Local dependency notes

- [patterns/procedure_indent_patterns.py](../../../patterns/procedure_indent_patterns.md)
- [rules/procedure_indent_rules.py](../../../rules/procedure_indent_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/procedure_indent/indent_resolver.py](indent_resolver.md)
- [converter/composers/procedure_indent_normalizer.py](../procedure_indent_normalizer.md)
- [tests/test_transaction_verb_not_paragraph.py](../../../tests/test_transaction_verb_not_paragraph.md)

## Symbol contracts and control points

### `Frame` - L52-L68

```python
class Frame()
```

One open block on the indentation stack.

Declared class/data-model fields:

```python
kind: str
own_indent: int
```

### `Frame.body_indent` - L59-L64

```python
body_indent(self) -> int
```

Control points:

- L60: `if self.kind == BLOCK_KIND_EVALUATE`
- L62: `if self.kind == BLOCK_KIND_SQL`

### `Frame.when_indent` - L67-L68

```python
when_indent(self) -> int
```

### `FrameStack` - L71-L109

```python
class FrameStack()
```

Open blocks, innermost last. Tolerates a mismatched terminator.

### `FrameStack.__init__` - L74-L75

```python
__init__(self) -> None
```

### `FrameStack.__len__` - L77-L78

```python
__len__(self) -> int
```

Observed calls (lexical order): `len`.

### `FrameStack.clear` - L80-L81

```python
clear(self) -> None
```

Observed calls (lexical order): `self._frames.clear`.

### `FrameStack.push` - L83-L84

```python
push(self, kind: str, own_indent: int) -> None
```

Observed calls (lexical order): `Frame`, `self._frames.append`.

### `FrameStack.top` - L87-L88

```python
top(self) -> Frame | None
```

### `FrameStack.pop` - L90-L103

```python
pop(self, kind: str) -> Frame | None
```

Close the nearest frame of `kind`.

Observed calls (lexical order): `len`, `range`, `self._frames.pop`.

Control points:

- L97: `for index in range(len(self._frames) - 1, -1, -1)`
- L98: `if self._frames[index].kind == kind`

### `FrameStack.peek` - L105-L109

```python
peek(self, kind: str) -> Frame | None
```

Observed calls (lexical order): `len`, `range`.

Control points:

- L106: `for index in range(len(self._frames) - 1, -1, -1)`
- L107: `if self._frames[index].kind == kind`

### `LineClassifier` - L112-L188

```python
class LineClassifier()
```

Yes/no questions about one line. Owns no indent arithmetic.

### `LineClassifier.__init__` - L115-L116

```python
__init__(self, fixed_format) -> None
```

### `LineClassifier.is_untouchable` - L118-L126

```python
is_untouchable(self, line: str) -> bool
```

Comment, page-eject, debug, '-' continuation or blank.

Observed calls (lexical order): `str`, `str(line or '').strip`, `self.fixed_format.is_comment_or_control_line`, `self.fixed_format.is_continuation_line`, `self.fixed_format.is_sequence_artifact`.

Control points:

- L120: `if not str(line or '').strip()`
- L122: `if self.fixed_format.is_comment_or_control_line(line)`
- L124: `if self.fixed_format.is_continuation_line(line)`

### `LineClassifier.is_continuation` - L129-L162

```python
is_continuation(upper: str, previous_upper: str) -> bool
```

True when this line continues the statement above it.

Observed calls (lexical order): `upper.strip`, `text.rstrip`, `text.split`, `text.split()[0].rstrip`, `text.startswith`, `previous_upper.rstrip`, `previous_upper.rstrip().rstrip`, `previous.split`.

Control points:

- L142: `if not RESPECT_STATEMENT_CONTINUATIONS or not previous_upper`
- L146: `if not text`
- L149: `if text.rstrip('.') in NON_PARAGRAPH_SINGLE_WORDS`
- L152: `if text.split()[0].rstrip('.') in STATEMENT_VERBS`
- L155: `if text.startswith(CONTINUATION_OPENERS)`
- L159: `if not previous`

### `LineClassifier.is_area_a_header` - L165-L173

```python
is_area_a_header(upper: str) -> bool
```

Observed calls (lexical order): `SECTION_HEADER_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `match.group`, `match.group('name').upper`.

Control points:

- L166: `if SECTION_HEADER_PATTERN.match(upper)`
- L170: `if not match`

### `LineClassifier.is_self_closing` - L176-L181

```python
is_self_closing(upper: str) -> bool
```

A one-line block carrying its own terminator.

Observed calls (lexical order): `upper.rstrip`, `upper.rstrip('.').endswith`.

### `LineClassifier.opens_scope` - L184-L188

```python
opens_scope(upper: str) -> bool
```

A READ / SEARCH / STRING that is not already terminated.

Observed calls (lexical order): `upper.rstrip`, `upper.rstrip('.').endswith`, `upper.endswith`.

Control points:

- L186: `if upper.rstrip('.').endswith(SCOPED_CLOSING_SUFFIXES)`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
