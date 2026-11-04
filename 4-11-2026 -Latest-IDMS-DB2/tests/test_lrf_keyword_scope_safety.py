"""A path keyword must never resolve against a different logical record."""
from converter.domain.models import LogicalRecord, LrfPath
from converter.repositories.lrf_repository import LrfRepository
from converter.resolvers.lrf_path_resolver import LrfPathResolver


def _record(lr_name: str, keyword: str, driving: str) -> LogicalRecord:
    from converter.domain.models import LrfPathCommand

    return LogicalRecord(
        logical_record_name=lr_name,
        element_records=[driving],
        paths=[LrfPath(
            keyword=keyword,
            path_group_verb="OBTAIN",
            logical_record=lr_name,
            commands=[LrfPathCommand(
                verb="OBTAIN", scope="EACH", record_name=driving,
                within_name=f"SET-{driving}",
            )],
        )],
    )


def test_duplicate_keyword_resolves_using_explicit_logical_record_scope():
    repo = LrfRepository([
        _record("LR-ONE", "BY-KEY", "RECORD-ONE"),
        _record("LR-TWO", "BY-KEY", "RECORD-TWO"),
    ])

    first = repo.path_for_keyword("BY-KEY", "LR-ONE")
    second = repo.path_for_keyword("BY-KEY", "LR-TWO")

    assert first is not None and first.logical_record == "LR-ONE"
    assert first.commands[-1].record_name == "RECORD-ONE"
    assert second is not None and second.logical_record == "LR-TWO"
    assert second.commands[-1].record_name == "RECORD-TWO"


def test_duplicate_keyword_without_scope_is_refused_as_ambiguous():
    repo = LrfRepository([
        _record("LR-ONE", "BY-KEY", "RECORD-ONE"),
        _record("LR-TWO", "BY-KEY", "RECORD-TWO"),
    ])

    assert repo.path_for_keyword("BY-KEY") is None
    assert LrfPathResolver(lrf_repository=repo).plan_for_keyword("BY-KEY") is None


def test_unknown_logical_record_does_not_fall_back_to_other_lr():
    repo = LrfRepository([_record("LR-ONE", "BY-KEY", "RECORD-ONE")])

    assert repo.path_for_keyword("BY-KEY", "LR-MISSING") is None
    assert LrfPathResolver(lrf_repository=repo).plan_for_keyword(
        "BY-KEY", "LR-MISSING"
    ) is None


def test_expander_uses_the_source_logical_record_not_first_matching_keyword():
    from converter.transformers.lrf_path_expander import LrfPathExpander

    repo = LrfRepository([
        _record("LR-ONE", "BY-KEY", "RECORD-ONE"),
        _record("LR-TWO", "BY-KEY", "RECORD-TWO"),
    ])
    expander = LrfPathExpander(path_resolver=LrfPathResolver(lrf_repository=repo))
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST LR-TWO WHERE BY-KEY.\n"
    )

    output = expander.expand(source)
    executable = "\n".join(
        line for line in output.splitlines()
        if not (len(line) >= 7 and line[6] in "*/D-")
    )
    assert "OBTAIN FIRST RECORD-TWO WITHIN SET-RECORD-TWO." in executable
    assert "RECORD-ONE" not in executable


def test_expander_refuses_keyword_when_source_lr_is_unresolved():
    from converter.transformers.lrf_path_expander import LrfPathExpander

    repo = LrfRepository([_record("LR-ONE", "BY-KEY", "RECORD-ONE")])
    expander = LrfPathExpander(path_resolver=LrfPathResolver(lrf_repository=repo))
    source = (
        "       PROCEDURE DIVISION.\n"
        "           OBTAIN FIRST LR-MISSING WHERE BY-KEY.\n"
    )

    output = expander.expand(source)
    assert "OBTAIN FIRST LR-MISSING WHERE BY-KEY." in output
    assert "*DB2-KEEP:" in output
    assert "OBTAIN FIRST RECORD-ONE" not in output
