# `converter/generators/db2_infrastructure/cursor_flag_builder.py`

Source: [converter/generators/db2_infrastructure/cursor_flag_builder.py](../../../../../converter/generators/db2_infrastructure/cursor_flag_builder.py) | 64 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `1b03b8c603ea27bfea63fac7520a02f40baeb335d3d5b3d3293a61450d72f5d9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the end-of-cursor flag group for each cursor.

## Import declarations

```python
from __future__ import annotations
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from rules.db2_infrastructure_rules import CONDITION_TEMPLATE, EOC_TEMPLATE, FLAG_DECLARATION_TEMPLATE, FLAG_NAME_TEMPLATE, IND_88_LEVEL, NOT_EOC_TEMPLATE, VALUE_EOC, VALUE_NOT_EOC
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_spec.py](cursor_spec.md)
- [rules/db2_infrastructure_rules.py](../../../rules/db2_infrastructure_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](infrastructure_block_builder.md)

## Symbol contracts and control points

### `CursorFlagBuilder` - L29-L64

```python
class CursorFlagBuilder()
```

Renders one flag group per cursor.

### `CursorFlagBuilder.build` - L32-L38

```python
build(self, specs: list[CursorSpec]) -> list[str]
```

Observed calls (lexical order): `lines.extend`, `self._group`.

Control points:

- L35: `for spec in specs or []`

### `CursorFlagBuilder._group` - L43-L64

```python
_group(self, spec: CursorSpec) -> list[str]
```

Observed calls (lexical order): `FLAG_DECLARATION_TEMPLATE.format`, `FLAG_NAME_TEMPLATE.format`, `CONDITION_TEMPLATE.format`, `NOT_EOC_TEMPLATE.format`, `EOC_TEMPLATE.format`.

Control points:

- L44: `if not spec.cursor_name`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
