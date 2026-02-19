# Example106: Math Operations

This repository contains simple math operations (addition and subtraction) with production-ready test cases and CI integration examples.

## Usage

### Math Operations

```
from src.math_operations import add, subtract

print(add(2, 3))        # 5
print(subtract(5, 2))   # 3
```

### Running Tests

Ensure you have dependencies installed:

```
pip install -r default/requirements.txt
```

Run all tests with:

```
pytest tests/
```

### CI/CD Workflow

This repository is configured for GitHub Actions CI. Workflow file: `.github/workflows/ci.yml`

- On push to `Feature1` or pull request to `main`, tests are executed and reports are generated in the `reports` directory.

## Structure

- `src/`: Source code for math operations
- `tests/`: Pytest test files
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow metadata

