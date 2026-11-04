# `tests/test_generic_final_sql_location_and_timestamp_regression.py`

Source: [tests/test_generic_final_sql_location_and_timestamp_regression.py](../../../tests/test_generic_final_sql_location_and_timestamp_regression.py) | 84 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b0d66ea7158a94a8c856451d3039133f6a90c3d2a2def5b51e8b1938f5bab321`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Structural regression cases observed by comparing converted COBOL with the manual.

## Import declarations

```python
from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer
from converter.generators.timestamp.timestamp_paragraph_builder import TimestampParagraphBuilder
from converter.services.final_generated_output_service import FinalGeneratedOutputService
```

## Local dependency notes

- [converter/composers/paragraph_entry_display_composer.py](../converter/composers/paragraph_entry_display_composer.md)
- [converter/generators/timestamp/timestamp_paragraph_builder.py](../converter/generators/timestamp/timestamp_paragraph_builder.md)
- [converter/services/final_generated_output_service.py](../converter/services/final_generated_output_service.md)

## Symbol contracts and control points

### `fixed` - L10-L11

```python
fixed(n: int, body: str) -> str
```

### `bodies` - L14-L15

```python
bodies(source: str) -> list[str]
```

Observed calls (lexical order): `line[7:72].strip`, `source.splitlines`.

### `test_area_a_scope_terminators_must_not_be_treated_as_paragraphs` - L18-L30

```python
test_area_a_scope_terminators_must_not_be_treated_as_paragraphs()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `ParagraphEntryDisplayComposer`, `ParagraphEntryDisplayComposer().compose`, `bodies`, `bodies(result).count`.

### `test_unnumbered_sql_paragraph_uses_real_query_identity_not_undeclared_name` - L33-L47

```python
test_unnumbered_sql_paragraph_uses_real_query_identity_not_undeclared_name()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql`.

### `test_no_query_identity_is_not_fabricated` - L50-L60

```python
test_no_query_identity_is_not_fabricated()
```

Observed calls (lexical order): `'\n'.join`, `fixed`, `FinalGeneratedOutputService._ensure_sql_location_before_runtime_sql`.

### `test_timestamp_is_placed_inside_unambiguous_mainline_initialization` - L63-L78

```python
test_timestamp_is_placed_inside_unambiguous_mainline_initialization()
```

Observed calls (lexical order): `fixed`, `TimestampParagraphBuilder`, `TimestampParagraphBuilder().ensure_perform`, `line.strip`, `line[7:72].strip`, `line[:6].isdigit`, `b.count`, `b.index`.

### `test_timestamp_keeps_existing_perform_and_ambiguous_initialization_unchanged` - L81-L84

```python
test_timestamp_keeps_existing_perform_and_ambiguous_initialization_unchanged()
```

Observed calls (lexical order): `fixed`, `TimestampParagraphBuilder`, `TimestampParagraphBuilder().ensure_perform`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
