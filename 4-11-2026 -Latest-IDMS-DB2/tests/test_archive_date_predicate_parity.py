"""The rule's typed-date domain is only part of mainframe parity proof."""
from datetime import date, timedelta
from random import Random

import pytest

from mainframe.verification.archive_date_predicate import (
    original_archive_decision, manual_sql_date_decision, ZERO_SENTINEL,
    HIGH_SENTINEL,
)


def _equal(cap, cr, cutoff):
    assert original_archive_decision(cap, cr, cutoff) == manual_sql_date_decision(cap, cr, cutoff)


@pytest.mark.parametrize('cap,cr,cutoff', [
    (date(2002, 1, 1), date(2003, 1, 1), date(2004, 1, 1)),
    (date(2004, 1, 1), date(2003, 1, 1), date(2004, 1, 1)),
    (date(2005, 1, 1), date(2003, 1, 1), date(2004, 1, 1)),
    (ZERO_SENTINEL, date(2003, 1, 1), date(2004, 1, 1)),
    (ZERO_SENTINEL, date(2004, 1, 1), date(2004, 1, 1)),
    (HIGH_SENTINEL, date(2003, 1, 1), date(2004, 1, 1)),
    (date(2004, 1, 1), HIGH_SENTINEL, date(2004, 1, 1)),
    (ZERO_SENTINEL, ZERO_SENTINEL, date(2004, 1, 1)),
])
def test_valid_db2_date_domain_matches(cap, cr, cutoff):
    _equal(cap, cr, cutoff)


def test_seeded_dates_around_cutoff_and_cross_year():
    rand = Random(1200)
    base = date(2020, 1, 1)
    for _ in range(3000):
        cutoff = base + timedelta(days=rand.randrange(-6000, 6000))
        cap = cutoff + timedelta(days=rand.randrange(-1500, 1500))
        cr = cutoff + timedelta(days=rand.randrange(-1500, 1500))
        _equal(cap, cr, cutoff)


def test_reject_nulls_as_unproven_db2_semantics():
    with pytest.raises(ValueError):
        original_archive_decision(None, date(2000, 1, 1), date(2020, 1, 1))
    with pytest.raises(ValueError):
        manual_sql_date_decision(date(2000, 1, 1), None, date(2020, 1, 1))
    with pytest.raises(ValueError):
        original_archive_decision(date(2000, 1, 1), date(2000, 1, 1), None)
