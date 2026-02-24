import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (0, 0, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (1.5, 2.5, -1.0),
    (1e10, 1e9, 9e9),
    (-1e10, 1e10, -2e10),
    (654321, 123456, 530865),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
