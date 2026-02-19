# Example106: Math Operations

This repository implements basic math operations (addition & subtraction) and provides comprehensive test coverage with pytest, CI metadata, and requirements for seamless integration.

## Source Structure
- `src/math_operations.py`: Core logic for add & subtract
- `tests/`: Pytest test cases for all math functions
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow metadata

## Usage
```python
from src.math_operations import add, subtract
print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

## Running Tests
Ensure dependencies from requirements.txt are installed, then run:
```
pytest tests/
```

## CI/CD
All workflow metadata is provided in `default/math.json`. This file is consumed to generate the required `.github/workflows/ci.yml` for automated testing and reporting.
