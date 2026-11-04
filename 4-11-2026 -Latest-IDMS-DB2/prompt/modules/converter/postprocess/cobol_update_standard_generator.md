# `converter/postprocess/cobol_update_standard_generator.py`

Source: [converter/postprocess/cobol_update_standard_generator.py](../../../../converter/postprocess/cobol_update_standard_generator.py) | 255 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `b073af493147fcc3d090a1d6626a7880e0f92a6def36b348581d25699bd0dd75`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`LEGACY_RESTART_SELECT_QUERYNO` (L51), `LEGACY_RESTART_UPDATE_QUERYNO` (L52), `LEGACY_RESTART_INSERT_QUERYNO` (L53)

## Import declarations

```python
from __future__ import annotations
from converter.postprocess.dynamic_metadata_resolver import DclgenRoleInfo, UpdateProgramContext
from rules.update_restart_rules import RESTART_DEFAULT_PHASE, RESTART_PARAGRAPH_NAMES, RESTART_RETENTION_DAYS, RESTART_STATUS_COMPLETE, RESTART_STATUS_INCOMPLETE, UPDATE_RESTART_WS_NAMES, UPDATE_STANDARD_DATE_WS_LINES
from rules.update_standard_generator_templates import ABEND_CALL_STATEMENT, COMMIT_COUNTER_LEGACY, COMMIT_COUNTER_RESET_VALUE, COPYBOOK_INCLUDE_TEMPLATE, CS_PROGRAM_FIELD, DA_DD_MM_CCYY_FIELD, DCLGEN_INCLUDE_TEMPLATE, DISPLAY_ERROR_REC_TEMPLATE, DISPLAY_PREVIOUS_RUN_COMPLETE, EOF_NOT_SET_VALUE, EOF_SET_VALUE, PROCESS_COMMIT_TEMPLATE, READ_FLAT_FILE_TEMPLATE, RESTART_CONTROL_TEMPLATE, RESTART_FOUND_TEMPLATE, RESTART_LENGTH_BASE, RESTART_SQL_TEMPLATE, SQL_ERROR_PARAGRAPH, WORKING_STORAGE_TEMPLATE, WRITE_RESTART_TEMPLATE
```

## Local dependency notes

- [converter/postprocess/dynamic_metadata_resolver.py](dynamic_metadata_resolver.md)
- [rules/update_restart_rules.py](../../rules/update_restart_rules.md)
- [rules/update_standard_generator_templates.py](../../rules/update_standard_generator_templates.md)

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/postprocess/update_program_enhancer.py](update_program_enhancer.md)
- [converter/postprocess/update_restart_paragraph_manager.py](update_restart_paragraph_manager.md)
- [converter/postprocess/update_storage_include_manager.py](update_storage_include_manager.md)

## Symbol contracts and control points

### `CobolUpdateStandardGenerator` - L57-L255

```python
class CobolUpdateStandardGenerator()
```

Generates update-program COBOL snippets from resolved metadata.

### `CobolUpdateStandardGenerator.copybook_include` - L66-L69

```python
copybook_include(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `COPYBOOK_INCLUDE_TEMPLATE.format`.

### `CobolUpdateStandardGenerator.dclgen_include` - L71-L72

```python
dclgen_include(self, role: DclgenRoleInfo) -> str
```

Observed calls (lexical order): `DCLGEN_INCLUDE_TEMPLATE.format`.

### `CobolUpdateStandardGenerator.dclgen_include_by_name` - L74-L77

```python
dclgen_include_by_name(self, include_name: str) -> str
```

Observed calls (lexical order): `DCLGEN_INCLUDE_TEMPLATE.format`, `str`, `str(include_name or '').strip`, `str(include_name or '').strip().upper`.

### `CobolUpdateStandardGenerator.working_storage` - L79-L98

```python
working_storage(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `WORKING_STORAGE_TEMPLATE.format`.

### `CobolUpdateStandardGenerator.date_working_storage` - L100-L101

```python
date_working_storage(self) -> str
```

Observed calls (lexical order): `'\n'.join`.

### `CobolUpdateStandardGenerator.read_flat_file` - L103-L111

```python
read_flat_file(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `READ_FLAT_FILE_TEMPLATE.format`.

### `CobolUpdateStandardGenerator.restart_paragraphs` - L113-L121

```python
restart_paragraphs(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `self.restart_control`, `self.restart_found`, `self.write_restart`, `self.process_commit`, `self.restart_sql`, `'\n\n'.join`, `part.strip`.

### `CobolUpdateStandardGenerator.restart_control` - L123-L144

```python
restart_control(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `RESTART_CONTROL_TEMPLATE.format`.

Control points:

- L125: `if not role`

### `CobolUpdateStandardGenerator.restart_found` - L146-L164

```python
restart_found(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `RESTART_FOUND_TEMPLATE.format`.

Control points:

- L148: `if not role`

### `CobolUpdateStandardGenerator.write_restart` - L166-L188

```python
write_restart(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `WRITE_RESTART_TEMPLATE.format`.

Control points:

- L168: `if not role`

### `CobolUpdateStandardGenerator.process_commit` - L190-L218

```python
process_commit(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `PROCESS_COMMIT_TEMPLATE.format`, `DISPLAY_ERROR_REC_TEMPLATE.format`.

Control points:

- L192: `if not role`

### `CobolUpdateStandardGenerator.restart_sql` - L220-L255

```python
restart_sql(self, context: UpdateProgramContext) -> str
```

Observed calls (lexical order): `DISPLAY_ERROR_REC_TEMPLATE.format`, `RESTART_SQL_TEMPLATE.format`.

Control points:

- L222: `if not role`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
