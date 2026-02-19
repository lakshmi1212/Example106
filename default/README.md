# Example106 Math Operations

## Overview
This project implements basic math operations (addition and subtraction) with production-ready pytest tests and CI/CD workflow integration.

## Usage

### Math Functions
- `add(a, b)`: Returns sum of two numbers.
- `subtract(a, b)`: Returns difference between two numbers.

### Running Tests
Install dependencies:
```
pip install -r default/requirements.txt
```
Run tests:
```
python -m pytest tests/ -v --tb=short --junitxml=reports/report.xml --html=reports/report.html --self-contained-html
```

## CI/CD Workflow
- Automated tests run on push to `Feature1` or pull request to `main`.
- Test reports are generated in `reports/`.
- Results are uploaded to S3 bucket.

## Structure
- `src/`: Business logic
- `tests/`: Test cases
- `default/`: Metadata, requirements, documentation
