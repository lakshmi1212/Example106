# Math Operations Example

This repository demonstrates basic math operations (`add`, `subtract`) with production-ready tests and CI integration.

## Usage

```python
from src.math_operations import add, subtract

result1 = add(2, 3)        # 5
result2 = subtract(5, 2)   # 3
```

## Testing

Install dependencies:

```
pip install -r default/requirements.txt
```

Run all tests:

```
pytest tests/
```

## CI/CD Workflow

Automated tests run via GitHub Actions (see `.github/workflows/ci.yml`).

Test reports are generated in JUnit and HTML format in the `reports/` directory.
