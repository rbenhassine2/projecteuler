"""
Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

from euler.utils.helpers import get_primes, is_prime

def solve_01(number: int) -> int:
    if is_prime(number):
        # return number it is itself a prime
        return number
    
    limit = number // 2

    print("limit", limit)

    current_number = number

    for prime in get_primes(limit):
        while current_number % prime == 0:
            current_number = current_number // prime 
            print(current_number,prime)
            if current_number <= prime:
                return prime

    return -1