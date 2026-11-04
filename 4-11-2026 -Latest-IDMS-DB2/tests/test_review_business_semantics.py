from types import SimpleNamespace

from converter.domain.models import DclgenColumn, SheetMappingRow
from review.checks.chk_11_sqlcode_commit_conversion import SqlcodeCommitConversionCheck
from review.checks.chk_24_picture_and_length import PictureAndLengthCheck


def test_finish_without_database_update_does_not_imply_commit():
    source = "READY AREA USAGE-MODE IS RETRIEVAL.\nOBTAIN NEXT REC.\nFINISH."
    assert not SqlcodeCommitConversionCheck._source_requires_commit(source)


def test_finish_with_modify_requires_commit():
    source = "OBTAIN CALC REC.\nMODIFY REC.\nFINISH."
    assert SqlcodeCommitConversionCheck._source_requires_commit(source)


def test_explicit_source_commit_requires_commit():
    source = "OBTAIN NEXT REC.\nCOMMIT.\nFINISH."
    assert SqlcodeCommitConversionCheck._source_requires_commit(source)


def test_numeric_legacy_date_to_db2_date_host_is_representation_conversion():
    row = SheetMappingRow(
        cobol_record_idms="REC", cobol_zone="03 DA-BUSINESS",
        idms_pic_clause="PIC 9(8)", new_db2_record="DZTABTV",
        new_db2_field_name="DA_BUSINESS", new_db2_data_type="DATE",
    )
    col = DclgenColumn(
        table_name="DZTABTV", column_name="DA_BUSINESS", db2_type="DATE",
        cobol_host_name="DA-BUSINESS", cobol_picture="X(10)", nullable=False,
    )
    ctx = SimpleNamespace(sheet_mapping_rows=[row], dclgen_columns=[col])
    assert PictureAndLengthCheck._category_mismatches(ctx) == []


def test_numeric_to_character_non_temporal_still_fails_category_check():
    row = SheetMappingRow(
        cobol_record_idms="REC", cobol_zone="03 NR-CODE",
        idms_pic_clause="PIC 9(8)", new_db2_record="DZTABTV",
        new_db2_field_name="NR_CODE", new_db2_data_type="CHAR(8)",
    )
    col = DclgenColumn(
        table_name="DZTABTV", column_name="NR_CODE", db2_type="CHAR(8)",
        cobol_host_name="NR-CODE", cobol_picture="X(8)", nullable=False,
    )
    ctx = SimpleNamespace(sheet_mapping_rows=[row], dclgen_columns=[col])
    assert PictureAndLengthCheck._category_mismatches(ctx) == [
        "DZTABTV.NR_CODE: NUMERIC to ALPHANUMERIC"
    ]
