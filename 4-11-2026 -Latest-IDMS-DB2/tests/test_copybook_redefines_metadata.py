from converter.parsers.copybook_parser import CopybookParser
from converter.repositories.copybook_repository import CopybookRepository


def test_copybook_parser_retains_redefines_for_safe_group_width_resolution():
    fields = CopybookParser().parse(
        """
        01 OUT-REC.
           05 BASE-FIELD PIC 9(13).
           05 ALT-FIELD REDEFINES BASE-FIELD.
              10 ALT-PART PIC X(13).
        """
    )
    repository = CopybookRepository(fields)
    assert repository.redefines_for("ALT-FIELD") == "BASE-FIELD"
    assert repository.effective_picture_for("ALT-FIELD") == "9(13)"
    assert repository.group_width_for("ALT-FIELD") == 13
