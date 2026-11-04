# `patterns/field_reference_rewriter_patterns.py`

Source: [patterns/field_reference_rewriter_patterns.py](../../../patterns/field_reference_rewriter_patterns.py) | 134 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `7fac046b2ce286a475b33f540f6593a523100e3d606a0cfb52e45ef9ea70388b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`QUALIFIED_REFERENCE_PATTERN` (L12), `EXEC_SQL_PATTERN` (L20), `END_EXEC_PATTERN` (L26), `DIVISION_PATTERN` (L32), `PARAGRAPH_PATTERN` (L38), `STRING_PATTERN` (L44), `HOST_REFERENCE_OF_PATTERN` (L50), `HOST_REFERENCE_DOT_PATTERN` (L56), `INITIALIZE_DCL_PATTERN` (L62), `GENERATED_OBTAIN_COMMENT_PATTERN` (L68), `MOVE_SPACES_TO_RECORD_PATTERN` (L75), `LEVEL_NUMBER_FIELD_PATTERN` (L82), `REDEFINES_FIELD_PATTERN` (L88), `REDEFINES_BASE_PATTERN` (L94), `COBOL_IDENTIFIER_PATTERN` (L100), `OF_IN_BEFORE_PATTERN` (L106), `OF_IN_AFTER_PATTERN` (L112), `DCL_DOT_REFERENCE_PATTERN` (L118), `HOST_OF_DCL_REFERENCE_PATTERN` (L124), `HOST_REFERENCE_OF_SPLIT_PATTERN` (L131)

## Import declarations

```python
from __future__ import annotations
import re
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/field_reference/field_reference_field_extractor.py](../converter/transformers/field_reference/field_reference_field_extractor.md)
- [converter/transformers/field_reference/field_reference_host_resolver.py](../converter/transformers/field_reference/field_reference_host_resolver.md)
- [converter/transformers/field_reference_line_utils.py](../converter/transformers/field_reference_line_utils.md)
- [converter/transformers/field_reference_record_context.py](../converter/transformers/field_reference_record_context.md)
- [converter/transformers/field_reference_replacement_engine.py](../converter/transformers/field_reference_replacement_engine.md)
- [converter/transformers/field_reference_rewriter.py](../converter/transformers/field_reference_rewriter.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
