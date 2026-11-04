# `review/runner/workspace_inputs.py`

Source: [review/runner/workspace_inputs.py](../../../../review/runner/workspace_inputs.py) | 138 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `a04cb7c0b2eb76333347ae3a09c2fa561223245947f00a842cda30d71006617f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Read-only, per-program source/metadata adapter for production reviews.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, replace
from pathlib import Path
import re
import tempfile
from converter.parsers.cobol_parser import CobolParser
from converter.parsers.copybook_parser import CopybookParser
from converter.parsers.dclgen_parser import DclgenParser
from converter.parsers.sheet_mapping_parser import SheetMappingParser
from converter.infrastructure.local_uploaded_file import LocalUploadedFile
from converter.repositories.mapping_repository import MappingRepository
from converter.repositories.dclgen_repository import DclgenRepository
from converter.resolvers.table_name_resolver import TableNameResolver
from converter.services.name_derivation_resolver import NameDerivationResolver
from mainframe.verification.copybook_provenance import resolve_copybooks
```

## Local dependency notes

- [converter/infrastructure/local_uploaded_file.py](../../converter/infrastructure/local_uploaded_file.md)
- [converter/parsers/cobol_parser.py](../../converter/parsers/cobol_parser.md)
- [converter/parsers/copybook_parser.py](../../converter/parsers/copybook_parser.md)
- [converter/parsers/dclgen_parser.py](../../converter/parsers/dclgen_parser.md)
- [converter/parsers/sheet_mapping_parser.py](../../converter/parsers/sheet_mapping_parser.md)
- [converter/repositories/dclgen_repository.py](../../converter/repositories/dclgen_repository.md)
- [converter/repositories/mapping_repository.py](../../converter/repositories/mapping_repository.md)
- [converter/resolvers/table_name_resolver.py](../../converter/resolvers/table_name_resolver.md)
- [converter/services/name_derivation_resolver.py](../../converter/services/name_derivation_resolver.md)
- [mainframe/verification/copybook_provenance.py](../../mainframe/verification/copybook_provenance.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_semantic_release_gate.py](../../mainframe/zowe_semantic_release_gate.md)
- [review/runner/review_file.py](review_file.md)
- [tests/test_full_program_representation_audit.py](../../tests/test_full_program_representation_audit.md)

## Symbol contracts and control points

### `_read` - L25-L30

```python
_read(path: Path) -> str
```

Observed calls (lexical order): `path.read_bytes`, `raw.decode`.

### `_code` - L33-L43

```python
_code(text: str) -> str
```

Observed calls (lexical order): `text.splitlines`, `len`, `raw[:6].isdigit`, `raw[:7].isspace`, `raw.lstrip`, `raw.lstrip().startswith`, `result.append`, `'\n'.join`, `'\n'.join(result).upper`.

Control points:

- L35: `for raw in text.splitlines()`
- L36: `if len(raw) >= 7 and (raw[:6].isdigit() or raw[:7].isspace())`
- L37: `if raw[6] in '*/Dd'`
- L40: `if raw.lstrip().startswith(('*', '/'))`

### `ReviewInputs` - L47-L53

```python
class ReviewInputs()
```

Declared class/data-model fields:

```python
source: str
target_id: str
mapping_rows: list
dclgen_columns: list
copybook_fields: list
diagnostics: list[str]
```

### `WorkspaceReviewInputs` - L56-L138

```python
class WorkspaceReviewInputs()
```

### `WorkspaceReviewInputs.__init__` - L57-L83

```python
__init__(self, workspace: Path)
```

Observed calls (lexical order): `Path`, `(self.root / 'Mapping Sheet').glob`, `sorted`, `p.suffix.lower`, `len`, `self.errors.append`, `LocalUploadedFile`, `SheetMappingParser`, `SheetMappingParser().parse_uploaded_file`, `(self.root / 'DCLGen').glob`, `p.is_file`, `DclgenParser`, `DclgenParser().parse`, `_read`, `self.columns.extend`, `NameDerivationResolver`.
Another 9 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L65: `if len(sheets) != 1`
- L69: `if not self.mapping`
- L73: `for path in files`
- L75: `if not self.columns`
- L78: `for path in sorted((self.root / 'Program').glob('*.cbl'))`
- L81: `if source_id`

### `WorkspaceReviewInputs.for_program` - L85-L138

```python
for_program(self, generated: str, source_override: str='') -> ReviewInputs
```

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `_code`, `bool`, `re.search`, `list`, `self.sources.get`, `NameDerivationResolver`, `NameDerivationResolver().derive`, `notes.append`, `len`, `re.findall`, `set`, `c.table_name.upper`, `row.cobol_record_idms.upper`, `re.escape`.
Another 15 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L94: `if source_override`
- L96: `if NameDerivationResolver().derive(source_id) != target`
- L100: `if len(candidates) == 1`
- L113: `for row in self.mapping`
- L115: `if table not in tables`
- L117: `if source_records and row.cobol_record_idms.upper() not in source_records`
- L122: `if needs_sql_metadata and (not columns)`
- L124: `if needs_sql_metadata and (not rows)`
- Another 4 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
