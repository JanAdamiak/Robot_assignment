import pytest

from utils import validate_bounds


@pytest.mark.parametrize(
    "minimum, maximum, value, expected",
    [(1, 2, 2, True), (0, 0, 0, True), (0, 6, -1, False), (3, 4, 7, False)],
)
def test_validate_bounds(minimum, maximum, value, expected):
    assert validate_bounds(minimum, maximum, value) == expected
