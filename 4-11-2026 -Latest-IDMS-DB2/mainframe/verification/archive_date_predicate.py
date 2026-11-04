"""Restricted parity model for IDMS numeric dates and DB2 DATE fields.

This models an *already identified* archive-date condition; it does NOT
rewrite SQL or prove real DB2 host binding, collation, or job execution.
Only valid DB2 dates, non-null inputs, and valid archive cutoff dates qualify.
"""
from __future__ import annotations

from datetime import date

ZERO_SENTINEL = date(1, 1, 1)
HIGH_SENTINEL = date(9999, 12, 31)


def cobol_numeric_date(value: date) -> int:
    """Result of the generator's 01.01.0001/31.12.9999 realignment."""
    if not isinstance(value, date):
        raise ValueError('DB2 DATE must be non-null and valid')
    if value == ZERO_SENTINEL:
        return 0
    if value == HIGH_SENTINEL:
        return 99999999
    return value.year * 10000 + value.month * 100 + value.day


def original_archive_decision(capitalized: date, created: date, cutoff: date) -> bool:
    """Original COBOL rule, after DATE sentinel mapping into packed YYYYMMDD."""
    cap = cobol_numeric_date(capitalized)
    cr = cobol_numeric_date(created)
    threshold = _cutoff(cutoff)
    return ((cap < threshold and cap != 0) or
            (cr < threshold and cap == 0))


def manual_sql_date_decision(capitalized: date, created: date, cutoff: date) -> bool:
    """Manual DB2 WHERE rule interpreted as typed DATE (not raw host text)."""
    _cutoff(cutoff)
    if not isinstance(capitalized, date) or not isinstance(created, date):
        raise ValueError('DATE columns must be non-null and valid')
    return ((capitalized < cutoff and capitalized != ZERO_SENTINEL) or
            (created < cutoff and capitalized == ZERO_SENTINEL))


def _cutoff(value: date) -> int:
    if not isinstance(value, date):
        raise ValueError('archive cutoff must be a valid date')
    return value.year * 10000 + value.month * 100 + value.day
