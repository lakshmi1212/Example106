# Example106 Math Operations

This repository provides basic math operations (addition and subtraction) with production-ready test automation and CI integration.

## Project Structure

```
src/
  math_operations.py
  __init__.py
tests/
  test_add.py
  test_subtract.py
  __init__.py
default/
  requirements.txt
  README.md
  math.json
```

## Usage

```
from src.math_operations import add, subtract
print(add(2, 3))        # Output: 5
print(subtract(5, 2))   # Output: 3
```

## Running Tests

Install dependencies:
```
pip install -r default/requirements.txt
```

Run all tests:
```
pytest tests/
```

## CI/CD Workflow

- The workflow file is located at `.github/workflows/ci.yml`
- Tests run automatically on pushes to the Feature1 branch and pull requests to main.
- Test results are output in both JUnit and HTML formats in the `reports/` directory.

## License

MIT
