import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(1, 2) == 3
    assert add(100, 200) == 300

def test_add_negative_numbers():
    assert add(-1, -2) == -3
    assert add(-100, -200) == -300

def test_add_mixed_sign_numbers():
    assert add(-1, 1) == 0
    assert add(100, -50) == 50

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_floats():
    assert add(1.5, 2.3) == pytest.approx(3.8)
    assert add(-1.5, 2.5) == pytest.approx(1.0)
