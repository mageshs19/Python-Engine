# `converter/pipeline/lrf_cursor_fix.py`

Source: [converter/pipeline/lrf_cursor_fix.py](../../../../converter/pipeline/lrf_cursor_fix.py) | 161 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `d3369bef8a5b43289451f24e4ae3d0dd787dd8407b3683abd2586842d5287466`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> LRF Cursor WHERE Clause Fix - Production Deployment Guide

## Import declarations

```python
from __future__ import annotations
from typing import TYPE_CHECKING
from converter.pipeline.conversion.conversion_context import ConversionContext
from converter.resolvers.lrf_cursor_where_resolver import LrfCursorWhereResolver
from converter.generators.db2_infrastructure.cursor_spec_builder_lrf_patch import integrate_lrf_support_into_cursor_spec_builder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/cursor_spec_builder_lrf_patch.py](../generators/db2_infrastructure/cursor_spec_builder_lrf_patch.md)
- [converter/resolvers/lrf_cursor_where_resolver.py](../resolvers/lrf_cursor_where_resolver.md)

## Symbol contracts and control points

### `create_lrf_cursor_where_resolver` - L27-L54

```python
create_lrf_cursor_where_resolver(relationship_resolver, cursor_column_resolver, host_variable_resolver, mapping_repository)
```

Factory function to create and configure LrfCursorWhereResolver.

Observed calls (lexical order): `LrfCursorWhereResolver`.

### `setup_lrf_cursor_where_resolution` - L57-L140

```python
setup_lrf_cursor_where_resolution(db2_infrastructure_generator) -> bool
```

Activate LRF cursor WHERE clause generation in the pipeline.

Observed calls (lexical order): `all`, `create_lrf_cursor_where_resolver`, `integrate_lrf_support_into_cursor_spec_builder`.

Control points:

- L115: `if not all([relationship_resolver, cursor_column_resolver, host_variable_resolver])`

### `setup_lrf_cursor_fix_for_context` - L143-L161

```python
setup_lrf_cursor_fix_for_context(context: ConversionContext) -> bool
```

Setup LRF cursor fix in the conversion context.

Observed calls (lexical order): `context.component_factory.get_component`, `setup_lrf_cursor_where_resolution`.

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
