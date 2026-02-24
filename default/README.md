# Example106: Math Operations

## Overview
This repository provides basic math operations (addition, subtraction) and their corresponding tests using pytest. The project is CI-ready with workflow metadata in `math.json` for seamless integration.

## Structure
- `src/` — Source code for math operations
- `tests/` — Pytest test cases
- `default/requirements.txt` — Python dependencies
- `default/math.json` — CI workflow metadata

## Usage
```python
from src.math_operations import add, subtract

print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests
Install dependencies:
```bash
pip install -r default/requirements.txt
```
Run tests:
```bash
pytest tests/
```

## CI/CD
Workflow metadata is defined in `default/math.json` for GitHub Actions integration.
