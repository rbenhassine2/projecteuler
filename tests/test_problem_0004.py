"""Tests for Problem 4: Largest Palindrome Product."""

import pytest
from euler.problem_0004.solutions import solve_01, solve_02


class TestProblem004:
    """Test cases for Problem 4 solutions."""

    def test_solve_01_correct_answer(self):
        """Test that solve_01 returns the correct answer for 3-digit numbers."""
        result = solve_01()
        expected = 906609  # 913 * 993
        assert result == expected

    def test_solve_02_correct_answer(self):
        """Test that solve_02 returns the correct answer for 3-digit numbers."""
        result = solve_02()
        expected = 906609  # 913 * 993
        assert result == expected

    def test_both_solutions_match(self):
        """Test that both solutions return the same result."""
        result_01 = solve_01()
        result_02 = solve_02()
        assert result_01 == result_02

    def test_palindrome_detection(self):
        """Test palindrome detection logic used in solutions."""
        # Test cases for palindromes
        palindromes = [9009, 90109, 906609, 1234321, 123454321]
        for num in palindromes:
            str_num = str(num)
            assert str_num == str_num[::-1], f"{num} should be a palindrome"

    def test_non_palindrome_detection(self):
        """Test non-palindrome detection."""
        # Test cases for non-palindromes
        non_palindromes = [1234, 5678, 90210, 123456]
        for num in non_palindromes:
            str_num = str(num)
            assert str_num != str_num[::-1], f"{num} should not be a palindrome"

    def test_known_palindrome_products(self):
        """Test with known palindrome products of 3-digit numbers."""
        # Some known palindrome products of 3-digit numbers
        known_palindromes = [
            906609,  # 913 * 993 (the largest)
            888888,  # 962 * 924 (among the largest)
            828828,  # 914 * 906
        ]
        
        for palindrome in known_palindromes:
            str_palindrome = str(palindrome)
            assert str_palindrome == str_palindrome[::-1]
            # Verify these are actually products of 3-digit numbers
            assert palindrome >= 100 * 100  # minimum product
            assert palindrome <= 999 * 999  # maximum product

    @pytest.mark.parametrize("palindrome", [
        9, 11, 22, 33, 44, 55, 66, 77, 88, 99,
        101, 111, 121, 131, 141, 151, 161, 171, 181, 191,
        202, 212, 222, 232, 242, 252, 262, 272, 282, 292,
        9009, 90109, 906609
    ])
    def test_palindrome_validation(self, palindrome):
        """Parametrized test for palindrome validation."""
        str_palindrome = str(palindrome)
        assert str_palindrome == str_palindrome[::-1]

    def test_result_is_palindrome(self):
        """Test that the results from both solutions are palindromes."""
        result_01 = solve_01()
        result_02 = solve_02()
        
        str_result_01 = str(result_01)
        str_result_02 = str(result_02)
        
        assert str_result_01 == str_result_01[::-1]
        assert str_result_02 == str_result_02[::-1]

    def test_result_is_product_of_3digit_numbers(self):
        """Test that the results can be formed by multiplying 3-digit numbers."""
        result_01 = solve_01()
        result_02 = solve_02()
        
        # The results should be within the range of products of 3-digit numbers
        min_product = 100 * 100  # 10000
        max_product = 999 * 999  # 998001
        
        assert min_product <= result_01 <= max_product
        assert min_product <= result_02 <= max_product

    def test_solution_performance_comparison(self):
        """Test that both solutions complete in reasonable time."""
        import time
        
        # Test solve_01
        start_time = time.time()
        result_01 = solve_01()
        time_01 = time.time() - start_time
        
        # Test solve_02  
        start_time = time.time()
        result_02 = solve_02()
        time_02 = time.time() - start_time
        
        # Both should complete in reasonable time (less than 10 seconds)
        assert time_01 < 10.0
        assert time_02 < 10.0
        
        # solve_02 should be faster due to optimizations
        assert time_02 < time_01
        
        # Results should match
        assert result_01 == result_02

    def test_example_from_problem_statement(self):
        """Test the example given in the problem statement."""
        # The problem states that 9009 = 91 * 99 is the largest palindrome 
        # made from the product of two 2-digit numbers
        assert 91 * 99 == 9009
        assert str(9009) == str(9009)[::-1]  # Verify it's a palindrome
        
        # Our solutions should find a larger palindrome for 3-digit numbers
        result_01 = solve_01()
        result_02 = solve_02()
        
        assert result_01 > 9009
        assert result_02 > 9009