#!/usr/bin/python3
"""
Module for the makeChange function
"""


def makeChange(coins, total):
    """
    Determines the minimum number of coins needed to meet the total amount.

    Args:
        coins (list): The list of coin denominations.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed to meet total.
             Returns -1 if total cannot be met.
    """
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if total >= coin:
            count += total // coin
            total %= coin
        if total == 0:
            return count

    return -1
