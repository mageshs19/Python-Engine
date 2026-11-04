# `converter/generators/db2_infrastructure/infrastructure_patterns.py`

Source: [converter/generators/db2_infrastructure/infrastructure_patterns.py](../../../../../converter/generators/db2_infrastructure/infrastructure_patterns.py) | 26 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `a1753fc882bb7ca007c83cf911ada6bb5bd9f93dbf34ad904b5f29bd93cc99f7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL division/section regex patterns for DB2 infrastructure insertion.

## Module-level bindings

`PROCEDURE_DIVISION_PATTERN` (L8), `LINKAGE_SECTION_PATTERN` (L13), `WORKING_STORAGE_PATTERN` (L18), `DATA_DIVISION_PATTERN` (L23)

## Import declarations

```python
import re
```

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/block_inserter.py](block_inserter.md)

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
