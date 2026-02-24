import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 0),
    (0, 0, 0),
    (-1, -1, 0),
    (-1, 1, -2),
    (1.5, 2.5, -1.0),
    (1e10, 1, 1e10 - 1),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 1)
    with pytest.raises(TypeError):
        subtract(1, None)
