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

def get_primes(limit:int)->Iterator[int]:
    assert limit >= 2
    yield 2
    n = 3
    while n<=limit:
        if is_prime(n):
            yield n
        n+=2

def get_primes_by_idx(idx:int)->int:
    assert idx > 0

    number = 2
    while True:
        if is_prime(number):
            idx -= 1
        if idx == 0:
            return number
        number+=1
      



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