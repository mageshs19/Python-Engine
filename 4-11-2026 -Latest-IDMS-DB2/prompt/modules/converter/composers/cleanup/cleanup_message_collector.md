# `converter/composers/cleanup/cleanup_message_collector.py`

Source: [converter/composers/cleanup/cleanup_message_collector.py](../../../../../converter/composers/cleanup/cleanup_message_collector.py) | 21 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `ce239f316e96d8638eaee6bc9bca6570fdf92697910c443946ff161ffab096b5`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Cleanup message collector.

## Import declarations

```python
from rules.cobol_cleanup_rules import CLEANUP_MESSAGES
```

## Local dependency notes

- [rules/cobol_cleanup_rules.py](../../../rules/cobol_cleanup_rules.md)

## Importers (18)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/cleanup/child_fetch_early_stop_cleanup.py](child_fetch_early_stop_cleanup.md)
- [converter/composers/cleanup/db2_date_output_cleanup.py](db2_date_output_cleanup.md)
- [converter/composers/cleanup/dclgen_include_cleanup.py](dclgen_include_cleanup.md)
- [converter/composers/cleanup/error_status_flag_cleanup.py](error_status_flag_cleanup.md)
- [converter/composers/cleanup/initialize_before_output_cleanup.py](initialize_before_output_cleanup.md)
- [converter/composers/cleanup/orphaned_idms_status_guard_cleanup.py](orphaned_idms_status_guard_cleanup.md)
- [converter/composers/cleanup/output_write_placement_cleanup.py](output_write_placement_cleanup.md)
- [converter/composers/cleanup/paragraph_terminator_cleanup.py](paragraph_terminator_cleanup.md)
- [converter/composers/cleanup/residual_idms_comment_cleanup.py](residual_idms_comment_cleanup.md)
- [converter/composers/cleanup/residual_idms_error_clause_cleanup.py](residual_idms_error_clause_cleanup.md)
- [converter/composers/cobol_cleanup_composer.py](../cobol_cleanup_composer.md)
- [converter/composers/late_db2_date_composer.py](../late_db2_date_composer.md)
- [tests/test_orphaned_idms_status_guard_cleanup.py](../../../tests/test_orphaned_idms_status_guard_cleanup.md)
- [tests/test_output_write_placement_cleanup.py](../../../tests/test_output_write_placement_cleanup.md)
- [tests/test_paragraph_terminator_area_a.py](../../../tests/test_paragraph_terminator_area_a.md)
- [tests/test_residual_idms_error_clause_cleanup.py](../../../tests/test_residual_idms_error_clause_cleanup.md)
- [tests/test_sw_status_child_fetch_driven_normalization.py](../../../tests/test_sw_status_child_fetch_driven_normalization.md)
- 1 further importers are recorded in [the source manifest](../../../../source_manifest.json).

## Symbol contracts and control points

### `CleanupMessageCollector` - L12-L21

```python
class CleanupMessageCollector()
```

### `CleanupMessageCollector.__init__` - L13-L14

```python
__init__(self) -> None
```

### `CleanupMessageCollector.reset` - L16-L17

```python
reset(self) -> None
```

### `CleanupMessageCollector.add` - L19-L21

```python
add(self, key: str, **fields: str) -> None
```

Observed calls (lexical order): `self.messages.append`, `template.format`.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
