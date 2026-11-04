# `mainframe/zowe_resolver.py`

Source: [mainframe/zowe_resolver.py](../../../mainframe/zowe_resolver.py) | 145 lines.
Owning logic guide: [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md).
Source SHA-256: `d1b6738fd1c2a2831e19caa9dd8fd9dab296c839561948701562a0458853a44f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Works out what ONE IDMS program needs.

## Module-level bindings

`_NOT_A_RECORD` (L45)

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass, field
from mainframe.zowe_patterns import COPY_IDMS_RECORD_PATTERN, DB_WITHIN_PATTERN, FIXED_SEQUENCE_PATTERN, IDMS_VERB_RECORD_PATTERN, PLAIN_COPY_PATTERN, RECORD_VERSION_SUFFIX_PATTERN
from mainframe.zowe_rules import BODY_END_COLUMN, BODY_START_COLUMN, COMMENT_INDICATORS, DCLGEN_MEMBER_TEMPLATE, DCLGEN_PREFIX, DCLGEN_RECORD_TAIL_LENGTH, DCLGEN_SUFFIX, INDICATOR_COLUMN
```

## Local dependency notes

- [mainframe/zowe_patterns.py](zowe_patterns.md)
- [mainframe/zowe_rules.py](zowe_rules.md)

## Importers (5)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/__init__.py](__init__.md)
- [mainframe/zowe_commands.py](zowe_commands.md)
- [mainframe/zowe_fetcher.py](zowe_fetcher.md)
- [mainframe/zowe_manifest.py](zowe_manifest.md)
- [tests/test_dzecabtv_fix.py](../tests/test_dzecabtv_fix.md)

## Symbol contracts and control points

### `logical_body` - L52-L72

```python
logical_body(line: str) -> str
```

The COBOL body of one physical line, or '' for a comment.

Observed calls (lexical order): `str`, `str(line or '').rstrip`, `str(line or '').rstrip('\n').rstrip`, `FIXED_SEQUENCE_PATTERN.match`, `text.lstrip`, `len`, `text[BODY_START_COLUMN:BODY_END_COLUMN].rstrip`.

Control points:

- L59: `if not text`
- L62: `if not FIXED_SEQUENCE_PATTERN.match(text)`
- L64: `if stripped[:1] in COMMENT_INDICATORS`
- L69: `if indicator in COMMENT_INDICATORS`

### `logical_text` - L75-L78

```python
logical_text(source_text: str) -> str
```

Whole member reduced to executable COBOL bodies.

Observed calls (lexical order): `logical_body`, `str`, `str(source_text or '').splitlines`, `'\n'.join`.

### `base_record_name` - L81-L84

```python
base_record_name(record: str) -> str
```

VMBTL03-R01 -> VMBTL03. A view suffix is not part of the name.

Observed calls (lexical order): `str`, `str(record or '').strip`, `str(record or '').strip().upper`, `RECORD_VERSION_SUFFIX_PATTERN.sub`.

### `dclgen_member_for` - L87-L96

```python
dclgen_member_for(record: str) -> str
```

VMBEVEF -> DZEVEFTV, VMBTL03-R01 -> DZTL03TV

Observed calls (lexical order): `base_record_name`, `base_record_name(record).replace`, `len`, `DCLGEN_MEMBER_TEMPLATE.format`.

Control points:

- L90: `if len(name) < DCLGEN_RECORD_TAIL_LENGTH`

### `ProgramDependencies` - L100-L105

```python
class ProgramDependencies()
```

Declared class/data-model fields:

```python
program: str = ''
copybooks: list[str] = field(default_factory=list)
records: list[str] = field(default_factory=list)
dclgens: list[str] = field(default_factory=list)
subschema: str = ''
```

### `_unique` - L108-L114

```python
_unique(values) -> list[str]
```

Observed calls (lexical order): `str`, `str(value or '').strip`, `str(value or '').strip().upper`, `out.append`.

Control points:

- L110: `for value in values`
- L112: `if name and name not in out`

### `resolve_dependencies` - L117-L145

```python
resolve_dependencies(program: str, source_text: str) -> ProgramDependencies
```

Observed calls (lexical order): `logical_text`, `_unique`, `PLAIN_COPY_PATTERN.finditer`, `match.group`, `COPY_IDMS_RECORD_PATTERN.finditer`, `IDMS_VERB_RECORD_PATTERN.finditer`, `match.group('record').strip`, `match.group('record').strip().upper`, `records.append`, `DB_WITHIN_PATTERN.search`, `match.group('subschema').strip`, `match.group('subschema').strip().upper`, `dclgen_member_for`, `ProgramDependencies`, `str`, `str(program or '').strip`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L127: `for match in IDMS_VERB_RECORD_PATTERN.finditer(text)`
- L129: `if name and name not in _NOT_A_RECORD and (name not in records)`
- L134: `if match`

## Change responsibility

After modifying this Python file, review [prompt/02_MAINFRAME_PIPELINE.md](../../02_MAINFRAME_PIPELINE.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
