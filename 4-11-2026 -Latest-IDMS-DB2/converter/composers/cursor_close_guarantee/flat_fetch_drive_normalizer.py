"""Normalize a proven split COBOL cursor loop to one FETCH-driven loop.

Do not infer business semantics from paragraph names.  The rewrite requires:
 * an already-opened cursor and a single initial FETCH in a performed setup;
 * a mainline THRU business loop ending on that cursor's EOC;
 * a single final FETCH in the business paragraph;
 * SQLCODE 0/100 handling with a passive CONTINUE success branch; and
 * exactly these two FETCH call sites in the entire procedure.

The original sequence (prime; do business until EOC; tail FETCH) is equal to
(FETCH until EOC; on SQLCODE 0 do business), including the empty set.  The
rewrite changes no SQL, row predicates, counters, or business statements.
Anything ambiguous is returned verbatim; the final layout phase owns geometry.
"""
from __future__ import annotations

import re

from converter.composers.cursor_close_guarantee.nested_parent_fetch_normalizer import _body

_NAME = r"[A-Z0-9][A-Z0-9-]*"
_PARA = re.compile(rf"^({_NAME})\.$", re.I)
_FETCH_NAME = re.compile(rf"^\d+-FETCH-({_NAME})$", re.I)
_SETUP_CALL = re.compile(rf"^PERFORM\s+({_NAME})\s+THRU\s+({_NAME})\.$", re.I)
_DRIVER = re.compile(rf"^PERFORM\s+({_NAME})\s+THRU\s+({_NAME})(?:\s+UNTIL\s+({_NAME})-EOC)?\.?$", re.I)


def _replace(line: str, logical: str) -> str:
    """Rebuild all 80 columns, not just the new executable body.

    The previous implementation produced `old-seq  new-seq  PERFORM...`
    after a later resequencer.  Fixed-format ownership requires keeping the
    original indicator and right identification area in their own columns.
    The rewrite refuses a line that cannot fit rather than truncating COBOL.
    """
    body = "    " + logical
    if len(body) > 65:
        raise ValueError("cursor rewrite would overflow the fixed-format body")
    if len(line) >= 7 and line[:6].isdigit():
        suffix = line[72:80] if len(line) >= 80 else "00000000"
        return f"{line[:7]}{body:<65}{suffix}"
    return "       " + body


class FlatFetchDriveNormalizer:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def apply(self, text: str) -> str:
        self.messages = []
        lines = str(text).splitlines()
        bodies = [_body(line).upper() for line in lines]
        proc = next((i for i, item in enumerate(bodies) if item.startswith("PROCEDURE DIVISION")), -1)
        if proc < 0:
            return text
        headers = []
        for i in range(proc + 1, len(lines)):
            matched = _PARA.fullmatch(bodies[i])
            line = lines[i]
            if not matched or matched.group(1) in {"EXIT", "GOBACK", "CONTINUE", "END-EXEC"}:
                continue
            # COBOL paragraph labels occupy Area A, never an Area B operand.
            if len(line) >= 7 and line[:6].isdigit():
                area_a = len(line) > 7 and line[7] != " "
            else:
                area_a = len(line) - len(line.lstrip()) <= 7
            if area_a:
                headers.append((matched.group(1), i))
        if not headers:
            return text
        spans = {
            name: (start, headers[j + 1][1] if j + 1 < len(headers) else len(lines))
            for j, (name, start) in enumerate(headers)
        }
        main_end = headers[0][1]
        main = bodies[proc + 1:main_end]
        for fetch in spans:
            cm = _FETCH_NAME.fullmatch(fetch)
            if not cm:
                continue
            cursor = cm.group(1)
            fs, fe = spans[fetch]
            zero = [i for i in range(fs + 1, fe) if bodies[i] in {"WHEN ZERO", "WHEN 0"}]
            hundred = [i for i in range(fs + 1, fe) if bodies[i] == "WHEN 100"]
            if len(zero) != 1 or len(hundred) != 1 or zero[0] >= hundred[0]:
                continue
            zero_body = [i for i in range(zero[0] + 1, hundred[0]) if bodies[i]]
            placeholders = [i for i in zero_body if bodies[i] == "CONTINUE"]
            if len(placeholders) != 1:
                continue
            # Only the one success-branch CONTINUE and ordinary counter ADDs
            # may already be present; a CALL or PERFORM would change the CFG.
            if any(not (bodies[i] == "CONTINUE" or re.fullmatch(r"ADD\s+\d+\s+TO\s+" + _NAME, bodies[i])) for i in zero_body):
                continue
            if not any(re.fullmatch(rf"SET\s+{re.escape(cursor)}-EOC\s+TO\s+TRUE\.?", bodies[i]) for i in range(hundred[0] + 1, fe)):
                continue
            # All FETCH invocation edges in the procedure must be the initial
            # priming and the terminal advance, with no named helper calls.
            calls = [i for i in range(proc + 1, len(lines)) if bodies[i].rstrip(".") == f"PERFORM {fetch}"]
            if len(calls) != 2:
                continue
            # A single mainline business THRU loop directly followed by CLOSE.
            drivers = []
            for i in range(proc + 1, main_end):
                match = _DRIVER.fullmatch(bodies[i])
                if match and match.group(1) in spans and match.group(2) in spans:
                    if match.group(3) == cursor:
                        drivers.append((i, i, match.group(1), match.group(2)))
                    elif match.group(3) is None:
                        following = next((j for j in range(i + 1, main_end) if bodies[j]), -1)
                        if following >= 0 and bodies[following].rstrip(".") == f"UNTIL {cursor}-EOC":
                            drivers.append((i, following, match.group(1), match.group(2)))
            if len(drivers) != 1:
                continue
            driver_start, driver_end, work, work_exit = drivers[0]
            bs, be = spans[work]
            es, ee = spans[work_exit]
            if not (bs < be <= es < ee):
                continue
            if headers[[n for n, _ in headers].index(work) + 1][0] != work_exit:
                continue
            # The business paragraph ends with the single advance, and its
            # exit paragraph contains only EXIT and optional DISPLAYs.
            tail = [i for i in calls if bs < i < be]
            if len(tail) != 1 or any(bodies[j] for j in range(tail[0] + 1, be)):
                continue
            if any(bodies[j] and not (bodies[j] == "EXIT." or bodies[j].startswith("DISPLAY ")) for j in range(es + 1, ee)):
                continue
            # Prime must be in exactly one setup paragraph performed THRU its
            # own exit from mainline; cursor OPEN must occur before prime.
            prime = [i for i in calls if i != tail[0]]
            if len(prime) != 1:
                continue
            setup_matches = []
            for name, (start, end) in spans.items():
                if start < prime[0] < end and name != work and name != fetch:
                    setup_matches.append((name, start, end))
            if len(setup_matches) != 1:
                continue
            setup, ss, se = setup_matches[0]
            if any(bodies[j] for j in range(prime[0] + 1, se)):
                continue
            setups = [(i, m.group(2)) for i in range(proc + 1, main_end)
                      if (m := _SETUP_CALL.fullmatch(bodies[i])) and m.group(1) == setup]
            if len(setups) != 1 or setups[0][0] >= driver_start:
                continue
            setup_exit = setups[0][1]
            if setup_exit not in spans:
                continue
            # The setup must be invoked exactly once by the mainline.
            # Otherwise removing its initial FETCH could affect a second
            # entry path that does not go through this mainline's driver.
            if sum(bool(re.match(rf"^PERFORM\s+{re.escape(setup)}(?:\s|\.)", b))
                   for b in bodies[proc + 1:]) != 1:
                continue
            # The initialization path owns the cursor OPEN before the prime.
            opens = [i for i in range(ss + 1, prime[0])
                     if re.fullmatch(rf"PERFORM\s+\d+-OPEN-{re.escape(cursor)}\.?", bodies[i])]
            if len(opens) != 1:
                continue
            closes = [i for i in range(driver_end + 1, main_end)
                      if re.fullmatch(rf"PERFORM\s+\d+-CLOSE-{re.escape(cursor)}\.?", bodies[i])]
            if len(closes) != 1:
                continue
            if any(bodies[i] for i in range(driver_end + 1, closes[0])):
                continue
            # Refuse other direct invocations of the business range.
            if sum(bool(re.match(rf"^PERFORM\s+{re.escape(work)}(?:\s|\.)", b))
                   for b in bodies[proc + 1:]) != 1:
                continue
            if any(re.search(rf"\bPERFORM\s+{re.escape(work_exit)}\b", b)
                   for b in bodies[proc + 1:]):
                continue
            updated = list(lines)
            updated[driver_start] = _replace(lines[driver_start], f"PERFORM {fetch} UNTIL {cursor}-EOC.")
            updated[placeholders[0]] = _replace(lines[placeholders[0]], f"PERFORM {work} THRU {work_exit}")
            for i in sorted(set(range(driver_start + 1, driver_end + 1)) | {prime[0], tail[0]}, reverse=True):
                del updated[i]
            self.messages.append(
                f"Cursor {cursor}: proved initial FETCH + terminal FETCH split loop; "
                f"now one FETCH-driven call site and one successful-row business edge."
            )
            return "\n".join(updated).rstrip() + "\n"
        return text


__all__ = ["FlatFetchDriveNormalizer"]
