"""
Problem 9: Special Pythagorean Triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a* b *c.
"""


import math

def solve_01(target_sum) -> int:
    """
    The Euclidean Formula for Primitive Triplets is:
    a = m^2 - n^2
    b = 2mn
    c = m^2 + n^2

    We are solving for a + b + c = target_sum

    => m^2 - n^2 + 2mn + m^2 + n^2 = target_sum
    => 2*m^2 + 2mn = target_sum
    => m^2 + mn = target_sum / 2
    => m + n = target_sum / 2 / m
    => n = target_sum / 2 / m - m
    """
    
    if target_sum %2 != 0:
        return -1
    
    
    half_sum = target_sum // 2

    for m in range(1,int(math.sqrt(half_sum))+1):
        if half_sum % m !=0:
            continue

        n = half_sum // m  - m

        if m > n:
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2

            if a + b + c == target_sum:
                return a * b * c
            
    raise Exception("Not found")

def solve_02(target_sum):
    """
    Optimized approach: for each possible value of 'a',
    solve for 'b' using the quadratic formula.
    """
    triplets = []
    
    for a in range(1, target_sum // 3):
        # From a² + b² = c² and a + b + c = target_sum
        # We get: a² + b² = (target_sum - a - b)²
        # Solving: b = (target_sum² - 2*target_sum*a) / (2*(target_sum - a))
        
        numerator = target_sum * target_sum - 2 * target_sum * a
        denominator = 2 * (target_sum - a)
        
        if denominator != 0 and numerator % denominator == 0:
            b = numerator // denominator
            c = target_sum - a - b
            
            if b > a and c > 0 and a * a + b * b == c * c:
                triplets.append((a, b, c))