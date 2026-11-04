# `tests/test_zowe_semantic_release_gate.py`

Source: [tests/test_zowe_semantic_release_gate.py](../../../tests/test_zowe_semantic_release_gate.py) | 117 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `3cab7e0eabb38108f713a399202bc82042a07f92768ee0d50c74d8542593e423`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Batch-wide semantic release checks have no per-program exceptions.

## Import declarations

```python
from pathlib import Path
from types import SimpleNamespace
import pytest
from mainframe import zowe_semantic_release_gate as gate
from mainframe.verification.record_write_contract import RecordWriteFinding
from mainframe.verification.record_population_contract import PopulationFinding
```

## Local dependency notes

- [mainframe/__init__.py](../mainframe/__init__.md)
- [mainframe/verification/record_population_contract.py](../mainframe/verification/record_population_contract.md)
- [mainframe/verification/record_write_contract.py](../mainframe/verification/record_write_contract.md)
- [mainframe/zowe_semantic_release_gate.py](../mainframe/zowe_semantic_release_gate.md)

## Symbol contracts and control points

### `workspace` - L11-L24

```python
workspace(tmp_path: Path, monkeypatch)
```

Observed calls (lexical order): `roots.values`, `item.mkdir`, `(roots['Mapping Sheet'] / 'mapping.csv').write_text`, `monkeypatch.setattr`.

Control points:

- L13: `for item in roots.values()`
- L18: `for (symbol, location) in (('program_dir', 'Program'), ('output_dir', 'Output'), ('review_dir', 'Review'), ('mapping_dir', 'Mapping Sheet'), ('dclgen_dir', 'DCLGen'))`

### `add_program` - L27-L36

```python
add_program(roots, source_id, target_id=None)
```

Observed calls (lexical order): `gate.NameDerivationResolver`, `gate.NameDerivationResolver().derive`, `(roots['Program'] / f'{source_id}.cbl').write_text`, `output.write_text`.

### `test_generic_batch_matches_multiple_inputs_and_records_success` - L39-L45

```python
test_generic_batch_matches_multiple_inputs_and_records_success(workspace)
```

Observed calls (lexical order): `add_program`, `gate.audit_generated_batch`, `all`, `item.startswith`, `len`, `(workspace['Review'] / gate.REPORT_NAME).read_text`.

### `test_unresolved_semantic_review_blocks_entire_batch` - L48-L65

```python
test_unresolved_semantic_review_blocks_entire_batch(workspace, monkeypatch)
```

Observed calls (lexical order): `add_program`, `monkeypatch.setattr`, `gate.audit_generated_batch`, `any`.

### `test_unresolved_semantic_review_blocks_entire_batch.FakeAuditor` - L53-L59

```python
class FakeAuditor(real_auditor)
```

### `test_unresolved_semantic_review_blocks_entire_batch.FakeAuditor.audit` - L54-L59

```python
audit(self, source, target)
```

Observed calls (lexical order): `Path`, `SimpleNamespace`, `super`, `super().audit`.

Control points:

- L55: `if Path(source).stem == 'VM7BD200'`

### `test_unpaired_output_blocks_batch` - L68-L73

```python
test_unpaired_output_blocks_batch(workspace)
```

Observed calls (lexical order): `add_program`, `(workspace['Output'] / 'ORPHAN_batch.cbl').write_text`, `gate.audit_generated_batch`, `any`.

### `test_duplicate_target_outputs_block_batch` - L76-L81

```python
test_duplicate_target_outputs_block_batch(workspace)
```

Observed calls (lexical order): `add_program`, `(workspace['Output'] / 'VMDZ4420_other.cbl').write_text`, `gate.audit_generated_batch`, `any`.

### `test_missing_mapping_source_or_generated_blocks_batch` - L84-L90

```python
test_missing_mapping_source_or_generated_blocks_batch(workspace)
```

Observed calls (lexical order): `gate.audit_generated_batch`, `add_program`, `(workspace['Mapping Sheet'] / 'mapping.csv').unlink`.

### `test_overlong_program_id_is_never_silently_truncated_on_upload` - L93-L97

```python
test_overlong_program_id_is_never_silently_truncated_on_upload(workspace)
```

Observed calls (lexical order): `add_program`, `gate.audit_generated_batch`, `any`.

### `test_unverified_copybook_output_blocks_release` - L100-L107

```python
test_unverified_copybook_output_blocks_release(workspace, monkeypatch)
```

Observed calls (lexical order): `add_program`, `monkeypatch.setattr`, `RecordWriteFinding`, `gate.audit_generated_batch`, `any`.

### `test_unpopulated_numeric_fields_block_release` - L110-L117

```python
test_unpopulated_numeric_fields_block_release(workspace, monkeypatch)
```

Observed calls (lexical order): `add_program`, `monkeypatch.setattr`, `PopulationFinding`, `gate.audit_generated_batch`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
