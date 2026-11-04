# `converter/resolvers/program_kind_resolver.py`

Source: [converter/resolvers/program_kind_resolver.py](../../../../converter/resolvers/program_kind_resolver.py) | 166 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `4e7d2989ca31f01ffc3cabf7fd92c00fb4fd24e500c15ef4185c78d32cb348a2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Decides whether a program is an UPDATE program, and says why.

## Module-level bindings

`_MARKER_PATTERNS` (L38), `_VERB_PATTERNS` (L44), `__all__` (L166)

## Import declarations

```python
from __future__ import annotations
from typing import Any
from patterns.program_kind_patterns import CONVERTED_WRITE_MARKER_PATTERN, IDMS_WRITE_LRF_PATTERN, IDMS_WRITE_VERB_PATTERN, KEEP_WRITE_MARKER_PATTERN
from patterns.sequence_patterns import is_fixed_format_line, logical_body
from rules.program_kind_rules import EVIDENCE_SAMPLE_LIMIT, INPUT_MAY_PROMOTE_ONLY, KIND_RETRIEVAL, KIND_UPDATE, MEASURE_KIND_FROM_SOURCE, PROGRAM_KIND_MESSAGES
```

## Local dependency notes

- [patterns/program_kind_patterns.py](../../patterns/program_kind_patterns.md)
- [patterns/sequence_patterns.py](../../patterns/sequence_patterns.md)
- [rules/program_kind_rules.py](../../rules/program_kind_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_pipeline_steps.py](../pipeline/conversion/conversion_pipeline_steps.md)
- [converter/postprocess/update_program_enhancer.py](../postprocess/update_program_enhancer.md)
- [converter/transformers/idms_statement/data_statement_converter.py](../transformers/idms_statement/data_statement_converter.md)
- [runners/batch/program_converter.py](../../runners/batch/program_converter.md)
- [runners/convert_programs.py](../../runners/convert_programs.md)

## Symbol contracts and control points

### `ProgramKindResolver` - L50-L163

```python
class ProgramKindResolver()
```

Source text in, program kind out, with evidence.

### `ProgramKindResolver.__init__` - L53-L54

```python
__init__(self) -> None
```

### `ProgramKindResolver.resolve` - L59-L95

```python
resolve(self, source_text: str, input_says_update: Any=None) -> tuple[str, list[str]]
```

Return (kind, messages). Never raises.

Observed calls (lexical order): `self._declared`, `self._say`, `list`, `self._logical_lines`, `self._write_evidence`, `len`, `self._report_evidence`.

Control points:

- L69: `if not MEASURE_KIND_FROM_SOURCE`
- L76: `if not lines`
- L84: `if evidence`
- L86: `if declared is False`
- L90: `if declared and INPUT_MAY_PROMOTE_ONLY`

### `ProgramKindResolver.is_update` - L97-L103

```python
is_update(self, source_text: str, input_says_update: Any=None) -> tuple[bool, list[str]]
```

Observed calls (lexical order): `self.resolve`.

### `ProgramKindResolver._declared` - L109-L112

```python
_declared(value: Any) -> bool | None
```

Observed calls (lexical order): `bool`.

Control points:

- L110: `if value is None`

### `ProgramKindResolver._logical_lines` - L115-L129

```python
_logical_lines(source_text: str) -> list[tuple[int, str]]
```

Observed calls (lexical order): `str`, `str(source_text or '').replace`, `str(source_text or '').replace('\r\n', '\n').replace`, `enumerate`, `raw.split`, `logical_body`, `is_fixed_format_line`, `line.strip`, `str(line).strip`, `' '.join`, `candidate.upper`, `candidate.upper().split`, `out.append`.

Control points:

- L118: `for (number, line) in enumerate(raw.split('\n'), start=1)`
- L127: `if candidate`

### `ProgramKindResolver._write_evidence` - L132-L142

```python
_write_evidence(lines: list[tuple[int, str]]) -> list[tuple[int, str]]
```

Observed calls (lexical order): `any`, `p.match`, `found.append`.

Control points:

- L136: `for (number, body) in lines`
- L137: `if any((p.match(body) for p in _MARKER_PATTERNS))`
- L140: `if any((p.match(body) for p in _VERB_PATTERNS))`

### `ProgramKindResolver._report_evidence` - L147-L154

```python
_report_evidence(self, evidence: list[tuple[int, str]], examined: int) -> None
```

Observed calls (lexical order): `len`, `self._say`.

Control points:

- L153: `for (number, body) in evidence[:EVIDENCE_SAMPLE_LIMIT]`

### `ProgramKindResolver._say` - L156-L163

```python
_say(self, key: str, **values: Any) -> None
```

Observed calls (lexical order): `PROGRAM_KIND_MESSAGES.get`, `self.messages.append`, `template.format`.

Control points:

- L158: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
