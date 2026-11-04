# `converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py`

Source: [converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py](../../../../../converter/composers/update_sql_cleanup/update_sql_cleanup_patterns.py) | 98 lines.
Owning logic guide: [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md).
Source SHA-256: `958ef5401b575e5861ab752c27897e4c27fb32b190c7135dc581db38df4c23bd`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Update-program SQL cleanup regex patterns.

## Module-level bindings

`CONVERTED_OBTAIN_CALC_PATTERN` (L12), `CONVERTED_MODIFY_PATTERN` (L17), `EXEC_SQL_START_PATTERN` (L22), `EXEC_SQL_END_PATTERN` (L27), `INCLUDE_PATTERN` (L32), `SQLCODE_IF_PATTERN` (L37), `END_IF_PATTERN` (L42), `MALFORMED_SQLERROR_ENDIF_PATTERN` (L47), `MOVE_TO_BARE_FIELD_PATTERN` (L52), `MOVE_TO_DCL_HOST_PATTERN` (L57), `SQL_LOCATION_PATTERN` (L62), `LINKAGE_SECTION_PATTERN` (L67), `TIMESTAMP_PARAGRAPH_PATTERN` (L72), `STOP_RUN_PATTERN` (L77), `SQLCODE_EVALUATE_PATTERN` (L84), `END_EVALUATE_PATTERN` (L89), `LONE_PERIOD_PATTERN` (L95)

## Import declarations

```python
import re
```

## Importers (3)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/update_sql_cleanup/scan_mixin.py](scan_mixin.md)
- [converter/composers/update_sql_cleanup/sql_block_scanner.py](sql_block_scanner.md)
- [converter/composers/update_sql_cleanup_base.py](../update_sql_cleanup_base.md)

## Change responsibility

After modifying this Python file, review [prompt/07_UPDATE_RESTART_AND_TRANSACTIONS.md](../../../../07_UPDATE_RESTART_AND_TRANSACTIONS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
