# `converter/analyzers/program_flow/flow_line_reader.py`

Source: [converter/analyzers/program_flow/flow_line_reader.py](../../../../../converter/analyzers/program_flow/flow_line_reader.py) | 59 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `febea60fcf7828d6c880afa7cc17b193f85ccfd2043f2a9d1ffbbd1500cdc711`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Turns raw COBOL records into LogicalLine values.

## Module-level bindings

`INDICATOR_COLUMN` (L22), `COMMENT_INDICATORS` (L23), `__all__` (L59)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import LogicalLine
from patterns.sequence_patterns import strip_sequence_numbers
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowLineReader` - L26-L56

```python
class FlowLineReader()
```

Reads a program into classified logical lines.

### `FlowLineReader.read` - L29-L43

```python
read(self, cobol_text: str) -> list[LogicalLine]
```

Observed calls (lexical order): `enumerate`, `str`, `str(cobol_text or '').splitlines`, `raw.rstrip`, `output.append`, `LogicalLine`, `strip_sequence_numbers`, `self._is_comment`.

Control points:

- L32: `for (number, raw) in enumerate(str(cobol_text or '').splitlines(), start=1)`

### `FlowLineReader.code_only` - L46-L48

```python
code_only(lines: list[LogicalLine]) -> list[LogicalLine]
```

Executable lines only. Comments and blanks removed.

### `FlowLineReader._is_comment` - L51-L56

```python
_is_comment(record: str) -> bool
```

Column 7 of a sequenced record, else a leading indicator.

Observed calls (lexical order): `str`, `len`, `text[:INDICATOR_COLUMN].strip`, `text[:INDICATOR_COLUMN].strip().isdigit`, `text.lstrip`.

Control points:

- L54: `if len(text) > INDICATOR_COLUMN and text[:INDICATOR_COLUMN].strip().isdigit()`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
