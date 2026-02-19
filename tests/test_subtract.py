import pytest
from src.math_operations import subtract

@pytest.mark.parametrize("a, b, expected", [
    (3, 2, 1),
    (1, 1, 0),
    (0, 0, 0),
    (2.5, 1.5, 1.0),
    (-3, -6, 3),
    (2000000, 1000000, 1000000),
    (1, -2, 3),
    (-5, 5, -10)
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 1)
    with pytest.raises(TypeError):
        subtract(1, None)
