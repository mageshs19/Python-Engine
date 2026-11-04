# `converter/composers/output_write/output_write_eligibility.py`

Source: [converter/composers/output_write/output_write_eligibility.py](../../../../../converter/composers/output_write/output_write_eligibility.py) | 133 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `8fea2d238a846168c24bb4a35455dad22db78a752eba7745237e91c214df869d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Decides whether one candidate block may be extracted.

## Module-level bindings

`__all__` (L133)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from converter.composers.output_write.output_write_block_finder import CandidateBlock
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.composers.output_write.output_write_scanner import OutputWriteScanner
from converter.services.name_normalizer import NameNormalizer
from rules.output_write_paragraph_rules import MINIMUM_BODY_LINES, REQUIRED_WRITE_COUNT, WRITE_PARAGRAPH_TEMPLATE
```

## Local dependency notes

- [converter/composers/output_write/output_write_block_finder.py](output_write_block_finder.md)
- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [converter/composers/output_write/output_write_scanner.py](output_write_scanner.md)
- [converter/services/name_normalizer.py](../../services/name_normalizer.md)
- [rules/output_write_paragraph_rules.py](../../../rules/output_write_paragraph_rules.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write/output_write_extractor.py](output_write_extractor.md)
- [converter/composers/output_write_paragraph_composer.py](../output_write_paragraph_composer.md)

## Symbol contracts and control points

### `Refusal` - L39-L52

```python
class Refusal()
```

A named diagnostic plus its template values.

Declared class/data-model fields:

```python
key: str = ''
values: dict = field(default_factory=dict)
```

### `Refusal.is_reportable` - L51-L52

```python
is_reportable(self) -> bool
```

Observed calls (lexical order): `bool`.

### `ExtractionPlan` - L56-L62

```python
class ExtractionPlan()
```

An accepted block and the paragraph it will become.

Declared class/data-model fields:

```python
block: CandidateBlock
paragraph: str = ''
record: str = ''
body: list[str] = field(default_factory=list)
```

### `OutputWriteEligibility` - L65-L130

```python
class OutputWriteEligibility()
```

All accept / refuse decisions for one candidate block.

### `OutputWriteEligibility.__init__` - L68-L74

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None, scanner: OutputWriteScanner | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`, `OutputWriteScanner`.

### `OutputWriteEligibility.assess` - L77-L116

```python
assess(self, lines: list[str], block: CandidateBlock, existing: set[str]) -> tuple[ExtractionPlan | None, Refusal | None]
```

(plan, refusal). Exactly one of the two is None.

Observed calls (lexical order): `block.body`, `self.scanner.write_records`, `len`, `self._wrong_write_count`, `self.lines.executable_lines`, `Refusal`, `self.scanner.already_extracted`, `NameNormalizer.to_cobol`, `WRITE_PARAGRAPH_TEMPLATE.format`, `ExtractionPlan`.

Control points:

- L87: `if len(writes) != REQUIRED_WRITE_COUNT`
- L90: `if len(self.lines.executable_lines(body)) < MINIMUM_BODY_LINES`
- L96: `if self.scanner.already_extracted(body)`
- L102: `if paragraph in existing`

### `OutputWriteEligibility._wrong_write_count` - L120-L130

```python
_wrong_write_count(block: CandidateBlock, writes: list[str]) -> Refusal
```

Two WRITEs is worth reporting; zero is just an ordinary IF.

Observed calls (lexical order): `Refusal`, `len`.

Control points:

- L125: `if not writes`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
