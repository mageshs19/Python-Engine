# `converter/ui/message_classifier.py`

Source: [converter/ui/message_classifier.py](../../../../converter/ui/message_classifier.py) | 177 lines.
Owning logic guide: [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md).
Source SHA-256: `b04555db270e321f855365cd75fd68115a9faab0146becdb48490e9ea5bd3bd1`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Classifies pipeline messages into severity and category.

## Import declarations

```python
from __future__ import annotations
from dataclasses import dataclass
from rules.validation_display_rules import CATEGORY_SEPARATOR, ERROR_KEYWORDS, ERROR_PREFIXES, FALLBACK_CATEGORY, INFO_PREFIXES, MAX_CATEGORY_WORDS, SEVERITY_ERROR, SEVERITY_INFO, SEVERITY_ORDER, SEVERITY_WARNING, WARNING_KEYWORDS, WARNING_PREFIXES
```

## Local dependency notes

- [rules/validation_display_rules.py](../../rules/validation_display_rules.md)

## Importers (1)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/ui/output_tabs.py](output_tabs.md)

## Symbol contracts and control points

### `ClassifiedMessage` - L46-L55

```python
class ClassifiedMessage()
```

One pipeline message with its severity and category.

Declared class/data-model fields:

```python
text: str
severity: str
category: str
```

### `ClassifiedMessage.is_actionable` - L54-L55

```python
is_actionable(self) -> bool
```

### `MessageClassifier` - L58-L177

```python
class MessageClassifier()
```

Assigns a severity and a category to a pipeline message.

### `MessageClassifier.classify` - L64-L80

```python
classify(self, message: str) -> ClassifiedMessage
```

Observed calls (lexical order): `' '.join`, `str`, `str(message or '').split`, `ClassifiedMessage`, `self._prefix`, `self._severity_from_prefix`, `self._severity_from_keywords`, `self._category`.

Control points:

- L67: `if not text`
- L73: `if severity is None`

### `MessageClassifier.classify_all` - L82-L94

```python
classify_all(self, messages: list[str]) -> list[ClassifiedMessage]
```

Classify a list, de-duplicated, severity-ordered.

Observed calls (lexical order): `set`, `self.classify`, `seen.add`, `out.append`, `self.sort`.

Control points:

- L87: `for message in messages or []`
- L89: `if not item.text or item.text in seen`

### `MessageClassifier.sort` - L97-L103

```python
sort(items: list[ClassifiedMessage]) -> list[ClassifiedMessage]
```

Errors first, then warnings, then info. Stable within a band.

Observed calls (lexical order): `enumerate`, `sorted`, `len`, `rank.get`.

### `MessageClassifier.counts` - L106-L111

```python
counts(items: list[ClassifiedMessage]) -> dict[str, int]
```

Control points:

- L108: `for item in items`
- L109: `if item.severity in result`

### `MessageClassifier.categories` - L114-L115

```python
categories(items: list[ClassifiedMessage]) -> list[str]
```

Observed calls (lexical order): `sorted`.

### `MessageClassifier.of_severity` - L118-L122

```python
of_severity(items: list[ClassifiedMessage], severity: str) -> list[ClassifiedMessage]
```

### `MessageClassifier._prefix` - L128-L141

```python
_prefix(text: str) -> str
```

Text before the first colon, when it reads like a source name.

Observed calls (lexical order): `text.split`, `text.split(CATEGORY_SEPARATOR, 1)[0].strip`, `candidate.split`, `len`.

Control points:

- L134: `if CATEGORY_SEPARATOR not in text`
- L138: `if not candidate or len(candidate.split()) > MAX_CATEGORY_WORDS`

### `MessageClassifier._severity_from_prefix` - L144-L159

```python
_severity_from_prefix(prefix: str) -> str | None
```

Observed calls (lexical order): `prefix.lower`, `lowered.startswith`.

Control points:

- L145: `if not prefix`
- L150: `if lowered.startswith(ERROR_PREFIXES)`
- L153: `if lowered.startswith(WARNING_PREFIXES)`
- L156: `if lowered.startswith(INFO_PREFIXES)`

### `MessageClassifier._severity_from_keywords` - L162-L171

```python
_severity_from_keywords(text: str) -> str
```

Observed calls (lexical order): `text.lower`, `any`.

Control points:

- L165: `if any((keyword in lowered for keyword in ERROR_KEYWORDS))`
- L168: `if any((keyword in lowered for keyword in WARNING_KEYWORDS))`

### `MessageClassifier._category` - L174-L177

```python
_category(prefix: str) -> str
```

Observed calls (lexical order): `prefix[:1].upper`.

Control points:

- L175: `if not prefix`

## Change responsibility

After modifying this Python file, review [prompt/15_UI_AND_LOGGING.md](../../../15_UI_AND_LOGGING.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
