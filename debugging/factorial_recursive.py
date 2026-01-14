#!/usr/bin/python3
import sys

def factorial(n):
    """
    Function Description:
    This function computes the factorial of a given non-negative integer using
    a recursive approach. The factorial of a number n is the product of all
    positive integers less than or equal to n.

    Parameters:
    n (int): A non-negative integer whose factorial is to be calculated.

    Returns:
    int: The factorial of the given number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

f = factorial(int(sys.argv[1]))
print(f)