# Example106 Math Operations

## Overview
This repository provides basic math operation functions (addition and subtraction) with corresponding unit tests and CI integration.

## Project Structure

- `src/`: Source code for math operations
    - `math_operations.py`: Implements `add` and `subtract` functions
- `tests/`: Pytest-based test cases
    - `test_add.py`, `test_subtract.py`
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow metadata

## Usage

1. **Install dependencies:**
    ```bash
    pip install -r default/requirements.txt
    ```
2. **Run tests:**
    ```bash
    pytest tests/
    ```

## CI Workflow
- See `.github/workflows/ci.yml` (generated from `default/math.json`).
- Runs on pushes to `Feature1` and pull requests to `main`.
- Produces HTML and JUnit test reports in the `reports/` directory.

## Adding Functions
- Implement new math functions in `src/math_operations.py`.
- Add corresponding tests in `tests/`.

---
