# `converter/pipeline/run.py`

Source: [converter/pipeline/run.py](../../../../converter/pipeline/run.py) | 66 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `9e37fe80b5cab50a7fc49557b94a01006457edd3084edd3b4cf99b6c8d8da6ce`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Runs the registry.

## Module-level bindings

`__all__` (L66)

## Import declarations

```python
from __future__ import annotations
from converter.pipeline.registry import PIPELINE
from converter.pipeline.stage import Document
```

## Local dependency notes

- [converter/pipeline/registry.py](registry.md)
- [converter/pipeline/stage.py](stage.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_steps.py](conversion/conversion_layout_steps.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](conversion/conversion_pipeline_steps.md)

## Symbol contracts and control points

### `run_stage` - L27-L45

```python
run_stage(name: str, doc: Document, pipeline=PIPELINE) -> Document
```

Run exactly ONE registered stage, by name.

Observed calls (lexical order): `getattr`, `stage.run`, `doc.messages.append`, `type`.

Control points:

- L33: `for stage in pipeline`
- L34: `if stage.name != name`
- L36: `if not getattr(stage, 'enabled', True)`

### `run_pipeline` - L48-L63

```python
run_pipeline(doc: Document, pipeline=PIPELINE, verbose: bool=False) -> Document
```

Run every enabled stage in registry order.

Observed calls (lexical order): `getattr`, `doc.messages.append`, `stage.run`, `type`.

Control points:

- L54: `for stage in pipeline`
- L55: `if not getattr(stage, 'enabled', True)`
- L56: `if verbose`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
