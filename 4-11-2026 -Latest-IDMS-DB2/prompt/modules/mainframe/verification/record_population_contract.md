# `mainframe/verification/record_population_contract.py`

Source: [mainframe/verification/record_population_contract.py](../../../../mainframe/verification/record_population_contract.py) | 201 lines.
Owning logic guide: [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md).
Source SHA-256: `c4751d502f69689c3f5f092fe0666604c6197d62c29c065cd8da3a3cb159f6eb`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Conservative per-WRITE fixed-record field-population audit.

## Module-level bindings

`_PARA` (L24), `_WRITE` (L25), `_DEST` (L26), `_INIT` (L27), `_MOVE` (L28), `_VERB` (L29)

## Import declarations

```python
from __future__ import annotations
import re
from collections import Counter
from dataclasses import dataclass
from .cobol_storage_layout import Field, extract_group
from .record_write_contract import _code, _mask_quoted_literals
```

## Local dependency notes

- [mainframe/verification/cobol_storage_layout.py](cobol_storage_layout.md)
- [mainframe/verification/record_write_contract.py](record_write_contract.md)

## Importers (4)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [mainframe/zowe_semantic_release_gate.py](../zowe_semantic_release_gate.md)
- [tests/test_copybook_provenance_and_occurs.py](../../tests/test_copybook_provenance_and_occurs.md)
- [tests/test_record_population_contract.py](../../tests/test_record_population_contract.md)
- [tests/test_zowe_semantic_release_gate.py](../../tests/test_zowe_semantic_release_gate.md)

## Symbol contracts and control points

### `PopulationFinding` - L33-L37

```python
class PopulationFinding()
```

Declared class/data-model fields:

```python
level: str
buffer: str
field: str
reason: str
```

### `_leaves` - L40-L52

```python
_leaves(root: Field) -> list[tuple[Field, tuple[str, ...]]]
```

Observed calls (lexical order): `walk`.

### `_leaves.walk` - L42-L50

```python
walk(node: Field, ancestors: tuple[str, ...])
```

Observed calls (lexical order): `re.search`, `walk`, `found.append`.

Control points:

- L43: `if node.name == 'FILLER' or re.search('\\bREDEFINES\\b', node.source, re.I)`
- L46: `if node.children`
- L47: `for c in node.children`
- L49: `if re.search('\\bPIC(?:TURE)?\\s+(?:IS\\s+)?S?9', node.source, re.I)`

### `_paragraphs` - L55-L77

```python
_paragraphs(lines: list[str]) -> list[tuple[str, str]]
```

Return paragraph body with its label; fixed-format sequence excluded.

Observed calls (lexical order): `_code`, `re.match`, `_PARA.fullmatch`, `' '.join`, `result.append`, `new.group`, `new.group(1).upper`, `body.append`.

Control points:

- L61: `for line in lines`
- L63: `if re.match('^PROCEDURE\\s+DIVISION\\b', code, re.I)`
- L66: `if not procedure or not code`
- L69: `if new`
- L70: `if name`
- L75: `if name`

### `_written_targets_before` - L80-L109

```python
_written_targets_before(body: str, write_pos: int) -> tuple[set[tuple[str, str | None]], set[str]]
```

Capture simple MOVE targets and INITIALIZE groups without guessing receivers.

Observed calls (lexical order): `_mask_quoted_literals`, `_mask_quoted_literals(body[:write_pos]).upper`, `set`, `_MOVE.finditer`, `_VERB.search`, `occurrence.end`, `len`, `next_verb.start`, `re.match`, `_DEST.search`, `dest.group`, `dest.start`, `segment[:dest.start()].strip`, `re.fullmatch`, `targets.add`, `_INIT.finditer`.
Another 1 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L90: `for occurrence in _MOVE.finditer(earlier)`
- L93: `if ' TO ' not in f' {segment} '`
- L96: `if re.match('\\s+CORR(?:ESPONDING)?\\b', segment)`
- L99: `if dest`
- L105: `if re.fullmatch('SPACE[S]?', sender)`

### `_proven_caller_initializers` - L112-L146

```python
_proven_caller_initializers(paragraphs: list[tuple[str, str]], write_paragraph: str, buffer: str) -> bool
```

Prove that every direct call initializes the buffer immediately before WRITE.

Observed calls (lexical order): `dict`, `re.compile`, `re.escape`, `_mask_quoted_literals`, `_mask_quoted_literals(body).upper`, `call.finditer`, `match.end`, `re.match`, `masked[:match.start()].rstrip`, `match.start`, `re.search`, `previous.group`, `_mask_quoted_literals(bodies[init_name]).upper`, `init.start`.

Control points:

- L123: `for (caller, body) in paragraphs`
- L125: `for match in call.finditer(masked)`
- L128: `if not re.match('\\s*\\.', masked[match.end():])`
- L132: `if not previous or previous.group(1) not in bodies`
- L135: `if init_name in {caller, write_paragraph}`
- L139: `if not init`
- L144: `if re.search('\\b(?:IF|EVALUATE|WHEN|PERFORM|CALL|READ|WRITE|EXEC|EXIT|GO|GOBACK|STOP)\\b', before)`

### `audit_record_population` - L149-L201

```python
audit_record_population(text: str) -> tuple[PopulationFinding, ...]
```

Raise a release blocker for provably unpopulated numeric record fields.

Observed calls (lexical order): `_paragraphs`, `text.splitlines`, `_mask_quoted_literals`, `_WRITE.finditer`, `(write.group(2) or write.group(1)).upper`, `write.group`, `extract_group`, `_leaves`, `PopulationFinding`, `findings.append`, `_written_targets_before`, `write.start`, `_proven_caller_initializers`, `initialized.add`, `Counter`, `any`.
Another 2 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L157: `for (paragraph_name, body) in paragraphs`
- L159: `for write in _WRITE.finditer(masked)`
- L167: `if not leaves`
- L170: `if _proven_caller_initializers(paragraphs, paragraph_name, buffer)`
- L192: `for (field, chain) in leaves`
- L193: `if any((ancestor in initialized for ancestor in chain))`
- L196: `if not proven`

## Change responsibility

After modifying this Python file, review [prompt/09_REVIEW_AND_RELEASE_GATES.md](../../../09_REVIEW_AND_RELEASE_GATES.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
