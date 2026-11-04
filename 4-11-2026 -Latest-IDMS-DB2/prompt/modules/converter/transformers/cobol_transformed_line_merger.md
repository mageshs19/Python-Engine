# `converter/transformers/cobol_transformed_line_merger.py`

Source: [converter/transformers/cobol_transformed_line_merger.py](../../../../converter/transformers/cobol_transformed_line_merger.py) | 94 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `fae27154f540d28cd43ed03362ca756b26ad3f63b5864504b86e42f366eb0529`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Import declarations

```python
from __future__ import annotations
from converter.transformers.cobol_transformer_line_utils import CobolTransformerLineUtils
from rules.cobol_transformer_rules import GENERATED_LINE_PREFIXES
```

## Local dependency notes

- [converter/transformers/cobol_transformer_line_utils.py](cobol_transformer_line_utils.md)
- [rules/cobol_transformer_rules.py](../../rules/cobol_transformer_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](cobol_transformer.md)

## Symbol contracts and control points

### `CobolTransformedLineMerger` - L9-L94

```python
class CobolTransformedLineMerger()
```

Merges transformed statement output with original fixed-format style when the transformation is a safe one-line token replacement.

### `CobolTransformedLineMerger.__init__` - L15-L19

```python
__init__(self, line_utils: CobolTransformerLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolTransformerLineUtils`.

### `CobolTransformedLineMerger.merge_transformed_lines_with_original_style` - L21-L47

```python
merge_transformed_lines_with_original_style(self, *, original_line: str, original_logical: str, transformed_lines: list[str]) -> list[str]
```

Observed calls (lexical order): `len`, `str`, `str(transformed_lines[0] or '').strip`, `self.is_single_line_token_replacement`, `self.line_utils.replace_logical_body`.

Control points:

- L28: `if not transformed_lines`
- L31: `if len(transformed_lines) == 1`
- L34: `if self.is_single_line_token_replacement(original_logical=original_logical, transformed_line=transformed)`

### `CobolTransformedLineMerger.is_single_line_token_replacement` - L49-L77

```python
is_single_line_token_replacement(self, *, original_logical: str, transformed_line: str) -> bool
```

Observed calls (lexical order): `str`, `str(original_logical or '').strip`, `str(transformed_line or '').strip`, `transformed.upper`, `transformed_upper.startswith`, `transformed.startswith`.

Control points:

- L59: `if not original or not transformed`
- L62: `if 'SQLCODE = 100' in transformed_upper`
- L65: `if 'SQLCODE NOT = 100' in transformed_upper`
- L68: `if 'SQLCODE NOT = 0' in transformed_upper`
- L71: `if transformed_upper.startswith(GENERATED_LINE_PREFIXES)`
- L74: `if transformed.startswith('*')`

### `CobolTransformedLineMerger.transformer_changed_line` - L79-L94

```python
transformer_changed_line(self, *, original_logical: str, transformed_lines: list[str]) -> bool
```

Observed calls (lexical order): `len`, `str`, `str(transformed_lines[0] or '').strip`, `str(original_logical or '').strip`.

Control points:

- L85: `if not transformed_lines`
- L88: `if len(transformed_lines) != 1`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
