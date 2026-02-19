# Example106: Math Operations

This repository provides simple Python functions for addition and subtraction, along with comprehensive pytest-based tests and a sample CI workflow configuration.

## Folder Structure

- `src/` : Source code for math operations
- `tests/` : Pytest test files for all functions
- `default/requirements.txt` : Python dependencies
- `default/README.md` : This file
- `default/math.json` : CI workflow metadata (for workflow generation)

## Usage

Install dependencies:

```bash
pip install -r default/requirements.txt
```

Run tests:

```bash
pytest tests/
```

## CI/CD Workflow

- Workflow file: `.github/workflows/ci.yml`
- Runs on: push to `Feature1`, PR to `main`
- Python version: 3.10
- Dependencies: pytest, pytest-html
- Test command: 

  ```bash
  python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
  ```

## Meta JSON

See `default/math.json` for all workflow and test metadata.
