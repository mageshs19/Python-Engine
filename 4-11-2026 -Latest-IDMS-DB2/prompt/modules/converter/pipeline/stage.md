# `converter/pipeline/stage.py`

Source: [converter/pipeline/stage.py](../../../../converter/pipeline/stage.py) | 87 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `25a4471cd2512e11f9e891edf9578bc6efd243661b0b7cac11aefe1aa15718b1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> The pipeline contract.

## Module-level bindings

`__all__` (L87)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Callable, Protocol
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_steps.py](conversion/conversion_layout_steps.md)
- [converter/pipeline/conversion/conversion_pipeline_steps.py](conversion/conversion_pipeline_steps.md)
- [converter/pipeline/registry.py](registry.md)
- [converter/pipeline/run.py](run.md)

## Symbol contracts and control points

### `Document` - L23-L37

```python
class Document()
```

What flows through the pipeline. One program, one instance.

Declared class/data-model fields:

```python
cobol: str
program_id: str = ''
metadata: dict = field(default_factory=dict)
messages: list[str] = field(default_factory=list)
```

### `Document.replace` - L31-L37

```python
replace(self, cobol: str, notes: list[str] | None=None) -> 'Document'
```

Observed calls (lexical order): `Document`, `str`, `str(n).strip`.

### `Stage` - L40-L45

```python
class Stage(Protocol)
```

Declared class/data-model fields:

```python
name: str
description: str
enabled: bool
```

### `Stage.run` - L45-L45

```python
run(self, doc: Document) -> Document
```

### `FunctionStage` - L49-L59

```python
class FunctionStage()
```

A stage backed by a plain function: (str) -> (str, list\[str\]).

Declared class/data-model fields:

```python
name: str
description: str
fn: Callable[[str], tuple[str, list[str]]]
enabled: bool = True
```

### `FunctionStage.run` - L57-L59

```python
run(self, doc: Document) -> Document
```

Observed calls (lexical order): `self.fn`, `doc.replace`.

### `composer_stage` - L62-L84

```python
composer_stage(name: str, description: str, factory: Callable[[], object], method: str='compose', enabled: bool=True) -> FunctionStage
```

Adapt an EXISTING composer into a Stage. No composer changes needed.

Observed calls (lexical order): `FunctionStage`.

### `composer_stage._run` - L76-L82

```python
_run(text: str) -> tuple[str, list[str]]
```

Observed calls (lexical order): `factory`, `getattr`, `getattr(obj, method)`, `callable`, `notes`, `list`.

Control points:

- L80: `if callable(notes)`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
