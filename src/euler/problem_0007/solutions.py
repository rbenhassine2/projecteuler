"""
Problem 7: 10 001st Prime

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from euler.utils.primes import get_primes_by_idx

def solve_01(number) -> int:
    return get_primes_by_idx(number)

def solve_02(number) -> int:
    if number == 1:
        return 2
    
    primes = [2]
    candidate = 3
    
    while len(primes) < number:
        is_prime = True
        sqrt_candidate = int(candidate ** 0.5) + 1
        
        for prime in primes:
            if prime >= sqrt_candidate:
                break
            if candidate % prime == 0:
                is_prime = False
                break
        
        if is_prime:
            primes.append(candidate)
        
        candidate += 2
    
    return primes[-1]