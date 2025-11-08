# Coding Interview Practice Framework

A professional testing framework for coding interview preparation.

## Setup

```bash
# Create virtual environment (recommended)
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```

**Note:** Always activate the virtual environment before running tests!

## Project Structure

```
CodingPractice/
├── solutions/          # Your solution implementations
├── tests/             # Test files
├── pytest.ini         # Pytest configuration
└── requirements.txt   # Dependencies
```

## Running Tests

**Make sure to activate the virtual environment first:**
```bash
source venv/bin/activate  # On macOS/Linux
```

Then run your tests:

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_backtracking.py

# Run tests by marker (difficulty)
pytest -m easy
pytest -m medium
pytest -m hard

# Run tests by topic
pytest -m array
pytest -m string
pytest -m tree

# Run with coverage
pytest --cov=solutions --cov-report=html

# Watch mode (auto-run on file changes)
ptw
```

## Writing Tests

1. Create your solution in `solutions/` directory
2. Create corresponding test in `tests/` directory
3. Use pytest markers to tag difficulty and topic

Example:
```python
import pytest

@pytest.mark.easy
@pytest.mark.array
def test_two_sum():
    from solutions.two_sum import two_sum
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
```

## Code Quality

```bash
# Format code
black solutions/ tests/

# Lint code
flake8 solutions/ tests/

# Type checking
mypy solutions/
```

