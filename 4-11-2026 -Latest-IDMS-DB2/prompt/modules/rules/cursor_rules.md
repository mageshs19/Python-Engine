# `rules/cursor_rules.py`

Source: [rules/cursor_rules.py](../../../rules/cursor_rules.py) | 58 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `88d56aae0744a7c588581189917d78e7c7bca6fb2ca0ec1fd9de787d81165e87`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor generation rules.

## Module-level bindings

`CURSOR_AUTHORITY_RULES` (L12), `CURSOR_PARAGRAPH_BASE` (L24), `CURSOR_PARAGRAPH_ORDER_STRIDE` (L25), `CURSOR_OPERATION_OFFSETS` (L26)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/lifecycle_standardization_composer.py](../converter/composers/lifecycle_standardization_composer.md)
- [converter/generators/db2_infrastructure_generator.py](../converter/generators/db2_infrastructure_generator.md)
- [converter/resolvers/cursor_name_resolver.py](../converter/resolvers/cursor_name_resolver.md)
- [tests/test_generic_cursor_numbering_and_perform_integrity.py](../tests/test_generic_cursor_numbering_and_perform_integrity.md)

## Symbol contracts and control points

### `cursor_paragraph_number` - L33-L58

```python
cursor_paragraph_number(cursor_order: int, operation: str) -> int
```

Return the stable four-digit paragraph number for a cursor operation.

Observed calls (lexical order): `int`, `ValueError`, `str`, `str(operation or '').strip`, `str(operation or '').strip().lower`.

Control points:

- L47: `if order < 1`
- L51: `if operation_key not in CURSOR_OPERATION_OFFSETS`

Explicit raises: `ValueError(f'Invalid cursor order: {cursor_order}')`; `ValueError(f'Unsupported cursor order: {cursor_order}')`; `ValueError(f'Unsupported cursor operation: {operation}')`.

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
