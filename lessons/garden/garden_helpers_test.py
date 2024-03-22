"""Test my garden functions."""

__author__ = "730718367"

from lessons.garden.garden_helpers import add_by_kind, add_by_date, lookup_by_kind_and_date


def test_add_by_kind_use_case() -> None:
    """Test function add_by_kind with existing dict[str] value."""
    test_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    test_plant_kind: str = "flower"
    test_new_plant: str = "daisy"
    add_by_kind(test_by_kind, test_plant_kind, test_new_plant)
    assert test_by_kind == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}


def test_add_by_kind_edge_case() -> None:
    """Test function add_by_kind with empty dictionary."""
    test_by_kind: dict[str, list[str]] = {}
    test_plant_kind: str = "flower"
    test_new_plant: str = "daisy"
    add_by_kind(test_by_kind, test_plant_kind, test_new_plant)
    assert test_by_kind == {"flower": ["daisy"]}


def test_add_by_date_use_case() -> None:
    """Test function add_by_date with existing dict[str] value."""
    test_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    test_month: str = "April"
    test_plant: str = "daisy"
    add_by_date(test_by_date, test_month, test_plant)
    assert test_by_date == {"April": ["marigold", "daisy"], "June": ["carrots"]}


def test_add_by_date_edge_case() -> None:
    """Test function add_by_date with non-existing dict[str] value."""
    test_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    test_month: str = "January"
    test_plant: str = "blueberry"
    add_by_date(test_by_date, test_month, test_plant)
    assert test_by_date == {"April": ["marigold"], "June": ["carrots"], "January": ["blueberry"]}


def test_lookup_by_kind_and_date_use_case() -> None:
    """Test function lookup_by_kind_and_date with value that exist both in kind and month."""
    test_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    test_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    test_kind: str = "flower"
    test_month: str = "April"
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, test_kind, test_month) == "flowers to plant in April: ['marigold']"


def test_lookup_by_kind_and_date_edge_case() -> None:
    """Test function lookup_by_kind_and_date with value that do not exist in both kind and month."""
    test_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    test_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    test_kind: str = "flower"
    test_month: str = "June"
    assert lookup_by_kind_and_date(test_by_kind, test_by_date, test_kind, test_month) == "No flowers to plant in June."