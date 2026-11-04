# `converter/composers/structural_safety_composer.py`

Source: [converter/composers/structural_safety_composer.py](../../../../converter/composers/structural_safety_composer.py) | 487 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `bd9809a5dc08d6b93bf729a831d19bda6148f014d2ec5eba7e00ac3cd1331279`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Final structural safety pass. COMMENT-ONLY, never deletes.

## Module-level bindings

`DCLGEN_PREFIX` (L108), `FALLBACK_COMMENT_PREFIX` (L112), `COPY_VERB` (L115), `FD_VERBS` (L116), `INCLUDE_WORD` (L117), `EXEC_WORD` (L118), `DATA_RECORD_PREFIXES` (L119), `NON_RECORD_WORDS` (L122), `__all__` (L487)

## Import declarations

```python
from __future__ import annotations
from converter.services.fixed_format_line_service import FixedFormatLineService
from patterns.structural_safety_patterns import EXIT_STATEMENT_PATTERN, MOVE_BARE_SOURCE_PATTERN, MOVE_BARE_TARGET_PATTERN, PARAGRAPH_HEADER_PATTERN, PROCEDURE_DIVISION_PATTERN, QUALIFIER_PATTERN, SECTION_HEADER_PATTERN
from rules.structural_safety_rules import ENFORCE_ORPHANED_RECORD_GUARD, ENFORCE_UNREACHABLE_STATEMENT_GUARD, MAX_UNREACHABLE_STATEMENTS, ORPHANED_LINE_PREFIX, ORPHANED_RECORD_MARKER_TEMPLATE, STRUCTURAL_SAFETY_MESSAGES, UNREACHABLE_MARKER
```

## Local dependency notes

- [converter/services/fixed_format_line_service.py](../services/fixed_format_line_service.md)
- [patterns/structural_safety_patterns.py](../../patterns/structural_safety_patterns.md)
- [rules/structural_safety_rules.py](../../rules/structural_safety_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_steps.py](../pipeline/conversion/conversion_layout_steps.md)

## Symbol contracts and control points

### `StructuralSafetyComposer` - L128-L484

```python
class StructuralSafetyComposer()
```

Comments references the compiler would reject.

### `StructuralSafetyComposer.__init__` - L131-L138

```python
__init__(self, original_idms_text: str='', fixed_format: FixedFormatLineService | None=None) -> None
```

Observed calls (lexical order): `str`, `FixedFormatLineService`.

### `StructuralSafetyComposer.compose` - L141-L157

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `str`, `str(text).replace`, `str(text).replace('\r\n', '\n').replace`, `str(text).replace('\r\n', '\n').replace('\r', '\n').split`, `self._guard_orphaned_records`, `self._guard_unreachable_statements`, `'\n'.join`, `'\n'.join(lines).rstrip`.

Control points:

- L144: `if not text`
- L151: `if ENFORCE_ORPHANED_RECORD_GUARD`
- L154: `if ENFORCE_UNREACHABLE_STATEMENT_GUARD`

### `StructuralSafetyComposer._guard_orphaned_records` - L161-L207

```python
_guard_orphaned_records(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._idms_record_names`, `self._declared_names`, `enumerate`, `self._is_skippable`, `output.append`, `self._logical`, `self._whole_record_reference`, `self._note_reference`, `output.extend`, `self._comment_lines`, `ORPHANED_RECORD_MARKER_TEMPLATE.format`, `self.messages.append`, `STRUCTURAL_SAFETY_MESSAGES['orphaned_record_commented'].format`, `self._report_references`.

Control points:

- L163: `if not records`
- L168: `if not orphans`
- L175: `for (number, line) in enumerate(lines, start=1)`
- L176: `if self._is_skippable(line)`
- L181: `if not body`
- L186: `if not record`

### `StructuralSafetyComposer._note_reference` - L209-L239

```python
_note_reference(self, body: str, orphans: set[str], number: int, seen: dict[str, tuple[int, str, int]]) -> None
```

Record an orphan used in a form this pass will not comment.

Observed calls (lexical order): `word.strip`, `self._without_literals`, `self._without_literals(body).upper`, `self._without_literals(body).upper().split`, `seen.get`.

Control points:

- L233: `for record in orphans & words`
- L234: `if record in NON_RECORD_WORDS`

### `StructuralSafetyComposer._report_references` - L241-L256

```python
_report_references(self, seen: dict[str, tuple[int, str, int]]) -> None
```

Observed calls (lexical order): `STRUCTURAL_SAFETY_MESSAGES.get`, `sorted`, `self.messages.append`, `template.format`.

Control points:

- L248: `if not template`
- L250: `for record in sorted(seen)`

### `StructuralSafetyComposer._without_literals` - L259-L279

```python
_without_literals(body: str) -> str
```

The statement with quoted literals blanked out.

Observed calls (lexical order): `str`, `out.append`, `''.join`.

Control points:

- L268: `for char in str(body or '')`
- L269: `if quote`
- L270: `if char == quote`
- L274: `if char in ("'", '"')`

### `StructuralSafetyComposer._idms_record_names` - L282-L288

```python
_idms_record_names(self) -> set[str]
```

Observed calls (lexical order): `set`, `QUALIFIER_PATTERN.finditer`, `match.group`, `match.group('record').upper`, `name.startswith`, `names.add`.

Control points:

- L284: `for match in QUALIFIER_PATTERN.finditer(self.original_idms_text)`
- L286: `if name and (not name.startswith(DCLGEN_PREFIX))`

### `StructuralSafetyComposer._declared_names` - L291-L347

```python
_declared_names(self, lines: list[str]) -> set[str]
```

Every name the program declares, by any means.

Observed calls (lexical order): `set`, `self._is_skippable`, `self._logical`, `PROCEDURE_DIVISION_PATTERN.match`, `body.upper`, `upper.split`, `len`, `parts[0].rstrip`, `parts[0].rstrip('.').isdigit`, `declared.add`, `parts[1].rstrip`, `parts[1].rstrip('.').upper`, `upper.startswith`, `upper[len(prefix):].split`, `upper[len(prefix):].split()[0].rstrip`, `upper[len(prefix):].split()[0].rstrip('.').upper`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L299: `for line in lines`
- L300: `if self._is_skippable(line)`
- L304: `if not body`
- L307: `if PROCEDURE_DIVISION_PATTERN.match(body)`
- L312: `if not parts`
- L316: `if len(parts) >= 2 and parts[0].rstrip('.').isdigit()`
- L322: `if parts[0] == COPY_VERB and len(parts) >= 2`
- L327: `if parts[0] in FD_VERBS and len(parts) >= 2`
- Another 4 conditions/loops exist in this source span.

### `StructuralSafetyComposer._whole_record_reference` - L350-L358

```python
_whole_record_reference(body: str, orphans: set[str]) -> str
```

Observed calls (lexical order): `pattern.match`, `match.group`, `match.group('name').upper`.

Control points:

- L351: `for pattern in (MOVE_BARE_SOURCE_PATTERN, MOVE_BARE_TARGET_PATTERN)`
- L353: `if not match`
- L356: `if name in orphans and name not in NON_RECORD_WORDS`

### `StructuralSafetyComposer._report_other_reference` - L360-L387

```python
_report_other_reference(self, body: str, orphans: set[str], number: int) -> None
```

Name an orphan used in a form this pass will not comment.

Observed calls (lexical order): `STRUCTURAL_SAFETY_MESSAGES.get`, `word.strip`, `word.strip('.,()\'"').upper`, `body.split`, `sorted`, `template.format`, `self.messages.append`.

Control points:

- L373: `if not template`
- L380: `for record in sorted(orphans & words)`
- L381: `if record in NON_RECORD_WORDS`
- L386: `if message not in self.messages`

### `StructuralSafetyComposer._guard_unreachable_statements` - L390-L459

```python
_guard_unreachable_statements(self, lines: list[str]) -> list[str]
```

Observed calls (lexical order): `self._is_skippable`, `output.append`, `self._logical`, `PROCEDURE_DIVISION_PATTERN.match`, `EXIT_STATEMENT_PATTERN.match`, `PARAGRAPH_HEADER_PATTERN.match`, `SECTION_HEADER_PATTERN.match`, `output.extend`, `self._comment_lines`, `self.messages.append`, `STRUCTURAL_SAFETY_MESSAGES['unreachable_aborted'].format`, `STRUCTURAL_SAFETY_MESSAGES['unreachable_commented'].format`.

Control points:

- L396: `for line in lines`
- L400: `if self._is_skippable(line)`
- L406: `if PROCEDURE_DIVISION_PATTERN.match(body)`
- L412: `if not in_procedure or not body`
- L417: `if EXIT_STATEMENT_PATTERN.match(body)`
- L424: `if PARAGRAPH_HEADER_PATTERN.match(body) or SECTION_HEADER_PATTERN.match(body)`
- L431: `if not after_exit`
- L443: `if commented > MAX_UNREACHABLE_STATEMENTS`
- Another 1 conditions/loops exist in this source span.

### `StructuralSafetyComposer._comment_lines` - L462-L471

```python
_comment_lines(self, reference: str, body: str) -> list[str]
```

Comment line(s), wrapped when the text exceeds columns 8-72.

Observed calls (lexical order): `str`, `str(body or '').lstrip`, `str(body or '').lstrip('*').strip`, `self.fixed_format.is_fixed_line`, `self.fixed_format.split`, `self.fixed_format.emit`.

Control points:

- L466: `if self.fixed_format.is_fixed_line(reference)`

### `StructuralSafetyComposer._logical` - L473-L477

```python
_logical(self, line: str) -> str
```

Observed calls (lexical order): `self.fixed_format.logical`, `str`, `str(self.fixed_format.logical(line) or '').strip`, `str(line or '').strip`.

### `StructuralSafetyComposer._is_skippable` - L479-L484

```python
_is_skippable(self, line: str) -> bool
```

Comment / page-eject / debug / continuation, read from column 7.

Observed calls (lexical order): `bool`, `self.fixed_format.is_comment_or_control_line`, `str`, `str(line or '').lstrip`, `str(line or '').lstrip().startswith`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
