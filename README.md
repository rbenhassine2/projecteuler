# Project Euler Solutions

Python solutions for [Project Euler](https://projecteuler.net/) problems using Python 3.13 and uv.

## Progress

Currently solved problems:
- [Problem 1](https://projecteuler.net/problem=1): Multiples of 3 or 5
- [Problem 2](https://projecteuler.net/problem=2): Even Fibonacci numbers
- [Problem 3](https://projecteuler.net/problem=3): Largest prime factor
- [Problem 4](https://projecteuler.net/problem=4): Largest palindrome product
- [Problem 5](https://projecteuler.net/problem=5): Smallest multiple

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management.

```bash
# Install dependencies
uv sync

# Run a specific problem
uv run python -m euler.problem_0001
# or alternatively:
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

1. Create `src/euler/problem_XXXX/` package
2. Add `main.py` and `solutions.py` and `__main__.py` files following existing patterns
3. Add corresponding test in `tests/test_problem_XXXX.py`, when doable.
4. Follow the existing template structure