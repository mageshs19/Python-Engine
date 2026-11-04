# `review/engine/cobol_view.py`

Source: [review/engine/cobol_view.py](../../../../review/engine/cobol_view.py) | 194 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `d29e0c8109378207e5f8f96f36ad23f3f44b30d3eac681fdcc5bb72fcae0bdda`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only fixed-format COBOL inspection.

## Module-level bindings

`WIDTH` (L12), `IND` (L13), `COMMENTS` (L16), `VALID_INDICATORS` (L17), `AREA_B_MIN` (L18), `_SEQ_IN_BODY` (L20)

## Import declarations

```python
from __future__ import annotations
import re
from dataclasses import dataclass
```

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [review/checks/chk_29_lr_status_field_replacement.py](../checks/chk_29_lr_status_field_replacement.md)
- [review/engine/check_base.py](check_base.md)
- [review/engine/reviewer.py](reviewer.md)
- [tests/test_business_parity_review_rules_v128.py](../../tests/test_business_parity_review_rules_v128.md)
- [tests/test_generic_scope_and_reference_v129.py](../../tests/test_generic_scope_and_reference_v129.md)

## Symbol contracts and control points

### `Line` - L24-L79

```python
class Line()
```

Declared class/data-model fields:

```python
number: int
raw: str
```

### `Line.is_fixed` - L29-L34

```python
is_fixed(self) -> bool
```

Observed calls (lexical order): `len`, `self.raw[0:6].isdigit`, `self.raw[RSEQ_A:RSEQ_B].isdigit`.

### `Line.left_sequence` - L37-L38

```python
left_sequence(self) -> str
```

### `Line.right_sequence` - L41-L42

```python
right_sequence(self) -> str
```

### `Line.indicator` - L45-L46

```python
indicator(self) -> str
```

Observed calls (lexical order): `len`.

### `Line.body` - L49-L50

```python
body(self) -> str
```

### `Line.logical` - L53-L54

```python
logical(self) -> str
```

Observed calls (lexical order): `self.body.strip`, `self.body.strip().upper`.

### `Line.indent` - L57-L59

```python
indent(self) -> int
```

Observed calls (lexical order): `b.lstrip`, `len`.

### `Line.is_blank` - L62-L63

```python
is_blank(self) -> bool
```

Observed calls (lexical order): `self.body.strip`.

### `Line.is_comment` - L66-L67

```python
is_comment(self) -> bool
```

Observed calls (lexical order): `self.body.lstrip`, `self.body.lstrip().startswith`.

### `Line.is_code` - L70-L71

```python
is_code(self) -> bool
```

### `Line.has_sequence_in_body` - L74-L75

```python
has_sequence_in_body(self) -> bool
```

Observed calls (lexical order): `_SEQ_IN_BODY.match`, `bool`.

### `Line.overflow` - L78-L79

```python
overflow(self) -> str
```

### `CobolView` - L82-L194

```python
class CobolView()
```

### `CobolView.__init__` - L83-L85

```python
__init__(self, text: str) -> None
```

Observed calls (lexical order): `str`, `str(text or '').replace`, `str(text or '').replace('\r\n', '\n').replace`, `Line`, `clean.split`, `enumerate`.

### `CobolView.populated` - L88-L89

```python
populated(self) -> list[Line]
```

Observed calls (lexical order): `l.raw.strip`.

### `CobolView.code` - L92-L93

```python
code(self) -> list[Line]
```

### `CobolView.comments` - L96-L97

```python
comments(self) -> list[Line]
```

### `CobolView.code_text` - L100-L101

```python
code_text(self) -> str
```

Observed calls (lexical order): `'\n'.join`.

### `CobolView.all_text` - L104-L105

```python
all_text(self) -> str
```

Observed calls (lexical order): `'\n'.join`.

### `CobolView.is_empty` - L108-L109

```python
is_empty(self) -> bool
```

Observed calls (lexical order): `any`, `l.raw.strip`.

### `CobolView.has_code_token` - L112-L113

```python
has_code_token(self, token: str) -> bool
```

Observed calls (lexical order): `str`, `str(token).upper`.

### `CobolView.has_token` - L115-L116

```python
has_token(self, token: str) -> bool
```

Observed calls (lexical order): `str`, `str(token).upper`.

### `CobolView.has_comment` - L118-L132

```python
has_comment(self, token: str) -> bool
```

True when any COMMENT line contains the token.

Observed calls (lexical order): `str`, `str(token or '').strip`, `str(token or '').strip().upper`, `any`, `line.logical.upper`.

Control points:

- L130: `if not needle`

### `CobolView.logical_text` - L134-L143

```python
logical_text(self) -> str
```

Whole program as logical lines, one per row.

Observed calls (lexical order): `'\n'.join`.

### `CobolView.code_with` - L145-L147

```python
code_with(self, token: str) -> list[Line]
```

Observed calls (lexical order): `str`, `str(token).upper`.

### `CobolView.starting_with` - L149-L151

```python
starting_with(self, prefix: str) -> list[Line]
```

Observed calls (lexical order): `str`, `str(prefix).upper`, `l.logical.startswith`.

### `CobolView.matching` - L153-L154

```python
matching(self, pattern: re.Pattern) -> list[Line]
```

Observed calls (lexical order): `pattern.match`.

### `CobolView.searching` - L156-L157

```python
searching(self, pattern: re.Pattern) -> list[Line]
```

Observed calls (lexical order): `pattern.search`.

### `CobolView.exact` - L159-L161

```python
exact(self, text: str) -> list[Line]
```

Observed calls (lexical order): `str`, `str(text).strip`, `str(text).strip().upper`.

### `CobolView.count_of` - L163-L164

```python
count_of(self, text: str) -> int
```

Observed calls (lexical order): `self.all_text.count`, `str`, `str(text).upper`.

### `CobolView.first_group` - L166-L171

```python
first_group(self, pattern: re.Pattern, group: str) -> str
```

Observed calls (lexical order): `pattern.match`, `m.group`.

Control points:

- L167: `for l in self.code`
- L169: `if m`

### `CobolView.paragraph_exists` - L173-L174

```python
paragraph_exists(self, name: str) -> bool
```

Observed calls (lexical order): `bool`, `self.exact`, `str`, `str(name).upper`.

### `CobolView.sequence` - L177-L185

```python
sequence(self, right: bool=False) -> list[int]
```

Observed calls (lexical order): `v.isdigit`, `int`, `out.append`.

Control points:

- L179: `for l in self.lines`
- L180: `if not l.is_fixed`
- L183: `if v.isdigit()`

### `CobolView.constant_step` - L188-L194

```python
constant_step(values: list[int]) -> int | None
```

Observed calls (lexical order): `len`, `all`, `zip`.

Control points:

- L189: `if len(values) < 2`
- L192: `if step <= 0`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
