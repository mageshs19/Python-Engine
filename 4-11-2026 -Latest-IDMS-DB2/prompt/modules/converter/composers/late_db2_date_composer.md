# `converter/composers/late_db2_date_composer.py`

Source: [converter/composers/late_db2_date_composer.py](../../../../converter/composers/late_db2_date_composer.py) | 79 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `3b8816f6340bab1b34527d123b796056a2815f96ea420c531620a0c590c86bd2`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Late DB2 date output conversion.

## Import declarations

```python
from __future__ import annotations
from converter.composers.cleanup.cleanup_message_collector import CleanupMessageCollector
from converter.composers.cleanup.db2_date_output_cleanup import Db2DateOutputCleanup
from converter.composers.cleanup.initialize_before_output_cleanup import InitializeBeforeOutputCleanup
```

## Local dependency notes

- [converter/composers/cleanup/cleanup_message_collector.py](cleanup/cleanup_message_collector.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](cleanup/db2_date_output_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](cleanup/initialize_before_output_cleanup.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/pipeline/conversion/conversion_layout_steps.py](../pipeline/conversion/conversion_layout_steps.md)

## Symbol contracts and control points

### `LateDb2DateComposer` - L51-L79

```python
class LateDb2DateComposer()
```

Applies the date and INITIALIZE passes to the relocated block.

### `LateDb2DateComposer.__init__` - L54-L60

```python
__init__(self) -> None
```

Observed calls (lexical order): `CleanupMessageCollector`, `Db2DateOutputCleanup`, `InitializeBeforeOutputCleanup`.

### `LateDb2DateComposer.compose` - L62-L79

```python
compose(self, text: str) -> str
```

Observed calls (lexical order): `self.collector.reset`, `str`, `self.initialize_cleanup.ensure_initialize_before_output_population`, `self.date_cleanup.convert_db2_date_moves_to_output_dates`, `list`, `output.rstrip`.

Control points:

- L65: `if not text`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
