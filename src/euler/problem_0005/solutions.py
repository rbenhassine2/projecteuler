"""
Problem 5: Smallest Multiple

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def solve_01(number) -> int:
    result = sum(range(number+1))
    if result%2!=0:
        result+=1
    while True:
        divisible = True
        for i in range(2,number+1):
            if result % i != 0:
                divisible = False
                break
        if divisible:
            return result
        result += 2

def solve_02(number) -> int:
    """Optimized solution using LCM (Least Common Multiple)"""
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return a * b // gcd(a, b)
    
    result = 1
    for i in range(1, number + 1):
        result = lcm(result, i)
    return result