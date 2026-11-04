# `converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.py`

Source: [converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.py](../../../../../../converter/generators/db2_infrastructure/cursor_declare/declare_operand_parser.py) | 106 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `62329ea7268dadf140d0d4e089171ddd17b08e395be9bb7dc58ce3c8d1f65b9d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Reads the COLUMN out of a free-text SQL fragment.

## Module-level bindings

`__all__` (L106)

## Import declarations

```python
from __future__ import annotations
from rules.cursor_declaration_rules import HOST_VARIABLE_PREFIX, OPERAND_QUALIFIER_SEPARATOR, OPERAND_TRIM_CHARACTERS, ORDER_BY_DIRECTIONS, SYMBOL_OPERATORS
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](../../../../rules/cursor_declaration_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_declare/declare_column_ownership.py](declare_column_ownership.md)
- [converter/generators/db2_infrastructure/cursor_declare/declare_order_by_planner.py](declare_order_by_planner.md)

## Symbol contracts and control points

### `DeclareOperandParser` - L40-L103

```python
class DeclareOperandParser()
```

Stateless operand reader.

### `DeclareOperandParser.left_operand` - L44-L68

```python
left_operand(cls, condition: str) -> str
```

The column on the left of a predicate, bare and unqualified.

Observed calls (lexical order): `str`, `str(condition or '').strip`, `len`, `text.find`, `min`, `text[:cut].strip`, `head.split`, `cls.bare_column`.

Control points:

- L51: `if not text`
- L55: `for token in SYMBOL_OPERATORS`
- L57: `if position >= 0`
- L61: `if not head`
- L65: `if not words`

### `DeclareOperandParser.order_by_column` - L71-L88

```python
order_by_column(cls, entry: str) -> str
```

The bare COLUMN part of '<column> \[ASC\|DESC\]'.

Observed calls (lexical order): `str`, `str(entry or '').strip`, `str(entry or '').strip().split`, `str(value or '').strip`, `str(value or '').strip().upper`, `len`, `parts[-1].upper`, `cls.bare_column`.

Control points:

- L74: `if not parts`
- L82: `if len(parts) >= 2 and parts[-1].upper() in directions`
- L85: `if not parts`

### `DeclareOperandParser.bare_column` - L91-L103

```python
bare_column(token: str) -> str
```

'T.NR_ID' -> 'NR_ID'. A host reference yields ''.

Observed calls (lexical order): `str`, `str(token or '').strip`, `str(token or '').strip().strip`, `text.startswith`, `text.rsplit`, `text.strip`.

Control points:

- L94: `if not text`
- L97: `if text.startswith(HOST_VARIABLE_PREFIX)`
- L100: `if OPERAND_QUALIFIER_SEPARATOR in text`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
