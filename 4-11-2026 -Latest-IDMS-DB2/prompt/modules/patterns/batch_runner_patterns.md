# `patterns/batch_runner_patterns.py`

Source: [patterns/batch_runner_patterns.py](../../../patterns/batch_runner_patterns.py) | 12 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `9def7bec48bda7f563a117e374eb1c9be34227c29e8625d0491f4ca77c143966`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`COPY_NAME_PATTERN` (L9)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/conversion_actions.py](../converter/ui/conversion_actions.md)
- [runners/batch/update_postprocess_pipeline.py](../runners/batch/update_postprocess_pipeline.md)
- [runners/update/update_postprocess_pipeline.py](../runners/update/update_postprocess_pipeline.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
