# `patterns/cursor_rules.py`

Source: [patterns/cursor_rules.py](../../../patterns/cursor_rules.py) | 45 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `35505f08acab638c6b18fc88180de641976d7ec28ea4616dcc5fec082ae12d3b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor generation rules.

## Module-level bindings

`CURSOR_AUTHORITY_RULES` (L6), `CURSOR_PARAGRAPH_NUMBERING` (L14)

## Symbol contracts and control points

### `cursor_paragraph_number` - L33-L45

```python
cursor_paragraph_number(cursor_order: int, operation: str) -> int
```

Observed calls (lexical order): `str`, `str(operation or '').strip`, `str(operation or '').strip().lower`, `ValueError`.

Control points:

- L39: `if cursor_order not in CURSOR_PARAGRAPH_NUMBERING`
- L42: `if operation_key not in CURSOR_PARAGRAPH_NUMBERING[cursor_order]`

Explicit raises: `ValueError(f'Unsupported cursor order: {cursor_order}')`; `ValueError(f'Unsupported cursor operation: {operation}')`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
