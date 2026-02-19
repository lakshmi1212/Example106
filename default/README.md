# Example106 Math Operations

This repository provides basic math functions (addition, subtraction) with production-ready pytest tests and CI/CD integration.

## Usage

Import from `src.math_operations`:

```python
from src.math_operations import add, subtract

result_add = add(2, 3)
result_subtract = subtract(5, 2)
```

## Test Execution

Run all tests:

```bash
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI Workflow

See `.github/workflows/ci.yml` for automated test and reporting pipeline.

## Requirements

- Python 3.10+
- pytest==8.0.0
- pytest-html==4.1.1
