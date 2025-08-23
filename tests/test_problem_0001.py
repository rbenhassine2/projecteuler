"""Tests for Problem 1: Multiples of 3 or 5."""

import pytest
from euler.problem_0001.solutions import solve_01


class TestProblem001:
    """Test cases for Problem 1 solution."""

    def test_solve_01_example_case(self):
        """Test the example case from the problem statement."""
        result = solve_01(10)
        expected = 23  # 3 + 5 + 6 + 9 = 23
        assert result == expected

    def test_solve_01_default_case(self):
        """Test the default case (limit=1000)."""
        result = solve_01()
        expected = 233168
        assert result == expected

    def test_solve_01_small_limits(self):
        """Test edge cases with small limits."""
        assert solve_01(0) == 0
        assert solve_01(1) == 0
        assert solve_01(3) == 0
        assert solve_01(4) == 3
        assert solve_01(6) == 8  # 3 + 5 = 8

    def test_solve_01_custom_limits(self):
        """Test with custom limit values."""
        assert solve_01(15) == 45  # 3,5,6,9,10,12 = 45
        assert solve_01(20) == 78  # adds 15,18 to previous = 45+33 = 78

    @pytest.mark.parametrize("limit,expected", [
        (0, 0),
        (3, 0),
        (5, 3),
        (10, 23),
        (15, 45),
    ])
    def test_solve_01_parametrized(self, limit, expected):
        """Parametrized test cases."""
        assert solve_01(limit) == expected