# `converter/generators/cursor_declaration/legacy_banner_builder.py`

Source: [converter/generators/cursor_declaration/legacy_banner_builder.py](../../../../../converter/generators/cursor_declaration/legacy_banner_builder.py) | 65 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `70e72c67274f5a2874c86f5a5a3b99ec0a5ccb45a4d508a9bf87a164a25f9ef1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The three-line comment banner above a legacy declaration.

## Module-level bindings

`__all__` (L65)

## Import declarations

```python
from __future__ import annotations
from converter.services.name_normalizer import NameNormalizer
from rules.cursor_declaration_legacy import BANNER_NAME_TRIM, TABLE_PREFIX_LENGTH, TABLE_VIEW_SUFFIXES
from rules.manual_reference_rules import CURSOR_BANNER_BLANK, CURSOR_BANNER_TITLE_TEMPLATE, CURSOR_BANNER_UNDERLINE
```

## Local dependency notes

- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/cursor_declaration_legacy.py](../../../rules/cursor_declaration_legacy.md)
- [rules/manual_reference_rules.py](../../../rules/manual_reference_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/cursor_declaration/cursor_declaration_generator.py](cursor_declaration_generator.md)

## Symbol contracts and control points

### `LegacyBannerBuilder` - L29-L62

```python
class LegacyBannerBuilder()
```

Renders the banner. Decides nothing else.

### `LegacyBannerBuilder.banner` - L32-L39

```python
banner(self, table: str) -> list[str]
```

Observed calls (lexical order): `CURSOR_BANNER_TITLE_TEMPLATE.format`, `self.short_table_name`.

### `LegacyBannerBuilder.short_table_name` - L42-L62

```python
short_table_name(table: str) -> str
```

DZBEFFTV -> BEFF. Prefix and TV/TB suffix removed.

Observed calls (lexical order): `NameNormalizer.normalize`, `str`, `token.endswith`, `len`, `token.strip`.

Control points:

- L50: `if not full`
- L54: `for suffix in TABLE_VIEW_SUFFIXES`
- L55: `if token.endswith(suffix)`
- L59: `if len(token) > TABLE_PREFIX_LENGTH`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
