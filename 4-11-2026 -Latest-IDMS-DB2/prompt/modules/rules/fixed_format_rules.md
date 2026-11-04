# `rules/fixed_format_rules.py`

Source: [rules/fixed_format_rules.py](../../../rules/fixed_format_rules.py) | 351 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `0dbeba9cdb81fba19fe4453bb64a1f341039b0becf7c420199bc0086c3c2f339`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Configuration, import facade, constants, or module-level wiring. Inspect its imports and top-level bindings below; do not infer runtime activity from its filename.

## Module-level bindings

`LEFT_SEQUENCE_START` (L22), `LEFT_SEQUENCE_END` (L23), `INDICATOR_INDEX` (L24), `BODY_START` (L25), `BODY_END` (L26), `RIGHT_SEQUENCE_START` (L27), `RIGHT_SEQUENCE_END` (L28), `LEFT_SEQUENCE_WIDTH` (L30), `INDICATOR_WIDTH` (L31), `BODY_WIDTH` (L32), `RIGHT_SEQUENCE_WIDTH` (L33), `TOTAL_WIDTH` (L34), `MIN_ADDRESSABLE_LENGTH` (L39), `LINE_ENDINGS` (L43), `DEFAULT_LEFT_START` (L53), `DEFAULT_LEFT_STEP` (L54), `DEFAULT_RIGHT_START` (L55), `DEFAULT_RIGHT_STEP` (L56), `AREA_A_INDENT` (L63), `AREA_B_INDENT` (L64), `SQL_INDENT` (L65), `SQL_CONTINUATION_INDENT` (L66), `SPACE_INDICATOR` (L71), `COMMENT_INDICATOR` (L72), `PAGE_INDICATOR` (L73), `DEBUG_INDICATOR` (L74), `DEBUG_INDICATOR_LOWER` (L75), `CONTINUATION_INDICATOR` (L76), `VALID_INDICATORS` (L78), `PRESERVE_VERBATIM_INDICATORS` (L88), `PROCEDURE_DIVISION_NAME` (L98), `NON_PARAGRAPH_WORDS` (L100), `PROCEDURE_VERBS` (L166), `COBOL_STATEMENT_STARTERS` (L229), `RIGHT_SEQUENCE_GENERATED_PREFIX` (L256), `SQL_LEVEL_1_KEYWORDS` (L261), `SQL_LEVEL_2_KEYWORDS` (L283), `AREA_A_HEADER_PREFIXES` (L292), `AREA_A_DATA_LEVELS` (L301), `AREA_B_DATA_LEVELS` (L307), `WRAP_IF_PREFIX` (L319), `WRAP_MOVE_PREFIX` (L320), `WRAP_TO_PREFIX` (L321), `BOOLEAN_OPERATOR_WORDS` (L323), `QUALIFIER_CONNECTOR_WORDS` (L328), `FIXED_FORMAT_MESSAGES` (L337)

## Importers (9)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_body_formatter.py](../converter/composers/fixed_format_body_formatter.md)
- [converter/composers/fixed_format_composer.py](../converter/composers/fixed_format_composer.md)
- [converter/composers/fixed_format_line_composer.py](../converter/composers/fixed_format_line_composer.md)
- [converter/composers/fixed_format_line_parser.py](../converter/composers/fixed_format_line_parser.md)
- [converter/composers/fixed_format_sequence_manager.py](../converter/composers/fixed_format_sequence_manager.md)
- [converter/composers/fixed_format_sequence_stripper.py](../converter/composers/fixed_format_sequence_stripper.md)
- [converter/composers/fixed_format_wrapper.py](../converter/composers/fixed_format_wrapper.md)
- [converter/services/final_sequence_resequencer_service.py](../converter/services/final_sequence_resequencer_service.md)
- [converter/services/fixed_format_line_service.py](../converter/services/fixed_format_line_service.md)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
