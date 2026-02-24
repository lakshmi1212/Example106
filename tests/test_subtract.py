import pytest
from src.math_operations import subtract

def test_subtract_positive_integers():
    assert subtract(5, 3) == 2

def test_subtract_negative_integers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_sign_integers():
    assert subtract(-2, 3) == -5
    assert subtract(3, -2) == 5

def test_subtract_zeros():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_floats():
    assert subtract(5.5, 2.1) == pytest.approx(3.4)
    assert subtract(-2.5, 2.5) == pytest.approx(-5.0)

def test_subtract_int_and_float():
    assert subtract(5, 2.5) == pytest.approx(2.5)
    assert subtract(2.5, 5) == pytest.approx(-2.5)

def test_subtract_invalid_types():
    with pytest.raises(TypeError):
        subtract('5', 3)
    with pytest.raises(TypeError):
        subtract(2, None)
    with pytest.raises(TypeError):
        subtract([1,2], 3)
