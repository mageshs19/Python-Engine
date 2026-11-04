from __future__ import annotations

import pytest

from converter.services.db2_date_format_service import Db2DateFormatService
from rules.final_feedback_fix_rules import DEFAULT_DB2_DATE_EXTERNAL_FORMAT


@pytest.mark.parametrize(
    ("configured", "expected"),
    [
        ("ISO", "YYYY-MM-DD"),
        ("YYYY-MM-DD", "YYYY-MM-DD"),
        ("EUR", "DD.MM.YYYY"),
        ("EUROPEAN", "DD.MM.YYYY"),
        ("DD.MM.CCYY", "DD.MM.YYYY"),
        ("NUMERIC", "YYYYMMDD"),
        ("CCYYMMDD", "YYYYMMDD"),
    ],
)
def test_supported_formats_and_aliases_normalize(configured, expected):
    assert Db2DateFormatService(configured).date_external_format == expected


def test_blank_format_keeps_legacy_default():
    assert Db2DateFormatService("").date_external_format == DEFAULT_DB2_DATE_EXTERNAL_FORMAT
    assert Db2DateFormatService(None).date_external_format == DEFAULT_DB2_DATE_EXTERNAL_FORMAT


@pytest.mark.parametrize("configured", ["YYYY/MM/DD", "US", "DD-MM-YYYY", "UNKNOWN"])
def test_unsupported_explicit_format_fails_closed(configured):
    with pytest.raises(ValueError, match="Unsupported DB2 date external format"):
        Db2DateFormatService(configured)


def test_format_change_updates_helpers_and_sentinels_consistently():
    source = "MOVE DA-DD-MM-CCYY TO WS-DATE. IF WS-DATE = '01.01.0001' OR WS-DATE = '31.12.9999' CONTINUE."

    result = Db2DateFormatService("ISO").apply(source)

    assert "DA-YYYY-MM-DD" in result
    assert "'0001-01-01'" in result
    assert "'9999-12-31'" in result
    assert "DA-DD-MM-CCYY" not in result
