"""Tests for safe cursor relationship predicate generation."""

from __future__ import annotations


def test_parent_not_navigated_returns_no_predicates_and_reports_reason(
    relationship_policy,
):
    predicates = relationship_policy.where_conditions(
        record="VMBFAS",
        navigated_records=set(),
        lrf_cursors={},
    )

    assert predicates == []
    assert any(
        "never positions" in message
        for message in relationship_policy.messages
    )


def test_lrf_marker_does_not_add_duplicate_predicates(
    relationship_policy,
):
    predicates = relationship_policy.where_conditions(
        record="VMBFAS",
        navigated_records={"VMBSIAS"},
        lrf_cursors={"VMBFAS": object()},
    )

    assert predicates == [
        "KY_SIFORM = : DCLDZBSIASTV.KY-SIFORM",
    ]
    assert any(
        "no duplicate was added" in message
        for message in relationship_policy.messages
    )

def test_lrf_area_sweep_does_not_inherit_foreign_key_predicates(
    relationship_policy,
):
    """A root SWEEP must not be narrowed by unrelated mapped FK columns."""
    from types import SimpleNamespace

    predicates = relationship_policy.where_conditions(
        record="VMBFAS",
        navigated_records={"VMBSIAS"},
        lrf_cursors={
            "VMBFAS": SimpleNamespace(
                sweep_condition="SWEEP-VMBFAS",
                mode="FIRST",
            )
        },
    )

    assert predicates == []
    assert any(
        "relationship predicates were not applied" in message
        for message in relationship_policy.messages
    )


def test_lrf_relationship_path_keeps_relationship_predicates(
    relationship_policy,
):
    """An ALL/path child access must retain its parent-child predicate."""
    from types import SimpleNamespace

    predicates = relationship_policy.where_conditions(
        record="VMBFAS",
        navigated_records={"VMBSIAS"},
        lrf_cursors={
            "VMBFAS": SimpleNamespace(
                sweep_condition="ALL-VMBFAS-BY-VMBSIAS",
                mode="FIRST",
            )
        },
    )

    assert predicates == ["KY_SIFORM = : DCLDZBSIASTV.KY-SIFORM"]
