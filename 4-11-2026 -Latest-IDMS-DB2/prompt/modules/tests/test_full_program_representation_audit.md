# `tests/test_full_program_representation_audit.py`

Source: [tests/test_full_program_representation_audit.py](../../../tests/test_full_program_representation_audit.py) | 189 lines.
Owning logic guide: [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md).
Source SHA-256: `b5a258ab10e78c5e8fa2f4bbb909fba717d8b583d700706a8c55dad4b98f2fc8`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

No module-level purpose docstring. The symbol contracts and observed dependencies below are extracted from source; use the owning guide for subsystem context.

## Module-level bindings

`ROOT` (L21), `COL` (L22), `PACKED` (L24), `IDENTITY` (L89)

## Import declarations

```python
from pathlib import Path
from dataclasses import replace
import re
import pytest
from converter.domain.models import DclgenColumn, SheetMappingRow
from converter.composers.program_identity_initializer import ProgramIdentityInitializer
from mainframe.verification.group_representation_contract import audit_character_group_moves, audit_target_character_widths
from review.engine.context import ReviewContext
from review.engine.reviewer import Reviewer, is_accepted, blockers
from review.engine.check_base import Check, CRITICAL
from review.checks.chk_35_group_representation import GroupRepresentationCheck
from review.checks.chk_36_production_evidence import ProductionEvidenceCheck
from review.checks.chk_04_program_header import CSPG
from review.checks.chk_24_picture_and_length import picture_category, picture_length
from review.runner.workspace_inputs import WorkspaceReviewInputs
from review.runner.review_file import build_context
from converter.analyzers.program_flow.procedure_control_flow_graph import ProcedureControlFlowGraphBuilder
```

## Local dependency notes

- [converter/analyzers/program_flow/procedure_control_flow_graph.py](../converter/analyzers/program_flow/procedure_control_flow_graph.md)
- [converter/composers/program_identity_initializer.py](../converter/composers/program_identity_initializer.md)
- [converter/domain/models.py](../converter/domain/models.md)
- [mainframe/verification/group_representation_contract.py](../mainframe/verification/group_representation_contract.md)
- [review/checks/chk_04_program_header.py](../review/checks/chk_04_program_header.md)
- [review/checks/chk_24_picture_and_length.py](../review/checks/chk_24_picture_and_length.md)
- [review/checks/chk_35_group_representation.py](../review/checks/chk_35_group_representation.md)
- [review/checks/chk_36_production_evidence.py](../review/checks/chk_36_production_evidence.md)
- [review/engine/check_base.py](../review/engine/check_base.md)
- [review/engine/context.py](../review/engine/context.md)
- [review/engine/reviewer.py](../review/engine/reviewer.md)
- [review/runner/review_file.py](../review/runner/review_file.md)
- [review/runner/workspace_inputs.py](../review/runner/workspace_inputs.md)

## Symbol contracts and control points

### `fixed` - L41-L43

```python
fixed(text)
```

Observed calls (lexical order): `'\n'.join`, `s.ljust`, `enumerate`, `text.splitlines`.

### `test_character_group_to_packed_is_blocked` - L46-L50

```python
test_character_group_to_packed_is_blocked(formatter)
```

Observed calls (lexical order): `audit_character_group_moves`, `formatter`, `len`.

### `test_same_length_does_not_prove_binary_encoding` - L53-L54

```python
test_same_length_does_not_prove_binary_encoding(width)
```

Observed calls (lexical order): `audit_character_group_moves`, `replace`.

### `test_rule_is_not_driven_by_names` - L57-L59

```python
test_rule_is_not_driven_by_names(name)
```

Observed calls (lexical order): `PACKED.replace`, `PACKED.replace('DEST-KEY', name).replace`, `audit_character_group_moves`.

### `test_display_group_and_elementary_numeric_move_not_misclassified` - L62-L65

```python
test_display_group_and_elementary_numeric_move_not_misclassified()
```

Observed calls (lexical order): `PACKED.replace`, `audit_character_group_moves`.

### `test_comments_literals_and_storage_values_do_not_become_moves` - L68-L72

```python
test_comments_literals_and_storage_values_do_not_become_moves()
```

Observed calls (lexical order): `PACKED.replace`, `audit_character_group_moves`.

### `test_nested_receiving_group_and_wrapped_transfer` - L75-L79

```python
test_nested_receiving_group_and_wrapped_transfer()
```

Observed calls (lexical order): `PACKED.replace`, `PACKED.replace('01 DEST-KEY.', '01 OUTER.\n 02 DEST-KEY.').replace`, `audit_character_group_moves`.

### `test_character_contract_conflict_only_for_used_host` - L82-L86

```python
test_character_contract_conflict_only_for_used_host()
```

Observed calls (lexical order): `SheetMappingRow`, `audit_target_character_widths`, `len`, `replace`.

### `test_generic_diagnostic_identity_is_first_executable_statement` - L104-L109

```python
test_generic_diagnostic_identity_is_first_executable_statement(formatter)
```

Observed calls (lexical order): `formatter`, `ProgramIdentityInitializer`, `ProgramIdentityInitializer().compose`, `result.index`, `result.count`.

### `test_identity_does_not_guess_or_override_author_defined_assignment` - L117-L118

```python
test_identity_does_not_guess_or_override_author_defined_assignment(source)
```

Observed calls (lexical order): `ProgramIdentityInitializer`, `ProgramIdentityInitializer().compose`.

### `test_picture_parser_ignores_usage_and_value_tokens` - L127-L129

```python
test_picture_parser_ignores_usage_and_value_tokens(pic, category, length)
```

Observed calls (lexical order): `picture_category`, `picture_length`.

### `test_cs_program_parentheses_are_not_regex_end_anchors` - L132-L133

```python
test_cs_program_parentheses_are_not_regex_end_anchors()
```

Observed calls (lexical order): `CSPG.fullmatch`.

### `test_exception_in_critical_check_cannot_pass_review` - L136-L145

```python
test_exception_in_critical_check_cannot_pass_review()
```

Observed calls (lexical order): `Broken`, `ReviewContext`, `Reviewer`, `Reviewer([Broken()]).review`, `is_accepted`, `blockers`.

### `test_exception_in_critical_check_cannot_pass_review.Broken` - L137-L141

```python
class Broken(Check)
```

Declared class/data-model fields:

```python
CHECK_ID = 'CHK-X'
SEVERITY = CRITICAL
```

### `test_exception_in_critical_check_cannot_pass_review.Broken.review` - L140-L141

```python
review(self, ctx, view, record)
```

Observed calls (lexical order): `ValueError`.

Explicit raises: `ValueError('missing evidence')`.

### `test_missing_metadata_blocks_requested_production_review` - L148-L150

```python
test_missing_metadata_blocks_requested_production_review()
```

Observed calls (lexical order): `ReviewContext`, `ProductionEvidenceCheck`, `Reviewer`, `Reviewer([ProductionEvidenceCheck()]).review`, `is_accepted`.

### `test_real_current_member_fails_representation_not_paragraph_numbering` - L153-L165

```python
test_real_current_member_fails_representation_not_paragraph_numbering()
```

Observed calls (lexical order): `WorkspaceReviewInputs`, `build_context`, `len`, `GroupRepresentationCheck`, `ProductionEvidenceCheck`, `Reviewer`, `Reviewer([GroupRepresentationCheck(), ProductionEvidenceCheck()]).review`, `is_accepted`.

### `test_manual_numbering_does_not_change_the_nine_local_business_edges` - L168-L181

```python
test_manual_numbering_does_not_change_the_nine_local_business_edges()
```

Observed calls (lexical order): `(ROOT / 'tests/fixtures/representation_v122/VMDZ4310.cbl').read_text`, `(ROOT / 'mainframe/workspace/Manual Output/VMDZ4310.txt').read_text`, `edges`, `ProgramIdentityInitializer`, `ProgramIdentityInitializer().compose`.

### `test_manual_numbering_does_not_change_the_nine_local_business_edges.edges` - L172-L179

```python
edges(text)
```

Observed calls (lexical order): `ProcedureControlFlowGraphBuilder`, `ProcedureControlFlowGraphBuilder().build`, `len`, `re.sub`, `normalize`.

### `test_workspace_metadata_failure_is_reported_not_success` - L184-L189

```python
test_workspace_metadata_failure_is_reported_not_success(tmp_path)
```

Observed calls (lexical order): `WorkspaceReviewInputs`, `adapter.for_program`, `any`.

## Change responsibility

After modifying this Python file, review [prompt/10_TESTING_AND_VALIDATION.md](../../10_TESTING_AND_VALIDATION.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
