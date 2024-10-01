#!/usr/bin/python3
"""
Prime Game - Maria and Ben take turns picking prime numbers
from a set and removing the prime and its multiples.
The player that cannot make a move loses.
"""


def is_prime(n):
    """ Helper function to check if a number is prime """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """ Helper function to find all primes up to n using sieve algorithm """
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    return [i for i, prime in enumerate(sieve) if prime]


def isWinner(x, nums):
    """
    Determines the winner of the game based on prime numbers.
    Args:
        x: the number of rounds
        nums: array of n for each round
    Returns:
        Name of the player that won the most rounds or None if a draw.
    """
    if not nums or x < 1:
        return None

    maria_wins = 0
    ben_wins = 0

    # Precompute primes up to the maximum value in nums
    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)

    for n in nums:
        # Count prime picks and multiples
        prime_count = sum(1 for prime in primes if prime <= n)

        # Maria wins if prime_count is odd, Ben wins if it's even
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    return None
