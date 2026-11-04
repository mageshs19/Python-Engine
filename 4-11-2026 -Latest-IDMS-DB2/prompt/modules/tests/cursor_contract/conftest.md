# `tests/cursor_contract/conftest.py`

Source: [tests/cursor_contract/conftest.py](../../../../tests/cursor_contract/conftest.py) | 169 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d6f27addcbcb42d90c755a65d793e436d490e6a75bbb603f3157de28bf46496b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`CURSOR` (L14), `GROUP` (L15), `TABLE` (L16), `RECORD` (L17), `SQL_ERROR` (L18), `SQL_LOCATION_SUFFIX` (L19), `COLUMNS` (L20), `HOSTS` (L21)

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.generators.cursor_paragraph.cursor_paragraph_body_builder import CursorParagraphBodyBuilder
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from rules.cursor_declaration_rules import QUERYNO_BASE, QUERYNO_STEP
```

## Local dependency notes

- [converter/generators/cursor_paragraph/cursor_paragraph_body_builder.py](../../converter/generators/cursor_paragraph/cursor_paragraph_body_builder.md)
- [converter/generators/db2_infrastructure/cursor_declare_builder.py](../../converter/generators/db2_infrastructure/cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](../../converter/generators/db2_infrastructure/cursor_spec.md)
- [rules/cursor_declaration_rules.py](../../rules/cursor_declaration_rules.md)

## Symbol contracts and control points

### `LineUtilsStub` - L27-L41

```python
class LineUtilsStub()
```

### `LineUtilsStub.and_lines` - L30-L34

```python
and_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `LineUtilsStub.comma_lines` - L37-L41

```python
comma_lines(items: list[str], indent: str) -> list[str]
```

Observed calls (lexical order): `enumerate`.

### `names` - L45-L60

```python
names() -> dict
```

Observed calls (lexical order): `list`.

### `paragraphs` - L64-L65

```python
paragraphs() -> CursorParagraphBodyBuilder
```

Observed calls (lexical order): `CursorParagraphBodyBuilder`.

### `declares` - L69-L70

```python
declares() -> CursorDeclareBuilder
```

Observed calls (lexical order): `CursorDeclareBuilder`, `LineUtilsStub`.

### `bodies` - L74-L78

```python
bodies()
```

### `bodies._bodies` - L75-L76

```python
_bodies(lines: list[str]) -> list[str]
```

Observed calls (lexical order): `line.strip`.

### `clause_index` - L82-L89

```python
clause_index()
```

### `clause_index._index` - L83-L87

```python
_index(items: list[str], token: str) -> int
```

Observed calls (lexical order): `enumerate`, `body.upper`, `body.upper().startswith`, `token.upper`.

Control points:

- L84: `for (position, body) in enumerate(items)`
- L85: `if body.upper().startswith(token.upper())`

### `has_clause` - L93-L97

```python
has_clause(clause_index)
```

### `has_clause._has` - L94-L95

```python
_has(items: list[str], token: str) -> bool
```

Observed calls (lexical order): `clause_index`.

### `when_other` - L101-L113

```python
when_other(clause_index)
```

### `when_other._branch` - L102-L111

```python
_branch(items: list[str]) -> list[str]
```

Observed calls (lexical order): `clause_index`, `len`, `range`, `items[position].upper`, `items[position].upper().startswith`.

Control points:

- L104: `if start < 0`
- L107: `for position in range(start + 1, len(items))`
- L108: `if items[position].upper().startswith('END-EVALUATE')`

### `sql_moves` - L117-L124

```python
sql_moves()
```

### `sql_moves._moves` - L118-L122

```python
_moves(items: list[str]) -> list[str]
```

Observed calls (lexical order): `body.endswith`.

### `fetch` - L128-L139

```python
fetch(paragraphs, bodies)
```

### `fetch._fetch` - L129-L137

```python
_fetch(**overrides) -> list[str]
```

Observed calls (lexical order): `list`, `arguments.update`, `bodies`, `paragraphs.fetch_paragraph`.

### `cursor_paragraph` - L143-L153

```python
cursor_paragraph(paragraphs, bodies)
```

### `cursor_paragraph._build` - L144-L151

```python
_build(shape: str, paragraph_name: str) -> list[str]
```

Observed calls (lexical order): `bodies`, `getattr`, `getattr(paragraphs, shape)`.

### `spec` - L157-L169

```python
spec()
```

### `spec._spec` - L158-L167

```python
_spec(order: int=0, **overrides) -> CursorSpec
```

Observed calls (lexical order): `list`, `source.update`, `CursorSpec.read`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
