"""
Problem 4: Largest Palindrome Product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009= 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def solve_01() -> int:
    result = 0
    for op1 in range(100,1000):
        for op2 in range(100,1000):
            product = op1*op2

            str_product = str(product)

            if product>result and str_product == str_product[::-1]:
                result = product
    return result


def solve_02() -> int:
    result = 0
    for op1 in range(999, 99, -1):
        if op1 * 999 <= result:
            break
        for op2 in range(op1, 99, -1):
            product = op1 * op2
            if product <= result:
                break
            
            str_product = str(product)
            if str_product == str_product[::-1]:
                result = product
    return result