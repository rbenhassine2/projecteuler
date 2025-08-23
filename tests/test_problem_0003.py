"""Tests for Problem 3: Largest Prime Factor."""

import pytest
from euler.problem_0003.solutions import solve_01


class TestProblem003:
    """Test cases for Problem 3 solution."""

    def test_solve_01_example_case(self):
        """Test the example case from the problem statement."""
        result = solve_01(13195)
        expected = 29  # Largest prime factor of 13195
        assert result == expected

    def test_solve_01_prime_number(self):
        """Test when the input is already a prime number."""
        assert solve_01(7) == 7
        assert solve_01(13) == 13
        assert solve_01(29) == 29

    def test_solve_01_small_composite_numbers(self):
        """Test with small composite numbers."""
        assert solve_01(4) == 2  # 2 * 2
        assert solve_01(6) == 3  # 2 * 3
        assert solve_01(9) == 3  # 3 * 3
        assert solve_01(10) == 5  # 2 * 5
        assert solve_01(12) == 3  # 2^2 * 3
        assert solve_01(15) == 5  # 3 * 5

    def test_solve_01_powers_of_prime(self):
        """Test with powers of prime numbers."""
        assert solve_01(8) == 2  # 2^3
        assert solve_01(16) == 2  # 2^4
        assert solve_01(25) == 5  # 5^2
        assert solve_01(27) == 3  # 3^3

    def test_solve_01_products_of_two_primes(self):
        """Test with products of exactly two prime numbers."""
        assert solve_01(14) == 7  # 2 * 7
        assert solve_01(21) == 7  # 3 * 7
        assert solve_01(35) == 7  # 5 * 7
        assert solve_01(77) == 11  # 7 * 11

    def test_solve_01_larger_numbers(self):
        """Test with larger composite numbers."""
        assert solve_01(100) == 5  # 2^2 * 5^2
        assert solve_01(210) == 7  # 2 * 3 * 5 * 7
        assert solve_01(1001) == 13  # 7 * 11 * 13

    @pytest.mark.parametrize("number,expected", [
        (4, 2),
        (6, 3),
        (9, 3),
        (10, 5),
        (15, 5),
        (21, 7),
        (35, 7),
        (49, 7),
        (77, 11),
        (143, 13),
    ])
    def test_solve_01_parametrized(self, number, expected):
        """Parametrized test cases for various composite numbers."""
        assert solve_01(number) == expected

    def test_solve_01_edge_cases(self):
        """Test edge cases."""
        # Test with 2 (smallest prime)
        assert solve_01(2) == 2
        
        # Test with 3 (another small prime)
        assert solve_01(3) == 3