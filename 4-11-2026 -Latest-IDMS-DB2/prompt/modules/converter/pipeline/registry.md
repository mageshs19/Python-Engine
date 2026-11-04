# `converter/pipeline/registry.py`

Source: [converter/pipeline/registry.py](../../../../converter/pipeline/registry.py) | 185 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `cbe05d113e82030a7d2598b2b7ca6e05fd5c03cb8bf2b8280655a7c69261b8c4`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> THE pipeline. Order in this file IS execution order.

## Module-level bindings

`PIPELINE` (L120), `__all__` (L185)

## Import declarations

```python
from __future__ import annotations
from converter.pipeline.stage import Stage, composer_stage
from converter.composers.cursor_order_cleanup_composer import CursorOrderCleanupComposer
from converter.composers.update_restart_skip_composer import UpdateRestartSkipComposer
from converter.composers.cursor_close_guarantee_composer import CursorCloseGuaranteeComposer
from converter.composers.output_write_paragraph_composer import OutputWriteParagraphComposer
from converter.composers.counter_declaration_composer import CounterDeclarationComposer
from converter.composers.procedure_indent_normalizer import ProcedureIndentNormalizer
from converter.composers.move_alignment_composer import MoveAlignmentComposer
from converter.composers.statement_layout_composer import StatementLayoutComposer
from converter.composers.unnecessary_comments_cleanup_composer import UnnecessaryCommentsCleanupComposer
```

## Local dependency notes

- [converter/composers/counter_declaration_composer.py](../composers/counter_declaration_composer.md)
- [converter/composers/cursor_close_guarantee_composer.py](../composers/cursor_close_guarantee_composer.md)
- [converter/composers/cursor_order_cleanup_composer.py](../composers/cursor_order_cleanup_composer.md)
- [converter/composers/move_alignment_composer.py](../composers/move_alignment_composer.md)
- [converter/composers/output_write_paragraph_composer.py](../composers/output_write_paragraph_composer.md)
- [converter/composers/procedure_indent_normalizer.py](../composers/procedure_indent_normalizer.md)
- [converter/composers/statement_layout_composer.py](../composers/statement_layout_composer.md)
- [converter/composers/unnecessary_comments_cleanup_composer.py](../composers/unnecessary_comments_cleanup_composer.md)
- [converter/composers/update_restart_skip_composer.py](../composers/update_restart_skip_composer.md)
- [converter/pipeline/stage.py](stage.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/run.py](run.md)
- [tests/pipeline/test_every_stage_has_a_call_site.py](../../tests/pipeline/test_every_stage_has_a_call_site.md)

## Symbol contracts and control points

### `_cursor_order_cleanup` - L53-L57

```python
_cursor_order_cleanup()
```

Observed calls (lexical order): `CursorOrderCleanupComposer`.

### `_update_restart_skip` - L60-L64

```python
_update_restart_skip()
```

Observed calls (lexical order): `UpdateRestartSkipComposer`.

### `_cursor_close_guarantee` - L67-L71

```python
_cursor_close_guarantee()
```

Observed calls (lexical order): `CursorCloseGuaranteeComposer`.

### `_output_write_paragraph` - L74-L78

```python
_output_write_paragraph()
```

Observed calls (lexical order): `OutputWriteParagraphComposer`.

### `_counter_declaration` - L81-L85

```python
_counter_declaration()
```

Observed calls (lexical order): `CounterDeclarationComposer`.

### `_procedure_indent` - L88-L92

```python
_procedure_indent()
```

Observed calls (lexical order): `ProcedureIndentNormalizer`.

### `_move_alignment` - L95-L99

```python
_move_alignment()
```

Observed calls (lexical order): `MoveAlignmentComposer`.

### `_statement_layout` - L102-L106

```python
_statement_layout()
```

Observed calls (lexical order): `StatementLayoutComposer`.

### `_unnecessary_comments` - L109-L113

```python
_unnecessary_comments()
```

Observed calls (lexical order): `UnnecessaryCommentsCleanupComposer`.

### `describe` - L177-L182

```python
describe() -> list[str]
```

One readable line per stage. Printed by tools/pipeline_doc.py.

Observed calls (lexical order): `enumerate`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
