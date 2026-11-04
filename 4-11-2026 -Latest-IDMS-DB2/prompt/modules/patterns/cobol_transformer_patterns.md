# `patterns/cobol_transformer_patterns.py`

Source: [patterns/cobol_transformer_patterns.py](../../../patterns/cobol_transformer_patterns.py) | 105 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7f777130a88f9a1f73bd20e126154585de2be6e6c1c65883771d74712894e26d`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`RIGHT_SEQUENCE_PATTERN` (L6), `LEFT_SEQUENCE_PATTERN` (L12), `RIGHT_SEQUENCE_WITH_SPACES_PATTERN` (L18), `ON_ANY_ERROR_STATUS_PATTERN` (L24), `IDMS_DECLARATIVE_PATTERNS` (L30), `IDMS_EXECUTABLE_PATTERNS` (L59), `IDMS_ABORT_PARAGRAPH_PATTERN` (L78), `EXIT_LINE_PATTERN` (L84), `FINISH_STATEMENT_PATTERN` (L90), `BIND_STATEMENT_PATTERN` (L96), `FIND_CURRENT_STATEMENT_PATTERN` (L102)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)
- [converter/transformers/cobol_transformer_line_utils.py](../converter/transformers/cobol_transformer_line_utils.md)
- [converter/transformers/idms_residual_cleanup.py](../converter/transformers/idms_residual_cleanup.md)
- [tests/test_idms_stop_semantics_preservation.py](../tests/test_idms_stop_semantics_preservation.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
