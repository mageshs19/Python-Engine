# `converter/postprocess/main_flow/main_flow_line_utils.py`

Source: [converter/postprocess/main_flow/main_flow_line_utils.py](../../../../../converter/postprocess/main_flow/main_flow_line_utils.py) | 79 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `3eeb3c6c5abc8f1a53ee76377b532052b7d140bb0b668f03e293ee44034e2165`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from rules.update_restart_rules import MAIN_FLOW_AREA_B_INDENT, MAIN_FLOW_BODY_END, MAIN_FLOW_BODY_START, MAIN_FLOW_COMMENT_INDICATORS, MAIN_FLOW_FIXED_BODY_WIDTH, MAIN_FLOW_FULL_WIDTH, MAIN_FLOW_RIGHT_SEQUENCE_WIDTH, MAIN_FLOW_SEQUENCE_WIDTH, MAIN_FLOW_TOTAL_WIDTH
```

## Local dependency notes

- [rules/update_restart_rules.py](../../../rules/update_restart_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_main_flow_rewriter.py](../update_main_flow_rewriter.md)

## Symbol contracts and control points

### `MainFlowLineUtils` - L16-L79

```python
class MainFlowLineUtils()
```

Fixed-format line rendering + logical extraction.

### `MainFlowLineUtils._line_like` - L23-L54

```python
_line_like(self, *, reference_line: str, body: str) -> str
```

Observed calls (lexical order): `str`, `str(reference_line or '').rstrip`, `str(body or '').strip`, `len`, `text[:MAIN_FLOW_SEQUENCE_WIDTH].strip`, `text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit`, `body_area[:MAIN_FLOW_FIXED_BODY_WIDTH].ljust`, `body_area[:MAIN_FLOW_FIXED_BODY_WIDTH].rstrip`.

Control points:

- L27: `if len(text) >= MAIN_FLOW_FULL_WIDTH and text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit()`
- L45: `if len(text) > MAIN_FLOW_SEQUENCE_WIDTH and text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit()`

### `MainFlowLineUtils._logical` - L56-L79

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `len`, `text[:MAIN_FLOW_SEQUENCE_WIDTH].strip`, `text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit`, `text[MAIN_FLOW_BODY_START:MAIN_FLOW_BODY_END].strip`, `body.strip`, `body[-MAIN_FLOW_RIGHT_SEQUENCE_WIDTH:].strip`, `body[-MAIN_FLOW_RIGHT_SEQUENCE_WIDTH:].strip().isdigit`, `text.strip`.

Control points:

- L59: `if len(text) >= MAIN_FLOW_FULL_WIDTH and text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit()`
- L65: `if len(text) > MAIN_FLOW_SEQUENCE_WIDTH and text[:MAIN_FLOW_SEQUENCE_WIDTH].strip().isdigit()`
- L70: `if body[:1] in MAIN_FLOW_COMMENT_INDICATORS`
- L72: `if len(body) >= MAIN_FLOW_RIGHT_SEQUENCE_WIDTH and body[-MAIN_FLOW_RIGHT_SEQUENCE_WIDTH:].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
