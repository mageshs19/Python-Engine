# `converter/composers/schema_date_transfer_composer.py`

Source: [converter/composers/schema_date_transfer_composer.py](../../../../converter/composers/schema_date_transfer_composer.py) | 117 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `fdc77ea4b3001dde6f77a90412b610dc1ed1ec75f753572fcf0e82e305c09dd4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Source-/schema-proven DB2 DATE to legacy eight-byte record moves.

## Module-level bindings

`MOVE` (L16), `__all__` (L117)

## Import declarations

```python
from __future__ import annotations
import re
from converter.composers.db2_date_working_storage_manager import Db2DateWorkingStorageManager
from converter.composers.db2_date_line_utils import Db2DateLineUtils
from converter.services.fixed_format_line_service import FixedFormatLineService
from converter.services.name_normalizer import NameNormalizer
```

## Local dependency notes

- [converter/composers/db2_date_line_utils.py](db2_date_line_utils.md)
- [converter/composers/db2_date_working_storage_manager.py](db2_date_working_storage_manager.md)
- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [converter/services/name_normalizer.py](../services/name_normalizer.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline.py](../pipeline/conversion/conversion_pipeline.md)
- [tests/test_schema_driven_4310_generic_rules.py](../../tests/test_schema_driven_4310_generic_rules.md)

## Symbol contracts and control points

### `SchemaDateTransferComposer` - L22-L115

```python
class SchemaDateTransferComposer()
```

### `SchemaDateTransferComposer.__init__` - L23-L29

```python
__init__(self, dclgen_columns=(), copybook_repository=None)
```

Observed calls (lexical order): `list`, `Db2DateLineUtils`, `FixedFormatLineService`, `Db2DateWorkingStorageManager`.

### `SchemaDateTransferComposer._schema_date` - L31-L38

```python
_schema_date(self, field: str, group: str) -> bool
```

Observed calls (lexical order): `NameNormalizer.normalize`, `NameNormalizer.to_cobol`, `bool`, `len`, `matches[0].db2_type.upper`, `re.match`, `matches[0].cobol_picture.strip`, `matches[0].cobol_picture.strip().upper`.

### `SchemaDateTransferComposer._eight_byte_output` - L40-L45

```python
_eight_byte_output(self, target: str) -> bool
```

Observed calls (lexical order): `repo.find`, `repo.group_width_for`.

Control points:

- L42: `if repo is None or repo.find(target) is None`

### `SchemaDateTransferComposer._body` - L48-L55

```python
_body(line: str) -> str
```

Observed calls (lexical order): `len`, `line[:6].isdigit`, `line[7:72].strip`, `line.lstrip`, `line.lstrip().startswith`, `line.strip`.

Control points:

- L49: `if len(line) >= 7 and line[:6].isdigit()`
- L50: `if line[6:7] in ('*', '/', 'D', 'd')`
- L53: `if line.lstrip().startswith(('*', '/'))`

### `SchemaDateTransferComposer._replacement` - L57-L76

```python
_replacement(self, field, group, target, copy)
```

Observed calls (lexical order): `self.renderer.emit`.

### `SchemaDateTransferComposer.compose` - L78-L115

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self.messages.clear`, `text.splitlines`, `len`, `self._body`, `re.match`, `output.append`, `parts[-1].endswith`, `parts.append`, `' '.join`, `' '.join(parts).upper`, `MOVE.fullmatch`, `match.groupdict`, `self._schema_date`, `self._eight_byte_output`, `output.extend`, `self._replacement`.
Another 5 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L80: `if not text`
- L87: `while i < len(lines)`
- L89: `if re.match('^PROCEDURE\\s+DIVISION\\b', body, re.I)`
- L91: `if not in_procedure or not re.match('^MOVE\\s+', body, re.I)`
- L96: `while j + 1 < len(lines) and (not parts[-1].endswith('.')) and (j - i < 6)`
- L98: `if not nxt or re.match('^(?:MOVE|IF|ELSE|END-|EVALUATE|PERFORM|EXEC)\\b', nxt, re.I)`
- L102: `if not match`
- L105: `if not (self._schema_date(info['field'], info['group']) and self._eight_byte_output(info['target']))`
- Another 1 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
