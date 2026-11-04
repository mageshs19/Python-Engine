# `converter/analyzers/program_flow/flow_write_scanner.py`

Source: [converter/analyzers/program_flow/flow_write_scanner.py](../../../../../converter/analyzers/program_flow/flow_write_scanner.py) | 82 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `7d6f23d21bbfb7d3e1d76ff0ce983bd09da9994138cf6f92cc96c811b9b47e58`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Finds output WRITE statements and IDMS update verbs.

## Module-level bindings

`__all__` (L82)

## Import declarations

```python
from __future__ import annotations
from converter.analyzers.program_flow.flow_models import LogicalLine, OutputWrite
from converter.services.name_normalizer import NameNormalizer
from rules.program_flow_rules import IDMS_WRITE_VERBS, STATEMENT_TERMINATOR, WRITE_VERBS
```

## Local dependency notes

- [converter/analyzers/program_flow/flow_models.py](flow_models.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/program_flow_rules.py](../../../rules/program_flow_rules.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/__init__.py](__init__.md)
- [converter/analyzers/program_flow/program_flow_analyzer.py](program_flow_analyzer.md)

## Symbol contracts and control points

### `FlowWriteScanner` - L34-L79

```python
class FlowWriteScanner()
```

Separates file writes from IDMS update verbs.

### `FlowWriteScanner.scan` - L37-L71

```python
scan(self, lines: list[LogicalLine], paragraph_by_line: dict[int, str]) -> tuple[list[OutputWrite], list[OutputWrite]]
```

Observed calls (lexical order): `line.upper.split`, `words[0].rstrip`, `target.append`, `OutputWrite`, `self._operand`, `paragraph_by_line.get`.

Control points:

- L45: `for line in lines or []`
- L46: `if line.is_comment`
- L50: `if not words`
- L55: `if verb in WRITE_VERBS`
- L57: `if verb in IDMS_WRITE_VERBS`

### `FlowWriteScanner._operand` - L74-L79

```python
_operand(words: list[str]) -> str
```

The record name after the verb, in COBOL form.

Observed calls (lexical order): `len`, `words[1].rstrip`, `NameNormalizer.normalize`, `NameNormalizer.to_cobol`.

Control points:

- L76: `if len(words) < 2`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
