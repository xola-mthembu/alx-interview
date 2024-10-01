#!/usr/bin/python3
"""
Module for Prime Game
"""


def is_prime(n):
    """Helper function to determine if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def sieve_of_eratosthenes(n):
    """Helper function to generate a list of prime numbers up to n."""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes


def isWinner(x, nums):
    """
    Determines the winner of the prime game after x rounds.
    Maria and Ben take turns removing primes and their multiples.
    """
    if x < 1 or not nums:
        return None

    # Initialize scores
    maria_score = 0
    ben_score = 0

    # For each round
    for n in nums:
        primes = sieve_of_eratosthenes(n)
        turn = 0  # Maria starts

        # Simulate game by removing primes and their multiples
        while primes:
            turn += 1
            # Remove the prime numbers and their multiples
            p = primes.pop(0)
            primes = [i for i in primes if i % p != 0]

        # If turn is odd, Maria made the last move, else Ben did
        if turn % 2 != 0:
            maria_score += 1
        else:
            ben_score += 1

    # Determine the overall winner
    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
