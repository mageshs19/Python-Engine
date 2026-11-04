# `converter/generators/db2_infrastructure/infrastructure_block_builder.py`

Source: [converter/generators/db2_infrastructure/infrastructure_block_builder.py](../../../../../converter/generators/db2_infrastructure/infrastructure_block_builder.py) | 221 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `b36595a6d2f4689a9c07a142451b7eac81d0568ffac567a80ae42614bae279f3`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Assembles the generated DB2 infrastructure DATA DIVISION block.

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import COMMENT_TITLE_WIDTH, DB2_CURSOR_DECLARATIONS_MARKER, DB2_CURSOR_FLAGS_MARKER, DB2_INFRASTRUCTURE_MARKER, MARKER_MESSAGES, MARKER_SHORT_FORMS, MARKER_TRUNCATION_SUFFIX, SQLCA_INCLUDE_NAME, SQLERRWS_INCLUDE_NAME
from converter.generators.db2_infrastructure.cursor_declare_builder import CursorDeclareBuilder
from converter.generators.db2_infrastructure.cursor_flag_builder import CursorFlagBuilder
from converter.generators.db2_infrastructure.cursor_spec import CursorSpec
from converter.generators.db2_infrastructure.include_renderer import IncludeRenderer
from converter.generators.db2_infrastructure.sql_location_builder import SqlLocationBuilder
```

## Local dependency notes

- [catalogs/output_sections.py](../../../catalogs/output_sections.md)
- [converter/generators/db2_infrastructure/cursor_declare_builder.py](cursor_declare_builder.md)
- [converter/generators/db2_infrastructure/cursor_flag_builder.py](cursor_flag_builder.md)
- [converter/generators/db2_infrastructure/cursor_spec.py](cursor_spec.md)
- [converter/generators/db2_infrastructure/include_renderer.py](include_renderer.md)
- [converter/generators/db2_infrastructure/sql_location_builder.py](sql_location_builder.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure_generator.py](../db2_infrastructure_generator.md)
- [tests/test_marker_banner_width.py](../../../tests/test_marker_banner_width.md)

## Symbol contracts and control points

### `InfrastructureBlockBuilder` - L71-L221

```python
class InfrastructureBlockBuilder()
```

Assembles the DB2 infrastructure block for WORKING-STORAGE.

### `InfrastructureBlockBuilder.__init__` - L74-L81

```python
__init__(self, line_utils) -> None
```

Observed calls (lexical order): `IncludeRenderer`, `SqlLocationBuilder`, `CursorFlagBuilder`, `CursorDeclareBuilder`.

### `InfrastructureBlockBuilder.build` - L85-L100

```python
build(self, include_names: list[str], cursor_specs: list[dict[str, object]]) -> str
```

Observed calls (lexical order): `CursorSpec.read_all`, `lines.extend`, `self._infrastructure_section`, `self.sql_location.build`, `self._flags_section`, `self._declarations_section`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L96: `if specs`

### `InfrastructureBlockBuilder._infrastructure_section` - L108-L123

```python
_infrastructure_section(self, include_names: list[str]) -> list[str]
```

Marker comment, then SQLERRWS, SQLCA and each DCLGEN include.

Observed calls (lexical order): `self._marker_lines`, `self.includes.render_all`.

### `InfrastructureBlockBuilder._flags_section` - L125-L130

```python
_flags_section(self, specs: list[CursorSpec]) -> list[str]
```

Observed calls (lexical order): `self._marker_lines`, `self.flags.build`.

### `InfrastructureBlockBuilder._declarations_section` - L132-L152

```python
_declarations_section(self, specs: list[CursorSpec]) -> list[str]
```

Every DECLARE, with only the final one closing the sentence.

Observed calls (lexical order): `self._marker_lines`, `len`, `enumerate`, `lines.extend`, `self.declares.build`, `lines.append`.

Control points:

- L146: `for (index, spec) in enumerate(specs)`

### `InfrastructureBlockBuilder._marker_lines` - L157-L180

```python
_marker_lines(self, title: str) -> list[str]
```

A banner comment that is guaranteed to fit columns 8-72.

Observed calls (lexical order): `self._fit_marker`, `self.line_utils.comment_block`.

Control points:

- L178: `if not fitted`

### `InfrastructureBlockBuilder._fit_marker` - L182-L207

```python
_fit_marker(self, title: str) -> str
```

The longest usable form of a marker title.

Observed calls (lexical order): `str`, `str(title or '').strip`, `len`, `MARKER_SHORT_FORMS.get`, `str(MARKER_SHORT_FORMS.get(text, '')).strip`, `self._log`, `self._truncate`.

Control points:

- L194: `if not text`
- L198: `if len(text) <= width`
- L202: `if short and len(short) <= width`

### `InfrastructureBlockBuilder._truncate` - L210-L216

```python
_truncate(title: str, width: int) -> str
```

Cut to width, keeping a visible marker that a cut happened.

Observed calls (lexical order): `str`, `len`.

Control points:

- L214: `if width <= len(suffix)`

### `InfrastructureBlockBuilder._log` - L218-L221

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `MARKER_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L220: `if template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
