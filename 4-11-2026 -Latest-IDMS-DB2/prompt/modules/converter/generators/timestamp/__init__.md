# `converter/generators/timestamp/__init__.py`

Source: [converter/generators/timestamp/__init__.py](../../../../../converter/generators/timestamp/__init__.py) | 31 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `4a8341ecc43a24dc900bcea2349baaa52e8c89d90df95a4c8799aeda3d50f940`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`__all__` (L23)

## Import declarations

```python
from __future__ import annotations
from converter.generators.timestamp.cs_program_declarator import CsProgramDeclarator
from converter.generators.timestamp.program_id_resolver import ProgramIdResolver
from converter.generators.timestamp.program_name_binder import ProgramNameBinder
from converter.generators.timestamp.timestamp_anchors import NOT_FOUND, TimestampAnchors
from converter.generators.timestamp.timestamp_paragraph_builder import TimestampParagraphBuilder
from converter.generators.timestamp.timestamp_ws_builder import TimestampWorkingStorageBuilder
```

## Local dependency notes

- [converter/generators/timestamp/cs_program_declarator.py](cs_program_declarator.md)
- [converter/generators/timestamp/program_id_resolver.py](program_id_resolver.md)
- [converter/generators/timestamp/program_name_binder.py](program_name_binder.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp_anchors.md)
- [converter/generators/timestamp/timestamp_paragraph_builder.py](timestamp_paragraph_builder.md)
- [converter/generators/timestamp/timestamp_ws_builder.py](timestamp_ws_builder.md)

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
