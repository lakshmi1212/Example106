# Example106 - Math Operations

This repository demonstrates basic math operations (addition and subtraction) implemented in Python, with automated tests and CI workflow integration.

## Folder Structure

- `src/` - Source code for math operations
- `tests/` - Pytest-based unit tests
- `default/` - Metadata, requirements, and documentation

## Usage

1. Install dependencies:
   ```bash
   pip install -r default/requirements.txt
   ```
2. Run tests:
   ```bash
   pytest tests/
   ```

## CI/CD

A GitHub Actions workflow (see `.github/workflows/ci.yml`) runs all tests and generates reports on every push to the Feature1 branch and PRs to main.

## Requirements

- Python 3.10 or higher
- See `default/requirements.txt`

## Maintainers

- QA Automation & DevOps Integration Agent
