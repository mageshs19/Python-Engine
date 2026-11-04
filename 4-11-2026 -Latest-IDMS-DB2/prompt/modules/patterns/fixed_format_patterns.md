# `patterns/fixed_format_patterns.py`

Source: [patterns/fixed_format_patterns.py](../../../patterns/fixed_format_patterns.py) | 103 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `4d0580e7be2af1a92d9bf8c6565f2312ade08dbbb1b2af76220656196837a17f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL regex patterns. These patterns are used by fixed-format composers and helpers. Keep regex definitions here instead of defining them inside composer classes.

## Module-level bindings

`LEFT_SEQUENCE_PATTERN` (L7), `RIGHT_SEQUENCE_PATTERN` (L11), `SEQUENCE_ONLY_PATTERN` (L15), `DIVISION_PATTERN` (L19), `SECTION_PATTERN` (L23), `PARAGRAPH_PATTERN` (L27), `AREA_A_PREFIX_PATTERN` (L31), `DATA_LEVEL_PATTERN` (L49), `EXEC_SQL_START_PATTERN` (L53), `EXEC_SQL_END_PATTERN` (L57), `BOOLEAN_OPERATOR_END_PATTERN` (L61), `IF_BOOLEAN_SPLIT_PATTERN` (L65), `MOVE_STATEMENT_PATTERN` (L69), `DEBUG_LINE_PATTERN` (L73), `TRUE_LEFT_SEQUENCE_PATTERN` (L82), `RIGHT_SEQUENCE_WITH_SPACES_PATTERN` (L88), `TRAILING_TIGHT_RIGHT_SEQUENCE_PATTERN` (L94), `COBOL_IDENTIFIER_TOKEN_PATTERN` (L100)

## Import declarations

```python
import re
```

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_body_formatter.py](../converter/composers/fixed_format_body_formatter.md)
- [converter/composers/fixed_format_line_composer.py](../converter/composers/fixed_format_line_composer.md)
- [converter/composers/fixed_format_line_parser.py](../converter/composers/fixed_format_line_parser.md)
- [converter/composers/fixed_format_sequence_manager.py](../converter/composers/fixed_format_sequence_manager.md)
- [converter/composers/fixed_format_sequence_stripper.py](../converter/composers/fixed_format_sequence_stripper.md)
- [converter/composers/fixed_format_wrapper.py](../converter/composers/fixed_format_wrapper.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
