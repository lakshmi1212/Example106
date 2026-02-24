import pytest
from src.math_operations import add

@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, -1, -2),
    (-1, 1, 0),
    (1.5, 2.5, 4.0),
    (1e10, 1e10, 2e10),
    (-1e10, 1e10, 0),
    (123456, 654321, 777777),
])
def test_add(a, b, expected):
    assert add(a, b) == expected
