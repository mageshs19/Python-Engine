# `tests/pipeline/test_single_owner_transformations.py`

Source: [tests/pipeline/test_single_owner_transformations.py](../../../../tests/pipeline/test_single_owner_transformations.py) | 217 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `d7f5c754e554b6422abcd3d4b44090f6598415ce7e74165c3b19278ac3d296e5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L8)

## Import declarations

```python
from __future__ import annotations
import ast
from pathlib import Path
from converter.composers.paragraph_entry_display_composer import ParagraphEntryDisplayComposer
from converter.composers.cursor_close_guarantee_composer import CursorCloseGuaranteeComposer
from converter.composers.lifecycle_standardization_composer import LifecycleStandardizationComposer
from converter.composers.cursor_guarantee.cursor_lines import CursorLines
from converter.composers.cursor_guarantee.business_paragraph_resolver import BusinessParagraphResolver
from converter.composers.cursor_guarantee.cursor_models import CursorParagraphSet
from converter.composers.cursor_paragraph_numbering_composer import CursorParagraphNumberingComposer
```

## Local dependency notes

- [converter/composers/cursor_close_guarantee_composer.py](../../converter/composers/cursor_close_guarantee_composer.md)
- [converter/composers/cursor_guarantee/business_paragraph_resolver.py](../../converter/composers/cursor_guarantee/business_paragraph_resolver.md)
- [converter/composers/cursor_guarantee/cursor_lines.py](../../converter/composers/cursor_guarantee/cursor_lines.md)
- [converter/composers/cursor_guarantee/cursor_models.py](../../converter/composers/cursor_guarantee/cursor_models.md)
- [converter/composers/cursor_paragraph_numbering_composer.py](../../converter/composers/cursor_paragraph_numbering_composer.md)
- [converter/composers/lifecycle_standardization_composer.py](../../converter/composers/lifecycle_standardization_composer.md)
- [converter/composers/paragraph_entry_display_composer.py](../../converter/composers/paragraph_entry_display_composer.md)

## Symbol contracts and control points

### `_call_counts` - L11-L25

```python
_call_counts(path: Path, method_name: str, stage_names: set[str]) -> dict[str, int]
```

Observed calls (lexical order): `ast.parse`, `path.read_text`, `ast.walk`, `isinstance`.

Control points:

- L14: `for node in ast.walk(tree)`
- L15: `if not isinstance(node, ast.Call)`
- L18: `if not isinstance(func, ast.Attribute) or func.attr != method_name`
- L20: `if not node.args or not isinstance(node.args[0], ast.Constant)`
- L23: `if value in counts`

### `test_mutating_pipeline_stages_have_one_call_site_each` - L28-L37

```python
test_mutating_pipeline_stages_have_one_call_site_each()
```

Observed calls (lexical order): `_call_counts`, `counts.update`.

### `test_cursor_lifecycle_has_one_mutating_owner_in_production_pipeline` - L40-L47

```python
test_cursor_lifecycle_has_one_mutating_owner_in_production_pipeline()
```

Observed calls (lexical order): `(ROOT / 'converter/pipeline/conversion/conversion_pipeline_steps.py').read_text`, `factory_path.read_text`, `(ROOT / 'converter/composers/cursor_flow_composer.py').exists`.

### `test_nonmatching_debug_display_is_preserved_and_entry_display_is_added` - L50-L59

```python
test_nonmatching_debug_display_is_preserved_and_entry_display_is_added()
```

Observed calls (lexical order): `'\n'.join`, `'000010 PROCEDURE DIVISION.'.ljust`, `'000020 DO-WORK.'.ljust`, `"000030D DISPLAY 'BUSINESS DIAGNOSTIC'.".ljust`, `'000040 GOBACK.'.ljust`, `ParagraphEntryDisplayComposer`, `ParagraphEntryDisplayComposer().compose`.

### `test_vmdz4420_nested_cursor_flow_is_not_rewritten_twice` - L62-L82

```python
test_vmdz4420_nested_cursor_flow_is_not_rewritten_twice()
```

Observed calls (lexical order): `fixture.read_text`, `LifecycleStandardizationComposer`, `lifecycle.compose`, `CursorCloseGuaranteeComposer`, `composer.compose`, `output.splitlines`, `sum`, `any`.

### `test_external_business_loop_removes_existing_fetch_to_business_edge` - L85-L140

```python
test_external_business_loop_removes_existing_fetch_to_business_edge()
```

Observed calls (lexical order): `'\n'.join`, `'000010 PROCEDURE DIVISION.'.ljust`, `'000020 MAIN-PROCEDURE.'.ljust`, `'000030 PERFORM 2100-OPEN-DZBEFFC1.'.ljust`, `'000040 PERFORM 2200-FETCH-DZBEFFC1.'.ljust`, `"000050 PERFORM VERWERK-EFFEKT UNTIL ERROR-STATUS NOT = '0000'.".ljust`, `'000060 PERFORM 2300-CLOSE-DZBEFFC1.'.ljust`, `'000070 VERWERK-EFFEKT.'.ljust`, `'000080 PERFORM 3100-OPEN-DZEVEFC1.'.ljust`, `'000090 PERFORM 3200-FETCH-DZEVEFC1.'.ljust`, `'000100 PERFORM NEXT-VMBEVEF UNTIL DZEVEFC1-EOC.'.ljust`, `'000110 PERFORM 3300-CLOSE-DZEVEFC1.'.ljust`, `'000120 PERFORM 2200-FETCH-DZBEFFC1.'.ljust`, `'000130 NEXT-VMBEVEF.'.ljust`, `"000140 DISPLAY 'DCLDZEVEFTV' ".ljust`, `'000150 PERFORM 3200-FETCH-DZEVEFC1.'.ljust`.
Another 31 call expressions are in this source span; the list is intentionally bounded.

### `test_business_resolver_skips_exit_paragraphs_before_cursor_business_body` - L143-L169

```python
test_business_resolver_skips_exit_paragraphs_before_cursor_business_body()
```

Observed calls (lexical order): `'000010 PROCEDURE DIVISION.'.ljust`, `'000020 BEGIN-PROGRAMMA.'.ljust`, `'000030 PERFORM 2100-OPEN-DZBFASC1.'.ljust`, `'000040 BEGIN-PROGRAMMA-EXIT.'.ljust`, `'000050 EXIT.'.ljust`, `'000060 BEHANDELING.'.ljust`, `"000070 DISPLAY 'DCLDZBFASV'.".ljust`, `'000080 PERFORM 2200-FETCH-DZBFASC1.'.ljust`, `'000090 2100-OPEN-DZBFASC1.'.ljust`, `'000100 CONTINUE.'.ljust`, `'000110 2200-FETCH-DZBFASC1.'.ljust`, `'000120 EXEC SQL FETCH DZBFASC1 INTO :DCLDZBFASV.FIELD END-EXEC.'.ljust`, `'000130 2300-CLOSE-DZBFASC1.'.ljust`, `'000140 CONTINUE.'.ljust`, `CursorParagraphSet`, `BusinessParagraphResolver`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

### `test_cursor_numbering_composer_changes_only_cursor_labels_not_business_flow` - L172-L217

```python
test_cursor_numbering_composer_changes_only_cursor_labels_not_business_flow()
```

Observed calls (lexical order): `'\n'.join`, `CursorParagraphNumberingComposer`, `CursorParagraphNumberingComposer().compose`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
