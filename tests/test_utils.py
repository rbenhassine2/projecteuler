"""Tests for utility functions."""

import pytest
from euler.utils.helpers import is_prime, factorial


class TestIsPrime:
    """Test cases for is_prime function."""

    def test_is_prime_small_numbers(self):
        """Test prime checking for small numbers."""
        assert is_prime(2) is True
        assert is_prime(3) is True
        assert is_prime(5) is True
        assert is_prime(7) is True
        assert is_prime(11) is True
        assert is_prime(13) is True

    def test_is_prime_non_primes(self):
        """Test non-prime numbers."""
        assert is_prime(0) is False
        assert is_prime(1) is False
        assert is_prime(4) is False
        assert is_prime(6) is False
        assert is_prime(8) is False
        assert is_prime(9) is False
        assert is_prime(10) is False

    def test_is_prime_negative_numbers(self):
        """Test negative numbers."""
        assert is_prime(-1) is False
        assert is_prime(-2) is False
        assert is_prime(-5) is False

    def test_is_prime_larger_numbers(self):
        """Test larger prime and non-prime numbers."""
        assert is_prime(17) is True
        assert is_prime(19) is True
        assert is_prime(23) is True
        assert is_prime(97) is True
        assert is_prime(100) is False
        assert is_prime(121) is False  # 11^2

    @pytest.mark.parametrize("number,expected", [
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (17, True),
        (25, False),
        (29, True),
        (49, False),
    ])
    def test_is_prime_parametrized(self, number, expected):
        """Parametrized test cases for is_prime."""
        assert is_prime(number) is expected


class TestFactorial:
    """Test cases for factorial function."""

    def test_factorial_small_numbers(self):
        """Test factorial for small numbers."""
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120

    def test_factorial_larger_numbers(self):
        """Test factorial for larger numbers."""
        assert factorial(6) == 720
        assert factorial(7) == 5040
        assert factorial(10) == 3628800

    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
    ])
    def test_factorial_parametrized(self, n, expected):
        """Parametrized test cases for factorial."""
        assert factorial(n) == expected

    def test_factorial_negative_raises_error(self):
        """Test that factorial raises error for negative numbers."""
        with pytest.raises(ValueError):
            factorial(-1)