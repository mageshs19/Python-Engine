# `patterns/fixed_format_rules.py`

Source: [patterns/fixed_format_rules.py](../../../patterns/fixed_format_rules.py) | 180 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `14bb6882d94d9586abeddc4f6643ae82c47cad7e6bd79441a7e88f4e63f5f1b9`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fixed-format COBOL layout rules. These constants define the final physical COBOL layout: - Columns 1-6 : left sequence number - Column 7 : indicator area - Columns 8-72 : COBOL body - Columns 73-80 : right sequence number

## Module-level bindings

`TOTAL_WIDTH` (L9), `BODY_WIDTH` (L10), `LEFT_SEQUENCE_WIDTH` (L11), `INDICATOR_WIDTH` (L12), `RIGHT_SEQUENCE_WIDTH` (L13), `DEFAULT_LEFT_START` (L14), `DEFAULT_LEFT_STEP` (L15), `DEFAULT_RIGHT_START` (L19), `DEFAULT_RIGHT_STEP` (L20), `AREA_A_INDENT` (L21), `AREA_B_INDENT` (L22), `SQL_INDENT` (L23), `SQL_CONTINUATION_INDENT` (L24), `SPACE_INDICATOR` (L25), `COMMENT_INDICATOR` (L26), `PAGE_INDICATOR` (L27), `DEBUG_INDICATOR` (L28), `CONTINUATION_INDICATOR` (L29), `VALID_INDICATORS` (L30), `NON_PARAGRAPH_WORDS` (L38), `PROCEDURE_VERBS` (L66), `SQL_LEVEL_1_KEYWORDS` (L91), `SQL_LEVEL_2_KEYWORDS` (L112), `AREA_A_HEADER_PREFIXES` (L117), `AREA_A_DATA_LEVELS` (L125), `AREA_B_DATA_LEVELS` (L130)

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
