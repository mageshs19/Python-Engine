# `tests/test_copybook_provenance_and_occurs.py`

Source: [tests/test_copybook_provenance_and_occurs.py](../../../tests/test_copybook_provenance_and_occurs.py) | 135 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `3c02446520642bf3059bb5e7fa77569f53d3fbda03d08cc6be31b8027acdf532`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Generic COPY provenance and output-buffer data-flow regressions.

## Import declarations

```python
from pathlib import Path
import pytest
from mainframe.verification.cobol_storage_layout import group_byte_length
from mainframe.verification.copybook_provenance import resolve_copybooks
from mainframe.verification.record_population_contract import audit_record_population
from mainframe.verification.record_write_contract import audit_fixed_record_writes
from mainframe.zowe_copybook_upload import require_copybook_upload_configuration
```

## Local dependency notes

- [mainframe/verification/cobol_storage_layout.py](../mainframe/verification/cobol_storage_layout.md)
- [mainframe/verification/copybook_provenance.py](../mainframe/verification/copybook_provenance.md)
- [mainframe/verification/record_population_contract.py](../mainframe/verification/record_population_contract.md)
- [mainframe/verification/record_write_contract.py](../mainframe/verification/record_write_contract.md)
- [mainframe/zowe_copybook_upload.py](../mainframe/zowe_copybook_upload.md)

## Symbol contracts and control points

### `test_fixed_occurs_group_and_leaf_and_redefines` - L13-L22

```python
test_fixed_occurs_group_and_leaf_and_redefines()
```

Observed calls (lexical order): `group_byte_length`.

### `test_variable_or_unsafe_occurs_is_not_assumed_fixed` - L27-L29

```python
test_variable_or_unsafe_occurs_is_not_assumed_fixed(clause)
```

Observed calls (lexical order): `pytest.raises`, `group_byte_length`.

### `test_derived_copybook_expands_only_when_source_copy_proves_name` - L32-L44

```python
test_derived_copybook_expands_only_when_source_copy_proves_name(tmp_path)
```

Observed calls (lexical order): `inputs.mkdir`, `(inputs / 'VMBD123I.cpy').write_text`, `resolve_copybooks`, `audit_fixed_record_writes`, `audit_record_population`.

### `test_no_original_copy_provenance_blocks_derivation` - L47-L49

```python
test_no_original_copy_provenance_blocks_derivation(tmp_path)
```

Observed calls (lexical order): `resolve_copybooks`.

### `test_source_copybook_with_nested_copy_is_blocked` - L52-L55

```python
test_source_copybook_with_nested_copy_is_blocked(tmp_path)
```

Observed calls (lexical order): `(tmp_path / 'VMBD123I.cpy').write_text`, `resolve_copybooks`.

### `test_missing_output_copybook_dataset_blocks_before_network` - L58-L63

```python
test_missing_output_copybook_dataset_blocks_before_network(tmp_path, monkeypatch)
```

Observed calls (lexical order): `(tmp_path / 'Generated Copybooks').mkdir`, `(tmp_path / 'Generated Copybooks' / 'VMDZ123I.cpy').write_text`, `monkeypatch.delenv`, `pytest.raises`, `require_copybook_upload_configuration`.

### `test_sequential_initializer_proves_other_paragraph_write` - L66-L84

```python
test_sequential_initializer_proves_other_paragraph_write()
```

Observed calls (lexical order): `audit_record_population`, `text.replace`, `any`.

### `test_conditional_initializer_is_not_accepted_as_proof` - L87-L103

```python
test_conditional_initializer_is_not_accepted_as_proof()
```

Observed calls (lexical order): `any`, `audit_record_population`.

### `test_real_source_copybook_matches_documented_output_layout` - L106-L114

```python
test_real_source_copybook_matches_documented_output_layout(tmp_path)
```

Observed calls (lexical order): `Path`, `Path(__file__).resolve`, `(workspace / 'Program' / 'VM4BD310.cbl').read_text`, `(workspace / 'Output').glob`, `next`, `next((workspace / 'Output').glob('VMDZ4310_*.cbl')).read_text`, `resolve_copybooks`, `audit_fixed_record_writes`, `audit_record_population`, `(tmp_path / 'VMDZ510I.cpy').read_text`, `group_byte_length`.

### `test_copybook_name_is_not_rewritten_inside_value_literal` - L117-L126

```python
test_copybook_name_is_not_rewritten_inside_value_literal(tmp_path)
```

Observed calls (lexical order): `(tmp_path / 'VMBD123I.cpy').write_text`, `resolve_copybooks`, `result.staged_members[0].read_text`.

### `test_copybook_replacing_without_period_is_blocked` - L129-L135

```python
test_copybook_replacing_without_period_is_blocked(tmp_path)
```

Observed calls (lexical order): `(tmp_path / 'VMBD123I.cpy').write_text`, `resolve_copybooks`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
