"""Conservatively make nested parent cursors FETCH-driven.

The normalizer is independent of program names, paragraph numbering and child
flag naming. It recognizes a proven parent mainline pattern:

    OPEN(parent); FETCH(parent); PERFORM business UNTIL parent-EOC; CLOSE(parent)
    business: OPEN(child); FETCH(child) UNTIL ...; CLOSE(child); FETCH(parent)
    parent FETCH WHEN ZERO: ... CONTINUE

It turns the redundant outside business loop into one FETCH-driven loop,
with business processing on SQLCODE=0. Both drivers must never coexist.
If any edge is ambiguous, it makes no changes rather than guessing.
The final fixed-format renderer alone owns sequence numbers and layout.
"""
from __future__ import annotations

import re

_NAME = r"[A-Z0-9][A-Z0-9-]*"
_HEADER = re.compile(rf"^(?P<name>{_NAME})\.$", re.I)
_FETCH = re.compile(rf"^(?P<name>\d+-FETCH-(?P<cursor>{_NAME}))\.$", re.I)
_PROCEDURE = re.compile(r"^PROCEDURE\s+DIVISION\b", re.I)
_PERFORM = re.compile(rf"^PERFORM\s+(?P<name>{_NAME})\b", re.I)


def _body(line: str) -> str:
    text = str(line).rstrip("\r\n")
    if len(text) >= 7 and text[:6].isdigit():
        if text[6] in "*/Dd-":
            return ""
        return text[7:72].strip()
    if text.lstrip().startswith("*"):
        return ""
    return text.strip()


def _as_intermediate(body: str) -> str:
    # Semantic-only edit. FinalGeneratedOutputService performs fixed formatting.
    return "    " + body


class NestedParentFetchNormalizer:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def apply(self, text: str) -> str:
        self.messages = []
        lines = text.splitlines()
        bodies = [_body(x).upper() for x in lines]
        procedure = next((i for i, b in enumerate(bodies) if _PROCEDURE.match(b)), -1)
        if procedure < 0:
            return text
        headers: list[tuple[str, int]] = []
        # Avoid interpreting DATA declarations / SQL END-EXEC as paragraphs.
        for i in range(procedure + 1, len(lines)):
            m = _HEADER.fullmatch(bodies[i])
            # A COBOL paragraph label starts in Area A, unlike a final
            # operand or scope terminator ending in a period in Area B.
            raw = lines[i]
            area_a = (len(raw) >= 8 and raw[:6].isdigit() and raw[7] != " ") or (not raw[:6].isdigit() and len(raw) - len(raw.lstrip()) <= 7)
            if m and area_a and not bodies[i].startswith(("END-", "STOP ")):
                headers.append((m.group("name"), i))
        if not headers:
            return text
        starts = {name: i for name, i in headers}
        spans = {
            name: (start, headers[pos + 1][1] if pos + 1 < len(headers) else len(lines))
            for pos, (name, start) in enumerate(headers)
        }
        main_end = headers[0][1]

        for fetch, fetch_start in headers:
            m = _FETCH.fullmatch(fetch + ".")
            if not m:
                continue
            cursor = m.group("cursor")
            fs, fe = spans[fetch]
            # Need a successful-row CONTINUE and an EOC branch in the same FETCH.
            zero_at = next((i for i in range(fs + 1, fe) if bodies[i] == "WHEN ZERO"), -1)
            end_zero = next((i for i in range(zero_at + 1, fe)
                             if bodies[i].startswith(("WHEN ", "END-EVALUATE"))), -1) if zero_at >= 0 else -1
            if end_zero < 0 or not any(bodies[i] == "CONTINUE" for i in range(zero_at + 1, end_zero)):
                continue
            if not any(bodies[i].startswith("WHEN 100") for i in range(end_zero, fe)):
                continue
            # Prove one OPEN, one priming FETCH, one loop and one CLOSE in mainline.
            open_name = next((name for name in starts if re.fullmatch(rf"\d+-OPEN-{re.escape(cursor)}", name)), "")
            close_name = next((name for name in starts if re.fullmatch(rf"\d+-CLOSE-{re.escape(cursor)}", name)), "")
            if not open_name or not close_name:
                continue
            opens = [i for i in range(procedure + 1, main_end) if bodies[i] == f"PERFORM {open_name}" or bodies[i] == f"PERFORM {open_name}."]
            primes = [i for i in range(procedure + 1, main_end) if bodies[i].rstrip(".") == f"PERFORM {fetch}"]
            closes = [i for i in range(procedure + 1, main_end) if bodies[i].rstrip(".") == f"PERFORM {close_name}"]
            if len(opens) != 1 or len(primes) != 1 or len(closes) != 1 or not (opens[0] < primes[0] < closes[0]):
                continue
            prime = primes[0]
            # Look for an explicit single-paragraph driver with this exact parent EOC.
            drivers: list[tuple[int, int, str]] = []
            for i in range(prime + 1, closes[0]):
                mm = re.fullmatch(rf"PERFORM\s+({_NAME})\s+UNTIL\s+{re.escape(cursor)}-EOC\.?", bodies[i])
                if mm:
                    drivers.append((i, i, mm.group(1)))
                elif re.fullmatch(rf"PERFORM\s+({_NAME})", bodies[i]):
                    following = next((j for j in range(i + 1, closes[0]) if bodies[j]), -1)
                    if following >= 0 and re.fullmatch(rf"UNTIL\s+{re.escape(cursor)}-EOC\.?", bodies[following]):
                        drivers.append((i, following, bodies[i].split()[1]))
            if len(drivers) != 1:
                continue
            driver_start, driver_end, business = drivers[0]
            if business not in spans or not (prime < driver_start <= driver_end < closes[0]):
                continue
            # Only comments or blanks may separate these two mainline actions.
            if any(bodies[i] for i in range(prime + 1, driver_start)):
                continue
            bs, be = spans[business]
            tail = [i for i in range(bs + 1, be) if bodies[i].rstrip(".") == f"PERFORM {fetch}"]
            if len(tail) != 1:
                continue
            # The parent next-FETCH must be the last executable statement in
            # the business paragraph, and the body must own a separate child
            # cursor lifecycle. Otherwise no semantic equivalence is proven.
            if any(bodies[i] for i in range(tail[0] + 1, be)):
                continue
            child_opens = [b for b in bodies[bs + 1:be] if re.fullmatch(r"PERFORM \d+-OPEN-[A-Z0-9-]+\.?", b)]
            child_closes = [b for b in bodies[bs + 1:be] if re.fullmatch(r"PERFORM \d+-CLOSE-[A-Z0-9-]+\.?", b)]
            if not child_opens or not child_closes:
                continue
            child_cursor_names = {re.search(r"-OPEN-(.+?)(?:\.)?$", x).group(1) for x in child_opens}
            if cursor in child_cursor_names or not any(any(c in x for c in child_cursor_names) for x in child_closes):
                continue
            # Verify there is no existing FETCH -> business edge or another
            # parent FETCH call elsewhere that would make a double driver.
            if any(bodies[i] == f"PERFORM {business}" for i in range(zero_at + 1, end_zero)):
                continue
            calls = [i for i in range(procedure + 1, len(lines))
                     if bodies[i].rstrip(".") == f"PERFORM {fetch}"]
            if sorted(calls) != sorted((prime, tail[0])):
                continue
            placeholder = next(i for i in range(zero_at + 1, end_zero) if bodies[i] == "CONTINUE")
            # One atomic edit. Replacements use original indices; deletions
            # applied backwards, and no fallback edit is ever attempted.
            new = list(lines)
            new[prime] = _as_intermediate(f"PERFORM {fetch} UNTIL {cursor}-EOC.")
            new[placeholder] = _as_intermediate(f"PERFORM {business}")
            new[closes[0]] = _as_intermediate(f"PERFORM {close_name}.")
            for i in sorted(set(range(driver_start, driver_end + 1)) | {tail[0]}, reverse=True):
                del new[i]
            self.messages.append(
                f"Nested parent cursor {cursor}: normalized to one FETCH-driven "
                f"business edge ({fetch} -> {business}); removed redundant tail FETCH."
            )
            return "\n".join(new).rstrip() + "\n"
        return text
