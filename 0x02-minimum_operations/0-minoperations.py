#!/usr/bin/python3
"""
Module to find the min number of operations to get n H characters in a file.
"""


def minOperations(n):
    """
    Finds the fewest operations needed to result in exactly n H characters.

    Args:
    n (int): The desired number of H characters.

    Returns:
    int: The minimum number of operations needed, or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
