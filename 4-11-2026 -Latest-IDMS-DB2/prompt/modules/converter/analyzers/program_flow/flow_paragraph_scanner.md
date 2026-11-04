# `converter/analyzers/program_flow/flow_paragraph_scanner.py`

Source: [converter/analyzers/program_flow/flow_paragraph_scanner.py](../../../../../converter/analyzers/program_flow/flow_paragraph_scanner.py) | 86 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `9f33858051fb6105a1a06750a7ba88006455c9eb78edd30468b9bb7f27bde37f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds PROCEDURE DIVISION paragraphs and maps lines to their owner.

## Module-level bindings

`__all__` (L86)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import LogicalLine, ParagraphSpan
from patterns.cobol_patterns import PARAGRAPH_PATTERN, PROCEDURE_DIVISION_PATTERN
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [patterns/cobol_patterns.py](../../../patterns/cobol_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowParagraphScanner` - L27-L83

```python
class FlowParagraphScanner()
```

Read-only paragraph discovery.

### `FlowParagraphScanner.spans` - L30-L71

```python
spans(self, lines: list[LogicalLine]) -> list[ParagraphSpan]
```

Observed calls (lexical order): `PROCEDURE_DIVISION_PATTERN.match`, `PARAGRAPH_PATTERN.match`, `max`, `output.append`, `ParagraphSpan`, `match.group`, `match.group('name').upper`, `current.lines.append`.

Control points:

- L35: `for line in lines or []`
- L36: `if line.is_comment`
- L40: `if not body`
- L43: `if PROCEDURE_DIVISION_PATTERN.match(body)`
- L46: `if not inside_procedure`
- L51: `if match`
- L52: `if current is not None`
- L64: `if current is not None`
- Another 1 conditions/loops exist in this source span.

### `FlowParagraphScanner.name_by_line` - L74-L83

```python
name_by_line(paragraphs: list[ParagraphSpan]) -> dict[int, str]
```

Line number -> owning paragraph name.

Observed calls (lexical order): `max`, `range`.

Control points:

- L78: `for paragraph in paragraphs or []`
- L80: `for number in range(paragraph.start_line, last + 1)`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
