# `converter/composers/procedure_indent/indent_resolver.py`

Source: [converter/composers/procedure_indent/indent_resolver.py](../../../../../converter/composers/procedure_indent/indent_resolver.py) | 134 lines.
Owning logic guide: [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md).
Source SHA-256: `b379a86dfa57ad3c52cf67093b5f593ec267fa131f448c8d36ba5b328dc1e438`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Decides the body indent for one PROCEDURE DIVISION line.

## Module-level bindings

`__all__` (L134)

## Import declarations

```python
from __future__ import annotations
from patterns.procedure_indent_patterns import ELSE_PATTERN, END_EXEC_PATTERN, EVALUATE_START_PATTERN, EXEC_SQL_START_PATTERN, IF_START_PATTERN, INLINE_PERFORM_PATTERN, LONE_PERIOD_PATTERN, SCOPE_TERMINATOR_PATTERN, SCOPED_OPENER_PATTERN, WHEN_PATTERN
from rules.procedure_indent_rules import AREA_B_INDENT, BLOCK_KIND_EVALUATE, BLOCK_KIND_IF, BLOCK_KIND_OTHER, BLOCK_KIND_PERFORM, BLOCK_KIND_SQL, LONE_PERIOD_INDENT, PRESERVE_INDENT, PRESERVE_SQL_BODY_INDENT, SCOPE_TERMINATORS, WHEN_OFFSET
from converter.composers.procedure_indent.indent_models import FrameStack, LineClassifier
```

## Local dependency notes

- [converter/composers/procedure_indent/indent_models.py](indent_models.md)
- [patterns/procedure_indent_patterns.py](../../../patterns/procedure_indent_patterns.md)
- [rules/procedure_indent_rules.py](../../../rules/procedure_indent_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/procedure_indent_normalizer.py](../procedure_indent_normalizer.md)

## Symbol contracts and control points

### `IndentResolver` - L59-L131

```python
class IndentResolver()
```

Body indent for one line, given the open blocks.

### `IndentResolver.__init__` - L62-L63

```python
__init__(self, classifier: LineClassifier) -> None
```

### `IndentResolver.resolve` - L65-L131

```python
resolve(self, upper: str, stack: FrameStack) -> int
```

Indent for this line. Mutates `stack` as blocks open/close.

Observed calls (lexical order): `END_EXEC_PATTERN.match`, `stack.pop`, `SCOPE_TERMINATOR_PATTERN.match`, `terminator.group`, `terminator.group('token').upper`, `SCOPE_TERMINATORS.get`, `LONE_PERIOD_PATTERN.match`, `stack.clear`, `ELSE_PATTERN.match`, `stack.peek`, `WHEN_PATTERN.match`, `EXEC_SQL_START_PATTERN.match`, `stack.push`, `EVALUATE_START_PATTERN.match`, `IF_START_PATTERN.match`, `self.classifier.is_self_closing`.
Another 3 call expressions are in this source span; the list is intentionally bounded.

Control points:

- L71: `if END_EXEC_PATTERN.match(upper)`
- L76: `if top is not None and top.kind == BLOCK_KIND_SQL`
- L77: `if PRESERVE_SQL_BODY_INDENT`
- L83: `if terminator`
- L90: `if LONE_PERIOD_PATTERN.match(upper)`
- L95: `if ELSE_PATTERN.match(upper)`
- L100: `if WHEN_PATTERN.match(upper)`
- L102: `if frame`
- Another 8 conditions/loops exist in this source span.

## Change responsibility

After modifying this Python file, review [prompt/08_POSTPROCESS_FORMATTING_NUMBERING.md](../../../../08_POSTPROCESS_FORMATTING_NUMBERING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
