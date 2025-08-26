"""Common utility functions for Project Euler problems."""

import math
from typing import Iterator


def factorial(n: int) -> int:
    """Calculate factorial of n."""
    return math.factorial(n)

def fibonacci(limit:int) -> Iterator[int]:
    """
    Generate Fibonacci numbers up to a specified limit.

    This generator yields numbers from the Fibonacci sequence starting with 1 and 2,
    continuing each subsequent number as the sum of the two preceding ones, until
    the generated number exceeds the given limit.

    Args:
        limit: The upper bound (inclusive) for the Fibonacci numbers to generate.
               The sequence stops when the next Fibonacci number would exceed this value.

    Yields:
        int: The next Fibonacci number in the sequence that is <= limit.

    Examples:
        >>> list(fibonacci(10))
        [1, 2, 3, 5, 8]
        >>> list(fibonacci(15))
        [1, 2, 3, 5, 8, 13]
    """
    a,b=1,2
    while a<=limit:
        yield a
        a,b=b,a+b