# `converter/generators/db2_infrastructure/sql_location_builder.py`

Source: [converter/generators/db2_infrastructure/sql_location_builder.py](../../../../../converter/generators/db2_infrastructure/sql_location_builder.py) | 50 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `cdf88c4d678957df242e33d01201bf10d303e97fe32ae2eacff8bc319ec7369a`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Builds the SQL-LOCATION declaration, when the site wants one.

## Import declarations

```python
from __future__ import annotations
from catalogs.output_sections import DB2_SQL_ERROR_LOCATION_MARKER, DECLARE_SQL_LOCATION_FIELD, SQL_LOCATION_FIELD_NAME, SQL_LOCATION_PICTURE
from rules.db2_infrastructure_rules import SQL_LOCATION_DECLARATION_TEMPLATE
```

## Local dependency notes

- [catalogs/output_sections.py](../../../catalogs/output_sections.md)
- [rules/db2_infrastructure_rules.py](../../../rules/db2_infrastructure_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/infrastructure_block_builder.py](infrastructure_block_builder.md)

## Symbol contracts and control points

### `SqlLocationBuilder` - L33-L50

```python
class SqlLocationBuilder()
```

Renders the SQL-LOCATION block, or nothing at all.

### `SqlLocationBuilder.__init__` - L36-L37

```python
__init__(self, line_utils) -> None
```

### `SqlLocationBuilder.build` - L39-L50

```python
build(self) -> list[str]
```

Observed calls (lexical order): `self.line_utils.comment_block`, `SQL_LOCATION_DECLARATION_TEMPLATE.format`.

Control points:

- L40: `if not DECLARE_SQL_LOCATION_FIELD`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
