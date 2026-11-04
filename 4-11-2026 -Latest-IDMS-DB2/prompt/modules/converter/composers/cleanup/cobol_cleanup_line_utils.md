# `converter/composers/cleanup/cobol_cleanup_line_utils.py`

Source: [converter/composers/cleanup/cobol_cleanup_line_utils.py](../../../../../converter/composers/cleanup/cobol_cleanup_line_utils.py) | 84 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `9381d272e45302f4c67bf8cb0fba48ae293626d436ce33aa8b07f184a9019d5b`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Shared line helpers for the COBOL cleanup passes.

## Import declarations

```python
from __future__ import annotations
from patterns.sequence_patterns import is_comment_or_control, is_fixed_format_line, is_sequence_artifact, strip_sequence_numbers
```

## Local dependency notes

- [patterns/sequence_patterns.py](../../../patterns/sequence_patterns.md)

## Importers (13)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/business_control_flag_analyzer.py](business_control_flag_analyzer.md)
- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/cursor_nesting_analyser.py](cursor_nesting_analyser.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](db2_date_output_cleanup.md)
- [converter/composers/cleanup/dclgen_include_cleanup.py](dclgen_include_cleanup.md)
- [converter/composers/cleanup/error_status_flag_cleanup.py](error_status_flag_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](initialize_before_output_cleanup.md)
- [converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py](orphaned_idms_status_guard_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](output_write_placement_cleanup.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](paragraph_terminator_cleanup.md)
- [converter/composers/cleanup/residual_idms_comment_cleanup.py](residual_idms_comment_cleanup.md)
- [converter/composers/cleanup/residual_idms_error_clause_cleanup.py](residual_idms_error_clause_cleanup.md)
- 1 further importers are recorded in [the source manifest](../../../../source_manifest.json).

## Symbol contracts and control points

### `CobolCleanupLineUtils` - L34-L84

```python
class CobolCleanupLineUtils()
```

Line inspection helpers shared by every cleanup pass.

### `CobolCleanupLineUtils.logical` - L40-L41

```python
logical(self, line: str) -> str
```

Observed calls (lexical order): `str`, `strip_sequence_numbers`, `strip_sequence_numbers(str(line or '')).strip`.

### `CobolCleanupLineUtils.leading_spaces` - L43-L45

```python
leading_spaces(self, line: str) -> str
```

Observed calls (lexical order): `str`, `len`, `value.lstrip`.

### `CobolCleanupLineUtils.is_comment_or_blank` - L50-L66

```python
is_comment_or_blank(self, logical: str) -> bool
```

Legacy signature: classify from already-stripped text.

Observed calls (lexical order): `str`, `str(logical or '').strip`, `stripped.startswith`, `bool`, `is_sequence_artifact`.

Control points:

- L58: `if not stripped`
- L61: `if stripped.startswith('*') or stripped.startswith('/')`

### `CobolCleanupLineUtils.is_comment_or_blank_line` - L68-L78

```python
is_comment_or_blank_line(self, line: str) -> bool
```

Classify from the RAW line by reading column 7.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `text.strip`, `is_comment_or_control`, `self.is_sequence_artifact`.

Control points:

- L72: `if not text.strip()`
- L75: `if is_comment_or_control(text)`

### `CobolCleanupLineUtils.is_fixed_line` - L80-L81

```python
is_fixed_line(self, line: str) -> bool
```

Observed calls (lexical order): `is_fixed_format_line`.

### `CobolCleanupLineUtils.is_sequence_artifact` - L83-L84

```python
is_sequence_artifact(self, line: str) -> bool
```

Observed calls (lexical order): `is_sequence_artifact`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
