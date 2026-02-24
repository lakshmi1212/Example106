# math_operations.py
"""
Provides basic math operations: add and subtract.
"""

def add(a, b):
    """
    Returns the sum of a and b.
    Raises TypeError if inputs are not int or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a + b

def subtract(a, b):
    """
    Returns the result of a minus b.
    Raises TypeError if inputs are not int or float.
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both arguments must be int or float.")
    return a - b
