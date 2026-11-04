# `converter/generators/db2_infrastructure/spec_builder/__init__.py`

Source: [converter/generators/db2_infrastructure/spec_builder/__init__.py](../../../../../../converter/generators/db2_infrastructure/spec_builder/__init__.py) | 7 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `9fb38be9ad968f7aeab50399e13270355c3aeea468712ef89a4c89fd38d043f6`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Public cursor-spec builder API.

## Module-level bindings

`__all__` (L7)

## Import declarations

```python
from converter.generators.db2_infrastructure.spec_builder.cursor_spec_builder import CursorSpecBuilder
```

## Local dependency notes

- [converter/generators/db2_infrastructure/spec_builder/cursor_spec_builder.py](cursor_spec_builder.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/generators/db2_infrastructure/cursor_spec_builder.py](../cursor_spec_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
