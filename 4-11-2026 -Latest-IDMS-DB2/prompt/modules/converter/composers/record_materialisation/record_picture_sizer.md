# `converter/composers/record_materialisation/record_picture_sizer.py`

Source: [converter/composers/record_materialisation/record_picture_sizer.py](../../../../../converter/composers/record_materialisation/record_picture_sizer.py) | 313 lines.
Owning logic guide: [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md).
Source SHA-256: `435e16c86bba0218cbf00647a22870b09d947329818b4363e6e05af8096bc3f7`.

Generated source map. Read this file to locate the relevant symbols, then inspect the touched source before changing behavior. Lexical calls/branches are not a proof of runtime wiring or semantic equivalence.

## Responsibility

Source-declared description (not an independently verified runtime claim):

> Sizes a COBOL PICTURE clause in stored bytes.

## Module-level bindings

`COUNTED_SYMBOLS` (L38), `COMP_3_SYMBOLS` (L41), `COMP_3_SYMBOL` (L42), `PIC_KEYWORDS` (L45), `STOP_WORDS` (L53), `NAME_CHARACTERS` (L84), `PICTURE_GROUP` (L88), `OPEN_PAREN` (L89), `CLOSE_PAREN` (L90), `PERIOD` (L91), `__all__` (L313)

## Import declarations

```python
from __future__ import annotations
```

## Importers (2)

Static imports only; dependency injection, string imports and runtime dispatch can add edges.

- [converter/composers/record_materialisation/record_move_scanner.py](record_move_scanner.md)
- [tests/test_record_picture_sizer.py](../../../tests/test_record_picture_sizer.md)

## Symbol contracts and control points

### `RecordPictureSizer` - L94-L310

```python
class RecordPictureSizer()
```

Measures a PICTURE clause, never under-reporting.

### `RecordPictureSizer.declared_bytes` - L101-L121

```python
declared_bytes(cls, body: str, match=None) -> int
```

Stored byte count of one data description entry.

Observed calls (lexical order): `str`, `cls.is_comp_3`, `cls.size_of`, `cls.candidates`, `max`.

### `RecordPictureSizer.size_of` - L124-L159

```python
size_of(cls, picture: str, usage: str='') -> int
```

Character positions of a PICTURE, honouring repeat counts.

Observed calls (lexical order): `str`, `str(picture or '').upper`, `len`, `cls._repeat_at`, `cls.is_comp_3`.

Control points:

- L137: `if not text`
- L144: `while index < length`
- L145: `if text[index] not in COUNTED_SYMBOLS`
- L153: `if not digits`
- L156: `if cls.is_comp_3(usage) or cls.is_comp_3(text)`

### `RecordPictureSizer.picture_bytes` - L162-L164

```python
picture_bytes(cls, picture: str) -> int
```

Back-compatible entry point for callers that pass a clause.

Observed calls (lexical order): `cls.size_of`.

### `RecordPictureSizer.candidates` - L170-L186

```python
candidates(cls, body: str, match=None) -> list[str]
```

Every readable form of this entry's PICTURE, unordered.

Observed calls (lexical order): `cls._group`, `out.append`, `cls.clause_of`, `cls._has_pic_keyword`, `str`.

Control points:

- L175: `if captured`
- L179: `if clause`
- L183: `if not clause and body and (not cls._has_pic_keyword(str(body)))`

### `RecordPictureSizer.clause_of` - L189-L223

```python
clause_of(cls, body: str) -> str
```

The PICTURE clause of a data description line, bounded.

Observed calls (lexical order): `str`, `text.upper`, `cls._find_word`, `len`, `text[start + keyword_length:].split`, `tokens[0].upper`, `token.upper`, `token.upper().strip`, `kept.append`, `' '.join`, `' '.join(kept).strip`, `' '.join(kept).strip().rstrip`.

Control points:

- L200: `for keyword in PIC_KEYWORDS`
- L203: `if position >= 0`
- L208: `if start < 0`
- L213: `if tokens and tokens[0].upper() == 'IS'`
- L218: `for token in tokens`
- L219: `if token.upper().strip(PERIOD) in STOP_WORDS`

### `RecordPictureSizer.is_comp_3` - L226-L228

```python
is_comp_3(text: str) -> bool
```

Observed calls (lexical order): `str`, `str(text or '').upper`, `any`.

### `RecordPictureSizer._repeat_at` - L234-L267

```python
_repeat_at(text: str, index: int) -> tuple[int, int]
```

Read an optional '( n )' starting at `index`.

Observed calls (lexical order): `len`, `text[cursor].isspace`, `text[cursor].isdigit`, `int`.

Control points:

- L244: `while cursor < length and text[cursor].isspace()`
- L247: `if cursor >= length or text[cursor] != OPEN_PAREN`
- L252: `while cursor < length and text[cursor].isspace()`
- L257: `while cursor < length and text[cursor].isdigit()`
- L261: `while cursor < length and text[cursor].isspace()`
- L264: `if cursor >= length or text[cursor] != CLOSE_PAREN or (not digits)`

### `RecordPictureSizer._find_word` - L270-L293

```python
_find_word(upper: str, word: str) -> int
```

Index of `word` in `upper` when it stands as a whole token.

Observed calls (lexical order): `upper.find`, `len`.

Control points:

- L274: `while True`
- L277: `if position < 0`
- L290: `if before_ok and after_ok`

### `RecordPictureSizer._has_pic_keyword` - L296-L300

```python
_has_pic_keyword(cls, body: str) -> bool
```

Observed calls (lexical order): `str`, `str(body or '').upper`, `any`, `cls._find_word`.

### `RecordPictureSizer._group` - L303-L310

```python
_group(match, name: str) -> str
```

Observed calls (lexical order): `match.group`, `str`, `str(match.group(name) or '').strip`.

Control points:

- L304: `if match is None`

## Change responsibility

After modifying this Python file, review [prompt/06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md](../../../../06_RECORD_COPYBOOK_AND_DATE_CONTRACTS.md), update any affected behavioral contracts, then run `python prompt/tools/maintain_docs.py refresh` and `python prompt/tools/maintain_docs.py check` from the repository root. Keep scratch Markdown only in `prompt/temp/`. Generated notes must not be hand-edited; add explanations to the owning guide.
