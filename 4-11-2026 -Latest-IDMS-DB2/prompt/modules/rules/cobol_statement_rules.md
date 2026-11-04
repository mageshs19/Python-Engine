# `rules/cobol_statement_rules.py`

Source: [rules/cobol_statement_rules.py](../../../rules/cobol_statement_rules.py) | 224 lines.
Owning logic guide: [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md).
Source SHA-256: `806f60b5d37737c76595d96f25e6814c4f66eaf93c43b98f6a8125e403aed78b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> COBOL statement classification rules.

## Module-level bindings

`NON_PARAGRAPH_SINGLE_WORDS` (L16), `NON_PARAGRAPH_WORDS` (L83), `PROCEDURE_VERBS` (L85), `SQL_LEVEL_1_KEYWORDS` (L146), `SQL_LEVEL_2_KEYWORDS` (L168)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/fixed_format_body_formatter.py](../converter/composers/fixed_format_body_formatter.md)
- [converter/services/cobol_area_alignment_classifier.py](../converter/services/cobol_area_alignment_classifier.md)
- [converter/services/procedure_block_indent_service.py](../converter/services/procedure_block_indent_service.md)
- [converter/transformers/cobol_transformer.py](../converter/transformers/cobol_transformer.md)

## Symbol contracts and control points

### `is_non_paragraph_word` - L174-L182

```python
is_non_paragraph_word(word: str) -> bool
```

Return True when the supplied word is a COBOL verb or keyword that should not be treated as a paragraph name.

Observed calls (lexical order): `str`, `str(word or '').strip`, `str(word or '').strip().upper`.

### `starts_with_procedure_verb` - L185-L196

```python
starts_with_procedure_verb(statement: str) -> bool
```

Return True when the statement starts with a known PROCEDURE DIVISION verb.

Observed calls (lexical order): `str`, `str(statement or '').strip`, `str(statement or '').strip().upper`, `clean_statement.startswith`.

Control points:

- L193: `if not clean_statement`

### `starts_with_sql_level_1_keyword` - L199-L210

```python
starts_with_sql_level_1_keyword(statement: str) -> bool
```

Return True when the SQL statement starts with a level-1 SQL keyword.

Observed calls (lexical order): `str`, `str(statement or '').strip`, `str(statement or '').strip().upper`, `clean_statement.startswith`.

Control points:

- L207: `if not clean_statement`

### `starts_with_sql_level_2_keyword` - L213-L224

```python
starts_with_sql_level_2_keyword(statement: str) -> bool
```

Return True when the SQL statement starts with a level-2 SQL keyword.

Observed calls (lexical order): `str`, `str(statement or '').strip`, `str(statement or '').strip().upper`, `clean_statement.startswith`.

Control points:

- L221: `if not clean_statement`

## Change responsibility

After modifying this Python file, review [prompt/14_RULES_PATTERNS_AND_CATALOGS.md](../../14_RULES_PATTERNS_AND_CATALOGS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
