# `converter/transformers/cobol_identification_transformer.py`

Source: [converter/transformers/cobol_identification_transformer.py](../../../../converter/transformers/cobol_identification_transformer.py) | 100 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fadc18de5481308b01b603215d994cb2a4f5f9a6ad991a8259ed5d8c1536cf4b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Replace AUTHOR and DATE-WRITTEN in IDENTIFICATION DIVISION.

## Module-level bindings

`__all__` (L100)

## Import declarations

```python
from __future__ import annotations
import re
from converter.transformers.cobol_transformer_line_utils import CobolTransformerLineUtils
from rules.manual_reference_rules import AUTHOR_TEMPLATE, DATE_WRITTEN_TEMPLATE, DEFAULT_AUTHOR, DEFAULT_DATE_WRITTEN
from rules.program_metadata_loader import get_author, get_date_written
```

## Local dependency notes

- [converter/transformers/cobol_transformer_line_utils.py](cobol_transformer_line_utils.md)
- [rules/manual_reference_rules.py](../../rules/manual_reference_rules.md)
- [rules/program_metadata_loader.py](../../rules/program_metadata_loader.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](cobol_transformer.md)

## Symbol contracts and control points

### `CobolIdentificationTransformer` - L25-L97

```python
class CobolIdentificationTransformer()
```

Replaces AUTHOR and DATE-WRITTEN in IDENTIFICATION DIVISION.

### `CobolIdentificationTransformer.__init__` - L28-L33

```python
__init__(self, line_utils: CobolTransformerLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolTransformerLineUtils`.

### `CobolIdentificationTransformer.reset` - L35-L37

```python
reset(self) -> None
```

Clear per-program state.

### `CobolIdentificationTransformer.author_replacement` - L39-L67

```python
author_replacement(self, *, original_line: str, logical_line: str) -> str | None
```

Replace AUTHOR line with configured author name.

Observed calls (lexical order): `get_author`, `re.search`, `AUTHOR_TEMPLATE.format`, `self.line_utils.replace_logical_body`.

Control points:

- L55: `if not author`
- L59: `if not re.search('AUTHOR\\.', logical_line, re.IGNORECASE)`

### `CobolIdentificationTransformer.date_written_replacement` - L69-L97

```python
date_written_replacement(self, *, original_line: str, logical_line: str) -> str | None
```

Replace DATE-WRITTEN line with configured date.

Observed calls (lexical order): `get_date_written`, `re.search`, `DATE_WRITTEN_TEMPLATE.format`, `self.line_utils.replace_logical_body`.

Control points:

- L85: `if not date_written`
- L89: `if not re.search('DATE-WRITTEN\\.', logical_line, re.IGNORECASE)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
