# `patterns/cobol_patterns.py`

Source: [patterns/cobol_patterns.py](../../../patterns/cobol_patterns.py) | 279 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `3331788f31a105ba3c9e19cae5df5c5db5df4fd7be6ac2b9d0220e2b7b2aabec`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL regex patterns.

## Module-level bindings

`PROGRAM_ID_PATTERN` (L16), `DIVISION_PATTERN` (L24), `IDENTIFICATION_DIVISION_PATTERN` (L34), `ENVIRONMENT_DIVISION_PATTERN` (L42), `DATA_DIVISION_PATTERN` (L50), `PROCEDURE_DIVISION_PATTERN` (L58), `WORKING_STORAGE_PATTERN` (L66), `LINKAGE_SECTION_PATTERN` (L74), `SECTION_PATTERN` (L82), `PARAGRAPH_PATTERN` (L90), `END_PROGRAM_PATTERN` (L98), `STOP_RUN_PATTERN` (L106), `GOBACK_PATTERN` (L114), `COMMENT_OR_SKIP_PATTERN` (L122), `COMMENT_PATTERN` (L130), `PAGE_EJECT_PATTERN` (L138), `SEQUENCE_ONLY_PATTERN` (L146), `LEFT_SEQUENCE_PATTERN` (L154), `RIGHT_SEQUENCE_PATTERN` (L162), `DATA_ENTRY_START_PATTERN` (L170), `FILE_DESCRIPTOR_PATTERN` (L181), `SELECT_FILE_PATTERN` (L189), `SQL_ERROR_PARAGRAPH_PATTERN` (L197), `SQL_ERROR_DOT_PATTERN` (L205), `DB2_INFRASTRUCTURE_MARKER_PATTERN` (L213), `NON_PARAGRAPH_SINGLE_WORDS` (L221), `PROGRAM_NAME_LITERAL_MOVE_PATTERN` (L276)

## Import declarations

```python
import re
```

## Importers (8)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/analyzers/program_flow/flow_paragraph_scanner.py](../converter/analyzers/program_flow/flow_paragraph_scanner.md)
- [converter/composers/counter_declaration/counter_totals_writer.py](../converter/composers/counter_declaration/counter_totals_writer.md)
- [converter/generators/procedure_division_organizer.py](../converter/generators/procedure_division_organizer.md)
- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/services/program_paragraph_analyzer.py](../converter/services/program_paragraph_analyzer.md)
- [converter/transformers/cobol_program_id_transformer.py](../converter/transformers/cobol_program_id_transformer.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)
- [tests/test_patterns.py](../tests/test_patterns.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
