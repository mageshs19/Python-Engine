# `mainframe/zowe_semantic_release_gate.py`

Source: [mainframe/zowe_semantic_release_gate.py](../../../mainframe/zowe_semantic_release_gate.py) | 180 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `19fec8245770dd6b72ec2ea2177828401e97bcafd2b9c3450685ecdfdd84b24f`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Fail-closed semantic coverage gate for each generated program in a Zowe batch.

## Module-level bindings

`REPORT_NAME` (L24)

## Import declarations

```python
from __future__ import annotations
from pathlib import Path
import shutil
from converter.analyzers.program_flow.business_operation_parity_audit import BusinessOperationParityAuditor
from converter.parsers.cobol_parser import CobolParser
from converter.services.name_derivation_resolver import NameDerivationResolver
from mainframe.zowe_workspace import copybook_dir, dclgen_dir, mapping_dir, output_dir, program_dir, review_dir
from mainframe.zowe_writer import member_from_output_name
from mainframe.verification.record_write_contract import audit_fixed_record_writes
from mainframe.verification.record_population_contract import audit_record_population
from mainframe.verification.copybook_provenance import resolve_copybooks
from mainframe.verification.manual_direct_update_parity import manually_confirmed_direct_updates
from review.runner.workspace_inputs import WorkspaceReviewInputs
from mainframe.verification.group_representation_contract import audit_character_group_moves, audit_target_character_widths
```

## Local dependency notes

- [converter/analyzers/program_flow/business_operation_parity_audit.py](../converter/analyzers/program_flow/business_operation_parity_audit.md)
- [converter/parsers/cobol_parser.py](../converter/parsers/cobol_parser.md)
- [converter/services/name_derivation_resolver.py](../converter/services/name_derivation_resolver.md)
- [mainframe/verification/copybook_provenance.py](verification/copybook_provenance.md)
- [mainframe/verification/group_representation_contract.py](verification/group_representation_contract.md)
- [mainframe/verification/manual_direct_update_parity.py](verification/manual_direct_update_parity.md)
- [mainframe/verification/record_population_contract.py](verification/record_population_contract.md)
- [mainframe/verification/record_write_contract.py](verification/record_write_contract.md)
- [mainframe/zowe_workspace.py](zowe_workspace.md)
- [mainframe/zowe_writer.py](zowe_writer.md)
- [review/runner/workspace_inputs.py](../review/runner/workspace_inputs.md)

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_pipeline_steps.py](zowe_pipeline_steps.md)
- [tests/test_zowe_semantic_release_gate.py](../tests/test_zowe_semantic_release_gate.md)

## Symbol contracts and control points

### `_derive_db2_program_id` - L27-L29

```python
_derive_db2_program_id(source_text: str) -> str
```

Observed calls (lexical order): `CobolParser`, `CobolParser().program_id`, `NameDerivationResolver`, `NameDerivationResolver().derive`.

### `audit_generated_batch` - L32-L180

```python
audit_generated_batch() -> tuple[bool, list[str]]
```

Observed calls (lexical order): `program_dir`, `program_dir().glob`, `sorted`, `output_dir`, `output_dir().glob`, `mapping_dir`, `mapping_dir().glob`, `len`, `BusinessOperationParityAuditor`, `dclgen_dir`, `WorkspaceReviewInputs`, `generated_copybooks.exists`, `shutil.rmtree`, `set`, `source.read_text`, `_derive_db2_program_id`.
Another 22 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L36: `if not sources or not generated`
- L39: `if len(mapping_files) != 1`
- L50: `if generated_copybooks.exists()`
- L55: `for source in sources`
- L58: `if not target or target in {'[]', 'UNKNOWN'}`
- L66: `if len(candidates) != 1 or candidates[0] in seen_targets`
- L76: `if member != target or member in seen_members`
- L92: `for error in copybooks.errors`
- Another 11 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
