# Project Euler Solutions

Python solutions for [Project Euler](https://projecteuler.net/) problems using Python 3.13 and uv.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv sync

# Run a specific problem
uv run python -m euler.problem_0001.main

# Run tests
uv run pytest
```

## Project Structure

- `src/euler/` - Main package directory
  - `problem_XXXX/` - Individual problem solutions (e.g., `problem_0001/`)
    - `main.py` - Entry point for the problem
    - `solutions.py` - Solution implementations
  - `utils/` - Common utility functions and helpers
- `tests/` - Test files for solutions
- `pyproject.toml` - Project configuration and dependencies

## Adding New Problems

1. Create `src/euler/problem_XXXX/` directory
2. Add `main.py` and `solutions.py` files following existing patterns
3. Add corresponding test in `tests/test_problem_XXXX.py`
4. Follow the existing template structure