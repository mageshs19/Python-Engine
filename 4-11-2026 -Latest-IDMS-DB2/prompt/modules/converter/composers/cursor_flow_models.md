# `converter/composers/cursor_flow_models.py`

Source: [converter/composers/cursor_flow_models.py](../../../../converter/composers/cursor_flow_models.py) | 26 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `f4e48b42cd251fed47bdc6a51ed1939e87259c40fdbddc3eec50d9835c5c7066`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cursor flow domain models.

## Import declarations

```python
from dataclasses import dataclass
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cursor_flow_plan_discoverer.py](cursor_flow_plan_discoverer.md)
- [converter/composers/cursor_flow_rewriter.py](cursor_flow_rewriter.md)

## Symbol contracts and control points

### `CursorFlowPlan` - L12-L26

```python
class CursorFlowPlan()
```

Declared class/data-model fields:

```python
cursor_name: str
open_number: int
fetch_number: int
close_number: int
open_paragraph: str
fetch_paragraph: str
close_paragraph: str
eoc_condition: str
business_paragraph: str
open_index: int
fetch_index: int
business_index: int
until_index: int
close_index: int = -1
```

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
