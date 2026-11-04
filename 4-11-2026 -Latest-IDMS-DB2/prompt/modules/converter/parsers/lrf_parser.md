# `converter/parsers/lrf_parser.py`

Source: [converter/parsers/lrf_parser.py](../../../../converter/parsers/lrf_parser.py) | 228 lines.
Owning logic guide: [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md).
Source SHA-256: `bf2c150e4239ec2845b11e1c1ab65a35557cfee17b1ba7b5a6bdde6b58c49605`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Parses IDMS subschema source into LogicalRecord metadata.

## Module-level bindings

`COMMENT_PREFIXES` (L40)

## Import declarations

```python
from __future__ import annotations
from converter.domain.models import LogicalRecord, LrfPath, LrfPathCommand
from patterns.lrf_patterns import COMMENTS_PATTERN, ELEMENTS_ARE_PATTERN, ELEMENT_NAME_PATTERN, ERASE_PATTERN, FIND_OBTAIN_PATTERN, IF_SET_EMPTY_PATTERN, LOGICAL_RECORD_PATTERN, ON_STATUS_PATTERN, PATH_GROUP_PATTERN, QUOTED_TEXT_PATTERN, SELECT_KEYWORD_PATTERN, SUBSCHEMA_HEADER_PATTERN, WHERE_PATTERN
from rules.lrf_rules import DIAG_LRF_PATHS_TEMPLATE, DIAG_LRF_TOTAL_RECORDS_TEMPLATE
```

## Local dependency notes

- [converter/domain/models.py](../domain/models.md)
- [patterns/lrf_patterns.py](../../patterns/lrf_patterns.md)
- [rules/lrf_rules.py](../../rules/lrf_rules.md)

## Importers (6)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/input_loader.py](../ui/input_loader.md)
- [runners/batch/shared_input_loader.py](../../runners/batch/shared_input_loader.md)
- [runners/retrieval/retrieval_program_converter.py](../../runners/retrieval/retrieval_program_converter.md)
- [runners/update/update_input_loader.py](../../runners/update/update_input_loader.md)
- [tests/test_lrf_path_expander.py](../../tests/test_lrf_path_expander.md)
- [tests/test_lrf_update_expander.py](../../tests/test_lrf_update_expander.md)

## Symbol contracts and control points

### `LrfParser` - L43-L228

```python
class LrfParser()
```

### `LrfParser.__init__` - L44-L45

```python
__init__(self) -> None
```

### `LrfParser.parse` - L48-L168

```python
parse(self, text: str, source_label: str='') -> list[LogicalRecord]
```

Observed calls (lexical order): `enumerate`, `str`, `str(text or '').splitlines`, `raw_line.rstrip`, `line.strip`, `stripped.startswith`, `SUBSCHEMA_HEADER_PATTERN.match`, `header.group`, `header.group('subschema').upper`, `header.group('schema').upper`, `LOGICAL_RECORD_PATTERN.match`, `lr_match.group`, `lr_match.group('lr').upper`, `records.setdefault`, `LogicalRecord`, `ELEMENTS_ARE_PATTERN.match`.
Another 24 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L60: `for (number, raw_line) in enumerate(str(text or '').splitlines(), start=1)`
- L64: `if not stripped or stripped.startswith('*')`
- L68: `if header`
- L75: `if lr_match`
- L90: `if ELEMENTS_ARE_PATTERN.match(line)`
- L94: `if COMMENTS_PATTERN.match(line)`
- L100: `if group`
- L118: `if keyword and current_lr is not None`
- Another 8 conditions/loops exist in this source span.

### `LrfParser._path_line` - L171-L228

```python
_path_line(self, *, stripped: str, raw_line: str, number: int, path: LrfPath, current_command: LrfPathCommand | None) -> LrfPathCommand | None
```

Observed calls (lexical order): `ON_STATUS_PATTERN.match`, `status.group`, `status.group('action').strip`, `status.group('action').strip().upper`, `WHERE_PATTERN.match`, `where.group`, `where.group('clause').strip`, `where.group('clause').strip().upper`, `IF_SET_EMPTY_PATTERN.match`, `LrfPathCommand`, `empty.group`, `empty.group('set_name').upper`, `path.commands.append`, `ERASE_PATTERN.match`, `erase.group`, `erase.group('record').upper`.
Another 6 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L181: `if status and current_command is not None`
- L188: `if where and current_command is not None`
- L193: `if empty`
- L205: `if erase`
- L216: `if access`

## Change responsibility

After modifying this Python file, review [prompt/03_INPUT_METADATA_AND_RESOLUTION.md](../../../03_INPUT_METADATA_AND_RESOLUTION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
