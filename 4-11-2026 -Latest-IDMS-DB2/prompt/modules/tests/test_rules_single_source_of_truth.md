# `tests/test_rules_single_source_of_truth.py`

Source: [tests/test_rules_single_source_of_truth.py](../../../tests/test_rules_single_source_of_truth.py) | 56 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `cc7193cddbc5207f75d7c8a5dbaa64b0b68a423aa860087397eeced23217c159`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> A fact may have exactly one home.

## Module-level bindings

`MANUAL_REFERENCE_QUERYNO_BASE` (L19)

## Import declarations

```python
from __future__ import annotations
import rules.cursor_declaration_rules as cursor_rules
import rules.db2_infrastructure_rules as infra_rules
import pathlib
```

## Local dependency notes

- [rules/cursor_declaration_rules.py](../rules/cursor_declaration_rules.md)
- [rules/db2_infrastructure_rules.py](../rules/db2_infrastructure_rules.md)

## Symbol contracts and control points

### `test_queryno_base_has_one_value` - L22-L23

```python
test_queryno_base_has_one_value()
```

### `test_queryno_step_has_one_value` - L26-L27

```python
test_queryno_step_has_one_value()
```

### `test_queryno_template_has_one_value` - L30-L31

```python
test_queryno_template_has_one_value()
```

### `test_queryno_first_matches_the_manual_reference` - L34-L35

```python
test_queryno_first_matches_the_manual_reference()
```

### `test_the_template_placeholder_is_honoured` - L38-L42

```python
test_the_template_placeholder_is_honoured()
```

A renamed placeholder raises KeyError at render time.

Observed calls (lexical order): `cursor_rules.QUERYNO_TEMPLATE.format`.

### `test_no_rules_module_declares_a_restart_queryno` - L44-L56

```python
test_no_rules_module_declares_a_restart_queryno()
```

RestartConfig owns the restart QUERYNOs. A rules-module copy is dead the moment the config changes, and reads as authoritative.

Observed calls (lexical order): `pathlib.Path`, `pathlib.Path(__file__).resolve`, `rules.rglob`, `enumerate`, `path.read_text`, `path.read_text(encoding='utf-8').splitlines`, `line.strip`, `line.strip().startswith`, `', '.join`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
