# `converter/composers/output_write/output_write_extractor.py`

Source: [converter/composers/output_write/output_write_extractor.py](../../../../../converter/composers/output_write/output_write_extractor.py) | 143 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `44c441d6582244120a190a8e5161a0ee32e204edad66abfb7a06206e942262ae`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Performs one accepted extraction.

## Module-level bindings

`__all__` (L143)

## Import declarations

```python
from __future__ import annotations
import re
from converter.services.perform_thru_scope import perform_spans, paragraph_indices
from converter.composers.output_write.output_write_eligibility import ExtractionPlan
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.composers.output_write.output_write_renderer import OutputWriteRenderer
from converter.composers.output_write.output_write_scanner import OutputWriteScanner
```

## Local dependency notes

- [converter/composers/output_write/output_write_eligibility.py](output_write_eligibility.md)
- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [converter/composers/output_write/output_write_renderer.py](output_write_renderer.md)
- [converter/composers/output_write/output_write_scanner.py](output_write_scanner.md)
- [converter/services/perform_thru_scope.py](../../services/perform_thru_scope.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/output_write/__init__.py](__init__.md)
- [converter/composers/output_write_paragraph_composer.py](../output_write_paragraph_composer.md)

## Symbol contracts and control points

### `OutputWriteExtractor` - L34-L140

```python
class OutputWriteExtractor()
```

Splices the call site in and the new paragraph after.

### `OutputWriteExtractor.__init__` - L37-L45

```python
__init__(self, line_utils: OutputWriteLineUtils | None=None, renderer: OutputWriteRenderer | None=None, scanner: OutputWriteScanner | None=None) -> None
```

Observed calls (lexical order): `OutputWriteLineUtils`, `OutputWriteRenderer`, `OutputWriteScanner`.

### `OutputWriteExtractor.apply` - L48-L87

```python
apply(self, lines: list[str], plan: ExtractionPlan) -> None
```

Rewrite `lines` in place for one accepted plan.

Observed calls (lexical order): `self.lines.template_line`, `self.renderer.call_site_lines`, `self.lines.call_indent`, `self.renderer.paragraph_lines`, `self._per_write_reset`, `next`, `enumerate`, `self.lines.paragraph_name`, `paragraph_block.insert`, `self._insert_index`, `len`.

Control points:

- L68: `if reset`
- L74: `if heading_index is not None`

### `OutputWriteExtractor._insert_index` - L90-L112

```python
_insert_index(self, *, lines: list[str], end_index: int, shift: int) -> int
```

Index just past the paragraph that held the extracted block.

Observed calls (lexical order): `self.scanner.paragraph_end_index`, `paragraph_indices`, `perform_spans`, `max`.

Control points:

- L107: `for span in containing`

### `OutputWriteExtractor._per_write_reset` - L114-L140

```python
_per_write_reset(self, lines: list[str], plan: ExtractionPlan) -> str
```

Preserve a source-proven fixed output-buffer clear per WRITE.

Observed calls (lexical order): `' '.join`, `self.lines.logical`, `re.search`, `write.group`, `re.escape`, `next`, `self.lines.clone`.

Control points:

- L125: `if not write`
- L128: `if re.search(f'\\bMOVE\\s+SPACES?\\s+TO\\s+{re.escape(group)}\\b', body)`
- L138: `if original is None`

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
