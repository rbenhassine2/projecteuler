"""
Problem 10: Summation of Primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


from euler.utils.primes import sieve_of_eratosthenes

def solve_01(limit) -> int:    
    return sum(sieve_of_eratosthenes(limit))