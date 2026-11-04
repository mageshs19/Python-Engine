# `converter/generators/timestamp_generator.py`

Source: [converter/generators/timestamp_generator.py](../../../../converter/generators/timestamp_generator.py) | 145 lines.
Owning logic guide: [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md).
Source SHA-256: `9765c460fb552fd0046882d0a67e2cda0b05bb282e4ac6a12bf40941e9cb36b7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`__all__` (L145)

## Import declarations

```python
from __future__ import annotations
from typing import List, Tuple
from converter.generators.initialization.line_geometry import LineGeometry
from converter.generators.timestamp.cs_program_declarator import CsProgramDeclarator
from converter.generators.timestamp.program_id_resolver import ProgramIdResolver
from converter.generators.timestamp.timestamp_anchors import TimestampAnchors
from converter.generators.timestamp.timestamp_paragraph_builder import TimestampParagraphBuilder
from converter.generators.timestamp.timestamp_ws_builder import TimestampWorkingStorageBuilder
from patterns.timestamp_patterns import COBOL_WRITE_OPERATION_PATTERN, DB2_WRITE_OPERATION_PATTERN, END_EXEC_PATTERN, EXEC_SQL_PATTERN
from rules.timestamp_audit_rules import TIMESTAMP_MESSAGES, TIMESTAMP_PARAGRAPH_EXIT_NAME, TIMESTAMP_PARAGRAPH_NAME, TIMESTAMP_WS_MARKER
from converter.generators.timestamp.program_name_binder import ProgramNameBinder
```

## Local dependency notes

- [converter/generators/initialization/line_geometry.py](initialization/line_geometry.md)
- [converter/generators/timestamp/cs_program_declarator.py](timestamp/cs_program_declarator.md)
- [converter/generators/timestamp/program_id_resolver.py](timestamp/program_id_resolver.md)
- [converter/generators/timestamp/program_name_binder.py](timestamp/program_name_binder.md)
- [converter/generators/timestamp/timestamp_anchors.py](timestamp/timestamp_anchors.md)
- [converter/generators/timestamp/timestamp_paragraph_builder.py](timestamp/timestamp_paragraph_builder.md)
- [converter/generators/timestamp/timestamp_ws_builder.py](timestamp/timestamp_ws_builder.md)
- [patterns/timestamp_patterns.py](../../patterns/timestamp_patterns.md)
- [rules/timestamp_audit_rules.py](../../rules/timestamp_audit_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_component_factory.py](../pipeline/conversion/conversion_component_factory.md)

## Symbol contracts and control points

### `TimestampGenerator` - L38-L142

```python
class TimestampGenerator()
```

Declared class/data-model fields:

```python
WS_MARKER = TIMESTAMP_WS_MARKER
PARAGRAPH_NAME = TIMESTAMP_PARAGRAPH_NAME
PARAGRAPH_EXIT_NAME = TIMESTAMP_PARAGRAPH_EXIT_NAME
```

### `TimestampGenerator.__init__` - L44-L74

```python
__init__(self, mapping_repository=None, table_name_resolver=None, host_variable_resolver=None) -> None
```

Observed calls (lexical order): `LineGeometry`, `TimestampAnchors`, `ProgramIdResolver`, `CsProgramDeclarator`, `ProgramNameBinder`, `TimestampWorkingStorageBuilder`, `TimestampParagraphBuilder`.

### `TimestampGenerator.apply` - L76-L106

```python
apply(self, cobol_text: str, target_program_id: str='') -> Tuple[str, List[str]]
```

Observed calls (lexical order): `str`, `text.strip`, `self.geometry.split`, `self.cs_program.declare`, `self.messages.extend`, `self.program_name.bind`, `self.working_storage.ensure`, `self.paragraph.ensure_paragraph`, `self.paragraph.ensure_perform`, `self._log`, `self.geometry.join`, `self.geometry.join(lines).rstrip`.

Control points:

- L84: `if not text.strip()`

### `TimestampGenerator.has_db2_write_activity` - L108-L130

```python
has_db2_write_activity(self, cobol_text: str) -> bool
```

Observed calls (lexical order): `self.geometry.split`, `str`, `self.geometry.is_comment_or_blank`, `self.geometry.body`, `EXEC_SQL_PATTERN.match`, `DB2_WRITE_OPERATION_PATTERN.match`, `END_EXEC_PATTERN.match`, `COBOL_WRITE_OPERATION_PATTERN.match`.

Control points:

- L111: `for line in self.geometry.split(str(cobol_text or ''))`
- L112: `if self.geometry.is_comment_or_blank(line)`
- L116: `if EXEC_SQL_PATTERN.match(body)`
- L120: `if in_exec_sql and DB2_WRITE_OPERATION_PATTERN.match(body)`
- L123: `if END_EXEC_PATTERN.match(body)`
- L127: `if COBOL_WRITE_OPERATION_PATTERN.match(body)`

### `TimestampGenerator._has_db2_write_activity` - L132-L133

```python
_has_db2_write_activity(self, text: str) -> bool
```

Observed calls (lexical order): `self.has_db2_write_activity`.

### `TimestampGenerator._log` - L135-L142

```python
_log(self, key: str, **values) -> None
```

Observed calls (lexical order): `TIMESTAMP_MESSAGES.get`, `str`, `self.messages.append`, `template.format`.

Control points:

- L137: `if not template`

## Change responsibility

After modifying this Python file, review [prompt/04_LR_IDMS_DB2_CONVERSION.md](../../../04_LR_IDMS_DB2_CONVERSION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
