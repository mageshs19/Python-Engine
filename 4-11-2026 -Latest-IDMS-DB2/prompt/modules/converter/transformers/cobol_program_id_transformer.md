# `converter/transformers/cobol_program_id_transformer.py`

Source: [converter/transformers/cobol_program_id_transformer.py](../../../../converter/transformers/cobol_program_id_transformer.py) | 228 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `0dfb46109a33524cb8d907c5d1591d4faa3d1d68b35e6a894e7685f5987a937f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Target PROGRAM-ID replacement, PROGRAM-ID period cleanup, and the PROGRAM-NAME literal rewrite.

## Module-level bindings

`__all__` (L226)

## Import declarations

```python
from __future__ import annotations
import re
from converter.transformers.cobol_transformer_line_utils import CobolTransformerLineUtils
from patterns.cobol_patterns import PROGRAM_ID_PATTERN
from patterns.final_feedback_fix_patterns import MOVE_TO_PROGRAM_NAME_PATTERN
from rules.cobol_transformer_rules import ENFORCE_PROGRAM_NAME_LITERAL, PROGRAM_NAME_LITERAL_MESSAGES
```

## Local dependency notes

- [converter/transformers/cobol_transformer_line_utils.py](cobol_transformer_line_utils.md)
- [patterns/cobol_patterns.py](../../patterns/cobol_patterns.md)
- [patterns/final_feedback_fix_patterns.py](../../patterns/final_feedback_fix_patterns.md)
- [rules/cobol_transformer_rules.py](../../rules/cobol_transformer_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/transformers/cobol_transformer.py](cobol_transformer.md)

## Symbol contracts and control points

### `CobolProgramIdTransformer` - L69-L223

```python
class CobolProgramIdTransformer()
```

Handles target PROGRAM-ID replacement, final PROGRAM-ID period cleanup, and the PROGRAM-NAME literal rewrite.

### `CobolProgramIdTransformer.__init__` - L75-L81

```python
__init__(self, line_utils: CobolTransformerLineUtils | None=None) -> None
```

Observed calls (lexical order): `CobolTransformerLineUtils`.

### `CobolProgramIdTransformer.reset` - L86-L93

```python
reset(self) -> None
```

Clear per-program state.

### `CobolProgramIdTransformer.program_id_replacement` - L98-L121

```python
program_id_replacement(self, *, original_line: str, logical_line: str, target_program_id: str) -> str | None
```

Observed calls (lexical order): `PROGRAM_ID_PATTERN.search`, `str`, `str(target_program_id or '').strip`, `str(target_program_id or '').strip().upper`, `self.line_utils.replace_logical_body`.

Control points:

- L105: `if not target_program_id`
- L108: `if not PROGRAM_ID_PATTERN.search(logical_line)`
- L113: `if not program_id`

### `CobolProgramIdTransformer.fix_program_id_period` - L123-L149

```python
fix_program_id_period(self, *, text: str, target_program_id: str) -> str
```

Observed calls (lexical order): `str`, `str(target_program_id or '').strip`, `str(target_program_id or '').strip().upper`, `re.compile`, `re.escape`, `pattern.sub`, `re.sub`.

Control points:

- L131: `if program_id`

### `CobolProgramIdTransformer.program_name_literal_replacement` - L154-L223

```python
program_name_literal_replacement(self, *, original_line: str, logical_line: str, source_program_id: str, target_program_id: str) -> str | None
```

Rewrite MOVE '<source-id>' TO PROGRAM-NAME.

Observed calls (lexical order): `str`, `str(source_program_id or '').strip`, `str(source_program_id or '').strip().upper`, `str(target_program_id or '').strip`, `str(target_program_id or '').strip().upper`, `MOVE_TO_PROGRAM_NAME_PATTERN.search`, `match.group`, `str(match.group('program') or '').strip`, `str(match.group('program') or '').strip().upper`, `self.messages.append`, `PROGRAM_NAME_LITERAL_MESSAGES['left_unchanged'].format`, `MOVE_TO_PROGRAM_NAME_PATTERN.sub`, `PROGRAM_NAME_LITERAL_MESSAGES['rewritten'].format`, `self.line_utils.replace_logical_body`.

Control points:

- L172: `if not ENFORCE_PROGRAM_NAME_LITERAL`
- L177: `if not source or not target or source == target`
- L183: `if not match`
- L187: `if literal != source`
- L210: `if new_body == text`

### `CobolProgramIdTransformer.program_name_literal_replacement._replace` - L195-L202

```python
_replace(found: re.Match) -> str
```

Observed calls (lexical order): `found.group`.

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
