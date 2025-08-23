"""Common utility functions for Project Euler problems."""

import math
from typing import Iterator, List


def is_prime(n: int) -> bool:
    """Check if a number is prime."""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    return math.factorial(n)