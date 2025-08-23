"""Tests for Problem 2: Even Fibonacci Numbers."""

import pytest
from euler.problem_0002.solutions import solve_01


class TestProblem002:
    """Test cases for Problem 2 solution."""

    def test_solve_01_small_limit(self):
        """Test with small limit values."""
        assert solve_01(10) == 10  # Even Fibonacci numbers <= 10: [2, 8]
        assert solve_01(2) == 2   # Only 2
        assert solve_01(1) == 0   # No even numbers
        
    def test_solve_01_example_case(self):
        """Test with example case from problem description."""
        result = solve_01(89)
        expected = 44  # Even Fibonacci numbers <= 89: [2, 8, 34] = 44
        assert result == expected

    def test_solve_01_default_case(self):
        """Test the problem's target case (limit=4000000)."""
        result = solve_01(4000000)
        expected = 4613732  # Sum of even Fibonacci numbers <= 4000000
        assert result == expected

    def test_solve_01_edge_cases(self):
        """Test edge cases."""
        assert solve_01(0) == 0
        assert solve_01(3) == 2   # Only 2 is even and <= 3
        assert solve_01(8) == 10  # 2 + 8 = 10

    @pytest.mark.parametrize("limit,expected", [
        (0, 0),
        (1, 0),
        (2, 2),
        (3, 2),
        (8, 10),
        (10, 10),
        (34, 44),
        (89, 44),
    ])
    def test_solve_01_parametrized(self, limit, expected):
        """Parametrized test cases."""
        assert solve_01(limit) == expected