# `tests/restart/test_m9a_legacy_cleanup.py`

Source: [tests/restart/test_m9a_legacy_cleanup.py](../../../../tests/restart/test_m9a_legacy_cleanup.py) | 284 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `61f0b93156ce8dd100c9a7ca63b528948f45c8151c9fd157bbbf1d6dd4aae7b8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> M9a contract tests: removing the previous restart mechanism.

## Import declarations

```python
from __future__ import annotations
import pytest
from converter.composers.restart.legacy_restart_cleanup import LegacyRestartCleanup
from rules import restart_standard_rules as std
from rules.restart_cleanup_rules import PARAGRAPH_SPAN_LIMIT
from rules.restart_cleanup_rules import LEGACY_RESTART_DETECTION_TOKENS
```

## Local dependency notes

- [converter/composers/restart/legacy_restart_cleanup.py](../../converter/composers/restart/legacy_restart_cleanup.md)
- [rules/__init__.py](../../rules/__init__.md)
- [rules/restart_cleanup_rules.py](../../rules/restart_cleanup_rules.md)
- [rules/restart_standard_rules.py](../../rules/restart_standard_rules.md)

## Symbol contracts and control points

### `cleanup` - L26-L27

```python
cleanup(config, line_utils)
```

Observed calls (lexical order): `LegacyRestartCleanup`.

### `_logical` - L30-L31

```python
_logical(lines)
```

Observed calls (lexical order): `' '.join`, `str`, `str(l).strip`, `str(l).upper`, `str(l).upper().split`.

### `_program` - L34-L40

```python
_program(data: list[str], procedure: list[str]) -> list[str]
```

### `test_legacy_tokens_are_detected` - L47-L49

```python
test_legacy_tokens_are_detected(cleanup)
```

Observed calls (lexical order): `cleanup.detect`, `any`.

### `test_a_clean_program_reports_nothing_found` - L52-L54

```python
test_a_clean_program_reports_nothing_found(cleanup)
```

Observed calls (lexical order): `cleanup.detect`, `any`.

### `test_every_detection_token_is_recognised` - L57-L63

```python
test_every_detection_token_is_recognised(cleanup)
```

Observed calls (lexical order): `cleanup.detect`.

Control points:

- L62: `for token in LEGACY_RESTART_DETECTION_TOKENS`

### `test_a_comment_does_not_trigger_detection` - L66-L67

```python
test_a_comment_does_not_trigger_detection(cleanup)
```

Observed calls (lexical order): `cleanup.detect`.

### `test_a_restart_paragraph_is_removed` - L74-L86

```python
test_a_restart_paragraph_is_removed(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_logical`, `cleanup.remove_paragraphs`.

### `test_the_following_paragraph_survives` - L89-L100

```python
test_the_following_paragraph_survives(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_logical`, `cleanup.remove_paragraphs`.

### `test_every_restart_role_is_removed` - L103-L112

```python
test_every_restart_role_is_removed(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_logical`, `cleanup.remove_paragraphs`.

Control points:

- L105: `for role in std.RESTART_PARAGRAPH_ROLES`
- L110: `for role in std.RESTART_PARAGRAPH_ROLES`

### `test_a_business_paragraph_is_never_removed` - L115-L117

```python
test_a_business_paragraph_is_never_removed(cleanup)
```

Observed calls (lexical order): `_logical`, `cleanup.remove_paragraphs`.

### `test_an_absent_paragraph_is_reported` - L120-L122

```python
test_an_absent_paragraph_is_reported(config, cleanup)
```

Observed calls (lexical order): `cleanup.remove_paragraphs`, `any`.

### `test_the_removal_is_reported_with_a_line_count` - L125-L130

```python
test_the_removal_is_reported_with_a_line_count(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `cleanup.remove_paragraphs`, `any`.

### `test_a_paragraph_ending_at_a_section_is_bounded` - L133-L144

```python
test_a_paragraph_ending_at_a_section_is_bounded(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_logical`, `cleanup.remove_paragraphs`.

### `test_an_over_long_span_is_refused` - L147-L155

```python
test_an_over_long_span_is_refused(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_logical`, `cleanup.remove_paragraphs`, `any`.

### `test_an_unreferenced_legacy_declaration_is_removed` - L162-L169

```python
test_an_unreferenced_legacy_declaration_is_removed(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_a_referenced_legacy_declaration_survives` - L172-L179

```python
test_a_referenced_legacy_declaration_survives(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_the_legacy_abend_marker_is_removed` - L182-L189

```python
test_the_legacy_abend_marker_is_removed(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_a_wrapped_marker_is_removed_whole` - L192-L202

```python
test_a_wrapped_marker_is_removed_whole(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_a_referenced_marker_survives` - L205-L211

```python
test_a_referenced_marker_survives(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_an_ordinary_declaration_is_never_removed` - L214-L220

```python
test_an_ordinary_declaration_is_never_removed(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`, `any`.

### `test_a_program_without_a_procedure_division_is_untouched` - L223-L226

```python
test_a_program_without_a_procedure_division_is_untouched(cleanup)
```

Observed calls (lexical order): `cleanup.remove_declarations`, `any`.

### `test_the_procedure_division_is_never_edited` - L229-L236

```python
test_the_procedure_division_is_never_edited(cleanup)
```

Observed calls (lexical order): `_program`, `_logical`, `cleanup.remove_declarations`.

### `test_clean_removes_paragraphs_and_declarations` - L243-L252

```python
test_clean_removes_paragraphs_and_declarations(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_program`, `_logical`, `cleanup.clean`, `any`.

### `test_cleaning_twice_is_stable` - L255-L263

```python
test_cleaning_twice_is_stable(config, cleanup)
```

Observed calls (lexical order): `config.paragraph`, `_program`, `cleanup.clean`, `_logical`.

### `test_cleaning_a_clean_program_changes_nothing` - L266-L271

```python
test_cleaning_a_clean_program_changes_nothing(cleanup)
```

Observed calls (lexical order): `_program`, `cleanup.clean`.

### `test_messages_are_reset_between_runs` - L274-L279

```python
test_messages_are_reset_between_runs(cleanup)
```

Observed calls (lexical order): `_program`, `cleanup.clean`, `len`.

### `test_empty_input_is_safe` - L282-L284

```python
test_empty_input_is_safe(cleanup)
```

Observed calls (lexical order): `cleanup.clean`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
