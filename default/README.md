# Example106 Math Operations

This repository provides basic math operations (`add`, `subtract`) and their corresponding pytest test cases.

## Structure

- `src/math_operations.py`: Production code for math operations
- `tests/test_add.py`: Tests for addition
- `tests/test_subtract.py`: Tests for subtraction
- `default/requirements.txt`: Python dependencies
- `default/math.json`: CI workflow and metadata

## Usage

1. Install dependencies:

    ```bash
    pip install -r default/requirements.txt
    ```

2. Run tests:

    ```bash
    pytest tests/
    ```

## CI Workflow

A GitHub Actions workflow will run all tests on push to the `Feature1` branch.

Workflow file: `.github/workflows/ci.yml` (to be generated from `default/math.json`)

