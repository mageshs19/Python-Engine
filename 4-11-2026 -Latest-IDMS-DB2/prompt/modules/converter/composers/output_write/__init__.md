# `converter/composers/output_write/__init__.py`

Source: [converter/composers/output_write/__init__.py](../../../../../converter/composers/output_write/__init__.py) | 56 lines.
Owning logic guide: [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md).
Source SHA-256: `bcbbdb3696aabf23f9a7fd5d2834b355f8fec4e71cefa2e33ff18a0fbbc13519`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Output write paragraph extraction.

## Module-level bindings

`__all__` (L44)

## Import declarations

```python
from converter.composers.output_write.output_write_line_utils import OutputWriteLineUtils
from converter.composers.output_write.output_write_scanner import OutputWriteScanner
from converter.composers.output_write.output_write_guard import OutputWriteGuard
from converter.composers.output_write.output_write_renderer import OutputWriteRenderer
from converter.composers.output_write.output_write_block_finder import UNNAMED_PARAGRAPH, CandidateBlock, OutputWriteBlockFinder
from converter.composers.output_write.output_write_eligibility import ExtractionPlan, OutputWriteEligibility, Refusal
from converter.composers.output_write.output_write_extractor import OutputWriteExtractor
```

## Local dependency notes

- [converter/composers/output_write/output_write_block_finder.py](output_write_block_finder.md)
- [converter/composers/output_write/output_write_eligibility.py](output_write_eligibility.md)
- [converter/composers/output_write/output_write_extractor.py](output_write_extractor.md)
- [converter/composers/output_write/output_write_guard.py](output_write_guard.md)
- [converter/composers/output_write/output_write_line_utils.py](output_write_line_utils.md)
- [converter/composers/output_write/output_write_renderer.py](output_write_renderer.md)
- [converter/composers/output_write/output_write_scanner.py](output_write_scanner.md)

## Change responsibility

After modifying this Python file, review [prompt/05_SQL_CURSOR_AND_BUSINESS_FLOW.md](../../../../05_SQL_CURSOR_AND_BUSINESS_FLOW.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
