#!/usr/bin/python3
import sys

def factorial(n):
    """
    Compute the factorial of a given number using recursion.

    Parameters:
        n (int): A non-negative integer for which the factorial is computed.

    Returns:
        int: The factorial value of the input number n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
