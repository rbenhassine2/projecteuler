"""
Problem 6: Sum Square Difference

The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385.

The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def solve_01(number) -> int:
    return sum(range(number+1))**2 - sum(map(lambda x: x*x, range(number+1)))

def solve_02(number) -> int:
    sum_of_numbers = number * (number + 1) // 2
    square_of_sum = sum_of_numbers ** 2
    sum_of_squares = number * (number + 1) * (2 * number + 1) // 6
    return square_of_sum - sum_of_squares