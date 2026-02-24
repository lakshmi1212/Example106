# Example106: Math Operations

This repository provides basic math operations (addition and subtraction) and their tests.

## Folder Structure

- `src/` : Source code for math operations
- `tests/` : Pytest test cases for math operations
- `default/` : Project metadata and requirements

## Usage

```
from src.math_operations import add, subtract

print(add(2, 3))  # Output: 5
print(subtract(5, 2))  # Output: 3
```

## Running Tests

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow

Workflow file: `.github/workflows/ci.yml`

- Triggers on push to `Feature1` and pull request to `main`
- Runs all tests and generates reports
